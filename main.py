from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

ride_share = RideSharing('World Rider')
print(ride_share)

jisan = Rider("Jisan Ahmed", "jisan@gmail.com", 2049, "Mirpur 10", 1820)
ride_share.add_rider(jisan)

rifat = Driver("Rifat Khan", "rifat@gmail.com", 22200, "Gulshan")
ride_share.add_drivers(rifat)

jisan.request_ride(ride_share, 'Uttara', 'car')
jisan.show_current_ride()

rifat.reach_destination(jisan.current_ride)


print(ride_share)