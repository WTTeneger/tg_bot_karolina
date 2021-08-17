import pymysql
from _settings import env
# print()

class DB():
    
    """Работа с Базой данных
    получить данные::

        DB.GET('Текст запроса SQL')
    отправить данные::

        DB.POST('Текст запроса SQL')
    """

    def GET(self):
        """Получает данные с Базы данных
        """
        connection = pymysql.connect(host=env.DB_HOST, user=env.DB_USER,
                                     password=env.DB_PASSWORD, database=env.DB_DATABASE, charset=env.DB_CHARSET)
        cursor = connection.cursor()
        cursor.execute(self)
        OTV = cursor.fetchall()
        return(OTV)

    def POST(self):
        """Отправляет данные в Базу данных
        """
        connection = pymysql.connect(host=env.DB_HOST, user=env.DB_USER,
                                     password=env.DB_PASSWORD, database=env.DB_DATABASE, charset=env.DB_CHARSET)
        cursor = connection.cursor()
        cursor.execute(self)
        connection.commit()
        return('True')
    
def test():
    print(env.DB_DATABASE)