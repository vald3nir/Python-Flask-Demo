from datetime import datetime


def get_today_date_formatted():
    return datetime.today().strftime('%Y-%m-%d')


def get_today_date_utc():
    return datetime.utcnow()
