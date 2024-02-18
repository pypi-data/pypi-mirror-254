import logging
import numpy as np
import pandas as pd
from drawranflow.models import IdentifiersNsa, UploadedFile
from .utils_sa import get_gnb_id, get_trgt_gnb_id
from django.db import IntegrityError, transaction


def split_values(row):
    row = str(row).strip()
    if pd.notna(row) and str(row).lower() != 'nan':
        values = str(row).split(',')
        return values[1] if len(values) > 1 else values[0]
    else:
        return np.nan


# Define reusable functions here
def filter_dataframe_by_protocol_nsa(df, protocol):
    return df[df['frame.protocols'].apply(lambda x: protocol.lower() in x.lower() if isinstance(x, str) else False)]


def update_identifiers_df_nsa(identifiers_df, condition_df, column_name):
    identifiers_df.at[condition_df.index, column_name] = condition_df.iloc[0][column_name]


def bulk_update_identifiers_nsa(identifiers_df):
    batch_size = 100  # You can adjust this based on your needs
    identifiers_to_update = []
    with transaction.atomic():
        for _ , row in identifiers_df.iterrows():
            try:
                c_rnti_value = row.get('c_rnti', None)
                if pd.isnull(c_rnti_value):
                    c_rnti_value = '00000'

                identifier_object, created = IdentifiersNsa.objects.get_or_create(
                        c_rnti=c_rnti_value,
                        pci=row.get('pci', None),
                        cucp_f1c_ip=row.get('cucp_f1c_ip', None),
                        du_f1c_ip=row.get('du_f1c_ip', None),
                        gnb_id=row.get('gnb_id', None),
                        uploaded_file_id=row['uploadedFiles_id'],
                        frame_time=row.get('frame_time', None),
                        tmsi=row.get('tmsi', None),
                        plmn=row.get('plmn', None),
                        gtp_teid=row.get('gtp_teid', None),
                        enb_ue_s1ap_id=row.get('enb_ue_s1ap_id', None),
                        mme_ue_s1ap_id=row.get('mme_ue_s1ap_id', None),
                        x2ap_ue_ran_id=row.get('x2ap_ue_ran_id', None),
                        x2ap_5g_ran_id=row.get('x2ap_5g_ran_id', None),
                    )

                if not created:
                    identifiers_to_update.append(identifier_object)

            except IntegrityError as e:
                logging.error(f"IntegrityError occurred during get_or_create: {e}")
            except Exception as e:
                logging.error(f"Error occurred during get_or_create: {e}")

            # Bulk update in batches
            if len(identifiers_to_update) >= batch_size:
                try:
                    Identifiers.objects.bulk_update(
                        identifiers_to_update,
                        fields=['c_rnti', 'cucp_f1c_ip', 'du_f1c_ip', 'enb_ue_s1ap_id', 'mme_ue_s1ap_id',
                                'frame_time', 'x2ap_ue_ran_id', 'x2ap_5g_ran_id', 'gnb_id','plmn','tmsi','gtp_teid']
                    )
                    identifiers_to_update = []
                except Exception as e:
                    logging.error(f"Error occurred during bulk update: {e}")

        # Final bulk update for any remaining objects
        if identifiers_to_update:
            try:
                IdentifiersNsa.objects.bulk_update(
                    identifiers_to_update,
                    fields=['c_rnti', 'cucp_f1c_ip', 'du_f1c_ip', 'enb_ue_s1ap_id', 'mme_ue_s1ap_id',
                                'frame_time', 'x2ap_ue_ran_id', 'x2ap_5g_ran_id', 'gnb_id','plmn','tmsi','gtp_teid']
                )
            except Exception as e:
                logging.error(f"Error occurred during final bulk update: {e}")


def update_identifiers_nsa(identifiers_df, match_df, column_name, actualcolumn, identifier_row, index):
    try:
        logging.debug(f"update_identifiers: {identifier_row['c_rnti']} - {column_name} - {actualcolumn}")
        new_value = match_df.iloc[0][actualcolumn]
        identifiers_df.at[index, column_name] = str(new_value)
        logging.debug(f"Updated {column_name} to {new_value}")
        return new_value
    except IndexError:
        logging.warning(f"IndexError during identifier update.")
        return None
    except Exception as e:
        logging.error(f"Error occurred during identifier update: {e}")
        return None


