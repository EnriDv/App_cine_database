import oracledb

try: 
    con = oracledb.connect(user='System', password='ucbdatabase', dsn='localhost:1521/xe')
    cursor = con.cursor()
    print('FELICIDADES')
except:
    print('ERROR')



def query():
    try:
        cursor.execute(""" select * from ACCOUNT """)
        
        row = cursor.fetchall()

        print(row)
        
        for r in row:
            print(r)

        print('EXITO')
        

    except:
        print('ERROR')

query()

def exit():
    cursor.close()
    con.close()