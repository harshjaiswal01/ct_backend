# 3. Python Programming Challenges for Customer Service Data Handling
# Objective: This assignment is designed to test and enhance your Python programming skills, 
# focusing on real-world applications in customer service data management. 
# You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program a function that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
#       Open a new service ticket.
#       Update the status of an existing ticket.
#       Display all tickets or filter by status.

# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_service_ticket(ticket, customer_nm, customer_iss): 
    service_tickets.update({ticket:{"Customer":customer_nm, "Issue":customer_iss, "Status":"open"}})
    # print(service_tickets)

def update_service_ticket(ticket, status):
    service_tickets[ticket]["Status"] = status
    # service_tickets.update(ticket:{"Status":status})

while True:
    try:
        print('''
            Please select an option given below:-
              1. Open a new service ticket
              2. Update the status of an existing ticket
              3. Display all tickets or filter by status
              4. Exit
              ''')
        user_input = int(input("Please enter your choice: "))
        if user_input < 0 or user_input > 4:
            raise ValueError("Choice Invalid")
        elif user_input > 0 and user_input <= 4:
            pass
        else:
            raise ValueError("Only Numeric")
    except:
        pass
    else:
        if user_input == 1:
            ticket_key = input("Please enter Ticket Key/ID: ")
            customer_name = input("Please enter Customer Name: ")
            customer_issue = input("What is the issue? ")
            add_service_ticket(ticket_key, customer_name, customer_issue)
        elif user_input == 2:
            ticket_key = input("Please enter Ticket Key/ID: ")
            status_update = input("Please enter current status: ").lower()
            update_service_ticket(ticket_key, status_update)
        elif user_input == 3:
            print("\nCurrent Tickets in the System:")
            for tickets in service_tickets:
                print("Ticket Key/ID:",tickets, "Ticket Details:", service_tickets[tickets])
            # filter_ask1 = ""
            # filter_ask2 = ""
            try:
                filter_ask1 = input("Would you like to filter by open or closed status? Yes or No? ").lower()
                if filter_ask1 == "yes":
                    filter_ask2 = input("Open or closed? ").lower()
                    if filter_ask2 == "open":
                        for ticket in service_tickets:
                            if service_tickets[ticket]["Status"] == "open":
                                print("Ticket Key/ID:", ticket, "Ticket Details:", service_tickets[ticket])
                    elif filter_ask2 == "closed":
                        for ticket in service_tickets:
                            if service_tickets[ticket]["Status"] == "closed":
                                print("Ticket Key/ID:", ticket, "Ticket Details:", service_tickets[ticket])
                    else:
                        raise ValueError("Open or Closed")
                elif filter_ask1 == "no":
                    pass
                else:
                    raise ValueError("yes or no")
            except ValueError as ve:
                if "yes or no" in str(ve):
                    print("Please only enter yes or no")
                elif "Open or Closed" in str(ve):
                    print("Please only enter Open or Closed")
        elif user_input == 4:
            break
    finally:
        # print("\nHave a great day!")
        pass