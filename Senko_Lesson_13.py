# Senko_Timur group_208
# DZ


def function(fn):
    def wrapper(W):
        print(f'Тип данных который вы отправили: {type(W)}')
    return wrapper


letters = 0
numbers = 0
n = []


@function
def sort_all(m):
    global letters, numbers
    if type(m) == list:
        for i in str(m):
            if i.isalpha():
                letters += 1
            if i.isdigit():
                numbers += 1
        return f'Кол-во букв: {letters}, кол-во цифр: {numbers}'

    elif type(m) == tuple:    # Я вот здесь явно что-то важное забыл (не знаю как правильно сделать)
        m = str(m)
        return f"{''.join([p for p in m if not p.isdigit()])}"

    elif type(m) == int:
        for k in str(m):
            if k in '13579':
                return f'Кол-во нечётных цифр: {len(k)}'

    elif type(m) == str:
        if m.isalpha() == 0:
            return f'Кол-во букв в строке: 0'


sort_all([1, 2, 3, 'a', 'bc8?'])
sort_all((1, 2, 3, 'a', 'bc8?', 7, 8, 9))
sort_all(7887)
sort_all('7887')
