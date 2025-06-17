class Pavlo:
    def init(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.start_age = 15

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        course = age - self.start_age
        return max(0, min(course, 4))

    def get_name_list(self):
        return [self.first_name, self.last_name]


class Student(Pavlo):
    def init(self, first_name=None, last_name=None, birth_year=None,
             college=None, specialty=None, record_book_number=None):
        super().init(first_name, last_name, birth_year)
        self.college = college
        self.specialty = specialty
        self.record_book_number = record_book_number

    def get_full_info(self):
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Коледж": self.college,
            "Спеціальність": self.specialty,
            "Номер залікової книжки": self.record_book_number,
            "Курс": self.calculate_course()
        }

    def _calculate_age(self):
        if self.birth_year is None:
            return None
        return 2025 - self.birth_year


student = Student(
    first_name="Павло",
    last_name="Безушкевич",
    birth_year=2008,
    college="ТФК ЛНТУ",
    specialty="ІСТ",
    record_book_number="ZK987654")

student.start_age = 17

print(student.get_full_info())
print("Вік:", student._calculate_age())
