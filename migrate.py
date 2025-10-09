
import argparse, os, re, sqlite3, datetime

def ensure_meta(conn):
    conn.execute("""CREATE TABLE IF NOT EXISTS schema_version(
        version   INTEGER NOT NULL,
        filename  TEXT NOT NULL,
        applied_at TEXT NOT NULL
    )""")
    conn.commit()

def applied_versions(conn):
    rows = conn.execute("SELECT version, filename FROM schema_version ORDER BY version").fetchall()
    return {int(v): fn for (v, fn) in rows}

def discover_migrations(migrations_dir):
    files = []
    for name in os.listdir(migrations_dir):
        if name.lower().endswith(".sql"):
            m = re.match(r"^(\d{4})_.*\.sql$", name)
            if m:
                files.append((int(m.group(1)), name))
    files.sort()
    return files

def apply_migration(conn, path, version, filename):
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("BEGIN;")
        conn.executescript(sql)
        conn.execute("INSERT INTO schema_version(version, filename, applied_at) VALUES (?,?,?)",
                    (version, filename, datetime.datetime.utcnow().isoformat(timespec='seconds') + "Z"))
        conn.execute("COMMIT;")
        print(f"[OK] Applied {filename}")
    except Exception as e:
        conn.execute("ROLLBACK;")
        raise

def main():
    ap = argparse.ArgumentParser(description="SQLite migrations runner")
    ap.add_argument("--db", required=True, help="Path to SQLite .db file")
    ap.add_argument("--dir", default="migrations", help="Migrations directory")
    args = ap.parse_args()

    if not os.path.exists(args.db):
        # create empty DB file
        open(args.db, "a").close()

    conn = sqlite3.connect(args.db)
    try:
        ensure_meta(conn)
        applied = applied_versions(conn)
        to_apply = discover_migrations(args.dir)
        for ver, name in to_apply:
            if ver not in applied:
                apply_migration(conn, os.path.join(args.dir, name), ver, name)
        print("[DONE] Database is up-to-date.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
