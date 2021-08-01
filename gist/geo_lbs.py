import math
import numpy as np
import pygeohash as pgh

print(pgh.encode(42.6, -5.6))
# >>> 'ezs42e44yx96'

print(pgh.encode(42.6, -5.6, precision=5))
# >>> 'ezs42'

print(pgh.decode('ezs42'))
# >>> ('42.6', '-5.6')

print(pgh.geohash_approximate_distance('bcd3u', 'bc83n'))


def latlong_to_coord(lat, long):
    lat = np.deg2rad(lat)
    long = np.deg2rad(long)
    return np.array([np.cos(lat) * np.cos(long), np.cos(lat) * np.sin(long), np.sin(lat)])


def point_angle(point1, point2):
    return math.acos(np.dot(point1, point2))


lat1, long1, lat2, long2 = 28.32465, 160.7193, 31.32465, 120.71
radius = 6356725

pot1 = latlong_to_coord(lat1, long1)
pot2 = latlong_to_coord(lat2, long2)

distance = radius * point_angle(pot1, pot2)
print(distance)
