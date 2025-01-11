import asyncio
import aiohttp


async def get_hosts(oauth_token, user_id):
    """
    Получение списка хостов пользователя из API Яндекс Вебмастера.
    :param oauth_token: OAuth-токен для доступа к API.
    :param user_id: Идентификатор пользователя (user_id).
    :return: Список хостов или None, если произошла ошибка.
    """
    url = f"https://api.webmaster.yandex.net/v4/user/{user_id}/hosts"
    headers = {"Authorization": f"OAuth {oauth_token}"}

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                print(f"Статус ответа: {response.status}")

                response_text = await response.text()
                print(
                    f"Тело ответа: {response_text}"
                )  # Логируем полный ответ для анализа

                if response.status == 200:
                    data = await response.json()
                    return data["hosts"]  # Возвращаем список хостов
                else:
                    print(f"Ошибка: {response.status}, {response_text}")
                    return None
        except Exception as e:
            print(f"Исключение при выполнении запроса: {e}")
            return None


async def main():
    TOKEN = "y0__wgBEIu4670BGJSqNCClt7-AEvotjIBBPNGOODLcTjj5bZ25q7p0"  # Ваш OAuth-токен
    USER_ID = "398121995"  # Ваш user_id

    hosts = await get_hosts(TOKEN, USER_ID)
    if hosts:
        print("Список сайтов:")
        for host in hosts:
            print(
                f"- Host ID: {host['host_id']}, Verified: {host['verified']}, Indexing Status: {host.get('indexing_status', 'UNKNOWN')}"
            )
    else:
        print("Не удалось получить список сайтов.")


if __name__ == "__main__":
    asyncio.run(main())
