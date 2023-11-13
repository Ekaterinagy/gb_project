## Урок 2. Создание первых тестов на pytest

### Задание 1.  
  
Условие:    
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) 

[test_positive.py](test_positive.py)
```
def test_step5():
    # test5 task1.1

    result1 = checkout("cd {}; 7z l -bb arx2.7z".format(out), "qwe")
    result2 = checkout("cd {}; 7z l arx2.7z".format(out), "bits")

    assert result1 and result2, "test5 FAIL"
```    
и разархивирования с путями (x):

[test_positive.py](test_positive.py)
```
def test_step7():
    # test7 task1.2
    result1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(out, folder2), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder2), "qwe")
    result3 = checkout("cd {}; ls".format(folder2), "rty")
    assert result1 and result2 and result3, "test7 FAIL"
```

### Задание 2. 
Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32
[test_positive.py](test_positive.py)

```
def get_command_output(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
    return result


def test_step8():
    # test8 task2
    result1 = get_command_output("7z h -ba {}/arx2.7z".format(out))
    result2 = result1[0:result1.find(" ")]
    result3 = get_command_output("crc32 {}/arx2.7z".format(out)).replace("\n", "")
    assert result2.lower() == result3
```