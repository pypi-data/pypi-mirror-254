import os

from easy_tasks import help_with_json
from var_print import varp


def write_config_json():
    data = {
        "FIREFOX_PROFILE_USER_DATA": r"C:\Users\Creed\AppData\Roaming\Mozilla\Firefox\Profiles",
        "GECKODRIVER_PATH": None,
        "USER_AGENT": "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    }
    help_with_json.dump_as_json(
        data,
        r"C:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\GitHub\selenium_simplification\selenium_simplification\Firefox\config.json",
    )


def read_config_json():
    data = help_with_json.get_from_json(
        r"C:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\GitHub\selenium_simplification\selenium_simplification\Firefox\config.json"
    )

    varp(data)
    # print(data)


if __name__ == "__main__":
    write_config_json()
    read_config_json()
