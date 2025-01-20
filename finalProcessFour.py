import sys
import csv
import matplotlib.pyplot as plt

def main(argv):
    
    filename  = argv [1]
    job = argv [2]
    year = argv [3]
    

    education = ["No minimum level of education required", "High school diploma or equivalent", "Non-university certificate or diploma", "University certificate or diploma below bachelor's level", "Bachelor's degree", "University certificate, diploma or degree above the bachelor's level", "College, CEGEP and other non-university certificate or diploma"]
    experience = ["Less than 1 year", "1 year to less than 3 years", "3 years to less than 5 years", "5 years to less than 8 years", "8 years or more"]



    vacanciesEdu = [0,0,0,0,0,0,0]
    vacanciesExp = [0,0,0,0,0]
    processedEdu = {}
    processedExp = {}

    file = open(filename, "r", encoding="utf-8-sig")

    csvReader = csv.reader(file)

    for rows in csvReader:
        if job == rows[1] and year == rows[0][:4]:
            for i in range (len(education)):
                if rows[2] == education[i]:
                    vacanciesEdu[i] += int(rows[3])
            for i in range (len(experience)):
                if rows[2] == experience[i]:
                    vacanciesExp[i] += int(rows[3])


    education[0] = "No minimum level \nof education \nrequired"
    education[1] = "High school diploma\n or equivalent"
    education[2] = "Non-university\n certificate or \ndiploma"
    education[3] = "University certificate\n or diploma below bachelor's \nlevel"
    education[5] = "University certificate,\n diploma or degree above\n the bachelor's level"
    education[6] =  "College, CEGEP and other \nnon-university certificate\n or diploma"
            
            
            
    
    for i in range(len(education)):
        if vacanciesEdu[i] != 0:
            processedEdu[education[i]] = vacanciesEdu[i]

    for i in range(len(experience)):
        if vacanciesExp[i] != 0:
            processedExp[experience[i]] = vacanciesExp[i]
            



    fig, axs = plt.subplots(2)

    processedVac = list(processedEdu.values())
    processedEdu = list(processedEdu.keys())


    axs[0].bar(processedEdu, processedVac, width=0.8)
    axs[0].set_xlabel("Education Level", fontweight='bold')
    axs[0].set_xticklabels(processedEdu, rotation=25)
    axs[0].set_ylabel("Job Vacancies",fontweight='bold')
    axs[0].set_title("Job vacancies in Canada for " + job + " in " + year, fontweight='bold')
    

    for i in range(len(processedEdu)):
        axs[0].text(i, processedVac[i], processedVac[i], ha = 'center')


    processedVac = list(processedExp.values())
    processedExp = list(processedExp.keys())

    axs[1].bar(processedExp, processedVac)
    axs[1].set_xlabel("Experience Level", fontweight='bold')
    axs[1].set_ylabel("Job Vacancies",fontweight='bold')
    axs[1].set_title("Job vacancies in Canada for " + job + " in " + year, fontweight='bold')

    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    for i in range(len(processedVac)):
        axs[1].text(i, processedVac[i], processedVac[i], ha = 'center')

    
    fig.tight_layout(pad=5.0)
    plt.show()
    

main(sys.argv)