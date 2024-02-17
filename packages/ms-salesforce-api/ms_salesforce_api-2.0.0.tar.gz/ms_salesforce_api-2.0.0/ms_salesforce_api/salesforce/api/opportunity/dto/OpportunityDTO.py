from ms_salesforce_api.salesforce.helpers.string import normalize_value


class OpportunityLineItemDTO(object):
    def __init__(
        self,
        product_id,
        profit_center_name,
        country,
        jira_task_url,
        opportunity_id,
    ):
        self.product_id = product_id
        self.profit_center_name = profit_center_name
        self.country = country
        self.jira_task_url = jira_task_url
        self.opportunity_id = opportunity_id

    @staticmethod
    def from_salesforce_record(line_item_record, opportunity_id):
        product = line_item_record.get("Product2", {})
        profit_center = product.get("LKP_ProfitCenter__r", {})
        profit_center_name = ""
        country = ""

        if profit_center:
            profit_center_name = normalize_value(profit_center.get("Name", ""))
            country = normalize_value(profit_center.get("PCK_Country__c", ""))

        return OpportunityLineItemDTO(
            product_id=product.get("Id", ""),
            profit_center_name=profit_center_name,
            country=country,
            jira_task_url=normalize_value(
                line_item_record.get("JiraComponentURL__c", "")
            ),
            opportunity_id=opportunity_id,
        )

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "profit_center_name": self.profit_center_name,
            "country": self.country,
            "jira_task_url": self.jira_task_url,
            "opportunity_id": self.opportunity_id,
        }


class OpportunityDTO(object):
    def __init__(
        self,
        jira_component_url,
        lead_source,
        opportunity_id,
        opportunity_line_items,
        opportunity_name_short,
        probability,
        stage_name,
        tier_short,
    ):
        self.jira_component_url = jira_component_url
        self.lead_source = lead_source
        self.opportunity_id = opportunity_id
        self.opportunity_line_items = opportunity_line_items
        self.opportunity_name_short = opportunity_name_short
        self.probability = probability
        self.stage_name = stage_name
        self.tier_short = tier_short

    @staticmethod
    def from_salesforce_record(record):
        opportunity_line_items = record.get("OpportunityLineItems", {})
        if opportunity_line_items and isinstance(opportunity_line_items, dict):
            line_items_records = record.get("OpportunityLineItems", {}).get(
                "records", []
            )
            opportunity_line_items = [
                OpportunityLineItemDTO.from_salesforce_record(
                    line_item, record["Id"]
                ).to_dict()
                for line_item in line_items_records
            ]
        else:
            opportunity_line_items = []

        return OpportunityDTO(
            jira_component_url=normalize_value(
                record.get("JiraComponentURL__c", "")
            ),
            lead_source=normalize_value(record.get("LeadSource", "")),
            opportunity_id=record["Id"],
            opportunity_line_items=opportunity_line_items,
            opportunity_name_short=normalize_value(
                record.get("Opportunity_Name_Short__c", "")
            ),
            probability=float(record.get("Probability", 0.0)),
            stage_name=normalize_value(record.get("StageName", "")),
            tier_short=normalize_value(record.get("Tier_Short__c", "")),
        )

    def to_dict(self):
        return {
            "jira_component_url": self.jira_component_url,
            "lead_source": self.lead_source,
            "opportunity_id": self.opportunity_id,
            "opportunity_line_items": self.opportunity_line_items,
            "opportunity_name_short": self.opportunity_name_short,
            "probability": self.probability,
            "stage_name": self.stage_name,
            "tier_short": self.tier_short,
        }
