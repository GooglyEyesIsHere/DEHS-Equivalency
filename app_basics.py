from main import CourseDatabase

db = CourseDatabase("DE_Equivalency_List_25_26.csv")
db.load_data()
db.preprocess()


def search(query):
    return db.search(query)