import logging
from itertools import islice
from urllib.parse import quote

from gc_google_services_api.bigquery import BigQueryManager

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class BigQueryExporter:
    """
    Initializes the Bigquery exporter with the given project ID and dataset ID.

    Args:
        project_id (str): The ID of the Google Cloud project.
        dataset_id (str): The ID of the BigQuery dataset.
    """

    def __init__(self, project_id, dataset_id):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.client = BigQueryManager(
            project_id=project_id, dataset_id=dataset_id
        )
        self.batch_size = 200
        self.schemas = {
            "all_opportunity": {
                "opportunity_id": "STRING",
                "opportunity_name_short": "STRING",
                "probability": "FLOAT",
                "stage_name": "STRING",
                "tier_short": "STRING",
                "jira_component_url": "STRING",
                "lead_source": "STRING",
            },
            "opportunity_line_item": {
                "opportunity_id": "STRING",
                "product_id": "STRING",
                "profit_center_name": "STRING",
                "country": "STRING",
                "jira_task_url": "STRING",
            },
        }

        for table_name, table_schema in self.schemas.items():
            self.client.create_table_if_not_exists(table_name, table_schema)

    def _execute_query(self, query, log_id, default_error_value=None):
        custom_error_value = f"{log_id}_custom_error"

        result = self.client.execute_query(
            query,
            custom_error_value,
        )

        if result == custom_error_value:
            logging.error(
                f"[ERROR - _execute_query]: Error executing query for {log_id} in BigQuery."  # noqa: E203
            )
            result = default_error_value

        return result

    def _export_opportunities(self, opportunities):
        opportunities_values = []
        for opp in opportunities:
            opportunities_values.append(
                f"""
                (
                    "{opp['opportunity_id']}",
                    "{opp['opportunity_name_short']}",
                    {opp['probability']},
                    "{opp['stage_name']}",
                    "{opp['tier_short']}",
                    "{quote(opp['jira_component_url'], safe='s')}",
                    "{opp['lead_source']}"
                )
                """
            )
        if opportunities_values:
            insert_opportunities_query = f"""
                INSERT INTO `{self.project_id}.{self.dataset_id}.all_opportunity` (
                    opportunity_id,
                    opportunity_name_short,
                    probability,
                    stage_name,
                    tier_short,
                    jira_component_url,
                    lead_source
                ) VALUES {', '.join(opportunities_values)};
            """

            insert_opportunities_query = (
                insert_opportunities_query.replace("\n", "")
                .replace("    ", "")
                .replace("  ", "")
            )

            self._execute_query(
                query=insert_opportunities_query,
                log_id="INSERT_all_opportunity",
            )

    def _export_PLIs(self, opportunities):
        total_plis = sum(
            len(opp["opportunity_line_items"]) for opp in opportunities
        )

        for i in range(0, total_plis, self.batch_size):
            batch_opportunities = []
            batch_plis = []

            for opp in opportunities:
                remaining_plis = islice(
                    opp["opportunity_line_items"], i, i + self.batch_size
                )
                batch_opportunities.append(opp)
                batch_plis.extend(remaining_plis)
                opportunity_id = opp["opportunity_id"]

                if len(batch_plis) >= self.batch_size:
                    self._process_plis_batch(
                        batch_plis,
                        opportunity_id,
                    )

                    batch_opportunities = []
                    batch_plis = []

            if batch_plis:
                self._process_plis_batch(batch_plis, opportunity_id)

    def _process_plis_batch(self, plis, opportunity_id):
        plis_values = []
        for pli in plis:
            plis_values.append(
                f"""
                (
                    "{opportunity_id}",
                    "{pli['product_id']}",
                    "{pli['profit_center_name']}",
                    "{pli['country']}",
                    "{quote(pli['jira_task_url'], safe='s')}"
                )
                """
            )

        if plis_values:
            insert_plis_query = f"""
                INSERT INTO `{self.project_id}.{self.dataset_id}.opportunity_line_item` (
                    opportunity_id,
                    product_id,
                    profit_center_name,
                    country,
                    jira_task_url
                ) VALUES {', '.join(plis_values)};
            """

            insert_plis_query = (
                insert_plis_query.replace("\n", "")
                .replace("    ", "")
                .replace("  ", "")
            )

            self._execute_query(
                query=insert_plis_query, log_id="INSERT_opportunity_line_items"
            )

    def export_data(self, opportunities):
        opportunities_batches = [
            opportunities[i : i + self.batch_size]  # noqa: E203
            for i in range(0, len(opportunities), self.batch_size)
        ]
        for batch in opportunities_batches:
            self._export_opportunities(batch)

            self._export_PLIs(batch)

    def delete_all_rows(self):
        table_names = self.schemas.keys()
        for table_name in table_names:
            delete_query_table = f"DELETE FROM `{self.project_id}.{self.dataset_id}.{table_name}` WHERE true"  # noqa: E203
            self._execute_query(
                query=delete_query_table,
                log_id=f"delete_table_{table_name}",
            )
