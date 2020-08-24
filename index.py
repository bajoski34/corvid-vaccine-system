from classes.Doctor import Doctor
from classes.Patient import Patient

global user
user = input('Are you a Patient or Staff? (P/S/END): ').upper()


if(user == "P" or user != "S"):
    print('Your option is not valid')
    # print(user)

if(user == 'P'):
    name = input('Please Enter your name: ');
    person = Patient(name)
    print('Your name is '+ person.name)
if(user == 'S'):
    name = input('Please Enter your name: ');
    age = int(input('Enter your Age: '));
    person = Doctor(name)
    print('Your name is '+ person.name)

