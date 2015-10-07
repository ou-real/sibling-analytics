import os
import fnmatch
import logging


def split_path(path):
    logger = logging.getLogger(__name__)
    path = os.path.normpath(path)
    components = []
    while True:
        (path,tail) = os.path.split(path)
        if tail == "":
            components.reverse()
            return components
        components.append(tail)

def clone_directory(src, dest):
    logger = logging.getLogger(__name__)
    for root, dirnames, filenames in os.walk(src):
        path_list = split_path(root)
        if len(path_list) > 1:
            path_list[0] = dest
            new_dir = os.path.join(*path_list)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

def get_subdirs(src):
    logger = logging.getLogger(__name__)
    for root, subdirs, files in os.walk(src):
        if root != src:
            yield root

def get_folders_recursive(src, regex):
    logger = logging.getLogger(__name__)
    for root, subdirs, files in os.walk(src):
        for file_name in files:
            if fnmatch.fnmatch(file_name, regex):
                yield root

def get_files_recursive(src, regex):
    logger = logging.getLogger(__name__)
    for root, subdirs, files in os.walk(src):
        for file_name in files:
            if fnmatch.fnmatch(file_name, regex):
                yield os.path.join(root, file_name)


def keep_existing_mkdir(*path):
    logger = logging.getLogger(__name__)
    path = os.path.join(*path)
    path = os.path.abspath(os.path.normpath(path))
    if os.path.exists(path):
        new_name = path
        i = 1
        while os.path.exists(new_name):
            new_name = '{}_{}'.format(path, i)
            i+=1
        path = new_name
    logger.info('Creating directory "{}"'.format(path))
    os.makedirs(path)
    return path

def mkdir(*path):
    logger = logging.getLogger(__name__)
    path = os.path.join(*path)
    path = os.path.abspath(os.path.normpath(path))
    if os.path.exists(path):
        logger.warning('Directory "{}" already exists.'.format(path))
    else:
        logger.info('Creating directory "{}"'.format(path))
        os.makedirs(path)
    return path