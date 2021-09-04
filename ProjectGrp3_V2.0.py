import pickle
import os
import time
import datetime


def set_report():  # Used to return a dictionary with student report data
    adno = int(input('Enter Admission no: '))
    name = input('Enter name: ')
    yearsec = input("Enter the class(Year-Section):")
    english = float(input('Enter Marks in English: '))
    maths = float(input('Enter Marks in Maths: '))
    physics = float(input('Enter Marks in Physics: '))
    chemistry = float(input('Enter Marks in Chemistry: '))
    cs = float(input('Enter Marks in CS: '))
    avg = float((english + maths + physics + chemistry + cs)/5)
    print("--------------------------------------------------------------------------------------------------")

    # creates a dictionary for student details and marks and returns it
    student = {}
    student['Admission no'] = adno
    student['name'] = name
    student['class'] = yearsec
    student['english'] = english
    student['maths'] = maths
    student['physics'] = physics
    student['chemistry'] = chemistry
    student['cs'] = cs
    student['avg'] = avg
    return student


def display_reportdata(student):  # Used to display student report data
    print('\nSTUDENT DETAILS:\n')
    print('Admission Number:', student['Admission no'])
    print('Name:', student['name'])
    print('Class:', student['class'])
    print('English:', student['english'])
    print('Maths:', student['maths'])
    print('Physics:', student['physics'])
    print('Chemistry:', student['chemistry'])
    print('CS:', student['cs'])
    print('Average:', student['avg'])


def display_reportdata_tabular(student):  # same as above but in tabular form
    print(student['Admission no'], student['name'], student['class'], student['english'],
          student['maths'], student['physics'], student['chemistry'],
          student['cs'], sep='\t')

# Used to display teacher profile data


def display_profiledata_teacher(teacher):
    print('\nStaff ID:', teacher['Staff ID'])
    print('Password:', teacher['Password'])


def display_profiledata(profile):  # Used as a print format for other def's
    print('\nAdmission Number:', profile['Admission no'])
    print('Password:', profile['Password'])
    print('Roll Number:', profile['rollno'])
    print('Class:', profile['class'])
    print('Name:', profile['name'])
    print('DOB:', profile['Date of Birth'])
    print('Email:', profile['Email'])
    print('Mobile No:', profile['Mobile Number'])
    print('Fathers Name:', profile['Fathers Name'])
    print('Mothers Name:', profile['Mothers Name'])
    print('Fees:', profile['Fees'], '\n')


# Used to display a students profile data to them
def s_display_profiledata(profile):
    print('\nName:', profile['name'])
    print('Date of Birth:', profile['Date of Birth'])
    print('Email:', profile['Email'])
    print('Mobile No:', profile['Mobile Number'])
    print('Fathers Name:', profile['Fathers Name'])
    print('Mothers Name:', profile['Mothers Name'])


def set_profile_teacher():  # Used to return a dictionary with details for a teacher's profile
    finished = False
    while finished is False:
        try:
            staffid = int(input("\nStaff ID: "))
            passwrd = input("Password: ")
            finished = True
        except ValueError:
            print("\n Please use only numericals for the staff id.")
    print("--------------------------------------------------------------------------------------------------")
    teacher = {}
    teacher['Staff ID'] = staffid
    teacher['Password'] = passwrd
    return teacher


def set_profile():  # Used to return a dictionary of a student profile, used by admins
    adno = int(input("Admission no:"))
    passwrd = input("Password:")
    rollno = int(input("Enter the roll number:"))
    yearsec = input("Enter the class and section('year'-'section'):")
    name = input("Enter your name:")
    fees = int(input("Enter the fee amount:"))
    dob = input("Enter your date of birth(DD/MM/YYYY):")
    mail = input("Enter your email:")
    mno = int(input("Enter your mobile number:"))
    fname = input("Enter your father's full name:")
    mname = input("Enter your mother's full name:")

    print("--------------------------------------------------------------------------------------------------")

    # creates a dictionary for student profile and returns it
    profile = {}
    profile['Admission no'] = adno
    profile['Password'] = passwrd
    profile['rollno'] = rollno
    profile['class'] = yearsec
    profile['name'] = name
    profile['Date of Birth'] = dob
    profile['Email'] = mail
    profile['Mobile Number'] = mno
    profile['Fathers Name'] = fname
    profile['Mothers Name'] = mname
    profile['Fees'] = fees
    return profile


