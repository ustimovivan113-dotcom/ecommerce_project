# Store Classes

## Функционал
- Класс Product с атрибутами: name (str), description (str), price (float), quantity (int).
- Классы-наследники: Smartphone (добавлены efficiency, model, memory, color) и LawnGrass (добавлены country, germination_period, color).
- Оператор + для продуктов: складывает только одинаковые классы, иначе TypeError.
- Метод add_product в Category: добавляет только Product или наследников, иначе TypeError.
- Класс Category с атрибутами: name (str), description (str), products (list[Product]).
- Атрибуты класса Category: category_count (int), product_count (int) — авто-обновляются при создании.

## Установка
poetry install

## Тесты
poetry run pytest

## Покрытие
poetry run pytest --cov=src