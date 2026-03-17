Student Marks Analysis Project
Overview

This is a Python project that analyzes student marks using the Pandas library.
It calculates total marks, average marks, grades, and ranking for each student and generates a complete result table.
The project is beginner-friendly and demonstrates data analysis concepts using Python.

Features

Reads student data from a CSV file (students.csv)

Calculates Total Marks for each student

Calculates Average Marks

Assigns Grades based on average marks

Computes Student Ranking

Identifies Highest Scorer

Saves the final result to a new CSV file (student_result.csv)

Grade System
Average Marks	Grade
90 and above	A+
80 – 89	A
70 – 79	B
60 – 69	C
Below 60	F
Project Structure
PROJECT5/
│
├── main.py                # Python script to analyze marks
├── students.csv           # Input file with student names and marks
├── student_result.csv     # Output file generated after running the script
├── README.md              # Project documentation
└── .gitignore             # Ignore virtual environment and cache files
How to Run

Clone or download this project.

Make sure you have Python 3 installed.

Install Pandas if not already installed.

Open terminal in VS Code (or command prompt) inside PROJECT5 folder.

Run the Python script: python main.py

Check student_result.csv for the final results.

Example Output
Name	Math	Science	English	Total	Average	Grade	Rank
Qasim	95	90	88	273	91.0	A+	1
Raja	80	85	78	243	81.0	A	2
Javed	70	75	72	217	72.3	B	3
Khan	60	65	68	193	64.3	C	4
Technologies Used

Python 3

Pandas library for data analysis

CSV files for input/output

Author

Raja Qasim Javed Khan
