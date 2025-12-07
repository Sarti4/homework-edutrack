class Student:
    def __init__(self, name, age, grade, avg_score):
        self.name = name
        self.age = age
        self.grade = grade
        self.avg_score = avg_score

    def update_score(self, new_score):
        self.avg_score = new_score

    def promote(self):
        self.grade += 1

    def get_info(self):
        return f"Учень: {self.name}, Вік: {self.age}, Клас: {self.grade}, Середній бал: {self.avg_score}"


students = []

while True:
    print("\n--- Меню ---")
    print("1 — Додати учня")
    print("2 — Показати всіх учнів")
    print("3 — Оновити середній бал")
    print("4 — Перевести учня в наступний клас")
    print("0 — Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Ім'я: ")
        age = int(input("Вік: "))
        grade = int(input("Клас: "))
        avg_score = float(input("Середній бал: "))

        student = Student(name, age, grade, avg_score)
        students.append(student)
        print(" Учня додано!")

    elif choice == "2":
        if not students:
            print("Список порожній.")
        else:
            for i, student in enumerate(students, 1):
                print(i, student.get_info())

    elif choice == "3":
        if not students:
            print("Немає учнів.")
            continue

        index = int(input("Номер учня: ")) - 1
        new_score = float(input("Новий середній бал: "))
        students[index].update_score(new_score)
        print(" Бал оновлено!")

    elif choice == "4":
        if not students:
            print("Немає учнів.")
            continue

        index = int(input("Номер учня: ")) - 1
        students[index].promote()
        print(" Учня переведено в наступний клас!")

    elif choice == "0":
        print("Програму завершено.")
        break

    else:
        print(" Невірний вибір!")
