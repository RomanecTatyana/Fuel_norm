# Встановлення

## Вимоги
- Python 3.11+
- pip
- (опц.) VS Code з розширеннями **Python**, **Jupyter**, **SQLite**

## Кроки
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

## requirements.txt (приклад вмісту)
```
pandas
numpy
matplotlib
plotly
sqlalchemy
openpyxl
pytest
python-dotenv
```