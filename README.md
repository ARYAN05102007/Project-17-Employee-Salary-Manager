# Project 17: Employee Salary Manager

**Allotted group:** Group 17
**Members:** Aryan, Harshit Rathaur, Preet Nagar, Yash Raj Kohli

## Objective

To develop a program that calculates salaries and prints payslips for a small company.

## Files

| File | Purpose |
|------|---------|
| `salary_manager.py` | The complete program (source code) |
| `payslips.txt` | Created by the program when menu option 4 is chosen |
| `README.md` | This file |

## How to run

Install Python 3, then run this command in the folder that has the file:

```
python salary_manager.py
```

The program uses only basic Python. No `import` statement and no extra library is needed.

## Menu options

| Option | What it does |
|--------|--------------|
| 1 | Shows the payroll as a table of employees against salary components |
| 2 | Shows the net salary of every employee, the highest-paid employee and the set of departments |
| 3 | Shows the total net salary of all employees (calculated using recursion) |
| 4 | Saves the payslips of all employees to `payslips.txt` |
| 5 | Exits the program |

Any other input shows the message "Enter a number from 1 to 5." and the menu appears again.

## Salary rules

All amounts are **monthly**.

| Component | Rule |
|-----------|------|
| HRA | 20% of basic pay |
| DA | 10% of basic pay |
| Gross salary | Basic + HRA + DA |
| PF deduction | 12% of basic pay |
| Income tax | Worked out on the yearly income `(Gross - PF) x 12` using the slabs below, then divided by 12 |
| Net salary | Gross - PF - Income tax |

**Income tax slabs (on yearly taxable income):**

| Yearly taxable income | Tax |
|-----------------------|-----|
| Up to 3,00,000 | No tax |
| 3,00,001 to 6,00,000 | 5% of the amount above 3,00,000 |
| 6,00,001 to 9,00,000 | 15,000 + 10% of the amount above 6,00,000 |
| 9,00,001 to 12,00,000 | 45,000 + 15% of the amount above 9,00,000 |
| 12,00,001 to 15,00,000 | 90,000 + 20% of the amount above 12,00,000 |
| Above 15,00,000 | 1,50,000 + 30% of the amount above 15,00,000 |

**Example (basic pay Rs. 50,000):** HRA = 10,000, DA = 5,000, Gross = 65,000, PF = 6,000.
Yearly taxable income = (65,000 - 6,000) x 12 = 7,08,000, so yearly tax = 15,000 + 10% of 1,08,000 = 25,800.
Monthly tax = 2,150 and **Net salary = 65,000 - 6,000 - 2,150 = Rs. 56,850**.

## How the compulsory features are done

| Requirement | Where in the code |
|-------------|-------------------|
| Employees stored in a dictionary with ID, name, department and basic pay | `employees` dictionary at the top of the file |
| HRA (20%), DA (10%), PF (12%) | `calculate_salary()` |
| Income tax by slabs using if-elif-else | `calculate_tax()` |
| Net salary and highest-paid employee | `calculate_salary()` and `show_summary()` |
| Payslips saved to a file | `save_payslips()` |

## Where the key topics appear

| Topic | Use in this project |
|-------|---------------------|
| Nested loops | `show_table()`: the outer loop goes over employees, the inner loop goes over the salary components |
| Recursion | `total_net()` calls itself to add up all net salaries |
| Sets | `show_summary()` builds a set of departments (repeated names are stored only once) |
| Tuples | The ID and name of each employee are held as a tuple `(ID, name)`, which is the key of the dictionary |
| Dictionaries | The main data is the `employees` dictionary; each value is also a dictionary with `dept` and `basic` |

## Functions

| Function | Purpose |
|----------|---------|
| `calculate_tax()` | Returns the yearly income tax using if-elif-else slabs |
| `calculate_salary()` | Returns the list `[basic, hra, da, gross, pf, tax, net]` |
| `total_net()` | Adds all net salaries using recursion |
| `show_table()` | Prints the payroll table using nested loops |
| `show_summary()` | Prints net salaries, the highest-paid employee and the departments |
| `save_payslips()` | Writes the payslips to `payslips.txt` |

The menu is a `while True` loop at the end of the file. It calls these functions according to the choice entered.

## Other Python concepts used

- **Strings:** f-string formatting, `strip()`, repeating a character with `"=" * 36`
- **Operators:** arithmetic, comparison and assignment operators
- **Lists:** the salary list returned by `calculate_salary()` and the `nets` list
- **If-elif-else:** tax slabs and menu choices
- **Loops:** `for` loops over employees and components, `while` loop for the menu
- **Functions:** every task is a separate function
- **File handling:** `with open(...)` to write `payslips.txt`
- **Exception handling:** `try / except OSError` while writing the file

## Sample data

| ID | Name | Department | Basic pay |
|----|------|------------|-----------|
| 101 | Aarav Sharma | IT | 50,000 |
| 102 | Priya Singh | HR | 35,000 |
| 103 | Rohan Verma | FINANCE | 45,000 |
| 104 | Neha Gupta | IT | 60,000 |
| 105 | Karan Mehta | SALES | 30,000 |
| 106 | Sneha Joshi | HR | 40,000 |

## Sample output

**Option 1: Payroll table**

```
ID    Name                Basic      HRA       DA    Gross       PF      Tax      Net
-------------------------------------------------------------------------------------
101   Aarav Sharma      50000.0  10000.0   5000.0  65000.0   6000.0   2150.0  56850.0
102   Priya Singh       35000.0   7000.0   3500.0  45500.0   4200.0    815.0  40485.0
103   Rohan Verma       45000.0   9000.0   4500.0  58500.0   5400.0   1560.0  51540.0
104   Neha Gupta        60000.0  12000.0   6000.0  78000.0   7200.0   3330.0  67470.0
105   Karan Mehta       30000.0   6000.0   3000.0  39000.0   3600.0    520.0  34880.0
106   Sneha Joshi       40000.0   8000.0   4000.0  52000.0   4800.0   1110.0  46090.0
```

**Option 2: Net salaries and highest paid**

```
--- Net Salaries ---
Aarav Sharma (IT): Rs. 56850.00
Priya Singh (HR): Rs. 40485.00
Rohan Verma (FINANCE): Rs. 51540.00
Neha Gupta (IT): Rs. 67470.00
Karan Mehta (SALES): Rs. 34880.00
Sneha Joshi (HR): Rs. 46090.00

Highest-Paid Employee: Neha Gupta -> Rs. 67470.00
Departments: ['FINANCE', 'HR', 'IT', 'SALES']
```

**Option 3: Total net salary**

```
Total Net Salary: Rs. 297315.00
```

**Option 4: First payslip in `payslips.txt`**

```
====================================
PAYSLIP - November 2026
====================================
ID         : 101
Name       : Aarav Sharma
Department : IT
Basic Pay  : 50000.00
HRA (20%)  : 10000.00
DA (10%)   : 5000.00
Gross      : 65000.00
PF (12%)   : 6000.00
Tax        : 2150.00
Net Salary : 56850.00
```

## Notes

- The employee data is written in the `employees` dictionary. To add an employee, add one more line in the same format.
- The income tax slabs are sample slabs. They can be changed in `calculate_tax()`.
- The pay month on the payslips ("November 2026") is typed inside `save_payslips()`.
- Choosing option 4 again overwrites the old `payslips.txt` file.
-
