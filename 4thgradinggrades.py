name = input("Your name:")
idnumber = int(input("Your ID numer:"))
coursesection = input("Your course and section:")
grading1st = eval(input("Your 1st grading grades:"))
grading2nd = eval(input("Your 2nd grading grades:"))
grading3rd = eval(input("Your 3rd grading grades:"))
grading4th = eval(input("Your 4th grading grades:"))
finalgrade = (grading1st + grading2nd + grading3rd + grading4th) / 4

print("name:", name)
print("idnumber:", idnumber)
print("coursesection:", coursesection)
print("grading1st:", grading1st)
print("grading2nd:", grading2nd)
print("grading3rd:", grading3rd)
print("grading4th:", grading4th)
print("Your final grade is", finalgrade)