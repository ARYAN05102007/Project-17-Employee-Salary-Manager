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

