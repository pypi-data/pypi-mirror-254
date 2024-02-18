import mimetypes
import os
import uuid
from typing import Annotated

from fastapi import FastAPI, UploadFile, status, Form
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from uvicorn import run

from lapa_file_store.configuration import (
    config_int_host_port,
    config_str_host_ip,
    global_absolute_path_local_storage,
    global_object_square_logger,
    config_str_module_name
)
from lapa_file_store.utils.Helper import create_entry_in_file_store, get_file_row

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@global_object_square_logger.async_auto_logger
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"text": config_str_module_name}
    )


@app.post("/upload_file", status_code=status.HTTP_201_CREATED)
@global_object_square_logger.async_auto_logger
async def upload_file(
        file: UploadFile,
        file_purpose: Annotated[str, Form(title="Username", description="Specify the purpose of the file")] = None,
        system_relative_path: Annotated[str, Form(title="System relative path",
                                                  description="Specify the path using '/'. For e.g. home/user_document")] = "others/misc"
):
    try:
        file_bytes = await file.read()
        filename = file.filename
        content_type = file.content_type

        file_storage_token = str(uuid.uuid4())
        system_file_name = str(uuid.uuid4())
        file_extension = filename.rsplit(".", 1)[-1]
        system_file_name_with_extension = system_file_name + "." + file_extension
        response = create_entry_in_file_store(
            file_name_with_extention=filename,
            content_type=content_type,
            file_storage_token=file_storage_token,
            file_purpose=file_purpose,
            system_relative_path=system_relative_path,
            system_file_name_with_extension=system_file_name_with_extension,
        )

        # create folder
        system_absolute_path = os.path.join(
            global_absolute_path_local_storage,
            os.sep.join(system_relative_path.split("/")),
        )

        """
        Check if the path already exists or not
        If Yes --> Do not create directory in the OS
        If No --> Create directory in the OS
        """
        if os.path.exists(system_absolute_path):
            global_object_square_logger.logger.warning('Directory path already exists. Not creating the path again. '
                                                       f'Path - {str(system_absolute_path)}')
        else:
            os.makedirs(system_absolute_path)
            global_object_square_logger.logger.info('Directory created successfully. '
                                                    f'Path - {str(system_absolute_path)}')

        system_file_absolute_path = os.path.join(
            system_absolute_path, system_file_name_with_extension
        )
        with open(system_file_absolute_path, "wb") as file:
            file.write(file_bytes)

        # Check if the file exists
        if os.path.exists(system_file_absolute_path):
            # Additional information you want to include
            additional_info = {"FileStorageToken": response[0]["file_storage_token"]}

            # Return JSONResponse with file response and additional information
            return JSONResponse(content={"additional_info": additional_info})

        else:
            # Handle the case when the file does not exist
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.get("/download_file", status_code=status.HTTP_201_CREATED)
@global_object_square_logger.async_auto_logger
async def download_file(file_storage_token: str):
    try:
        local_dict_file_row = get_file_row(file_storage_token)
        local_string_system_absolute_file_path = os.path.join(
            global_absolute_path_local_storage,
            os.sep.join(local_dict_file_row["file_system_relative_path"].split("/")),
            local_dict_file_row["file_system_file_name_with_extension"],
        )
        # Get content type
        content_type, _ = mimetypes.guess_type(local_string_system_absolute_file_path)

        if local_string_system_absolute_file_path:
            return FileResponse(
                local_string_system_absolute_file_path,
                media_type=content_type,
                filename=local_dict_file_row["file_name_with_extension"],
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="File not found"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


if __name__ == "__main__":
    try:
        run(app, host=config_str_host_ip, port=config_int_host_port)
    except Exception as exc:
        global_object_square_logger.logger.critical(exc, exc_info=True)
