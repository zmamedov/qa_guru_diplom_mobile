from pathlib import Path

import qa_guru_diplom_mobile


def abs_path_from_project(file_name):
    return str(Path(qa_guru_diplom_mobile.__file__).parent.parent.joinpath(file_name))
