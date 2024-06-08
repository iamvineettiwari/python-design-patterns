from FactoryMethodPattern.Creator.AccountingDepartment import AccountingDepartment
from FactoryMethodPattern.Creator.ITDepartment import ITDepartment


def main():
    it_department = ITDepartment()
    accounting_department = AccountingDepartment()

    emp_one = it_department.create_employee(first="John", last="Doe", base=20000)
    emp_two = it_department.create_employee(first="Alex", last="Smith", base=20000)
    emp_three = accounting_department.create_employee(first="John", last="William", base=20000)

    emp_one.show_info()
    emp_one.do_work()

    print()

    emp_two.show_info()
    emp_two.do_work()

    print()

    emp_three.show_info()
    emp_three.do_work()

    print()


if __name__ == '__main__':
    main()