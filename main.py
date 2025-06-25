import pandas as pd
from booking import Hotel , Reservation , PaymentValid

df = pd.read_csv("005 hotels.csv")

print (df)
hotel_ID = input("Enter the hotel id : ")
hotel = Hotel(hotel_id= hotel_ID)
hotel1 = Hotel(hotel_id=hotel_ID)
if hotel.available():
    number = input("Enter your credit card number : ")
    payment_valid = PaymentValid(number)
    if payment_valid.credit_card_valid(expiration="12/26" , holder="JOHN SMITH" , cvc="123"):
        hotel.booking()
        name = input ("Enter your name : ")
        reservation = Reservation(name , hotel , hotel1)
        ticket = reservation.generate()
        print (ticket)
    else :
        print ("There was problem in your payment!")

else :
    print ("Hotel is not free today")