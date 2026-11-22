"""
Project 17: Employee Salary Manager
Group 17: Preet Nagar, Yash Raj Kohli, Harshit Rathaur, Aryan

Run program: python salary_manager.py
"""

# Main dictionary: key = (id, name) tuple, value = dictionary
employees = {
    (101, "Aarav Sharma"): {"dept": "IT", "basic": 50000},
    (102, "Priya Singh"): {"dept": "HR", "basic": 35000},
    (103, "Rohan Verma"): {"dept": "FINANCE", "basic": 45000},
    (104, "Neha Gupta"): {"dept": "IT", "basic": 60000},
    (105, "Karan Mehta"): {"dept": "SALES", "basic": 30000},
    (106, "Sneha Joshi"): {"dept": "HR", "basic": 40000},
    (107, "Preet Nagar"): {"dept": "IT", "basic": 10000}
}


def calculate_tax(annual_income):
    """Yearly income tax using slabs (if-elif-else)."""
    if annual_income <= 300000:
        tax = 0
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
    return tax


def calculate_salary(basic):
    """Return list: [basic, hra, da, gross, pf, tax, net]"""
    hra = basic * 0.20
    da = basic * 0.10
    pf = basic * 0.12
    gross = basic + hra + da
    tax = calculate_tax((gross - pf) * 12) / 12   # monthly tax
    net = gross - pf - tax
    return [basic, round(hra, 2), round(da, 2), round(gross, 2),
            round(pf, 2), round(tax, 2), round(net, 2)]


def total_net(nets, i=0):
    """Add all net salaries using recursion."""
    if i == len(nets):
        return 0.0
    return nets[i] + total_net(nets, i + 1)

def show_table():
    """Employees vs salary components (nested loops)."""
    heads = ["Basic", "HRA", "DA", "Gross", "PF", "Tax", "Net"]
    print(f"\n{'ID':<6}{'Name':<16}", end="")
    for h in heads:
        print(f"{h:>9}", end="")
    print()
    print("-" * 85)

    for (emp_id, name), info in employees.items():     # outer loop
        line = f"{emp_id:<6}{name:<16}"
        for value in calculate_salary(info["basic"]):  # inner loop
            line += f"{value:>9.1f}"
        print(line)


def show_summary():
    """Net salaries, highest-paid employee and set of departments."""
    highest_name = ""
    highest_net = 0
    departments = set()

    print("\n--- Net Salaries ---")
    for (emp_id, name), info in employees.items():
        net = calculate_salary(info["basic"])[6]
        print(f"{name} ({info['dept']}): Rs. {net:.2f}")
        departments.add(info["dept"])
        if net > highest_net:
            highest_net = net
            highest_name = name

    print(f"\nHighest-Paid Employee: {highest_name} -> Rs. {highest_net:.2f}")
    print("Departments:", sorted(departments))


def save_payslips():
    """Write payslips of all employees to payslips.txt"""
    try:
        with open("payslips.txt", "w") as f:
            for (emp_id, name), info in employees.items():
                b, hra, da, gross, pf, tax, net = calculate_salary(info["basic"])
                f.write("=" * 36 + "\n")
                f.write("PAYSLIP - November 2026\n")
                f.write("=" * 36 + "\n")
                f.write(f"ID         : {emp_id}\n")
                f.write(f"Name       : {name}\n")
                f.write(f"Department : {info['dept']}\n")
                f.write(f"Basic Pay  : {b:.2f}\n")
                f.write(f"HRA (20%)  : {hra:.2f}\n")
                f.write(f"DA (10%)   : {da:.2f}\n")
                f.write(f"Gross      : {gross:.2f}\n")
                f.write(f"PF (12%)   : {pf:.2f}\n")
                f.write(f"Tax        : {tax:.2f}\n")
                f.write(f"Net Salary : {net:.2f}\n\n")
        print("Payslips saved in 'payslips.txt'.")
    except OSError:
        print("Could not write the file.")


# ---------------- Menu (program starts here) ----------------
while True:
    print("\n=== Employee Salary Manager ===")
    print("1. Show Payroll Table")
    print("2. Show Net Salaries & Highest Paid")
    print("3. Show Total Net Salary")
    print("4. Save Payslips to File")
    print("5. Exit")
    choice = input("Choose (1-5): ").strip()

    if choice == "1":
        show_table()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        nets = []
        for info in employees.values():
            nets.append(calculate_salary(info["basic"])[6])
        print(f"Total Net Salary: Rs. {total_net(nets):.2f}")
    elif choice == "4":
        save_payslips()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Enter a number from 1 to 5.")

