import os
import zipfile
from urllib.error import HTTPError, URLError
from urllib.parse import ParseResult, parse_qs, urlparse

import aiofiles
import aiohttp
import pandas as pd
from loguru import logger

from config_data.config import DOWNLOAD_URL, KAGGLE_URL

data_path = "freelancer-data/freelancer_earnings_bd.csv"


class ImportData:

    @staticmethod
    async def download_file(
        session: aiohttp.ClientSession, url: str, dest: str
    ) -> None:
        """
        Функция для загрузки файла
        """
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    async with aiofiles.open(dest, "wb") as file:
                        await file.write(await response.read())
                else:
                    raise Exception(f"Ошибка загрузки файла: {response.status}")
        except aiohttp.ClientError as ex:
            logger.error(f"Ошибка клиента: {ex}")
        except aiohttp.HttpProcessingError as ex:
            logger.error(f"Ошибка обработки HTTP: {ex}")
        except Exception as ex:
            logger.error(f"Неизвестная ошибка download_file: {ex}")

    @staticmethod
    def get_dataset_and_filename_from_url(url: str) -> tuple[str, str] | None:
        """
        Функция для получения dataset и filename из url
        """
        try:
            parsed_url: ParseResult = urlparse(url)
            path: str = parsed_url.path
            dataset: str = path.replace("/datasets/", "")
            query_params: dict[str, list[str]] = parse_qs(parsed_url.query)
            filename: str = query_params.get("select", [None])[0]
            return dataset, filename
        except HTTPError as ex:
            logger.error(f"HTTP ошибка: {ex.code} - {ex.reason}")
            return None
        except URLError as ex:
            logger.error(f"Ошибка URL: {ex.reason}")
            return None
        except Exception as ex:
            logger.error(f"Неизвестная ошибка get_dataset_and_filename_from_url: {ex}")
            return None

    async def load_data_from_kaggle_api(self) -> None:
        """
        Функция для скачивания zip с файлами с сайта kaggle и его распаковки
        """
        try:
            filedir = "freelancer-data"
            dataset, filename = self.get_dataset_and_filename_from_url(url=KAGGLE_URL)
            if dataset is not None and filename is not None:
                os.makedirs(filedir, exist_ok=True)

                download_url: str = f"{DOWNLOAD_URL}/{dataset}"
                zip_path: str = f"{filedir}/freelancer-earnings-and-job-trends.zip"

                async with aiohttp.ClientSession() as session:
                    await self.download_file(session, download_url, zip_path)

                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extract(filename, filedir)
                logger.info("Данные в файл .csv успешно загружены!")
            else:
                logger.error(
                    f"В url {KAGGLE_URL} отсутствует корректная информация по dataset - {dataset}, filename - {filename}"
                )
        except Exception as ex:
            logger.error(f"Неизвестная ошибка load_data_from_kaggle_api(: {ex}")


df_sql = pd.read_csv(data_path)
df_sql.columns = df_sql.columns.str.lower()
