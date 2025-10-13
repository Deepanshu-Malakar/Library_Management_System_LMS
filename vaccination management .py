#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices)
print(voices[0].id)
engine.setProperty("voice",voices[0].id)
print("*-------------------------------------------------- ___________________________________----------------------------------------------------------------------------*")
print("**-------------------------------------------------|                                                                      |--------------------------------------------------------------------------**")
print("***----------------------------------------------- |Welcome to Vaccination Management System |-------------------------------------------------------------------------***")
print("****--------------------------------------------- |___________________________________|------------------------------------------------------------------------****")
print("******---------------------------------------------------------------------------------------------------------------------------------------------------------------------------******")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Welcome ,to, Vaccination management system.")
#________________________________________________________________________________________________________________________________
u=""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1234")
if mydb.is_connected:
    speak("Connection Established successfully")
cur=mydb.cursor()
#__________________________________________________________________________________________________________________________________
#Creating the Database
cur.execute("create database if not exists Vaccination_management")
cur.execute("use Vaccination_management")

#Creating tables(1.Registration, 2.Vaccination , 3.certificate)
cur.execute(
    "create table if not exists Registration(Reg_no int primary key,Name varchar(20),Age int,Aadhar_no int,Gender char(1),Address varchar(50),Health_conditions Varchar(50))")

cur.execute(
    "create table if not exists vaccination(Reg_no int,Name varchar(20),First_dose char(2),Second_dose char(2))")

cur.execute(
    "create table if not exists Certificate(Reg_no int,Name varchar(20),Certificated varchar(20))")

cur.execute("Alter table Certificate modify Certificated varchar(30)")
mydb.commit()



#________________________________________________________________________________________________________________________________

def register():
    cur.execute("select * from registration")
    data=cur.fetchall()
    r=100+len(data)
    speak("your registration number is "+str(r))
    print("your registration number is",r)
    speak("Now sir")
    speak("Please!, provide us, the following information, of the person, you want to register.")
    n=input("enter  name: ")
    Age=int(input("Enter  Age: "))
    Aadhar_no=int(input("Enter  Aadhar no: "))
    Gender=input("Enter gender m/f: ")
    Address=input("Enter Address: ")
    Health_conditions=input("Do you have any major disease:")
    query="insert into Registration values(%s,%s,%s,%s,%s,%s,%s)"
    v1=(r,n,Age,Aadhar_no,Gender,Address,Health_conditions)
    cur.execute(query,v1)  #values inserted in registration
    mydb.commit()
    query="insert into Vaccination values(%s,%s,%s,%s)"
    v2=(r,n,"NO","NO")
    cur.execute(query,v2)  #Values inserted in vaccination
    mydb.commit()
    query="insert into Certificate values(%s,%s,%s)"
    v3=(r,n,"NO")
    cur.execute(query,v3)  #values inserted in registration
    mydb.commit()
    if Gender=="m":
        speak("Congratulations: Mister "+n+" :Registration ,completed ,Successfully.")
        print("Congratulations: Mister "+n+" :Registration ,completed ,Successfully.")
        print(110*"-")
    elif Gender=="f":
        speak("Congratulations: Mis "+n+" :Registration ,completed, Successfully.")
        print("Congratulations: Mis "+n+" :Registration ,completed, Successfully.")
        print(110*"-")
    
    
#_________________________________________________________________________________________________________________________________

