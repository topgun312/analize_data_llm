import asyncio
import re
from parser.import_data import ImportData

from loguru import logger

from db.add_data_to_db import insert_data_from_df_to_sql
from db.work_db import DBWork
from llm_api.gigachat_api import GigaChatApi

load_data = ImportData()
giga_chat = GigaChatApi()
work_db = DBWork()

logger.add(
    "logs/logs_{time}.txt",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file}:{line} | {message}",
    level="DEBUG",
    colorize=True,
    rotation="08:00",
    compression="zip",
)


async def console_work() -> None:
    """
    Основная функция для управления скриптом
    """
    while True:
        try:
            action = int(
                input(
                    "Для работы с системой которая анализирует статистические данные о доходах фрилансеров выполните следующие действия: \n"
                    "1 - Скачайте данные о фрилансерах с сайта kaggle \n"
                    "2 - Создайте SQL БД и таблицу  \n"
                    "3 - Загрузите данные с .csv файла в БД \n"
                    "4 - Если выполнил три предыдущих пункта переходи непосредственно к запросам \n"
                )
            )
            if action == 1:
                await load_data.load_data_from_kaggle_api()
            elif action == 2:
                await work_db.create_db_and_table()
            elif action == 3:
                await insert_data_from_df_to_sql()
            elif action == 4:
                await send_query()
                break
            else:
                print("Введите число от 1 до 4 для корректной работы кошелька!")
                continue
        except ValueError:
            logger.error("Неверный ввод. Пожалуйста, введите числовое значение.")
        except asyncio.CancelledError:
            logger.info("Работа прервана пользователем.")
            break
        except Exception as ex:
            logger.error(f"Ошибка console_work: {ex}")


async def send_query() -> None:
    """
    Функция для управления запросами к gigachat
    """
    while True:
        try:
            action = int(
                input("Введите 1 чтоб задать вопрос или 2 для окончания работы: \n")
            )
            if action == 1:
                answer = input("Введите вопрос: ")
                query = giga_chat.sql_query_prompt(query=answer)
                cleaned_query = re.sub(r"```|sql|`", "", query).strip()
                result = await work_db.execute_query(query=cleaned_query)
                print(f"Ответ на ваш вопрос {answer} следующий: ", result)
            elif action == 2:
                break
            else:
                print("Введите число 1 для продолжения работы или 2 для выхода!")
                continue
        except ValueError:
            logger.error("Неверный ввод. Пожалуйста, введите числовое значение.")
        except asyncio.CancelledError:
            logger.info("Работа прервана пользователем.")
            break
        except Exception as ex:
            logger.error(f"Ошибка send_query: {ex}")


if __name__ == "__main__":
    asyncio.run(console_work())
