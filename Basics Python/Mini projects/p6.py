# sheet:02=task_2

# method=1

m=int(input("enter some number="))
n=int(input("enter some number="))
if m%n==0:
    print("true")
else:
    print("False")
 
#  method=2
def multi(n,m):
    for i in range(10):
        if n==m*i:
            print(i,"true")
            return()
        else:
            print(i,"false")

n=int(input("enter some number n="))
m=int(input("enter some number m="))
multi(n,m)

 