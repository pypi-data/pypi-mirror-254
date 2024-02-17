from typing import List, Dict

from database_mysql_local.generic_crud import GenericCRUD

from .contact import Contact
from .contact_constants import SCHEMA_NAME, TABLE_NAME, VIEW_TABLE_NAME, ID_COLUMN_NAME, logger
from .contact_local_extentions import (
    ContactBatchInsertionError,
    ContactDeletionError,
    ContactInsertionError,
    ContactObjectInsertionError,
    ContactUpdateError)


class ContactsLocal(GenericCRUD):

    def __init__(self, is_test_data: bool = False) -> None:
        super().__init__(
            default_schema_name=SCHEMA_NAME,
            default_table_name=TABLE_NAME,
            default_view_table_name=VIEW_TABLE_NAME,
            default_id_column_name=ID_COLUMN_NAME,
            is_test_data=is_test_data
        )

    def insert_contact_dict(self, contact_dict: dict) -> int:
        logger.start(object={'contact_to_insert': contact_dict})
        if not contact_dict:
            logger.error("contact_to_insert cannot be empty")
            logger.end()
            raise ContactInsertionError("contact_to_insert cannot be empty")

        first_name = contact_dict.get('first_name')
        last_name = contact_dict.get('last_name')
        # TODO EmailAddressesLocal.process_email( email )
        organization = contact_dict.get('organization')
        if not first_name and not last_name and not organization:
            logger.error(
                "contact_to_insert must have at least one of the following " +
                "fields: first_name, last_name, organization")
            logger.end()
            raise ContactInsertionError(
                "contact_to_insert must have at least one of the following" +
                "fields: first_name, last_name, organization")

        contact_id = None
        try:
            contact_json = {
                'owner_profile_id': contact_dict.get('owner_profile_id', None),
                'account_name': contact_dict.get('account_name', None),
                'person_id': contact_dict.get('person_id', None),
                'name_prefix': contact_dict.get('name_prefix', None),
                'first_name': contact_dict.get('first_name', None),
                'additional_name': contact_dict.get('additional_name', None),
                'last_name': contact_dict.get('last_name', None),
                'full_name': contact_dict.get('full_name', None),
                'name_suffix': contact_dict.get('name_suffix', None),
                'nickname': contact_dict.get('nickname', None),
                'display_as': contact_dict.get('display_as', None),
                'title': contact_dict.get('title', None),
                'organization': contact_dict.get('organization', None),
                'organization_profile_id': contact_dict.get('organization_profile_id', None),
                'job_title': contact_dict.get('job_title', None),
                'department': contact_dict.get('department', None),
                'notes': contact_dict.get('notes', None),
                'email1': contact_dict.get('email1', None),
                'email2': contact_dict.get('email2', None),
                'email3': contact_dict.get('email3', None),
                'phone1': contact_dict.get('phone1', None),
                'phone2': contact_dict.get('phone2', None),
                'phone3': contact_dict.get('phone3', None),
                'address1_street': contact_dict.get('address1_street', None),
                'address1_city': contact_dict.get('address1_city', None),
                'address1_state': contact_dict.get('address1_state', None),
                'address1_postal_code': contact_dict.get('address1_postal_code', None),
                'address1_country': contact_dict.get('address1_country', None),
                'address2_street': contact_dict.get('address2_street', None),
                'address2_city': contact_dict.get('address2_city', None),
                'address2_state': contact_dict.get('address2_state', None),
                'address2_postal_code': contact_dict.get('address2_postal_code', None),
                'address2_country': contact_dict.get('address2_country', None),
                'birthday': contact_dict.get('birthday', None),
                'day': contact_dict.get('day', None),
                'month': contact_dict.get('month', None),
                'year': contact_dict.get('year', None),
                'cira': contact_dict.get('cira', None),
                'anniversary': contact_dict.get('anniversary', None),
                'website1': contact_dict.get('website1', None),
                'website2': contact_dict.get('website2', None),
                'website3': contact_dict.get('website3', None),
                'photo_url': contact_dict.get('photo_url', None),
                'photo_file_name': contact_dict.get('photo_file_name', None),
                'source': contact_dict.get('source', None),
                'import_contact_id': contact_dict.get('import_contact_id', None),
                'created_user_id': contact_dict.get('created_user_id', 0),
            }
            if contact_dict.get('display_as', None) is None:
                contact_json['display_as'] = contact_dict.get(
                    'first_name', None)
                if contact_dict.get('last_name', None) is not None:
                    contact_json['display_as'] += " " + contact_dict.get('last_name', "")
            contact_id = self.insert(data_json=contact_json)
            logger.end("contact added", object={'contact_id': contact_id})
        except Exception as err:
            logger.error(f"Contact.insert Error: {err}, contact_id: {contact_id}", object=err)
            logger.end()
            raise ContactInsertionError("Error occurred while inserting contact." + str(err))

        return contact_id

    # TODO: Do we still need this method when we have update_contact_by_dict?
    def update(self, contact_id: int, person_id: int, name_prefix: str, first_name: str,
               additional_name: str, job_title: str) -> None:
        try:
            object1 = {
                'person_id': person_id,
                'name_prefix': name_prefix,
                'first_name': first_name,
                'additional_name': additional_name,
                'job_title': job_title,
                'contact_id': contact_id
            }
            logger.start(object=object1)
            contact_data = {
                'person_id': person_id,
                'name_prefix': name_prefix,
                'first_name': first_name,
                'additional_name': additional_name,
                'job_title': job_title,
                'contact_id': contact_id
            }
            self.update_by_id(id_column_name="contact_id", id_column_value=contact_id, data_json=contact_data)
            logger.end("contact updated", object={'contact_id': contact_id})
        except Exception as err:
            logger.error(f"Contact.update Error: {err}, contact_id: {contact_id}", object=err)
            logger.end()
            raise ContactUpdateError("Error occurred while updating contact." + str(err))

    def update_contact_by_dict(self, contact_id, contact_dict: dict) -> None:
        logger.start(object={'contact_dict': contact_dict})
        contact_json = {
            'owner_profile_id': contact_dict.get('owner_profile_id', None),
            'account_name': contact_dict.get('account_name', None),
            'person_id': contact_dict.get('person_id', None),
            'name_prefix': contact_dict.get('name_prefix', None),
            'first_name': contact_dict.get('first_name', None),
            'additional_name': contact_dict.get('additional_name', None),
            'last_name': contact_dict.get('last_name', None),
            'full_name': contact_dict.get('full_name', None),
            'name_suffix': contact_dict.get('name_suffix', None),
            'nickname': contact_dict.get('nickname', None),
            'display_as': contact_dict.get('display_as', None),
            'title': contact_dict.get('title', None),
            'organization': contact_dict.get('organization', None),
            'organization_profile_id': contact_dict.get('organization_profile_id', None),
            'job_title': contact_dict.get('job_title', None),
            'department': contact_dict.get('department', None),
            'notes': contact_dict.get('notes', None),
            'email1': contact_dict.get('email1', None),
            'email2': contact_dict.get('email2', None),
            'email3': contact_dict.get('email3', None),
            'phone1': contact_dict.get('phone1', None),
            'phone2': contact_dict.get('phone2', None),
            'phone3': contact_dict.get('phone3', None),
            'address1_street': contact_dict.get('address1_street', None),
            'address1_city': contact_dict.get('address1_city', None),
            'address1_state': contact_dict.get('address1_state', None),
            'address1_postal_code': contact_dict.get('address1_postal_code', None),
            'address1_country': contact_dict.get('address1_country', None),
            'address2_street': contact_dict.get('address2_street', None),
            'address2_city': contact_dict.get('address2_city', None),
            'address2_state': contact_dict.get('address2_state', None),
            'address2_postal_code': contact_dict.get('address2_postal_code', None),
            'address2_country': contact_dict.get('address2_country', None),
            'birthday': contact_dict.get('birthday', None),
            'day': contact_dict.get('day', None),
            'month': contact_dict.get('month', None),
            'year': contact_dict.get('year', None),
            'cira': contact_dict.get('cira', None),
            'anniversary': contact_dict.get('anniversary', None),
            'website1': contact_dict.get('website1', None),
            'website2': contact_dict.get('website2', None),
            'website3': contact_dict.get('website3', None),
            'photo_url': contact_dict.get('photo_url', None),
            'photo_file_name': contact_dict.get('photo_file_name', None),
            'source': contact_dict.get('source', None),
            'import_contact_id': contact_dict.get('import_contact_id', None),
            'created_user_id': contact_dict.get('created_user_id', 0),
        }
        if contact_dict.get('display_as', None) is None:
            contact_json['display_as'] = contact_dict.get(
                'first_name', None)
            if contact_dict.get('last_name', None) is not None:
                contact_json['display_as'] += " " + contact_dict.get('last_name', "")
        self.update_by_id(id_column_name="contact_id", id_column_value=contact_id,
                          data_json=contact_json)
        logger.end()

    def delete_by_contact_id(self, contact_id: any) -> None:
        try:
            logger.start(object={'contact_id': contact_id})
            self.delete_by_id(id_column_name="contact_id", id_column_value=contact_id)
            logger.end("contact deleted", object={'contact_id': contact_id})
        except Exception as err:
            logger.error(f"Contact.delete Error: {err}", object=err)
            # cursor.close()
            logger.end()
            raise ContactDeletionError("Error occurred while deleting contact." + str(err))

    def insert_update_contact(self, contact_dict: dict) -> int:
        logger.start(object={'contact_dict': contact_dict})
        if not contact_dict:
            logger.error("contact_dict cannot be empty")
            logger.end()
            raise ContactInsertionError("contact_dict cannot be empty")

        existing_contact_dict = None
        try:
            existing_contact_dict = self.get_existing_contact_dict(contact_dict)
            if existing_contact_dict:
                # If the contact exists, update it
                contact_id = existing_contact_dict.get('contact_id', None)
                self.update_contact_by_dict(contact_id=contact_id,
                                            contact_dict=contact_dict)
            else:
                # If the contact does not exist, insert it
                contact_id = self.insert_contact_dict(contact_dict)
        except Exception as e:
            logger.error(f"Failed to insert/update contact: {e}")
            logger.end()
            raise ContactInsertionError(f"Failed to insert/update contact: {e}")

        logger.end()
        return contact_id

    def insert_batch(self, contact_list: List[Dict]) -> List[int]:
        logger.start()
        inserted_ids = []
        try:
            for contact in contact_list:
                contact_id = self.insert_contact_dict(contact_dict=contact)
                inserted_ids.append(contact_id)
            logger.end("contacts added", object={'inserted_ids': inserted_ids})
        except Exception as err:
            inserted_ids_str = ",".join(str(x) for x in inserted_ids)
            logger.error(f"Contact.insert_batch Error: {err} " + inserted_ids_str, object=err)
            raise ContactBatchInsertionError("Error occurred while batch inserting contacts." + str(err))

        return inserted_ids

    def get_contact_by_contact_id(self, contact_id: int) -> dict:
        logger.start(object={'contact_id': contact_id})
        try:
            contact = self.select_one_dict_by_id(view_table_name=VIEW_TABLE_NAME,
                                                 id_column_name=ID_COLUMN_NAME, id_column_value=contact_id)
        except Exception as err:
            logger.error(
                f"Contact.get_contact_by_id Error: {err}", object=err)
            logger.end()
            raise
        return contact

    def insert_contact_object(self, contact: Contact) -> int:
        logger.start(object={'contact': contact})
        if not contact:
            logger.error("contact cannot be empty")
            logger.end()
            raise ContactBatchInsertionError("contact cannot be empty")

        required_fields = [
            'first_name', 'last_name', 'organization', 'job_title'
        ]
        if not any(getattr(contact, field, None) for field in required_fields):
            logger.error(
                "contact must have at least one of the following " +
                "fields: first_name, last_name, organization, job_title")
            logger.end()
            raise ContactObjectInsertionError(
                "contact must have at least one of the following" +
                "fields: first_name, last_name, organization, job_title")
        contact_id = None
        try:
            contact_json = vars(contact)
            if contact.display_as is None:
                display_name = contact.first_name
                if contact.last_name is not None:
                    display_name += " " + contact.last_name
                contact_json['display_as'] = display_name

            contact_id = self.insert(data_json=contact_json)
            logger.end("contact added", object={'contact_id': contact_id})
        except Exception as err:
            logger.error(f"Contact.insert Error: {err}, contact_id: {contact_id}", object=err)
            logger.end()
            raise ContactObjectInsertionError("Error occurred while inserting contact." + str(err))

        return contact_id

    # TODO: Change it to a more sophisticated method later
    def get_existing_contact_dict(self, contact_dict: dict) -> dict:
        logger.start(object={'contact_dict': contact_dict})

        existing_contact = self._check_if_phone_exists(contact_dict) or self._check_if_email_exists(contact_dict)

        logger.end(object={'existing_contact': existing_contact})
        return existing_contact

    def _check_if_phone_exists(self, contact_dict: dict) -> dict:
        phone1 = contact_dict.get('phone1')
        phone2 = contact_dict.get('phone2')
        phone3 = contact_dict.get('phone3')

        if phone1:
            return self._check_if_name_exists(contact_dict, 'phone1', phone1)
        elif phone2:
            return self._check_if_name_exists(contact_dict, 'phone2', phone2)
        elif phone3:
            return self._check_if_name_exists(contact_dict, 'phone3', phone3)

        return {}

    def _check_if_email_exists(self, contact_dict: dict) -> dict:
        email1 = contact_dict.get('email1')
        email2 = contact_dict.get('email2')
        email3 = contact_dict.get('email3')

        if email1:
            return self._check_if_name_exists(contact_dict, 'email1', email1)
        elif email2:
            return self._check_if_name_exists(contact_dict, 'email2', email2)
        elif email3:
            return self._check_if_name_exists(contact_dict, 'email3', email3)

        return {}

    def _check_if_name_exists(self, contact_dict: dict, id_column_name: str, id_column_value: str) -> dict:
        try:
            contact = self.select_one_dict_by_id(
                view_table_name=VIEW_TABLE_NAME,
                id_column_name=id_column_name,
                id_column_value=id_column_value
            )
        except Exception as err:
            logger.error(
                f"Contact._check_if_contact_exists Error: {err}", object=err)
            logger.end()
            raise

        if contact:
            # Check if existing contact's name is not equal to the new contact's name
            if contact.get('first_name') != contact_dict.get('first_name') or \
                    contact.get('last_name') != contact_dict.get('last_name'):
                # Warn about the different name
                logger.warning(
                    "Contact with the same phone number or email already exists but " +
                    "the name is different" + str(contact))
            return contact

        return {}

    def insert_contact(self, is_test_data: bool = False, **kwargs):
        data_json = {"is_test_data": is_test_data}
        data_json.update(kwargs)

        contact_id = self.insert(schema_name="contact", table_name="contact_table",
                                 data_json=data_json)
        return contact_id

    def get_test_contact_id(self) -> int:
        return self.get_test_entity_id(entity_name="contact",
                                       insert_function=self.insert_contact)
