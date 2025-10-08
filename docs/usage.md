# Як користуватись

## Розрахунок норм
```bash
python scripts/calc_norms.py --db sqlite:///fuel_norms_project.db     --from 2025-01-01 --to 2025-12-31     --out dist/norms_calculated.parquet
```
Параметри:
- `--db` — рядок підключення до SQLite/іншої БД;
- `--from/--to` — період операцій;
- `--out` — файл для збереження результатів (CSV/Parquet/Excel).

## Експорт звіту в Excel
```bash
python scripts/report.py --db sqlite:///fuel_norms_project.db     --out dist/report.xlsx
```

## Приклади аналізу у ноутбуках
- `notebooks/eda_fuel_per_100km.ipynb` — розподіли L/100км, boxplot, outliers
- `notebooks/eda_engine_hours.ipynb` — L/мотогодину, вплив умов

## Пріоритет норм та коефіцієнтів (рекомендація)
1) Якщо є норма **для конкретного vehicle_id**, використовуємо її.  
2) Якщо ні — беремо норму **для типу техніки** (`vehicle_type`).  
3) Коефіцієнти відбираємо за умовами (`season`, `road_type`, `route_type`, `payload_pct`, `temp_c_avg`) і перемножуємо `factor`.  
4) Підсумкова **нормативна витрата** = база × добуток коефіцієнтів × (шлях/100 або мотогодини).