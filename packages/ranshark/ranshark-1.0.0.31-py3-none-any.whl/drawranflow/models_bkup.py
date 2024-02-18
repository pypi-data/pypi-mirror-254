from django.db import models


class UploadedFile(models.Model):
    filename = models.CharField(max_length=255, null=True)
    uploadDate = models.DateTimeField(auto_now_add=True)
    processDate = models.DateTimeField(null=True)
    processed = models.BooleanField(default=False)
    completeAt = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    isAnalysisComplete = models.BooleanField(default=False)
    processing_status = models.CharField(max_length=255, null=True)
    network=models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "uploadfile"


class Identifiers(models.Model):
    id = models.BigAutoField(primary_key=True)

    c_rnti = models.CharField(max_length=255, null=True, blank=True)
    gnb_du_ue_f1ap_id = models.CharField(max_length=255, null=True, blank=True)
    gnb_cu_ue_f1ap_id = models.CharField(max_length=255, null=True, blank=True)
    gnb_cu_cp_ue_e1ap_id = models.CharField(max_length=255, null=True, blank=True)
    gnb_cu_up_ue_e1ap_id = models.CharField(max_length=255, null=True, blank=True)
    ran_ue_ngap_id = models.CharField(max_length=255, null=True, blank=True)
    amf_ue_ngap_id = models.CharField(max_length=255, null=True, blank=True)
    xnap_src_ran_id = models.CharField(max_length=255, null=True, blank=True)
    xnap_trgt_ran_id = models.CharField(max_length=255, null=True, blank=True)
    pci = models.CharField(max_length=255, null=True)  # Allow NULL
    cucp_f1c_ip = models.CharField(max_length=255, null=False, blank=True)
    du_f1c_ip = models.CharField(max_length=255, null=False, blank=True)
    gnb_id = models.CharField(max_length=255, null=False, blank=True)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    frame_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    f1ap_cause = models.CharField(max_length=255, null=True, blank=True)
    ngap_cause = models.CharField(max_length=255, null=True, blank=True)
    nas_cause = models.CharField(max_length=255, null=True, blank=True)
    plmn = models.CharField(max_length=255, null=True, blank=True)
    tmsi = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "identifiers"


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)

    frame_number = models.IntegerField()
    frame_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    ip_src = models.CharField(max_length=255, null=True)
    ip_dst = models.CharField(max_length=255, null=True)
    protocol = models.CharField(max_length=255, null=True)
    f1_proc = models.CharField(max_length=255, null=True)
    e1_proc = models.CharField(max_length=255, null=True)
    ng_proc = models.CharField(max_length=255, null=True)
    xn_proc = models.CharField(max_length=255, null=True)
    c1_rrc = models.CharField(max_length=255, null=True)
    c2_rrc = models.CharField(max_length=255, null=True)
    mm_message_type = models.CharField(max_length=255, null=True)
    sm_message_type = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    src_node = models.CharField(max_length=255, null=True)  # Add source node field
    dst_node = models.CharField(max_length=255, null=True)  # Add destination node field
    message_json = models.JSONField(null=True)
    c_rnti = models.CharField(max_length=255, null=True, blank=True)
    gnb_du_ue_f1ap_id = models.CharField(max_length=255, null=True, blank=True)
    gnb_cu_ue_f1ap_id = models.CharField(max_length=255, null=True, blank=True)
    gnb_cu_cp_ue_e1ap_id = models.CharField(max_length=255, null=True, blank=True)
    gnb_cu_up_ue_e1ap_id = models.CharField(max_length=255, null=True, blank=True)
    ran_ue_ngap_id = models.CharField(max_length=255, null=True, blank=True)
    amf_ue_ngap_id = models.CharField(max_length=255, null=True, blank=True)
    xnap_src_ran_id = models.CharField(max_length=255, null=True, blank=True)
    xnap_trgt_ran_id = models.CharField(max_length=255, null=True, blank=True)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    identifiers = models.ForeignKey(Identifiers, on_delete=models.CASCADE, default=None, blank=True, null=True)
    gnb_id = models.CharField(max_length=255, null=False, blank=True)
    f1ap_cause = models.CharField(max_length=255, null=True, blank=True)
    ngap_cause = models.CharField(max_length=255, null=True, blank=True)
    nas_cause = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Message from {self.ip_src} to {self.ip_dst} at {self.frame_time}'
    class Meta:
        db_table = "message"


