## Урок 1. Тестирование cli в linux без использования фреймворков 
  
### Задание 1.  
  
Условие:    
Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.  
* lesson1/task1/solution1.py
```
# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess


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


```
#### Вывод 1
```

~/gb_lessons/linux_on_pythin/gb_project/lesson1/task1$ python solution1.py 
start test_command() text 20.04.6 command cat /etc/os-release
SUCCESS
start test_command() text focal command cat /etc/os-release
SUCCESS
start test_command() text x command cat /etc/os-release
FAIL
start test_command() text x command x
/bin/sh: 1: x: not found
FAIL
start test_command() text lesson1 command pwd
SUCCESS


```
  
### Задание 2. (повышенной сложности)  
Условие:    
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.    
* lesson1/task1/solution2.py
* lesson1/task1/solution2_test_data.txt
```
# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом,
# чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.
import string
import subprocess


def test_command(text, command, punctuation_mode_enabled=False):
    print(f'test_command start: [text: {text}, command: {command}, punctuation_mode_enabled: {punctuation_mode_enabled}]')
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode != 0:
        print(f'FAIL of execution command: [{command}],ErrorCode:', result.returncode)
        return
    out = result.stdout

    if not punctuation_mode_enabled:
        print('SUCCESS' if text in out else 'FAIL')
        return

    # expert mode
    out = out.replace('\n', ' ')
    for char in string.punctuation:
        out = out.replace(char, ' ')
    out_list = set(out.split(' '))
    print('[DEBUG] out_list', out_list)
    print('SUCCESS' if text in out_list else 'FAIL')


t_command = 'x'
t_text = 'Анна'

test_command(t_text, t_command)
t_command = 'cat solution2_test_data.txt'
test_command(t_text, t_command)
test_command(t_text, t_command, True)

t_command = "grep -rn 'Анна'"
test_command('solution2', t_command, True)
test_command('data', t_command, True)

```

#### Вывод 2
```
~/gb_lessons/linux_on_pythin/gb_project/lesson1/task1$ python solution2.py 
test_command start: [text: Анна, command: x, punctuation_mode_enabled: False]
/bin/sh: 1: x: not found
FAIL of execution command: [x],ErrorCode: 127
test_command start: [text: Анна, command: cat solution2_test_data.txt, punctuation_mode_enabled: False]
SUCCESS
test_command start: [text: Анна, command: cat solution2_test_data.txt, punctuation_mode_enabled: True]
SUCCESS
test_command start: [text: solution2, command: grep -rn 'Анна', punctuation_mode_enabled: True]
SUCCESS
test_command start: [text: data, command: grep -rn 'Анна', punctuation_mode_enabled: True]
SUCCESS

```
