from faker import Faker
import pandas as pd 
fake = Faker()


def create_rows_faker(num):
    output = [{
        "first_name":fake.first_name(),
        "last_name":fake.last_name(),
        "address":fake.address().replace('\n', ', '),
        "date_of_birth": fake.date_of_birth().isoformat()
                   } for x in range(num)]
    return output

def main():
    df_fake = pd.DataFrame(create_rows_faker(500000))
    df_fake.to_csv('input_data_faker.csv')

