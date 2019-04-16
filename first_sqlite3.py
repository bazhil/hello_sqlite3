import sqlite3
from Employee import Employee

def insert_emp(emp):
    """
    Функция которая вставляет данные работника в БД
    :param emp: экземпляр объекта Employee
    :return:
    """
    with conn:
        c.execute("INSERT INTO employees Values (?, ?, ?)", (emp.firstname, emp.lastname, emp.pay))

def get_epms_by_lastname(lastname):
    """
    Функция, которая осуществляет поиск работника в БД по фамилии
    :param lastname: фамилия
    :return: все сотрудники с фамилией lastname
    """
    c.execute("SELECT * FROM employees WHERE lastname=:lastname", {'lastname': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    """
    Функция, которая обновляет заработную плату работника в БД
    :param emp: экземпляр объекта Employee
    :param pay: Величина новой заработной платы
    :return:
    """
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE firstname = :firstname AND lastname = :lastname""",
                  {'firstname': emp.firstname, 'lastname': emp.lastname, 'pay': pay})

def remove_emp(emp):
    """
    Функция, которая удаляет работника из БД
    :param emp:
    :return:
    """
    with conn:
        c.execute("DELETE FROM employees WHERE firstname = :firstname AND lastname = :lastname",
                  {'firstname': emp.firstname, 'lastname': emp.lastname})


if __name__ = '__main__':
    conn = sqlite3.connect('employee.db')

    c = conn.cursor()

    #  Создание БД
    # c.execute("""CREATE TABLE employees (
    #             firstname text,
    #             lastname text,
    #             pay interger)""")

    emp_1 = Employee('Ivan', 'Ivanov', 10000)
    emp_2 = Employee('Igor', 'Ivanov', 10000)
    emp_3 = Employee('Sergey', 'Sidorov', 10000)
    emp_4 = Employee('Anton', 'Ivanov', 12000)

    insert_emp(emp_1)
    insert_emp(emp_2)
    insert_emp(emp_3)
    insert_emp(emp_4)

    emps = get_epms_by_lastname('Ivanov')
    print(emps)

    update_pay(emp_2, 15000)

    emps = get_epms_by_lastname('Ivanov')
    print(emps)

    remove_emp(emp_4)

    c.execute("SELECT * FROM employees")
    print(c.fetchall())

    conn.close()