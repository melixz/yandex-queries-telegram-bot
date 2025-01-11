import aiohttp
from datetime import datetime, timedelta
from core.config import YANDEX_API_KEY, YANDEX_HOST_ID, YANDEX_USER_ID

API_URL = "https://api.webmaster.yandex.net/v4"


async def get_top_queries(
    metric: str, limit: int = 10, query_indicator: str = None, device_type: str = "ALL"
):
    """
    Получает топ поисковых запросов из API Яндекс Вебмастера.
    :param metric: Метрика для сортировки (TOTAL_SHOWS, TOTAL_CLICKS).
    :param limit: Количество запросов (по умолчанию 10).
    :param query_indicator: Индикатор для фильтрации запросов (например, TOTAL_SHOWS или TOTAL_CLICKS).
    :param device_type: Тип устройства (ALL, DESKTOP, MOBILE_AND_TABLET, MOBILE, TABLET).
    :return: Список запросов с метриками.
    """
    headers = {"Authorization": f"OAuth {YANDEX_API_KEY}"}

    date_to = datetime.now()
    date_from = date_to - timedelta(days=30)

    params = {
        "order_by": metric,
        "limit": limit,
        "date_from": date_from.strftime("%Y-%m-%d"),
        "date_to": date_to.strftime("%Y-%m-%d"),
        "device_type_indicator": device_type,
    }

    if query_indicator:
        params["query_indicator"] = query_indicator

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{API_URL}/user/{YANDEX_USER_ID}/hosts/{YANDEX_HOST_ID}/search-queries/popular",
            headers=headers,
            params=params,
        ) as response:
            response_text = await response.text()
            if response.status != 200:
                raise Exception(f"Ошибка API ({response.status}): {response_text}")

            data = await response.json()
            return data.get("queries", [])
