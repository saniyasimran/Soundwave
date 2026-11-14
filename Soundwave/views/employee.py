emp_id = input("Enter Employee ID: ")
category = input("Enter Employee Category: ")
shift = input("Enter Shift (Night/Early Morning/Day): ").lower()
distance = float(input("Enter Distance in km: "))
pickup = int(input("Enter Pickup Hour (0-23): "))
cancel = int(input("Enter Previous Cancellations: "))
registered = input("Registered for transport? (yes/no): ").lower()
trip = input("Trip Type (one-way/round-trip): ").lower()

# Eligibility
if registered == "yes" and (
    shift in ["night", "early morning"]
    or (shift == "day" and distance > 20)
):
    eligible = True
else:
    eligible = False

base_fare = 100
distance_fare = 0
extra = 0

if eligible:
    if distance <= 10:
        distance_fare = distance * 10
    elif distance <= 20:
        distance_fare = distance * 12
    else:
        distance_fare = distance * 15

    if trip == "round-trip":
        distance_fare *= 2

    if pickup >= 22 or pickup < 6:
        extra = 150

    total = base_fare + distance_fare + extra

    if cancel > 3:
        status = "Transport Approved - Review Required"
        review = "Yes"
    else:
        status = "Transport Approved"
        review = "No"

    remarks = "Eligible for company cab"
else:
    base_fare = 0
    total = 0
    status = "Transport Not Eligible"
    review = "No"
    remarks = "Eligibility conditions not satisfied"

print("\n----- CAB FARE DETAILS -----")
print("Employee ID:", emp_id)
print("Employee Category:", category)
print("Shift:", shift.title())
print("Distance:", distance, "km")
print("Trip Type:", trip)
print("Base Fare: ₹", base_fare)
print("Distance Fare: ₹", distance_fare)
print("Additional Charges: ₹", extra)
print("Total Fare: ₹", total)
print("Transport Status:", status)
print("Review Status:", review)
print("Remarks:", remarks)