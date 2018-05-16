

"""
class Class:
    def __init__(self, number_of_people):

        self.location = 'Nuke town'
        self.gross_people = 10
        self.number_of_people = number_of_people

        Attendance = 100*(self.number_of_people /
                            self.gross_people)

        Attendance = round(Attendance, 0)

        print('% Of Attendance = ', Attendance)
        print('At Location    = ', self.location)

    def explode(self):
        self.number_of_people = 0
        print(self.location, 'exploded')
        print(self.number_of_people,'survivors remaining')

our_class = Class(8)
our_class.explode()
"""



try:
    import yoface

except TypeError:
    print('TADA')