def Display_info():
    speak(u+"sir,"+"Please provide us, the registration number, of the person, whose information, you want.")
    r=int(input("Enter registration number of person whose info you want: "))
    speak("Which information do you want? ")
    print("1.registration\n2.vaccination\n3.certificate\n4.all")
    a=int(input("enter task number: "))
    print(110*"-")
    if a==1:
        cur.execute("select * from registration")
        d1=cur.fetchall()
        for row in d1:
            if row[0]==r:
                speak("Displaying registration information, of"+row[1])
                print("Registration number=",row[0])
                print("Name=",row[1])
                print("Age=",row[2])
                print("Aadhar number=",row[3])
                print("Gender=",row[4])
                print("Address=",row[5])
                print("Major disease=",row[6])
                print(110*"-")


    elif a==2:
        cur.execute("select * from vaccination")
        d1=cur.fetchall()
        for row in d1:
            if row[0]==r:
                speak("Displaying vaccination information, of"+row[1])
                print("Registration number=",row[0])
                print("Name=",row[1])
                print("First Dose=",row[2])
                print("Second Dose=",row[3])
                print(110*"-")

                
    elif a==3:
        cur.execute("select * from Certificate")
        d1=cur.fetchall()
        for row in d1:
            if row[0]==r:
                speak("Displaying Certificate information, of"+row[1])
                print("Registration number=",row[0])
                print("Name=",row[1])
                print("Certificate=",row[2])
                print(110*"-")


    elif a==4:
        
        cur.execute("select * from vaccination")
        d1=cur.fetchall()
        
        cur.execute("select * from Certificate")
        d2=cur.fetchall()

        cur.execute("select * from registration")
        d3=cur.fetchall()
        
        for row in d3:
            if row[0]==r:
                speak("Displaying All the information, of"+row[1])
                print("Registration number=",row[0])
                print("Name=",row[1])
                print("Age=",row[2])
                print("Aadhar number=",row[3])
                print("Gender=",row[4])
                print("Address=",row[5])
                print("Major disease=",row[6])

                
        for row in d1:
            if row[0]==r:
                print("First Dose=",row[2])
                print("Second Dose=",row[3])
        for row in d2:
            if row[0]==r:
                print("Certificate=",row[2])
                print(110*"-")                
                
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Update_Vaccination_Information():
    speak("Please ,provide us, the registration number, of the person ,whose vaccination, is to be done.")
    r=int(input("enter registration number of the person whose vaccination is to be done: "))
    t=(r,)
    cur.execute("select * from certificate where Reg_no=%s",t)
    data=cur.fetchall()
    for row in data:
        if row[2]=="NO":
            cur.execute("update vaccination set First_dose='OK' where Reg_no=%s",(r,))
            cur.execute("update certificate set Certificated='Partially Vaccinated' where Reg_no=%s",(r,))
            mydb.commit()
            speak("Congratulations, "+row[1]+" ,You are now partially vaccinated ")
            print("Congratulations, "+row[1]+" ,You are now partially vaccinated ")
            print(110*"-")
        if row[2]=="Partially Vaccinated":
            cur.execute("update vaccination set Second_dose='OK' where Reg_no=%s",(r,))
            cur.execute("update certificate set Certificated='Fully Vaccinated' where Reg_no=%s",(r,))
            mydb.commit()
            speak("Congratulations, "+row[1]+" ,You are now Fully vaccinated ")
            print("Congratulations, "+row[1]+", You are now Fully vaccinated ")
            print(110*"-")
        if row[2]=="Fully Vaccinated":
            speak(row[1]+" ,Sorry! ,Ummm, You are already ,fully vaccinated.")
            print(row[1]+" ,Sorry! ,Ummm, You are already ,fully vaccinated.")
            print(110*"-")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Login():
    speak("Logging in")
    users=["Mayank","Aditya","Deepanshu","External"]
    speak("May we know your name sir:")
    global u
    u=input("enter user name:")
    if u in users:
        speak("Welcome  "+u+" sir")
        print("Welcome  "+u+" sir")
        print(110*"=")

        while True:
            print("1.register")
            print("2.Display Information")
            print("3.Update_Vaccination_Information")
            print("4.exit")
            speak(u+"sir, How may I help you?")
            a=int(input("enter task number: "))
            print(110*"=")
            if a==1:
                register()
            elif a==2:
                Display_info()
            elif a==3:
                Update_Vaccination_Information()
            elif a==4:
                speak("Thankyou "+u+" sir, for using our service.")
                print("Thankyou "+u+" sir, for using our service.")
                print(200*"x")
                break
    else:
        speak("Sorry "+u+": you dont have access permissions")
        print("Sorry "+u+": you dont have access permissions")
        print(200*"x")
        
#_________________________________________________________________________________________________________________________________
Login()
