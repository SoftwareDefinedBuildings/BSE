import psycopg2
import psycopg2.extras
import re

db = psycopg2.connect( # Connect to PostgreSQL Database.
    host = 'localhost',
    database = 'testdb',
    user = 'testuser',
    password = 'testuser'
)

psycopg2.extras.register_hstore(db)
cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor) 
my_dict = {
	'First Key': 'First Value',
	'Second Key': 'Second Value'
}
string_to_store = str(my_dict)
string_to_store = re.sub("\'","\"",string_to_store)
print string_to_store

#cursor.execute("INSERT INTO test1 (id,uuid,metadata) VALUES (2,'abc',%s)", [my_dict] )
#db.commit()

cursor.execute("SELECT metadata FROM test1")
print cursor.fetchone()
d= cursor.fetchone()
print "Metadata : ",d["metadata"]
