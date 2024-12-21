
goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) ==1:
           yield item[args[0]]
        else:
            yield {i: item[i] for i in args}
        
    # Необходимо реализовать генератор
    # 
field(goods, 'title') #должен выдавать 'Ковер', 'Диван для отдыха'
field(goods, 'title', 'price') #должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

titles_and_prices1 = field(goods, 'title')
titles_and_prices2 = field(goods, 'title','price')
print(*titles_and_prices1)
print(*titles_and_prices2)