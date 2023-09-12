# db.py
import sqlite3 # стандартный модуль для БД

# 1 - подключение к БД (connect)
# 2 - создание курсора  (cursor) для запросов к БД
# 3 - запросы( execute)
# 4 - закрытие или сохранение бд


###################################################    создаем таблицу
# CREATE TABLE *название_таблицы*(
#   *название поля* *тип поля* *доп параметры(первичный ключ, уникальное значение и тд)*,
#   *название поля* *тип поля* *доп параметры(первичный ключ, уникальное значение и тд)*,
# 
# )

class DataBase:
    def __init__(self) -> None: # делаю подключение и создаю курсор
        self.con = sqlite3.connect("user.sqlite", check_same_thread=False) # подключение
        # con = sqlite3.connect(r"C:\Users\User\Desktop\bot_dbbbb\user.sqlite")
        self.cur = self.con.cursor() #  создание курсора  (cursor) для запросов к БД

        # CREATE TABLE IF NOT EXISTS  - создание таблицы если она еще не создана

        self.cur.execute("""CREATE TABLE IF NOT EXISTS user(
                        id      INT     PRIMARY KEY,
                        name    TEXT,
                        is_ban  INT
        )
        """) # запрос к БД

        #is_ban = 0 - ЭТО НЕ БАН
        #is_ban = 1 - ЭТО БАН

        self.con.commit() # сохранение
        print("Таблица создана")





    ###################################################    добавляем пользователя
    #INSERT INTO *название таблицы* VALUES (*то что добавляем*)

    def add_user(self, id, name, is_ban):
        #   ? - потом подставлю значение под этот знак
        self.cur.execute("INSERT INTO user VALUES(?,?,?)", (id, name, is_ban)) # запрос к БД

        self.con.commit() # сохранение
        print("Пользователь добавлен")

    # add_user(1, "alex", 0)

    ###################################################    проверка бана

    def check_ban_user(self, id):
        self.cur.execute("SELECT is_ban FROM user WHERE id=?", (id,)) # запрос к БД

        data = self.cur.fetchone() # извлекаю одну записи из БД
        return data # возвращаю данные из функции (1, 'pavel', 0) или None



    ###################################################    извлекаем пользователя 
    # SELECT *то что хотим извлечь* FROM *название таблицы*

    def select_user(self, id):
        self.cur.execute("SELECT * FROM user WHERE id=?", (id,)) # запрос к БД

        data = self.cur.fetchone() # извлекаю одну записи из БД
        return data # возвращаю данные из функции (1, 'pavel', 0) или None


    ###################################################    извлекаем пользователя c баном
    # SELECT *то что хотим извлечь* FROM *название таблицы*

    def select_ban_all_user(self):
        self.cur.execute("SELECT * FROM user WHERE is_ban=1") # запрос к БД

        data = self.cur.fetchone() # извлекаю одну записи из БД
        return data # возвращаю данные из функции (1, 'pavel', 0) или None
    
    ###################################################    извлекаем пользователя c баном
    # SELECT *то что хотим извлечь* FROM *название таблицы*

    def select_unban_all_user(self):
        self.cur.execute("SELECT * FROM user WHERE is_ban=0") # запрос к БД

        data = self.cur.fetchone() # извлекаю одну записи из БД
        return data # возвращаю данные из функции (1, 'pavel', 0) или None



    ###################################################    извлекаем всех пользователей 
    # SELECT *то что хотим извлечь* FROM *название таблицы*

    def select_all_user(self ):
        self.cur.execute("SELECT * FROM user") # запрос к БД

        data = self.cur.fetchall() # извлекаю все записи из БД
        return data # возвращаю данные из функции [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]



    ###################################################    удалить пользователя
    # DELETE FROM *название таблицы* WHERE *условие*


    def delete_user(self, id):
        self.cur.execute("DELETE FROM user WHERE id=?", (id,)) # запрос к БД

        self.con.commit() # сохранение
        print("Пользователь удален")



    # delete_user(4)# при вовторном удалении ошибки не будет



    ###################################################    обновить пользователя
    # UPDATE *название таблицы*  SET   *стобец=новое значение*       WHERE *условие*

    def update_name_user(self, id, name):
        self.cur.execute("UPDATE user SET name=? WHERE id=?", (name, id)) # #запрос + параметры которые подставляются под знак ?

        self.con.commit() # сохранение
        print("Имя пользователя обновлено")

    ###################################################    добавить в бан

    def ban_user(self, id):
        self.cur.execute("UPDATE user SET is_ban=1 WHERE id=?", (id, )) # #запрос + параметры которые подставляются под знак ?

        self.con.commit() # сохранение
        
    ###################################################   разбанить

    def unban_user(self, id):
        self.cur.execute("UPDATE user SET is_ban=0 WHERE id=?", (id, )) # #запрос + параметры которые подставляются под знак ?

        self.con.commit() # сохранение



# update_name_user(3,"Alex")






# print(
#     select_all_user()
# )


















# x = (1,2) # tuple
# y = (1)   # int
# z = (1,)  # tuple
# print(x)
# print(y)
# print(z)
























