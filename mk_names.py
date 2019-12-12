from faker import Faker
#fake = Faker('en_GB')
fake = Faker('ar_EG')

for _ in range(10):
    print(fake.name())
