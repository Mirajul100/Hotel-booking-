import pandas as pd
from booking import Hotel , Reservation

df = pd.read_csv("005 hotels.csv")

print (df)
hotel_ID = input("Enter the hotel id : ")
hotel = Hotel(hotel_id= hotel_ID)
hotel1 = Hotel(hotel_id=hotel_ID)
if hotel.available():
    hotel.booking()
    name = input ("Enter your name : ")
    reservation = Reservation(name , hotel , hotel1)
    ticket = reservation.generate()
    print (ticket)

else :
    print ("Hotel is not free today")