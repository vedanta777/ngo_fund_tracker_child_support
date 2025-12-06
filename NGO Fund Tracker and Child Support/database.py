# establishing connection between Python and MySQL

import mysql.connector
mydb = mysql.connector.connect (host = "*****", user = "*****", passwd = "*****")
mycursor = mydb.cursor()

# creating database for data manipulation

mycursor.execute ("create database if not exists NGO_FundTracker_ChildSupport")
mycursor.execute ("use NGO_FundTracker_ChildSupport")

# creating tables for sorting data

mycursor.execute ("create table if not exists funds (id int auto_increment primary key, type enum('donation','expense'), donor_name varchar(100), amount decimal(10,2), purpose varchar(255), date date)")
mycursor.execute ("create table if not exists children (id int auto_increment primary key, name varchar(100), age int, gender varchar(50), status enum('supported','available for adoption','adopted'))")
mycursor.execute ("create table if not exists users (id int auto_increment primary key, username varchar(100), passwd varchar(255), role enum('admin','donor'))")

# data manipulation functions

def add_funds () :
    donor_name = input("Enter name of the donor - ")
    amount = float(input("Enter the amount to be donated - "))
    type = input("Enter type as donation or expense - ")
    purpose = input("Enter purpose of donation in about 256 words max - ")
    date = input("Enter date of donation in yyyy-mm-dd format - ")
    mycursor.execute ("insert into funds (type, donor_name, amount, purpose, date) values (%s,%s,%s,%s,%s)", (type,donor_name,amount,purpose,date))
    mydb.commit()
    print("Data Entry successfull !!")

# calling the function

print ("Hello !! What would you like to do ??")

def data_manipulation () :

    print ("Here are the functions you can use - ")
    print ("1 - Enter data")
    print ("2 - Retrieve data")
    print ("3 - Get data about funds and expenses")                                                                                                              
    print ("4 -  Exit")
    choice = int(input("Enter the number corresponding to the function you wish to use - "))

    if choice == 1 :
        add_funds ()
        print ("Hello once again !!")
        data_manipulation ()
    if choice == 2 :
        name = input("Enter the name of the donor whose data you want - ")
        mycursor.execute("use ngo_fundtracker_childsupport")
        mycursor.execute ("select * from funds where donor_name = %s",(name,))
        data = mycursor.fetchall()
        if data :
            print ("Data Retrieval successful !!")
            for row in data :
                print(row)
        else :
            print ("No data found !!")
        print ("Hello once again !!")
        data_manipulation ()
    if choice == 3 :
        mycursor.execute ("select sum from funds where type = 'donation'")
        donation = cursor.fetchone()
        mycursor.execute ("select sum from funds where type = ''")
        expenses = cursor.fetchone()
        balance= float(donation) - float(expenses)
        print ("Total balance is - ", balance)
    if choice == 4 :
        print ("Okay Bye !!!")
        exit()                                                                                            
                                                                                                              
data_manipulation ()


