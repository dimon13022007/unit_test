# перший варіант


class Employee:
    def __init__(self, firstname, lastname, patronymic, phone, gmail):
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.phone = phone
        self.gmail = gmail

    def showInfo(self):
        print(f'Employee first name - {self.firstname}')
        print(f'Employee last name - {self.lastname}')
        print(f'Employee patronymic - {self.patronymic}')
        print(f'Employee phone - {self.phone}')
        print(f'Employee gmail - {self.gmail}')
        return f'Employee first name - {self.firstname}' \
               f'Employee last name - {self.lastname}' \
               f'Employee patronymic - {self.patronymic}' \
               f'Employee phone - {self.phone}' \
               f'Employee gmail - {self.gmail}'

    # def showInfo4(self):
    #     print(f'Best employee - {self.firstname} {self.lastname}')


class Auto:
    def __init__(self, carname, release, model, sale_price):
        self.carname = carname
        self.release = release
        self.model = model
        self.sale_price = sale_price

    def showInfo1(self):
        print(f'Car name - {self.carname}')
        print(f'Car release - {self.release}')
        print(f'Car model - {self.model}')
        print(f'Sale price - {self.sale_price}')
        return f'Car name - {self.carname}' \
               f'Car release - {self.release}' \
               f'Car model - {self.model}' \
               f'Sale price - {self.sale_price}'

    def showInfo5(self):
        print(f'the car that sells the most - {self.carname}')


class Sales(Employee, Auto):
    def __init__(self, firstname, lastname, patronymic, phone, gmail, carname, release, model, sale_price, date_of_sale,
                 actual_seeling_price):
        self.date_of_sale = date_of_sale
        self.actual_seeling_price = actual_seeling_price
        Employee.__init__(self, firstname, lastname, patronymic, phone, gmail)
        Auto.__init__(self, carname, release, model, sale_price)
        # Sales.__init__(self, firstname, lastname, patronymic, phone, gmail, carname, release, model, sale_price,
        # date_of_sale, actual_selling_price)

    def showInfo2(self):
        print(f'Employee first name - {self.firstname}')
        print(f'Employee last name - {self.lastname}')
        print(f'Employee patronymic - {self.patronymic}')
        print(f'Employee phone - {self.phone}')
        print(f'Employee gmail - {self.gmail}')
        print(f'Car name - {self.carname}')
        print(f'Car release - {self.release}')
        print(f'Car model - {self.model}')
        print(f'Sale price - {self.sale_price}')
        print(f'Date of sale {self.date_of_sale}')
        print(f'Actual selling price - {self.actual_seeling_price}')
        return f'Employee first name - {self.firstname}' \
               f'Employee last name - {self.lastname}' \
               f'Employee patronymic - {self.patronymic}' \
               f'Employee phone - {self.phone}' \
               f'Employee gmail - {self.gmail}' \
               f'Car name - {self.carname}' \
               f'Car release - {self.release}' \
               f'Car model - {self.model}' \
               f'Sale price - {self.sale_price}' \
               f'Date of sale {self.date_of_sale}' \
               f'Actual selling price - {self.actual_seeling_price}'


emplo = Employee('Vlad', 'Kuriluk', 'Antonovich', '+380236844', 'sdggghc213@gmail.com')
# emplo.showInfo()
auto = Auto('Audi', 2021, 'Q7', 30000)
# auto.showInfo1()
sales = Sales('Vlad', 'Kuriluk', 'Antonovich', '+380236844', 'sdggghc213@gmail.com', 'Audi', 2021, 'Q7', 30000,
              '13.02.2023', 90000)

# sales.showInfo2()
choice = int(input('1 - employee/ 2 - car/ 3 - sales/ 4 employee info in file/ 5 car info in file/ 6 sales info in '
                   'file/ 7 best employee/ 8 the best-selling car: '))
file = open('File5.txt', 'w')
car_cost = 90000
if choice == 1:
    emplo.showInfo()
if choice == 2:
    auto.showInfo1()
if choice == 3:
    sales.showInfo2()
if choice == 4:
    file.write(emplo.showInfo())
if choice == 5:
    file.write(auto.showInfo1())
if choice == 6:
    file.write(sales.showInfo2())
# if choice == 7:
#     emplo.showInfo4()
if choice == 8:
    auto.showInfo5()
else:
    print('Вы ввели неправильное число')

sale_data = int(input('Enter sale month: '))
if sale_data == 2:
    print(f'Total profit - {car_cost * 90}')
else:
    print(f'Total profit - {car_cost * 400}')
sale_day = int(input('Enter sale day: '))
if sale_day <= 3:
    print(f'Today we received - {car_cost * 6}')

if sale_day >= 15:
    print(f'Today we received - {car_cost * 4}')













