import sqlite3
def init_db():
    # Connect to the database file (creates it if it doesn't exist)
    conn = sqlite3.connect("pub_finder.db")

    # Create a cursor to send commands to the database
    cursor = conn.cursor()

    # Create the table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS domain_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            name TEXT,
            company TEXT,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) 
        """)
    # Save the changes and close the connection
    conn.commit()
    conn.close()

def get_result(domain):
    conn = sqlite3.connect("pub_finder.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, company, email
        FROM domain_profiles
        WHERE domain = ?
     """, (domain,))

    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return {
        "name": row[0],
        "company": row[1],
        "email": row[2]
    }

def save_result(domain, result):
    conn = sqlite3.connect("pub_finder.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO domain_profiles (domain, name, company, email)
        VALUES (?, ?, ?, ?) 
    """, (
        domain,
        result.get("name"),
        result.get("company"),
        result.get("email")
    ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialised")
    
    # Test saving a result
    fake_result = {
        "name": "Pompignoli Marco",
        "company": "UNIDAD EDITORIAL REVISTAS, S.L.U.",
        "email": "domain-admin-contact@unidadeditorial.es"
    }
    save_result("diariomedico.com", fake_result)
    print("Result saved")
    
    # Test retrieving it
    retrieved = get_result("diariomedico.com")
    print(retrieved)
    
    # Test a domain that does not exist
    missing = get_result("notindatabase.com")
    print(missing)  