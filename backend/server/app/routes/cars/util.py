import math

def calculate_polies(startLat, startLong, finalLat, finalLong):
  points = []
  Lat = startLat
  Long = startLong
  numberOfSegments = math.ceil(max(abs(finalLat-startLat), abs(finalLong-startLong)))
  for _ in range(numberOfSegments):
    for j in range(numberOfSegments):
      points.append([[Lat, Long+j],[Lat+1, Long+1+j]])
    Lat += 1
  print(points)
  return points
  
