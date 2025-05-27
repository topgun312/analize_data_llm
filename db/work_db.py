import asyncio

import asyncpg
from loguru import logger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from config_data.config import DATABASE, DB_NAME, DB_URL, HOST, PASSWORD, PORT, USER_DB
from db.models import Base


class DBWork:
    def __init__(self):
        self.engine = create_async_engine(
            url=DB_URL,
            echo=False,
            future=True,
            pool_size=50,
            max_overflow=100,
        )

    @staticmethod
    async def create_database() -> None:
        """
        Метод класса для создания БД
        """
        try:
            engine_create = await asyncpg.connect(
                user=USER_DB, password=PASSWORD, database=DATABASE, host=HOST, port=PORT
            )
            await engine_create.execute(f"CREATE DATABASE {DB_NAME}")
            logger.info(f"База данных {DB_NAME} успешно создана")
        except Exception as ex:
            logger.error(f"Ошибка создания БД: {ex}")

    async def create_table(self) -> None:
        """
        Метод класса для создания таблицы БД
        """
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.drop_all)
                await conn.run_sync(Base.metadata.create_all)
                logger.info(f"Таблица в БД успешно создана")
        except Exception as ex:
            logger.error(f"Ошибка удаления и создания таблиц в БД: {ex}")

    async def create_db_and_table(self) -> None:
        """
        Общий метод класса для создания БД и таблиц
        """
        try:
            await self.create_database()
            await asyncio.sleep(1)
            await self.create_table()
        except Exception as ex:
            logger.error(f"Ошибка общей функции для создания БД и таблиц: {ex}")

    async def execute_query(self, query: str) -> str | None:
        """
        Метод класса для запросов к БД
        """
        try:
            async with self.engine.begin() as conn:
                res = await conn.execute(text(query))
                res_list = res.scalars().all()
                result = ", ".join(
                    [str(i) if i is not None else "Нет данных" for i in res_list]
                )
                return result
        except Exception as ex:
            logger.error(f"Ошибка запросов к бд: {ex}")
            return None
