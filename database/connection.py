import pymysql

def getMySQLConnection(
        host,
        port,
        username, 
        password,
        db,
        charset='utf8'
    ):
    return pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=db,
            charset=charset
        )