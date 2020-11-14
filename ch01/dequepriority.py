from collections import deque

task_list =['confirm', 'unconfirm']


def check_priority(dq):
    if dq[-1] in task_list:
        dq.rotate()

dq = deque()
dq.append('invoceyesset')   # Имитация работы моей системы автоматизации терминальной программы
check_priority(dq)
print(dq)
dq.append('invoicenoset')   # Имитация работы моей системы автоматизации терминальной программы
check_priority(dq)
print(dq)
dq.append('confirm')        # Имитация работы моей системы автоматизации терминальной программы
print(dq)
check_priority(dq)
print(dq)
