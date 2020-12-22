class InvalidMechanicIdException(Exception):
    pass


class InvalidMechanicSpecializationException(Exception):
    pass


class Mechanic:
    def __init__(self, mechanic_id, specialization, vehicle_count):
        self.__mechanic_id = mechanic_id
        self.__specialization = specialization
        self.__vehicle_count = vehicle_count

    def get_mechanic_id(self):
        return self.__mechanic_id

    def get_specialization(self):
        return self.__specialization

    def get_vehicle_count(self):
        return self.__vehicle_count

    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count += vehicle_count


class VehicleService:
    def __init__(self, mechanic_list):
        self.__mechanic_list = mechanic_list

    def assign_vehicle_for_service(self, mechanic_id, vehicle_type):
        status = 0
        m_id = "null"
        for mech_id in self.__mechanic_list:
            if mechanic_id == mech_id.get_mechanic_id():
                status = 1
                m_id = mech_id
                break

        if status == 0:
            raise InvalidMechanicIdException("InvalidMechanicIdException")

        status = 0

        if vehicle_type == m_id.get_specialization():
            m_id.set_vehicle_count(1)
            status = 1

        if status == 0:
            raise InvalidMechanicSpecializationException("InvalidMechanicSpecializationException")


m1 = Mechanic(101, "TW", 1)
m2 = Mechanic(102, "FW", 0)
m3 = Mechanic(103, "TW", 4)
m4 = Mechanic(104, "FW", 2)
m5 = Mechanic(105, "FW", 1)
mechanic_list = [m1, m2, m3, m4, m5]
v1 = VehicleService(mechanic_list)

try:
    v1.assign_vehicle_for_service(105, "FW")
except InvalidMechanicIdException as e:
    print(str(e))
except InvalidMechanicSpecializationException as e:
    print(str(e))
