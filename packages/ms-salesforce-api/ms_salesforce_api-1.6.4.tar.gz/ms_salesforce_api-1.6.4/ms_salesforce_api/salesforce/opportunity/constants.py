DEFAULT_ALL_OPPORTUNITIES_QUERY = """
SELECT
    Id,
    Opportunity_Name_Short__c,
    StageName,
    LeadSource,
    Probability,
    Tier_Short__c,
    JiraComponentURL__c,
    (
        SELECT
            Id,
            Product2.Id,
            Product2.LKP_ProfitCenter__r.Name,
            toLabel(Product2.LKP_ProfitCenter__r.PCK_Country__c
        )
        FROM
            OpportunityLineItems
    )
FROM
    Opportunity
"""

DEFAULT_ALL_OPPORTUNITIES_CREATE_TABLE_QUERY = """
CREATE TABLE all_opportunity (
    opportunity_id VARCHAR(255) PRIMARY KEY,
    opportunity_name_short VARCHAR(255) DEFAULT NULL,
    probability FLOAT DEFAULT NULL,
    stage_name VARCHAR(255) DEFAULT NULL,
    tier_short VARCHAR(255) DEFAULT NULL,
    jira_component_url VARCHAR(255) DEFAULT NULL,
    lead_source VARCHAR(255) DEFAULT NULL
);
"""

DEFAULT_OPPORTUNITY_LINE_ITEM_CREATE_TABLE_QUERY = """
CREATE TABLE opportunity_line_item (
    id SERIAL PRIMARY KEY,
    opportunity_id VARCHAR(255) DEFAULT NULL,
    product_id VARCHAR(255) DEFAULT NULL,
    profit_center_name VARCHAR(255) DEFAULT NULL,
    country VARCHAR(255) DEFAULT NULL,
    jira_task_url VARCHAR(255) DEFAULT NULL,
    FOREIGN KEY (opportunity_id) REFERENCES all_opportunity(opportunity_id)
);
"""

DEFAULT_POSTGRES_DATABASE_SCHEMAS_MAP = [
    {
        "db_name": "all_opportunity",
        "query": DEFAULT_ALL_OPPORTUNITIES_CREATE_TABLE_QUERY,
    },
    {
        "db_name": "opportunity_line_item",
        "query": DEFAULT_OPPORTUNITY_LINE_ITEM_CREATE_TABLE_QUERY,
    },
]

DEFAULT_DELETE_ALL_OPPORTUNITY_TABLE = "DELETE FROM all_opportunity WHERE true"
DEFAULT_DELETE_OPPORTUNITY_LINE_ITEM_TABLE = (
    "DELETE FROM opportunity_line_item WHERE true"
)
