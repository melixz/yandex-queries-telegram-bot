def calculate_ctr(data):
    """
    Рассчитывает CTR для каждого поискового запроса.
    :param data: Список запросов с метриками.
    :return: Отсортированный список запросов по CTR.
    """
    for query in data:
        shows = query["indicators"].get("TOTAL_SHOWS", 0)
        clicks = query["indicators"].get("TOTAL_CLICKS", 0)
        query["ctr"] = (clicks / shows) if shows > 0 else 0

    sorted_data = sorted(data, key=lambda x: x["ctr"], reverse=True)
    return sorted_data[:10]
