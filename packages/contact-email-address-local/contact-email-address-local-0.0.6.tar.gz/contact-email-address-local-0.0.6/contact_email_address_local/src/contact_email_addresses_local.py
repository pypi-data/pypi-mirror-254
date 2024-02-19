from .contact_email_addresses_constants import CONTACT_EMAIL_ADDRESSES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
from database_mysql_local.generic_mapping import GenericMapping
from email_address_local.email_address import EmailAddressesLocal
from language_remote.lang_code import LangCode
from logger_local.LoggerLocal import Logger
from user_context_remote.user_context import UserContext

logger = Logger.create_logger(object=CONTACT_EMAIL_ADDRESSES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

user_context = UserContext.login_using_user_identification_and_password()

DEFAULT_SCHEMA_NAME = "contact_email_address"
DEFAULT_ENTITY_NAME1 = "contact"
DEFAULT_ENTITY_NAME2 = "email_address"
DEFAULT_ID_COLUMN_NAME = "contact_email_id"
DEFAULT_TABLE_NAME = "contact_email_address_table"
DEFAULT_VIEW_TABLE_NAME = "contact_email_address_view"


class ContactEmailAdressesLocal(GenericMapping):
    def __init__(self, default_schema_name: str = DEFAULT_SCHEMA_NAME, default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2, default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_table_name: str = DEFAULT_TABLE_NAME, default_view_table_name: str = DEFAULT_VIEW_TABLE_NAME,
                 lang_code: LangCode = None, is_test_data: bool = False) -> None:

        super().__init__(default_schema_name=default_schema_name, default_entity_name1=default_entity_name1,
                         default_entity_name2=default_entity_name2, default_id_column_name=default_id_column_name,
                         default_table_name=default_table_name, default_view_table_name=default_view_table_name,
                         is_test_data=is_test_data)
        self.email_address_local = EmailAddressesLocal()
        self.lang_code = lang_code or user_context.get_effective_profile_preferred_lang_code()

    def insert_contact_and_link_to_email_address(self, contact_dict: dict, contact_email_address: str,
                                                 contact_id: int) -> int:
        """
        Insert contact and link to existing or new email address
        :param contact_dict: contact_dict
        :param contact_email_address: contact_email_address
        :param contact_id: contact_id
        :return: contact_id
        """
        logger.start(object={"contact_dict": contact_dict, "contact_email_address": contact_email_address,
                                  "contact_id": contact_id})
        if not contact_email_address:
            # TODO: we can try to look if there's an email address in the database by phone number
            # when contact-phones-local is done
            return None
        email_address_id = self.email_address_local.get_email_address_id_by_email_address(email_address=contact_email_address)
        if not email_address_id:
            # Create a new  email address and add it to email_address_table and email_address_ml_table
            logger.info(log_message="email_address_id is None, creating a new email address and adding it to"
                             " email_address_table and email_address_ml_table")
            first_name = contact_dict.get("first_name")
            last_name = contact_dict.get("last_name")
            name = f"{first_name} {last_name}"
            email_address_id = self.email_address_local.insert(email_address=contact_email_address, lang_code=self.lang_code,
                                                               name=name, is_test_data=self.is_test_data)
            if not email_address_id:
                logger.error(log_message="email_address_id is None")
                return None
            # Link contact to email address
            logger.info(log_message="Linking contact to email address")
            contact_email_address_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                           entity_name2=self.default_entity_name2,
                                                           entity_id1=contact_id, entity_id2=email_address_id)
        else:
            # check if there is link to existing email address
            logger.info(log_message="Linking contact to existing email address")
            mapping_tuple = self.select_multi_mapping_tuple_by_id(entity_name1=self.default_entity_name1,
                                                                  entity_name2=self.default_entity_name2,
                                                                  entity_id1=contact_id, entity_id2=email_address_id)
            if not mapping_tuple:
                # Link contact to existing email address
                logger.info(log_message="Linking contact to existing email address")
                contact_email_address_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                               entity_name2=self.default_entity_name2,
                                                               entity_id1=contact_id, entity_id2=email_address_id)
            else:
                logger.info(log_message="contact is already linked to email address")
                contact_email_address_id = mapping_tuple[0]
        logger.end(object={"contact_email_address_id": contact_email_address_id})
        return contact_email_address_id
