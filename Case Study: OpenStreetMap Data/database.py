import csv
import psycopg2

conn = psycopg2.connect("host=127.0.0.1 san_francisco.db")
cur = conn.cursor()

# create nodes table
cur.execute(
    "CREATE TABLE nodes (id, lat, lon, user, uid, version, changeset, timestamp);")
with open('nodes.csv', 'rb') as f:
    d = csv.DictReader(f)
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp'])
             for i in d]

cur.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()

# create nodes_tags table
cur.execute("CREATE TABLE nodes_tags (id, key, value, type);")
with open('nodes_tags.csv', 'rb') as f:
    d = csv.DictReader(f)
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in d]

cur.executemany(
    "INSERT INTO nodes_tags (id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
conn.commit()

# Create ways table
cur.execute("CREATE TABLE ways (id, user, uid, version, changeset, timestamp);")
with open('ways.csv', 'rb') as f:
    d = csv.DictReader(f)
    to_db = [(i['id'], i['user'], i['uid'], i['version'],
              i['changeset'], i['timestamp']) for i in d]

cur.executemany(
    "INSERT INTO ways (id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
conn.commit()

# Create ways_nodes table
cur.execute("CREATE TABLE ways_nodes (id, node_id, position);")
with open('ways_nodes.csv', 'rb') as f:
    d = csv.DictReader(f)
    to_db = [(i['id'], i['node_id'], i['position']) for i in d]

cur.executemany(
    "INSERT INTO ways_nodes (id, node_id, position) VALUES (?, ?, ?);", to_db)
conn.commit()

# Create ways_tags table
cur.execute("CREATE TABLE ways_tags (id, key, value, type);")
with open('ways_tags.csv', 'rb') as f:
    d = csv.DictReader(f)
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in d]

cur.executemany(
    "INSERT INTO ways_tags (id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
conn.commit()
