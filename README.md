# Project 17: Employee Salary Manager

**Allotted group:** Group 17
**Members:** Preet Nagar, Yash Raj Kohli, Harshit Rathaur, Aryan

## Objective

To develop a program that calculates salaries and prints payslips for a small company.

## Files

| File | Purpose |
|------|---------|
| `salary_manager.py` | The complete program (source code) |
| `payslips.txt` | Created by the program when you choose "Save payslips to file" |
| `README.md` | This file |

## How to run

Make sure Python 3 is installed. No extra libraries are needed, and the program uses no `import` statements.

```
python salary_manager.py
```

To run the doctests (the small tests written inside the functions):

```
python -m doctest salary_manager.py -v
```

If everything is correct, the last lines show `16 passed and 0 failed`.

## Menu options

| Option | What it does |
|--------|--------------|
| 1 | Shows the payroll as a table of employees against salary components |
| 2 | Shows the net salary of every employee and the highest-paid employee |
| 3 | Shows the total net salary of the company |
| 4 | Shows the set of departments, with employee count and total net salary of each |
| 5 | Adds a new employee (with input checking) |
| 6 | Saves the payslips of all employees to `payslips.txt` |
| 7 | Exits the program |

## Salary rules

All amounts are **monthly**.

| Component | Rule |
|-----------|------|
| HRA | 20% of basic pay |
| DA | 10% of basic pay |
| Gross salary | Basic + HRA + DA |
| PF deduction | 12% of basic pay |
| Income tax | Worked out on yearly taxable income (`(Gross - PF) x 12`) using the slabs below, then divided by 12 |
| Net salary | Gross - PF - Income tax |

**Income tax slabs (yearly income):**

| Yearly taxable income | Tax |
|-----------------------|-----|
| Up to 3,00,000 | No tax |
| 3,00,001 to 6,00,000 | 5% of the amount above 3,00,000 |
| 6,00,001 to 9,00,000 | 15,000 + 10% of the amount above 6,00,000 |
| 9,00,001 to 12,00,000 | 45,000 + 15% of the amount above 9,00,000 |
| 12,00,001 to 15,00,000 | 90,000 + 20% of the amount above 12,00,000 |
| Above 15,00,000 | 1,50,000 + 30% of the amount above 15,00,000 |

These are sample slabs. They can be changed in the function `calculate_tax()`.

## How the compulsory features are done

| Requirement | Where in the code |
|-------------|-------------------|
| Employees stored in a dictionary with ID, name, department and basic pay | `employees` dictionary at the top of the file |
| HRA (20%), DA (10%), PF (12%) | `calculate_hra()`, `calculate_da()`, `calculate_pf()` |
| Income tax by slabs using if-elif-else | `calculate_tax()` |
| Net salary and highest-paid employee | `calculate_salary()`, `find_highest_paid()`, `show_net_salaries()` |
| Payslips saved to a file | `make_payslip()`, `save_payslips()` |

## Where the key topics appear

| Topic | Use in this project |
|-------|---------------------|
| Nested loops | `print_payroll_table()`: the outer loop goes over employees, the inner loop goes over salary components |
| Recursion | `total_net_salary()` calls itself to add up all net salaries |
| Sets | `get_departments()` builds a set of department names (duplicates are ignored automatically) |
| Tuples | The ID and name of each employee are held as a tuple `(ID, name)`, which is the key of the dictionary |
| Dictionaries | The main data is the `employees` dictionary; each salary record is also a dictionary |

## Other Python concepts used

- **Strings:** formatting, `.strip()`, `.title()`, `.upper()`, `.center()`, `.join()`
- **Operators:** arithmetic, comparison and logical operators
- **Lists:** payroll records, column names, list of net salaries
- **If-else:** tax slabs, menu choices, input checks
- **Loops:** `for` loops for records and tables, `while` loop for the menu
- **Functions:** every task is a separate function
- **File handling:** `with open(...)` to write `payslips.txt`
- **Doctests:** examples written inside the docstrings of the calculation functions
- **Exception handling:** `try / except` for wrong input (`ValueError`) and file errors (`OSError`)

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
ID    Name                   Basic         HRA          DA       Gross          PF         Tax  Net Salary
==========================================================================================================
101   Aarav Sharma       50,000.00   10,000.00    5,000.00   65,000.00    6,000.00    2,150.00   56,850.00
102   Priya Singh        35,000.00    7,000.00    3,500.00   45,500.00    4,200.00      815.00   40,485.00
103   Rohan Verma        45,000.00    9,000.00    4,500.00   58,500.00    5,400.00    1,560.00   51,540.00
104   Neha Gupta         60,000.00   12,000.00    6,000.00   78,000.00    7,200.00    3,330.00   67,470.00
105   Karan Mehta        30,000.00    6,000.00    3,000.00   39,000.00    3,600.00      520.00   34,880.00
106   Sneha Joshi        40,000.00    8,000.00    4,000.00   52,000.00    4,800.00    1,110.00   46,090.00
```

**Option 2: Highest-paid employee**

```
Highest-paid employee: Neha Gupta (ID 104)
Net salary           : 67,470.00
```

**Option 3: Total net salary**

```
Total net salary of all employees: 297,315.00
```

**Option 6: A payslip in `payslips.txt`**

```
========================================
        PAYSLIP - NOVEMBER 2026
========================================
Employee ID : 101
Name        : Aarav Sharma
Department  : IT
----------------------------------------
EARNINGS
  Basic Pay    :      50,000.00
  HRA (20%)    :      10,000.00
  DA (10%)     :       5,000.00
  Gross Salary :      65,000.00
DEDUCTIONS
  PF (12%)     :       6,000.00
  Income Tax   :       2,150.00
----------------------------------------
NET SALARY     :      56,850.00
========================================
```

## Notes

- The basic pay in the sample data is monthly.
- The pay month shown on payslips is set by `PAY_MONTH` at the top of `salary_manager.py`.
- When a new employee is added from the menu, it is kept only while the program is running. It is not saved after exit.
