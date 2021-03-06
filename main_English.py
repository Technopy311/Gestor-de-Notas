import os
global approved
global fail

DB = "./db/"
SUBJECTS = "./db/asig/"


def entering():
    names = open("names.txt", "a")
    subject = " "
    note_saving = 0
    averages = " "
    x = 0
    global approved
    global fail

    approved = 0
    fail = 0

    students = input("How many students do you want to enter?: ")

    try:
        students = int(students)
    except ValueError:
        print("The option must be numeric \n.")
        exit()

    while x < students:
        db = open("./db/data.txt", "a")
        name = input("Enter the student's name: ")
        print("Choose the subject")
        print("Calculus(1)")
        print("Programming (2)")
        print("Ethics (3)")
        asig = input(": ")

        try:
            asig = int(asig)
        except ValueError:
            print("The option must be numeric. \n")
            exit()

        print("Now please enter the marks with decimal point, example: 5.6")        
        note1 = input("Enter the first mark:")
        note2 = input("Enter the second mark: ")
        note3 = input("Enter the third mark: ")

        try:
            note1 = float(note1)
        except ValueError:
            print("The mark mus be numeric. \n")
        try:
            note2 = float(note2)
        except ValueError:
            print("The mark mus be numeric. \n")
        try:
            note3 = float(note3)
        except ValueError:
            print("The mark mus be numeric. \n")
            exit()

        if asig == 1:
            subject = "Calculus"
            note_saving = 1
        elif asig == 2:
            subject = "Programming"
            note_saving = 2
        elif asig == 3:
            subject = "Ethics"
            note_saving = 3
        elif asig > 3 or asig < 1:
            print("That subject doesn't exists. \n")
            exit()

        if note_saving == 1:
            path = (SUBJECTS + "calculus.txt")
            averages = open(path, 'a')
        elif note_saving == 2:
            path = (SUBJECTS + "programation.txt")
            averages = open(path, 'a')
        elif note_saving == 3:
            path = (SUBJECTS + "ethics.txt")
            averages = open(path, 'a')
        else:
            print("No idea what happened, selfdestroying in 5..4..3..2..1..0")
            print("KABOOOOOM!")
            exit()

        student = list((name, subject, note1, note2, note3))

        if (student[2]) >= 1.0 and student[2] <= 7.0:
            pass
        else:
            print("The marks aren't into a valid range.\n")
            exit()
        if (student[3]) >= 1.0 and student[3] <= 7.0:
            pass
        else:
            print("The marks aren't into a valid range.\n")
            exit()
        if (student[4]) >= 1.0 and student[4] <= 7.0:
            pass
        else:
            print("The marks aren't into a valid range.\n")
            exit()

        average = ((student[2]) + (student[3]) + (student[4]))/3
        student.append(average)

        average = str(average)
        averages.write(average)
        averages.write("\n")

        average = float(average)

        if average >= 4:
            status = 'approved'
            approved = approved + 1
            text = "\nThe studen doesn't need to re-make the subject.\n"
        else:
            status = "failed"
            fail += fail + 1
            text = "\nThe student must re-make the subject. \n"

        student.append(status)

        print("The student: " + student[0] + " of the subject: " + student[1])
        print("Got an average of: " + str(average) + " so he/she " + status + " the subject.")
        print(text)

        db.write("names:" + str(student[0]) + ". \n subject: " + str(student[1]) + ". \n Notas 1: " +
                 str(student[2]) + ". \n note2: " + str(student[3]) + ". \n note3: " + str(student[4])
                 + ". \n average: " + str(student[5]) + ". \n status of the subject is: " + str(student[6]) + "\n")

        destiny = (DB + (student[0]) + ".txt")
        destiny = str(destiny)
        os.rename(DB + "data.txt", destiny)

        names.write(student[0] + "\n")

        x += 1

        if x == students:
            print("Were " + str(approved) + " students approved & "
                  + str(fail) + " students failed.")
            db.close()
            names.close()
            averages.close()
            menu()
        else:
            pass


def watch():
    def options():
        print("###########################################################################")
        print("What would you like to do?. Choose an option:\n")
        print("##(1) Show the information of an student.")
        print("##(2) List the existent archives in DB.")
        print("###########################################################################")
        user_option = input(":")
        try:
            user_option = int(user_option)
        except ValueError:
            print("The option must be numeric.")
            exit()
        return user_option

    def listing():
        archives = os.listdir(DB)

        for file in archives:
            print(file)

    option = options()

    def all_students():
        archives = os.listdir(DB)
        value = input("Choose an archive by the name and extension \'example.txt\':")

        if value in archives:
            print("The archive exists.")
        else:
            print("The archive doesn't exists.")
            exit()

        student = open(DB + value, 'r')
        student = student.read()
        print("\n" + student + "\n")

    if option == 1:
        print("Showing existent archives from the DB:\n")
        listing()
        all_students()
        exit()
    elif option == 2:
        listing()
    else:
        print("\nThat option doesn't exists.\n")
        exit()


def menu():
    print("#####################################################")
    print("Welcome to mark manager. Choose an option: \n")
    print("1: Enter new data. \n")
    print("2: Show saved info. \n")
    print("3: Exit Manager.")
    print("##################################################### \n")
    option = input("Enter your option: ")

    try:
        option = int(option)

    except ValueError:
        print("The option must be numeric.")
        exit()

    if option is None:
        print("Option can't be none.")
        exit()
    elif option <= 0 or option > 3:
        print("That option doesn't exists.\n")
        exit()
    elif option == 1:
        print("Chosen option " + str(option) + "\n")
        entering()
    elif option == 2:
        print("Chosen option " + str(option) + "\n")
        watch()
    elif option == 3:
        print("Chosen option " + str(option) + "\n")
        print("Thank you to using our manager :D.")
        exit()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nManager closed by force way. \n")
