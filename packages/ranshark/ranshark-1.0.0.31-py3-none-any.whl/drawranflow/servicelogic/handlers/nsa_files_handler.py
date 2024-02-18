from drawranflow.models import UploadedFile, IdentifiersNsa, MessageNsa
import pyshark
import os
from django.conf import settings
import logging
import pandas as pd
import numpy as np
from drawranflow.servicelogic.handlers.utils_sa import get_interface_from_protocol, get_direction


class FileHandlers:
    MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', None)

    @classmethod
    def upload_pcap_file(cls, file, network):
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)

        # Try to get an existing UploadedFile record with the same filename
        try:
            upload_table = UploadedFile.objects.get(filename=file.name)

            # If it exists, delete associated records and the UploadedFile record
            IdentifiersNsa.objects.filter(uploaded_file__id=upload_table.id).delete()
            MessageNsa.objects.filter(
                identifiers__id__in=IdentifiersNsa.objects.filter(uploaded_file__id=upload_table.id).values(
                    'id')).delete()
            upload_table.delete()

            # Remove the file from the file system
            if os.path.exists(file_path):
                cls.delete_files(file_path)
        except UploadedFile.DoesNotExist:
            pass

        # Save the new file
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Create or update the UploadedFile record
        uploaded_file_record, created = UploadedFile.objects.get_or_create(filename=file.name, processed=False,
                                                                           network=network)
        uploaded_file_record.save()

        if uploaded_file_record:
            messages = {
                'message_type': 'success',
                'message_text': 'File uploaded successfully',
            }
        else:
            messages = {
                'message_type': 'error',
                'message_text': 'File upload failed',
            }

        return messages

    @classmethod
    def delete_files(cls, file_path):
        # Remove the main file
        os.remove(file_path)
        file_prefix = os.path.basename(file_path).split('.')[0]

        # Find and delete associated files with the same prefix
        for file_name in os.listdir(settings.MEDIA_ROOT):
            if file_name.startswith(file_prefix):
                file_to_delete = os.path.join(settings.MEDIA_ROOT, file_name)
                logging.debug(f"Deleting file: {file_to_delete}")
                os.remove(file_to_delete)

    @classmethod
    def construct_pcap_filter(cls, identifier_data):
        filter_conditions = []
        if identifier_data.c_rnti != 'nan' and identifier_data.pci != 'nan' and identifier_data.c_rnti != '00000':
            filter_conditions.append(f"(mavlterrc.rnti=={identifier_data.c_rnti} && "
                                     f"mavlterrc.cellid=={identifier_data.pci})")

        if identifier_data.enb_ue_s1ap_id != 'nan' and identifier_data.mme_ue_s1ap_id != 'nan':
            filter_conditions.append(f"(s1ap.ENB_UE_S1AP_ID=={identifier_data.enb_ue_s1ap_id}) ||"
                                     f" (s1ap.ENB_UE_S1AP_ID=={identifier_data.enb_ue_s1ap_id} &&"
                                     f" s1ap.MME_UE_S1AP_ID=={identifier_data.mme_ue_s1ap_id})")

        if identifier_data.enb_ue_s1ap_id != 'nan' and identifier_data.mme_ue_s1ap_id == 'nan':
            filter_conditions.append(f"(s1ap.ENB_UE_S1AP_ID=={identifier_data.enb_ue_s1ap_id})")

        if identifier_data.x2ap_ue_ran_id != 'nan' and identifier_data.x2ap_5g_ran_id != 'nan':
            filter_conditions.append(f"(x2ap.UE_X2AP_ID=={identifier_data.x2ap_ue_ran_id}) ||"
                                     f" (x2ap.UE_X2AP_ID=={identifier_data.x2ap_ue_ran_id} &&"
                                     f" x2ap.SgNB_UE_X2AP_ID=={identifier_data.x2ap_5g_ran_id})")

        if identifier_data.x2ap_ue_ran_id != 'nan' and identifier_data.x2ap_5g_ran_id == 'nan':
            filter_conditions.append(f"(ex2ap.UE_X2AP_ID=={identifier_data.x2ap_ue_ran_id})")

        filter_string = " or ".join(filter_conditions)
        logging.debug(f'Filter string - {filter_string}')
        # Log or use the generated filter_string as needed

        return filter_string

    @classmethod
    def fetch_identifier_data(cls, row_id):
        logging.debug(f'identifier_data in fetch_identifier_data: {row_id}')
        identifier_data = IdentifiersNsa.objects.get(id=row_id)

        return identifier_data

    @classmethod
    def filter_pcap(cls, input_file, filter_string, output_file):
        capture = pyshark.FileCapture(input_file, display_filter=f"{filter_string}", output_file=f'{output_file}')
        capture.set_debug()
        filtered_packets = [packet for packet in capture]
        logging.debug(f'filtered_packets,{filtered_packets} - output: {output_file}, filterString:{filter_string}')

        return output_file

    @classmethod
    def update_messages_with_identifier_key(cls, df, item_id):
        global identifier_data
        try:
            upload_table = UploadedFile.objects.get(id=item_id)
            logging.error(f"Started filtering messages for each call flow : {upload_table.filename}")

            # The columns to check for undesired values
            columns_to_check = [
                'mavlterrc.rnti',
                'mavlterrc.cellid',
                's1ap.ENB_UE_S1AP_ID',
                's1ap.MME_UE_S1AP_ID',
                'e212.imsi',
                's1ap.CellIdentity',
                'x2ap.eUTRANcellIdentifier',
                'x2ap.UE_X2AP_ID',
                'x2ap.SgNB_UE_X2AP_ID',
                's1ap.pLMN_Identity',
                'x2ap.gTP_TEID',
                's1ap.gTP_TEID',
            ]

            # Specify undesired values
            undesired_values = ["none", "nan", "", None, "NaN", np.nan]

            # Create a mask to filter out rows with undesired values in the specified columns
            mask = df[columns_to_check].apply(
                lambda col: ~col.astype(str).str.lower().isin(undesired_values)
            )

            # Apply the mask to filter the DataFrame
            filtered_df = df[mask.any(axis=1)]

            identifiers = IdentifiersNsa.objects.filter(uploaded_file_id=item_id)
            messages_to_insert = []
            for identifier_data in identifiers:
                two_sec = pd.Timedelta(minutes=10)
                logging.debug(f"Identifier data: {identifier_data.c_rnti}, id: {identifier_data.id}")

                # Reset filter_conditions for each identifier_data
                filter_conditions = pd.Series(False, index=filtered_df.index)
                if identifier_data.c_rnti != 'nan' and identifier_data.pci != 'nan' and identifier_data.c_rnti != '00000':
                    filter_conditions |= ((filtered_df['mavlterrc.rnti'] == identifier_data.c_rnti)
                                          & (filtered_df['mavlterrc.cellid'] == identifier_data.pci)
                                          & (filtered_df['frame.time'] <= identifier_data.frame_time + two_sec))

                if identifier_data.enb_ue_s1ap_id != 'nan' and identifier_data.mme_ue_s1ap_id != 'nan':
                    filter_conditions |= (((filtered_df['s1ap.ENB_UE_S1AP_ID'] == identifier_data.enb_ue_s1ap_id) &
                                           (filtered_df['frame.time'] > identifier_data.frame_time)) |
                                          ((filtered_df['s1ap.ENB_UE_S1AP_ID'] == identifier_data.enb_ue_s1ap_id) &
                                           (filtered_df['s1ap.MME_UE_S1AP_ID'] == identifier_data.mme_ue_s1ap_id)) &
                                          (filtered_df['frame.time'] > identifier_data.frame_time))

                if identifier_data.enb_ue_s1ap_id != 'nan' and identifier_data.mme_ue_s1ap_id == 'nan':
                    filter_conditions |= (filtered_df[
                                              's1ap.ENB_UE_S1AP_ID'] == identifier_data.enb_ue_s1ap_id) \
                                         & (filtered_df['s1ap.MME_UE_S1AP_ID'].isna() & (
                            filtered_df['frame.time'] > identifier_data.frame_time))

                if identifier_data.x2ap_ue_ran_id != 'nan' and identifier_data.x2ap_5g_ran_id != 'nan':
                    filter_conditions |= (((filtered_df['x2ap.UE_X2AP_ID'] == identifier_data.x2ap_ue_ran_id) &
                                           (filtered_df['frame.time'] > identifier_data.frame_time)) |
                                          ((filtered_df['x2ap.UE_X2AP_ID'] == identifier_data.x2ap_ue_ran_id) &
                                           (filtered_df['x2ap.SgNB_UE_X2AP_ID'] == identifier_data.x2ap_5g_ran_id)) &
                                          (filtered_df['frame.time'] > identifier_data.frame_time))

                if identifier_data.x2ap_ue_ran_id != 'nan' and identifier_data.x2ap_5g_ran_id == 'nan':
                    filter_conditions |= (filtered_df[
                                              'ex2ap.UE_X2AP_ID'] == identifier_data.x2ap_ue_ran_id) \
                                         & (filtered_df['x2ap.SgNB_UE_X2AP_ID'].isna() & (
                            filtered_df['frame.time'] > identifier_data.frame_time))

                updated_messages = filtered_df[filter_conditions]
                condition = ((updated_messages['_ws.col.info'] == 'UEContextReleaseComplete') &
                             updated_messages['frame.protocols'].str.contains('s1ap'))

                if condition.any():  # If the condition is met at least once
                    first_occurrence = condition.idxmax()

                    updated_messages = updated_messages.loc[:first_occurrence + 4].copy()

                updated_messages_copy = updated_messages.copy()
                # Modify the copied DataFrame
                updated_messages_copy.loc[:, 'identifiers_id'] = identifier_data.id

                gnb_id_value = str(identifier_data.gnb_id)

                updated_messages_copy.loc[:, 'gnb_id'] = gnb_id_value

                updated_messages = updated_messages_copy
                logging.debug(f"updated_messages: {updated_messages}")

                # Create instances of the 'Message' model

                for index, row in updated_messages.iterrows():
                    interface = get_interface_from_protocol(row['frame.protocols'])
                    srcNode, dstNode = get_direction(row['_ws.col.info'], interface)
                    if identifier_data.c_rnti == "00000":
                        if srcNode == "CUCP" and dstNode == "Target_CUCP":
                            srcNode = "src_CUCP"
                            dstNode = "CUCP"
                        if srcNode == "Target_CUCP" and dstNode == "CUCP":
                            srcNode = "CUCP"
                            dstNode = "src_CUCP"
                    message = MessageNsa(
                        frame_number=row['frame.number'],
                        frame_time=row['frame.time'],
                        ip_src=row['ip.src'],
                        ip_dst=row['ip.dst'],
                        protocol=row['frame.protocols'],
                        message=row['_ws.col.info'],
                        src_node=srcNode if srcNode else None,
                        dst_node=dstNode if dstNode else None,
                        message_json=None,
                        c_rnti=row['mavlterrc.rnti'],
                        enb_ue_s1ap_id=row.get('s1ap.ENB_UE_S1AP_ID', None),
                        mme_ue_s1ap_id=row.get('s1ap.MME_UE_S1AP_ID', None),
                        x2ap_ue_ran_id=row.get('x2ap.UE_X2AP_ID', None),
                        x2ap_5g_ran_id=row.get('x2ap.SgNB_UE_X2AP_ID', None),
                        uploaded_file_id=item_id,
                        gnb_id=row['gnb_id'],
                        identifiers_id=row['identifiers_id'],
                        s1ap_cause=row.get('s1ap.cause_desc', None),
                        nas_cause=row.get('nas.cause_desc', None)
                    )
                    messages_to_insert.append(message)

            # Bulk insert the 'Message' instances into the 'messages' model
            MessageNsa.objects.bulk_create(messages_to_insert)
            logging.debug(f"{len(messages_to_insert)} messages inserted for identifier {identifier_data.id}")

            logging.error(f"End of filtering messages and update in message table for each call "
                          f"flow : {upload_table.filename}")

        except Exception as e:
            logging.error(f"Exception during update_messages_with_identifier_key: {e}")
            pass
