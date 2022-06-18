
# c.execute(""" CREATE TABLE User(
#       FirstName text,
#       LastName text,
#       age integer,
#       address text,
#       city text,
#       zipcode integer,
#       password text,
#       gender text
# ) """)


from tkinter import *
import sqlite3
from tkinter import messagebox


def delete():
    # create database
    conn = sqlite3.connect('facebook.db')

    # create cursor
    c = conn.cursor()

    # delete a record
    c.execute("DELETE from User WHERE oid = " + ID_box.get())
    print('Deleted Successfully')

    # query of the database
    c.execute("SELECT *, oid FROM User")

    records = c.fetchall()
    # print(records)

    # Loop through the results
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + \
            ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


def update():

    global editor

    editor = Tk()
    editor.title('Update Data')
    # editor.iconbitmap('E:/images/global.ico')
    editor.geometry('300x480')

    # Create a databases or connect to one
    conn = sqlite3.connect('facebook.db')

    # Create cursor
    c = conn.cursor()

    record_id = ID_box.get()

    # query of the database
    c.execute("SELECT * FROM User WHERE oid=" + record_id)

    records = c.fetchall()
    # print(records)

    # Creating global variable for all text boxes
    global Firstname_editor
    global Lastname_editor
    global age_editor
    global address_editor
    global city_editor
    global zipcode_editor
    global password_editor
    global gender_editor

    # Create text boxes
    Firstname_editor = Entry(editor, width=30)
    Firstname_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    Lastname_editor = Entry(editor, width=30)
    Lastname_editor.grid(row=1, column=1)

    age_editor = Entry(editor, width=30)
    age_editor.grid(row=2, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    password_editor = Entry(editor, width=30)
    password_editor.grid(row=6, column=1)

    gender_editor = Entry(editor, width=30)
    gender_editor.grid(row=7, column=1)
    # Create textbox labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Age")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="Address")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="City")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zip Code")
    zipcode_label.grid(row=5, column=0)
    password_label = Label(editor, text="Password")
    password_label.grid(row=6, column=0)
    gender_label = Label(editor, text="Gender")
    gender_label.grid(row=7, column=0)

    edit_btn = Button(editor, text=" SAVE ", command=edit, padx=50)
    edit_btn.grid(row=10, column=1,  pady=10)

    # loop through the results
    for record in records:
        Firstname_editor.insert(0, record[0])
        Lastname_editor.insert(0, record[1])
        age_editor.insert(0, record[2])
        address_editor.insert(0, record[3])
        city_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
        password_editor.insert(0, record[6])
        gender_editor.insert(0, record[7])


def edit():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    record_id = ID_box.get()
    c.execute(""" UPDATE User SET
        FirstName=:first,
        LastName =:last,
        age =:age,
        address =:address,
        city =:city,
        zipcode=:zipcode ,
        password =:password,
        gender =:gender
         WHERE oid = :oid""",
              {
                  'first': Firstname_editor.get(),
                  'last': Lastname_editor.get(),
                  'age': age_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'password': password_editor.get(),
                  'gender': gender_editor.get(),
                  'oid': record_id}
              )
    conn.commit()
    conn.close()
    editor.destroy()


def query():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM User")
    records = c.fetchall()
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + \
            ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('facebook.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO User VALUES (:FirstName, :LastName, :age, :address, :city, :zipcode,:password,:gender)", {
        'FirstName': f_name.get(),
        'LastName': l_name.get(),
        'age': age.get(),
        'address': address.get(),
        'city': city.get(),
        'zipcode': zipcode.get(),
        'password': Password_box.get(),
        'gender': Gender_box.get(),
    })
    # showinfo messagebox
    messagebox.showinfo("Adresses", "Inserted Successfully")

    conn.commit()

    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)
    Password_box.delete(0, END)
    Gender_box.delete(0, END)


root = Tk()
root.title('Facebook')
conn = sqlite3.connect('facebook.db')
c = conn.cursor()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)


age = Entry(root, width=30)
age.grid(row=2, column=1)

address = Entry(root, width=30)
address.grid(row=3, column=1)


city = Entry(root, width=30)
city.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

Password_box = Entry(root, width=30)
Password_box.grid(row=6, column=1)


Gender_box = Entry(root, width=30)
Gender_box.grid(row=7, column=1)

# Create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Age")
address_label.grid(row=2, column=0)

city_label = Label(root, text="Address")
city_label.grid(row=3, column=0)    

state_label = Label(root, text="City")
state_label.grid(row=4, column=0)


zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

Password_label = Label(root, text="Password")
Password_label.grid(row=6, column=0)

Gender_label = Label(root, text="Gender")
Gender_label.grid(row=7, column=0)

Update_label = Label(root, text="ID to del/update")
Update_label.grid(row=10, column=0)
submit = Button(root, text="Submit", command=submit, padx=100).grid(
    row=8, column=1, padx=70, pady=10)
Log_in = Button(root, text='Show Records', command=query, padx=80).grid(
    row=9, column=1, columnspan=2, padx=70, pady=10)


ID_box = Entry(root, width=30)
ID_box.grid(row=10, column=1)

Update = Button(root, text='Update', command=update, padx=100)
Update.grid(row=11, column=1, pady=10)
Delete = Button(root, text='Delete', command=delete,
                padx=100).grid(row=13, column=1, padx=10, pady=10)

root.mainloop()
