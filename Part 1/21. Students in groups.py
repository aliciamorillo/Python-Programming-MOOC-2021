#Please write a program which asks for the number of students on a course and the desired group size. 

numberStudents = int(input("How many students on the course?"))
groupSize = int(input("Desired group size?"))

division = numberStudents // groupSize
resto = numberStudents % groupSize

if resto == 0 :
    print("Number of groups formed:", division)
else:
    print("Number of groups formed:", division+1)