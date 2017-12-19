import csv
import pyproj

cr = csv.reader(open("X_geoloc_egc_t2.csv", "rb"), delimiter=";")

inProj = pyproj.Proj("+init=EPSG:3945")
outProj = pyproj.Proj("+init=EPSG:4326")

for row in cr:
	if row[0] != "coord_x":
		x2,y2 =  pyproj.transform(inProj, outProj, float(row[0]), float(row[1]))
	    	print(x2,y2)
        
