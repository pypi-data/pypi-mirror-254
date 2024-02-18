from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.LoggerLocal import Logger
from user_context_remote.user_context import UserContext

IMPORTER_LOCAL_PYTHON_COMPONENT_ID = 114
IMPORTER_LOCAL_PYTHON_COMPONENT_NAME = 'importer-local-python-package'

logger_code_init = {
    'component_id': IMPORTER_LOCAL_PYTHON_COMPONENT_ID,
    'component_name': IMPORTER_LOCAL_PYTHON_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': 'idan.a@circlez.ai'
}
logger = Logger.create_logger(object=logger_code_init)


class ImportersLocal(GenericCRUD):
    def __init__(self):
        super().__init__(default_schema_name="importer", default_table_name="importer_table",
                         default_view_table_name="importer_view", default_id_column_name="importer_id")
        self.user = UserContext()

    def insert(self, data_source_id: int, location_id: int, entity_type_id: int, entity_id: int, url: str,
               user_external_id: int) -> int:
        # TODO Can we have data type for url which is not str?
        #   (like what?)
        object1 = {
            'data_source_id': data_source_id,
            'location_id': location_id,
            'entity_type_name': entity_type_id,
            'entity_id': entity_id,
            'url': url,
            'user_external_id': user_external_id
        }
        logger.start(object=object1)
        try:
            country_id = self._get_country(location_id)
            data_json = {
                "data_source_id": data_source_id,
                "external_user_country_id_old": country_id,
                "entity_type_id": entity_type_id,
                "entity_id": entity_id,
                "url": url,
                "created_user_id": self.user.get_effective_user_id(),
                "user_external_id": user_external_id,
            }
            importer_id = super().insert(data_json=data_json)
            if not importer_id:
                logger.error("insert importer record failed", object={'data_json': data_json})
                raise Exception("insert importer record failed with data_json: " + str(data_json))

            logger.end("add importer record succeeded", object={'importer_id': importer_id})
            return importer_id
        except Exception as e:
            logger.exception(object=e)
            raise

    def _get_country(self, location_id):
        return super().select_one_tuple_by_id(schema_name="location", view_table_name="location_view",
                                              id_column_name="location_id", id_column_value=location_id,
                                              select_clause_value="country_id")[0]
