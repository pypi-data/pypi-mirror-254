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
