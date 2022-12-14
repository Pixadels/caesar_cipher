"""Модуль реализует шифр Цезаря.
На вход подаются текст для шифровки и смещение.
На выходе зашифрованная и расшифрованная строки.
"""

__version__ = '0.2'
__author__ = 'Linar Shayakhmetov'

ALPHABET_LEFT: int = 0x0  # Можно поменять левый край алфавита
ALPHABET_RIGHT: int = 0x10FFFF  # Можно поменять правый край алфавита
# Существуют служебные символы, которые я думаю будет красиво пропускать
# если новый символ будет попадать в этот диапазон
SUR_LEFT: int = 0xD800
SUR_RIGHT: int = 0xDFFF
SUR_LEN: int = SUR_RIGHT - SUR_LEFT + 1  # 57343 - 55296 + 1


def encryptionCaesar(text: str, shift: int) -> str:
    """Зашифруем полученную строку."""
    ALPHABET_LEN = ALPHABET_RIGHT - ALPHABET_LEFT + 1
    new_str = ''
    for ch in text:
        new_ord = ((ord(ch)+shift-ALPHABET_LEFT) % ALPHABET_LEN)
        new_ord += ALPHABET_LEFT
        # обработка суррогатов, они не принимаются и не возвращаются
        if SUR_LEFT <= new_ord <= SUR_RIGHT:
            new_str += chr(new_ord + SUR_LEN)
        else:
            new_str += chr(new_ord)
    return new_str


def decryptionCaesar(text: str, shift: int) -> str:
    """Расшифруем ранее зашифрованную строку."""
    shift *= -1
    ALPHABET_LEN = ALPHABET_RIGHT - ALPHABET_LEFT + 1
    new_str = ''
    for ch in text:
        new_ord = ((ord(ch)+shift-ALPHABET_LEFT) % ALPHABET_LEN)
        new_ord += ALPHABET_LEFT
        # обработка суррогатов, они не принимаются и не возвращаются
        if SUR_LEFT <= new_ord <= SUR_RIGHT:
            new_str += chr(new_ord - SUR_LEN)
        else:
            new_str += chr(new_ord)
    return new_str


if __name__ == '__main__':
    text: str = str(input('Введите текст для шифровки: '))
    shift: int = int(input('Введите смещение: '))

    text_encrypt: str = encryptionCaesar(text, shift)
    text_decrypt: str = decryptionCaesar(text_encrypt, shift)

    print(f'Результат шифровки: {text_encrypt}')
    print(f'Результат расшифровки: {text_decrypt}')
