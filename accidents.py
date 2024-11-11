import csv

def read_accidents(filename):
    accidents = {}
    with open(filename, mode ="r", newline= " ")as file:
        reader = csv.reader(file)
        for row in reader:
            year = row[0]
            fatalities = row[1]
            Injuries = row[2]
            crashes = row[3]
            fatal_crashes = row[4]
            dafc = row[5]
            fcicpu = row[6]
            fcies = row[7]
            fcwduti = row[8]
            fcifoi = row[9]
            accidents[year] = [fatalities, Injuries, crashes, fatal_crashes, dafc, fcicpu, fcies, fcwduti, fcifoi]
            next (reader)
        return accidents

def display_accidents_info(accidents_info):
    if accidents_info:
        print("Accidents information:")
        print(f"Fatalities: {accidents_info[0]}")
        print(f"Injuries: {accidents_info[1]}")
        print(f"Crashes: {accidents_info[2]}")
        print(f"Fatal crashes: {accidents_info[3]}")
        print(f"Distraction Affected Fatal Crashes: {accidents_info[4]}")
        print(f"Fatal Crashes involving Cell Phone Use: {accidents_info[5]}")
        print(f"Fatal Crashes involving Excessive Speed: {accidents_info[6]}")
        print(f"Fatal Crashes under the Influence: {accidents_info[7]}")
        print(f"Fatal Crashes involving Fatigue or Illness: {accidents_info[8]}")
    else:
        print("No data found")
        
def main():
    file_name= "accidents(1).csv"
    accidents = read_accidents(file_name)
    year= input("Insert the year:").strip()
    accidents_info= accidents.get(year)
    display_accidents_info(accidents_info)
    
main()