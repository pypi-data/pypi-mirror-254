from datetime import datetime

from database_mysql_local.generic_crud import GenericCRUD


class GetTestIds(GenericCRUD):
    def __init__(self):
        super().__init__(default_schema_name="message", default_table_name="message_table",
                         default_view_table_name="message_outbox_view", default_id_column_name="message_id")

    def insert_message(self, parent_message_id: int = None,
                       message_message_relationship_id: int = None, sender_profile_id: int = None,
                       sender_email: str = None, to_profile_id: int = None, to_profile_list_id: int = None,
                       to_email: str = None, cc_profile_id: int = None, cc_profile_list_id: int = None,
                       cc_email: str = None, bcc_profile_id: int = None, bcc_profile_list_id: int = None,
                       bcc_email: str = None, group_list_id: int = None, occurrence_id: int = None,
                       location_id: int = None, message_channel_id: int = None, message_type_id: int = None,
                       push_notification: bool = None, group_id: int = None, session_id: int = None,
                       visibility_id: int = None, pin: bool = None, mailbox_id: int = None,
                       is_gen_ai: bool = None, machine_learning_model_id: int = None,
                       is_require_moderator: bool = None, moderator_profile_id: int = None,
                       moderator_feedback_type: int = None, moderator_feedback_text: str = None,
                       is_moderator_approved: bool = None, profile_id: int = None,
                       class_parameters_json: str = None, function_parameters_json: str = None,
                       action_id: int = None, campaign_id: int = None, requested_channel_id: int = None,
                       actual_channel_id: int = None, provider_id: int = None, is_test_data: bool = None) -> int:
        """Inserts a message into the database"""
        data_json = {}
        for arg in locals().items():
            if arg[0] in ("self", "__class__", "data_json") or arg[1] is None:
                continue
            if arg[1] is not None:
                data_json[arg[0]] = arg[1]

        message_id = self.insert(schema_name="message", data_json=data_json)
        return message_id

    def get_test_message_id(self) -> int:
        return self.get_test_entity_id(entity_name="message",
                                       insert_function=self.insert_message)

    def insert_campaign(self, name: str = None, start_hour: int = None,
                        end_hour: int = None, occurrence_id: int = None, days_of_week: str = None,
                        max_audience: int = None, max_exposure_per_day: int = None,
                        minimal_days_between_messages_to_the_same_recipient: int = None,
                        message_template_id: int = None, dialog_workflow_script_id: int = None,
                        is_test_data: bool = None, start_timestamp: datetime = None,
                        end_timestamp: datetime = None, created_timestamp: datetime = None,
                        created_user_id: int = None, updated_timestamp: datetime = None,
                        updated_user_id: int = None) -> int:
        """Inserts a campaign into the database"""
        data_json = {}
        for arg in locals().items():
            if arg[0] in ("self", "__class__", "data_json") or arg[1] is None:
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

    def insert_contact(self, is_test_data: bool = False, **kwargs):
        data_json = {"is_test_data": is_test_data}
        data_json.update(kwargs)

        contact_id = self.insert(schema_name="contact", table_name="contact_table",
                                 data_json=data_json)
        return contact_id

    def get_test_contact_id(self) -> int:
        return self.get_test_entity_id(entity_name="contact",
                                       insert_function=self.insert_contact)
