import functools
import re
f_ref=open("D:/AnuPythonProjects/PythonPracticeProjects/testQuestions/test_second/employee_test","r")
empl_lst=[]
for i in f_ref:
    line=i.rstrip("\n").split(",")
    empl_lst.append(line)
# print(empl_lst)
# Question1: Creation and insertion of employee objects
class Employee:
    def __init__(self,eid,ename,edesignation,mailId,salary):
        self.eid=eid
        self.ename=ename
        self.edesignation=edesignation
        self.mailId=mailId
        self.salary=salary


lst=[]
for i in empl_lst:
 empObj=Employee(i[0],i[1],i[2],i[3],i[4])
 lst.append(empObj)

# Question 2::Maximum Salary
salaryList=list(map(lambda obj1:obj1.salary,lst))

data=functools.reduce(lambda  obj1,obj2:obj1 if obj1>obj2 else obj2,salaryList)
print("Maximum Salary:::",data)


# Question 3::: valid Emails
emailList=list(map(lambda o:o.mailId,lst))
# print("Original emailList::",emailList)

email_reg_exp='[a-zA-Z]\w*@gmail[.]com'
checkValidEmail=lambda emailId:re.fullmatch(email_reg_exp,emailId)
validEmailList=list(filter(checkValidEmail,emailList))
print("Valid Email IDs:",validEmailList)

f_write=open("validEmailList","w")
for i in validEmailList:
    f_write.write(i+"\n")









