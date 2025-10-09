# Початкове налаштування

## 1) Змінні середовища
Скопіюй `.env.example` у `.env` і за потреби зміни параметри:
```
# демо (фейкова) БД у репозиторії
DATABASE_URL=sqlite:///data/samples/fuel_norms_fake.db
OUTPUT_DIR=dist

# приклад для реальної БД поза репозиторієм (Windows)
# DATABASE_URL=sqlite:///E:/Fuel_norm/secrets/fuel_norms_real.db
```

## 2) Підготовка БД
Є два варіанти:
1. Використати готовий файл `fuel_norms_fake.db` (демодані).
2. Створити БД скриптом ініціалізації (наприклад, `scripts/init_db.py`), який:
   - створює таблиці (`trans_category`);
   - застосовує стартовий сидінг (довідники, приклади умов, коефіцієнти).

## 3) Перевірка підключення
```bash
python -c "import sqlite3; import pandas as pd; con=sqlite3.connect('fuel_norms_fake.db'); print(pd.read_sql_query('select name from sqlite_master where type=\'table\'', con).head())"
```

## 4) Структура довідників/таблиць (скорочено)
- `trans_category(id, uuid_1c, category)`
- В’юхи: `vw_ops_km`, `vw_ops_engine_hours`