def find_messages_nsa(df, condition, additional_condition=None):
    try:
        if additional_condition is None:
            return df[condition]
        else:
            return df[condition & additional_condition]
    except Exception as e:
        logging.error(f"Error occurred during message retrieval: {e}")
        return pd.DataFrame()

# THis is for NSA call flow
def message_handler_nsa(df, item_id):
    try:
        upload_table = UploadedFile.objects.get(id=item_id)
        logging.error(f"Preparing initial analysis for the NSA, pcap file: {upload_table.filename}")

        lte_df = filter_dataframe_by_protocol_nsa(df, 'lte_rrc')
        s1ap_df = filter_dataframe_by_protocol_nsa(df, 's1ap')
        x2ap_df = filter_dataframe_by_protocol_nsa(df, 'x2ap')
        s1ap_df.loc[:, 's1ap.ENB_UE_S1AP_ID'] = s1ap_df['s1ap.ENB_UE_S1AP_ID'].apply(split_values)

        # Find RRC Setup, Reestablishment, and Setup Request messages
        rrc_setup_df = lte_df[lte_df['_ws.col.info'] == 'RRCConnectionSetup']
        rrc_reestablish_res_df = lte_df[lte_df['_ws.col.info'] == 'RRC Reestablishment']
        rrc_setup_request_df = lte_df[
            (lte_df['_ws.col.info'] == 'RRCConnectionRequest') & ~lte_df['mavlterrc.rnti'].isnull()]
        rrc_reestablish_df = lte_df[
            (lte_df['_ws.col.info'] == 'RRC Reestablishment Request') & ~lte_df['mavlterrc.rnti'].isnull()]

        combined_df = pd.concat([rrc_setup_request_df, rrc_reestablish_df])

        service_request_df = s1ap_df[
            ((s1ap_df['_ws.col.info'] == 'Service request')
             | (s1ap_df['_ws.col.info'] == 'PDN connectivity request')
             | (s1ap_df['_ws.col.info'] == 'Tracking area update request')) & ~s1ap_df['s1ap.ENB_UE_S1AP_ID'].isnull()
            ]
        service_request_df.loc[:, 's1ap.CellIdentity'] = combined_df['s1ap.CellIdentity'].map(get_gnb_id)

        s1ap_initial_messages_df = s1ap_df[
            ((s1ap_df['_ws.col.info'] == 'InitialContextSetupRequest') |
             (s1ap_df['_ws.col.info'] == 'Activate default EPS bearer context request') |
             (s1ap_df['_ws.col.info'] == 'UECapabilityInformation') |
             (s1ap_df['_ws.col.info'] == 'Identity request') |
             (s1ap_df['_ws.col.info'] == 'Authentication request') |
             (s1ap_df['_ws.col.info'] == 'Security mode command') |
             (s1ap_df['_ws.col.info'] == 'ESM Information request') |
             (s1ap_df['_ws.col.info'] == 'Registration Reject') |
             (s1ap_df['_ws.col.info'].str.contains('Registration reject')) |
             (s1ap_df['_ws.col.info'] == 'PDU Session Setup Request')) &
            ~s1ap_df['s1ap.ENB_UE_S1AP_ID'].isnull() &
            ~s1ap_df['s1ap.MME_UE_S1AP_ID'].isnull()
            ]
        s1ap_act_bearer_req_df = s1ap_df[
            ((s1ap_df['_ws.col.info'] == 'InitialContextSetupRequest') |
             (s1ap_df['_ws.col.info'] == 'Activate default EPS bearer context request')) &
            ~s1ap_df['s1ap.ENB_UE_S1AP_ID'].isnull() &
            ~s1ap_df['s1ap.MME_UE_S1AP_ID'].isnull()
            ]
        x2ap_gnb_addition_df = x2ap_df[
            (x2ap_df['_ws.col.info'] == 'SgNBAdditionRequest') &
            ~x2ap_df['x2ap.UE_X2AP_ID'].isnull() &
            x2ap_df['x2ap.SgNB_UE_X2AP_ID'].isnull()
            ]

        x2ap_gnb_addition_res_df = x2ap_df[
            (x2ap_df['_ws.col.info'] == 'RRC Reconfiguration') |
            (x2ap_df['_ws.col.info'] == 'SgNBAdditionRequestAcknowledge') &
            ~x2ap_df['x2ap.UE_X2AP_ID'].isnull() &
            ~x2ap_df['x2ap.SgNB_UE_X2AP_ID'].isnull()
            ]
        # Define the column mapping
        column_name_mapping = {
            'mavlterrc.rnti': 'c_rnti',
            'mavlterrc.cellid': 'pci',
            'frame.time': 'frame_time',
            's1ap.ENB_UE_S1AP_ID': 'enb_ue_s1ap_id',
            's1ap.MME_UE_S1AP_ID': 'mme_ue_s1ap_id',
            'ip.src': 'du_f1c_ip',
            'ip.dst': 'cucp_f1c_ip',
            'x2ap.UE_X2AP_ID': 'x2ap_ue_ran_id',
            'x2ap.SgNB_UE_X2AP_ID': 'x2ap_5g_ran_id',
            's1ap.CellIdentity': 'gnb_id',
            'nas_eps.emm.m_tmsi': 'tmsi',
            's1ap.pLMN_Identity': 'plmn',
        }


        identifiers_df = combined_df[list(column_name_mapping.keys())].copy()
        # Map 'xnap.NR_Cell_Identity' to 'gnb_id' in xnap_df
        x2ap_gnb_addition_df.loc[:, 'x2ap.eUTRANcellIdentifier'] = x2ap_gnb_addition_df['x2ap.eUTRANcellIdentifier'].map(get_trgt_gnb_id).astype(str)

        # Copy relevant columns from combined_df to identifiers_df
        identifiers_df.rename(columns=column_name_mapping, inplace=True)

        # Save to Identifiers table
        identifiers_df['uploadedFiles_id'] = item_id
        for index, identifier_row in identifiers_df.iterrows():
            try:
                logging.debug(f"identifier_row: {identifier_row}")
                identifier_time = identifier_row['frame_time']
                identifier_crnti = identifier_row['c_rnti']
                identifier_du_ip = identifier_row['du_f1c_ip']
                identifier_cucp_ip = identifier_row['cucp_f1c_ip']
                if identifier_crnti is not None and not pd.isnull(identifier_crnti):
                    matching_lte_rrc_setup = find_messages_nsa(
                        rrc_setup_df,
                        (rrc_setup_df['frame.time'] > identifier_time) &
                        (rrc_setup_df['frame.time'] <= identifier_time + pd.Timedelta('2s')) &
                        (rrc_setup_df['ip.src'] == identifier_cucp_ip) &
                        (rrc_setup_df['ip.dst'] == identifier_du_ip) &
                        (rrc_setup_df['mavlterrc.rnti'] == identifier_row['c_rnti'])&
                        (rrc_setup_df['mavlterrc.cellid'] == identifier_row['pci'])
                    )
                    if not matching_lte_rrc_setup.empty:
                        matching_s1ap_setup = find_messages_nsa(
                            service_request_df,
                            (service_request_df['frame.time'] >= identifier_row['frame_time']) &
                            (service_request_df['frame.time'] <= identifier_row['frame_time'] + pd.Timedelta('2s'))

                        )

                        # Update ran_ue_ngap_id in the Identifier DataFrame
                        enb_ue_s1ap_id = update_identifiers_nsa(identifiers_df, matching_s1ap_setup, 'enb_ue_s1ap_id',
                                                            's1ap.ENB_UE_S1AP_ID', identifier_row, index)
                        update_identifiers_nsa(identifiers_df, matching_s1ap_setup, 'tmsi',
                                                            'nas_eps.emm.m_tmsi', identifier_row, index)


                        # Find NGAP Initial Context Setup messages
                        matching_s1ap_ictxt_setup = find_messages_nsa(s1ap_initial_messages_df,
                                                                  (s1ap_initial_messages_df['frame.time'] >= identifier_row[
                                                                      'frame_time']) &
                                                                  (s1ap_initial_messages_df['frame.time'] <= identifier_row[
                                                                      'frame_time'] + pd.Timedelta('1s')) &
                                                                  (s1ap_initial_messages_df[
                                                                       's1ap.ENB_UE_S1AP_ID'] == enb_ue_s1ap_id))

                        # Update amf_ue_ngap_id using the update_identifiers function
                        mme_ue_s1ap_id = update_identifiers_nsa(identifiers_df, matching_s1ap_ictxt_setup, 'mme_ue_s1ap_id',
                                                            's1ap.MME_UE_S1AP_ID', identifier_row, index)

                        gtp_eid = update_identifiers_nsa(identifiers_df, matching_s1ap_ictxt_setup, 'gtp_teid',
                                                         's1ap.gTP_TEID', identifier_row, index)
                        if gtp_eid is np.nan or gtp_eid is "nan" or gtp_eid is None:
                            matching_act_bearer = find_messages_nsa(s1ap_act_bearer_req_df,
                                                                    (s1ap_act_bearer_req_df['frame.time'] >= identifier_row[
                                                                        'frame_time']) &
                                                                    (s1ap_act_bearer_req_df['frame.time'] <= identifier_row[
                                                                        'frame_time'] + pd.Timedelta('1s')) &
                                                                    (s1ap_act_bearer_req_df[
                                                                         's1ap.ENB_UE_S1AP_ID'] == enb_ue_s1ap_id) &
                                                                    (s1ap_act_bearer_req_df[
                                                                         's1ap.MME_UE_S1AP_ID'] == mme_ue_s1ap_id)
                                                                    )
                            gtp_eid = update_identifiers_nsa(identifiers_df, matching_act_bearer, 'gtp_teid',
                                                         's1ap.gTP_TEID', identifier_row, index)
                            logging.debug(f"matching_act_bearer: {matching_act_bearer}")
                        logging.debug(f"row: {index},enb_ue_s1ap_id: {enb_ue_s1ap_id}, mme_ue_s1ap_id: {mme_ue_s1ap_id},gtp_eid:{gtp_eid}")

                        matching_x2ap_req_setup = find_messages_nsa(x2ap_gnb_addition_df,
                                                                (x2ap_gnb_addition_df['frame.time'] >= identifier_row[
                                                                    'frame_time']) &
                                                                (x2ap_gnb_addition_df['frame.time'] <= identifier_row[
                                                                    'frame_time'] + pd.Timedelta("10s")) &
                                                                (x2ap_gnb_addition_df[
                                                                     'x2ap.gTP_TEID'].str.contains(gtp_eid)))



                        # Update xnap_src_ran_id using the update_identifier_and_log function
                        x2ap_ue_ran_id = update_identifiers_nsa(identifiers_df, matching_x2ap_req_setup, 'x2ap_ue_ran_id',
                                                             'x2ap.UE_X2AP_ID', identifier_row, index)
                        logging.debug(f"row: {index},x2ap_ue_ran_id:{x2ap_ue_ran_id}")

                        matching_x2ap_resp_setup = find_messages_nsa(x2ap_gnb_addition_res_df,
                                                                 (x2ap_gnb_addition_res_df['frame.time'] >= identifier_row[
                                                                     'frame_time']) &
                                                                 (x2ap_gnb_addition_res_df[
                                                                      'x2ap.UE_X2AP_ID'] == x2ap_ue_ran_id))

                        # Update xnap_trgt_ran_id using the update_identifier_and_log function
                        update_identifiers_nsa(identifiers_df, matching_x2ap_resp_setup, 'x2ap_5g_ran_id',
                                           'x2ap.SgNB_UE_X2AP_ID', identifier_row, index)

            except Exception as e:
                logging.error(f"Error occurred during row processing: {e}")
        bulk_update_identifiers_nsa(identifiers_df)
        logging.error(f"Identifiers are successfully derived")
    except Exception as e:
        logging.error("Error - Message Handler", e)
