from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.yandex_api import get_top_queries
from utils.helpers import calculate_ctr


router = Router()


@router.message(Command("top_views"))
async def top_views_handler(message: Message):
    try:
        data = await get_top_queries(metric="TOTAL_SHOWS")
        response = "\n".join(
            [
                f"{i + 1}. {query['query_text']} - {query['indicators']['TOTAL_SHOWS']} показов"
                for i, query in enumerate(data)
            ]
        )
        await message.answer(f"Топ-10 запросов по просмотрам:\n{response}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")


@router.message(Command("top_clicks"))
async def top_clicks_handler(message: Message):
    try:
        data = await get_top_queries(metric="TOTAL_CLICKS")
        response = "\n".join(
            [
                f"{i + 1}. {query['query_text']} - {query['indicators']['TOTAL_CLICKS']} кликов"
                for i, query in enumerate(data)
            ]
        )
        await message.answer(f"Топ-10 запросов по кликам:\n{response}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")


@router.message(Command("top_ctr"))
async def top_ctr_handler(message: Message):
    try:
        data = await get_top_queries(metric="TOTAL_SHOWS")
        sorted_data = calculate_ctr(data)
        response = "\n".join(
            [
                f"{i + 1}. {query['query_text']} - {query['ctr']:.2%} CTR"
                for i, query in enumerate(sorted_data)
            ]
        )
        await message.answer(f"Топ-10 запросов по CTR:\n{response}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
