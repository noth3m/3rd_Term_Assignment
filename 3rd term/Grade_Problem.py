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
    def remark():
        good = ['Good Job , Keep it up','Wow! , You killed it!!','']
    def check_pass_or_fail(self):
        if self.Theory > 35:
            check = 'pass'
            if self.Viva == 0:
                check = 'absent'
        else:
            check = 'fail'
        return check
    state = check_pass_or_fail()
    def average(self):
        average = self.Theory + self.Viva
        average = average/2
        return average
    average = int(average())
    abs_marks = average()
# still being worked on 
            