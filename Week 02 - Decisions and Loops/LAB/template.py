"""
RECORD CHECK  -  my version
===========================

Name  : 
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
countoverlimit = 0
while True:
    label = str(input("Enter a Source IP or (quit): "))
    if label == "quit":
        break
    

    value = float(str(input("Enter failed attempts:")))    # replace with an input() call, converted with float()
    limit = float(str(input("Enter total attempts: ")))     # replace with an input() call, converted with float()  


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit - value  # replace with your calculation
    percent = (difference/limit) * 100      # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

    status = ""   # replace with your if / else (or if / elif / else)
    if percent >= 100:
        status = "OVER LIMIT"
        countoverlimit +=1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

# your report lines go here

    print("=" * 34)
    print(f"Failed login     :{value:>10.2f}")
    print(f"Total attempt    :{limit:>10.2f}")
    print(f"Difference       :{difference:>+10.2f}")
    print(f"percentage       :{percent:>10.2f}%")
    print(f"Status           :{status:>10}")

print(f"number of over limits:{countoverlimit}")



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
