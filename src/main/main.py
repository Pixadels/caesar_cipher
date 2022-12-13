"""Модуль реализует шифр Цезаря.
На вход подаются текст для шифровки и смещение.
На выходе зашифрованная и расшифрованная строки.
"""

__version__ = '0.1'
__author__ = 'Linar Shayakhmetov'

ALPHABET_LEN: int = 0x10FFFF + 1  # Размер словаря


# шифруем
def encryptionCaesar(text: str, shift: int) -> str:
    """Зашифруем полученную строку."""
    global ALPHABET_LEN
    new_str: str = ''
    for ch in text:
        new_str += chr(((ord(ch) + shift) % ALPHABET_LEN))
    return new_str


# дешифруем
def decryptionCaesar(text: str, shift: int) -> str:
    """Расшифруем ранее зашифрованную строку."""
    global ALPHABET_LEN
    shift *= -1
    new_str: str = ''
    for ch in text:
        new_str += chr(((ord(ch) + shift) % ALPHABET_LEN))
    return new_str


if __name__ == '__main__':
    text: str = str(input('Введите текст для шифровки: '))
    shift: int = int(input('Введите смещение: '))

    text_encrypt: str = encryptionCaesar(text, shift)
    text_decrypt: str = decryptionCaesar(text_encrypt, shift)

    print(f'Результат шифровки: {text_encrypt}')
    print(f'Результат расшифровки: {text_decrypt}')
