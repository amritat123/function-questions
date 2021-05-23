def all_students(nav_kharcha):
    i=0
    while i<=nav_kharcha:
        total_batat=nav_kharcha*student_list
        if total_batat<=50000:
            print("bajat andar h")
        else:
            print("bajat andar nhi h ")
        i+=1
        break
nav_kharcha=int(input("please enter the student kharcha="))
student_list=int(input("enter the student list"))
all_students(nav_kharcha)

        