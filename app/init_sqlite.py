import os

project_files = {
    "init_sqlite.py": '''\
import os
import sqlite3
import requests
'''
}

def download_sql_file():
    url = "https://drive.google.com/file/d/14uDe4chM0D5RBC10gmzrqPUnY7YkG9re/view?usp=drive_link"
    target_path = "./data/customers.sql"

    if not os.path.exists(target_path):
        print("Downloading large SQL file from Google Drive...")
        r = requests.get(url)
        with open(target_path, "wb") as f:
            f.write(r.content)
        print("Download complete.")

def init_sql():
    os.makedirs("./data", exist_ok=True)
    download_sql_file()
    db_path = "./data/customers.db"
    conn = sqlite3.connect(db_path)
    with open("./data/customers.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("SQLite database initialized successfully.")

if __name__ == "__main__":
    init_sql()