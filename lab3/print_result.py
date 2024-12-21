# Здесь должна быть реализация декоратора
def print_result(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if type(result) == list:
            print(*result)
        if type(result) == dict:
            for i in result.keys():
                print('{} = {}'.format(i, result[i]))
        else:
            print(result)
        return result
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()