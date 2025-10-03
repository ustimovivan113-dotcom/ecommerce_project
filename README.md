# Store Classes

## Функционал
- Класс Product с атрибутами: name (str), description (str), price (float), quantity (int).
- Класс Category с атрибутами: name (str), description (str), products (list[Product]).
- Атрибуты класса Category: category_count (int), product_count (int) — авто-обновляются при создании.

## Установка
poetry install

## Тесты
poetry run pytest

## Покрытие
poetry run pytest --cov=store_classes