import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

def addrecord():
    print("Add a new Record")
    print("================")
    f=open('Railway.csv','a')
    s=csv.writer(f)
    
    Tid=int(input('Enter Tid='))
    Tname=input('Enter Tname=')
    State =input('Enter Country=')
    Destination=input('Enter Destination=')    
    Duration=int(input('Enter Duration='))

    rec=[Tid,Tname,State,Destination,Duration]
    s.writerow(rec)
    f.close()
    print("Record Saved")
    input("Press any key to continue..")


def modifyrecord():
    print("Modify a Record")
    print("================")
    f=open('Railway.csv','r',newline='\r\n')
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter State you want to modify')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("State=",rec[0])
            print("TotalRailways=",rec[1])
            print("Sale=",rec[2])
            print("Rent=",rec[3])
            choice=input("Do you want to modify this record(y/n)")
            if choice=='y' or choice=='Y':
                sale=int(input('Enter Railway for Sale='))
                rent=input('Enter Railway for rent=')
                rec[0]=rec[0]
                rec[1]=int(sale)+int(rent)
                rec[2]=sale
                rec[3]=rent
                rec=[rec[0],rec[1],sale,rent]
                s1.writerow(rec)
                print("Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()  
    f1.close()
    os.remove("Railway.csv")
    os.rename("temp.csv","Railway.csv")
    input("Press any key to continue..")

def deleterecord():
    print("Delete a Record")
    print("================")
    f=open('Railway.csv','r',newline='\r\n')
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter Train ID you want to delete')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("Train=",rec[0])
            print("TotalRailways=",rec[1])
            print("Sale=",rec[2])
            print("Rent=",rec[3])
            choice=input("Do you want to delete this record(y/n)")
            if choice=='y' or choice=='Y':
                pass
                print("Record Deleted")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("Railway.csv")
    os.rename("temp.csv","Railway.csv")
    input("Press any key to continue..")

    

df=pd.read_csv('Railway.csv')
while(True):
    print("")
    print("#######################################################")
    print("#                   KYF Real Estate                   #")
    print("#######################################################")
    print("")
    print("1: Railway status")
    print("2: Railway Status Graph")
    print("6: Add New Country Railway Status")
    print("7: Update Sales and Rent Railway Status")
    print("8: Remove a Country Railway Status")
    print("9: Exit")
    print("")
    c=int(input("Enter your choice"))
    print("")
    if(c==1):
        df=pd.read_csv('Railway.csv')
        print(df)
    elif(c==2):
        plt.bar(df.State,df.TotalRailways,width=1,color=['c','r','b','g','y','m'])
        plt.xlabel("COUNTRIES")
        plt.ylabel("TOTAL RailwayS")
        plt.title("Railway TRACKER")
        plt.show()

    elif(c==6):
        addrecord()
    elif(c==7):
        modifyrecord()
    elif(c==8):
        deleterecord()
    elif(c==9):
        break
    else:
        print("Invalid Choice")      
        

           
           
