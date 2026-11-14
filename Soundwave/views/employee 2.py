name = input("Enter Passenger Name: ")
ptype = input("Enter Passenger Type: ")
ticket = input("Enter Ticket Class: ").lower()
weight = float(input("Enter Baggage Weight (kg): "))
bags = int(input("Enter Number of Checked Bags: "))
loyalty = input("Loyalty Member? (yes/no): ").lower()
checkin = input("Online Check-in Completed? (yes/no): ").lower()
paid = input("Baggage Charge Accepted for Payment? (yes/no): ").lower()

# Free baggage allowance
if ticket == "economy":
    allowed = 15
elif ticket == "premium economy":
    allowed = 20
elif ticket == "business":
    allowed = 30
else:
    allowed = 0

if loyalty == "yes" and allowed > 0:
    allowed += 5

excess = max(0, weight - allowed)

# Calculate baggage charge
if excess == 0:
    charge = 0
elif excess <= 5:
    charge = 1000
elif excess <= 10:
    charge = 2500
else:
    charge = 3000

# Boarding eligibility
if allowed == 0:
    checkin_status = "Invalid Ticket Class"
    boarding = "Not Cleared"
    remarks = "Invalid ticket class"
elif weight > 40:
    checkin_status = "Check-in Rejected"
    boarding = "Not Cleared"
    remarks = "Baggage exceeds 40 kg limit"
elif checkin != "yes":
    checkin_status = "Online Check-in Incomplete"
    boarding = "Not Cleared"
    remarks = "Complete online check-in"
elif charge > 0 and paid != "yes":
    checkin_status = "Payment Pending"
    boarding = "Not Cleared"
    remarks = "Accept baggage charge"
else:
    checkin_status = "Check-in Successful"

    if ticket == "business" and excess == 0:
        boarding = "Priority Cleared"
    else:
        boarding = "Boarding Cleared"

    remarks = "Passenger eligible for boarding"

print("\n----- AIRLINE CHECK-IN DETAILS -----")
print("Passenger Name:", name)
print("Ticket Class:", ticket.title())
print("Loyalty Membership:", loyalty.title())
print("Allowed Baggage:", allowed, "kg")
print("Actual Baggage:", weight, "kg")
print("Excess Baggage:", excess, "kg")
print("Baggage Charge: ₹", charge)
print("Check-in Status:", checkin_status)
print("Boarding Status:", boarding)
print("Remarks:", remarks)