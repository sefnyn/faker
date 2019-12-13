"""
Make fake dataset in CSV format

Usage:
    python3 mk_dataset.py NNN

On entry:
    NNN - optional number of records to generate

On exit:
    dataset contains the fake dataset
"""

import sys,csv
from faker import Faker
from faker.providers import date_time,job,lorem,address,internet

fake = Faker('en_GB')
dataset = 'dataset.csv'

if len(sys.argv) > 1:
    default = int(sys.argv[1])
else:
    default = 10

print('Making fake dataset with ' + str(default) + ' records')
with open(dataset, 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile)
    header = ["Personal name", "D.O.B.", "Postcode", "E-mail address", "Occupation", "Random year", "Fake text"]
    mywriter.writerow(header)
    for _ in range(default):
        record = []
        dob = str(fake.date_of_birth(minimum_age=25, maximum_age=70))
        record.append(fake.name())
        record.append(dob)
        record.append(fake.postcode())
        record.append(fake.email())
        record.append(fake.job())
        record.append(fake.year())
        record.append(fake.text(max_nb_chars=40))
        mywriter.writerow(record)

