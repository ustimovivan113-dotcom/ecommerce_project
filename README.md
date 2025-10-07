# Store Classes

## Функционал
- Класс Product с атрибутами: name (str), description (str), price (float), quantity (int).
- Класс Category с атрибутами: name (str), description (str), products (list[Product]).
- Атрибуты класса Category: category_count (int), product_count (int) — авто-обновляются при создании.
- Добавлен абстрактный класс BaseProduct для общей функциональности продуктов.
- Добавлены классы Smartphone и LawnGrass, наследующие от Product.
- Добавлен PrintMixin для печати информации при создании объектов Product и наследников.
- Реализован метод add_product в Category для добавления продуктов с проверкой типа.

## Установка
poetry install

## Тесты
poetry run pytest

## Покрытие
poetry run pytest --cov=src
