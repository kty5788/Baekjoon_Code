class Student():
    sumall = 0
    def __init__(self,score):
        if score < 40:
            self.score = 40
        else:
            self.score = score
        Student.sumall += self.score

for i in range(5):
    a = int(input())
    Student(a)
    
    

print(int(Student.sumall/5))