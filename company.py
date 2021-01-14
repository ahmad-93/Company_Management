import sqlite3
import os,requests
from typing import Counter
from sqlite3.dbapi2 import version_info
import getpass
import time,sys
import smtplib
import random
import binascii
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import operator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
os.system("clear")
Vers = requests.get('https://pastebin.com/raw/dYNasC5t').text.format('utf-8')
db = sqlite3.connect("company.db")
cr = db.cursor()
into = cr.execute
create = "create table if not exists "
into(create+"company(worker text, password integer, job text, salary integer, email text, increase text, deduction text)")
into(create+"users(user text, password integer, email text)")
into(create+"admins(user text, password integer, email text)")
into(create+"codes(code integer)")
into(create+"safe(money integer)")
into(create+"companymail(mail text, password text)")
into(create+"cracker(crack text)")
into(create+"url(ur text)")
into("select money from safe")
rte = cr.fetchone()
if rte == None:
    into("insert into safe values('0')")
    db.commit()
into("select ur from url")
hh = cr.fetchone()
if hh == None:
    into("insert into url values('gadtyAaJ')")
into("select crack from cracker")
hh = cr.fetchone()
if hh == None:
    into("insert into cracker values('XRTK-HGFT-BBBB-SRQP')")
usrname1 = []
usrname2 = []
def speed(f):
        for e in f+"\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(00000.04)
def speedd(f):
        for e in f+"\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(00000.01)
def timm(f):
        for e in f+"\n":
            sys.stdout.write(e)
            time.sleep(00000.005)
def timmm(f):
        for e in f + "\n":
            sys.stdout.write(e)
            time.sleep(00000.0002)
def time_logo(f):
        for e in f:
            sys.stdout.write(e)
            time.sleep(00000.0005)
def time_correct(f):
        for e in f+"\n":
            sys.stdout.write(e)
            time.sleep(000000.0007)

def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
encoding='utf-8'
errors='surrogatepass'

def close_app():
    db.commit()
    db.close()
    time_logo("""\033[94m
  ####   ####   ####  #####    #####  ###### ##  ##
 ##     ##  ## ##  ## ##  ##   ##  ## ##      ####
 ## ### ##  ## ##  ## ##  ##   #####  ####     ##
 ##  ## ##  ## ##  ## ##  ##   ##  ## ##       ##
  ####   ####   ####  #####    #####  ######   ##
""")
    speed("\n\033[91mApp Is Closed..")
    timm(" "*350)

