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
        print('id', '\t', 'name', '\t\t', 'speciality')
        for doc in self.all_data:
            print(doc['id'], '\t', doc['name'], '\t', doc['spl'])

    def find_doctors(self, did=None, name=None, spl=None):
        if did is None and name is None and spl is None:
            print('Not enough enough information to search doctors')
        else:
            count = 0
            for doc in self.all_data:
                if doc['id'] == did or doc['name'] == name or doc['spl'] == spl:
                    print(doc['id'], '\t', doc['name'], '\t', doc['spl'])
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
        print('pid', '\t', 'patient name', '\t', 'did', '\t', 'doctor name', '\t\t', 'date', '\t\t\t', 'Speciality')
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
                        return True
            else:
                print('No appointment available on given date')