import psycopg2
from time import sleep


class ConstructorBD():
    """
    Класс взаимодействует с базой данных. функция create_bd создает базу данных. Функция delete_bd удаляет базу данных.
    Функция create_table запрашивает им бд и создает там таблицы. 
    """
 
    def __init__(self):

        self.dbname = input("Введите название бд: ")
        self.user = input("Введите имя пользователя: ")
        self.password = input("Введите пароль: ")
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password)

    def create_bd(self):
        """
        Создается новая бд, админ указывает имя создаваемой бд. После перезагрузки вводим название бд которую создали.
        """
        name_bd = input("Введите название базы данных: ")
        create_bd = f"CREATE DATABASE {name_bd}"
        self.conn.autocommit = True
        
        with self.conn.cursor() as cur:
            cur.execute(create_bd)
            print(f"База данных {name_bd} успешно созданна.")
            print("Требуется перезагрузка программы.")
            sleep(1)

    def delete_bd(self):
        """
        Админ указывает имя бд которую не обходимо удалить. После подтверждения бд удаляется.
        """
        name_bd = input("Введите название бд которую хотите удалить: ")
        print(f"ВНИМАНИЕ! Вы действительно хотите удалить бд {name_bd} на всегда.")
        admin_answer = input("Введите (yes/no): ")
        self.conn.autocommit = True
        
        if admin_answer == "yes":
            with self.conn.cursor() as cur:
                cur.execute(f"DROP DATABASE {name_bd};")
            print(f"БД {name_bd} успешно удалена.")
            sleep(1)
        elif admin_answer == "no":
            return

    def create_table(self):
        """
        Админ вводит название бд в которой необходимо создать таблицы. Если таблицы уже присутствуют в данной бд, то они обнуляются.
        """
        name_bd = input("Введите название бд, в которой нужно создать таблицы: ")
        conn = psycopg2.connect(dbname=name_bd, user=self.user, password=self.password)
        conn.autocommit = True
        
        with conn.cursor() as cur:
            cur.execute("""
                    DROP TABLE IF EXISTS client_phone;
                    DROP TABLE IF EXISTS client;
                    """)

            cur.execute("""
                    CREATE TABLE IF NOT EXISTS client(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(40) NOT NULL,
                        last_name VARCHAR(80) NOT NULL,
                        email VARCHAR(80) NOT NULL
                    );
                    """)

            cur.execute("""
                    CREATE TABLE IF NOT EXISTS client_phone(
                        id SERIAL PRIMARY KEY,
                        client_id INTEGER NOT NULL REFERENCES client(id),
                        number VARCHAR(30) NOT NULL
                    );
                    """)
            print("Таблицы успешно созданны.")
            sleep(1)
            
        
admin_1 = ConstructorBD()




