import random

x, y = (5, 8)
print(x)

z = (5, 8)
x, y = z
print(y)

a = 5
b = 8
a = a + b  # (5 + 8 = 13)
b = a - b  # (13 — 8 = 5)
a = a - b  # (13 — 5 = 8)
print(a, b)

a = 5
b = 8
a, b = b, a

z = tuple([5, 8])


def foo(z):
    return z[0] + z[1]


sfbd = None


def set_invoice_yes1(cons_data, result):
    response = sfbd.set_invoice_mark(cons_data[1])
    if response[1]:
        result.append((cons_data[0], response[1]))
    elif response[0] == 'ShortFormBookingDisplay':
        sfbd.exit()
    else:
        pass


def set_invoice_yes2(cons_data, result):
    display, message = sfbd.set_invoice_mark(cons_data[1])
    if message:
        result.append((cons_data[0], message))
    elif display == 'ShortFormBookingDisplay':
        sfbd.exit()
    else:
        pass


def set_invoice_yes3(cons_data, result):
    cons_id, mark = cons_data
    display, message = sfbd.set_invoice_mark(mark)
    if message:
        result.append((cons_id, message))
    elif display == 'ShortFormBookingDisplay':
        sfbd.exit()
    else:
        pass


COLORS = {}


def draw_line(*args):
    pass


draw_line(25, 36, 48, 56, COLORS['red'])
draw_line((25, 36), (48, 56), COLORS['red'])

screen.register_shape("triangle", ((5, -3), (0, 5), (-5, -3)))
wx.Frame.__init__(self, parent, title=title, size=(200, 100))

def func(*args, **kwargs):
    def more_func(*args):
        for _ in args:
            yield _ * _

some_tuple = tuple()

_, b = z
_, _, a, b, _ = some_tuple

def boo():
    for _ in range(10):
        print(_)

boo()

large_tuple = tuple(random.sample(range(0, 100), 99))
a, *some = large_tuple
a

a, b, *some = large_tuple
print(a, b)

a, *some, b = large_tuple
print(a, b)


def func1(data):
    for rec in data:
        _, first_name, last_name, *some, total_grade = rec
        yield f'Student {first_name} {last_name} has got grade {total_grade}'


def func2(data):
    for rec in data:
        *some, math_grade, phys_grade, _ = rec
        yield (math_grade + phys_grade) / 2

a, b, c = z

dict(zip(keys, values))

def draw_square1(x1, y1, x2, y2, x3, y3, x4, y4):
    pass

def draw_square2(x1, y1, x2, y2, x3, y3, x4, y4):
    pass