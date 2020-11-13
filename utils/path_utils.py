import logging
from errno import EEXIST
from os import makedirs
from os import sep, remove
from os.path import abspath, isfile
from shutil import rmtree

log = logging.getLogger(__name__)


def get_base_path():
    path_hierarchy = abspath(__file__).split(sep)[:-2]
    return f"{sep.join(path_hierarchy)}"


def mkdir_safe(dir_path: str):
    try:
        makedirs(dir_path)
    except OSError as e:
        if e.errno != EEXIST:
            raise


def rm_safe(path: str):
    try:
        if isfile(path):
            remove(path)
        else:
            rmtree(path, ignore_errors=False)
    except Exception as e:
        log.error('Failed to delete file/folder: %s', path, exc_info=e)
