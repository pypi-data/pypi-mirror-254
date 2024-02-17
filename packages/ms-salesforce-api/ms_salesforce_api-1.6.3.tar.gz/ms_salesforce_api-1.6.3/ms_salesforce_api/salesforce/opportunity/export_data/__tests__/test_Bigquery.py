import re
import unittest
from unittest import mock


class BigQueryExporterTestCase(unittest.TestCase):
    def setUp(self):
        self.project_id = "your-project-id"
        self.dataset_id = "your-dataset-id"

        self.opportunities = [
            {
                "jira_component_url": "<a "
                'href="https://makingscience.atlassian.net/browse/ESMSBD0001-24069" '
                'target="_blank">View Jira Task</a>',
                "lead_source": "Crosselling/upselling",
                "opportunity_id": "006AX0000064R0gYAE",
                "opportunity_line_items": [
                    {
                        "country": "ES",
                        "jira_task_url": "",
                        "opportunity_id": "006AX0000064R0gYAE",
                        "product_id": "",
                        "profit_center_name": "Arch. & Infras. Eng. | "
                        "Spain",
                    },
                    {
                        "country": "ES",
                        "jira_task_url": "",
                        "opportunity_id": "006AX0000064R0gYAE",
                        "product_id": "",
                        "profit_center_name": "Adtech International",
                    },
                    {
                        "country": "ES",
                        "jira_task_url": "",
                        "opportunity_id": "006AX0000064R0gYAE",
                        "product_id": "",
                        "profit_center_name": "Data International",
                    },
                    {
                        "country": "ES",
                        "jira_task_url": "",
                        "opportunity_id": "006AX0000064R0gYAE",
                        "product_id": "",
                        "profit_center_name": "DataOps | Spain",
                    },
                ],
                "opportunity_name_short": "Negativizar Trafico Web",
                "probability": 50.0,
                "stage_name": "Requirements Set",
                "tier_short": "T3",
            }
        ]

        self.mock_bigquery_manager = mock.patch(
            "gc_google_services_api.bigquery.BigQueryManager"
        ).start()
        from ..Bigquery import BigQueryExporter

        self.exporter = BigQueryExporter(self.project_id, self.dataset_id)

    def tearDown(self):
        self.mock_bigquery_manager.reset_mock()

    def test_export_opportunities(self):
        self.exporter._export_opportunities(self.opportunities)

        expected_query = """
        INSERT INTO `your-project-id.your-dataset-id.opportunity_line_item` (
            opportunity_id,
            product_id,
            profit_center_name,
            country,
            jira_task_url
        ) VALUES (
            "006AX0000064R0gYAE",
            "",
            "Arch.&Infras.Eng.|Spain",
            "ES",
            ""
        ),
        (
            "006AX0000064R0gYAE",
            "",
            "AdtechInternational",
            "ES",
            ""
        ),(
            "006AX0000064R0gYAE",
            "","DataInternational",
            "ES",
            ""
        ),(
            "006AX0000064R0gYAE",
            "",
            "DataOps|Spain",
            "ES",
            ""
        );
        """
        execute_query_calls = self.exporter.client.execute_query.call_args_list

        expected_query_stripped = re.sub(r"\s+", "", expected_query)

        self.assertEqual(
            expected_query_stripped,
            re.sub(r"\s+", "", str(execute_query_calls[1][0][0])),
        )

    def test_export_PLIs(self):
        self.exporter._export_PLIs(self.opportunities)

        expected_query = """
            INSERT INTO `your-project-id.your-dataset-id.opportunity_line_item` (
                opportunity_id,
                product_id,
                profit_center_name,
                country,
                jira_task_url
            ) VALUES (
                "006AX0000064R0gYAE",
                "",
                "Arch.&Infras.Eng.|Spain",
                "ES",
                ""
            ), (
                "006AX0000064R0gYAE",
                "",
                "AdtechInternational",
                "ES",
                ""
            ), (
                "006AX0000064R0gYAE",
                "",
                "DataInternational",
                "ES",
                ""
            ),(
            "006AX0000064R0gYAE",
            "",
            "DataOps|Spain","ES",
            ""
        );
        """

        execute_query_calls = self.exporter.client.execute_query.call_args_list
        expected_query_stripped = re.sub(r"\s+", "", expected_query)
        execute_query_stripped = re.sub(
            r"\s+", "", str(execute_query_calls[0][0][0])
        )

        self.assertEqual(execute_query_stripped, expected_query_stripped)

    @mock.patch(
        "ms_salesforce_api.salesforce.project.export_data.Bigquery.BigQueryManager"  # noqa: E501
    )
    def test_export_data(self, mock_bq_manager):
        mock_client = mock.Mock()
        mock_bq_manager.return_value = mock_client

        self.exporter.export_data(self.opportunities)

        expected_opportunities_query = """
            INSERT INTO `your-project-id.your-dataset-id.all_opportunity` (
                opportunity_id,
                opportunity_name_short,
                probability,
                stage_name,
                tier_short,
                jira_component_url,
                lead_source
            ) VALUES (
                "006AX0000064R0gYAE",
                "NegativizarTraficoWeb",
                50.0,
                "RequirementsSet",
                "T3",
                "%3Ca%20href%3D%22https%3A%2F%2Fmakingscience.atlassian.net%2Fbrowse%2FESMSBD0001-24069%22%20target%3D%22_blank%22%3EView%20Jira%20Task%3C%2Fa%3E",
                "Crosselling/upselling"
            );
        """

        expected_PLIs_query = """
            INSERT INTO `your-project-id.your-dataset-id.opportunity_line_item` (
                opportunity_id,
                product_id,
                profit_center_name,
                country,
                jira_task_url
            ) VALUES (
                "006AX0000064R0gYAE",
                "",
                "Arch.&Infras.Eng.|Spain",
                "ES",
                ""
            ), (
                "006AX0000064R0gYAE",
                "",
                "AdtechInternational",
                "ES",
                ""
            ), (
                "006AX0000064R0gYAE",
                "",
                "DataInternational",
                "ES",
                ""
            ), (
                "006AX0000064R0gYAE",
                "",
                "DataOps|Spain",
                "ES",
                ""
            );
        """

        execute_query_calls = self.exporter.client.execute_query.call_args_list

        expected_opportunities_query_stripped = re.sub(
            r"\s+", "", expected_opportunities_query
        )

        execute_opportunities_query_stripped = re.sub(
            r"\s+", "", str(execute_query_calls[0][0][0])
        )

        expected_pli_query_stripped = re.sub(r"\s+", "", expected_PLIs_query)
        execute_pli_query_stripped = re.sub(
            r"\s+", "", str(execute_query_calls[1][0][0])
        )

        self.assertEqual(
            execute_opportunities_query_stripped,
            expected_opportunities_query_stripped,
        )

        self.assertEqual(
            execute_pli_query_stripped,
            expected_pli_query_stripped,
        )
