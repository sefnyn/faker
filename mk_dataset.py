from faker import Faker
from faker.providers import date_time,job,lorem

fake = Faker('en_GB')

for _ in range(10):
    dob = str(fake.date_of_birth(minimum_age=25, maximum_age=70))
    print(fake.name() + '\t' +  fake.job() + '\t' + dob + '\t' + fake.text(max_nb_chars=40))
