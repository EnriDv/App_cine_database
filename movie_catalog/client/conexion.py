import oracledb

class Conect:
    def __init__(self):
        self.con = oracledb.connect(user='System', password='ucbdatabase', dsn='localhost:1521/xe')
        self.cursor = self.con.cursor()

    def exit(self):
        self.cursor.close()
        self.con.close()

