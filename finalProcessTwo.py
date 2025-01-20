import sys
import csv
import matplotlib.pyplot as plt

def main(argv):
    
    filename  = argv [1]
    job = argv [2]
    regions = ["Newfoundland and Labrador", "Alberta", "British Columbia"," Manitoba", "New Brunswick", "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon", "Nunavut", "NorthWest Territories"]
    vacancies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    processed = {}

    file = open(filename, "r", encoding="utf-8-sig")

    csvReader = csv.reader(file)

    for rows in csvReader:
        if job == rows[1]:
            for i in range(len(regions)):
                if rows[2] == regions[i]:
                    vacancies[i] += int(rows[3])
            
    regions[0] = "Newfoundland \nand Labrador"
    regions[2] = "British \nColumbia"
    regions[4] = "New \nBrunswick"
    regions[5] = "Nova \nScotia"
    regions[7] = "Prince Edward \nIsland"
    regions[12] = "Northwest \nTerritories"

    
    for i in range(len(regions)):
        if vacancies[i] != 0:
            processed[regions[i]] = vacancies[i]
            

    processedVac = list(processed.values())
    processedReg = list(processed.keys())

    plt.bar(processedReg, processedVac, width=0.8)
    plt.xlabel("Provinces", fontweight='bold')
    plt.ylabel("Job Vacancies",fontweight='bold')
    plt.title("Job vacancies in Canada for " + job, fontweight='bold')

    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    for i in range(len(processedReg)):
        plt.text(i, processedVac[i], processedVac[i], ha = 'center')

    plt.show()
    

main(sys.argv)