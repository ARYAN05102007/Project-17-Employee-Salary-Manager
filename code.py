""" 
Project 17: Employee Salary Manager
Group 17
Members: Preet Nagar, Yash Raj Kohli, Harshit Rathaur, Aryan

A small payroll program that calculates salaries, prints a payroll
table, finds the highest-paid employee and saves payslips to a file.

Run the program :  python salary_manager.py
Run the doctests:  python -m doctest salary_manager.py -v
"""

# ---------------------------------------------------------------
# DATA
# The main data is held in a DICTIONARY.
#   key   -> a TUPLE of (employee ID, employee name)
#   value -> a dictionary with the department and the monthly basic pay
# ---------------------------------------------------------------
employees = {
    (101, "Aarav Sharma"): {"department": "IT", "basic": 50000},
    (102, "Priya Singh"): {"department": "HR", "basic": 35000},
    (103, "Rohan Verma"): {"department": "FINANCE", "basic": 45000},
    (104, "Neha Gupta"): {"department": "IT", "basic": 60000},
    (105, "Karan Mehta"): {"department": "SALES", "basic": 30000},
    (106, "Sneha Joshi"): {"department": "HR", "basic": 40000},
}

# Salary rules (as given in the project)
HRA_RATE = 0.20   # House Rent Allowance = 20% of basic pay
DA_RATE = 0.10    # Dearness Allowance   = 10% of basic pay
PF_RATE = 0.12    # Provident Fund       = 12% of basic pay

PAYSLIP_FILE = "payslips.txt"
PAY_MONTH = "November 2026"   # change this when needed

# Columns of the payroll table (used by the nested loops)
COMPONENTS = ["basic", "hra", "da", "gross", "pf", "tax", "net"]
HEADINGS = ["Basic", "HRA", "DA", "Gross", "PF", "Tax", "Net Salary"]


# ---------------------------------------------------------------
# SALARY CALCULATIONS
# ---------------------------------------------------------------
def calculate_hra(basic):
    """Return HRA (20% of basic pay).

    >>> calculate_hra(50000)
    10000.0
    >>> calculate_hra(0)
    0.0
    """
    return round(basic * HRA_RATE, 2)


def calculate_da(basic):
    """Return DA (10% of basic pay).

    >>> calculate_da(50000)
    5000.0
    """
    return round(basic * DA_RATE, 2)


def calculate_pf(basic):
    """Return PF deduction (12% of basic pay).

    >>> calculate_pf(50000)
    6000.0
    """
    return round(basic * PF_RATE, 2)


def calculate_tax(annual_income):
    """Return the yearly income tax using slabs (if-elif-else).

    Slabs used (sample slabs):
        up to 3,00,000          : no tax
        3,00,001 to 6,00,000    : 5%
        6,00,001 to 9,00,000    : 10%
        9,00,001 to 12,00,000   : 15%
        12,00,001 to 15,00,000  : 20%
        above 15,00,000         : 30%

    >>> calculate_tax(250000)
    0.0
    >>> calculate_tax(600000)
    15000.0
    >>> calculate_tax(708000)
    25800.0
    >>> calculate_tax(1800000)
    240000.0
    """
    if annual_income <= 300000:
        tax = 0.0
    elif annual_income <= 600000:
        tax = (annual_income - 300000) * 0.05
    elif annual_income <= 900000:
        tax = 15000 + (annual_income - 600000) * 0.10
    elif annual_income <= 1200000:
        tax = 45000 + (annual_income - 900000) * 0.15
    elif annual_income <= 1500000:
        tax = 90000 + (annual_income - 1200000) * 0.20
    else:
        tax = 150000 + (annual_income - 1500000) * 0.30
    return round(tax, 2)


def calculate_salary(basic):
    """Return a dictionary with all salary components for one employee.

    >>> calculate_salary(50000)["gross"]
    65000.0
    >>> calculate_salary(50000)["tax"]
    2150.0
    >>> calculate_salary(50000)["net"]
    56850.0
    """
    hra = calculate_hra(basic)
    da = calculate_da(basic)
    gross = round(basic + hra + da, 2)
    pf = calculate_pf(basic)

    # Tax is worked out on the yearly income after PF, then made monthly
    yearly_taxable = (gross - pf) * 12
    tax = round(calculate_tax(yearly_taxable) / 12, 2)

    net = round(gross - pf - tax, 2)

    salary = {
        "basic": basic,
        "hra": hra,
        "da": da,
        "gross": gross,
        "pf": pf,
        "tax": tax,
        "net": net,
    }
    return salary


def build_payroll(employee_data):
    """Return a list with one salary record (dictionary) per employee."""
    payroll = []
    for key, info in employee_data.items():
        record = calculate_salary(info["basic"])
        record["id"] = key[0]       # first item of the tuple
        record["name"] = key[1]     # second item of the tuple
        record["department"] = info["department"]
        payroll.append(record)
    return payroll


# ---------------------------------------------------------------
# RECURSION, SETS AND SEARCHING
# ---------------------------------------------------------------
def total_net_salary(net_list, index=0):
    """Recursively add up all the net salaries in a list.

    >>> total_net_salary([100.0, 200.0, 300.0])
    600.0
    >>> total_net_salary([])
    0
    """
    if index == len(net_list):          # base case: nothing left to add
        return 0
    return net_list[index] + total_net_salary(net_list, index + 1)


