from lesson4.ssh_checkers import ssh_checkout, ssh_getout
from lesson4.test_data_conf import TestDataConfigure

conf = TestDataConfigure()


class TestPositive:
    def test_step1(self):
        # test1
        result1 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; 7z a -t{} {}/arx2".format(conf.folder_in, conf.z_type, conf.folder_out),
                               "Everything is Ok", 22)
        result2 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; ls".format(conf.folder_out), f"arx2.{conf.z_type}", 22)
        assert result1 and result2, "test1 FAIL"

    def test_step2(self, make_files):
        # test2
        result1 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; 7z e arx2.{} -o{} -y".format(conf.folder_out, conf.z_type,
                                                                    conf.folder_ext),
                               "Everything is Ok", 22)
        result2 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; ls".format(conf.folder_ext), make_files[0], 22)

        assert result1 and result2, "test2 FAIL"

    def test_step3(self):
        # test3
        assert ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                            "cd {}; 7z t arx2.{}".format(conf.folder_out, conf.z_type),
                            "Everything is Ok", 22), "test3 FAIL"

    def test_step4(self):
        # test4
        assert ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                            "cd {}; 7z u {}/arx2.{}".format(conf.folder_in, conf.folder_out, conf.z_type),
                            "Everything is Ok", 22), "test4 FAIL"

    def test_step5(self, make_files):
        # test5 task1.1

        result1 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; 7z l -bb arx2.{}".format(conf.folder_out, conf.z_type), make_files[0], 22)
        result2 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; 7z l -bb arx2.{}".format(conf.folder_out, conf.z_type), make_files[1], 22)

        assert result1 and result2, "test5 FAIL"

    def test_step6(self, make_files):
        # test7 task1.2
        print('make_files', make_files)
        result1 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; 7z x arx2.{} -o{} -y".format(conf.folder_out, conf.z_type, conf.folder_ext2),
                               "Everything is Ok", 22)
        result2 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; ls".format(conf.folder_ext2), make_files[0], 22)
        result3 = ssh_checkout(conf.user_address, conf.user_name, conf.user_password,
                               "cd {}; ls".format(conf.folder_ext2), make_files[1], 22)
        assert result1 and result2 and result3, "test7 FAIL"

    def test_step7(self):
        # test8 task2
        result1 = ssh_getout(conf.user_address, conf.user_name, conf.user_password,
                             "7z h -ba {}/arx2.{}".format(conf.folder_out, conf.z_type), 22)[0]
        print("result1", result1)
        result2 = result1[0:result1.find(" ")]
        print("result2", result2)
        result3 = (ssh_getout(conf.user_address, conf.user_name, conf.user_password,
                              "crc32 {}/arx2.{}".format(conf.folder_out, conf.z_type), 22)[0]
                   .replace("\n", ""))
        print("result3", result3)
        assert result2.lower() == result3
