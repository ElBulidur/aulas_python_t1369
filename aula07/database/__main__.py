from distutils.log import error
import mysql.connector

try:
    senha = 'root' #
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port =3306,
        user='root', 
        password='871ce144069ea0816545f52f09cd135d1182262c3b235808fa5a3281',  
        database='db_funcionario'
    )
    
    print('Conexao OK')
except mysql.connector.Error as erro:
    print(erro)


# CRUD - CREATE, READ, UPDATE, DELETE  (SQL)

