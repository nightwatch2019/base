# connect remote mysql server

import pymysql

my_host = "111.230.244.189"
my_user = "nightwatch"
my_password = "3.1415926535@@"

class TestRemoteDB(object):
    "connect remote database"
    db_host = my_host
    db_user = my_user
    db_password = my_password

    def __init__(self, db_db):
        "db_db: database_name"
        self.db_host = TestRemoteDB.db_host
        self.db_user = TestRemoteDB.db_user
        self.db_password = TestRemoteDB.db_password
        self.db_db = db_db

    def __connect(self):
        "connect remote database with arguments"
        self.db = pymysql.connect(self.db_host, self.db_user, self.db_password, self.db_db)
        self.cursor = self.db.cursor()

    def __close(self):
        if self.db:
            self.db.close()

    def select(self, sql):
        self.__connect()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.__close()
        return data
    
def test():
    test_db = TestRemoteDB("nightwatch")
    results = test_db.select("select * from employees")
    print(results)

if __name__ == "__main__":
    test()