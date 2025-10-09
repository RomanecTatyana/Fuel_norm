# SQLite Migrations — простий раннер

## Структура
- `migrations/0001_init_schema.sql` — початкова схема
- `migrations/0002_placeholder.sql` — приклад наступної міграції
- `migrate.py` — застосування міграцій до БД

## Як працює
- У БД підтримується таблиця `schema_version(version INTEGER, filename TEXT, applied_at TEXT)`.
- Раннер читає каталог `migrations/`, сортує файли за префіксом (`0001`, `0002`, ...), і виконує ті, яких ще немає у `schema_version`.
- Кожна міграція — звичайний `.sql` (одна транзакція на файл).

## Команди
```bash
python migrate.py --db data/samples/fuel_norms_fake.db
```
