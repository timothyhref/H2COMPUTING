import sqlite3
class Person:
    def __init__(self,full_name,date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
    def is_adult(self):
        import datetime
        birth_year = int(self.date_of_birth[:4])
        date = datetime.datetime.now()
        year = date.strftime("%Y")
        return (int(year) - birth_year) > 18
    def screen_name(self):
        name = ""
        for i in range(len(self.full_name)):
            if self.full_name[i].isalpha():
                name += self.full_name[i]
        month = self.date_of_birth[5:7]
        day = self.date_of_birth[-2:]
        return name+month+day

class Staff(Person):
    def __init__(self,full_name,date_of_birth):
        super().__init__(full_name,date_of_birth)
    def screen_name(self):
        name = super().screen_name()
        return name+"Staff"
    def is_adult(self):
        return True
class Student(Person):
    def __init__(self,full_name,date_of_birth):
        super().__init__(full_name,date_of_birth)
    def is_adult(self):
        return False

list =[]
with open("people.txt","r") as file:
    lines = file.readlines()
for line in lines:
    name,date,role = line.strip().split(",")
    if role == "Staff":
        list.append(Staff(name,date))
    elif role == "Student":
        list.append(Student(name,date))
    else:
        list.append(Person(name,date))

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
for item in list:
    cursor.execute('''INSERT INTO People(FullName,DateOfBirth,ScreenName,IsAdult)
    VALUES(?,?,?,?)''',(item.full_name,item.date_of_birth,item.screen_name(),item.is_adult()))
conn.commit()
conn.close()
john = Person("John Tan","2000-06-01")
print(john.is_adult())
print(john.screen_name())

        