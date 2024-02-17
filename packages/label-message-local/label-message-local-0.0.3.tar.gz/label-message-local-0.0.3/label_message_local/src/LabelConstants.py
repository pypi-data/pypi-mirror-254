from logger_local.LoggerComponentEnum import LoggerComponentEnum

DEVELOPER_EMAIL = 'akiva.s@circ.zone'
LABEL_MESSAGE_PACKAGE_COMPONENT_NAME = 'label_message_package'
LABEL_MESSAGE_PACKAGE_COMPONENT_ID = 254
LABEL_MESSAGE_COMPONENT_NAME = 'Label local Python package'
LABEL_MESSAGE_CODE_LOGGER_OBJECT = {
    'component_id': LABEL_MESSAGE_PACKAGE_COMPONENT_ID,
    'component_name': LABEL_MESSAGE_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
LABEL_MESSAGE_TEST_LOGGER_OBJECT = {
    'component_id': LABEL_MESSAGE_PACKAGE_COMPONENT_ID,
    'component_name': LABEL_MESSAGE_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Unit_Test.value,
    'developer_email': DEVELOPER_EMAIL
}
MESSAGE_OUTBOX_LABEL_ID = 18
