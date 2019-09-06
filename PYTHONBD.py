import sqlite3



# ...and read it back into a blob
with open('imagen.jpg', 'rb') as f:
  ablob = f.read()

# OK, now for the DB part: we make it...:
db = sqlite3.connect('prueba_blob.sqlite')
db.execute('INSERT INTO imagenes(imagen, tipo) VALUES(?, ?)', [sqlite3.Binary(ablob), "image/jpeg"])
db.commit()
db.close()

# ...and read it back:
db = sqlite3.connect('prueba_blob.sqlite')
row = db.execute('SELECT * FROM imagenes').fetchone()
print (repr(str(row[0])))