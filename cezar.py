try:
    import pyperclip
except ImportError:
    print("Модуль pyperclip не установлен. Копирование в буфер обмена недоступно.")
    pyperclip = None

sym = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Вы хотите расшифровать (d) или зашифровать (e)?')
    response = input('>> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Пожалуйста, введите (e) для шифрования или (d) для дешифрования.')

while True:
    max_key = len(sym) - 1
    print(f'Введите допустимый ключ от 0 до {max_key}')
    response = input('>> ')
    if response.isdecimal() and 0 <= int(response) <= max_key:
        key = int(response)
        break
    print('Пожалуйста, введите корректный ключ.')

print('Введите сообщение для шифрования/дешифровки:')
message = input('>> ').upper()

trans = ''
for char in message:
    if char in sym:
        num = sym.find(char)
        if mode == 'encrypt':
            num = (num + key) % len(sym)
        elif mode == 'decrypt':
            num = (num - key) % len(sym)
        trans += sym
    else:
        trans += char

print(f'Результат: {trans}')

if pyperclip:
    pyperclip.copy(trans)
    print(f'Текст был скопирован в буфер обмена в режиме {mode}.')

