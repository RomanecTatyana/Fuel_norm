"""Завантаження налаштувань підключення до БД з .env"""
import os
from dotenv import load_dotenv

# Load from .env if present
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/samples/fuel_norms_fake.db")