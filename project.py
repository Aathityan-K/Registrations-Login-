import re


def registration():
    print("""Welcome to Registration portal,

        1)email/username should have "@" and followed by "."eg:- sherlock@gmail.com,nothing@yahoo.in
        it should not be like this eg:- @gmail.com.There should not be any "." immediate next to "@" my@.in,
        it should not start with special characters and numbers

        2)password should be within (5-16) characters
        Must have minimum one special character,one digit,one uppercase,one lowercase character""")

    try:
        db = open("document.txt", "r")
        Email_id = input("Create Email :")
        Password = input("Create your password: ")
        Confirm_Password = input("Confirm your password: ")
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        P = []
        U = []
        for i in Password:
            P.append(i)
        for i in Email_id:
            U.append(i)
        integ = [i for i in P if i.isdigit()]
        lower = [i for i in P if i.islower()]
        upper = [i for i in P if i.isupper()]
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', Email_id) == None:
            print("""inValid Email,Please Enter a valid mail id with mentioned conditions""")
            registration()
        elif Password != Confirm_Password:
            print("Passwords don't match re enter correctly ,restart")
            registration()
        else:
            if len(Password) < 5 or len(Password) > 16:
                print("password should be 5-16 characters,restart")
                registration()
            elif bool(re.search('[@_!#$%^&*()<>?/\|}{~:0-9]', Email_id[0])) == True:
                print("Email id should not start with special characters and numbers,restart")
                registration()
            elif '@.' in Email_id:
                print("There should not be any '.'immediate next to @ in the email Enter correctly,restart")
                registration()
            elif Email_id in d:
                print("This email or password is not available try with another one,restart")
                registration()
            elif len(lower) == 0:
                print("""Password does not contain any special characters, 
                Must have minimum one special character,one digit,one uppercase,one lowercase character,restart""")
                registration()
            elif len(upper) == 0:
                print("""Password does not contain any special characters, 
                Must have minimum one special character,one digit,one uppercase,one lowercase character,restart""")
                registration()
            elif len(integ) == 0:
                print("""Password does not contain any special characters, 
                Must have minimum one special character,one digit,one uppercase,one lowercase character,restart""")
                registration()
            elif re.compile('[@_!#$%^&*()<>?/\|}{~:]').search(Password) == None:
                print("""Password does not contain any special characters, 
                Must have minimum one special character,one digit,one uppercase,one lowercase character,restart""")
                registration()
            else:
                db = open("document.txt", "a")
                data = db.write(Email_id + ", " + Password + "\n")
                print("Congratulations! Successfully Added, Go to login page and try to login")
                db.close()
        db.close()
    except Exception as Error:
        print(Error)


def login():
    try:
        db = open("document.txt", "r")
        Email_id = input("Enter your Email id : ")
        Password = input("Enter your password: ")

        if not len(Email_id or Password) < 1:
            d = []
            f = []
            for i in db:
                a, b = i.split(", ")
                b = b.strip()
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if data[Email_id]:
                    try:
                        if Password == data[Email_id]:
                            print("Log in success")
                            print("Hi ", Email_id, "Welcome to Guvi")
                        else:
                            print("Your Email doesn't exists,Go for registration")
                    except:
                        print("Email or Password is incorrect")
                else:
                    print("Email or Password is incorrect")
            except:
                print("Email or Password is incorrect")
        else:
            print("Please Enter Value")
        db.close()
    except Exception as Error:
        print(Error)


def forget():
    try:

        db = open("document.txt", "r")
        email_id = input("Enter your Email : ")
        if not len(email_id) < 1:
            d = []
            f = []
            for i in db:
                a, b = i.split(", ")
                b = b.strip()
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
        else:
            print("Your Email Does not exists,Go to registration")
        print("Your Password is ", data.get(email_id))
        db.close()
    except Exception as Error:
        print(Error)


def home():
    print("""Welcome to Guvi login page 
    if you have already an account click login
    if you don't have an account go to registration first
    If you Forget your password click \'forget password\'
    1.Login
    2.Registration
    3.Forget password""")
    try:
        choice = input("Enter your selection with number: ")
        if choice == "1":
            login()
        elif choice == "2":
            registration()
        elif choice == "3":
            forget()
        else:
            print("Please select correct option")
    except Exception as Error:
        print(Error)


home()