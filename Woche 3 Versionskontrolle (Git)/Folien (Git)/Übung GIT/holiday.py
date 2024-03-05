import random

def holiday_request_decision_extended():
    # Randomly choosing the length of vacation in weeks
    vacation_length = random.choice([1, 2, 3, 4, 5])
    
    # Making a decision based on the vacation length
    # Assumption: Longer vacations might be harder to approve
    if vacation_length <= 2:
        decision = "Accepted"
    elif vacation_length == 3:
        decision = random.choice(["Accepted", "Rejected"])
    else:
        decision = "Rejected"
        
    return f"Vacation Length: {vacation_length} week(s), Decision: {decision}"

# Example of how to use the function
result = holiday_request_decision_extended()
print(result)
