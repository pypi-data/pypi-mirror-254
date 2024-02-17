from fastapi import status
from fastapi.exceptions import HTTPException
from lapa_database_helper.main import LAPADatabaseHelper

from lapa_file_store.configuration import global_object_square_logger

local_object_lapa_database_helper = LAPADatabaseHelper()


def create_entry_in_file_store(
    file_name_with_extention: str,
    content_type: str,
    system_file_name_with_extension: str,
    file_storage_token: str,
    file_purpose: str,
    system_relative_path: str,
):
    try:
        database_name = "file_storage"
        schema_name = "public"
        table_name = "file"

        data = [
            {
                "file_name_with_extension": file_name_with_extention,
                "file_content_type": content_type,
                "file_system_file_name_with_extension": system_file_name_with_extension,
                "file_system_relative_path": system_relative_path,
                "file_storage_token": file_storage_token,
                "file_purpose": file_purpose,
            }
        ]

        response = local_object_lapa_database_helper.insert_rows(
            data, database_name, schema_name, table_name
        )

        return response
    except Exception as e:
        raise e


def get_file_row(file_storage_token):
    try:
        database_name = "file_storage"
        schema_name = "public"
        table_name = "file"

        filters = {"file_storage_token": file_storage_token}

        response = local_object_lapa_database_helper.get_rows(
            filters,
            database_name,
            schema_name,
            table_name,
            ignore_filters_and_get_all=False,
        )
        if isinstance(response, list) and len(response) == 1 and response[0]:
            return response[0]
        elif len(response) > 1:
            global_object_square_logger.logger.warning(
                f"Multiple files with same file_storage_token: {file_storage_token}"
            )

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"incorrect file_storage_token:{file_storage_token}",
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"incorrect file_storage_token:{file_storage_token}",
            )

    except Exception as e:
        raise e
