___#KIS-2023___

Решение задачи №4 отбора на кафедру КИС.

Задача заключалась в том, чтобы сравнить файлы в двух директориях и проверить их на схожесть.

Решение представлено на языке Python

Работа программы устроено следующем образом:
> Файлы из двух директорий по очереди открываются и сравниваются друг с другом с помощью расстояния Левенштейна

> Затем в зависимости от процента схожести считаются совпадающими (если 100% совпадение) и похожими или не похожими (в зависимости от порогового значения)

> После этого каждая пара файлов сохраняется отдельно и выводится в соответствии с форматом.

Для запуска скрипта, нужно запустить файл solution.py с помощью интерпретатора python и в качестве аргументов передать две директории:

__python solution.py dir_name_1 dir_name_2__
