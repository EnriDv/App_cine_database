import oracledb

try: 
    connection = oracledb.connect(user='System', password='ucbdatabase', dsn='DESKTOP-6TGSEQQ/XE')
    cursor = connection.cursor()
    print('FELICIDADES')
except:
    print('ERROR')

try:
    cursor.execute("""
                   select * from USSER
                   """)
    for i in len(cursor):
        print(cursor)
        cursor+=1

    print('hola')
    
except:
    print('ERROR')

cursor.close()
connection.close()