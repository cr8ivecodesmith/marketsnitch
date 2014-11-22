from django.db import models


class BiddersList(models.Model):
    award_id = models.ForeignKey('Awards', to_field='award_id')
    line_item_id = models.ForeignKey('BidLineItem', to_field='line_item_id')
    org_id = models.ForeignKey('Organization', to_field='org_id')
    bidder_name = models.CharField(max_length=2048)


class Awards(models.Model):
    award_id = models.PositiveIntegerField(null=False, unique=True)
    ref_id = models.ForeignKey('BidInformation', to_field='ref_id')
    award_title = models.CharField(max_length=2048, blank=True)
    publish_date = models.DateTimeField()
    previous_award_id = models.PositiveIntegerField(null=True)
    line_item_id = models.ForeignKey('BidLineItem', to_field='line_item_id')
    item_name = models.CharField(max_length=2048, blank=True)
    item_description = models.TextField()
    quantity = models.PositiveIntegerField(null=True)
    uom = models.CharField(max_length=2048, blank=True)
    budget = models.FloatField()
    unspc_code = models.CharField(max_length=2048, blank=True)
    unspc_description = models.TextField()
    awardee_id = models.ForeignKey('Organization', to_field='org_id')
    awardee = models.CharField(max_length=2048, blank=True)
    award_type = models.CharField(max_length=2048, blank=True)
    contract_amt = models.FloatField()
    award_date = models.DateTimeField(blank=True)
    award_reason = models.CharField(max_length=2048, blank=True)
    contract_no = models.CharField(max_length=2048, blank=True)
    proceed_date = models.DateTimeField(blank=True)
    contract_start_date = models.DateTimeField(blank=True)
    contract_end_date = models.DateTimeField(blank=True)
    is_short_list = models.IntegerField(max_length=1)
    is_re_award = models.IntegerField(max_length=1)
    is_amp = models.IntegerField(max_length=1)


class Organization(models.Model):
    org_id = models.PositiveIntegerField(null=False)
    member_type_id = models.PositiveIntegerField(null=True)
    member_type = models.CharField(blank=True)
    parent_org_id = models.PositiveIntegerField(null=True)
    is_org_foreign = models.NullBooleanField()
    org_name = models.CharField(blank=True)
    goverment_branch = models.CharField(blank=True)
    government_organization_type = models.CharField(blank=True)
    supplier_form_of_organization = models.CharField(blank=True)
    supplier_organization_type = models.CharField(blank=True)
    org_reg_date = models.DateTimeField(blank=True)
    website = models.URLField(blank=True)
    org_description = models.TextField(blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    country = models.CharField(blank=True)
    region = models.CharField(blank=True)
    province = models.CharField(blank=True)
    city = models.CharField(blank=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    address3 = models.TextField(blank=True)
    zip_code = models.PositiveIntegerField(null=True)
    org_status = models.CharField(blank=True)
    modified_date = models.DateTimeField(blank=True)


class BidLineItem(models.Model):
    ref_id = models.ForeignKey('BidInformation', to_field='ref_id')
    line_item_id = models.PositiveIntegerField(null=False)
    item_name = models.CharField(blank=True)
    item_description = models.TextField(blank=True)
    qty = models.PositiveIntegerField(null=True)
    uomid = models.PositiveIntegerField(null=True)
    uom = models.CharField(blank=True)
    budget = models.FloatField(null=True)
    modified_date = models.DateTimeField(blank=True)


class BidInformation(models.Model):
    ref_id = models.IntegerField()
    ref_no = models.IntegerField()
    stage = models.IntegerField()
    stage2_ref_id = models.IntegerField()
    org_id = models.ForeignKey('Organization', to_field='org_id')
    classification = models.CharField(blank=True)
    solicitation_no = models.CharField(blank=True)
    notice_type = models.CharField(blank=True)
    business_category = models.CharField(blank=True)
    procurement_mode = models.CharField(blank=True)
    funding_instrument = models.CharField(blank=True)
    funding_source = models.CharField(blank=True)
    approved_budget = models.FloatField(null=False, blank=False)
    publish_date = models.DateTimeField(null=False, blank=False)
    closing_date = models.DateTimeField(null=False, blank=False)
    contract_duration = models.IntegerField(null=True)
    calendar_type = models.CharField(blank=True)
    trade_agreement = models.CharField(blank=True)
    pre_bid_date = models.DateTimeField(null=False, blank=False)
    pre_bid_venue = models.CharField(blank=True)
    procuring_entity_org_id = models.ForeignKey('Organization', to_field='org_id')
    procuring_entity_org = models.CharField(blank=True)
    client_agency_org_id = models.ForeignKey('Organization', to_field='org_id')
    client_agency_org = models.CharField(blank=True)
    contact_person = models.CharField(blank=True)
    contact_person_address = models.TextField(blank=True)
    tender_title = models.CharField(blank=True)
    description = models.TextField(blank=True)
    other_info = models.TextField(blank=True)
    tender_status = models.CharField(blank=True)
    reason = models.TextField(blank=True)
    date_available = models.DateTimeField(null=True, blank=True)
    collection_contact = models.CharField(blank=True)
    collection_point = models.CharField(blank=True)
    special_instruction = models.TextField(blank=True)
    created_by = models.CharField()
    creation_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __unicode__(self):
        return "{}: {} {}".format(ref_id, notice_type, business_category)
