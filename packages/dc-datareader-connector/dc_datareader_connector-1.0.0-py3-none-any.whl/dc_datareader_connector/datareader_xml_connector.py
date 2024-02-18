from typing import Tuple, Union
from mimetypes import MimeTypes
import json
import traceback
import ntpath
import requests
import os
import time
from .utils.utils import MAX_ATTEMPS


class DatareaderXMLConnector:
    def __init__(self, logger=object) -> None:
        self._logger = logger
        self._base_url = os.getenv("URL_API_DATAREADER_CHILE")
        self._token = ""
        self._api_user = os.getenv("USER_API_DATAREADER")
        self._api_pass = os.getenv("PASSWORD_API_DATAREADER")

    def auth(self) -> None:
        """It authenticates itself in the API and generates the token"""
        try:
            attemps = 0
            while attemps < MAX_ATTEMPS:
                header = {"Content-Type": "application/json"}

                payload = json.dumps({"username": self._api_user, "password": self._api_pass})

                self._logger.info("Realizando autenticacion con API.")
                session = requests.Session()
                session.max_redirects = 60
                api_url = self._base_url.replace("docs", "")
                session.get(api_url)

                response = session.post(f"{self._base_url}/auth", headers=header, data=payload)

                if response.status_code == 200:
                    message = json.loads(response.text)
                    self._token = message["access_token"]
                    self._logger.info("Autenticacion realizada con exito.")
                    break
                else:
                    self._logger.info("Error en autenticacion")
                    self._logger.info(f"Error {response.status_code}")
                    time.sleep(5)
                    attemps += 1
                    if attemps == MAX_ATTEMPS:
                        self._logger.error("NO SE PUDO LOGUEAR EN API XML. Fin de Intentos")
                        break

        except Exception as ex:
            raise ex

    def recognize(
        self, comprobante_path: str, fields: list, empty_response: list
    ) -> Tuple[Union[None, dict], Union[bool, str]]:
        """Given a xml file, it recognizes the text
        If the file is processed OK, it saves it in the processed files folder,
        otherwise it saves them in the unprocessed folder."""
        try:
            attemps = 0
            invoice_data = empty_response
            message_error = False
            nombre_archivo = ntpath.basename(comprobante_path)
            while attemps < MAX_ATTEMPS:
                self._logger.info((f"Procesando archivo {nombre_archivo}. "))

                with open(comprobante_path, "rb") as a_file:
                    mime = MimeTypes()
                    mime_type = mime.guess_type(comprobante_path)[0]
                    file_dict = {"filedata": (nombre_archivo, a_file, mime_type)}
                    headers = {"Authorization": f"Bearer {self._token}"}
                    params = {"xml_fields": fields}

                    response = requests.post(
                        f"{self._base_url_xml}/read_file",
                        headers=headers,
                        files=file_dict,
                        params=params,
                        timeout=500,
                    )

                    if response.status_code == requests.codes.ok:
                        self._logger.info(f"Respuesta Ok para {nombre_archivo}")
                        json_data = json.loads(response.text)
                        invoice_data = json_data
                        break

                    message_error = f"{nombre_archivo}"
                    self._logger.error(f"No se pudo procesar {nombre_archivo}. Request Error")
                    time.sleep(5)
                    self.auth_xml()
                    attemps += 1
                    if attemps == MAX_ATTEMPS:
                        self._logger.error("NO SE PUDO PROCESAR EL ARCHIVO. Fin de Intentos")
                        break

        except Exception:
            message_error = f"{nombre_archivo}"
            self._logger.error(
                (
                    "No se pudo extraer la informacion para "
                    f"{nombre_archivo} error: {traceback.format_exc()}"
                )
            )

        return invoice_data, message_error