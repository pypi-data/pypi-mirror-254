from datetime import datetime

from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.LoggerLocal import Logger

CAMPAIGN_COMPONENT_ID = 282
CAMPAIGN_COMPONENT_NAME = "campaign-local"
DEVELOPER_EMAIL = "akiva.s@circ.zone"
object1 = {
    'component_id': CAMPAIGN_COMPONENT_ID,
    'component_name': CAMPAIGN_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
logger = Logger.create_logger(object=object1)


class CampaignLocal(GenericCRUD):
    def __init__(self) -> None:
        super().__init__(default_schema_name="campaign", default_table_name="campaign_table",
                         default_view_table_name="campaign_view", default_id_column_name="campaign_id")

    def insert_campaign(self, name: str = None, start_hour: int = None,
                        end_hour: int = None, occurrence_id: int = None, days_of_week: str = None,
                        max_audience: int = None, max_exposure_per_day: int = None,
                        minimal_days_between_messages_to_the_same_recipient: int = None,
                        message_template_id: int = None, dialog_workflow_script_id: int = None,
                        is_test_data: bool = None, start_timestamp: datetime = None,
                        end_timestamp: datetime = None, created_timestamp: datetime = None,
                        created_user_id: int = None, updated_timestamp: datetime = None,
                        updated_user_id: int = None, **kwargs) -> int:
        """Inserts a campaign into the database"""
        data_json = {}
        for arg in locals().items():
            if arg[0] in ("self", "__class__") or arg[1] is None:
                continue
            if arg[1] is not None:
                data_json[arg[0]] = arg[1]
        campaign_id = self.insert(schema_name="campaign", table_name="campaign_table",
                                  data_json=data_json)
        # # insert to campaign_criteria
        # criteria_id = self.insert(schema_name="criteria", table_name="criteria_table",
        #                              data_json={"is_test_data": is_test_data})
        #
        # # insert to campaign_criteria
        # campaign_criteria_id = self.insert(schema_name="campaign_criteria",
        #                                       table_name="campaign_criteria_table",
        #                                       data_json={"is_test_data": is_test_data,
        #                                                  "criteria_id": criteria_id,
        #                                                  "campaign_id": campaign_id})
        return campaign_id

    def get_test_campaign_id(self) -> int:
        return self.get_test_entity_id(entity_name="campaign",
                                       insert_function=self.insert_campaign)
