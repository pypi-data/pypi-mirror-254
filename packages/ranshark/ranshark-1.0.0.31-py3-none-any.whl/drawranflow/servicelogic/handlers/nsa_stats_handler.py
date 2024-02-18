from drawranflow.models import Identifiers, IdentifiersStats, Stats, Message, UploadedFile
import logging
from django.utils import timezone
from django.db import transaction, models
from django.db.models import Sum, F, Q, ExpressionWrapper


class computeStats:
    def __init__(self):
        pass

    @classmethod
    def packet_to_json(cls, packet):
        # Extract IP layer if it exists
        new_dict = {}
        for key in packet:
            # split the key by the first dot and get the top-level key and the second-level key suffix
            if key != "" and "per" not in key:
                if "." in key:
                    top_level_key, suffix = key.split(".", 1)
                else:
                    top_level_key = key
                    suffix = ""

                # create a new dictionary with the top-level key if it doesn't exist
                if top_level_key not in new_dict:
                    new_dict[top_level_key] = {}

                    # add the second-level key suffix and its value to the new dictionary
                new_dict[top_level_key][suffix] = packet[key]
                # convert the output dictionary to a pretty-printed JSON string
        return new_dict

    @classmethod
    def packetLayers(cls, packet):
        print(packet)
        f1ap = packet.f1ap._all_fields if 'F1AP' in packet else {}
        e1ap = packet.e1ap._all_fields if 'E1AP' in packet else {}
        ngap = packet.ngap._all_fields if 'NGAP' in packet else {}
        xnap = packet.xnap._all_fields if 'XNAP' in packet else {}
        ipadd = packet.ip._all_fields if 'IP' in packet else {}
        s1ap = packet.s1ap._all_fields if 'S1AP' in packet else {}
        mvlterrc = packet.MAVLTERRC._all_fields if 'MAVLTERRC' in packet else {}
        x2ap = packet.x2ap._all_fields if 'X2AP' in packet else {}


        filtered_ipdata = {key: value for key, value in ipadd.items() if key in ["ip.src", "ip.dst"]}
        del packet
        return {**filtered_ipdata, **f1ap, **ngap, **e1ap, **xnap, **s1ap, **mvlterrc, **x2ap}

    @classmethod
    def rrc_related_message_stats(cls, identifier):
        logging.debug("rrc_related_message_stats - Started.")
        time_window = timezone.timedelta(seconds=1)
        try:
            rrc_setup_messages = Message.objects.filter(
                identifiers_id=identifier.id,
                message='RRC Setup',
                gnb_id=identifier.gnb_id
            )
            logging.debug(f"rrc_setup_messages: {rrc_setup_messages}")

            if rrc_setup_messages:
                for rrc_setup in rrc_setup_messages:
                    related_messages = Message.objects.filter(
                        identifiers_id=identifier.id,
                        frame_time__gte=rrc_setup.frame_time,
                        frame_time__lte=rrc_setup.frame_time + time_window
                    )
                    has_service_request = related_messages.filter(message='Service request',
                                                                  protocol__icontains='f1ap').exists()
                    has_rrc_complete_request = related_messages.filter(message='RRC Setup Complete',
                                                                       protocol__icontains='f1ap').exists()
                    has_registration_request = related_messages.filter(message='Registration request',
                                                                       protocol__icontains='f1ap').exists()
                    has_tracking_request = related_messages.filter(message='Tracking area update request',
                                                                   protocol__icontains='f1ap').exists()

                    logging.debug(
                        f"has_service_request: {has_service_request} {has_rrc_complete_request} {has_registration_request}"
                        f" {has_tracking_request}")

                    identifiers_stats, created = IdentifiersStats.objects.get_or_create(
                        identifier_id=identifier.id,
                        uploadedFiles_id=identifier.uploaded_file_id,
                        gnb_id=identifier.gnb_id,
                        defaults={
                            'category': 'RRC'
                        },
                        cucp_f1c_ip=identifier.cucp_f1c_ip,
                    )
                    logging.debug(f"identifiers_stats {identifiers_stats}")

                    if created or (identifiers_stats is not None and identifiers_stats.attempts == 0):
                        identifiers_stats.attempts += 1
                        if has_service_request or has_registration_request or \
                                has_tracking_request or has_rrc_complete_request:
                            identifiers_stats.success += 1
                        if related_messages.filter(message='RRC Reject', protocol__icontains='f1ap').exists():
                            identifiers_stats.fails += 1
                        if not has_service_request and not has_registration_request \
                                and not has_tracking_request and not has_rrc_complete_request:
                            identifiers_stats.timeouts += 1

                        try:

                            identifiers_stats.save()
                            logging.debug("rrc_related_message_stats - Completed.")

                        except Exception as e:
                            logging.error(f"Error saving IdentifiersStats: {e} identifier - {identifier.id}")

        except Exception as e:
            logging.error(f"Error in processing rrc stats Exception, {e}")

    @classmethod
    def initial_related_messages_stats(cls, identifier):
        logging.debug("initial_related_messages_stats - Started.")

        # Get counts in a single database query
        counts = Message.objects.filter(
            identifiers_id=identifier.id,
            message__in=['InitialContextSetupRequest', 'InitialContextSetupResponse', 'InitialContextSetupFailure']
        ).values('message').annotate(count=models.Count('id'))

        ctxt, ctxt_created = IdentifiersStats.objects.get_or_create(
            category='InitialCtxt',
            identifier_id=identifier.id,
            uploadedFiles_id=identifier.uploaded_file_id,
            gnb_id=identifier.gnb_id,
            cucp_f1c_ip=identifier.cucp_f1c_ip,
        )

        if ctxt_created or (ctxt is not None and ctxt.attempts == 0):

            ctxt.attempts += next((item['count'] for item in counts if item['message'] == 'InitialContextSetupRequest'),
                                  0)
            ctxt.success += next((item['count'] for item in counts if item['message'] == 'InitialContextSetupResponse'),
                                 0)
            ctxt.fails += next((item['count'] for item in counts if item['message'] == 'InitialContextSetupFailure'), 0)

            if ctxt.attempts > 0 and ctxt.fails == 0 and ctxt.success == 0:
                ctxt.timeouts += 1

            ctxt.save()
            logging.debug("initial_related_messages_stats - Completed.")

    @classmethod
    def bearerctxt_related_messages_stats(cls, identifier):

        logging.debug("bearerctxt_related_messages_stats - Started.")

        # Get counts in a single database query
        counts = Message.objects.filter(
            identifiers_id=identifier.id,
            message__in=['BearerContextSetupRequest', 'BearerContextSetupResponse', 'BearerContextSetupFailure']
        ).values('message').annotate(count=models.Count('id'))

        ctxt, ctxt_created = IdentifiersStats.objects.get_or_create(
            category='Bctxt',
            identifier_id=identifier.id,
            uploadedFiles_id=identifier.uploaded_file_id,
            gnb_id=identifier.gnb_id,
            cucp_f1c_ip=identifier.cucp_f1c_ip
        )

        if ctxt_created or (ctxt is not None and ctxt.attempts == 0):
            # print("bearerctxt_related_messages_stats - Adding counts:")
            # print("bearerctxt_related_messages_stats - Before update - ctxt:", ctxt)
            # print("bearerctxt_related_messages_stats - Before update - attempts:", ctxt.attempts)
            # print("bearerctxt_related_messages_stats - Before update - success:", ctxt.success)
            # print("bearerctxt_related_messages_stats - Before update - fails:", ctxt.fails)
            # print("bearerctxt_related_messages_stats - Before update - timeouts:", ctxt.timeouts)

            ctxt.attempts += next((item['count'] for item in counts if item['message'] == 'BearerContextSetupRequest'),
                                  0)
            ctxt.success += next((item['count'] for item in counts if item['message'] == 'BearerContextSetupResponse'),
                                 0)
            ctxt.fails += next((item['count'] for item in counts if item['message'] == 'BearerContextSetupFailure'), 0)

            if ctxt.attempts > 0 and ctxt.fails == 0 and ctxt.success == 0:
                ctxt.timeouts += 1

            # print("bearerctxt_related_messages_stats - After update - ctxt:", ctxt)
            # print("bearerctxt_related_messages_stats - After update - attempts:", ctxt.attempts)
            # print("bearerctxt_related_messages_stats - After update - success:", ctxt.success)
            # print("bearerctxt_related_messages_stats - After update - fails:", ctxt.fails)
            # print("bearerctxt_related_messages_stats - After update - timeouts:", ctxt.timeouts)

            ctxt.save()

            logging.debug("bearerctxt_related_messages_stats - Completed.")

    @classmethod
    def pdu_setup_related_messages_stats(cls, identifier):

        logging.debug("pdu_setup_related_messages_stats - Started.")

        # Get counts in a single database query
        counts = Message.objects.filter(
            identifiers_id=identifier.id,
            message__in=['PDUSessionResourceSetupRequest', 'PDUSessionResourceSetupResponse',
                         'PDUSessionResourceSetupFailure', 'PDUSessionResourceModifyRequest',
                         'PDUSessionResourceModifyResponse']).values('message').annotate(count=models.Count('id'))

        pdu, pdu_created = IdentifiersStats.objects.get_or_create(
            category='PDU_Setup',
            identifier_id=identifier.id,
            uploadedFiles_id=identifier.uploaded_file_id,
            gnb_id=identifier.gnb_id,
            cucp_f1c_ip=identifier.cucp_f1c_ip
        )

        if pdu_created or (pdu is not None and pdu.attempts == 0):
            # print("bearerctxt_related_messages_stats - Adding counts:")
            # print("bearerctxt_related_messages_stats - Before update - ctxt:", ctxt)
            # print("bearerctxt_related_messages_stats - Before update - attempts:", ctxt.attempts)
            # print("bearerctxt_related_messages_stats - Before update - success:", ctxt.success)
            # print("bearerctxt_related_messages_stats - Before update - fails:", ctxt.fails)
            # print("bearerctxt_related_messages_stats - Before update - timeouts:", ctxt.timeouts)

            pdu.attempts += next((item['count'] for item in counts if
                                  item['message'] == 'PDUSessionResourceSetupRequest' or item[
                                      'message'] == 'PDUSessionResourceModifyRequest'),
                                 0)
            pdu.success += next((item['count'] for item in counts if
                                 item['message'] == 'PDUSessionResourceSetupResponse' or item[
                                     'message'] == 'PDUSessionResourceModifyResponse'),
                                0)
            pdu.fails += next((item['count'] for item in counts if
                               item['message'] == 'PDUSessionResourceSetupFailure' or item[
                                   'message'] == 'PDUSessionResourceModifyFailure'), 0)

            if pdu.attempts > 0 and pdu.fails == 0 and pdu.success == 0:
                pdu.timeouts += 1

            # print("bearerctxt_related_messages_stats - After update - ctxt:", ctxt)
            # print("bearerctxt_related_messages_stats - After update - attempts:", ctxt.attempts)
            # print("bearerctxt_related_messages_stats - After update - success:", ctxt.success)
            # print("bearerctxt_related_messages_stats - After update - fails:", ctxt.fails)
            # print("bearerctxt_related_messages_stats - After update - timeouts:", ctxt.timeouts)

            pdu.save()

            logging.debug("pdu_setup_related_messages_stats - Completed.")

    @classmethod
    def check_is_analysis_complete(cls, file_id):
        identifiers_count = Message.objects.filter(
            Q(identifiers__uploaded_file_id=file_id) &
            (Q(message='RRC Setup'))
        ).count()

        processed_identifiers_count = IdentifiersStats.objects.filter(
            uploadedFiles_id=file_id,
            category='RRC',
            attempts__gt=0,
        ).count()

        if identifiers_count == processed_identifiers_count:
            UploadedFile.objects.filter(id=file_id).update(isAnalysisComplete=True)
            UploadedFile.objects.filter(id=file_id).update(processing_status="Completed")


    @classmethod
    def update_stats_by_id(cls, file_id):
        upload_file = UploadedFile.objects.get(id=file_id)
        unique_ips = Identifiers.objects.filter(uploaded_file_id=file_id).values('cucp_f1c_ip', 'gnb_id').distinct()

        if not upload_file.isAnalysisComplete and not upload_file.processing_status == "In-Progress":
            upload_file.processing_status = "In-Progress"
            upload_file.save()
            logging.error("Stats computation started...")
            with transaction.atomic():
                for unique_ip in unique_ips:
                    cucp_f1c_ip = unique_ip['cucp_f1c_ip']
                    gnb_id = unique_ip['gnb_id']
                    # Use select_related to fetch related data in a single query
                    identifiers = Identifiers.objects.filter(uploaded_file_id=file_id, gnb_id=gnb_id,
                                                             cucp_f1c_ip=cucp_f1c_ip)
                    logging.debug(f"Stats computation started...{identifiers}")

                    for identifier in identifiers:
                        cls.rrc_related_message_stats(identifier)
                        cls.initial_related_messages_stats(identifier)
                        cls.bearerctxt_related_messages_stats(identifier)

                    cls.update_cumulative_stats(file_id, 'RRC', cucp_f1c_ip, gnb_id)
                    cls.update_cumulative_stats(file_id, 'InitialCtxt', cucp_f1c_ip, gnb_id)
                    cls.update_cumulative_stats(file_id, 'Bctxt', cucp_f1c_ip, gnb_id)
                    cls.check_is_analysis_complete(file_id)
            logging.error("computation Completed...")

    @classmethod
    def get_gnb_ids(cls, file_id):
        unique_gnb_ids_with_ips = Identifiers.objects.filter(
            uploaded_file_id=file_id,
            gnb_id__isnull=False,
        ).exclude(gnb_id="").values('gnb_id', 'cucp_f1c_ip').order_by('gnb_id').distinct()
        formatted_results = [f"{pair['gnb_id']}({pair['cucp_f1c_ip']})" for pair in unique_gnb_ids_with_ips]

        return formatted_results

    @classmethod
    def update_cumulative_stats(cls, upload_file_id, category, cucp_f1c_ip, gnb_id):
        identifier_stats_summary = IdentifiersStats.objects.filter(
            uploadedFiles_id=upload_file_id, category=category, gnb_id=gnb_id, cucp_f1c_ip=cucp_f1c_ip
        ).aggregate(
            attempts_count=Sum('attempts'),
            success_count=Sum('success'),
            fails_count=Sum('fails'),
            timeouts_count=Sum('timeouts')
        )
        cumulative_stats, created = Stats.objects.get_or_create(category=category, uploadedFiles_id=upload_file_id,
                                                                gnb_id=gnb_id, cucp_f1c_ip=cucp_f1c_ip)

        if identifier_stats_summary:
            cumulative_stats.attempts = identifier_stats_summary['attempts_count'] or 0
            cumulative_stats.success = identifier_stats_summary['success_count'] or 0
            cumulative_stats.fails = identifier_stats_summary['fails_count'] or 0
            cumulative_stats.timeouts = identifier_stats_summary['timeouts_count'] or 0

        cumulative_stats.save()
