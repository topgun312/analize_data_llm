import base64

from gigachat import GigaChat
from gigachat.models import ChatCompletion
from loguru import logger

from config_data.config import CLIENT_ID, SECRET, columns_and_types

credentials = f"{CLIENT_ID}:{SECRET}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()


class GigaChatApi:

    @staticmethod
    def create_gigachat():
        giga = GigaChat(
            credentials=f"{encoded_credentials}",
            scope="GIGACHAT_API_PERS",
            model="GigaChat",
            verify_ssl_certs=False,
        )
        return giga

    def sql_query_prompt(self, query: str) -> str | None:
        """
        Метод класса для работы с запросами к SQL базе данных
        """
        try:
            giga = self.create_gigachat()
            result: ChatCompletion = giga.chat(
                f"У меня есть таблица - freelancer_earnings_table в бд postgresql. "
                f"{columns_and_types}"
                f"НАПИШИ МНЕ один SQL ЗАПРОС К БД БЕЗ пояснения, БЕЗ комментариев и БЕЗ примеров, просто сырой запрос, если запросов несколько объединить их в один запрос - {query}"
            )

            answer: str = result.choices[0].message.content
            return answer
        except Exception as ex:
            logger.error(f"Ошибка получения данных sql_query_prompt: Х{ex}")
            return None
