import datetime


def date_transformer(timestamp: int):
    # 将时间戳转换为日期和时间
    dt = datetime.datetime.fromtimestamp(timestamp)

    # 格式化日期和时间字符串
    formatted_datetime = dt.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime
