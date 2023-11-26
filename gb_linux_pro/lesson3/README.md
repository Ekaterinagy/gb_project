## Урок 3. Использование фикстур в pytest. Создание отчетов о тестировании
###  Задание 1

Условие:
Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

#### Решение
После вызова каждого метода, создается запись в 
> [stat.txt](stat.txt) файл

```
@pytest.fixture(autouse=True, scope="function")
def finalization_method():
    time = datetime.now()
    processor_info = get_command_output("cat /proc/loadavg")
    files_count = data["count"]
    file_size = data["bs"]
    stats_info = (f'Время: {time}, кол-во файлов из конфига: {files_count}, размер файла из конфига {file_size},'
                  f' статистика загрузки процессора: {processor_info}')
    path = data["file_stat_txt"]
    with open(path, 'a', encoding='utf-8') as fw:
        fw.write(stats_info)
```


### Задание 2
Задание 2. (дополнительное задание)

Дополнить все тесты ключом команды 7z -t (тип архива). Вынести этот параметр в конфиг.

#### Решение

файл arx2.7z в рамках теста был заменен на arx2.{}
> cd {}; 7z a -t{} {}/arx2

добавлен параметр тип архива для приложения 7z
>7z_type: tar 
