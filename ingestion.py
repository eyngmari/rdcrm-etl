import requests
import logging
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class DataRdCrmApi():
    def __init__(self, token: str) -> None:
        self.token = token
        self.base_endpoint = 'https://plugcrm.net/api'

    def _get_endpoint(self) -> str:
        return f'{self.base_endpoint}/v1/deals'

    def get_data(self, page: int = 1) -> dict:
        endpoint = self._get_endpoint()
        logger.info(f'Getting data from endpoint: {endpoint}')
        params = {
            "token": self.token,
            "page": page,
            "limit": 200
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()


class DataTypeNotSupportedForIngestionException(Exception):
    def __init__(self, data):
        self.data = data
        self.message = f'Data type {type(data)} in not supporte for ingestion'
        super().__init__(self.message)


class DataWrite:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def _write_row(self, row: str) -> None:
        with open(self.filename, 'a') as f:
            f.write(row)

    def write(self, data):
        if isinstance(data, dict):
            self._write_row(json.dumps(data) + '\n')
        elif isinstance(data, list):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestionException(data)
