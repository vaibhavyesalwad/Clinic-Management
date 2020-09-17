import datetime
from clinic_classes import *
import json

docs = DoctorsData(10)
docs.add_new({'name': 'Shubham', 'id': 1, 'spl': 'MD', 'avl': 'AM'})
docs.add_new({'name': 'Sanket', 'id': 2, 'spl': 'MS', 'avl': 'PM'})
docs.add_new({'name': 'Pratik', 'id': 3, 'spl': 'Dermatologist', 'avl': 'AM'})
docs.add_new({'name': 'Akash', 'id': 4, 'spl': 'Cardiologist', 'avl': 'PM'})
docs.add_new({'name': 'Shrikant', 'id': 5, 'spl': 'Orthopedist', 'avl': 'AM'})
docs.add_new({'name': 'Prasad', 'id': 6, 'spl': 'Neurologist', 'avl': 'PM'})
docs.show_all_docs()
print(docs.all_data)

pats = PatientsData(50)
pats.add_new({'name': 'p1', 'id': 1, 'age': 15, 'contact': 1234, 'spl': 'MD'})
pats.add_new({'name': 'p2', 'id': 2, 'age': 38, 'contact': 1264, 'spl': 'MS'})
pats.add_new({'name': 'p3', 'id': 3, 'age': 50, 'contact': 1224, 'spl': 'MD'})
pats.add_new({'name': 'p4', 'id': 4, 'age': 28, 'contact': 1294, 'spl': 'Cardiologist'})
pats.add_new({'name': 'p5', 'id': 5, 'age': 34, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p6', 'id': 6, 'age': 60, 'contact': 1284, 'spl': 'Neurologist'})
pats.add_new({'name': 'p7', 'id': 7, 'age': 10, 'contact': 1284, 'spl': 'Dermatologist'})
pats.add_new({'name': 'p8', 'id': 8, 'age': 15, 'contact': 1284, 'spl': 'MS'})
pats.add_new({'name': 'p9', 'id': 9, 'age': 30, 'contact': 1284, 'spl': 'Orthopedist'})
pats.add_new({'name': 'p10', 'id': 10, 'age': 50, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p11', 'id': 11, 'age': 45, 'contact': 1284, 'spl': 'Dermatologist'})
pats.add_new({'name': 'p12', 'id': 12, 'age': 46, 'contact': 1284, 'spl': 'Neurologist'})
pats.add_new({'name': 'p13', 'id': 13, 'age': 67, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p14', 'id': 14, 'age': 31, 'contact': 1284, 'spl': 'Neurologist'})
pats.add_new({'name': 'p15', 'id': 15, 'age': 60, 'contact': 1284, 'spl': 'Neurologist'})
pats.add_new({'name': 'p16', 'id': 16, 'age': 10, 'contact': 1284, 'spl': 'Dermatologist'})
pats.add_new({'name': 'p17', 'id': 17, 'age': 15, 'contact': 1284, 'spl': 'MS'})
pats.add_new({'name': 'p18', 'id': 18, 'age': 30, 'contact': 1284, 'spl': 'Orthopedist'})
pats.add_new({'name': 'p19', 'id': 19, 'age': 50, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p20', 'id': 20, 'age': 45, 'contact': 1284, 'spl': 'Dermatologist'})
pats.add_new({'name': 'p21', 'id': 21, 'age': 46, 'contact': 1284, 'spl': 'Cardiologist'})
pats.add_new({'name': 'p22', 'id': 23, 'age': 50, 'contact': 1224, 'spl': 'MD'})
pats.add_new({'name': 'p24', 'id': 24, 'age': 28, 'contact': 1294, 'spl': 'Cardiologist'})
pats.add_new({'name': 'p25', 'id': 25, 'age': 34, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p26', 'id': 26, 'age': 60, 'contact': 1284, 'spl': 'Neurologist'})
pats.add_new({'name': 'p27', 'id': 27, 'age': 15, 'contact': 1234, 'spl': 'Orthopedist'})
pats.add_new({'name': 'p28', 'id': 28, 'age': 38, 'contact': 1264, 'spl': 'MS'})
pats.add_new({'name': 'p29', 'id': 29, 'age': 50, 'contact': 1224, 'spl': 'MD'})
pats.add_new({'name': 'p30', 'id': 30, 'age': 28, 'contact': 1294, 'spl': 'Cardiologist'})
pats.add_new({'name': 'p31', 'id': 31, 'age': 34, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p32', 'id': 32, 'age': 21, 'contact': 1284, 'spl': 'MD'})
pats.add_new({'name': 'p33', 'id': 33, 'age': 30, 'contact': 1284, 'spl': 'Orthopedist'})
pats.add_new({'name': 'p34', 'id': 34, 'age': 28, 'contact': 1294, 'spl': 'Cardiologist'})
pats.add_new({'name': 'p35', 'id': 35, 'age': 31, 'contact': 1284, 'spl': 'Neurologist'})
pats.add_new({'name': 'p36', 'id': 36, 'age': 28, 'contact': 1294, 'spl': 'Cardiologist'})
pats.add_new({'name': 'p37', 'id': 37, 'age': 38, 'contact': 1264, 'spl': 'MS'})
pats.add_new({'name': 'p38', 'id': 38, 'age': 30, 'contact': 1284, 'spl': 'Orthopedist'})
pats.add_new({'name': 'p39', 'id': 39, 'age': 28, 'contact': 1294, 'spl': 'Cardiologist'})


pats.show_all_pats()
print()
app = Appointments(docs.all_data, pats.all_data)
app.show_appointments()
print()
app.find_appointments(did=1)
print()
docs.find_doctors(spl='MD')
print()
pats.find_patients(contact=1234)
print()
app.take_appointment(pid=50, spl='MD', contact=1264, date=datetime.date(2020, 11, 18), name='p50')
print()
app.show_appointments()
print()
pats.show_all_pats()

while True:
    print()
    print("Choose Option:")
    print("1. Find Doctor")
    print("2. Check appointment availability of doctor")
    print("3. Book appointment")
    print("4. Show all appointments")
    print("5. Find patient")
    print("6: EXit")

    option = input("Enter option:")

    if option == '1':
        print()
        print("Finding doctor")
        spl = input("Enter speciality of doctor:")
        name = input("Enter name of doctor:")
        did = input("Enter doctor id:")
        docs.find_doctors(did=did, name=name, spl=spl)

    elif option == '2':
        print()
        print('Checking appointment availability of doctor')
        spl = input("Enter speciality of doctor:")
        date = input('Enter date in YYYY-MM-DD format:')
        year, month, day = map(int, date.split('-'))
        date = datetime.date(year, month, day)
        if app.check_availability(spl=spl, date=date):
            print('Appointment available on', date)
        else:
            print('Appointment NOT available on', date, 'as doctor has hands full')

    elif option == '3':
        print()
        print('Booking an appointment')
        pid = max([pat['id'] for pat in pats.all_data]) + 1
        name = input('Enter patient name:')
        nums = '0123456789'
        while True:
            age = input('Age:')
            if all([ch in nums for ch in age]):
                break
        spl = input("Enter speciality of doctor:")

        while True:
            date = input('Enter date in YYYY-MM-DD format:')
            if all([ch in nums for part in date.split('-') for ch in part]):
                break

        year, month, day = map(int, date.split('-'))
        date = datetime.date(year, month, day)
        while True:
            contact = input('Enter mobile number:')
            if all([ch in nums for ch in contact]):
                break
        if app.take_appointment(pid=pid, name=name, age=age, spl=spl, date=date, contact=contact):
            pats.add_new({'name': name, 'id': pid, 'age': age, 'contact': contact, 'spl': spl})

    elif option == '4':
        print()
        print('Showing all booked appointments')
        app.show_appointments()

    elif option == '5':
        print()
        print('Finding patient')
        name = input('Enter patient name:')
        pid = input('Enter patient id:')
        contact = input('Enter mobile number:')
        pats.find_patients(pid=pid, name=name, contact=contact)

    elif option == '6':
        break


