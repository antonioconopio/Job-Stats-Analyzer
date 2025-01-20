'''
process.py
Author(s): Antonio Conopio (1262963), Haris Anees (1267012), Huraimah Fatima (1305776)
Project: Milestone III Pre Processing
Date of Last Update: Thurs March 20, 2024

functional Summary
Pre processes data for our four questions. Breaks down the data into smaller files for easier 
final evaluations.

Commandline Parameters: 1
argv[1] = File to read

'''


import sys
import csv


def main(argv):

    if len(argv) < 2:
        print("Usage: python process.py <filename>", file=sys.stderr)
        sys.exit(1)

    # Setting arguments to variables
    filename = argv[1]

    # Opening the file
    try:
        file = open(filename, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                file, err), file=sys.stderr)
        sys.exit(1)

    # Creating a csv reader and a list of the headers
    csvreader = csv.reader(file)
    headers = next(csvreader)

    
    choice = 0
    file.seek(0)

    while(choice != 5):

        print("\n1. Question One")
        print("2. Question Two")
        print("3. Question Three")
        print("4. Question Four")
        print("5. Exit")
        choice = int(input("Please select a question: "))
        print("\n")

        match choice:
            case 1:
                chosenOccupation = input("Enter an occupation: ")
                questionOne (csvreader, file, chosenOccupation)
            case 2:
                year = int(input("Enter a year: "))
                questionTwo (csvreader, file, year)
            case 3:
                # occupation = input("Enter an occupation: ")
                start_year = int(input("Start Year: "))
                end_year = int(input("End Year: "))
                questionThree (csvreader, file, start_year, end_year)
            case 4:
                questionFour (csvreader, file)
        
    

def questionOne (csvreader, file, chosenOccupation):

    outFile = open('question1.csv', 'w', newline='')
    csvwriter = csv.writer(outFile)

    fields = ["Date", "OCCUPATION", "JOB VACANCY CHARACTERISTICS", "JOB VACANCIES"]
    jobCharacteristics = ["No minimum level of education required", "High school diploma or equivalent", "Non-university certificate or diploma", "University certificate or diploma below bachelor's level", "Bachelor's degree", "University certificate, diploma or degree above the bachelor's level"]

    csvwriter.writerow(fields)

    file.seek(0)

    for rows in csvreader:
        if rows[5] == "Job vacancies" and rows[0][0:4] == "2023":
            for degree in jobCharacteristics:
                if rows[4] == degree and rows[3] == chosenOccupation:
                    if rows[12] != "" and rows[12] != "0":
                        outRow = [rows[0],rows[3], rows[4], rows[12]]
                        csvwriter.writerow(outRow)
                    elif rows[12] == "" or rows[12] == "0":
                        outRow = [rows[0],rows[3], rows[4], "0"]
                        csvwriter.writerow(outRow)

    print("\nFile created!\n")

    outFile.close()
    

def questionTwo (csvreader, file, year):
    
    outFile = open('question2.csv', 'w', newline='')
    csvwriter = csv.writer(outFile)

    fields = ["Date", "OCCUPATION", "GEO", "JOB VACANCIES"]
    geo = ["Canada", "Alberta", "British Columbia"," Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon", "Nunavut", "NorthWest Territories"]

    csvwriter.writerow(fields)

    file.seek(0)

    for rows in csvreader:
        if rows[5] == "Job vacancies" and int(rows[0][0:4]) == year and rows[4] == "Type of work, all types":
            for prov in geo:
                if rows[1] == prov:
                    if rows[12] != "" and rows[12] != "0":
                        outRow = [rows[0],rows[3], rows[1], rows[12]]
                        csvwriter.writerow(outRow)
                    elif rows[12] == "" or rows[12] == "0":
                        outRow = [rows[0],rows[3], rows[1], "0"]
                        csvwriter.writerow(outRow)


    outFile.close()
    print("\nDONE!\n")



def questionThree (csvreader, file, start_year, end_year):

    total_vacancies = 0  
    total_months = 0 
    
    outFile = open('question3.csv', 'w', newline='')
    csvwriter = csv.writer(outFile)

    fields = ["DATE", "OCCUPATION", "JOB VACANCIES"]
    csvwriter.writerow(fields)

    file.seek(0)  # Resetting file pointer
    next(csvreader)

    for rows in csvreader:
        date = rows[0].split('-')[0]
        if start_year <= int(date) <= end_year and rows[4] == "Type of work, all types" and rows[5] == "Job vacancies":
            outRow = [rows[0], rows[3], rows[12] if rows[12] else "0"]
            csvwriter.writerow(outRow)

    print("\nFile created for Question Three!\n")
    outFile.close()

    try:
        file = open(outFile, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open names file '{}' : {}".format(file, err), file=sys.stderr)
        sys.exit(1)
        
    outFile_reader = csv.reader(outFile)
    headers = next(csvreader)

    for rows in outFile_reader:
        if rows[1] == occupation: 
            if rows[12] != "" and rows[12] != "0":
                total_vacancies += int(row[2])
                total_months += 1
            elif rows[12] == "" or rows[12] == "0":
                total_months += 1

    outFile.close()

    total_months = total_months/12

    # calculating the average 
    average_rate_of_change = total_vacancies / total_months

    print("The average rate of change is %d", average_rate_of_change)

def questionFour (csvreader, file):
    outFile = open('question4.csv', 'w', newline='')
    csvwriter = csv.writer(outFile)

    fields = ["DATE", "OCCUPATION", "CHARACTERISTICS", "JOB VACANCIES"]
    characterisitcs = ["No minimum level of education required", "High school diploma or equivalent", "Non-university certificate or diploma", "University certificate or diploma below bachelor's level", "Bachelor's degree", "University certificate, diploma or degree above the bachelor's level", "College, CEGEP and other non-university certificate or diploma", "Less than 1 year", "1 year to less than 3 years", "3 years to less than 5 years", "5 years to less than 8 years", "8 years or more"]


    csvwriter.writerow(fields)

    file.seek(0)

    for rows in csvreader:
        if rows[5] == "Job vacancies" and rows[1] == "Canada":
            for characteristic in characterisitcs:
                if rows[4] == characteristic:
                    if rows[12] != "" and rows[12] != "0":
                        outRow = [rows[0],rows[3], rows[4], rows[12]]
                        csvwriter.writerow(outRow)
                    elif rows[12] == "" or rows[12] == "0":
                        outRow = [rows[0],rows[3], rows[4], "0"]
                        csvwriter.writerow(outRow)

    print("\nDONE!\n")
    


main(sys.argv)