from .contact_user_externals_local_constants import CONTACT_USER_EXTERNALS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
from logger_local.LoggerLocal import Logger
from database_mysql_local.generic_mapping import GenericMapping
from user_external_local.user_externals_local import UserExternalsLocal
from user_context_remote.user_context import UserContext

DEFAULT_SCHEMA_NAME = 'contact_user_external'
DEFAULT_ENTITY_NAME1 = 'contact'
DEFAULT_ENTITY_NAME2 = 'user_external'
DEFAULT_ID_COLUMN_NAME = 'contact_user_external_id'
DEFAULT_TABLE_NAME = 'contact_user_external_table'
DEFAULT_VIEW_TABLE_NAME = 'contact_user_external_view'
DEFAULT_SYSTEM_ID = 6

logger = Logger.create_logger(object=CONTACT_USER_EXTERNALS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

user_context = UserContext.login_using_user_identification_and_password()


class ContactUserExternalsLocal(GenericMapping):
    def __init__(self, default_schema_name: str = DEFAULT_SCHEMA_NAME, default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2, default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_table_name: str = DEFAULT_TABLE_NAME, default_view_table_name: str = DEFAULT_VIEW_TABLE_NAME,
                 system_id: int = DEFAULT_SYSTEM_ID, is_test_data: bool = False):

        super().__init__(default_schema_name=default_schema_name, default_entity_name1=default_entity_name1,
                         default_entity_name2=default_entity_name2, default_id_column_name=default_id_column_name,
                         default_table_name=default_table_name, default_view_table_name=default_view_table_name,
                         is_test_data=is_test_data)
        self.user_external = UserExternalsLocal()
        self.system_id = system_id

    def insert_contact_and_link_to_existing_or_new_user_external(self, contact_dict: dict, contact_email_address: str,
                                                                 contact_id: int, system_id: int = None,
                                                                 user_external_dict: dict = None) -> int:
        """
        Insert contact and link to existing or new user_external
        :param contact_dict: contact dict
        :param contact_id: contact id
        :param contact_email_address: contact email address
        :param system_id: system id
        :param user_external_dict: user_external dict
        :return: contact_user-external_id
        """
        logger.start(object={"contact_dict": contact_dict, "contact_email_address": contact_email_address,
                                  "contact_id": contact_id, "system_id": system_id, "user_external_dict": user_external_dict})
        profile_id = user_context.get_effective_profile_id()
        system_id = system_id if system_id else self.system_id
        if user_external_dict:
            username = user_external_dict.get("username", contact_email_address)    # noqa: F841
            profile_id = user_external_dict.get("profile_id", profile_id)
            system_id = user_external_dict.get("system_id", system_id)
            access_token = user_external_dict.get("access_token", None)
            expiry = user_external_dict.get("expiry", None)
            refresh_token = user_external_dict.get("refresh_token", None)
            oauth_token = user_external_dict.get("oauth_token", None)   # noqa: F841
            oauth_token_secret = user_external_dict.get("oauth_token_secret", None)   # noqa: F841
            oauth_callback_confirmed = user_external_dict.get("oauth_callback_confirmed", None)  # noqa: F841
            environment_id_old = user_external_dict.get("environment_id_old", None)  # noqa: F841

        user_external_id_tuple = self.user_external.select_one_tuple_by_where(select_clause_value="user_external_id",
                                                                              where="username=%s AND system_id=%s",
                                                                              params=(contact_email_address, system_id),
                                                                              order_by="start_timestamp DESC")
        if not user_external_id_tuple:
            user_external_id = None
        else:
            user_external_id = user_external_id_tuple[0]

        if not user_external_id:
            if not access_token:
                logger.warning(exception_message="access_token is None")
                logger.end(object={"contact_user_external_id": None})
                return None
            # create new user_external and add it to user_external_table
            logger.info(log_message="user_external_id is None, creating new user_external")
            # TODO: when ready, use the minsert method that returns the id
            self.user_external.insert_or_update_user_external_access_token(username=contact_email_address,
                                                                           profile_id=profile_id,
                                                                           system_id=system_id,
                                                                           access_token=access_token,
                                                                           expiry=expiry,
                                                                           refresh_token=refresh_token)
            # TODO: when ready, use the minsert method that returns the id
            user_external_id_tuple = self.user_external.select_one_tuple_by_where(select_clause_value="user_external_id",
                                                                                  where="username=%s AND system_id=%s",
                                                                                  params=(contact_email_address, system_id),
                                                                                  order_by="start_timestamp DESC")
            if not user_external_id_tuple:
                logger.exception(exception_message="user_external_id_tuple is None")
                raise Exception("user_external_id_tuple is None")
            user_external_id = user_external_id_tuple[0]
            contact_user_external_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                           entity_name2=self.default_entity_name2,
                                                           entity_id1=contact_id, entity_id2=user_external_id)
        else:
            # link to existing user_external
            logger.info(log_message="user_external_id is not None, linking to existing user_external")
            mapping_tuple = self.select_multi_mapping_tuple_by_id(entity_name1=self.default_entity_name1,
                                                                  entity_name2=self.default_entity_name2,
                                                                  entity_id1=contact_id, entity_id2=user_external_id)
            if not mapping_tuple:
                logger.info(log_message="mapping_tuple is None, creating new mapping")
                contact_user_external_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                               entity_name2=self.default_entity_name2,
                                                               entity_id1=contact_id, entity_id2=user_external_id)
            else:
                logger.info(log_message="mapping_tuple is not None")
                contact_user_external_id = mapping_tuple[0]

        logger.end(object={"contact_user_external_id": contact_user_external_id})
        return contact_user_external_id
