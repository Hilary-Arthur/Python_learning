import MysqlConnector as connector


class SqlServlet:
    db, cursor = connector.mysql_Conn()
    def insert_data(self,cursor,data):
        sql = ""
        cursor.excute