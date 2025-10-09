PRAGMA foreign_keys = ON;

-- Категорії ОЗ (транспортні категорії)
CREATE TABLE IF NOT EXISTS trans_category (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  uuid_1c   TEXT UNIQUE NOT NULL,   -- стабільний UID з 1С
  category  TEXT NOT NULL           -- назва категорії 
);

-- Унікальність UID 1С
CREATE UNIQUE INDEX IF NOT EXISTS ux_trans_category_uuid
  ON trans_category(uuid_1c);
