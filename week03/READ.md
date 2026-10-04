Week 03

AI Tool Used: ChatGPT

Prompt Used: Create a Python cinema ticket office program using input, type conversion, f-strings, loops, if/elif/else, and input validation. The program should calculate ticket prices based on age, day, and student status, then print a summary.

What did you change?

I created the ticket office program and added age, day, and student input validation. I also added the ticket price calculation and summary.

Tests:

Input: Age 20, Weekday, Student yes
Result: 140.00 TRY (Student)

Input: Age 12, Weekend, Student no
Result: 150.00 TRY (Child)

Input: Age 65, Weekday, Student no
Result: 100.00 TRY (Senior)

Why does the order of the rules matter?

The order matters because one customer can meet more than one condition. For example, a 10-year-old student is both a child and a student, so the Child rule must come before the Student rule.
