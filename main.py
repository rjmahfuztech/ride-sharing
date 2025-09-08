from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

ride_share = RideSharing('World Rider')
print(ride_share)

jisan = Rider("Jisan Ahmed", "jisan@gmail.com", 2049, "Mirpur 10", 1820)
ride_share.add_rider(jisan)

rifat = Driver("Rifat Khan", "rifat@gmail.com", 22200, "Gulshan")
ride_share.add_drivers(rifat)


print(ride_share)