spam = ['apples', 'bananas', 'tofu', 'cats']

def addAnd(lists):
    if len(lists) > 2:
        list[len(lists)-1] = 'and ' + list[len(lists)-1]
        print(*lists, sep=', ')
    else:
        print(*lists, sep=', ')

addAnd(spam)