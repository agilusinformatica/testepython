from db import sql

resultado = sql.query("insert into ClientesTeste (Nome, Email) values ('Claudio A. C.', 'claudio@teste.com')")

print(resultado)