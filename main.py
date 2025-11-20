import pandas as pd
import rapidfuzz


class CourseDatabase:
    """
    Handles loading, cleaning, and searching of the DE Equivalency CSV.
    """

    def __init__(self, csv_path: str):
        """Initialize the database object."""
        self.csv_path = csv_path
        self.database = None
        self.database_read = []
        self.LETTER_CONV = {
            "A1": "Algebra 1 (or course equivalent)",
            "AG": "United States (American) Government (or course equivalent)",
            "AH": "United States (American) History (or course equivalent)",
            "BI": "Biology (or course equivalent)",
            "CT": "Career and Technical Education course (includes courses previously coded as PA = Practical Arts)",
            "DD": "District-Determined (must be converted to BI or EQ on individual student basis on official records)",
            "EC": "Economics (or course equivalent)",
            "EL": "Elective (includes world language courses)",
            "EN": "English/Language Arts",
            "EQ": "Equally Rigorous (to Chemistry and/or Physics) Science",
            "FE": "Personal Financial Literacy and Economics (or course equivalent)",
            "GE": "Geometry (or course equivalent)",
            "MA": "Mathematics",
            "PE": "Physical Education (only applies to Personal Fitness, not Physical Activity requirement, for dual enrollment purposes)",
            "PF": "Visual and Performing Fine Arts",
            "PL": "Personal Financial Literacy (or course equivalent)",
            "WH": "World History (or course equivalent)"
        }

    # ──────────────────────────────────────────────────────────────
    # Data Loading and Processing
    # ──────────────────────────────────────────────────────────────
    def load_data(self):
        """Read the CSV file into a pandas DataFrame."""
        self.database = pd.read_csv(self.csv_path)
        self.database.fillna("No Core Subject", inplace=True)
        print("File Read: [Warning: not all course numbers begin with X; some start with 0. These have been overridden to X.]")

    def preprocess(self):
        """Convert raw rows into standardized form for searching."""
        for i, row in self.database.iterrows():
            if row.tolist()[0] == "Prefix Abbreviation":
                break

            row_data = row.tolist()

            # Force prefix of course number to start with X
            row_data[1] = "X" + row_data[1][1:]

            # Translate abbreviation (if applicable)
            abbreviation = row_data[4]
            if abbreviation in self.LETTER_CONV:
                row_data[4] = self.LETTER_CONV[abbreviation]

            self.database_read.append(row_data)

    # ──────────────────────────────────────────────────────────────
    # Searching
    # ──────────────────────────────────────────────────────────────

    def clean_search_query(self, query: str, q_type: str):

        query_mid = query.upper().split(";")
        query_final = []
        for i, e in enumerate(query_mid):
            query_mid[i] = e.strip()
        for search in query_mid:

            # print(search)
            if q_type == "1":  # Course Prefix
                search = search.upper()
            elif q_type == "2":  # Course Number
                if len(query) > 2:
                    search = "X" + search[1:]
                else:
                    search = "Invalid course number"
            elif q_type == "3" and len(query) > 4:  # Course Name
                search = search.title()
            elif q_type == "4":  # Credit Value
                search = search
            elif q_type == "5":  # High school Graduation Code
                search = search.title()
                if search in self.LETTER_CONV:
                    search = self.LETTER_CONV[search]
            elif q_type == "6":  # GE Core Subject
                search = search.title()
            query_final.append(search)


       # print(query_mid)

        #print(query_mid)
        return query_final

        pass

    @staticmethod
    def clean_types_input(types: list):

        clean_types = types
        invalid_char = False
        outside_range_pos = False
        outside_range_neg = False
        no_types_given = len(types) == 0
        duplicates_given = False
        for e, i in enumerate(clean_types):
            if i.isdigit():
                if int(i) <= 0:
                    outside_range_neg = True
                    clean_types.pop(e)
                if int(i) > 6:
                    outside_range_pos = True
                    clean_types.pop(e)
                if types.count(i) > 1:
                    duplicates_given = True
                    clean_types.pop(e)

            else:
                invalid_char = True
                clean_types.pop(e)
        print(invalid_char, outside_range_pos, outside_range_neg, no_types_given, duplicates_given, clean_types)

        return clean_types


    def give_types_examples(self, types: list):
        examples = {"1": "ENC", "2": "1234", "3": "Not Implemented Yet", "4": "1.5", "5": "PE", "6": "Humanities"}
        if "5" in types:
            print("Reminder: ")
            for i, e in (self.LETTER_CONV.items()):
                print(f"{i} = {e}")
        print("Give your input in the form: ")
        for i in types:
            if i in examples:
                print(examples[i], end=" ")
        print()

    @staticmethod
    def find_courses_types(types: list):
        return_types = []
        for i in types:
            if i == "1" or i == "2" or i == "4" or i == "5":
                return_types.append("single")
            elif i == "3" or i == "6":
                return_types.append("multi")
        return return_types

    def search(self, query: str):
        """
        Search for a course by prefix, number, or both (hybrid search).
        """
        print("Started search, searching ", query)

        #  clean_types = self.clean_types_input(types)
        #  types_to_expect = self.find_courses_types(types)
        query = query.title().strip()
        hybrid = False  # " " in query
        #  query = self.clean_search_query(query, types[0])
        clean_queries = (self.clean_search_query(query, str(i)) for i in range(1, 7))



        results = []
        for row in self.database_read:
            if row[2] == 'English Composition (GE Core)':
                pass
            #for search in query:
            matches_all = [[], [], [], [], [], []]
            for q_type in range(6):
                clean_query = self.clean_search_query(query, str(q_type + 1))
                #print(clean_query, "GGGGG")

                matches = 0

                for index, item in enumerate(clean_query):

                    #print(index, item)
                    if item in row[q_type]:
                        matches_all[q_type].append(True)

                        #break

                    else:
                        matches_all[q_type].append(False)
                        #break
                #print("Loop Complete")
                #print(matches, matches_all)

                for q_type2 in range(6):
                    if True in matches_all[q_type2]:
                        matches += 1

                if matches >= len(clean_query) and row not in results:
                    results.append(row)





            '''
            if hybrid:
                if prefix in course_prefix and number in course_number:
                    results.append(row)
            else:
                if prefix in course_prefix or number in course_number:
                    results.append(row)
            '''

        self.display_results(results, query)

    # ──────────────────────────────────────────────────────────────
    # Output
    # ──────────────────────────────────────────────────────────────

    def display_results(self, results: list, query: str):
        """Print search results."""
        if results:
            print(f"\nFound {len(results)} matching course(s):\n")
            for row in results:
                print(row)
            if len(results) >= 20:
                print(f"\n Found {len(results)} matching courses. To narrow down the search further, be more specific by including more search terms.")
        else:
            print("\nNo courses found matching your search.")
            if " " in query:
                print("You may have been trying to search multiple items at once, and forgotten to include semicolons (;) between each search term. \nThis may have been the query you were trying to make: ")
                query_split = query.split()
                corrected_query = ""
                for i in query_split:
                    corrected_query = corrected_query + i + "; "
                corrected_query = corrected_query[:-2]
                print(corrected_query)
                print("Searching new query... ")
                self.search(corrected_query)



# ──────────────────────────────────────────────────────────────
# Main Driver
# ──────────────────────────────────────────────────────────────
def main():
    course_db = CourseDatabase("DE_Equivalency_List_Clean.csv")
    course_db.load_data()
    course_db.preprocess()
    print("To search for a course, enter a search (Such as Enc; 1101)")
    search_query = input("Enter your search here, separated by semicolons: ")
    course_db.search(search_query)


if __name__ == "__main__":
    main()
