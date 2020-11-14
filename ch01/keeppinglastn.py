from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)  # создаем ограниченную очередь
    for line in lines:  # На каждой полученной строке
        if pattern in line:     # Если паттерн содержится в строке
            yield line, previous_lines    # Добавим в генератор саму строку, и очередь из предыдущих строк(ограниченную)
        previous_lines.append(line) # Но очередь предыдущих строк пополняется всегда, даже если паттерн не встретился


# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:     # Прочитали файл
        for line, prevlines in search(f, 'python', 5):  # Для каждого значения из полученного генератора, каждой строки
            for pline in prevlines:     # Для каждой предыдущей строки, из очереди
                print(pline, end='')    # Выводим одну из предыдущих строк из очереди
            print(line, end='')     # Завершаем вывод для строки
            print('-' * 20)     # Это просто разделитель
