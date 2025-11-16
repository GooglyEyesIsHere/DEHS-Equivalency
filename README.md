# Dual Enrollment High School Equivalency Lookup Tool
This Python program will be used to convert the long PDF provided by the Florida Department of Education into a database with a search feature.
It will include all the information provided in the original PDF, such as the high school credit value of college courses.
To search for a course/courses, type in the query, followed by a semicolon, then the next query. 
For example, <br>Enc; 1101 <br>Will give a list of all courses containing both ENC and X101. 
Searches will be automatically formatted to the correct type, so course prefixes will be made uppercase and course numbers will have their first characters replaced by an X. 
Similar adjustments are also made for the other search categories.
Note also that there is no limit to how many search queries can be made in a single search.
For example, <br> Enc; 1101; English comp; 1; Comm <br> is a valid search and may return a result if everything is present in a single course.