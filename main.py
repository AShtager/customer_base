import elaboration_bd
import administrator_bd


def select_func():
    """
    Функция основного меню, запрашиваем какие действия нужно совершить, изходя из ответа запускаем соответствующие функции.
    """
    team = ("""
        Вы находитесь в основном меню.
        Вам доступны следующие операции.
            
        Создать новую базу данных нажмите - 1.
        Удалить базу данных - 2.
        Создать таблицы - 3.
        Добавить нового клиента - 4.
        Добавить номер телефона существующему клиенту - 5.
        Удалить номер телефона клиента - 6
        Для изменения данных клиента нажмите - 7.
        Поиск клиента - 8.
        Для вызова справки нажмите - h.    
        Для выхода нажмите - q.
            """)
    print(team)
    
    admin_answer = input("Введите команду: ").lower()

    while True:
        if admin_answer == "1":
            elaboration_bd.admin_1.create_bd()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower() 
        
        elif admin_answer == "2":
            elaboration_bd.admin_1.delete_bd()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()
        
        elif admin_answer == "3":
            elaboration_bd.admin_1.create_table()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()
        
        elif admin_answer == "4":
            administrator_bd.admin_2.new_client()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()
        
        elif admin_answer == "5":
            administrator_bd.admin_2.adeded_num()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()

        elif admin_answer == "6":
            administrator_bd.admin_2.delete_num()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()

        elif admin_answer == "7":
            administrator_bd.admin_2.modify_client()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()

        elif admin_answer == "8":
            administrator_bd.admin_2.find_client()
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()

        elif admin_answer == "h" or admin_answer == "р":
            elaboration_bd.sleep(2)
            print(team)
            admin_answer = input("Введите команду: ").lower()

        elif admin_answer == "q" or admin_answer == "й":
            elaboration_bd.admin_1.conn.close()
            print()
            print("Работа программы завершена.")
            print("Спасибо что выбрали нас. С любовью Schultz.корпорейшн ©")
            break
       
        else:
            print("Нет такой команды.")
            print("Для вызова справки нажмите - h.")
            admin_answer = input("Введите команду: ").lower()   

select_func()