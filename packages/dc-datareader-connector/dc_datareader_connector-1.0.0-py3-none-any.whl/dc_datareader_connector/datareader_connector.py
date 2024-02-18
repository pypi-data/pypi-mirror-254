from typing import Tuple, Union
from mimetypes import MimeTypes
import json
# import logging  ##
import sys  ##
# import pandas as pd
import traceback
import ntpath
import requests
import os
import time
from utils.constants import MAX_ATTEMPS
from utils.utils import get_json
from utils.fields_filter import df_merged_build, build_json

# _logger = logging.getLogger("Add Fields")


class DatareaderConnector:
    """_summary_"""

    def __init__(self, logger=object) -> None:
        """Allows you to interact with the datareader API

        Args:
            base_url (str): _description_
            logger (_type_, optional): _description_. Defaults to object.
        """
        self._logger = logger
        # self._base_url = "https://datareader-edge-20-qa.c3xsrv.com/api"
        # self._api_user = "calyx"
        # self._api_pass = "c4lyx"
        self._base_url = os.getenv("BASE_URL_API_DATAREADER")
        self._api_user = os.getenv("USER_API_DATAREADER")
        self._api_pass = os.getenv("PASSWORD_API_DATAREADER")
        self._token = "0"

    def auth(self) -> None:
        """It authenticates itself in the API and generates the token

        Args:
            user (str): _description_
            password (str): _description_

        Raises:
            ex: _description_
        """
        try:
            attemps = 0
            while attemps < MAX_ATTEMPS:
                header = {"Content-Type": "application/json"}

                payload = json.dumps({"username": self._api_user, "password": self._api_pass})

                self._logger.info("Realizando autenticacion con API.")

                session = requests.Session()
                session.max_redirects = 60
                api_url = self._base_url.replace("api", "")
                session.get(api_url)

                response = session.post(f"{self._base_url}/auth", headers=header, data=payload)

                if response.status_code == 200:
                    message = json.loads(response.text)
                    self._token = message["token"]
                    self._logger.info("Autenticacion realizada con exito.")
                    break
                else:
                    self._logger.info(f"Error {response.status_code}. Se intentara nuevamente")
                    time.sleep(5)
                    attemps += 1

        except Exception as ex:
            self._logger.error("Ocurrio un error al intentar obtener el token.")
            raise ex

    def recognize(self, comprobante_path: str) -> Tuple[Union[None, dict], Union[bool, str]]:
        """Given a pdf file, it recognizes the text and extracts the metadata.
        If the file is processed OK, it saves it in the processed files folder,
        otherwise it saves them in the unprocessed folder.

        Args:
            comprobante_path (str): _description_

        Returns:
            Tuple[Union[None, dict], Union[bool, str]]: _description_
        """
        try:
            attemps = 0
            while attemps < MAX_ATTEMPS:
                json_data = None
                message_error = False
                file_name = ntpath.basename(comprobante_path)
                self._logger.info((f"Procesando archivo {file_name}. "))

                with open(comprobante_path, "rb") as a_file:
                    mime = MimeTypes()
                    mime_type = mime.guess_type(comprobante_path)[0]
                    file_dict = {"filedata": (file_name, a_file, mime_type)}
                    headers = {"Authorization": f"Bearer {self._token}"}

                    response_respuesta = requests.post(
                        f"{self._base_url}/recognize/", headers=headers, files=file_dict
                    )

                    if response_respuesta.status_code == requests.codes.ok:
                        self._logger.info("Respuesta Ok.")
                        json_data = json.loads(response_respuesta.text)
                        break
                    elif response_respuesta.status_code == 403:
                        self._logger.info(
                            f"Error de autenticacion. Se intentara de nuevo archivo: {file_name}"
                        )
                        self.auth()
                        attemps += 1
                    elif response_respuesta.status_code == 422:
                        self._logger.info(
                            f"Error de autenticacion. Se intentara de nuevo archivo: {file_name}"
                        )
                        self.auth()
                        attemps += 1
                    elif response_respuesta.status_code == 500:
                        message_error = "Error 500"
                        self._logger.error("Error: 500. Internal Server Error")
                        json_data = get_json("/code/app/utils/json_templates/empty_response.json")
                        break
                    elif response_respuesta.status_code == 502:
                        message_error = "Error 502"
                        self._logger.error("Error: 502. Bad gateway")
                        json_data = get_json("/code/app/utils/json_templates/empty_response.json")
                        break
                    elif response_respuesta.status_code == 504:
                        self._logger.error("Error: 504 Gateway Time-out")
                        time.sleep(5)
                        self.auth()
                        attemps += 1
                    elif response_respuesta.status_code == 422:
                        self._logger.error("Error: 422 Not enough segments")
                        json_data = get_json("/code/app/utils/json_templates/empty_response.json")
                        break
                    else:
                        if response_respuesta.status_code == 503:
                            self._logger.error("Error: 503 Service Temporarily Unavailable")
                            time.sleep(5)
                            session = requests.Session()
                            session.max_redirects = 60
                            api_url = self._base_url.replace("api", "")
                            session.get(api_url)
                        else:
                            message_error = "Max Tries Reach"
                            self._logger.error(
                                f"Error:{response_respuesta.status_code}. {response_respuesta.text}"
                            )
                        self._logger.error("Se intentara de nuevo")
                        attemps += 1
                    if attemps == MAX_ATTEMPS:
                        self._logger.error("NO SE PUDO PROCESAR EL ARCHIVO. Fin de Intentos")
                        json_data = get_json("/code/app/utils/json_templates/empty_response.json")
                        break

        except Exception:
            message_error = f"{file_name}"
            self._logger.error(f"error: {traceback.format_exc()}")

        return [json_data, message_error]

    def build_field_filter(self, oc_df, prov_df, merge_column, rename_column):
        df_merged = df_merged_build(oc_df, prov_df, merge_column, rename_column, self._logger)
        return df_merged

    def build_json_to_input(self, merged_df, group_column, value_column, name_field, value_field):
        json_to_input = build_json(
            merged_df,
            group_column,
            value_column,
            name_field,
            value_field,
            self._logger,
        )
        return json_to_input

    def field_filter_create(self, json_to_field_filter, reference, values):
        try:
            attemps = 0
            for data in json_to_field_filter:
                payload = json.dumps(
                    {
                        "field_name": f"{reference}: {data[reference]}",
                        "field_value": f"{values}: {data[values]}",
                    }
                )
                while attemps < MAX_ATTEMPS:
                    headers = {
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self._token}",
                    }
                    self._logger.info("Cargando informacion a la tabla fields_filter.")

                    response = requests.post(
                        f"{self._base_url}/field/", headers=headers, data=payload
                    )

                    if response.status_code == 200:
                        self._logger.info(
                            f"Registro {reference} {data[reference]} cargado con exito."
                        )
                        break
                    else:
                        self._logger.info(f"Error {response.status_code}.")
                        if response.json()["detail"] == "Field filter already registered":
                            break
                        time.sleep(5)
                        self.auth()
                        attemps += 1

        except Exception as ex:
            self._logger.error("Ocurrio un error en la carga de Fields Filter.")
            raise ex

    def field_filter_delete_by_user(self):
        try:
            attemps = 0
            while attemps < MAX_ATTEMPS:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self._token}",
                }
                self._logger.info("Eliminando informacion de la tabla fields_filter.")

                response = requests.post(f"{self._base_url}/field/delete_by_user", headers=headers)

                if response.status_code == 200:
                    self._logger.info(f"Eliminado registros en field filters")
                    break
                else:
                    self._logger.info(f"Error {response.status_code}. Se intentara nuevamente")
                    time.sleep(5)
                    self.auth()
                    attemps += 1

        except Exception as ex:
            self._logger.error("Ocurrio un error en la eliminacion de Fields Filter.")
            raise ex



# df = DatareaderConnector(_logger)

# path_pas_df = r"C:\Users\romanoezequiel\Desktop\Repos\SUBMODULOS\datareader-submodule-dc_connector\Pasivo transitorio oc.xlsx"

# path_prov_df = r"C:\Users\romanoezequiel\Desktop\Repos\SUBMODULOS\datareader-submodule-dc_connector\Proveedores.xlsx"

# pas_df = pd.read_excel(path_pas_df, skiprows=0, sheet_name=0)

# prov_df = pd.read_excel(path_prov_df, skiprows=2, sheet_name=0)

# column_to_merge = "Proveedor"
# column_to_rename = "Acreedor"

# column_group_by_base = "Rut"
# column_group_values = "Pedido"

# field_name = "cuit"
# field_value = "purchase_order"

# df.auth()

# df_merged = df.build_field_filter(pas_df, prov_df, column_to_merge, column_to_rename)

# json_to_field_filter = df.build_json_to_input(
#     df_merged, column_group_by_base, column_group_values, field_name, field_value
# )

# charge = df.field_filter_create(json_to_field_filter, field_name, field_value)