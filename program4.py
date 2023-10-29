class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passengers(self, name):
     if not self.open_seats():
         return False
     self.passengers.append(name)
     return True
    def open_seats(self): 
        return self.capacity - len(self.passengers)    
flight = Flight(3)
group = ["rim", "tim", "dim", "rom" ]
for person in group: 
   if flight.add_passengers(group): 
      print(f"Added {person} to flight successfully")
else:
   print(f"no avaliable seats for {person}")
       