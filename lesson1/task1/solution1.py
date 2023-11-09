# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess


# python lesson1/task1/solution1.py

def test_command(text, command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out and result.returncode == 0:
        print('SUCCESS')
    else:
        print('FAIL')


t_command = 'cat /etc/os-release'
t_text = '20.04.6'
print('start test_command() text', t_text, 'command', t_command)
test_command(t_text, t_command)
t_command = 'cat /etc/os-release'
t_text = 'focal'
print('start test_command() text', t_text, 'command', t_command)
test_command(t_text, t_command)
t_command = 'cat /etc/os-release'
t_text = 'x'
print('start test_command() text', t_text, 'command', t_command)
test_command(t_text, t_command)
t_command = 'x'
print('start test_command() text', t_text, 'command', t_command)
test_command(t_text, t_command)
t_command = 'pwd'
t_text = 'lesson1'
print('start test_command() text', t_text, 'command', t_command)
test_command(t_text, t_command)
