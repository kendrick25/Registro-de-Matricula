import mysql.connector
class DataBase:
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "matricula"
            )
            self.cursor=self.connection.cursor()
        except Exception as ex:
            print(ex)