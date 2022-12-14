import sys
sys.path.insert(0, 'src/main')

from main import encryptionCaesar
from main import decryptionCaesar
import unittest


class TestCeasar(unittest.TestCase):
    def test_encryption(self):
        """Тестируем шифровку.
        Если fork возвращает True, то тест успешно пройден
        """
        # обычная строка
        assert fork('abc', 1, 'bcd', True)
        # обычное число
        # self.assertEqual(encryptionCaesar('123', 1), '234')
        assert fork('abc', 1, 'bcd', True)
        # крайние левые символы
        assert fork(chr(0)+chr(1)+chr(2), 1, chr(0+1)+chr(1+1)+chr(2+1), True)
        # крайние правые символы
        assert fork(chr(0x10FFFF-2)+chr(0x10FFFF-1)+chr(0x10FFFF), 1,
                    chr(0x10FFFF-2+1)+chr(0x10FFFF-1+1)+chr(0), True)
        # 1 крайний левый символ
        assert fork(chr(0), 1, chr(0+1), True)
        # 1 крайний правый символ
        assert fork(chr(0x10FFFF), 1, chr(0), True)
        # нулевое смещение
        assert fork('abc', 0, 'abc', True)
        # отрицательное смещение
        assert fork('bcd', -1, 'abc', True)
        # обработка суррогатов
        assert fork(chr(0xD800-1), 1, chr(0xDFFF+1), True)

    def test_decryption(self):
        """Тестируем расшифровку.
        Если fork возвращает True, то тест успешно пройден
        """
        # обычная строка
        assert fork('abc', 1, 'bcd', False)
        # обычное число
        # self.assertEqual(encryptionCaesar('123', 1), '234')
        assert fork('abc', 1, 'bcd', False)
        # крайние левые символы
        assert fork(chr(0)+chr(1)+chr(2), 1, chr(0+1)+chr(1+1)+chr(2+1), False)
        # крайние правые символы
        assert fork(chr(0x10FFFF-2)+chr(0x10FFFF-1)+chr(0x10FFFF), 1,
                    chr(0x10FFFF-2+1)+chr(0x10FFFF-1+1)+chr(0), False)
        # 1 крайний левый символ
        assert fork(chr(0), 1, chr(0+1), False)
        # 1 крайний правый символ
        assert fork(chr(0x10FFFF), 1, chr(0), False)
        # нулевое смещение
        assert fork('abc', 0, 'abc', False)
        # отрицательное смещение
        assert fork('bcd', -1, 'abc', False)
        # обработка суррогатов
        assert fork(chr(0xD800-1), 1, chr(0xDFFF+1), False)
        # обработка ошибок
        # assert fork(1, 1, 2, False)


def fork(to_encode: str, shift: int, to_decode: str, encode: bool) -> bool:
    """Функция для упрощения написания тестов

    Принимает строку для кодирования, смещение, строку для декодирования,
    и режим работы encode.
    Аргумент encode позволяет быстро превратить набор тестов функции шифрования
    в набор тестов функции расшифровки и наоборот
    """
    if encode:
        if encryptionCaesar(to_encode, shift) == to_decode:
            return True
    else:
        if decryptionCaesar(to_decode, shift) == to_encode:
            return True
    return False


if __name__ == "__main__":
    unittest.main()
