import math

def calculate_polies(startLat, startLong, finalLat, finalLong):
  points = []
  Lat = startLat
  Long = startLong
  num_of_lat = math.ceil(abs(finalLat-startLat))
  num_of_long = math.ceil(abs(finalLong-startLong))
  for i in range(num_of_lat):
    for j in range(num_of_long):
      points.append([(Lat+i, Long+j),(Lat+i+1, Long+1+j)])
  return points
  
