from .contact_locations_local_constants import CONTACT_LOCATIONS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
from database_mysql_local.generic_mapping import GenericMapping
from location_local.locations_local_crud import LocationsLocal
from language_remote.lang_code import LangCode
from user_context_remote.user_context import UserContext
from logger_local.LoggerLocal import Logger

DEFAULT_SCHEMA_NAME = "contact_location"
DEFAULT_ENTITY_NAME1 = "contact"
DEFAULT_ENTITY_NAME2 = "location"
DEFAULT_ID_COLUMN_NAME = "contact_location_id"
DEFAULT_TABLE_NAME = "contact_location_table"
DEFAULT_VIEW_TABLE_NAME = "contact_location_view"

logger = Logger.create_logger(object=CONTACT_LOCATIONS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

user_context = UserContext.login_using_user_identification_and_password()


class ContactLocationsLocal(GenericMapping):
    def __init__(self, default_schema_name: str = DEFAULT_SCHEMA_NAME, default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2, default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_table_name: str = DEFAULT_TABLE_NAME, default_view_table_name: str = DEFAULT_VIEW_TABLE_NAME,
                 lang_code: LangCode = None, is_test_data: bool = False) -> None:

        super().__init__(default_schema_name=default_schema_name, default_entity_name1=default_entity_name1,
                         default_entity_name2=default_entity_name2, default_id_column_name=default_id_column_name,
                         default_table_name=default_table_name, default_view_table_name=default_view_table_name,
                         is_test_data=is_test_data)
        self.locations_local = LocationsLocal()
        self.lang_code = lang_code or user_context.get_effective_profile_preferred_lang_code()

    def insert_contact_and_link_to_location(self, contact_dict: dict, location_dict: dict,
                                            contact_id: int) -> int:
        """
        Insert contact and link to existing or new location
        :param contact_dict: contact_dict
        :param contact_email_address: contact_email_address
        :param contact_id: contact_id
        :return: contact_id
        """
        logger.start(object={"contact_dict": contact_dict, "location_dict": location_dict,
                             "contact_id": contact_id})
        location_str = contact_dict.get("location", None)
        if not location_str or not location_dict:
            logger.end(log_message="contact has no location")
            return None
        # TODO: now the method always inserts a new location, later we can try to look if there's a location in the
        # database and create a new one only if there isn't one already
        location_id = self.locations_local.insert(data=location_dict, lang_code=self.lang_code.value)
        logger.info(log_message="Linking contact to location")
        contact_location_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                  entity_name2=self.default_entity_name2,
                                                  entity_id1=contact_id, entity_id2=location_id)
        logger.end(object={"contact_location_id": contact_location_id})
        return contact_location_id
