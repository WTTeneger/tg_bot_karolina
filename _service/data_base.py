import pymysql
from decouple import config
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
        connection = pymysql.connect(host=config("DB_HOST"), user=config("DB_USER"),
                                     password=config("DB_PASSWORD"), database=config("DB_DATABASE"), charset=config("DB_CHARSET"))
        cursor = connection.cursor()
        cursor.execute(self)
        OTV = cursor.fetchall()
        return(OTV)

    def POST(self):
        """Отправляет данные в Базу данных
        """
        connection = pymysql.connect(host=config("DB_HOST"), user=config("DB_USER"),
                                     password=config("DB_PASSWORD"), database=config("DB_DATABASE"), charset=config("DB_CHARSET"))
        cursor = connection.cursor()
        cursor.execute(self)
        connection.commit()
        return('True')
    
def test():
    print(config('DB_DATABASE'))