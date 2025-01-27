from tkinter import *
from tkinter import messagebox
root = Tk() # экземпляр класса
root.geometry('600x400')
root.title ('Телефонная  Книга')
root.config (bg = 'light grey')
root.resizable (0,0)
Database = [
    ['Drew', 'DeLeon', '4567891', 'address4', 'drew@deleon.com'],
    ['Jon', 'DeLeon', '4567891', 'address4', 'drew@deleon.com'],
    ['Bill', 'DeLeon', '4567891', 'address4', 'drew@deleon.com'],
    ]
FirstName_entry = StringVar()
LastName_entry = StringVar()
ContactNumber_entry = IntVar()
Address_entry = StringVar()
Email_entry = StringVar()
frame = Frame(root)# наследование
frame.pack (side = RIGHT)

scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox (frame, yscrollcommand = scroll.set, height =15,)
scroll.config (command = select.yview)
scroll.pack(side = RIGHT, fill = Y)
select.pack(side = LEFT, fill = BOTH, expand = 1)

def selected():
    return select.curselection()[0]
def delete():
    Database.pop(selected())
    selectset()
def add():
    with open("Phone_Data_Base.txt","w") as f:
        for element in Database:
            f.writelines(str(element))
            f.writelines('\n')
#         f.writelines(spisok)
    Database.append([FirstName_entry.get(), LastName_entry.get(),
                    ContactNumber_entry.get(), Address_entry.get(), Email_entry.get()])
    selectset()
    print("Contact added")
def search():
    FirstName = FirstName_entry.get()
    result = None
    for record in Database:
        if record[0] == FirstName:
            result = record
    view(result)
    print(result)
def view(contact):
    FIRSTNAME, LASTNAME, CONTACTNUMBER, ADDRESS, EMAIL = contact[0], contact[1], contact[2], contact[3], contact[4]
    FirstName_entry.set(FIRSTNAME)
    LastName_entry.set(LASTNAME)
    ContactNumber_entry.set(CONTACTNUMBER)
    Address_entry.set(ADDRESS)
    Email_entry.set(EMAIL)
def selectset():
    Database.sort()
    select.delete (0,END)
    for contact in Database:
        select.insert(END, contact[0] + "-" + contact[1]) #Конконтинация строки
selectset()


FILE_CONTACTS = 'contacts.txt'### константа для удобства
#FirstName
Label(root, text = 'First Name', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=20)
Entry(root, textvariable = FirstName_entry).place (x=130, y=20)
#LastName
Label(root, text = 'Last Name', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=70)
Entry(root, textvariable = LastName_entry).place (x=130, y=70)
#Contact Number
Label(root, text = 'Contact Number', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=0, y=120)
Entry(root, textvariable = ContactNumber_entry).place (x=130, y=120)
#Address
Label(root, text = 'Address', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=170)
Entry(root, textvariable = Address_entry).place (x=130, y=170)
#email
Label(root, text = 'Email', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=220)
Entry(root, textvariable = Email_entry).place (x=130, y=220)


#AddContact
Button(root, text = 'Add Contact', font = 'arial 12 bold',bg = 'white', command = add).place(x=70, y=280)
#Delete
Button(root, text = 'Delete Contact', font = 'arial 12 bold',bg = 'white', command = delete).place(x=215, y=330)
#Search
Button(root, text = 'Search Contact', font = 'arial 12 bold',bg = 'white', command = search).place(x=70, y=330)
#SortContacts
Button(root, text = 'Sort Contacts', font = 'arial 12 bold',bg = 'white', command = selectset).place(x=200, y=280)


root.mainloop()