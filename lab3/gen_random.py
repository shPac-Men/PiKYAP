# Пример:
 #должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
import random

def gen_random(num_count, begin , end):
    while num_count>0:
        yield random.randint(begin,end)
        num_count-=1

ans = gen_random(5,1,3)
print(*ans)