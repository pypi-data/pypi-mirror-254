from typing import Optional
from database_mysql_local.generic_mapping import GenericMapping
from logger_local.Logger import Logger
import re
from urllib.parse import urlparse
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from .internet_domain_local_constants import INTERNET_DOMAIN_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
logger = Logger.create_logger(object=INTERNET_DOMAIN_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

# TODO Please use url_type_table to identify the type of the URL based on the prefix

# TODO Please mark all private methods as private using __

import re
from typing import Optional

INTERNET_DOMAIN_SCHEMA_NAME = "internet_domain"
INTERNET_DOMAIN_TABLE_NAME = "internet_domain_table"
INTERNET_DOMAIN_VIEW_NAME = "internet_domain_view"
DEFAULT_ID_COLUMN_NAME = "internet_domain_id"
DEFAULT_ENTITY_NAME1 = "contact"
DEFAULT_ENTITY_NAME2 = "internet_domain"

class DomainLocal(GenericMapping):
    """
    DomainLocal is a class that uses regular expressions to parse URLs and extract components.
    """

    def __init__(self, default_schema_name: str = INTERNET_DOMAIN_SCHEMA_NAME,
                 default_table_name: str = INTERNET_DOMAIN_TABLE_NAME,
                 default_view_table_name: str = INTERNET_DOMAIN_VIEW_NAME,
                 default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2,
                 is_test_data: bool = False):
        self.domain_regex = re.compile(r'^(?:http[s]?://)?(?:www\.)?([^:/\s]+)')
        self.organization_regex = re.compile(r'^(?:http[s]?://)?(?:www\.)?([^\.]+)\.')
        self.username_regex = re.compile(r'^http[s]?://(?:([^:/\s]+)@)?')
        self.tld_regex = re.compile(r'^(?:http[s]?://)?(?:www\.)?[^\.]+\.(.*?)(?:/|$)')

        super().__init__(default_schema_name=default_schema_name,
                         default_table_name=default_table_name, default_view_table_name=default_view_table_name,
                         default_id_column_name=default_id_column_name, default_entity_name1=default_entity_name1,
                         default_entity_name2=default_entity_name2, is_test_data=is_test_data)


    def get_domain_name(self, url: str) -> Optional[str]:
        """
        Extracts the domain name from a URL.
        """
        if not self.valid_url(url):
            return None
        match = self.domain_regex.search(url)
        if match:
            return match.group(1)
        return None

    def get_organization_name(self, url: str) -> Optional[str]:
        """
        Extracts the organization name from a URL.
        """
        if not self.valid_url(url):
            return None
        match = self.organization_regex.search(url)
        if match:
            return match.group(1)
        return None

    def get_username(self, url: str) -> Optional[str]:
        """
        Extracts the username from a URL.
        """
        if not self.valid_url(url):
            return None
        match = self.username_regex.search(url)
        if match:
            return match.group(1)
        return None

    def get_tld(self, url: str) -> Optional[str]:
        """
        Extracts the top-level domain (TLD) from a URL.
        """
        if not self.valid_url(url):
            return None
        match = self.tld_regex.search(url)
        if match:
            return match.group(1)
        return None

    def valid_url(self, url: str) -> bool:
        """
        Validates the URL format.
        """
        return re.match(r'^http[s]?://', url) is not None

    def is_commercial_domain(self, url: str) -> bool:
        """
        Checks if the domain of a URL is a commercial domain (.com).
        """
        tld = self.get_tld(url)
        return tld == 'com'
    

    def link_contact_to_domain(self, contact_id: int, url: str) -> dict:
        """
        Links a contact to a domain.
        Returns a dictionary containing the following information:
        - contact_id
        - url
        - profile_id
        - internet_domain_id
        - contact_internet_domain_id
        """
        logger.start("link_contact_to_domain", object={
                     'contact_id': contact_id, 'url': url})
        try:
            full_domain_name = self.get_domain_name(url)
            tld = self.get_tld(url)
            is_commercial_webmain = self.is_commercial_domain(url)
            if not full_domain_name or not tld:
                logger.error(log_message="domain was not extracted successfully from url")
                logger.end(object={"insert_information": {}})
                return {}
            data_to_insert = {
                'domain': full_domain_name,
                'top_level_domain': tld,
                'profile_id': logger.user_context.get_effective_profile_id(),
                'is_commercial_webmain': is_commercial_webmain
            }
            # check if the domain already exists in the database
            self.set_schema(schema_name='internet_domain')
            internet_domain_id = self.select_one_tuple_by_id(
                select_clause_value='internet_domain_id',
                id_column_name='domain',
                id_column_value=full_domain_name,
            )
            if internet_domain_id:
                internet_domain_id = internet_domain_id[0]
            else:
                internet_domain_id = self.insert(
                    table_name='internet_domain_table', data_json=data_to_insert, ignore_duplicate=True)
            self.set_schema(schema_name='contact_internet_domain')
            # link the contact to the domain
            contact_internet_domain_id = self.insert_mapping(
                entity_id1=contact_id, entity_id2=internet_domain_id,
                ignore_duplicate=True
            )
        except Exception as e:
            logger.error("link_contact_to_domain", object={
                         'contact_id': contact_id, 'url': url}, data=e)
            raise e
        insert_information = {
            'contact_id': contact_id,
            'url': url,
            'profile_id': logger.user_context.get_effective_profile_id(),
            'internet_domain_id': internet_domain_id,
            'contact_internet_domain_id': contact_internet_domain_id
        }
        logger.end("link_contact_to_domain", object={
                   'contact_internet_domain_id': contact_internet_domain_id})
        return insert_information
