import pandas as pd
from fpdf import FPDF
import time

# Read CSV file
df = pd.read_csv("information_file/005 hotels.csv" , dtype= {"id" : str})
# Convert this into dictionary 
card_df = pd.read_csv("information_file/002 cards.csv" , dtype=str).to_dict(orient="records")
card_valid_df = pd.read_csv("information_file/003 card-security.csv" , dtype=str)
date_time = time.strftime("%d-%m-%Y")

class Hotel:
    def __init__(self , hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id , "name"].squeeze()
        self.city_name = df.loc[df["id"] == self.hotel_id , "city"].squeeze()

    def booking(self):
        df.loc[df["id"] == self.hotel_id , "available"] = "no"
        df.to_csv("information_file/005 hotels.csv" , index=False)

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
        
        # Generate the pfl file 
        pdf = FPDF(orientation="p" , unit="mm" , format="A4")
        pdf.add_page()

        pdf.set_font(family="Times" , size=20 , style="B")
        pdf.set_text_color(64 , 45 , 4)
        pdf.cell(w= 0 , h=10 , txt="---Thank you for our hotel reservation---" ,align="C" , ln=1 )

        pdf.set_font(family="Times" , size=14 , style="U")
        pdf.cell(w= 0 , h = 20 , txt= f"Here are your hotel booking data : {date_time}" , align="C" , ln=1)

        pdf.set_font(family="Times" , size=14 , style="")
        pdf.cell(w=50 , h = 8 , txt= f"Name           : {self.customer_name.title()}" , align="L" , ln=1)

        pdf.set_font(family="Times" , size=14 , style="")
        pdf.cell(w=50, h = 8 , txt= f"Hotel Name : {self.hotel.name.title()}" , align="L" , ln=1)
        
        pdf.set_font(family="Times" , size=14 , style="")
        pdf.cell(w=50, h = 8 , txt= f"City Name   : {self.city.city_name}" , align="L" , ln=1)

        pdf.output("pdf/reservation.pdf")
    
class PaymentValid:
    def __init__(self , number):
        self.number = number

    def credit_card_valid(self , expiration , holder , cvc):
        valid_card = {"number": self.number,
                      "expiration":expiration , 
                      "holder":holder,
                      "cvc":cvc}
        if valid_card in card_df:
            return True
        else :
            return False
        
# Inherited the parent class PaymentValid
class CardValid(PaymentValid):
    def authentication(self , given_pass):
        password = card_valid_df.loc[card_valid_df["number"] == self.number , "password"].squeeze()
        if password == given_pass:
            return True
        else :
            return False

class SpaReservation(Reservation):
    def spa_ticket_generate(self , user_input):
        if user_input == "yes":

            pdf = FPDF(orientation="p" , unit="mm" , format="A4")
            pdf.add_page()

            pdf.set_font(family="Times" , size=20 , style="B")
            pdf.set_text_color(64 , 45 , 4)
            pdf.cell(w= 0 , h=10 , txt="---Thank you for our hotel reservation---" ,align="C" , ln=1 )

            pdf.set_font(family="Times" , size=14 , style="U")
            pdf.cell(w= 0 , h = 20 , txt= f"Here are your Spa booking data : {date_time}" , align="C" , ln=1)

            pdf.set_font(family="Times" , size=14 , style="")
            pdf.cell(w=50 , h = 8 , txt= f"Name           : {self.customer_name.title()}" , align="L" , ln=1)

            pdf.set_font(family="Times" , size=14 , style="")
            pdf.cell(w=50, h = 8 , txt= f"Hotel Name : {self.hotel.name.title()}" , align="L" , ln=1)
            
            pdf.set_font(family="Times" , size=14 , style="")
            pdf.cell(w=50, h = 8 , txt= f"City Name   : {self.city.city_name}" , align="L" , ln=1)

            pdf.set_font(family="Times" , size=14 , style="")
            pdf.cell(w=50 , h= 8 , txt="Thank you for spa reservation" , align="L" ,ln=1)

            pdf.output("pdf/spa_reservation.pdf")
        else :
            print ("Thank You for visiting us")
        