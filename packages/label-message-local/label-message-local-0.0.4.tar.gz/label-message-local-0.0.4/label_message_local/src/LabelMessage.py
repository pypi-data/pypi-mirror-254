from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerLocal import Logger

from .LabelConstants import LABEL_MESSAGE_CODE_LOGGER_OBJECT

logger = Logger.create_logger(object=LABEL_MESSAGE_CODE_LOGGER_OBJECT)


class LabelsMessageLocal(GenericCRUD):

    def __init__(self):
        super().__init__(default_schema_name="label_message", default_table_name="label_message_table",
                         default_view_table_name='label_message_view')

    def add_label_message(self, label_id: int, message_id: int) -> int:
        label_data = {
            "label_id": label_id,
            "message_id": message_id
        }
        label_message_id = self.insert(data_json=label_data)
        return label_message_id
