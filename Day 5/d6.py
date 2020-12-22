from abc import ABCMeta, abstractmethod

Incentives = {"A": 4, "B": 6, "C": 10, "D": 13, "E": 16, "F": 20}

Sme_bonus = {"AGP": 6500, "AGPT": 8200, "AGDEV": 11500}


class Employee(metaclass=ABCMeta):
    def __init__(self, job_band, employee_name, basic_salary, qualification):
        self.__job_band = job_band
        self.__employee_name = employee_name
        self.__basic_salary = basic_salary
        self.__qualification = qualification

    def get_job_band(self):
        return self.__job_band

    def get_employee_name(self):
        return self.__employee_name

    def get_basic_salary(self):
        return self.__basic_salary

    def get_qualification(self):
        return self.__qualification

    @abstractmethod
    def validate_job_band(self):
        pass

    def validate_basic_salary(self):
        if self.__basic_salary > 3000:
            return True
        else:
            return False

    def validate_qualification(self):
        if self.__qualification in ["Bachelors", "Masters"]:
            return True
        else:
            return False

    @abstractmethod
    def calculate_gross_salary(self):
        pass


class Graduate(Employee):
    def __init__(self, job_band, employee_name, basic_salary, qualification, cgpa):
        super(Graduate, self).__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa = cgpa

    def get_cgpa(self):
        return self.__cgpa

    def validate_job_band(self):
        if self.get_job_band() in ["A", "B", "C"]:
            return True
        return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.get_basic_salary()
            incentive = Incentives[self.get_job_band()] * self.get_basic_salary() / 100
            tpi_amount = 0
            if 4 <= self.__cgpa <= 4.25:
                tpi_amount = 1000
            elif 4.26 <= self.__cgpa <= 4.5:
                tpi_amount = 1700
            elif 4.51 <= self.__cgpa <= 4.75:
                tpi_amount = 3200
            elif 4.76 <= self.__cgpa <= 5:
                tpi_amount = 5000

            gross_salary = self.get_basic_salary() + pf + tpi_amount + incentive

            return gross_salary
        return -1


class Lateral(Employee):
    def __init__(self, job_band, employee_name, basic_salary, qualification, skill_set):
        super(Lateral, self).__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set = skill_set

    def get_skill_set(self):
        return self.__skill_set

    def validate_job_band(self):
        if self.get_job_band() in ["D", "E", "F"]:
            return True
        return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.get_basic_salary()
            incentive = Incentives[self.get_job_band()] * self.get_basic_salary() / 100
            sme_bonus = Sme_bonus[self.get_skill_set()]
            gross_salary = self.get_basic_salary() + pf + sme_bonus + incentive

            return gross_salary
        return -1


Grad = Graduate("A", "Shreyans Jain", 15000, "Bachelors", 4.75)
lateral = Lateral("E", "Naman Jain", 35000, "Bachelors", "AGDEV")

print(Grad.calculate_gross_salary())
print(lateral.calculate_gross_salary())
