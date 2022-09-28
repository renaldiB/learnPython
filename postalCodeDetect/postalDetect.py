from geopy.geocoders import Nominatim

geoLoc = Nominatim(user_agent='geoapiExercises')

inp = input("Enter Postal Code: ")
postalCode = inp

location = geoLoc.geocode(postalCode)
print("Location:")
print(location)