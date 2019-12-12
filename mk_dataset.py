import sys,csv
from faker import Faker
from faker.providers import date_time,job,lorem

fake = Faker('en_GB')

if len(sys.argv) > 1:
    default = int(sys.argv[1])
else:
    default = 10

print('Making fake dataset with ' + str(default) + ' records')
with open('dataset.csv', 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile)
    for _ in range(default):
        record = []
        dob = str(fake.date_of_birth(minimum_age=25, maximum_age=70))
        record.append(fake.name())
        record.append(fake.job())
        record.append(dob)
        record.append(fake.text(max_nb_chars=40))
        mywriter.writerow(record)

