# Початкове налаштування

## 1) Змінні середовища
Скопіюй `.env.example` у `.env` і за потреби зміни параметри:
```
DATABASE_URL=sqlite:///fuel_norms_project.db
OUTPUT_DIR=dist
```

## 2) Підготовка БД
Є два варіанти:
1. Використати готовий файл `fuel_norms_project.db` (демодані).
2. Створити БД скриптом ініціалізації (наприклад, `scripts/init_db.py`), який:
   - створює таблиці (`vehicles`, `operations`, `norms`, `coefficients`, ...);
   - застосовує стартовий сидінг (довідники, приклади умов, коефіцієнти).

## 3) Перевірка підключення
```bash
python -c "import sqlite3; import pandas as pd; con=sqlite3.connect('fuel_norms_project.db'); print(pd.read_sql_query('select name from sqlite_master where type=\'table\'', con).head())"
```

## 4) Структура довідників/таблиць (скорочено)
- `vehicles(id, code, name, type, fuel_type, ...)`
- `operations(id, vehicle_id, op_date, distance_km/engine_hours, fuel_used_l, conditions_id, ...)`
- `conditions(id, season, road_type, route_type, temp_c_avg, payload_pct, ...)`
- `norms(id, vehicle_id|vehicle_type, basis[per_100km|per_engine_hour], base_value, ...)`
- `coefficients(id, filters..., factor)`
- В’юхи: `vw_ops_km`, `vw_ops_engine_hours`