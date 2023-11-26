# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом,
# чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.
import string
import subprocess


# python lesson1/task1/solution2.py

def test_command(text, command, punctuation_mode_enabled=False):
    print(
        f'test_command start: [text: {text}, command: {command}, punctuation_mode_enabled: {punctuation_mode_enabled}]')
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
    # print('[DEBUG] out_list', out_list)
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
