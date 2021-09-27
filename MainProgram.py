print()

#importing module
import ImportModule

#re-assigning variables from module program
phone_towing = ImportModule.Towing_Company
phone_laundry = ImportModule.Laundry_Company
phone_computer = ImportModule.Computer_Company
phone_hardware = ImportModule.Hardware_Company
phone_plumber = ImportModule.Plumber_Company

#creating search database with user input
print()
print("Select one of the following to continue:", towing , laundry, computer , hardware , plumber)

#user types for hte service they desire
searcheng = input("Search:")

#checks if the user input matches the databases options
#this is not the most efficient way too do this but its the easiest
if searcheng == towing:
    print(phone_towing)

if searcheng == laundry:
    print(phone_laundry)

if searcheng == computer:
    print(phone_computer)

if searcheng == hardware:
    print(phone_hardware)

if searcheng == plumber:
    print(phone_plumber)

if searcheng == ("else"):
    print("this item is not available in our database")
