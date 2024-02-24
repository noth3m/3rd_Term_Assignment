import random
class student:
    def input_info(self):
        Name = input('Name: ')
        Class = input('Class: ')
        Roll_no = input('Roll No.: ')
        Theory_marks = input('Theory marks: ')
        Viva_marks = input('Practical marks: ')
        Grade = [Theory_marks] + [Viva_marks]
        return  Grade
    Grade = input_info()
    Theory = Grade[0]
    Viva = Grade[1]
    def check_pass_or_fail(self):
        if 