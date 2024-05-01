from pathlib import Path

import telegram_mobile_test_project


def abs_path_from_project(file_name):
    return str(Path(telegram_mobile_test_project.__file__).parent.parent.joinpath(file_name))
