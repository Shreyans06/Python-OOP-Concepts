class Classroom:
    classroom_list = ['G015', 'G066', 'L123', 'L135', 'L143', 'L13']

    @staticmethod
    def search_classroom(class_room):
        if class_room.lower() in [i.lower() for i in Classroom.classroom_list]:
            return 'Found'
        else:
            return -1


c1 = Classroom()
print(c1.search_classroom("g015"))
