from datetime import datetime


class DatetimeService:
    @staticmethod
    def convert_date_string_to_datetime(date_str: str) -> datetime:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def convert_time_string_to_time_object(time_str: str) -> datetime.time:
        return datetime.strptime(time_str, "%H:%M").time()
