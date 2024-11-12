import csv

def read_accidents(filename):
    accidents = {}
    with open(filename, mode ="r", newline= "")as file:
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
        return accidents

def display_accidents_info(accidents_info):
    if accidents_info:
        while True:
            print("\nMenu:")
            print("1.Fatalities ")
            print("2.Injuries ")
            print("3.Crashes ")
            print("4.Fatal Crashes ")
            print("5.Distraction Affected Fatal Crashes ")
            print("6.Fatal Crashes involving Cell Phone Use ")
            print("7.Fatal Crashes involving Excessive Speed ")
            print("8.Fatal Crashes under the Influence ")
            print("9.Fatal Crashes involving Fatigue or Illness")
            print("10.Exit ")
            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"Fatalities: {accidents_info[0]}")
            if choice == "2":
                print(f"Injuries: {accidents_info[1]}")
            if choice == "3":
                print(f"Crashes: {accidents_info[2]}")
            if choice == "4":
                print(f"Fatal crashes: {accidents_info[3]}")
            if choice == "5":
                print(f"Distraction Affected Fatal Crashes: {accidents_info[4]}")
            if choice == "6":
                print(f"Fatal Crashes involving Cell Phone Use: {accidents_info[5]}")
            if choice == "7":
                print(f"Fatal Crashes involving Excessive Speed: {accidents_info[6]}")
            if choice == "8":
                print(f"Fatal Crashes under the Influence: {accidents_info[7]}")
            if choice == "9":
                print(f"Fatal Crashes involving Fatigue or Illness: {accidents_info[8]}")
            if choice == "10":
                break
            
        
def main():
    file_name= "accidents (1).csv"
    accidents = read_accidents(file_name)
    year= input("Insert the year:").strip()
    accidents_info= accidents.get(year)
    display_accidents_info(accidents_info)
    
main()