import asyncio
import aiohttp
from core.config import YANDEX_API_KEY


async def get_user(oauth_token):
    """
    Получение идентификатора пользователя (user_id) из API Яндекс Вебмастера.
    :param oauth_token: OAuth-токен для доступа к API.
    :return: Идентификатор пользователя (user_id) или None, если произошла ошибка.
    """
    url = "https://api.webmaster.yandex.net/v4/user"
    headers = {"Authorization": f"OAuth {oauth_token}"}

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                print(f"Статус ответа: {response.status}")

                response_text = await response.text()
                print(f"Тело ответа: {response_text}")

                if response.status == 200:
                    data = await response.json()
                    return data["user_id"]
                else:
                    print(f"Ошибка: {response.status}, {response_text}")
                    return None
        except Exception as e:
            print(f"Исключение при выполнении запроса: {e}")
            return None


async def main():
    TOKEN = YANDEX_API_KEY

    user_id = await get_user(TOKEN)
    if user_id:
        print(f"Идентификатор пользователя: {user_id}")
    else:
        print("Не удалось получить идентификатор пользователя.")


if __name__ == "__main__":
    asyncio.run(main())
