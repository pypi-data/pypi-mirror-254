from datetime import datetime


def log(log_msg: str) -> None:
    date_log = _get_formatted_date()
    print(f"{date_log} INFO: {log_msg}")


def warn(warn_msg: str) -> None:
    date_log = _get_formatted_date()
    print(f"{date_log} INFO: {warn_msg}")


def err(err_msg: str) -> None:
    date_log = _get_formatted_date()
    print(f"{date_log} INFO: {err_msg}")


def _get_formatted_date() -> str:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date
