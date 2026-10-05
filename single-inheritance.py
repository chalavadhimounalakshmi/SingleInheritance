print("---------Hospital Details---------------")
# Single inheritance without Constructor.
class Hospital:
    def hospital_name(self):
        print("Hospital: Apollo Hospital")
class Doctor(Hospital):
    def specialization(self):
        print("Specialization: Cardiology")
d = Doctor()
d.hospital_name()
d.specialization()
# ---------------------------------------------------------------
print("-----------BOOK DETAILS---------------------")
# Single inheritance with constructor.
class Book:
    def __init__(self,title):
        self.title=title
    def display_title(self):
        print("Book Title =",self.title)
class Novel(Book):
    def __init__(self,title,author):
        Book.__init__(self,title)
        self.author = author
    def display_author(self):
        print("Author =",self.author)
n=Novel("secretary ","Yaddanapudi Sulochana Rani")
n.display_title()
n.display_author()
# ---------------------------------------------------------------------
print("---------Movie Details------------")
# single inheritance with constructor + super() class.
class Movie:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print("Movie Name =",self.name)
class TeluguMovie(Movie):
    def __init__(self,name,director):
        super().__init__(name)
        self.director=director
    def display_director(self):
        print("Director =",self.director)
m=TeluguMovie("Bahubali ","s.s Rajamouli")
m.display_name()
m.display_director()
# ----------------------------------------------------------
print("----------Flight Details-------------")
# single inheritance with constructor + super().Real world Example.
class Flight:
    def __init__(self,flight_number):
        self.flight_number = flight_number
    def display_flight(self):
        print("Flight Number:",self.flight_number)
class DomesticFlight(Flight):
    def __init__(self,flight_number,destination):
        super().__init__(flight_number)
        self.destination = destination
    def display_destination(self):
        print("Destination = ",self.destination)
f = DomesticFlight("AI202","Hyderabad")
f.display_flight()
f.display_destination()