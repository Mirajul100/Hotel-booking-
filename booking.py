import pandas as pd

df = pd.read_csv("005 hotels.csv" , dtype= {"id" : str})

class Hotel:
    def __init__(self , hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id , "name"].squeeze()
        self.city_name = df.loc[df["id"] == self.hotel_id , "city"].squeeze()

    def booking(self):
        df.loc[df["id"] == self.hotel_id , "available"] = "no"
        df.to_csv("005 hotels.csv" , index=False)

    def available(self):
        find = df.loc[df["id"] == self.hotel_id , "available"].squeeze()
        if find == "yes":
            return True
        else :
            return False


class Reservation:
    def __init__(self , customer_name , hotel_name , city):
        self.customer_name = customer_name
        self.hotel = hotel_name
        self.city = city

    def generate(self):
        contend = f"""Thank you for your hotel reservation
        Here are your hotel booking data : 
        Name : {self.customer_name.title()}
        Hotel Name : {self.hotel.name} 
        City Name : {self.city.city_name}
        """
        return contend