import paramiko

from gb_linux_pro.lesson4.test_data_conf import TestDataConfigure


def upload_files(host, user, passwd, local_path, remote_path, port=22):
    print(f"Загружаем файл {local_path} в каталог {remote_path}")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()


def upload_files_by_conf(conf: TestDataConfigure):
    upload_files(conf.user_address, conf.user_name, conf.local_path, conf.remote_path, 22)


def download_files(host, user, passwd, remote_path, local_path, port=22):
    print(f"Скачиваем файл {remote_path} в каталог {local_path}")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remote_path, local_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()


def download_files_by_conf(conf: TestDataConfigure):
    download_files(conf.user_address, conf.user_name, conf.user_password, conf.remote_path, conf.local_path, 22)
