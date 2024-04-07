import elaboration_bd
import psycopg2


class AdminBD():

    def __init__(self, user=elaboration_bd.admin_1.user, password=elaboration_bd.admin_1.password):
        self.user = user
        self.password = password

    def new_client(self):
        """
        Добавить нового клиента. если указать его номер телефона, номмер сохранится в другой таблице. 
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        self.conn.autocommit = True
        name = input("Введите имя клиента: ")
        last_name = input("Введите фамилию клиента: ")

        email = input("Введите email: ")

        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO client(name, last_name, email) VALUES(%s, %s, %s);
                    """, (name, last_name, email)
                    )
            print("Клиент успешно добавлен.")
            elaboration_bd.sleep(1)

        phone_number = input(f"Введите номер телефона для {name} или нажмите Enter: ")
        if len(phone_number) > 0:
            with self.conn.cursor() as cur:
                
                cur.execute("""SELECT id FROM client
                            WHERE name=%(name)s AND last_name=%(last_name)s;""", 
                            ({"name": name, "last_name": last_name}))
                id_client = cur.fetchone()

                cur.execute("""
                        INSERT INTO client_phone(client_id, number) VALUES(%s, %s);  
                        """, (id_client, phone_number))
                print("Номер телефона упешно добовлен.")
                elaboration_bd.sleep(1)
        self.conn.close()

    def adeded_num(self):
        """
        Добавляем номер существующему клиенту по его id.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        self.conn.autocommit = True
        data_client = input("Введите id клиента: ")
        phone_number = input("Введите номер клиента: ")
        
        with self.conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO client_phone(client_id, number) VALUES(%s, %s);
                    """, (data_client, phone_number))
            print("Номер успешно добавлен.")
            elaboration_bd.sleep(1)
        self.conn.close()
        
    def delete_num(self):
        """
        Удаляем номер телефона. 
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        self.conn.autocommit = True
        client_phone = input("Введите номер телефона который нужно удалить: ")
        
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM client_phone
                    WHERE number=%s;""", (client_phone,))
        print("Номер успешно удален.")
        self.conn.close()
        elaboration_bd.sleep(1)

    def update_name(self):
        """
        Обновить имя существующего клиента.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        
        id_client = input("Введите id клиента: ")
        new_name = input("Введите новое имя клиента: ")
        
        with self.conn.cursor() as cur:
            cur.execute("UPDATE client SET name=%s WHERE id=%s", (new_name.title(), id_client))
            self.conn.commit()
        print("Имя успешно изменнено.")
        self.conn.close()
        elaboration_bd.sleep(2)

    def update_last_name(self):
        """
        Обновить фамилию существующего клиента.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)

        id_client = input("Введите id клиента: ")
        new_last_name = input("Введите новую фамилию: ")

        with self.conn.cursor() as cur:
            cur.execute("UPDATE client SET last_name=%s WHERE id=%s", (new_last_name.title(), id_client))
            self.conn.commit()
        print("Фамилия успешно изменена.")
        self.conn.close()
        elaboration_bd.sleep(1)

    def update_email(self):
        """
        Обновить email существующего клиента.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)

        id_client = input("Введите id клиента: ")
        new_email = input("Введите новый email: ")

        with self.conn.cursor() as cur:
            cur.execute("UDATE client SET email=%s WHERE id=%s", (new_email, id_client))
        print("email успешно изменен.")
        self.conn.close()
        elaboration_bd.sleep(1)

    def modify_client(self):
        """
        Функция которая узнает какие данные мы хотим изменить, изходя из нашего ответа запускает соответствующую функцию для 
        изменения данных.
        """
        team = """
        Вы находтьесь в меню изменения данных.
        Для того что бы изменить имя нажмите - 1.
        Для того что бы изменить фамилию нажмите - 2.
        Для того что бы изменить email нажмите - 3.
        Для выхода в основное меню нажмите - 4.
        """
        print(team)
        
        answer = int(input("Введите команду: "))
        
        while True:
            if answer == 1:
                self.update_name()
                break
            elif answer == 2:
                self.update_last_name()
                break
            elif answer == 3:
                self.update_email()
                break
            elif answer == 4:
                break
            else:
                print("Нет такой команды.")
                print(team)
                answer = int(input("Введите команду: "))
    
    def find_name(self):
        """
        Поиск клиентов по имени.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        name = input("Введите имя: ").title()

        with self.conn.cursor() as cur:
            cur.execute("""
                    SELECT * FROM client
                    WHERE name=%s;""", (name,)
                    )
            name_all = cur.fetchall()
            elaboration_bd.sleep(1)
            print("Результаты поиска.")
            print(*name_all, sep="\n")
        self.conn.close()

    def find_last_name(self):
        """
        Поиск клиентов по фамилии.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        last_name = input("Введите фамилию: ")

        with self.conn.cursor() as cur:
            cur.execute("""
                    SELECT * FROM client
                    WHERE last_name=%s;""", (last_name,)
                    )
            last_name_all = cur.fetchall()
            elaboration_bd.sleep(1)
            print("Результаты поиска.")
            print(*last_name_all, sep="\n")
        self.conn.close()

    def find_email(self):
        """
        Поиск клиентов по email.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        email = input("Введите email: ")

        with self.conn.cursor() as cur:
            cur.execute("""
                    SELECT * FROM client
                    WHERE email=%s;""", (email,)
                    )
            email_all = cur.fetchall()
            elaboration_bd.sleep(1)
            print("Результаты поиска.")
            print(*email_all, sep="\n")
        self.conn.close()

    def find_phone_number(self):
        """
        Поиск клиентов по номеру телефона.
        """
        self.conn = psycopg2.connect(dbname=elaboration_bd.admin_1.dbname, user=self.user, password=self.password)
        phone_number = input("Введите номер телефона: ")

        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM client
                        WHERE id IN (SELECT client_id FROM client_phone
                        WHERE number=%s)""", (phone_number,))
            phone_number_all = cur.fetchall()
            elaboration_bd.sleep(1)
            print("Результаты поиска.")
            print(*phone_number_all, sep="\n")
        self.conn.close()
        
    def find_client(self):
        """
        Функция запрашивать у пользователя по каким данным искать клиентов. Изходя из ответа запускает соответствующую 
        функцию для поиска.
        """
        team = """
        Вы находитесь в меню поиска клиента.
        Для того что бы начать поиск по имени нажмите - 1.
        Для того что бы начать поиск по фамилии нажмите - 2.
        Для того что бы начать поиск по email - 3.
        Для того что бы начать поиск по номеру телефона нажмите - 4.
        Для выхода в основное меню нажмите - 5.
        """
        print(team)

        answer = int(input("Введите команду: "))

        while True:
            
            if answer == 1:
                self.find_name()
                break
            elif answer == 2:
                self.find_last_name()
                break
            elif answer == 3:
                self.find_email()
                break
            elif answer == 4:
                self.find_phone_number()
                break
            elif answer == 5:
                break
            else:
                print("Нет такой команды.")
                print(team)
                answer = int(input("Введите команду: "))


admin_2 = AdminBD()
