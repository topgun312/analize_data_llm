from parser.import_data import df_sql

import asyncpg
from loguru import logger

from config_data.config import DB_NAME, HOST, PASSWORD, PORT, USER_DB


async def insert_data_from_df_to_sql() -> None:
    """
    Функция для загрузки данных с .csv файла в БД
    """
    try:
        engine = await asyncpg.connect(
            user=USER_DB, password=PASSWORD, database=DB_NAME, host=HOST, port=PORT
        )

        tuples: list[tuple] = [tuple(x) for x in df_sql.values]

        await engine.copy_records_to_table(
            "freelancer_earnings_table",
            records=tuples,
            columns=list(df_sql.columns),
            timeout=10,
        )
    except Exception as ex:
        logger.error(f"Ошибка загрузки данных с .csv файла в БД: {ex}")
