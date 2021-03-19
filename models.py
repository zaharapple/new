import datetime
import math


class Employee:
    def __init__(self, name, zp_day, days):
        self.name = name
        self.zp_day = zp_day
        self.days = days

    def work(self):
        return "I come to the office"

    def cheak_salary(self):
        def zp(zp_day):
            data_now = datetime.date.today()
            delta = datetime.timedelta(1)
            first_day = data_now.replace(day=1)

            days = 0
            while first_day != data_now:
                if first_day.isoweekday() not in (6, 7):
                    days += 1
                first_day += delta
            return zp_day * days + zp_day

        zp_now = zp(self.zp_day)
        zp_month = Employee.zp_month_calc(self)
        return f"Зарплата за месяц: {zp_month}. Зарплата на текущий рабочий день: {zp_now}"

    def zp_month_calc(self):
        return self.zp_day * self.days

    def __gt__(self, other):
        return self.zp_month_calc() > other.zp_month_calc()

    def __ge__(self, other):
        return self.zp_month_calc() >= other.zp_month_calc()

    def __lt__(self, other):
        return self.zp_month_calc() < other.zp_month_calc()

    def __le__(self, other):
        return self.zp_month_calc() <= other.zp_month_calc()

    def __eq__(self, other):
        return self.zp_month_calc() == other.zp_month_calc()

    def __ne__(self, other):
        return self.cheak_salary() != other.cheak_salary()


class Recruiter(Employee):

    def work(self):
        return 'I come to the office and start to hiring.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class Programmer(Employee):

    def __init__(self, name, zp_day, days, tech_stack):
        super().__init__(name, zp_day, days)
        self.tech_stack = tech_stack

    def work(self):
        return 'I come to the office and start to coding.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        tech_stack = self.tech_stack | other.tech_stack
        name = self.name + other.name
        zp_day = self.zp_day + other.zp_day
        day = math.ceil((self.days + other.days) / 2)
        return Programmer(name, zp_day, day, tech_stack)


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f"""{self.__class__.__name__} : {self.full_name} 
            адресс: {self.email} 
            на должность: {self.technologies} , main_skill: {self.main_skill} на уровне {self.main_skill_grade}       
        """


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return f"""{self.__class__.__name__} : {self.title} 
            Главное знание: {self.main_skill} 
            Уровень: {self.main_skill_level}       
        """
