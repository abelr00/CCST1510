"""
RECORD CHECK  -  my version
===========================

Name  : Abel Ruharo
Lane  :  Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here



def check_record(value, limit):
    difference= value - limit
    percent = (value/limit) *100
    return difference, percent

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def print_report(label, value,limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"value      :{value:>10.2f}")
    print(f"limit      :{limit:>10.2f}")
    print(f"difference :{difference:>10.2f}")
    print(f"percent    :{percent:>10.2f}%")
    print(f"status     :{status:>10}")
    print("=" * 34)
    

countoverlimit = 0
while True:
    label = str(input("Enter a Source IP or (quit): "))
    if label == "quit":
        break
    

    value = float(str(input("Enter failed attempts:")))    # replace with an input() call, converted with float()
    limit = float(str(input("Enter total attempts: ")))   



    difference,percent = check_record(value,limit)  # replace with your code
         # replace with your code
    status = status_of(percent)
    if  status == "OVER LIMIT":
        countoverlimit +=1

    print_report(label,value,limit,difference,percent,status)


print(f"the overlimit count:{countoverlimit}")





