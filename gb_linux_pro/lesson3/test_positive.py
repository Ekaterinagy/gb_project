import yaml

from checkers import checkout, get_command_output

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:

    def test_step1(self):
        # test1
        result1 = checkout("cd {}; 7z a -t{} {}/arx2".format(data["folder_in"], data["7z_type"], data["folder_out"]),
                           "Everything is Ok")
        result2 = checkout("cd {}; ls".format(data["folder_out"]), f"arx2.{data['7z_type']}")
        assert result1 and result2, "test1 FAIL"

    def test_step2(self, make_files):
        # test2
        result1 = checkout("cd {}; 7z e arx2.{} -o{} -y".format(data["folder_out"], data["7z_type"],
                                                                data["folder_ext"]),
                           "Everything is Ok")
        result2 = checkout("cd {}; ls".format(data["folder_ext"]), make_files[0])

        assert result1 and result2, "test2 FAIL"

    def test_step3(self):
        # test3
        assert checkout("cd {}; 7z t arx2.{}".format(data["folder_out"], data["7z_type"]),
                        "Everything is Ok"), "test3 FAIL"

    def test_step4(self):
        # test4
        assert checkout("cd {}; 7z u {}/arx2.{}".format(data['folder_in'], data["folder_out"], data["7z_type"]),
                        "Everything is Ok"), "test4 FAIL"

    def test_step5(self, make_files):
        # test5 task1.1

        result1 = checkout("cd {}; 7z l -bb arx2.{}".format(data["folder_out"], data["7z_type"]), make_files[0])
        result2 = checkout("cd {}; 7z l -bb arx2.{}".format(data["folder_out"], data["7z_type"]), make_files[1])

        assert result1 and result2, "test5 FAIL"

    def test_step7(self, make_files):
        # test7 task1.2
        result1 = checkout(
            "cd {}; 7z x arx2.{} -o{} -y".format(data["folder_out"], data["7z_type"], data["folder_ext2"]),
            "Everything is Ok")
        result2 = checkout("cd {}; ls".format(data["folder_ext2"]), make_files[0])
        result3 = checkout("cd {}; ls".format(data["folder_ext2"]), make_files[1])
        assert result1 and result2 and result3, "test7 FAIL"

    def test_step8(self):
        # test8 task2
        result1 = get_command_output("7z h -ba {}/arx2.{}".format(data["folder_out"], data["7z_type"]))
        result2 = result1[0:result1.find(" ")]
        result3 = (get_command_output("crc32 {}/arx2.{}".format(data["folder_out"], data["7z_type"]))
                   .replace("\n", ""))
        assert result2.lower() == result3
