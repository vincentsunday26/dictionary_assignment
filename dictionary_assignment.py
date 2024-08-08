# Initial menu
# Task 1: Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items
restaurant_menu["Beverages"] = {"Coffee": 2.99, "Tea": 2.49}

# Update the price of "Steak" to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# Updated menu
print(restaurant_menu)


#  Python Programming Challenges for Customer Service Data Handling

# Initial sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

# Function to update the status of an existing ticket to "closed"
def close_ticket(ticket_id):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = "closed"
    else:
        print(f"Ticket ID {ticket_id} not found.")

# Function to display all tickets
def display_tickets():
    for ticket_id, details in service_tickets.items():
        print(f"Ticket ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
