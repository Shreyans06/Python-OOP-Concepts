class Applicant:
    __application_dict = {'A': 0, 'B': 4, 'C': 0}
    __applicant_id_count = 1000

    def __init__(self, applicant_name):
        self.__applicant_name = applicant_name
        self.__applicant_id = 0
        self.__job_band = None

    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict

    def get_applicant_id(self):
        return self.__applicant_id

    def get_applicant_name(self):
        return self.__applicant_name

    def get_job_band(self):
        return self.__job_band

    def generate_applicant_id(self):
        self.__applicant_id = Applicant.__applicant_id_count + 1
        Applicant.__applicant_id_count += 1

    def apply_for_job(self, job_band):
        for key, val in Applicant.__application_dict.items():
            if key == job_band:
                if val < 5:
                    Applicant.__application_dict[job_band] += 1
                    self.generate_applicant_id()
                    self.__job_band = job_band
                else:
                    return -1


a = Applicant("Jack")
if a.apply_for_job("B") != -1:
    print(a.get_applicant_id(), a.get_applicant_name(), a.get_job_band())
else:
    print("Can't apply for the job")
