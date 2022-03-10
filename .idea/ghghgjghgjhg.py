def count_letters(a):
    print(f'Количество заглавных символов: {len([i for i in a if i.isupper()])}')
    print(f'Количество строчных символов: {len([i for i in a if i.islower()])}')