def my_account_user():
    into(f"select email from users where user = '{usrname2[0]}'")
    em = cr.fetchone()
    print(f"Name     => {usrname2[0]}")
    print("Password => ******")
    print(f"Email => {em[0]}")
    sh = input("\n\033[91m[\033[92m01\033[91m]\033[93m => Update\n\033[91m[\033[92m02\033[91m]\033[93m => Show Password 👁\n\033[91m[\033[92m03\033[91m]\033[93m => Back\n>>> ").strip()
    if sh == "1":
        wh = input("\n\033[91m[\033[92m01\033[91m]\033[93m => Update Name\n\033[91m[\033[92m02\033[91m]\033[93m => Update Password\n\033[91m[\033[92m03\033[91m]\033[93m => Email\n\033[91m[\033[92m04\033[91m]\033[93m => Back\n>>> ").strip()
        if wh == "1":
            name = input("Enter New Name: ").strip().capitalize()
            into(f"update users set user = '{name}' where user = '{usrname2[0]}'")
            speed("Name Is Updated ✅")
            usrname2.pop()
            usrname2.append(name)
            db.commit()
            my_account_user()
        elif wh == "2":
            new_password = getpass.getpass("Enter New Password: ").strip()
            bity = bin(int(binascii.hexlify(str(new_password).encode(encoding, errors)), 16))[2:]
            ner = bity.zfill(8 * ((len(bity) + 7) // 8))
            into(f"update users set password = '{ner}' where user = '{usrname2[0]}'")
            speed("Passwoed Is Updated ✅")
            db.commit()
            my_account_user()
        elif wh == "3":
            new_mail = input("Enter New Email: ").strip()
            if "@gmail.com" in new_mail:
                into(f"update users set email = '{new_mail}' where user = '{usrname2[0]}'")
                speed("Email Is Updated ✅")
                db.commit()
                my_account_user()
            else:
                speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                my_account_user()
        elif wh == "4":
            user()
        else: user()
    elif sh == "2":
        into(f"select password from users where user = '{usrname2[0]}'")
        ff = cr.fetchone()
        print(f"\nName     => {usrname2[0]}")
        print(f"Password => {ff[0]}")
        print(f"Email    => {em[0]}")
        b_d = input("\n\033[91m[\033[92m01\033[91m]\033[93m => Back\n\033[91m[\033[92m02\033[91m]\033[93m => Exit\n>>> ").strip()
        if b_d == "1":
            my_account_user()
        elif b_d == "2":
            close_app()
        else: my_account_user()
        
    elif sh == "3":
        user()
    else:
        user()

def my_account():
    into(f"select email from admins where user = '{usrname1[0]}'")
    em = cr.fetchone()
    print(f"Name     => {usrname1[0]}")
    print("Password => ******")
    print(f"Email   => {em[0]}")
    sh = input("\n\033[91m[\033[92m01\033[91m]\033[93m => Update\n\033[91m[\033[92m02\033[91m]\033[93m => Show Password 👁\n\033[91m[\033[92m03\033[91m]\033[93m => Back\n>>> ").strip()
    if sh == "1":
        wh = input("\n\033[91m[\033[92m01\033[91m]\033[93m => Update Name\n\033[91m[\033[92m02\033[91m]\033[93m => Update Password\n\033[91m[\033[92m03\033[91m]\033[93m => Email\n\033[91m[\033[92m04\033[91m]\033[93m => Back\n>>> ").strip()
        if wh == "1":
            name = input("Enter New Name: ").strip().capitalize()
            into(f"update admins set user = '{name}' where user = '{usrname1[0]}'")
            speed("Name Is Updated ✅")
            db.commit()
            usrname1.pop()
            usrname1.append(name)
            db.commit()
            my_account()
        elif wh == "2":
            new_password = getpass.getpass("Enter New Password: ").strip()
            bitr = bin(int(binascii.hexlify(str(new_password).encode(encoding, errors)), 16))[2:]
            ner = bitr.zfill(8 * ((len(bitr) + 7) // 8))
            into(f"update admins set password = '{ner}' where user = '{usrname1[0]}'")
            speed("Passwoed Is Updated ✅")
            db.commit()
            my_account()
        elif wh == "3":
            new_mail = input("Enter New Email: ").strip()
            if "@gmail.com" in new_mail:
                into(f"update admins set email = '{new_mail}' where user = '{usrname1[0]}'")
                speed("Email Is Updated ✅")
                db.commit()
                my_account()
            else:
                speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                my_account()
        elif wh == "4":
            administrator()
        else: administrator()
    elif sh == "2":
        into(f"select password from admins where user = '{usrname1[0]}'")
        ff = cr.fetchone()
        print(f"\nName     => {usrname1[0]}")
        print(f"Password => {ff[0]}")
        print(f"Email    => {em[0]}")
        b_d = input("\n\033[91m[\033[92m01\033[91m]\033[93m => Back\n\033[91m[\033[92m02\033[91m]\033[93m => Exit\n>>> ").strip()
        if b_d == "1":
            my_account()
        elif b_d == "2":
            close_app()
        else: my_account()
        
    elif sh == "3":
        administrator()
    else:
        administrator()

def about():
    os.system("clear")
    time_logo("""\033[95m    ##    ## ######## \033[0;91m👑     👑 \033[95m\033[1m######## ########  
    ###   ## ##       \033[0;96m\033[1m##     ## \033[95m\033[1m##       ##     ## 
    ####  ## ##       \033[0;96m\033[1m###   ### \033[95m\033[1m##       ##     ## 
    ## ## ## ######   \033[0;96m\033[1m#### #### \033[95m\033[1m######   ########  
    ##  #### ##       \033[0;96m\033[1m## ### ## \033[95m\033[1m##       ##   ##   
    ##   ### ##       \033[0;96m\033[1m##     ## \033[95m\033[1m##       ##    ##  
    ##    ## ######## \033[0;96m\033[1m##     ## \033[95m\033[1m######## ##     ##
    \033[0;96m\033[1m################# ##     ## ##################""")
    speedd("""
       \033[91m[\033[92m+\033[91m]\033[1m(C)opyright > Github.com/Ahmad-93\033[91m [\033[92m+\033[91m]
      \033[91m[\033[92m+\033[91m]\033[95m  App  Coded  V2.1 BY Ahmad Alnemer \033[91m[\033[92m+\033[91m]
     \033[91m[\033[92m+\033[91m]\033[92m      EMail  >  ahvip92@gmail.com     \033[91m[\033[92m+\033[91m]
    \033[91m[\033[92m+\033[91m]\033[94m  Facebook >  https://www.fb.com/viip4  \033[91m[\033[92m+\033[91m]
   \033[91m[\033[92m+\033[91m]  Instagram > instagram.com/ahmadnemer92  \033[91m[\033[92m+\033[91m]
    """)
    input("\n\033[92mPress Enter To Return Login Page...")
    login()



def back1():
        db.commit()
        timmm("""\n\033[94mReturn To The Menu Or Exit Program?
+---------------------------------+    
|         \033[91m[\033[92m01\033[91m]\033[94m  =>  Back          |
|         \033[91m[\033[92m02\033[91m]\033[94m  =>  Exit          |
+---------------------------------+
        """)
        y = input("\033[91m[\033[92m+\033[91m] \033[93m>>> ").strip()
        if y == "1":
            administrator()
        elif y == "2":
            close_app()
        else:
            print("    \033[91mNo Option !")
            back1()

def change_users():
    wh = input("Choose Option: \n\033[91m[\033[92m01\033[91m]\033[94m => Viwe All Users\n\033[91m[\033[92m02\033[91m]\033[94m => Update Users\n\033[91m[\033[92m03\033[91m]\033[94m => Delete Users\n>>> ").strip()
    if wh == "1":
        num = 0
        into("select * from users")
        real = cr.fetchall()
        if len(real) == 0:
            print("No Users In The Programe !")
        if len(real) > 0:
            print("------> View All Users <------")
        for i in real:
            print(f"\n---------[{str(num+1)}]---------")
            print(f"User => {i[0]},",end=" ")
            print(f"Password => {i[1]},",end=" ")
            print(f"Email => {i[2]}")

            num += 1
        print("-"*30)
        b_c = input("\033[91m[\033[92m01\033[91m]\033[94m => Back\n\033[91m[\033[92m02\033[91m]\033[94m => Exit\n>>> ").strip()
        if b_c == "1":
            administrator()
        else: close_app()
    elif wh == "2":
        w_u = input("Enter User Name To Update: \n>>> ").strip().capitalize()
        into(f"select user from users where user = '{w_u}'")
        ress = cr.fetchone()
        if ress == None:
            yy = input("This User I Not Exists\n\033[91m[\033[92m01\033[91m]\033[94m => Back\n\033[91m[\033[92m02\033[91m]\033[94m => Exit\n>>> ").strip()
            if yy == "1":
                back1()
            else: close_app()
        else:
            n_u = input("What Do You Want Update?\n\033[91m[\033[92m01\033[91m]\033[94m => Password\n\033[91m[\033[92m02\033[91m]\033[94m => Email\n>>> ").strip()
            if n_u == "1":
                n_p = getpass.getpass("Enter New Password: ").strip()
                count = 0
                limit = 2
                out = False
                while len(n_p) < 6 and not out:
                    if count < limit:
                        n_p = getpass.getpass("Password length must be more than 6 digits\nRe-Enter New password: ").strip()
                        count += 1
                    else:
                        out = True
                if out:
                    print("Please Try Again")
                else:
                    into(f"update users set password = '{n_p}' where user = '{w_u}'")
                    speed("Password Is Updated :)")
                    back1()
            elif wh == "2":
                n_e = input("Enter New Email: ").strip()
                if "@gmail.com" in n_e:
                    into(f"update users set email = '{n_e}' where user = '{w_u}'")
                    speed("Email Is Updated :)")
                    back1()
                else:
                    speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                    back1()
    elif wh == "3":
        d_n = input("Enter User Name To Delete: ").strip().capitalize()
        into(f"delete from users where user = '{d_n}'")
        speed("Name Is Deleted :)")
        back1()
    else: administrator()

def administrator():
    os.system("clear")
    time_logo("""\033[95m    ##    ## ######## \033[0;91m👑     👑 \033[95m\033[1m######## ########  
    ###   ## ##       \033[0;96m\033[1m##     ## \033[95m\033[1m##       ##     ## 
    ####  ## ##       \033[0;96m\033[1m###   ### \033[95m\033[1m##       ##     ## 
    ## ## ## ######   \033[0;96m\033[1m#### #### \033[95m\033[1m######   ########  
    ##  #### ##       \033[0;96m\033[1m## ### ## \033[95m\033[1m##       ##   ##   
    ##   ### ##       \033[0;96m\033[1m##     ## \033[95m\033[1m##       ##    ##  
    ##    ## ######## \033[0;96m\033[1m##     ## \033[95m\033[1m######## ##     ##
    \033[0;96m\033[1m################# ##     ## ##################""")
    timmm(f"\n\033[91m\033[1mBy Ahmed Alnemer                \033[93m\033[1mAdministrator: {usrname1[0]}           ")
    timmm("""\033[94m\033[1m-----------------------------------------------------
|-\033[91m[\033[92m+\033[91m]\033[0;96m\033[1m Welcome To The Company Management Program \033[91m[\033[92m+\033[91m]\033[94m-|\033[1m
+---------------------------------------------------+
|  \033[91m[\033[92m01\033[91m] \033[0;96m\033[1m=>\033[94m View Workers     \033[91m[\033[92m13\033[91m]\033[0;96m\033[1m =>\033[94m \033[94mMy Account      |
|  \033[91m[\033[92m02\033[91m] \033[0;96m\033[1m=>\033[94m Add Worker       \033[91m[\033[92m14\033[91m]\033[0;96m\033[1m =>\033[94m \033[94mShow Users      |
|  \033[91m[\033[92m03\033[91m] \033[0;96m\033[1m=>\033[94m Remove Worker    \033[91m[\033[92m15\033[91m]\033[0;96m\033[1m =>\033[94m \033[94mSwitch Account  |
|  \033[91m[\033[92m04\033[91m] \033[0;96m\033[1m=>\033[94m Update Workers   \033[91m[\033[92m00\033[91m]\033[0;96m\033[1m =>\033[94m \033[94mExit            |
|  \033[91m[\033[92m05\033[91m] \033[0;96m\033[1m=>\033[94m Print Workers                            |
|  \033[91m[\033[92m06\033[91m] \033[0;96m\033[1m=>\033[94m Salary Deduction                         |
|  \033[91m[\033[92m07\033[91m] \033[0;96m\033[1m=>\033[94m Salary Increase                          |
|  \033[91m[\033[92m08\033[91m] \033[0;96m\033[1m=>\033[94m Send message                             |
|  \033[91m[\033[92m09\033[91m] \033[0;96m\033[1m=>\033[94m Safe                                     |
|  \033[91m[\033[92m10\033[91m] \033[0;96m\033[1m=>\033[94m Calculator                               |
|  \033[91m[\033[92m11\033[91m] \033[0;96m\033[1m=>\033[94m Change Company Mail                      |
|  \033[91m[\033[92m12\033[91m] \033[0;96m\033[1m=>\033[94m Delete Company Data                      |
+---------------------------------------------------+""")
    msg = ("\033[91m[\033[92m+\033[91m] \033[93m\033[1mChoose Option >>> ")
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13","14", "15", "00"]
    user_input = input(msg).strip()
    print("\n")


    def change_mail():
        into("select mail from companymail")
        mm = cr.fetchone()
        if mm == None:
            new_mail = input("There Is No Company Email, Enter New Email: ").strip()
            if "@gmail.com" in new_mail:
                new_password = getpass.getpass("Enter Password: ").strip()
                r_new_password = getpass.getpass("R-Type Password: ").strip()
                if new_password == r_new_password:
                    nm_ma = new_mail, new_password
                    into("insert into companymail values(?, ?)",nm_ma)
                    speed("Email Is Added .. ✅")
                    speed("Please Allow Less Secure Apps\nFrom /Setting/Security/Allow Less Secure apps/ Turn On✅")
                    back1()
                else:
                    speed("\033[91mPassword Does Not Match, Try Again")
                    back1()
            else:
                speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                back1()
        else:
            ch = input(f"The Current Email Is: \"{mm[0]}\"\nDo You Want To Change It?\n\033[91m[\033[92m01\033[91m]\033[94m => Yes\n\033[91m[\033[92m02\033[91m]\033[94m => Back\n>>> ").strip()
            if ch == "1":
                new_mail = input("Enter New Email: ").strip()
                if "@gmail.com" in new_mail:
                    new_password = getpass.getpass("Enter Password: ").strip()
                    r_new_password = getpass.getpass("R-Type Password: ").strip()
                    if new_password == r_new_password:
                        into(f"update companymail set mail = '{new_mail}'")
                        into(f"update companymail set password = '{new_password}'")
                        speed("Email Is Updated .. ✅")
                        speed("Please Allow Less Secure Apps\nFrom /Setting/Security/Allow Less Secure apps/ Turn On✅")
                        back1()
                    else:
                        speed("\033[91mPassword Does Not Match, Try Again")
                        back1()
                else:
                    speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                    back1()
            elif ch == "2":
                administrator()
            else:
                print("\033[91mNo Option !")
                back1()




    def reset_company():
        yes = input("Do you want to reformat the company !?\n\033[91m[\033[92m01\033[91m]\033[94m => Yes\n\033[91m[\033[92m02\033[91m]\033[94m => No\n>>> ").strip()
        if yes == "1":
            yes2 = input("All Company Data Will Be Deleted, Are You Sure !?\n\033[91m[\033[92m01\033[91m]\033[94m => Yes\n\033[91m[\033[92m02\033[91m]\033[94m => No\n>>> ").strip()
            if yes2 == "1":
                code = getpass.getpass("Enter a Program Code Number: ").strip()
                coo = bin(int(binascii.hexlify(str(code).encode(encoding, errors)), 16))[2:]
                cos = coo.zfill(8 * ((len(coo) + 7) // 8))
                into(f"select code from codes where code = '{cos}'")
                co = cr.fetchone()
                if co == None:
                    if code != co:
                        speed("\nCode Is Wrong Please Try Again ...")
                        administrator()
                else:
                    into("select mail from companymail")
                    al = cr.fetchone()
                    into("select password from companymail")
                    ai = cr.fetchone()
                    From = al[0]
                    password = ai[0]
                    into("select email from admins")
                    em = cr.fetchall()
                    body = (f"Your Company Data Has Been Deleted !\nBy {usrname1[0]}")
                    try:
                        for t in [*em]:
                            msg = MIMEMultipart()
                            msg['From'] = From
                            msg['To'] = t[0]
                            msg['Subject'] = "Dear You From ViP-Company"
                            msg.attach(MIMEText(body, 'plain'))
                            server = smtplib.SMTP('smtp.gmail.com:587')
                            server.starttls()
                            server.login(From, password)
                            text = msg.as_string()
                            server.sendmail(From, t[0], text)
                            server.quit()
                    except:
                        print()
                    into("delete from login")
                    into("delete from codes")
                    into("delete from safe")
                    into("delete from company")
                    into("delete from rest")
                    speed("All Data Has Been Successfully Deleted :)")
                    db.commit()
                    login()
            else: administrator()
        else: administrator()


    def view():
        num = 0
        into("select * from company")
        result = cr.fetchall()
        if len(result) == 0:
            print("No Workers In The Company !")
        if len(result) > 0:
            print("\033[93m----\033[91m[\033[92m+\033[91m]\033[93m View All Workers \033[91m[\033[92m+\033[91m]\033[93m----")
            print(f"\033[92mThere Is In The company \033[91m{len(result)} \033[92mworkers\n")
        for r in result:
            print(f"\n---------[{str(num+1)}]---------")
            print(f"Name => {r[0]},", end=" ")
            print(f"Age => {r[1]},", end=" ")
            print(f"Job => {r[2]},", end=" ")
            print(f"Salary => {r[3]}$")
            if r[4] == "":
                print(end="")
            if r[5] == " ":
                print(end="")
            else:
                print(f"Increase => {r[5]}")
            if r[6] == " ":
                print(end="")
            else:
                print(f"Deduction => {r[6]}")
            num += 1
        print("-"*30)
        back1()


    def add():
        name = input("\033[93mAdd New Worker: ").capitalize().strip()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            age = input("\033[93mEnter He Age: ").strip()
            job = input("\033[93mEnter He Job: ").strip().capitalize()
            salary = input("\033[93mEnter He salary: ").strip().capitalize()
            def mail():
                email = input("\033[93mEnter Email: ").strip()
                if "@gmail.com" in email:
                    new_w = name, age, job, salary, email, " ", " "
                    into("insert into company values(?, ?, ?, ?, ?, ?, ?)",new_w)
                    speed("\033[93mWorker Is Added ✅")
                    back1()
                else:
                    speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                    mail()
            mail()
        else:
            print(f"\033[93m{name} Is Exist In company")
            back1()


    def delete_worker():
        name = input("Enter Worker Name To Delete: ").strip().capitalize()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            print(f"\033[93m{name} Not Exist In company")
            back1()
        else:
            into(f"delete from company where worker = '{name}'")
            speed(f"\033[93m{name} Was Deleted ✅")
            back1()


    def update_worker():
        name = input("Enter Worker Name: ").capitalize().strip()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            print(f"\033[93m{name} Not Exist In company")
            back1()
        else:
            w = input("\033[94mWhat Do You Want To Update: \n\033[91m[\033[92m01\033[91m]\033[94m => Job\n\033[91m[\033[92m02\033[91m]\033[94m => Salary\n\033[91m[\033[92m03\033[91m]\033[94m => Email\n>>> ").strip()
            if w == "1":
                job = input("Enter New Job: ").capitalize().strip()
                into(f"update company set job = '{job}' where worker = '{name}'")
                speed("\033[93mUpdated  ✅")
                back1()
            elif w == "2":
                sal = input("Enter New Salary: ").strip()
                into(f"update company set salary = '{sal}' where worker = '{name}'")
                speed("\033[93mUpdated  ✅")
                back1()
            elif w == "3":
                em = input("Enter New Email: ").strip()
                into(f"update company set email = '{em}' where worker = '{name}'")
                speed("\033[93mUpdated  ✅")
                back1()
            else:
                print(f"\033[93m{w} Is Not Found\nPlease Try Again")
                back1()


    def printd():
        file = open("workers.txt", "w")
        into("select * from company")
        result = cr.fetchall()
        if len(result) > 0:
            file.write("""========================================
=====> The Workers In The Company <=====
========================================\n""")
        num = 0
        for r in result:
            file.write(f"\n------------------[{str(num+1)}]-------------------\n")
            file.write("| Name => "+(r[0])+", Age => "+str(r[1]))
            file.write("\n| Job => "+(r[2])+", Salary => "+str(r[3])+"$""\n")
            file.write("| Email => "+(r[4])+"\n")
            if r[5] == "":
                print()
            else:
                file.write(f"| Increase => {r[5]}\n")
            if r[6] == "":
                print()
            else:
                file.write(f"| Deduction => {r[6]}\n")
            file.write("-"*40)
            num += 1
        if len(result) > 0:
            file.write("\n\n=================> End <================\n")
        file.close()
        speed("Printed In File Text :)")
        back1()


    def increase():
        name = input("Enter Worker Name To Deduct His Salary: ").strip().capitalize()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            print(f"\033[93m{name} Not Exist In company")
            back1()
        else:
            increase_value = input("Enter The Value To Increase: ").strip()
            into(f"select salary from company where worker = '{name}'")
            sl = cr.fetchone()
            into(f"update company set salary = '{int(sl[0])+int(increase_value)}' where worker = '{name}'")
            into(f"select money from safe")
            un = cr.fetchone()
            if int(increase_value) < int(un[0]):
                into(f"update safe set money = '{int(un[0])-int(increase_value)}'")
                speed("\n\033[93mThe Value Increased Successfully ✅")
                into(f"update company set increase = 'Increase {increase_value}$ In Date [{time.ctime()}]' where worker = '{name}'")
                back1()
            else:
                speed("\033[93mThere Is Not Enough Balance In The Safe")
                back1()

    def send():
        into("select mail from companymail")
        ma = cr.fetchone()
        if ma == None:
            add_new = input("There is no company email !\nAdd New Company Email?\n[ 1 ] => Add\n[ 2 ] => Back\n>>> ").strip()
            if add_new == "1":
                change_mail()
            elif add_new == "2":
                administrator()
            else:
                print("\033[91mNo Option !")
                back1
        else:
            all_one = input("\n\033[91m[\033[92m01\033[91m]\033[94m => To All Employees\n\033[91m[\033[92m02\033[91m]\033[94m => To One Employee\n>>> ").strip()
            if all_one == "1":
                into("select mail from companymail")
                al = cr.fetchone()
                into("select password from companymail")
                ai = cr.fetchone()
                From = al[0]
                password = ai[0]
                into("select email from company")
                em = cr.fetchall()
                body = input("\033[93mWrite Message :\n\n>>> ")
                try:
                    for t in [*em]:
                        msg = MIMEMultipart()
                        msg['From'] = From
                        msg['To'] = t[0]
                        msg['Subject'] = f"Dear You From ViP Company => Sent By Administrator {usrname1[0]}"
                        msg.attach(MIMEText(body, 'plain'))
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.starttls()
                        server.login(From, password)
                        text = msg.as_string()
                        server.sendmail(From, t[0], text)
                        server.quit()
                except:
                    print("\033[91mNo Send !\nCheck Employee Emails")
                    back2()
                speed(f'\n\033[93mSend Done .. ✅')
                back2()
            elif all_one == "2":
                name5 = input("\033[93mEnter Employee Name: ").strip().capitalize()
                into(f"select worker from company where worker = '{name5}'")
                result5 = cr.fetchone()
                if result5 == None:
                    print(f"{name5} Not Exist In company")
                    back2()
                else:
                    into(f"select email from company where worker = '{name5}'")
                    result6 = cr.fetchone()
                    if result6 == None:
                        print("\033[93mThis Employee Does Not Have an Email")
                        back2()
                    else:
                        into("select mail from companymail")
                        al = cr.fetchone()
                        into("select password from companymail")
                        ai = cr.fetchone()
                        From = al[0]
                        password = ai[0]
                        body = input("\033[93mWrite Message :\n\n>>> ")
                        try:
                            msg = MIMEMultipart()
                            msg['From'] = From
                            msg['To'] = result6[0]
                            msg['Subject'] = f"Dear You From ViP Company => Sent By Administrator {usrname1[0]}"
                            msg.attach(MIMEText(body, 'plain'))
                            server = smtplib.SMTP('smtp.gmail.com:587')
                            server.starttls()
                            server.login(From, password)
                            text = msg.as_string()
                            server.sendmail(From, result6[0], text)
                            server.quit()
                        except:
                            print("\033[91mNo Send !\nCheck Employee Emails")
                            back2()
                        speed(f'\n\033[93mSend Done To {name5}  ✅ ')
                        back1()
            else:
                print("\033[91mNo Option !")
                back1()


    def deduction():
        name = input("Enter Worker Name To Deduct His Salary: ").strip().capitalize()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            print(f"{name} Not Exist In company")
            back1()
        else:
            discount_value = input("Enter The Value To Be Deducted: ").strip()
            into(f"select salary from company where worker = '{name}'")
            sl = cr.fetchone()
            into(f"select money from safe")
            un = cr.fetchone()
            into(f"update company set salary = {int(sl[0])-int(discount_value)} where worker = '{name}'")
            into(f"update safe set money = {int(un[0])+int(discount_value)}")
            speed("\nThe Value Has Been Deducted Successfully :)")
            into(f"update company set deduction = 'Deduction {discount_value}$ In Date [{time.ctime()}]' where worker = '{name}'")
            back1()

    def calculator():
        from MainWindow import Ui_MainWindow
        READY = 0
        INPUT = 1
        class MainWindow(QMainWindow, Ui_MainWindow):
            def __init__(self, *args, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)
                self.setupUi(self)
                # Setup numbers.
                for n in range(0, 10):
                    getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))
                # Setup operations.
                self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
                self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
                self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
                self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7

                self.pushButton_pc.pressed.connect(self.operation_pc)
                self.pushButton_eq.pressed.connect(self.equals)

                # Setup actions
                self.actionReset.triggered.connect(self.reset)
                self.pushButton_ac.pressed.connect(self.reset)

                self.actionExit.triggered.connect(self.close)

                self.pushButton_m.pressed.connect(self.memory_store)
                self.pushButton_mr.pressed.connect(self.memory_recall)

                self.memory = 0
                self.reset()

                self.show()

            def display(self):
                self.lcdNumber.display(self.stack[-1])

            def reset(self):
                self.state = READY
                self.stack = [0]
                self.last_operation = None
                self.current_op = None
                self.display()

            def memory_store(self):
                self.memory = self.lcdNumber.value()

            def memory_recall(self):
                self.state = INPUT
                self.stack[-1] = self.memory
                self.display()

            def input_number(self, v):
                if self.state == READY:
                    self.state = INPUT
                    self.stack[-1] = v
                else:
                    self.stack[-1] = self.stack[-1] * 10 + v

                self.display()

            def operation(self, op):
                if self.current_op:  # Complete the current operation
                    self.equals()

                self.stack.append(0)
                self.state = INPUT
                self.current_op = op

            def operation_pc(self):
                self.state = INPUT
                self.stack[-1] *= 0.01
                self.display()

            def equals(self):
                # Support to allow '=' to repeat previous operation
                # if no further input has been added.
                if self.state == READY and self.last_operation:
                    s, self.current_op = self.last_operation
                    self.stack.append(s)

                if self.current_op:
                    self.last_operation = self.stack[-1], self.current_op

                    try:
                        self.stack = [self.current_op(*self.stack)]
                    except Exception:
                        self.lcdNumber.display('Err')
                        self.stack = [0]
                    else:
                        self.current_op = None
                        self.state = READY
                        self.display()
        if __name__ == '__main__':
            app = QApplication([])
            app.setApplicationName("Calculator")

            window = MainWindow()
            app.exec_()
            administrator()

    def safe():
        sa = input("\033[91m[\033[92m01\033[91m]\033[94m => Add Money\n\033[91m[\033[92m02\033[91m]\033[94m => Take Money\n\033[91m[\033[92m03\033[91m]\033[94m => View Money\n>>> ").strip()
        if sa == "1":
            add_money = input("Enter The Value To Add: ").strip()
            a_add = input("Are You Sure?? Y,N : ").strip().capitalize()
            if a_add == "Y" or a_add == "Yes":
                into(f"select money from safe")
                ls = cr.fetchone()

                into(f"update safe set money = '{int(ls[0])+int(add_money)}'")
                into("select mail from companymail")
                al = cr.fetchone()
                into("select password from companymail")
                ai = cr.fetchone()
                From = al[0]
                password = ai[0]
                into("select email from admins")
                em = cr.fetchall()
                body = (f"An Amount Of {add_money}$ Was Added To The Company's Treasury\n\nThe Current Company Balance Is {int(ls[0])+int(add_money)}$")
                try:
                    for t in [*em]:
                        msg = MIMEMultipart()
                        msg['From'] = From
                        msg['To'] = t[0]
                        msg['Subject'] = "Dear You From ViP-Company"
                        msg.attach(MIMEText(body, 'plain'))
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.starttls()
                        server.login(From, password)
                        text = msg.as_string()
                        server.sendmail(From, t[0], text)
                        server.quit()
                except:
                    print()
                speed("\033[93mMoney Is Added ✅")
                back1()
            else: back1()
        elif sa == "2":
            take_money = input("Enter The Value To Be Taken: ").strip()
            t_money = input("Are You Sure?? Y,N : ").strip().capitalize()
            if t_money == "Y" or t_money == "Yes":
                into(f"select money from safe")
                sl = cr.fetchone()
                if int(take_money) < int(sl[0]):
                    into(f"update safe set money = {int(sl[0])-int(take_money)}")
                    into("select mail from companymail")
                    al = cr.fetchone()
                    into("select password from companymail")
                    ai = cr.fetchone()
                    From = al[0]
                    password = ai[0]
                    into("select email from admins")
                    em = cr.fetchall()
                    body = (f"The Sum Of {take_money}$ Was Taken From The Company\n\nThe Current Company Balance Is {int(sl[0])-int(take_money)}$")
                    try:
                        for t in [*em]:
                            msg = MIMEMultipart()
                            msg['From'] = From
                            msg['To'] = t[0]
                            msg['Subject'] = "Dear You From ViP-Company"
                            msg.attach(MIMEText(body, 'plain'))
                            server = smtplib.SMTP('smtp.gmail.com:587')
                            server.starttls()
                            server.login(From, password)
                            text = msg.as_string()
                            server.sendmail(From, t[0], text)
                            server.quit()
                    except:
                        print()
                    speed("\033[93mThe Money Was Taken ✅")
                    back1()
                else:
                    speed("\033[93mThere Is Not Enough Balance In The Safe :(")
                    back1()
        elif sa == "3":
            sum = 0
            s = []
            into("select salary from company")
            to = cr.fetchall()
            into(f"select money from safe")
            ls = cr.fetchone()
            for i in [*to]:
                s.append(i[0])
            for t in s:
                sum += t
            print("+-----------------------------------+")
            print(f"| Money Is In The Safe     => ",end="")
            print(f"\033[91m{ls[0]}$")
            print(f"\033[94m| Workers Salaries         => ",end="")
            print(f"\033[91m{sum}$")
            print("\033[94m+-----------------------------------+")
            print(f"\033[94m| Net money                => ",end="")
            print(f"\033[91m{(ls[0])-sum}$")
            print("\033[94m+-----------------------------------+")
            back1()
        else:
            print(f"\033[93m{sa} Is Not Found")
            back1()


    if user_input in lst:
        if user_input == "1":
            view()
        elif user_input == "2":
            add()
        elif user_input == "3":
            delete_worker()
        elif user_input == "4":
            update_worker()
        elif user_input == "5":
            printd()
        elif user_input == "6":
            deduction()
        elif user_input == "7":
            increase()
        elif user_input == "8":
            send()
        elif user_input == "9":
            safe()
        elif user_input == "10":
            calculator()
        elif user_input == "11":
            change_mail()
        elif user_input == "12":
            reset_company()
        elif user_input == "13":
            my_account()
        elif user_input == "14":
            change_users()
        elif user_input == "15":
            login()
        else:
            close_app()
    else:
        if len(user_input) <= 0:
            print("    \033[91mNo Option !")
        else:
            print(f"\033[93mThis {user_input} Is Not Found")
        close_app()

def back2():
        db.commit()
        timmm("""\n\033[94mReturn To The Menu Or Exit Program?
+---------------------------------+    
|         \033[91m[\033[92m01\033[91m]\033[94m  =>  Back          |
|         \033[91m[\033[92m02\033[91m]\033[94m  =>  Exit          |
+---------------------------------+
        """)
        y = input("\033[91m[\033[92m+\033[91m] \033[93m>>> ").strip()
        if y == "1":
            user()
        elif y == "2":
            close_app()
        else:
            print("    \033[91mNo Option !")
            back2()
            
def user():
    os.system("clear")
    into("create table if not exists company(worker text,age integer, job text, salary integer, email text, increase text, deduction text)")
    time_logo("""\033[95m\033[1m    ##    ## ######## \033[0;91m\033[1m👑     👑 \033[95m\033[1m######## ########  
    \033[1m###   ## ##       \033[0;96m\033[1m##     ## \033[95m\033[1m##       ##     ## 
    \033[1m####  ## ##       \033[0;96m\033[1m###   ### \033[95m\033[1m##       ##     ## 
    \033[1m## ## ## ######   \033[0;96m\033[1m#### #### \033[95m\033[1m######   ########  
    \033[1m##  #### ##       \033[0;96m\033[1m## ### ## \033[95m\033[1m##       ##   ##   
    \033[1m##   ### ##       \033[0;96m\033[1m##     ## \033[95m\033[1m##       ##    ##  
    \033[1m##    ## ######## \033[0;96m\033[1m##     ## \033[95m\033[1m######## ##     ##
    \033[0;96m\033[1m################# ##     ## ##################""")
    timmm(f"\n\033[91m\033[1mBy Ahmed Alnemer                       \033[93m\033[1mUser: {usrname2[0]}           ")
    timmm("""\033[94m\033[1m-----------------------------------------------------
|-\033[91m[\033[92m+\033[91m]\033[0;96m\033[1m Welcome To The Company Management Program \033[1m\033[91m[\033[92m+\033[91m]\033[94m-|\033[1m
+---------------------------------------------------+
|         \033[91m[\033[92m01\033[91m] \033[0;96m\033[1m => \033[94m View All Workers                |
|         \033[91m[\033[92m02\033[91m] \033[0;96m\033[1m => \033[94m Add Worker                      |
|         \033[91m[\033[92m03\033[91m] \033[0;96m\033[1m => \033[94m Update Worker Properties        |
|         \033[91m[\033[92m04\033[91m] \033[0;96m\033[1m => \033[94m Print Workers In File Text      |
|         \033[91m[\033[92m05\033[91m] \033[0;96m\033[1m => \033[94m Send E-mail message             |
|         \033[91m[\033[92m06\033[91m] \033[0;96m\033[1m => \033[94m Calculator                      |
|         \033[91m[\033[92m07\033[91m] \033[0;96m\033[1m => \033[94m My Account                      |
|         \033[91m[\033[92m08\033[91m] \033[0;96m\033[1m => \033[94m Switch Account                  |
|         \033[91m[\033[92m00\033[91m] \033[0;96m\033[1m => \033[94m Exit                            |
+---------------------------------------------------+""")
    msg = ("""\033[91m[\033[92m+\033[91m] \033[93m\033[1mChoose Option >>> """)
    lst = ["1", "2", "3", "4", "5", "6", "7","8", "00"]
    user_input = input(msg).strip()
    print("\n")


    def view():
        num = 0
        into("select * from company")
        result = cr.fetchall()
        if len(result) == 0:
            print("No Workers In The Company !")
        if len(result) > 0:
            print("\033[93m----\033[91m[\033[92m+\033[91m]\033[93m View All Workers \033[91m[\033[92m+\033[91m]\033[93m----")
            print(f"\033[92mThere Is In The company \033[91m{len(result)} \033[92mworkers\n")
        for r in result:
            print(f"\n---------[{str(num+1)}]---------")
            print(f"Name => {r[0]},", end=" ")
            print(f"Age => {r[1]},", end=" ")
            print(f"Job => {r[2]},", end=" ")
            print(f"Salary => {r[3]}$")
            if r[4] == "":
                print(end="")
            if r[5] == " ":
                print(end="")
            else:
                print(f"Increase => {r[5]}")
            if r[6] == " ":
                print(end="")
            else:
                print(f"Deduction => {r[6]}")
            num += 1
        print("-"*30)
        back2()


    def add():
        name = input("\033[93mAdd New Worker: ").capitalize().strip()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            age = input("\033[93mEnter He Age: ").strip()
            job = input("\033[93mEnter He Job: ").strip().capitalize()
            salary = input("\033[93mEnter He salary: ").strip().capitalize()
            
            def mail():
                email = input("\033[93mEnter Email: ").strip()
                if "@gmail.com" in email:
                    new_w = name, age, job, salary, email, " ", " "
                    into("insert into company values(?, ?, ?, ?, ?, ?, ?)",new_w)
                    speed("\033[93mWorker Is Added ✅")
                    back2()
                else:
                    speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                    mail()
            mail()
        else:
            print(f"\033[93m{name} Is Exist In company")

    def update_worker():
        name = input("Enter Worker Name: ").capitalize().strip()
        into(f"select worker from company where worker = '{name}'")
        result = cr.fetchone()
        if result == None:
            print(f"\033[93m{name} Not Exist In company")
            back2()
        else:
            w = input("\033[94mWhat Do You Want To Update: \n\033[91m[\033[92m01\033[91m]\033[94m => Job\n\033[91m[\033[92m02\033[91m]\033[94m => Salary\n\033[91m[\033[92m03\033[91m]\033[94m => Email\n>>> ").strip()
            if w == "1":
                job = input("Enter New Job: ").capitalize().strip()
                into(f"update company set job = '{job}' where worker = '{name}'")
                speed("\033[93mUpdated  ✅")
                back2()
            elif w == "2":
                print("Just Administrator He Can Edit Salary")
                back2()
            elif w == "3":
                em = input("Enter New Email: ").strip()
                into(f"update company set email = '{em}' where worker = '{name}'")
                speed("\033[93mUpdated  ✅")
                back2()
            else:
                print(f"\033[93m{w} Is Not Found\nPlease Try Again")
                back2()

    def send():
        into("select mail from companymail")
        ma = cr.fetchone()
        if ma == None:
            print("There is no company email !\nplease contact the manager to add an email to the company")
            back2()
        else:
            all_one = input("\n\033[91m[\033[92m01\033[91m]\033[94m => To All Employees\n\033[91m[\033[92m02\033[91m]\033[94m => To One Employee\n>>> ").strip()
            if all_one == "1":
                into("select mail from companymail")
                al = cr.fetchone()
                into("select password from companymail")
                ai = cr.fetchone()
                From = al[0]
                password = ai[0]
                into("select email from company")
                em = cr.fetchall()
                body = input("\033[93mWrite Message :\n\n>>> ")
                try:
                    for t in [*em]:
                        msg = MIMEMultipart()
                        msg['From'] = From
                        msg['To'] = t[0]
                        msg['Subject'] = f"Dear You From ViP Company => Sent By Employee {usrname2}"
                        msg.attach(MIMEText(body, 'plain'))
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.starttls()
                        server.login(From, password)
                        text = msg.as_string()
                        server.sendmail(From, t[0], text)
                        server.quit()
                except:
                    print("\033[91mNo Send !\nCheck Employee Emails")
                    back2()
                speed(f'\n\033[93mSend Done .. ✅')
                back2()
            elif all_one == "2":
                name5 = input("Enter Employee Name: ").strip().capitalize()
                into(f"select worker from company where worker = '{name5}'")
                result5 = cr.fetchone()
                if result5 == None:
                    print(f"\033[93m{name5} Not Exist In company")
                    back2()
                else:
                    into(f"select email from company where worker = '{name5}'")
                    result6 = cr.fetchone()
                    if result6 == None:
                        print("\033[93mThis Employee Does Not Have an Email")
                        back2()
                    else:
                        into("select mail from companymail")
                        al = cr.fetchone()
                        into("select password from companymail")
                        ai = cr.fetchone()
                        From = al[0]
                        password = ai[0]

                        body = input("\033[93mWrite Message :\n\n>>> ")
                        try:
                            msg = MIMEMultipart()
                            msg['From'] = From
                            msg['To'] = result6[0]
                            msg['Subject'] = f"Dear You From ViP Company => Sent By Employee {usrname2[0]}"
                            msg.attach(MIMEText(body, 'plain'))
                            server = smtplib.SMTP('smtp.gmail.com:587')
                            server.starttls()
                            server.login(From, password)
                            text = msg.as_string()
                            server.sendmail(From, result6[0], text)
                            server.quit()
                        except:
                            print("\033[91mNo Send !\nCheck Employee Emails")
                            back2()
                        speed(f'\n\033[93mSend Done To {name5}  ✅ ')
                        back2()
            else:
                print("\033[91mNo Option !")
                back2()

    def printd():
        file = open("workers.txt", "w")
        into("select * from company")
        result = cr.fetchall()
        if len(result) > 0:
            file.write("""========================================
=====> The Workers In The Company <=====
========================================\n""")
        num = 0
        for r in result:
            file.write(f"\n------------------[{str(num+1)}]-------------------\n")
            file.write("| Name => "+(r[0])+", Age => "+str(r[1]))
            file.write("\n| Job => "+(r[2])+", Salary => "+str(r[3])+"$""\n")
            file.write("| Email => "+(r[4])+"\n")
            if r[5] == "":
                print()
            else:
                file.write(f"| Increase => {r[5]}\n")
            if r[6] == "":
                print()
            else:
                file.write(f"| Deduction => {r[6]}\n")
            file.write("-"*40)
            num += 1
        if len(result) > 0:
            file.write("\n\n=================> End <================\n")
        file.close()
        speed("Printed In File Text :)")
        back2()


    def calculator():
        from MainWindow import Ui_MainWindow
        READY = 0
        INPUT = 1
        class MainWindow(QMainWindow, Ui_MainWindow):
            def __init__(self, *args, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)
                self.setupUi(self)
                # Setup numbers.
                for n in range(0, 10):
                    getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))
                # Setup operations.
                self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
                self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
                self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
                self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7

                self.pushButton_pc.pressed.connect(self.operation_pc)
                self.pushButton_eq.pressed.connect(self.equals)

                # Setup actions
                self.actionReset.triggered.connect(self.reset)
                self.pushButton_ac.pressed.connect(self.reset)

                self.actionExit.triggered.connect(self.close)

                self.pushButton_m.pressed.connect(self.memory_store)
                self.pushButton_mr.pressed.connect(self.memory_recall)

                self.memory = 0
                self.reset()

                self.show()

            def display(self):
                self.lcdNumber.display(self.stack[-1])

            def reset(self):
                self.state = READY
                self.stack = [0]
                self.last_operation = None
                self.current_op = None
                self.display()

            def memory_store(self):
                self.memory = self.lcdNumber.value()

            def memory_recall(self):
                self.state = INPUT
                self.stack[-1] = self.memory
                self.display()

            def input_number(self, v):
                if self.state == READY:
                    self.state = INPUT
                    self.stack[-1] = v
                else:
                    self.stack[-1] = self.stack[-1] * 10 + v

                self.display()

            def operation(self, op):
                if self.current_op:  # Complete the current operation
                    self.equals()

                self.stack.append(0)
                self.state = INPUT
                self.current_op = op

            def operation_pc(self):
                self.state = INPUT
                self.stack[-1] *= 0.01
                self.display()

            def equals(self):
                # Support to allow '=' to repeat previous operation
                # if no further input has been added.
                if self.state == READY and self.last_operation:
                    s, self.current_op = self.last_operation
                    self.stack.append(s)

                if self.current_op:
                    self.last_operation = self.stack[-1], self.current_op

                    try:
                        self.stack = [self.current_op(*self.stack)]
                    except Exception:
                        self.lcdNumber.display('Err')
                        self.stack = [0]
                    else:
                        self.current_op = None
                        self.state = READY
                        self.display()
        if __name__ == '__main__':
            app = QApplication([])
            app.setApplicationName("Calculator")

            window = MainWindow()
            app.exec_()
            user()


    if user_input in lst:
        if user_input == "1":
            view()
        elif user_input == "2":
            add()
        elif user_input == "3":
            update_worker()
        elif user_input == "4":
            printd()
        elif user_input == "5":
            send()
        elif user_input == "6":
            calculator()
        elif user_input == "7":
            my_account_user()
        elif user_input == "8":
            login()
        else:
            close_app()
    else:
        if len(user_input) <= 0:
            print("    \033[91mNo Option !")
        else:
            print(f"This {user_input} Is Not Found")
        close_app()

def change_code():
    def co():
        into("select mail from companymail")
        al = cr.fetchone()
        into("select password from companymail")
        ai = cr.fetchone()
        From = al[0]
        password = ai[0]
        into("select email from admins")
        em = cr.fetchall()
        body = (f"The company code has been reset\nNew code: {new_code}")
        try:
            for t in [*em]:
                msg = MIMEMultipart()
                msg['From'] = From
                msg['To'] = t[0]
                msg['Subject'] = "Change Code"
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(From, password)
                text = msg.as_string()
                server.sendmail(From, t[0], text)
                server.quit()
        except: print()
    into("select code from codes")
    kk = cr.fetchone()
    if kk == None:
        n_code = getpass.getpass("\033[93mCreate New Code: ").strip()
        m_code = getpass.getpass("\033[93mRetype The Code: ").strip()
        if len(n_code) <= 0:
            print("No Option !")
        if n_code == m_code:
            bits = bin(int(binascii.hexlify(str(n_code).encode(encoding, errors)), 16))[2:]
            news = bits.zfill(8 * ((len(bits) + 7) // 8))
            into("insert into codes values(0)")
            into(f"update codes set code = '{news}'")
            speed("\033[93mCode Is Created ✅")
            close_app()
        else:
            print("\033[93mThe Code Does Not Match\nPlease Try Again")
            close_app()
    else:     
        last_code = getpass.getpass("\033[93mEnter Last Code: ").strip()
        bitss = bin(int(binascii.hexlify(str(last_code).encode(encoding, errors)), 16))[2:]
        news1 = bitss.zfill(8 * ((len(bitss) + 7) // 8))
        into(f"select code from codes where code = '{news1}'")
        resulte = cr.fetchone()
        if resulte == None:
            if last_code != resulte:
                last_code2 = getpass.getpass("\033[93mWrong Code, R-Enter Last Code: ").strip()
                bits2 = bin(int(binascii.hexlify(str(last_code2).encode(encoding, errors)), 16))[2:]
                news2 = bits2.zfill(8 * ((len(bits2) + 7) // 8))
                into(f"select code from codes where code = '{news2}'")
                resulte2 = cr.fetchone()
                if resulte2 == None:
                    if last_code2 != resulte2:
                        if_wrong = input("\033[93mDid You Forget The Code !, Y, N :\n>>> ").strip().capitalize()
                        if if_wrong == "Y" or if_wrong == "Yes":
                                rand = random.randint(1000,9999)
                                bits = bin(int(binascii.hexlify(str(rand).encode(encoding, errors)), 16))[2:]
                                new = bits.zfill(8 * ((len(bits) + 7) // 8))
                                into("select mail from companymail")
                                al = cr.fetchone()
                                into("select password from companymail")
                                ai = cr.fetchone()
                                From = al[0]
                                password = ai[0]
                                into("select email from admins")
                                em = cr.fetchall()
                                body = (f"The reset code is\n{rand}")
                                try:
                                    for t in [*em]:
                                        msg = MIMEMultipart()
                                        msg['From'] = From
                                        msg['To'] = t[0]
                                        msg['Subject'] = "Dear You From ViP-Company"
                                        msg.attach(MIMEText(body, 'plain'))
                                        server = smtplib.SMTP('smtp.gmail.com:587')
                                        server.starttls()
                                        server.login(From, password)
                                        text = msg.as_string()
                                        server.sendmail(From, t[0], text)
                                        server.quit()
                                except: print("")
                                co_res = input("Check Your MailBox And Enter Reset Code: ").strip()
                                n = int(new, 2)
                                new2 = int2bytes(n).decode(encoding, errors)
                                if new2 != co_res:
                                    speed("Wrong Code, Try Again")
                                    close_app()
                                else:
                                    new_code = getpass.getpass("\033[93mEnter New Code: ").strip()
                                    l_code = getpass.getpass("\033[93mRetype The Code: ").strip()
                                    if len(new_code) <= 0:
                                        print("\033[91mNo Option !")
                                    if new_code == l_code:
                                        bito = bin(int(binascii.hexlify(str(new_code).encode(encoding, errors)), 16))[2:]
                                        news3 = bito.zfill(8 * ((len(bito) + 7) // 8))
                                        into(f"update codes set code = '{news3}'")
                                        co()
                                        speed("\033[93mUpdated Code ✅")
                                        close_app()
                                    else:
                                        print("\033[93mThe Code Does Not Match\nPlease Try Again")
                                        close_app()

                        else:
                            print("\033[91mNo Option !") 
                            close_app()
                                    
                    else:
                        new_code = getpass.getpass("\033[93mEnter New Code: ").strip()
                        l_code = getpass.getpass("\033[93mRetype The Code: ").strip()
                        if len(new_code) <= 0:
                            print("\033[91mNo Option !")
                            close_app()
                        if new_code == l_code:
                            bito = bin(int(binascii.hexlify(str(new_code).encode(encoding, errors)), 16))[2:]
                            news3 = bito.zfill(8 * ((len(bito) + 7) // 8))
                            into(f"update codes set code = '{news3}'")
                            co()
                            speed("\033[93mUpdated Code ✅")
                            close_app()
                        else:
                            print("\033[93mThe Code Does Not Match\nPlease Try Again")
                            close_app()

                else:
                    new_code = getpass.getpass("\033[93mEnter New Code: ").strip()
                    l_code = getpass.getpass("\033[93mRetype The Code: ").strip()
                    if len(new_code) <= 0:
                        print("No Option !")
                        close_app()
                    if new_code == l_code:
                        bito = bin(int(binascii.hexlify(str(new_code).encode(encoding, errors)), 16))[2:]
                        news3 = bito.zfill(8 * ((len(bito) + 7) // 8))
                        into(f"update codes set code = '{news3}'")
                        speed("\033[93mUpdated Code ✅")
                        co()
                        close_app()
                    else:
                        print("\033[93mThe Code Does Not Match\nPlease Try Again")
                        close_app()

        else:
            new_code = getpass.getpass("\033[93mEnter New Code: ").strip()
            l_code = getpass.getpass("\033[93mRetype The Code: ").strip()
            if len(new_code) <= 0:
                print("\033[91mNo Option !")
                close_app()
            if new_code == l_code:
                bito = bin(int(binascii.hexlify(str(new_code).encode(encoding, errors)), 16))[2:]
                news3 = bito.zfill(8 * ((len(bito) + 7) // 8))
                into(f"update codes set code = '{news3}'")
                co()
                speed("\033[93mUpdated Code ✅")
                close_app()
            else:
                print("\033[93mThe Code Does Not Match\nPlease Try Again")
                close_app()


def correct():
    os.system("clear")
    time_correct("""\033[94m







##      ## ######## ##        ######   #######  ##     ## ######## 
##  ##  ## ##       ##       ##    ## ##     ## ###   ### ##       
##  ##  ## ##       ##       ##       ##     ## #### #### ##       
##  ##  ## ######   ##       ##       ##     ## ## ### ## ######   
##  ##  ## ##       ##       ##       ##     ## ##     ## ##       
##  ##  ## ##       ##       ##    ## ##     ## ##     ## ##       
 ###  ###  ######## ########  ######   #######  ##     ## ######## 
""")
    timm("  "*60)


def upd():
    msg ="\n\033[91mConnecting ..........."
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
    if Vers == "2.1":
        print("\033[93m\nYou Are Using The New Version  ✅")
        input("Press Enter To continue...")
        login()
    else:
        up = input("\nYou Are Using The Old Version, Do You Want To Update? Y, N: ").strip().capitalize()
        if up == "Y" or up == "yes":
            aroon ="\n Update Strated !\n"
            for i in aroon:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.02)
            os.system('git clone https://github.com/ahmad-93/company_management && cd company_management')
            speed("Program Is Updated ✅")
            timm(" "*200)
            if os.name=='nt':
                os.system('cls')
            else:
                os.system('clear')
            os.system('company.py')
        elif up == "N" or up == "No":
            login()
        else: login()


def login():
    os.system("clear")
    
    time_logo(f"""\033[1m\033[95m
    ##       ####  \033[0;96m\033[1m  ####  \033[95m\033[1m ######  ##  ## 
    ##      ##  ## \033[0;96m\033[1m ##     \033[95m\033[1m   ##    ### ## 
    ##      ##  ## \033[0;96m\033[1m ## ### \033[95m\033[1m   ##    ## ### 
    ##      ##  ## \033[0;96m\033[1m ##  ## \033[95m\033[1m   ##    ##  ## 
    ######   ####  \033[0;96m\033[1m  ####  \033[95m\033[1m ######  ##  ## 
                                  \033[97mVer: {Vers}""")
    timmm("""\n\033[1m    \033[91m[\033[92m+\033[91m]\033[93mLogin as Administrator Or User\033[91m[\033[92m+\033[91m]
  \033[94m\033[1m+---------------------------------------+    
  |      \033[91m[\033[92m01\033[91m] \033[0;96m => \033[94m \033[1mAdministrator          |
  |      \033[91m[\033[92m02\033[91m] \033[0;96m => \033[94m \033[1mUser                   |
  |      \033[91m[\033[92m03\033[91m] \033[0;96m => \033[94m \033[1mchange Program code    |
  |      \033[91m[\033[92m04\033[91m] \033[0;96m => \033[94m \033[1mCheck For Update       |
  |      \033[91m[\033[92m05\033[91m] \033[0;96m => \033[94m \033[1mAbout                  |
  |      \033[91m[\033[92m06\033[91m] \033[0;96m => \033[94m \033[1mExit                   |
  \033[94m+---------------------------------------+""")

    master = input("\033[91m[\033[92m+\033[91m] \033[93mChoose Option >>> ").strip()


    if master == "1":
        into("select code from codes")
        kk = cr.fetchone()
        if kk == None:
            n_code = getpass.getpass("\033[93mCreate New Code: ").strip()
            l_code = getpass.getpass("\033[93mRetype The Code: ").strip()
            if len(n_code) <= 0:
                print("    \033[91mNo Option !")
            if n_code == l_code:
                bitr = bin(int(binascii.hexlify(str(n_code).encode(encoding, errors)), 16))[2:]
                newsa = bitr.zfill(8 * ((len(bitr) + 7) // 8))
                into("insert into codes values(0)")
                into(f"update codes set code = '{newsa}'")
                speed("\033[93mCode Is Created ✅")
                close_app()
            else:
                print("\033[93mThe Code Does Not Match\nPlease Try Again")
                close_app()
                
        else:

            user_name = input("\033[93mEnter User Name: ").strip().capitalize()
            into(f"select user from admins where user = '{user_name}' ")
            result = cr.fetchone()
            if result == None:
                add = input("You Are Not Administrator, Add You? Y,N : ").strip().capitalize()
                if add == "Y" or add == "Yes":
                    code = getpass.getpass("\033[93mEnter a Program Code Number: ").strip()
                    bit1 = bin(int(binascii.hexlify(str(code).encode(encoding, errors)), 16))[2:]
                    news11 = bit1.zfill(8 * ((len(bit1) + 7) // 8))
                    into(f"select code from codes where code = '{news11}'")
                    co = cr.fetchone()
                    if co == None:
                        if code != co:
                            y = input("\n\033[93mCode Is Wrong\nLogin As a User? Y, N\n>>> ").strip().capitalize()
                            if y == "Y" or y == "Yes":
                                usrname2.append(user_name)
                                correct()
                                user()
                            elif y == "N" or y == "No":
                                close_app()
                            else: close_app()
                    else:
                        password = getpass.getpass("\033[93mEnter New Password: ").strip()
                        count = 0
                        limit = 2
                        out = False
                        while len(password) < 6 and not out:
                            if count < limit:
                                password = getpass.getpass("\033[93mPassword length must be more than 6 digits\nRe-Enter New password: ").strip()
                                count += 1
                            else:
                                out = True
                        if out:
                            print("Please Try Again")
                        else:
                            adm = bin(int(binascii.hexlify(str(password).encode(encoding, errors)), 16))[2:]
                            ads = adm.zfill(8 * ((len(adm) + 7) // 8))
                            def mail():
                                em_meneger = input("\033[93mEnter Your Email: ").strip()
                                if "@gmail.com" in em_meneger:
                                    gg2 = user_name, ads, em_meneger
                                    into("insert into admins values (?, ?, ?)",gg2)
                                    speed("\033[93mYou Added In Administrators..")
                                    log = input("\033[93mLog in with this account?\n\033[91m[\033[92m01\033[91m]\033[94m => Yes\n\033[91m[\033[92m02\033[91m]\033[94m => Back\n\033[91m[\033[92m03\033[91m]\033[94m => Exit\n>>> ").strip()
                                    if log == "1":
                                        usrname1.append(user_name)
                                        correct()
                                        administrator()
                                    elif log == "2":
                                        login()
                                    elif log == "3":
                                        close_app()
                                    else: 
                                        close_app()
                                else:
                                    speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                                    mail()
                            mail()
                            
                            
                else:
                    login()
            else:
                pas = getpass.getpass("\033[93mEnter Your Password: ").strip()
                adm1 = bin(int(binascii.hexlify(str(pas).encode(encoding, errors)), 16))[2:]
                ads1 = adm1.zfill(8 * ((len(adm1) + 7) // 8))
                into(f"select password from admins where password = '{ads1}' and user = '{user_name}'")
                resu = cr.fetchone()
                if resu == None:
                    r_pas = getpass.getpass("\033[93mPassword Is Wrong\nRe-Enter the password: ").strip()
                    adm2 = bin(int(binascii.hexlify(str(r_pas).encode(encoding, errors)), 16))[2:]
                    ads2 = adm2.zfill(8 * ((len(adm2) + 7) // 8))
                    into(f"select password from admins where password = '{ads2}' and user = '{user_name}'")
                    re = cr.fetchone()
                    if re == None:
                        print("\n\033[91mPassword Is Wrong\nPlease Try Again..")
                    else:
                        code = getpass.getpass("\033[93mEnter a Program Code: ").strip()
                        bit1 = bin(int(binascii.hexlify(str(code).encode(encoding, errors)), 16))[2:]
                        news11 = bit1.zfill(8 * ((len(bit1) + 7) // 8))
                        into(f"select code from codes where code = '{news11}'")
                        co = cr.fetchone()
                        if co == None:
                            if code != co:
                                y = input("\n\033[93mCode Is Wrong\nLogin As a User? Y, N\n>>> ").strip().capitalize()
                                if y == "Y" or y == "Yes":
                                    usrname2.append(user_name)
                                    correct()
                                    user()
                                elif y == "N" or y == "No":
                                    close_app()
                                else: close_app()
                        else:
                            usrname1.append(user_name)
                            correct()
                            administrator()
                else:
                    code = getpass.getpass("\033[93mEnter a Program Code Number: ").strip()
                    bit1 = bin(int(binascii.hexlify(str(code).encode(encoding, errors)), 16))[2:]
                    news11 = bit1.zfill(8 * ((len(bit1) + 7) // 8))
                    into(f"select code from codes where code = '{news11}'")
                    co = cr.fetchone()
                    if co == None:
                        if code != co:
                            y = input("\n\033[93mCode Is Wrong\nLogin As a User? Y, N\n>>> ").strip().capitalize()
                            if y == "Y" or y == "Yes":
                                usrname2.append(user_name)
                                user()
                            elif y == "N" or y == "No":
                                close_app()
                            else: close_app()
                    else:
                        usrname1.append(user_name)
                        correct()
                        administrator()

    elif master == "2":
        user_name = input("\033[93mEnter User Name: ").strip().capitalize()
        into(f"select user from users where user = '{user_name}' ")
        result = cr.fetchone()
        if result == None:
            add = input("\033[93mYou Are Not An Office Employee, Add You? Y,N : ").strip().capitalize()
            if add == "Y" or add == "Yes":
                password = getpass.getpass("\033[93mEnter New Password: ").strip()
                count = 0
                limit = 2
                out = False
                while len(password) < 6 and not out:
                    if count < limit:
                        password = getpass.getpass(
                            "\033[93mPassword length must be more than 6 digits\nRe-Enter New password: ").strip()
                        count += 1
                    else:
                        out = True
                if out:
                    print("\033[93mPlease Try Again")
                else:
                    sha = bin(int(binascii.hexlify(str(password).encode(encoding, errors)), 16))[2:]
                    rew = sha.zfill(8 * ((len(sha) + 7) // 8))
                    def mail2():
                        email = input("\033[93mEnter Your Email: ").strip()
                        if "@gmail.com" in email:
                            gg = user_name, rew, email
                            into("insert into users values (?, ?, ?)",gg)
                            speed("\033[93mYou Added In Users..")
                            log = input("Log in with this account?\n\033[91m[\033[92m01\033[91m]\033[94m => Yes\n\033[91m[\033[92m02\033[91m]\033[94m => Back\n\033[91m[\033[92m03\033[91m]\033[94m => Exit\n>>> ").strip()
                            if log == "1":
                                usrname2.append(user_name)
                                correct()
                                user()
                            elif log == "2":
                                login()
                            elif log == "3":
                                close_app()
                            else: close_app()
                        else:
                            speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                            mail2()
                    mail2()
            else:
                login()
        else:
            pas = getpass.getpass("\033[93mEnter Your Password: ").strip()
            sha2 = bin(int(binascii.hexlify(str(pas).encode(encoding, errors)), 16))[2:]
            rew2 = sha2.zfill(8 * ((len(sha2) + 7) // 8))
            into(f"select password from users where user = '{user_name}' and password = '{rew2}'")
            resu = cr.fetchone()
            if resu == None:
                    r_pas = getpass.getpass("\n\033[93mPassword Is Wrong\nRe-Enter the password: ")
                    sha3 = bin(int(binascii.hexlify(str(r_pas).encode(encoding, errors)), 16))[2:]
                    rew3 = sha3.zfill(8 * ((len(sha3) + 7) // 8))
                    into(f"select password from users where user = '{user_name}' and password = '{rew3}'")
                    re = cr.fetchone()
                    if re == None:
                        speed("\n\033[91mPassword Is Wrong\nPlease Try Again..")
                        login()
                    else:
                        usrname2.append(user_name)
                        correct()
                        user()
            else:
                usrname2.append(user_name)
                correct()
                user()

    elif master == "3":
        change_code()
    elif master == "4":
        upd()
    elif master == "5":
        about()
    elif master == "6":
        close_app()
    else:
        if len(master) == 0 :
            print("    \033[91mNo Option !")
            close_app()
        else: close_app()

def chek():
    into("select user from admins")
    mai = cr.fetchone()
    if mai == None:
        correct()
        timm(" "*350)
        os.system("clear")
        speed("""\033[0;96m\033[1m
        Welcome To The >Nemer< Program To Manage The Company
            at First You Have To Do Some Things
            Such as Adding an Email To The Company
                Creating a Code For The Program
                And Then Adding a New Manager
        """)
        input("Press Enter To Start...")
        def mail():
            new_mail = input("\033[93m\033[1m\nEnter New Company Email: ").strip()
            if "@gmail.com" in new_mail:
                new_password = getpass.getpass("Enter Password: ").strip()
                r_new_password = getpass.getpass("R-Type Password: ").strip()
                if new_password == r_new_password:
                    gg = new_mail, new_password
                    into("insert into companymail values(?, ?)",gg)
                    speed("Email Is Added .. ✅")
                    speed("Please Allow Less Secure Apps\nFrom /Setting/Security/Allow Less Secure apps/ Turn On✅")
                    db.commit()
                    input("\nPress Enter To continue...")
                    
                else:
                    speed("\033[91mPassword Does Not Match, Try Again")
                    mail()
            else:
                speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                mail()
        mail()
        def code():
            n_code = getpass.getpass("\033[93m\nCreate New Code: ").strip()
            m_code = getpass.getpass("\033[93mRetype The Code: ").strip()
            if len(n_code) <= 0:
                print("No Option !")
                code()
            if n_code == m_code:
                bits = bin(int(binascii.hexlify(str(n_code).encode(encoding, errors)), 16))[2:]
                news = bits.zfill(8 * ((len(bits) + 7) // 8))
                into("insert into codes values(0)")
                into(f"update codes set code = '{news}'")
                speed("\033[93mCode Is Created ✅")
                input("\nPress Enter To continue...")
                
            else:
                print("\033[93mThe Code Does Not Match\nPlease Try Again")
                code()
        code()
        def New_Admin():
            ad_name = input("\033[93m\nEnter Menegar Name: ").strip().capitalize()

            password = getpass.getpass("\033[93mEnter Password: ").strip()
            count = 0
            limit = 2
            out = False
            while len(password) < 6 and not out:
                if count < limit:
                    password = getpass.getpass("\033[93mPassword length must be more than 6 digits\nRe-Enter New password: ").strip()
                    count += 1
                else:
                    out = True
            if out:
                print("Please Try Again")
                speed("\033[91mApp Is Closed")
            else:
                adm = bin(int(binascii.hexlify(str(password).encode(encoding, errors)), 16))[2:]
                ads = adm.zfill(8 * ((len(adm) + 7) // 8))
                def mail():
                    em_meneger = input("\033[93m\nEnter Your Email: ").strip()
                    if "@gmail.com" in em_meneger:
                        gg = ad_name, ads, em_meneger
                        into("insert into admins values (?, ?, ?)",gg)
                        speed("\033[93mYou Added In Administrators..✅")
                        input("\nPress Enter To continue...")
                        os.system("clear")
                        speed("""
        Ok , The Program’s Basics Have Been Prepared
        You Can Now Log In And Start Working (:""")
                        input("\nPress Enter And Restart Program...")
                        speed("\033[91mApp Is Closed")
                        db.commit()
                        db.close()
                    else:
                        speed("\033[91mThe Email Is Invalid\nThe Extension Must Be \"@gmail.com\" Exclusively\nTry Again")
                        mail()
                mail()
        New_Admin()
    else:
        login()

def crack():
    try:
        into("select crack from cracker")
        crak = cr.fetchone()
        into("select ur from url")
        url = cr.fetchone()
        crack = requests.get(f'https://pastebin.com/raw/{url[0]}').text.format('utf-8')

        if crak[0] in crack:
            chek()
        else:
            print("""\033[91m\033[1m
            You Need Activation Key🔑..!
             Activation has expired
           Please Activate The Program\n
           Contact The Programmer on:\n
        Facebook: https://www.fb.com/viip4
           Gmail: ahvip92@gmail.com\n""")
            try:
                new_crack = input("\033[93mEnter Crack: ").strip()
                pasw = input("Enter Password: ").strip()
            
                version = requests.get('https://pastebin.com/raw/'+pasw).text.format('utf-8')
                if new_crack == version:
                    into(f"update cracker set crack = '{new_crack}'")
                    into(f"update url set ur = '{pasw}'")
                    speed("\nActivation Completed Successfully ✅, Thank You")
                    timm(" "*200)
                    db.commit()
                    chek()
                else: print("\033[91m\nCrack Not Found")
            except:
                print("\033[91m\nCrack Not Found")
    except:
        speed("\033[91m\033[1m\nNo Internet Connection.. :(")
        speed("""\033[91m\033[1m\n
        You must be connected to the Internet
           for the program to work properly\n""")
        timm(" "*200)
        login()     
crack()
