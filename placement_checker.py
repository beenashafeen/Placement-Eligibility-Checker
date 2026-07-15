print("===================================")
print("    PLACEMENT ELIGIBILITY CHECKER")
print("===================================\n")

# Getting student details
name = input("Enter Student Name: ")

cgpa = float(input("Enter CGPA: "))
tenth = float(input("Enter 10th Percentage: "))
inter = float(input("Enter 12th Percentage: "))
backlogs = int(input("Enter Number of Active Backlogs: "))

print("\n------ RESULT ------")

# Checking each condition one by one

if cgpa >= 7:
    cgpa_status = True
else:
    cgpa_status = False

if tenth >= 60:
    tenth_status = True
else:
    tenth_status = False

if inter >= 60:
    inter_status = True
else:
    inter_status = False

if backlogs == 0:
    backlog_status = True
else:
    backlog_status = False

# Final Eligibility Check

if cgpa_status and tenth_status and inter_status and backlog_status:
    print("Congratulations,", name + "!")
    print("You are eligible for campus placements.")
else:
    print("Sorry,", name + ".")
    print("You are not eligible for campus placements.")

    print("\nReason(s):")

    if cgpa_status == False:
        print("- CGPA should be 7.0 or above.")

    if tenth_status == False:
        print("- 10th Percentage should be 60% or above.")

    if inter_status == False:
        print("- 12th Percentage should be 60% or above.")

    if backlog_status == False:
        print("- Active Backlogs should be Zero.")
