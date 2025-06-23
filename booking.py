import pandas as pd

df = pd.read_csv("005 hotels.csv" , dtype= {"id" : str})

class Hotel:
    def __init__(self , hotel_id):
        self.hotel_id = hotel_id

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
    def __init__(self , customer_name , hotel_name):
        pass

    def generate(self):
        pass
