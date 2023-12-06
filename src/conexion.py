import oracledb

try: 
    con = oracledb.connect(user='System', password='ucbdatabase', dsn='DESKTOP-6TGSEQQ/XE')
    cursor = con.cursor()
    print('FELICIDADES')
except:
    print('ERROR')



def query():
    try:
        cursor.execute(""" select ID from account_""")
        
        row = cursor.fetchall()

        print(row)
        
        for r in row:
            print(r)

        print('EXITO')
        

    except:
        print('ERROR')

query()

cursor.close()
con.close()