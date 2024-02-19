from .contact_profiles_local_constants import CONTACT_PROFILES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
from database_mysql_local.generic_mapping import GenericMapping
from profile_local.profiles_local import ProfilesLocal
from contact_persons_local.contact_persons_local import ContactPersonsLocal
from language_remote.lang_code import LangCode
from logger_local.Logger import Logger
from user_context_remote.user_context import UserContext

DEFAULT_SCHEMA_NAME = "contact_profile"
DEFAULT_ENTITY_NAME1 = "contact"
DEFAULT_ENTITY_NAME2 = "profile"
DEFAULT_ID_COLUMN_NAME = "contact_profile_id"
DEFAULT_TABLE_NAME = "contact_profile_table"
DEFAULT_VIEW_TABLE_NAME = "contact_profile_view"

logger = Logger.create_logger(object=CONTACT_PROFILES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

user_context = UserContext.login_using_user_identification_and_password()


class ContactProfilesLocal(GenericMapping):
    def __init__(self, default_schema_name: str = DEFAULT_SCHEMA_NAME, default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2, default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_table_name: str = DEFAULT_TABLE_NAME, default_view_table_name: str = DEFAULT_VIEW_TABLE_NAME,
                 lang_code: LangCode = None, is_test_data: bool = False) -> None:

        super().__init__(default_schema_name=default_schema_name, default_entity_name1=default_entity_name1,
                         default_entity_name2=default_entity_name2, default_id_column_name=default_id_column_name,
                         default_table_name=default_table_name, default_view_table_name=default_view_table_name,
                         is_test_data=is_test_data)
        self.profiles_local = ProfilesLocal()
        self.lang_code = lang_code or user_context.get_effective_profile_preferred_lang_code()

    def insert_and_link_contact_profile(self, contact_dict: dict,
                                        contact_id: int, visibility_id: int = 0,
                                        is_approved: int = 1, stars: int = 0,
                                        last_dialog_workflow_state_id: int = 1) -> int:
        """
        Insert contact and link to existing or new email address
        :param contact_dict: contact_dict
        :param contact_email_address: contact_email_address
        :param contact_id: contact_id
        :return: contact_id
        """
        logger.start(object={"contact_dict": contact_dict, "contact_id": contact_id})
        contact_persons_local = ContactPersonsLocal()
        person_ids = contact_persons_local.get_person_ids_by_contact_id(
            contact_id=contact_id,
            limit=1,
            order_by="contact_person_id DESC"
        )
        person_id = None
        profile_id_tuple = None
        if person_ids:
            person_id = person_ids[0]
            profile_id_tuple = self.profiles_local.select_one_tuple_by_id(
                select_clause_value="profile_id",
                id_column_name="person_id",
                id_column_value=person_id
            )
        if not profile_id_tuple:
            # Create a new  profile and add it to profile_table and profile_ml_table
            logger.info(log_message="profile_id is None, creating a new profile and adding it to"
                        " profile_table and profile_ml_table")
            profile_dict = {
                "person_id": person_id,
                "name": contact_dict.get("display_as"),
                "lang_code": self.lang_code.value,
                "visibility_id": visibility_id,
                "is_approved": is_approved,
                "stars": stars,
                "last_dialog_workflow_state_id": last_dialog_workflow_state_id
            }
            profile_id = self.profiles_local.insert(person_id=person_id, profile_dict=profile_dict)
            if not profile_id:
                logger.error(log_message="profile was not created and inserted to the database, profile_id is None")
                return None
            logger.info(log_message="profile was created and inserted to the database")
            logger.info(log_message="Linking contact to profile")
            contact_profile_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                     entity_name2=self.default_entity_name2,
                                                     entity_id1=contact_id, entity_id2=profile_id)
            if not contact_profile_id:
                logger.error(log_message="contact was not linked to profile, contact_profile_id is None")
                return None
            logger.info(log_message="contact was linked to profile")
        else:
            # Check if there is link to existing profile
            logger.info(log_message="Checking if there is link to existing profile")
            profile_id = profile_id_tuple[0]
            mapping_tuple_list = self.select_multi_mapping_tuple_by_id(entity_name1=self.default_entity_name1,
                                                                       entity_name2=self.default_entity_name2,
                                                                       entity_id1=contact_id,
                                                                       entity_id2=profile_id)
            if not mapping_tuple_list:
                # Link contact to existing profile
                logger.info(log_message="Linking contact to existing profile")
                contact_profile_id = self.insert_mapping(entity_name1=self.default_entity_name1,
                                                         entity_name2=self.default_entity_name2,
                                                         entity_id1=contact_id, entity_id2=profile_id)
            else:
                logger.info(log_message="contact is already linked to profile")
                contact_profile_id = mapping_tuple_list[0][0]
        logger.end(object={"contact_profile_id": contact_profile_id})
        return contact_profile_id
