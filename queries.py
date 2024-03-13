from data_generator import GENRE, COVER

GENRES = ", ".join(f"'{genre}'" for genre in GENRE)
COVERS = ", ".join(f"'{cover}'" for cover in COVER)

delete_table = f'''CREATE TABLE IF NOT EXISTS books
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        length INTEGER,
                        genre TEXT CHECK (genre IN ({GENRES})),
                        cover TEXT check (cover in  ({COVERS})))'''

insert_many = "INSERT INTO books (name, length, genre, cover) VALUES (?, ?, ?, ?)"

get_average_length = "SELECT AVG(length) FROM books"

get_max_length = "SELECT name FROM books ORDER BY length DESC LIMIT 1"

select_all = "SELECT * FROM books"

QUERIES = {
    "create_table": delete_table,
    "insert_many": insert_many,
    "get_average_length": get_average_length,
    "get_max_length": get_max_length,
    "select_all": select_all,
}
