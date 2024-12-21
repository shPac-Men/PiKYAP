import random

def gen_random(num_count, begin , end):
    while num_count>0:
        yield random.randint(begin,end)
        num_count-=1

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.data = list(items)
        self.index = 0
        if len(kwargs) != 0:
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                flag = True
                if type(current) == str and self.ignore_case == True:
                    for i in self.used_elements:
                        if type(i) == str and i.lower() == current.lower():
                            flag = False
                            break
                if current not in self.used_elements and flag:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
for i in Unique(data):
    print(i) 
print()
data = ['a','A','b','B','a','A','b','B']
for i in Unique(data, ignore_case = True):
    print(i) 
print()
data = gen_random(10,1,3)
for i in Unique(data, ignore_case = True):
    print(i) 