def add_report():  # To create a report, used by admins and teachers
    ofile = open('stdreport.dat', 'ab')
    while True:
        pickle.dump(set_report(), ofile)
        ans = input('Do you want to enter more reports (y/n)?: ')
        if ans in 'nN':
            break
    ofile.close


def modify_report():  # To modifiy a created report, used by admins or teachers
    print('\nMODIFY RECORD')
    try:
        infile = open('stdreport.dat', 'rb')
    except FileNotFoundError:
        print('No record found to modify..')
        return

    found = False
    outfile = open("temp.dat", "wb")
    adno = int(input('Enter roll number: '))
    while True:
        try:
            # reading the oject from file
            student = pickle.load(infile)

            # display record if found and set flag
            if student['Admission no'] == adno:

                print('Name:', student['name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    student['name'] = input("Enter the name ")

                print('English marks:', student['english'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    student['english'] = float(input("Enter new marks: "))

                print('Maths marks:', student['maths'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    student['maths'] = float(input("Enter new marks: "))

                print('Physics marks:', student['physics'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    student['physics'] = float(input("Enter new marks: "))

                print('Chemistry marks:', student['chemistry'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    student['chemistry'] = float(input("Enter new marks: "))

                print('CS marks:', student['cs'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    student['cs'] = float(input("Enter new marks: "))

                pickle.dump(student, outfile)
                found = True
                break
            else:
                pickle.dump(student, outfile)
        except EOFError:
            break
    if found == False:
        print('Report not Found')
    else:
        print('Report updated')
        display_reportdata(student)

    infile.close()
    outfile.close()
    os.remove("stdreport.dat")
    os.rename("temp.dat", "stdreport.dat")


def add_profile():  # Used by admins to create profiles for students
    ofile = open('stdprofile.dat', 'ab')
    while True:
        pickle.dump(set_profile(), ofile)
        ans = input('Do you want to enter more profiles (y/n)?: ')
        if ans in 'nN':
            break
    ofile.close()


def add_teacher_profile():  # Used by admins to create profiles for teachers
    ofile = open('teacherprofile.dat', 'ab')
    while True:
        pickle.dump(set_profile_teacher(), ofile)
        ans = input('Do you want to enter more profiles (y/n)?: ')
        if ans in 'nN':
            break
    ofile.close()


def modify_teacher_profile():  # Used by admins to modify teacher profile data
    print('\nMODIFY Teacher Profile')
    try:
        infile = open('teacherprofile.dat', 'rb')
    except FileNotFoundError:
        print('teacherprofile.dat not found, creating...')
        f = open("teacherprofile.dat", "wb")
        f.close()
        time.sleep(1)
        print("Done, please create profiles for teachers.")
        add_teacher_profile()
        return

    found = False
    infile = open('teacherprofile.dat', 'rb')
    outfile = open("temp.dat", "wb")
    staffid = int(input("Staff ID:"))
    finished = False

    while True:
        try:
            # reading the object from file
            teacher = pickle.load(infile)

            # display record if found and set flag
            if teacher["Staff ID"] == staffid:

                print('Staff ID:', teacher['Staff ID'])
                ans = input('Do you want to edit(y/n)? ')

                while finished is False:
                    try:
                        if ans in 'yY':
                            teacher['Staff ID'] = int(
                                input("Enter new Staff ID: "))
                            finished = True
                    except ValueError:
                        print("\nPlease use only numericals for the staff id.")

                print('Password:', teacher['Password'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    teacher['Password'] = input("Enter the new Password: ")

                pickle.dump(teacher, outfile)
                found = True
                break
            else:
                pickle.dump(teacher, outfile)
        except EOFError:
            break
    if found == False:
        print('Teacher Profile not Found')
    else:
        print('Teacher Profile updated')
        display_profiledata_teacher(teacher)

    infile.close()
    outfile.close()
    os.remove("teacherprofile.dat")
    os.rename("temp.dat", "teacherprofile.dat")


def modify_profile():  # To modifiy created profiles, used by admins
    print('\nMODIFY Profile')
    try:
        infile = open('stdprofile.dat', 'rb')
    except FileNotFoundError:
        print('No record found to modify..')
        return

    found = False
    outfile = open("temp.dat", "wb")
    adno = int(input("\nEnter the admission no:"))
    while True:
        try:
            # reading the object from file
            profile = pickle.load(infile)

            # display record if found and set flag
            if profile['Admission no'] == adno:

                print('Admission no:', profile['Admission no'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Admission no'] = int(
                        input("Enter new admission no: "))

                print('Password:', profile['Password'])
                ans = input('Want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Password'] = input("Enter the new Password: ")

                print('Roll No:', profile['rollno'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['rollno'] = input("Enter the new roll no: ")

                print('Class:', profile['class'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['class'] = input("Enter the new class: ")

                print('Name:', profile['name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['name'] = input("Enter the name: ")

                print('Date of Birth:', profile['Date of Birth'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Date of Birth'] = input(
                        "Enter new DOB(DD/MM/YYYY): ")

                print('Mobile Number:', profile['Mobile Number'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Mobile Number'] = int(
                        input("Enter new mobile number: "))

                print('Email:', profile['Email'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Email'] = input("Enter new email: ")

                print('Fathers Name:', profile['Fathers Name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Fathers Name'] = input("Fathers name: ")

                print('Mothers name:', profile['Mothers Name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Mothers Name'] = input("Mothers name: ")

                print('Fees:', profile['Fees'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Fees'] = input("Fees: ")

                pickle.dump(profile, outfile)
                found = True
                break
            else:
                pickle.dump(profile, outfile)
        except EOFError:
            break
    if found == False:
        print('Profile not Found')
    else:
        print('Profile updated')
        display_profiledata(profile)

    infile.close()
    outfile.close()
    os.remove("stdprofile.dat")
    os.rename("temp.dat", "stdprofile.dat")


def s_modify_profile():  # Lets a student modifiy some parts of their own profile
    print('\nMODIFY Profile')
    try:
        infile = open('stdprofile.dat', 'rb')
    except FileNotFoundError:
        print('No record found to modify..')
        return

    found = False
    outfile = open("temp.dat", "wb")
    while True:
        try:
            # reading the object from file
            profile = pickle.load(infile)

            # display record if found and set flag
            if profile['Admission no'] == adno:

                print('Name:', profile['name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['name'] = input("Enter the name: ")

                print('Date of Birth:', profile['Date of Birth'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Date of Birth'] = input(
                        "Enter new DOB(DD/MM/YYYY): ")

                print('Mobile Number:', profile['Mobile Number'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Mobile Number'] = int(
                        input("Enter new mobile number: "))

                print('Email:', profile['Email'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Email'] = input("Enter new email: ")

                print('Fathers Name:', profile['Fathers Name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Fathers Name'] = input("Fathers name: ")

                print('Mothers name:', profile['Mothers Name'])
                ans = input('Do you want to edit(y/n)? ')
                if ans in 'yY':
                    profile['Mothers Name'] = input("Mothers name: ")

                pickle.dump(profile, outfile)
                found = True
                break
            else:
                pickle.dump(profile, outfile)
        except EOFError:
            break
    if found == False:
        print('Profile not Found')
    else:
        print('Profile updated')
        s_display_profiledata(profile)

    infile.close()
    outfile.close()
    os.remove("stdprofile.dat")
    os.rename("temp.dat", "stdprofile.dat")


def admin_login():  # Used for the admin login function
    incorrect = 3
    while incorrect != 0:
        user = input("\nUsername:")
        passwrd = input("Password:")
        if user == 'admin' and passwrd == 'admin':
            return True
        else:
            incorrect -= 1
            print("Wrong credentials ")
            if incorrect == 0:
                print("Exiting as incorrect inputs limit exceeded")
            else:
                print("Number of trys left before exiting:", incorrect)


def teacher_login():  # Used for the teacher login function
    try:
        ifile = open('teacherprofile.dat', 'rb')
    except FileNotFoundError:
        print("File is not found.... creating teacherprofile.dat")
        time.sleep(1)
        f = open("teacherprofile.dat", "wb")
        f.close()
        print('Done, Please add profiles to the file.')
        return

    ifile = open("teacherprofile.dat", "rb")
    incorrect = 3
    found = False

    try:
        staffid = int(input("Enter Staff ID:"))
        while True:
            profile = pickle.load(ifile)
            if staffid == profile['Staff ID']:
                found = True
                while incorrect != 0:
                    password = input("Enter Password:")
                    if password == profile['Password']:
                        return True
                    else:
                        incorrect -= 1
                        print("Wrong password")
                        if incorrect == 0:
                            print("Exiting as incorrect password limit exceeded")
                        else:
                            print("Number of trys left before exiting:", incorrect)
            else:
                pass
    except EOFError:
        if found == False:
            print('Incorrect admission number')
            teacher_login()
    ifile.close()


def student_login():  # Used for the student login function (also has global adno variable)
    global adno
    try:
        ifile = open("stdprofile.dat", "rb")
    except FileNotFoundError:
        print("File is not found.... creating stdprofile.dat")
        time.sleep(1)
        f = open("stdprofile.dat", "wb")
        f.close()
        print('Done. Please add profiles to the file ')
        return

    ifile = open("stdprofile.dat", "rb")
    incorrect = 3
    found = False

    try:
        adno = int(input("Enter admission number:"))
        while True:
            profile = pickle.load(ifile)
            if adno == profile['Admission no']:
                found = True
                while incorrect != 0:
                    password = input("Enter Password:")
                    if password == profile['Password']:
                        return True
                    else:
                        incorrect -= 1
                        print("Wrong password")
                        if incorrect == 0:
                            print("Exiting as incorrect password limit exceeded")
                        else:
                            print("Number of trys left before exiting:", incorrect)
            else:
                pass
    except EOFError:
        if found == False:
            print('Incorrect admission number')
            student_login()
    ifile.close()


def school_updates_write():  # To write school updates and save them, by admins only
    try:
        ifile = open("schoolupdates.dat", "rb")
    except FileNotFoundError:
        print("File does not exist.....creating schoolupdates.dat")
        time.sleep(1)
        f = open("schoolupdates.dat", "wb")
        f.close()
        print('Done')

    ifile = open("schoolupdates.dat", "rb")
    ofile = open("temp.dat", "wb")

    print("Please write the school update you want students to see:-")
    update = str(datetime.date.today()) + "\n" + input() + '\n'
    ch1 = input("Do you want to submit this?(y/n):")

    if ch1 in ['Yes', 'yes', 'y', 'Y']:
        pickle.dump(update, ofile)
    else:
        print("Exiting...")
        ofile.close()
        ifile.close()
        os.remove('temp.dat')

    if ch1 in ['Yes', 'yes', 'y', 'Y']:
        try:
            while True:
                oldstuff = pickle.load(ifile)
                pickle.dump(oldstuff, ofile)
        except EOFError:
            print("Done")
            ifile.close()
            ofile.close()
            os.remove("schoolupdates.dat")
            os.rename("temp.dat", "schoolupdates.dat")

        ch2 = input("Do you want to write another school update?(y/n):")
        if ch2 in ['Yes', 'yes', 'y', 'Y']:
            school_updates_write()
        else:
            pass
    else:
        pass


def school_updates_view():  # Used to view the school updates, can be used by all
    try:
        ifile = open("schoolupdates.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File does not exist. Please report this problem to the admin")
        time.sleep(3)

    try:
        while found == True:
            updates = pickle.load(ifile)
            print(updates)
    except EOFError:
        print('Finished')


def admin_classreport():  # Used to show the classreport to a admin or teacher,
    found = False
    try:
        filein = open('stdreport.dat', 'rb')
        found = True
    except FileNotFoundError:
        print('File not found, please contact the admin.')
        found = False
    if found == True:
        ch1 = input("Enter the class(Year-Section):")
        print("Showing all students of class", ch1)
        try:
            totalclassmarks = 0
            students = 0
            while True:
                student = pickle.load(filein)
                if student['class'] == ch1:
                    display_reportdata(student)
                    students += 1
                    totalclassmarks += student['avg']
                else:
                    pass
        except EOFError:
            filein.close
            print("\nThe class average of", ch1,
                  "is", (totalclassmarks/students))
            print('\nDone')


def student_report_view():  # Used by students to check their own report.
    found = False
    try:
        filein = open("stdreport.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File is not found, please contact the admin.")
        found = False
    if found == True:
        try:
            report = False
            while True:
                student = pickle.load(filein)
                if student['Admission no'] == adno:
                    display_reportdata(student)
                    report = True
                else:
                    pass
        except EOFError:
            filein.close()
            if report == False:
                print("Report for admission number", adno, "not found.")
            else:
                print('\nDone')


def student_profile_view():  # Used by students to check their own profile.
    found = False
    try:
        filein = open("stdprofile.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File is not found, please contact the admin.")
        found = False
    if found == True:
        try:
            report = False
            while True:
                student = pickle.load(filein)
                if student['Admission no'] == adno:
                    s_display_profiledata(student)
                    report = True
                else:
                    pass
        except EOFError:
            filein.close()
            if report == False:
                print("Profile for admission number", adno, "not found.")
            else:
                print('\nDone')


def fee_pay():  # Used to pay fees
    try:
        fin = open("stdprofile.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File is not found contact admin")
        found = False

    if found == True:
        try:
            while True:
                profile = pickle.load(fin)
                if profile["Admission no"] == adno:
                    fees = profile["Fees"]
                    print("Fees to be payed is", fees)
                    quit1 = False
                    while quit1 == False:
                        payment = int(
                            input("Enter the amount that you want to pay:"))
                        if fees < payment:
                            print(
                                "Please enter an amount equal to or lower than the fees.")
                        else:
                            fees = fees - payment
                            profile["Fees"] = fees
                            print("Transaction completed. Current due fees:", fees)
                            quit1 = True

        except EOFError:
            pass

    fin.close()
    ifile = open("stdprofile.dat", "rb")
    ofile = open("temp.dat", "wb")

    while True:
        try:
            profile = pickle.load(ifile)
            if profile['Admission no'] == adno:
                profile['Fees'] = fees
                pickle.dump(profile, ofile)
            else:
                pickle.dump(profile, ofile)
        except EOFError:
            break

    ifile.close()
    ofile.close()
    os.remove("stdprofile.dat")
    os.rename("temp.dat", "stdprofile.dat")


def view_all_student_profiles():  # Used by admins to view all profiles in stdprofile.dat
    try:
        ifile = open("stdprofile.dat", "rb")
        found = True
    except FileNotFoundError:
        print('No file found. Contact the admin')
        found = False
    while found is True:
        try:
            profile = pickle.load(ifile)
            display_profiledata(profile)
        except EOFError:
            break

    ifile.close()


def admin_student_report_view():  # Used by admins to check student reports.
    found = False
    try:
        filein = open("stdreport.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File is not found, please create and add reports.")
        found = False
    if found == True:
        try:
            report = False
            adno = int(input("Please enter the Student Admission Number:"))
            while True:
                student = pickle.load(filein)
                if student['Admission no'] == adno:
                    display_reportdata(student)
                    report = True
                else:
                    pass
        except EOFError:
            filein.close()
            if report == False:
                print("Report for admission number", adno, "not found.")
                admin_student_report_view()
            else:
                ch1 = input(
                    "\nDo you wish to view another student's file?(y/n):")
                if ch1 in 'Yy':
                    admin_student_report_view()
                else:
                    print('\nDone')


def admin_student_profile_view():  # Used by admins to check student profiles
    found = False
    try:
        filein = open("stdprofile.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File is not found, please create and add profiles.")
        found = False
    if found == True:
        try:
            report = False
            adno = int(input("Please enter the Student Admission No:"))
            while True:
                student = pickle.load(filein)
                if student['Admission no'] == adno:
                    display_profiledata(student)
                    report = True
                else:
                    pass
        except EOFError:
            filein.close()
            if report == False:
                print("Profile for Staff ID", adno, "not found.")
                admin_student_profile_view()
            else:
                ch1 = input(
                    "\nDo you wish to view another student's profile?(y/n):")
                if ch1 in 'Yy':
                    admin_student_profile_view()
                else:
                    print('\nDone')


def admin_teacher_profile_view():  # Used by admins to check teacher profiles
    found = False
    try:
        filein = open("teacherprofile.dat", "rb")
        found = True
    except FileNotFoundError:
        print("File is not found, please create and add profiles.")
        found = False
    if found == True:
        try:
            report = False
            staffid = int(input("Please enter the Teacher Staff ID:"))
            while True:
                teacher = pickle.load(filein)
                if teacher['Staff ID'] == staffid:
                    display_profiledata_teacher(teacher)
                    report = True
                else:
                    pass
        except EOFError:
            filein.close()
            if report == False:
                print("Profile for Staff ID", staffid, "not found.")
                admin_teacher_profile_view()
            else:
                ch1 = input(
                    "\nDo you wish to view another teacher's profile?(y/n):")
                if ch1 in 'Yy':
                    admin_teacher_profile_view()
                else:
                    print('\nDone')


def loginmenu():  # Self explanatory
    print("\nLogin Menu:\n\n1.Admin Login\n2.Teacher Login\n3.Student Login\n4.Help\n5.Exit\n")


def admin_menu_main():  # Self explanatory
    print("\nAdmin Menu:\n\n1.Student Commands\n2.Teacher Commands\n3.Display Class Report\n4.Add School Updates\n5.View School Updates\n6.Logout\n")


def admin_menu_2():  # Self explanatory
    print("\nStudent Commands:\n\n1.Add Student report\n2.Add Student Profile\n3.Modify Student Report\n4.Modify Student Profile\n5.Display Student Report\n6.Display Student Profile\n7.Return Back\n")


def admin_menu_3():  # Self explanatory
    print("\nTeacher Commands:\n\n1.Add Teacher Profile\n2.Modify Teacher Profile\n3.Display Teacher Profile\n4.Return Back\n")


def teacher_menu():  # Self explanatory
    print("\nTeacher Menu:\n\n1.Add Student Report\n2.Modify Student Report\n3.Display Student Report\n4.Display Class Report\n5.View School Updates\n6.Logout\n")


def student_menu():  # Self explanatory
    print("\nStudent Menu:\n\n1.My Profile\n2.Modify My Profile\n3.View My Report\n4.View School Updates\n5.Pay Fees\n6.Logout\n")


def intro():  # Self explanatory
    print("=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
    print(
        "STUDENT INFORMATION\nSYSTEM PROJECT\n")
    print("Group No :", "3\n")
    print("Done By :",
          "Akhil Sajan Mathew, Jeswin Thomas, Jeswin Jo Varghese, Jibin Thomas\n")
    print("SCHOOL :", "St.Anthony Public School")
    print("=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
    time.sleep(1)


def admin_return():  # Choice for returning to admin menu
    ch = input(
        "\nDo you want to return back to the admin menu? Else you will exit the application.(y/n): ")
    if ch in 'Yy':
        pass
    elif ch in 'Nn':
        print('\nExiting...')
        time.sleep(1)
        exit()
    else:
        print("\nPlease enter y or n.")
        admin_return()


def student_return():  # Choice for returning to student menu
    ch = input(
        "\nDo you want to return back to the student menu?Else you will exit the application.(y/n): ")
    if ch in 'Yy':
        pass
    elif ch in 'Nn':
        print('\nExiting...')
        time.sleep(1)
        exit()
    else:
        print("\nPlease enter y or n.")
        student_return()


def teacher_return():  # Choice for returning to teacher menu
    ch = input(
        "\nDo you want to return back to the teacher menu? Else you will exit the application.(y/n): ")
    if ch in 'Yy':
        pass
    elif ch in 'Nn':
        print('\nExiting...')
        time.sleep(1)
        exit()
    else:
        print("\nPlease enter y or n.")
        teacher_return()


def filecreator():  # Creates all the necessary files at launch.
    try:
        file1r = open("stdreport.dat", "r")
        file1r.close()
    except FileNotFoundError:
        print("Please wait until the required files are created...\n")
        time.sleep(1)
        f1 = open("stdreport.dat", "w")
        f1.close()
        print("stdreport.dat successfully created...\n")

    try:
        file2r = open("stdprofile.dat", "r")
        file2r.close()
    except FileNotFoundError:
        time.sleep(1)
        f2 = open("stdprofile.dat", "w")
        f2.close()
        print("stdprofile.dat successfully created...\n")

    try:
        file3r = open("teacherprofile.dat", "r")
        file3r.close()
    except FileNotFoundError:
        time.sleep(1)
        f3 = open("teacherprofile.dat", "w")
        f3.close()
        print("teacherprofile.dat successfully created...\n")

    try:
        file4r = open("schoolupdates.dat", "r")
        file4r.close()
    except FileNotFoundError:
        time.sleep(1)
        f4 = open("schoolupdates.dat", "w")
        f4.close()
        print("schoolupdates.dat successfully created...\n\nAll required files are succesfully created/detected.\n")
    time.sleep(1)


def help():
    print("\nINSTRUCTIONS ON HOW TO USE THE APPLICATION\n\n1.For the first time launching the application, please login into the admin account\n  using user = 'admin' and pass = 'admin'\n2.Please create reports and profiles for the students(Be sure to follow any type of format if given)\n3.Please create profiles for the teachers as well.\n4.Be sure to enter integer/numbers only for certain fields (Admission No.,Mobile Number,Grades/Marks,Staff ID etc.)\n")


def main():  # The def which makes the whole application work
    intro()
    filecreator()
    quit1 = False
    while quit1 is False:
        loginmenu()
        logch = input("Please Enter Your Choice:(1,2,3,4,5): ")
        if logch == '1':
            if admin_login() is True:
                quit2 = False
                while quit2 is False:
                    admin_menu_main()
                    adch1 = input("\nPlease Enter Your Choice: ")
                    if adch1 == '1':
                        admin_menu_2()
                        adch2 = input("\nPlease Enter Your Choice: ")
                        if adch2 == '1':
                            add_report()
                            admin_return()
                        elif adch2 == '2':
                            add_profile()
                            admin_return()
                        elif adch2 == '3':
                            modify_report()
                            admin_return()
                        elif adch2 == '4':
                            modify_profile()
                            admin_return()
                        elif adch2 == '5':
                            admin_student_report_view()
                            admin_return()
                        elif adch2 == '6':
                            admin_student_profile_view()
                            admin_return()
                        elif adch2 == '7':
                            pass
                        elif adch2 == '':
                            pass
                        else:
                            print("\nPlease enter one of the given choices only.\n")
                            time.sleep(1)

                    elif adch1 == '2':
                        admin_menu_3()
                        adch2 = input("\nPlease Enter Your Choice: ")
                        if adch2 == '1':
                            add_teacher_profile()
                            admin_return()
                        elif adch2 == '2':
                            modify_teacher_profile()
                            admin_return()
                        elif adch2 == '3':
                            admin_teacher_profile_view()
                            admin_return()
                        elif adch2 == '4':
                            pass
                        elif adch2 == '':
                            pass
                        else:
                            print("\nPlease enter one of the given choices only.\n")
                            time.sleep(1)
                    elif adch1 == '3':
                        admin_classreport()
                        admin_return()
                    elif adch1 == '4':
                        school_updates_write()
                        admin_return()
                    elif adch1 == '5':
                        school_updates_view()
                        admin_return()
                    elif adch1 == '6':
                        quit2 = True
                    else:
                        print("\nPlease enter one of the given choices only.\n")
                        time.sleep(1)
        elif logch == '2':
            if teacher_login() is True:
                quit3 = False
                while quit3 is False:
                    teacher_menu()
                    tech1 = input("\nPlease Enter Your Choice: ")
                    if tech1 == '1':
                        add_report()
                        teacher_return()
                    elif tech1 == '2':
                        modify_report()
                        teacher_return()
                    elif tech1 == '3':
                        admin_student_report_view()
                        teacher_return()
                    elif tech1 == '4':
                        admin_classreport()
                        teacher_return()
                    elif tech1 == '5':
                        school_updates_view()
                        teacher_return()
                    elif tech1 == '6':
                        quit3 = True
                    else:
                        print("\nPlease enter one of the given choices only.\n")
                        time.sleep(1)
        elif logch == '3':
            if student_login() is True:
                quit4 = False
                while quit4 is False:
                    student_menu()
                    stch1 = input("\nPlease Enter Your Choice: ")
                    if stch1 == '1':
                        student_profile_view()
                        student_return()
                    elif stch1 == '2':
                        s_modify_profile()
                        student_return()
                    elif stch1 == '3':
                        student_report_view()
                        student_return()
                    elif stch1 == '4':
                        school_updates_view()
                        student_return()
                    elif stch1 == '5':
                        fee_pay()
                        student_return()
                    elif stch1 == '6':
                        quit4 = True
                    else:
                        print("\nPlease enter one of the given choices only.\n")
                        time.sleep(1)
        elif logch == '4':
            help()
            time.sleep(1)
            ch = input(
                "\nDo you want to return to the login menu? Else you will exit the application(y/n): ")
            if ch in 'Yy':
                pass
            elif ch in 'Nn':
                print("\nExiting Application....")
                time.sleep(1)
                quit1 = True
            else:
                print("Wrong input... Self Destruction Initiated...")
                time.sleep(1)
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                print("Boom.")
                time.sleep(1)
                quit()
        elif logch == '5':
            print("\nExiting Application....")
            time.sleep(1)
            quit1 = True
        else:
            print("\nPlease enter one of the given choices only.\n")
            time.sleep(1)


main()
