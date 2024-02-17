import os
import urllib.parse
from typing import BinaryIO

import requests
from kiss_headers import parse_it

from lapa_file_store_helper.configuration import (
    config_int_lapa_file_store_port,
    config_str_lapa_file_store_ip,
    config_str_lapa_file_store_protocol,
)


class LAPAFileStoreHelper:
    def __init__(self):
        try:
            self.global_str_lapa_file_store_url_base = (
                f"{config_str_lapa_file_store_protocol}://"
                f"{config_str_lapa_file_store_ip}:{config_int_lapa_file_store_port}"
            )
        except Exception:
            raise

    def upload_file_using_file_path(
        self,
        file_path: str,
        file_purpose: str | None = None,
        system_relative_path: str = "others/misc",
    ):
        try:
            endpoint = "upload_file"
            payload = {
                "file_purpose": file_purpose,
                "system_relative_path": system_relative_path,
            }
            with open(file_path, "rb") as file:
                files = {"file": (file_path, file, "multipart/form-data")}
                response = requests.post(
                    self.global_str_lapa_file_store_url_base + "/" + endpoint,
                    files=files,
                    data=payload,
                ).json()
            return response

        except Exception:
            raise

    def upload_file_using_binary_io(
        self,
        file: BinaryIO,
        file_purpose: str | None = None,
        system_relative_path: str = "others/misc",
    ):
        try:
            endpoint = "upload_file"
            payload = {
                "file_purpose": file_purpose,
                "system_relative_path": system_relative_path,
            }

            files = {"file": (file.name, file, "multipart/form-data")}
            response = requests.post(
                self.global_str_lapa_file_store_url_base + "/" + endpoint,
                files=files,
                data=payload,
            ).json()

            return response

        except Exception:
            raise

    def download_file(self, file_storage_token: str, output_folder_path: str) -> str:
        """
        :param file_storage_token:
        :param output_folder_path:
        :return: filepath
        """
        try:
            endpoint = "download_file"
            payload = {
                "file_storage_token": file_storage_token,
            }

            response = requests.get(
                self.global_str_lapa_file_store_url_base + "/" + endpoint,
                params=payload,
            )
            if not os.path.exists(output_folder_path):
                os.mkdir(output_folder_path)

            headers = parse_it(response)
            if headers.content_disposition.has("filename*"):
                file_name = urllib.parse.unquote(
                    headers.content_disposition["filename*"][7:]
                )
            elif headers.content_disposition.has("filename"):
                file_name = headers.content_disposition["filename"]
            else:
                raise Exception(
                    f"unable to download file - not able to get file name. headers: {headers}",
                )

            downloaded_file_path = output_folder_path + os.sep + file_name
            with open(downloaded_file_path, "wb") as file:
                file.write(response.content)

            return downloaded_file_path

        except Exception:
            raise
