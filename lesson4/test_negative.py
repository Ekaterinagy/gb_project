from lesson4.ssh_checkers import ssh_checkout_negative
from lesson4.test_data_conf import TestDataConfigure

conf = TestDataConfigure()


class TestNegative:

    def test_step1(self):
        # test1
        assert ssh_checkout_negative(conf.user_address, conf.user_name, conf.user_password,
                                     "cd {}; 7z e bad_arx.7z -o{} -y".format(conf.folder_out, conf.folder_ext),
                                     "ERROR", 22), "test1 FAIL"

    def test_step2(self):
        # test2
        assert ssh_checkout_negative(conf.user_address, conf.user_name, conf.user_password,
                                     "cd {}; 7z t bad_arx.7z".format(conf.folder_out),
                                     "ERROR", 22), "test2 FAIL"