class Stats(models.Model):
    id = models.BigAutoField(primary_key=True)

    category = models.CharField(max_length=50)
    uploadedFiles = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    success = models.IntegerField(default=0)
    fails = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)
    cucp_f1c_ip = models.CharField(max_length=255, null=False, blank=True)
    gnb_id = models.CharField(max_length=255, null=False, blank=True)


class IdentifiersStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifier = models.ForeignKey(Identifiers, on_delete=models.CASCADE, related_name='identifier_stats')
    category = models.CharField(max_length=50)
    attempts = models.IntegerField(default=0)
    success = models.IntegerField(default=0)
    fails = models.IntegerField(default=0)
    timeouts = models.IntegerField(default=0)
    uploadedFiles = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    cucp_f1c_ip = models.CharField(max_length=255, null=False, blank=True)
    gnb_id = models.CharField(max_length=255, null=False, blank=True)

# 5G-NSA Models


class IdentifiersNsa(models.Model):
    id = models.BigAutoField(primary_key=True)

    c_rnti = models.CharField(max_length=255, null=True, blank=True)
    gnb_id = models.CharField(max_length=255, null=False, blank=True)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    frame_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    s1ap_cause = models.CharField(max_length=255, null=True, blank=True)
    x2ap_cause = models.CharField(max_length=255, null=True, blank=True)
    nas_cause = models.CharField(max_length=255, null=True, blank=True)
    plmn = models.CharField(max_length=255, null=True, blank=True)
    tmsi = models.CharField(max_length=255, null=True, blank=True)
    enb_ue_s1ap_id = models.CharField(max_length=255, null=True, blank=True)
    mme_ue_s1ap_id = models.CharField(max_length=255, null=True, blank=True)
    x2ap_ue_ran_id = models.CharField(max_length=255, null=True, blank=True)
    x2ap_5g_ran_id = models.CharField(max_length=255, null=True, blank=True)
    gtp_teid = models.CharField(max_length=255, null=True, blank=True)
    pci = models.CharField(max_length=255, null=True)  # Allow NULL
    cucp_f1c_ip = models.CharField(max_length=255, null=False, blank=True)
    du_f1c_ip = models.CharField(max_length=255, null=False, blank=True)
    class Meta:
        db_table = "identifiers_nsa"

class MessageNsa(models.Model):
    id = models.BigAutoField(primary_key=True)

    frame_number = models.IntegerField()
    frame_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    ip_src = models.CharField(max_length=255, null=True)
    ip_dst = models.CharField(max_length=255, null=True)
    protocol = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    src_node = models.CharField(max_length=255, null=True)  # Add source node field
    dst_node = models.CharField(max_length=255, null=True)  # Add destination node field
    message_json = models.JSONField(null=True)
    c_rnti = models.CharField(max_length=255, null=True, blank=True)
    enb_ue_s1ap_id = models.CharField(max_length=255, null=True, blank=True)
    mme_ue_s1ap_id = models.CharField(max_length=255, null=True, blank=True)
    x2ap_ue_ran_id = models.CharField(max_length=255, null=True, blank=True)
    x2ap_5g_ran_id = models.CharField(max_length=255, null=True, blank=True)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    identifiers = models.ForeignKey(IdentifiersNsa, on_delete=models.CASCADE, default=None, blank=True, null=True)
    gnb_id = models.CharField(max_length=255, null=False, blank=True)
    s1ap_cause = models.CharField(max_length=255, null=True, blank=True)
    x2ap_cause = models.CharField(max_length=255, null=True, blank=True)
    nas_cause = models.CharField(max_length=255, null=True, blank=True)
    plmn = models.CharField(max_length=255, null=True, blank=True)
    tmsi = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "messages_nsa"