def get_departments(employee_data):
    """Return a SET of all department names.

    >>> data = {(1, "A"): {"department": "IT", "basic": 1},
    ...         (2, "B"): {"department": "IT", "basic": 2},
    ...         (3, "C"): {"department": "HR", "basic": 3}}
    >>> get_departments(data) == {"IT", "HR"}
    True
    """
    departments = set()
    for info in employee_data.values():
        departments.add(info["department"])    # a set ignores duplicates
    return departments


def find_highest_paid(payroll):
    """Return the record of the employee with the highest net salary.

    >>> find_highest_paid([{"name": "A", "net": 10.0},
    ...                    {"name": "B", "net": 20.0}])["name"]
    'B'
    """
    highest = payroll[0]
    for record in payroll:
        if record["net"] > highest["net"]:
            highest = record
    return highest


# ---------------------------------------------------------------
# DISPLAY FUNCTIONS
# ---------------------------------------------------------------
def print_payroll_table(payroll):
    """Print the payroll as a table: employees (rows) x components (columns)."""
    header = f"{'ID':<6}{'Name':<16}"
    for heading in HEADINGS:
        header += f"{heading:>12}"

    line = "=" * len(header)
    print(line)
    print(header)
    print(line)

    for record in payroll:                      # outer loop -> each employee (row)
        row = f"{record['id']:<6}{record['name']:<16}"
        for component in COMPONENTS:            # inner loop -> each component (column)
            row += f"{record[component]:>12,.2f}"
        print(row)

    print(line)


def show_net_salaries(payroll):
    """Show the net salary of every employee and the highest-paid employee."""
    print("\nNet salary of each employee")
    print("-" * 40)
    for record in payroll:
        print(f"{record['name']:<18}{record['net']:>14,.2f}")

    best = find_highest_paid(payroll)
    print("-" * 40)
    print(f"Highest-paid employee: {best['name']} (ID {best['id']})")
    print(f"Net salary           : {best['net']:,.2f}")


def show_department_summary(payroll, departments):
    """Show the number of employees and total net salary of each department."""
    print("\nDepartments:", sorted(departments))
    print("-" * 46)
    for dept in sorted(departments):
        count = 0
        total = 0.0
        for record in payroll:
            if record["department"] == dept:
                count = count + 1
                total = total + record["net"]
        print(f"{dept:<10}{count} employee(s){total:>20,.2f}")


# ---------------------------------------------------------------
# PAYSLIPS AND FILE HANDLING
# ---------------------------------------------------------------
def make_payslip(record):
    """Return the payslip of one employee as a string."""
    lines = []
    lines.append("=" * 40)
    lines.append(f"PAYSLIP - {PAY_MONTH.upper()}".center(40))
    lines.append("=" * 40)
    lines.append(f"Employee ID : {record['id']}")
    lines.append(f"Name        : {record['name']}")
    lines.append(f"Department  : {record['department']}")
    lines.append("-" * 40)
    lines.append("EARNINGS")
    lines.append(f"  Basic Pay    : {record['basic']:>14,.2f}")
    lines.append(f"  HRA (20%)    : {record['hra']:>14,.2f}")
    lines.append(f"  DA (10%)     : {record['da']:>14,.2f}")
    lines.append(f"  Gross Salary : {record['gross']:>14,.2f}")
    lines.append("DEDUCTIONS")
    lines.append(f"  PF (12%)     : {record['pf']:>14,.2f}")
    lines.append(f"  Income Tax   : {record['tax']:>14,.2f}")
    lines.append("-" * 40)
    lines.append(f"NET SALARY     : {record['net']:>14,.2f}")
    lines.append("=" * 40)
    return "\n".join(lines)


def save_payslips(payroll, filename=PAYSLIP_FILE):
    """Save the payslips of all employees to a text file."""
    try:
        with open(filename, "w") as file:
            for record in payroll:
                file.write(make_payslip(record))
                file.write("\n\n")
        print(f"Payslips saved to '{filename}'.")
    except OSError:
        print("Error: the payslip file could not be written.")


# ---------------------------------------------------------------
# ADDING AN EMPLOYEE (with exception handling)
# ---------------------------------------------------------------
def add_employee(employee_data):
    """Ask the user for a new employee and add it to the dictionary."""
    try:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ").strip().title()
        department = input("Enter department: ").strip().upper()
        basic = float(input("Enter monthly basic pay: "))

        if name == "" or department == "":
            raise ValueError("name and department cannot be empty")
        if basic <= 0:
            raise ValueError("basic pay must be greater than zero")

        for key in employee_data:
            if key[0] == emp_id:
                raise ValueError("this employee ID already exists")

        employee_data[(emp_id, name)] = {"department": department, "basic": basic}
        print(f"Employee {name} added successfully.")
    except ValueError as error:
        print("Could not add employee ->", error)


# ---------------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------------
def main():
    print("=" * 40)
    print("      EMPLOYEE SALARY MANAGER")
    print("=" * 40)

    while True:
        print("\n1. Show payroll table")
        print("2. Show net salaries and highest-paid employee")
        print("3. Show total net salary of the company")
        print("4. Show departments")
        print("5. Add a new employee")
        print("6. Save payslips to file")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        # The payroll is rebuilt every time, so new employees are included
        payroll = build_payroll(employees)

        if choice == "1":
            print_payroll_table(payroll)
        elif choice == "2":
            show_net_salaries(payroll)
        elif choice == "3":
            net_list = []
            for record in payroll:
                net_list.append(record["net"])
            total = total_net_salary(net_list)
            print(f"\nTotal net salary of all employees: {total:,.2f}")
        elif choice == "4":
            show_department_summary(payroll, get_departments(employees))
        elif choice == "5":
            add_employee(employees)
        elif choice == "6":
            save_payslips(payroll)
        elif choice == "7":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
