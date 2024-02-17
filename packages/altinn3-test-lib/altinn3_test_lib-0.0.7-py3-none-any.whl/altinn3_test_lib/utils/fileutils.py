from os import path

import logging
logger = logging.getLogger()


def read_file_lines_into_object(file_name: str):

    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "test_files", file_name))
    f = open(filepath, "r")
    file_lines = "".join(f.readlines())

    return file_lines


