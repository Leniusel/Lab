#Name: Doris Tran
#Date: Sept 7, 2022
#M03 Lab Case Study: Lists, Functions, and Classes 
#A program that stores and print vehicle information

#class that stores the type of vehicle
class Vehicle:
  def _init_(self, type):
    self.type = type
    
#class that inherit from the Vehicle class. Also store automobile attributes
class Automobile(Vehicle):
  def _init_self(self, year, make, model, doors, roof):
    self.year = year
    self.make = make
    self.model = model
    self.doors = doors
    self.roof = roof
    super().__init__(type)  

#function to get the year. Automobiles where available as early as 1885
def get_year():
    try:
        yr = int(input("Enter the year: "))
        assert 9999 >= yr >= 1885
        return yr;
    except:
        print("Please enter a valid year.")
        return get_year();
      
#function to get 2 or 4 doors
def get_doors():
    try:
        print("\n[1] 2 doors\n[2] 4 doors")
        door = int(input("\nEnter option for the number of doors in your " + a.type + ": "))
        assert (door == 1 or door == 2)
        if(door == 1):
          return "2 doors"
        else:
          return "4 doors";
        return door;
    except:
        print("Please enter a valid option.")
        return get_doors();

#function to get roof options
def get_roof():
    try:
        print("\n[1] solid\n[2] sun roof")
        roof = int(input("\nEnter option for roof type: "))
        assert (roof == 1 or roof == 2)
        if(roof == 1):
          return "solid"
        else:
          return "sun roof";
    except:
        print("Please enter a valid option.")
        return get_doors();

#make an Automobile object
a = Automobile()

#allow user to input automobile information
a.type = input("Enter your vehicle: ").lower()
a.year = get_year()
a.make = input("Enter the manufacturer: ").capitalize()
a.model = input("Enter the model: ").capitalize()
a.doors = get_doors()
a.roof = get_roof()


#prints the information
print("\nVehicle Type:", a.type, "\nYear:", a.year, "\nMake:", a.make, "\nModel:", a.model, "\nNumber of Doors:", a.doors, "\nType of roof:", a.roof)
