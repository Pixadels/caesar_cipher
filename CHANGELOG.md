# Change Log

## [Unreleased] - yyyy-mm-dd

### Changed
- Сделать одну общую функцию для шифрования и дешифрования чтобы следовать DRY принципу

### Added
- Добавить ограничение на длину сообщения для шифровки
- Добавить ограничение на величину смещения


## [0.3] - 2022-12-14

### Changed
- [(d53216d)](https://github.com/Pixadels/caesar_cipher/commit/d53216dadefa39341e4665cd056261fc1c36f29f) Улучшен визуал интерфейса ввода вывода

### Added
- [(2040319)](https://github.com/Pixadels/caesar_cipher/commit/20403190cf2b72ff36cf9251687b8a89beb5d667) Добавлена проверка введенных данных на соответствие типам 
- [(d53216d)](https://github.com/Pixadels/caesar_cipher/commit/d53216dadefa39341e4665cd056261fc1c36f29f) Добавлен бесконечный цикл на ввод вывод 
- [(aa826c4)](https://github.com/Pixadels/caesar_cipher/commit/aa826c46603880a1f2c412a5026df0c9d6b07480) Добавлены аннотации типов для new_str, new_ord, ALPHABET_LEN 


## [0.2] - 2022-12-14 

### Added [(fefec5b)](https://github.com/Pixadels/caesar_cipher/commit/fefec5b40bd8c390c1a462814d724bdfef237c0e)
- Добавлена обработка суррогатных пар в функции шифрования и дешифровки
- Добавлены новые тесты


## [0.1] - 2022-12-14 
 
### Added [(72a39b0)](https://github.com/Pixadels/caesar_cipher/commit/72a39b0daf62d6d23b8b51f8c226addce2f0a874)
- Реализован базовый функционал - шифрование и дешифровка
- Реализованы тесты для обоих функций
