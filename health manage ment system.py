# HEALTH MANAGEMENT SYSTEM
# 3 clients--> Harry,Rohan and Hammad
# Total 6 files,i.e[2 files for food and exercise for each person---> ]


import datetime
def gettime():
    return datetime.datetime.now()
def harry():
    print("___________________harry__________________")
    print("1 for log and 2 for retrieve")
    n2=int(input("="))
    if n2==1:
        print("___________________log__________________")
        print("enter 1 for food and 2 for exercise")
        n3=int(input("="))
        if n3==1:
            print("___________________food__________________")
            with open("harry_food.txt","a") as data:
                value=input("enter here:")
                data.write(str([gettime()])+" "+value+"\n")
                print("successfull written")
        elif n3==2:
            print("___________________exercise__________________")
            with open("harry_exercise.txt","a") as data:
                value=input("enter here:")
                data.write(str([gettime()])+" "+value+"\n")
                print("successfully written")
        else:
            print("please select the vailed input")
    elif n2==2:
        print("___________________retrieve__________________")
        print("enter 1 for food and 2 for exercise")
        n4=int(input("="))
        if n4==1:
            print("___________________food__________________")
            with open("harry_food.txt") as data:
                print(data.read())
        elif n4==2:
            print("___________________exercise__________________")
            f=open("harry_exercise.txt")
            print(f.read())
        else:
            print("please select the vailed input")
    else:
        print("please select the vailed input")


def rohan():
    print("___________________rohan__________________")
    print("enter 1 for food and 2 for exercise")
    n1=int(input("="))
    if n1==1:
        print("___________________food__________________")
        print("1 for log  2 for retrieve")
        n2=int(input("="))
        if n2==1:
            print("___________________log__________________")
            with open("rohan_food.txt","a") as data:
                value=input("enter here:")
                data.write(str([gettime()])+" "+value+"\n")
                print("successfull written")
        elif n2==2:
            print("___________________retrieve__________________")
            with open("rohan_food.txt")as data:
                print(data.read(),end="")
        else:
            print("please enter teh vailed input")
    elif n1==2:
        print("___________________exercise__________________")
        print("print 1 for log and 2 for retrieve")
        n3=int(input("="))
        if n3==1:
            print("___________________log__________________")
            with open("rohan_exercise.txt","a") as data:
                value=input("enter here:")
                data.write(str([gettime()])+" "+value+"\n")
                print("successfully written")
        elif n3==2:
            print("___________________retrieve__________________")
            with open("rohan_exercise.txt")as data:
              print(data.read(),end="")
        else:
            print("please select the vailed input")
    else:
        print("please select the vailed input")
def hammad():
    print("___________________hammad__________________")
    print("enter 1 for food and 2 for exercise")
    n1 = int(input("="))
    if n1 == 1:
        print("___________________food__________________")
        print("1 for log  2 for retrieve")
        n2 = int(input("="))
        if n2 == 1:
            print("___________________log__________________")
            with open("hammad_food.txt", "a") as data:
                value = input("enter here:")
                data.write(str([gettime()]) + " " + value + "\n")
                print("successfull written")
        elif n2 == 2:
            print("___________________retrieve__________________")
            with open("hammad_food.txt") as data:
                print(data.read(), end="")
        else:
            print("please enter teh vailed input")
    elif n1 == 2:
        print("___________________exerciese__________________")
        print("print 1 for log and 2 for retrieve")
        n3 = int(input("="))
        if n3 == 1:
            print("___________________log__________________")
            with open("hammad_food.txt", "a") as data:
                value = input("enter here:")
                data.write(str([gettime()]) + " " + value + "\n")
                print("successfully written")
        elif n3 == 2:
            print("___________________retrieve__________________")
            with open("hammad_exercise.txt") as data:
                print(data.read(), end="")
        else:
            print("please select the vailed input")
    else:
        print("please select the vailed input")


print ("helth management system")
while True:
    print("print 1 for run and 2 for exit")
    no=int(input(":"))
    if no==1:
        print("enter  1 for HARRY , 2 for ROHAN , 3 for HAMMAD")
        n1 = int(input("="))
        if n1 == 1:
            harry()
        elif n1 == 2:
            rohan()
        elif n1 == 3:
            hammad()
        else:
            print("ERROR")

    else:
        print("********\n  exit  \n********")
        break