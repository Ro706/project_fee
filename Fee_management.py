# FEE MANAGEMENT
import pandas as pd 
from pyfiglet import Figlet
f=Figlet(font='slant')
print(f.renderText("FEE MANAGEMENT"))
roll=[]
classs=[]
name=[]
age=[]
city =[]
fee_deposite=[]
fee_month=[]
l=""
n="y"
data = {"ROLL NUMBER":roll,"CLASS":classs,"NAME":name,"AGE":age,"CITY":city,"FEE":fee_deposite,"FEE MONTH":fee_month}
df=pd.DataFrame(data)  
df=pd.read_csv("/home/dcoder/fee management/stud2.csv")    
df2=pd.read_csv('/home/dcoder/fee management/stud.csv' )
df=pd.concat([df,df2])
def show_all():
    print(df)
def search_roll():
    n = int(input("ENTER ROLL NUMBER:"))
    print(df[df['ROLL NUMBER'] == n])
def search_name():
    n = str(input("ENTER NAME :"))
    print(df[df["NAME"] == n])

def search_age():
    n = int(input("ENTER AGE:"))
    print(df[df["AGE"] == n])
    
def search_city():    
    n = str(input("ENTER CITY:"))
    print(df[df["CITY"] == n])
    
    
def search():
    print("1.ROLL NUMBER")
    print("2.NAME")
    print("3.AGE")
    print("4.CITY")
    print("5.ALL")
    return int(input("ENTERTHE CHOICE:"))

def fee_depositing():
    n = int(input("ENTER THE ROLL NUMBER :"))
    a = int(input("ENTER THE FEE TO BE DEPOSITE:")) 
    b = str(input("ENTER MONTH OF FEE : "))
def menu():
    print("ENTER 1: TO ADD STUDENT")
    print("ENTER 2: TO VIEW STUDENT")
    print("ENTER 3: TO DEPOSIT FEE")
    print("ENTER 4: TO REMOVE STUDENT")
    print("ENTER 5: TO VIEW FEE OF ANY STUDENT")
    return int(input("please select an above option:"))
    
loop = 1
choice = 0
while loop == 1:
  choice = menu()         
  if choice == 1:
      while n == "y":
          roll.append(int(input("ENTER THE ROLL NUMBER:")))
          name.append(str(input("ENTER THE NAME:")))
          age.append(int(input("ENTER AGE OF STUDENT:")))
          classs.append(str(input("ENTER THE CLASS :")))
          city.append(str(input("ENTER THE CITY:")))
          data ={"ROLL NUMBER":roll,"NAME":name,"AGE":age,"CLASS":classs,"CITY":city}
          df=pd.DataFrame(data)
          df.to_csv('/home/dcoder/fee management/stud.csv')
          df.to_csv('/home/dcoder/fee management/stud2.csv')
          n = str(input("want to run again(y/n):"))
  elif choice ==2:  
      loop = 2
      while loop ==2 :
        choice = search()
        if choice == 1:
            search_roll()
            n = str(input("want to run again(y/n): "))
            if n == "n":
                loop = 1
            else:
                pass    
        elif choice == 2:
            search_name()
            n = str(input("want to run again(y/n): "))
            if n == "n":
                loop = 1
            else:
                pass    
        elif choice == 3:
            search_age()
            n = str(input("want to run again(y/n): "))
            if n == "n":
                loop = 1
            else:
                pass    
        elif choice == 4:
            search_city()
            n = str(input("want to run again(y/n): "))
            if n == "n":
                loop = 1
            else:
                pass    
        elif choice == 5:
            show_all()
            n = str(input("want to run again(y/n): "))
            if n == "n":
                loop = 1
            else:
                pass    
        else:
            print("ERROR")
            pass
  elif choice == 3:
      n = int(input("ENTER THE ROLL NUMBER :"))
      a = int(input("ENTER THE FEE TO BE DEPOSITE:")) 
      b = str(input("ENTER MONTH OF FEE : "))
      fee_deposite.append(a)
      fee_month.append(b)
      fee = {"ROLL NUMBER":n,"FEE":fee_deposite,"FEE MONTH":fee_month}
      df2 = pd.DataFrame(fee)
      df2.to_csv('/home/dcoder/fee management/fee.csv')         
      print(df2)  
  elif choice == 5:
      while n == 'y':
          df2=pd.read_csv('/home/dcoder/fee management/fee.csv')
          a = int(input("ENTER THE ROLL NUMBER:"))
          print(df2[df2["ROLL NUMBER"] == a])
          n=str(input("want to run again(y/n):"))
  elif choice == 4:
      while n == 'y':
          a =int(input("INDEX NUMBER:"))                              
          df = df.drop([a],axis=0)
          a = int(input("INDEX NUMBER:"))
          df2 = df.drop([a],axis=0)
          print(df)
          df.to_csv('/home/dcoder/fee management/stud.csv')
          df.to_csv('/home/dcoder/fee management/stud2.csv')
          n = str(input("want to run again(y/n):"))
  else:
      print("ERROR")    

