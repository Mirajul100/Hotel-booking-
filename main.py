import pandas as pd
from booking import Hotel , SpaReservation , CardValid , Reservation

df = pd.read_csv("information_file/005 hotels.csv")

print (df)
try :
    hotel_ID = input("Enter the hotel id : ")
    hotel = Hotel(hotel_id= hotel_ID)
    hotel1 = Hotel(hotel_id=hotel_ID)
    if hotel.available():
        name = input ("Enter your name : ")
        number = input("Enter your credit card number : ")
        cvc = input ("Enter the credit card cvc number : ")
        payment_valid = CardValid(number)
        if payment_valid.credit_card_valid(expiration="12/26" , holder=name.title().upper() , cvc=cvc):
            given_pass = input ("Enter the chard password : ")
            if payment_valid.authentication(given_pass=given_pass):
                hotel.booking()
                reservation = Reservation(name , hotel , hotel1)
                ticket = reservation.generate()
                print("Successfully booking hotel")
                spa = input ("Do you want to book spa package? : ")
                spa_reservation = SpaReservation(customer_name=name , hotel_name=hotel , city=hotel)
                spa_reservation.spa_ticket_generate(user_input=spa.lower())
            else:
                print ("The card is not authentication")
        else :
            print ("There was problem in your payment!")
    else :
        print ("Hotel is not free today")
except(ValueError):
    print ("Please enter the right hotel id")