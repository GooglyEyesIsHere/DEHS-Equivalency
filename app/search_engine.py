from main import CourseDatabase

db = CourseDatabase("DE_Equivalency_List_Clean.csv")
db.load_data()
db.preprocess()


def search(query):

    results = db.search(query)
    resultsList = []
    thisResult = []

    if results is None:
        return ""

    for i, e in enumerate(results):
        thisResult.append(e)
        if i % 6 == 5:
            resultsList.append(thisResult)
            thisResult = []

    print("Starting results")
    print(resultsList)
    print("Ending results")

    return resultsList


