import pandas


def main():
    database = pandas.read_csv("DE_Equivalency_List_Clean.csv")
    database.fillna("No Core Subject", inplace=True)
    database_read = []
    LETTER_CONV = {"A1": "Algebra 1 (or course equivalent)", "AG": "United States (American) Government (or course equivalent)", "AH": "United States (American) History (or course equivalent)", "BI": "Biology (or course equivalent)", "CT": "Career and Technical Education course (includes courses previously coded as PA = Practical Arts)", "DD": "District-Determined (must be converted to BI or EQ on individual student basis on official records)", "EC": "Economics (or course equivalent)", "EL": "Elective (includes world language courses)", "EN": "English/Language Arts", "EQ": "Equally Rigorous (to Chemistry and/or Physics) Science ", "FE": "Personal Financial Literacy and Economics (or course equivalent)", "GE": "Geometry (or course equivalent)", "MA": "Mathematics", "PE": "Physical Education (only applies to Personal Fitness, not Physical Activity requirement, for dual enrollment purposes)", "PF": "Visual and Performing Fine Arts", "PL": "Personal Financial Literacy (or course equivalent)", "WH": "World History (or course equivalent)"}
    print("File Read:")

    """ A1 = Algebra 1 (or course equivalent)
 AG = United States (American) Government (or course equivalent)
 AH = United States (American) History (or course equivalent)
 BI = Biology (or course equivalent)
 CT = Career and Technical Education course (includes courses previously coded as PA = Practical Arts)
 DD = District-Determined (must be converted to BI or EQ on individual student basis on official records)
 EC = Economics (or course equivalent)
 EL = Elective (includes world language courses)
 EN = English/Language Arts
 EQ = Equally Rigorous (to Chemistry and/or Physics) Science 
 FE = Personal Financial Literacy and Economics (or course equivalent)
 GE = Geometry (or course equivalent)
 MA = Mathematics
 PE = Physical Education (only applies to Personal Fitness, not Physical Activity requirement, for dual enrollment purposes)
 PF = Visual and Performing Fine Arts
 PL = Personal Financial Literacy (or course equivalent)
 WH = World History (or course equivalent)
"""
    for i, e in database.iterrows():
        if e.tolist()[0] == "Prefix Abbreviation":
            break
        database_read.append(e.tolist())
        try:
            database_read[len(database_read)-1][4] = LETTER_CONV[database_read[len(database_read)-1][4]]
        except KeyError:
            pass
    hybrid = False
    searchFor = input("What course do you want? Search course number (2101) or course name (ENC)\n").upper().strip()
    if " " in searchFor:
        hybrid = True
        searchForSplit = searchFor.split()
        searchForNum = "X" + searchForSplit[1][1:]
        searchFor = searchForSplit[0]

    else:
        searchForNum = "X" + searchFor[1:]
    found = False
    for i, e in enumerate(database_read):
        if hybrid:
            if searchForNum in e[1] and searchFor in e[0]:
                found = True
                print(e)
        else:
            if searchForNum in e[1] or searchFor in e[0]:
                found = True
                print(e)
    if not found:
        print("No courses found matching your search.")


if __name__ == "__main__":
    main()
