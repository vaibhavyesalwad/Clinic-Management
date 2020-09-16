import datetime


class DoctorsData:
    def __init__(self, size):
        self.size = size
        self.rear = -1
        self.front = -1
        self.all_data = []

    def add_new(self, data):
        if self.rear == self.size -1:
            print('Doctors data full, at max', self.size, 'doctors work in hospital')
            return

        elif self.front == -1:
            self.all_data.append(data)
            print(f'{data} added info about new doctor to doctors data')
            self.front += 1
            self.rear += 1
            return

        self.all_data.append(data)
        print(f'{data} added info about new doctor to doctors data')
        self.rear += 1

    def remove(self):
        if self.rear == -1:
            print('Empty doctors data so no doctor to remove')
            return
        elif self.rear == 0:
            self.all_data.pop()
            self.rear -= 1
            self.front -= 1

        else:
            self.all_data.pop()
            self.rear -= 1

    def show_all_docs(self):
        print('Doctors in staff')
        print('id', '\t', 'name', '\t', 'spl', '\t\t','avl')
        for doc in self.all_data:
            print(doc['id'], '\t', doc['name'], '\t', doc['spl'], '\t\t', doc['avl'])

    def find_doctors(self, did=None, name=None, spl=None):
        if did is None and name is None and spl is None:
            print('Not enough enough information to search doctors')
        else:
            count = 0
            for doc in self.all_data:
                if doc['id'] == did or doc['name'] == name or doc['spl'] == spl:
                    print(doc['id'], '\t', doc['name'], '\t', doc['spl'], '\t\t', doc['avl'])
                    count += 1
            if count == 0:
                print("No such doctor found")


class PatientsData:
    def __init__(self, size):
        self.size = size
        self.rear = -1
        self.front = -1
        self.all_data = []

    def add_new(self, data):
        if self.rear == self.size -1:
            print('Patients data full, at max', self.size, 'patients can be handled by hospital')
            return

        elif self.front == -1:
            self.all_data.append(data)
            print(f'{data} added info about new patient to patients data')
            self.front += 1
            self.rear += 1
            return

        self.all_data.append(data)
        print(f'{data} added info about new patient to patients data')
        self.rear += 1

    def remove(self):
        if self.rear == -1:
            print('Empty patients data so no patient to remove')
            return
        elif self.rear == 0:
            self.all_data.pop()
            self.rear -= 1
            self.front -= 1

        else:
            self.all_data.pop()
            self.rear -= 1

    def show_all_pats(self):
        print('Patients applied for appointments')
        print('id', '\t', 'name', '\t', 'age', '\t', 'contact', '\t', 'treatment')
        for pat in self.all_data:
            print(pat['id'], '\t', pat['name'], '\t', pat['age'], '\t', pat['contact'], '\t\t', pat['spl'])

    def find_patients(self, pid=None, name=None, contact=None):
        if pid is None and name is None and contact is None:
            print('Not enough information to search patients')
        else:
            print('id', '\t', 'name', '\t', 'age', '\t', 'contact', '\t', 'treatment')
            for pat in self.all_data:
                if str(pat['id']) == str(pid) or pat['name'] == name or str(pat['contact']) == str(contact):
                    print(pat['id'], '\t', pat['name'], '\t', pat['age'], '\t', pat['contact'], '\t\t', pat['spl'])


class Appointments:
    def __init__(self, docs_data, patients_data, max_pt_to_doc=5):
        self.docs_data = docs_data
        self.patients_data = patients_data
        self.max_pt_to_doc = max_pt_to_doc
        self.appointments = self.create_apppointments()

    def create_apppointments(self):
        appointments = []
        total_pt_for_dr = {doc['id']: 0 for doc in self.docs_data}

        for doc in self.docs_data:
            patients = 0
            date = datetime.datetime.today().date()
            for pat in self.patients_data:
                if pat['spl'] == doc['spl']:
                    appointments.append({'pid': pat['id'], 'p_name': pat['name'], 'did': doc['id'],
                                  'd_name': doc['name'],'spl': doc['spl'], 'date': date})
                    patients += 1
                    if patients % 5 == 0:
                        year = date.year
                        month = date.month
                        day = date.day
                        date = datetime.date(year, month, day +1)

        return appointments

    def show_appointments(self):
        print('pid', '\t', 'patient name', '\t', 'did', '\t', 'doctor name', '\t\t', 'date', '\t\t', 'spl')
        for appointment in self.appointments:
            print(appointment['pid'], '\t\t', appointment['p_name'], '\t\t\t', appointment['did'], '\t\t',
                  appointment['d_name'], '\t\t', appointment['date'], '\t\t\t', appointment['spl'])

    def find_appointments(self, did=None, pid=None):
        if did is None and pid is None:
            print('not enough information to search appointments')
        else:
            print('pid', '\t', 'patient name', '\t', 'did', '\t', 'doctor name', '\t\t', 'date', '\t\t\t', 'spl')
            count = 0
            for appointment in self.appointments:
                if str(appointment['pid']) == str(pid) or str(appointment['did']) == str(did):
                    print(appointment['pid'], '\t\t', appointment['p_name'], '\t\t\t', appointment['did'], '\t\t',
                        appointment['d_name'], '\t\t', appointment['date'], '\t\t', appointment['spl'])
                    count += 1
            if count == 0:
                print("No appointment found")

    def check_availability(self, did=None, spl=None, date=None):
        if date is None or (did is None and spl is None):
            print('Not enough information to check availability of an appointment')
        elif did is not None:
            count = 0
            for appointment in self.appointments:
                if appointment['did'] == did and appointment['date'] == date:
                    count += 1
            if count != 5:
                return 'available'
            else:
                return None
        elif did is None and spl is not None:
            for doc in self.docs_data:
                if doc['spl'] == spl:
                    return self.check_availability(did=doc['id'], date=date)

    def take_appointment(self, pid=None, name=None, age=None, contact=None, spl=None, date=None, did=None):
        if pid is None or contact is None or spl is None or name is None or date is None:
            print('pid, patient name, contact and specialist for treatment are mandatory fields for appointment')
        else:
            if self.check_availability(did=did, spl=spl, date=date):
                for doc in self.docs_data:
                    if str(doc['id']) == str(did) or doc['spl'] == spl:
                        d_name = doc['name']
                        did = doc['id']
                        self.appointments.append({'pid': pid, 'p_name': name, 'did': did,
                                    'd_name': d_name, 'spl': spl, 'date': date})
                        print('appointment booked on', date, 'with Dr', d_name, '('+str(spl)+')')
                        pats.add_new({'name': name, 'id': pid, 'age': age, 'contact': contact, 'spl': spl})
            else:
                print('No appointment available on given date')



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
        app.take_appointment(pid=pid, name=name, age=age, spl=spl, date=date, contact=contact)

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
