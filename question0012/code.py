
#Trip cost calculator

print(f'Hello customer! Welcome to your cost calculator.')
noOfDays = input("How many days will you stay? : ")
hotelCostPerNight = input("How much does the hotel cost per night? ")
flightCost = input("How much does your flight cost? ")
rentalCar = input("If you need a rental car, please enter the price else press zero, ")

editedNoOfDays = int(noOfDays[1:])
editedHotelCostPerNight = float(hotelCostPerNight[1:])
editedFlightCost = float(flightCost[1:])

if len(rentalCar) == 1:
    editedRentalCar = 0
else:
    editedRentalCar = float(rentalCar[1:])

totalCostOfTrip = ((editedNoOfDays * editedHotelCostPerNight) + editedFlightCost + editedRentalCar)
print(f'Your total cose is, ${format(totalCostOfTrip,".2f")}')
