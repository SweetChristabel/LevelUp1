# Write your solution here
def get_station_data(filename: str):
    stationdata = {}
    with open(filename) as rawdata:
        for line in rawdata:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            else: stationdata[parts[3]] = (float(parts[0]),float(parts[1]))
    return stationdata

def distance(stations:dict, station1:str, station2: str):
    import math
    x_km = (stations[station1][0]-stations[station2][0]) * 55.26
    y_km = (stations[station1][1]-stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    winnerdistance = 0
    for station1 in stations:
        for station2 in stations:
            dsnc = distance(stations, station1, station2)
            if dsnc > winnerdistance:
                winnerdistance = dsnc
                winner = (station1, station2, dsnc)
    return winner

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)