import yaml


class TestDataConfigure:
    _config_location = "config.yml"
    user_address = None
    user_name = None
    user_password = None
    local_path = None
    remote_path = None
    folder_in = None
    folder_out = None
    folder_ext = None
    folder_ext2 = None
    z_type = None
    count = None
    bs = None
    stat_txt = None
    snapshot = None

    def __init__(self, config_location=None):
        if config_location:
            self._config_location = config_location
        self.load_config(self._config_location)

    def load_config(self, config_location):
        with open('config.yaml') as f:
            data = yaml.safe_load(f)
            self.user_name = data['user_name']
            self.user_password = data['user_pass']
            self.user_address = data['user_address']
            self.local_path = data['local_path']
            self.remote_path = data['remote_path']
            self.folder_in = data['folder_in']
            self.folder_out = data['folder_out']
            self.folder_ext = data['folder_ext']
            self.folder_ext2 = data['folder_ext']
            self.z_type = data['7z_type']
            self.bs = data['bs']
            self.count = data['count']
            self.stat_txt = data['file_stat_txt']
