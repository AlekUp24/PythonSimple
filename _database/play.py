import pandas as pd
import os


class Car:
    def __init__(self, brand, model, year, body_type, color_options, fuel, horsepower, torque, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.body_type = body_type
        self.color_options = color_options
        self.fuel = fuel
        self.horsepower = horsepower    
        self.torque = torque
        self.price = price

    
    def __str__(self):
        return f"{self.brand} {self.model} from {self.year} has {self.body_type} body type and comes in {self.color_options}. Fuel option is {self.fuel}. Price: $ {self.price}."

    def can_afford(self, budget):
        if budget >= self.price:
            return True
        else:
            return False


db_path = os.path.join(os.getcwd(),'_database\\2023_Car_Dataset.csv')
objects = []

# user vars
budget = 25000
considered_brands = ['Toyota','Ford','Tesla','Audi','Kia']

# create and prepare dataframe
db_data_simple = pd.read_csv(db_path)
df = pd.DataFrame(db_data_simple)

# rename headers and trim values
df.rename(columns=lambda x: x.replace(" ", "").strip(), inplace=True)
df.rename(columns=lambda x: x.replace("($)","").strip(), inplace=True)
df = df.applymap(lambda x: x.strip() if type(x)==str else x)

# filter only named brands
user_choices = df.loc[df['CarMake'].isin(considered_brands)]

# create objects for each and check if can afford
for index,row in user_choices.iterrows():
    objects.append(Car(row['CarMake'], row['CarModel'], row['Year'], row['BodyType'], row['ColorOptions'], row['FuelType'], row['Horsepower'], row['Torque(Nm)'], int(row['Price'].replace(",",""))))

for each in objects:
    if each.can_afford(budget):
        print(each)
      
