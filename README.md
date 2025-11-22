# README <br>
## Dual Enrollment High School Equivalency Lookup Tool <br>
A Python program designed to make the Florida Department of Education’s Dual Enrollment Equivalency List searchable, accurate, and user-friendly.

## Overview <br>
The Florida DOE publishes a long PDF each year listing how college courses convert to high school credits. This program converts that PDF into a structured CSV database and provides a fast, flexible search tool to help students, parents, and educators find course equivalency information efficiently.

## Features
-Search by course prefix, course number, course title, or multiple combined filters <br>
-Automatic formatting of search terms (e.g., “enc” → “ENC”, course numbers normalized to DOE style) <br>
-Supports unlimited search terms in a single query <br>
-Allows partial matches, keywords, and flexible combinations <br>
-Returns course prefix, course number, course name, high school credit value, high school graduation code, and GE core subject area <br>

## How to Use
Enter one or more search terms separated by semicolons (;). The program will return only courses that match all search terms. <br>

### Example 1 <br>
ENC; 1101 <br>
This searches for courses containing both “ENC” and “1101.” <br>
Sample output: <br>
ENC | X101 | Freshman Composition Skills I | 1.0 credit | English Language Arts <br>

### Example 2
enc; 1101; English comp; 1; Comm <br>
Because formatting is automatic, this will still run correctly. <br>

The tool will return results only if all search terms appear in the same course record. <br>

## Automatic Query Formatting <br>
The tool standardizes search terms to match the DOE format. <br>
-Course prefixes are converted to uppercase (e.g., “enc” → “ENC”) <br>
-Course numbers are normalized into the “X###” format <br>
-Partial words and lowercase text are accepted <br>
-Extra spaces are automatically removed <br>

This ensures that even imperfect or inconsistent search input produces accurate results. <br>

## Requirements
Python 3.9+ <br>
pandas <br>
rapidfuzz for advanced matching <br>
Install dependencies with: "pip install pandas" and "pip install rapidfuzz" <br>

## Running the Program 
python main.py

## Future Improvements
-Build a web-based version using Flask, React, or Click <br>
-Conduct usability testing comparing web-based tool’s speed and accuracy to the official PDF <br>
-Expand to support multiple years of DOE dual enrollment data <br>

## Author
Developed by Aiden Dugan <br>
Mentor: Dr. Gary Hrezo, Eastern Florida State College <br>
Part of a research project for the EFSC Undergraduate Research Exhibition. 