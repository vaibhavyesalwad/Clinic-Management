from clinic_classes import *
import json

docs = DoctorsData(10)
pats = PatientsData(50)

# Loading existing patients data
with open('existing_patients_data.json') as f:
     pats_data = json.load(f)

# Loading existing doctors data
with open('existing_doctors_data.json') as f:
    docs_data = json.load(f)

# adding existing data to our database
docs.all_data = docs_data
pats.all_data = pats_data

docs.show_all_docs()
print()
pats.show_all_pats()
print()

# creating prior appointments using existing data
app = Appointments(docs.all_data, pats.all_data)
print("Existing appointments")
app.show_appointments()
print()

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


