def format(time_string, datetime_value):
    aliases = {
        "WEEKDAY_SHORT": "%a",
        "WEEKDAY_LONG": "%A",
        "WEEKDAY_NUM": "%w",
        "DAY_OF_MONTH": "%d",
        "MONTH_SHORT": "%b",
        "MONTH_LONG": "%B",
        "MONTH_NUM": "%m",
        "YEAR_SHORT": "%y",
        "YEAR_LONG": "%Y",
        "HOUR_24": "%H",
        "HOUR_12": "%I",
        "AM_PM": "%p",
        "MINUTE": "%M",
        "SECOND": "%S",
        "MICROSECOND": "%f",
        "UTC_OFFSET": "%z",
        "TZ_NAME": "%Z",
        "DAY_OF_YEAR": "%j",
        "WEEK_NUM": "%U",
        "WEEK_NUM_START_MONDAY": "%W",
        "LOCAL_DATETIME": "%c",
        "LOCAL_DATE": "%x",
        "LOCAL_TIME": "%X",
    }

    for alias, directive in aliases.items():
        time_string = time_string.replace(alias, directive)

    return datetime_value.strftime(time_string) \
            .replace('January',   'января') \
            .replace('February',  'февраля') \
            .replace('March',     'марта') \
            .replace('April',     'апреля') \
            .replace('May',       'мая') \
            .replace('June',      'июня') \
            .replace('July',      'июля') \
            .replace('August',    'августа') \
            .replace('September', 'сентября') \
            .replace('October',   'октября') \
            .replace('November',  'ноября') \
            .replace('December',  'декабря') 

