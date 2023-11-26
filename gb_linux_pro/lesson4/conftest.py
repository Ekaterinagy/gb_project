import random
import string
from datetime import datetime

import pytest

from gb_linux_pro.lesson4.ssh_checkers import ssh_getout, ssh_checkout
from gb_linux_pro.lesson4.ssh_files_helper import upload_files
from gb_linux_pro.lesson4.test_data_conf import TestDataConfigure

conf = TestDataConfigure()


@pytest.fixture(autouse=True, scope="class")
def make_files():
    list_off_files = []
    for i in range(conf.count):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                        "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(conf.folder_in, filename,
                                                                                               conf.bs), "", 22):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture(autouse=True, scope="module")
def prepare_directories():
    print("prepare directories")
    out = ssh_getout(conf.user_address, conf.user_name, conf.user_password,
                     "mkdir {} {} {} {}".format(conf.folder_in, conf.folder_out, conf.folder_ext, conf.folder_ext2),
                     22)


@pytest.fixture(autouse=True, scope="module")
def deploy():
    res = []
    # проверяем наличия файла у юзера, иначе копируем
    out = ssh_getout(conf.user_address, conf.user_name, conf.user_password,
                     "find /home/test_user/ -type f -name 'p7zip-full.deb'", 22)
    print("step 1.0", out)
    if "p7zip-full.deb" in out[0]:
        print("file 'p7zip-full.deb' exist, upload not required, step 1 will skipped")
    else:
        upload_files(conf.user_address, conf.user_name, conf.user_password, "test_data/p7zip-full.deb",
                     "/home/test_user/p7zip-full.deb", port=22)
    # проверяем что пакет установлен, иначе устанавливаем
    if ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                    "echo 2222 | sudo -S dpkg -s p7zip-full",
                    "Status: install ok installed"):
        print("pkg already installed, step1_1 and step2_2 skipped")
        return True
    else:
        step1_1 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "echo 2222 | sudo -S dpkg -i home/test_data/p7zip-full.deb",
                               "Настраивается пакет")
        step1_2 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "echo 2222 | sudo -S dpkg -s p7zip-full",
                               "Status: install ok installed")
        return all([step1_1, step1_2])


@pytest.fixture(scope="function")
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture(autouse=True, scope="function")
def finalization_method(start_time):
    time = start_time
    processor_info = \
        ssh_getout(conf.user_address, conf.user_name, conf.user_password,
                   f"echo 2222 | sudo -S journalctl --since '{time}'", 22)[0]
    files_count = conf.count
    file_size = conf.bs
    stats_info = (f'Время: {time}, кол-во файлов из конфига: {files_count}, размер файла из конфига {file_size},'
                  f' лог журнала: {processor_info}')
    path = conf.stat_txt
    with open(path, 'a', encoding='utf-8') as fw:
        fw.write(stats_info)


@pytest.fixture(autouse=True, scope="session")
def clear_test_data():
    print("clear test data")
    ssh_getout(conf.user_address, conf.user_name, conf.user_password,
               "rm -rf {} {} {} {}".format(conf.folder_in, conf.folder_out,
                                           conf.folder_ext, conf.folder_ext2), 22)
