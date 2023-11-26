import random
import string
from datetime import datetime

import pytest
import yaml

from checkers import checkout, get_command_output

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(autouse=True, scope="module")
def clear_test_data():
    get_command_output("rm -fr {} {} {} {}".format(data["folder_in"], data["folder_out"],
                                                   data["folder_ext"], data["folder_ext2"]))


@pytest.fixture(autouse=True, scope="module")
def make_folders():
    return checkout("mkdir -p {} {} {} {}".format(data["folder_in"], data["folder_out"],
                                                  data["folder_ext"], data["folder_ext2"]), "")


@pytest.fixture(autouse=True, scope="class")
def make_files():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename,
                                                                                           data["bs"]), ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture(autouse=True, scope="function")
def finalization_method():
    time = datetime.now()
    processor_info = get_command_output("cat /proc/loadavg")
    files_count = data["count"]
    file_size = data["bs"]
    stats_info = (f'Время: {time}, кол-во файлов из конфига: {files_count}, размер файла из конфига {file_size},'
                  f' статистика загрузки процессора: {processor_info}')
    path = data["file_stat_txt"]
    with open(path, 'a', encoding='utf-8') as fw:
        fw.write(stats_info)
