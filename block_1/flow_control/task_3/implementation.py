def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    months = {
        "январь": 31,
        "февраль": 28,
        "март": 31,
        "апрель": 30,
        "май": 31,
        "июнь": 30,
        "июль": 31,
        "август": 31,
        "сентябрь": 30,
        "октябрь": 31,
        "ноябрь": 30,
        "декабрь": 31
    }
    result = 0

    month = month.lower()
    if month in months.keys():
        result = months[month]

    return result
