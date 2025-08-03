class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = self.set_health_rate(healthRate)

    def set_health_rate(self, rate):
        return max(0, min(100, rate))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10



class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = max(1000, salary)
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)

    def send_mail(self, to, subject, body):
        print(f"Sending email to: {to}\nSubject: {subject}\nBody: {body}")
class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = self.set_fuel_rate(fuelRate)
        self.velocity = self.set_velocity(velocity)

    def set_velocity(self, v):
        return max(0, min(200, v))

    def set_fuel_rate(self, f):
        return max(0, min(100, f))

    def run(self, velocity, distance):
        self.velocity = self.set_velocity(velocity)
        fuel_needed = (distance / 10) * 10
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            actual_distance = (self.fuelRate / 10) * 10
            self.fuelRate = 0
            self.stop(distance - actual_distance)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance == 0:
            print("You have arrived at your destination.")
        else:
            print(f"Car stopped. Remaining distance: {remain_distance} km.")



class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = self.set_fuel_rate(fuelRate)
        self.velocity = self.set_velocity(velocity)

    def set_velocity(self, v):
        return max(0, min(200, v))

    def set_fuel_rate(self, f):
        return max(0, min(100, f))

    def run(self, velocity, distance):
        self.velocity = self.set_velocity(velocity)
        fuel_needed = (distance / 10) * 10
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            actual_distance = (self.fuelRate / 10) * 10
            self.fuelRate = 0
            self.stop(distance - actual_distance)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance == 0:
            print("You have arrived at your destination.")
        else:
            print(f"Car stopped. Remaining distance: {remain_distance} km.")




class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = self.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num



# 1. إنشاء السيارة
samy_car = Car(name="Fiat 128", fuelRate=100, velocity=80)

# 2. إنشاء الموظف سامي
samy = Employee(
    name="Samy",
    money=1000,
    mood="",
    healthRate=100,
    emp_id=1,
    car=samy_car,
    email="samy@iti.org",
    salary=5000,
    distanceToWork=20
)


iti_office = Office(name="ITI Smart Village")
iti_office.hire(samy)

move_hour = 8.5 

iti_office.check_lateness(empId=1, moveHour=move_hour)

samy.drive(20)

print(f"\nEmployee Info After Drive:")
print(f"Name: {samy.name}")
print(f"Mood: {samy.mood}")
print(f"Fuel Remaining: {samy.car.fuelRate}%")
print(f"Salary: {samy.salary} L.E")
