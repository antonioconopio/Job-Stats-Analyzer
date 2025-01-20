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
import matplotlib.pyplot as plt


def main(argv):

    total_months = 0
    total_vacancies = 0
    total_years = 0

    vacancies = [""]
    months = [""]

    if len(argv) < 2:
        print("Usage: python process.py <filename>", file=sys.stderr)
        sys.exit(1)

    # Setting arguments to variables
    file_name = argv[1]

    # Opening the file
    try:
        file = open(file_name, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                file, err), file=sys.stderr)
        sys.exit(1)

        
    csvreader = csv.reader(file)
    headers = next(csvreader)

    file.seek(0)

    ##printing a menu that displays all occupation categories for the user to choose from 
    for rows in csvreader:
        if (rows[1] != "OCCUPATION"):
            print(rows[1])
    occupation = input("Enter an ocupation from the menu above: ")

    ## setting the file pointer to the beginning after reading it once for the menu 
    file.seek(0)

    for rows in csvreader:
        if rows[1] == occupation: 
            if rows[2] != "" and rows[2] != "0":
                total_vacancies += int(rows[2])
                total_months += 1
            elif rows[2] == "" or rows[2] == "0":
                total_months += 1


    ## this block of code calculates the average rate of change in job vacancies per year of a selected occupation by the user 
    total_years = total_months/12
    average_rate_of_change = total_vacancies / total_years
    rounded_average = round(average_rate_of_change,2)

    print("The average rate of change is: ",rounded_average, "vacancies per  year")

    file.seek(0)

    i = 0

    # x-axis list 
    for rows in csvreader: 
        if rows[1] == occupation: 
            vacancies[i] = rows[2]

    # y-axis list 
    for i in range(1, int(total_months) + 1):  # Correct iteration over total_months
        months.append(i)
 

    vacancies = list(map(int, vacancies))

    # Plotting the line graph
    plt.plot(months[1:], vacancies[1:], marker='o', linestyle='-')
    plt.xlabel('Months')
    plt.ylabel('Vacancies')
    plt.title('Average rate of change for job vacancies for' + occupation)
    plt.grid(True)
    plt.show()


main(sys.argv)