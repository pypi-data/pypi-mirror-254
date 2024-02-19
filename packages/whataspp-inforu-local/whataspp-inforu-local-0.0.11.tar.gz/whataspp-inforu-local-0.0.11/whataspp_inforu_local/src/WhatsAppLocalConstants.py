from logger_local.LoggerComponentEnum import LoggerComponentEnum

WHATSAPP_MESSAGE_INFORU_API_TYPE_ID = 8

WHATSAPP_API_URL = 'https://capi.inforu.co.il/api/v2/WhatsApp/SendWhatsAppChat'

WHATSAPP_LOGGER_COMPONENT_ID = 208
WHATSAPP_LOGGER_COMPONENT_NAME = "WhatsApp_InforU_LOCAL_PYTHON_PACKAGE"
WHATSAPP_DEVELOPER_EMAIL = "emad.a@circ.zone"


def get_logger_object(category: str = LoggerComponentEnum.ComponentCategory.Code):
    if category == LoggerComponentEnum.ComponentCategory.Code:
        return {
            'component_id': WHATSAPP_LOGGER_COMPONENT_ID,
            'component_name': WHATSAPP_LOGGER_COMPONENT_NAME,
            'component_category': LoggerComponentEnum.ComponentCategory.Code,
            'developer_email': WHATSAPP_DEVELOPER_EMAIL
        }
    elif category == LoggerComponentEnum.ComponentCategory.Unit_Test:
        return {
            'component_id': WHATSAPP_LOGGER_COMPONENT_ID,
            'component_name': WHATSAPP_LOGGER_COMPONENT_NAME,
            'component_category': LoggerComponentEnum.ComponentCategory.Unit_Test,
            'developer_email': WHATSAPP_DEVELOPER_EMAIL
        }
