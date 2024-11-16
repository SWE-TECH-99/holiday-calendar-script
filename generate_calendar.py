from ics import Calendar, Event
from datetime import datetime, timedelta

holidays = [
    {"date": "2024-12-20", "description": "Full Day"},
    {"date": "2024-12-21", "description": "Full Day"},
    {"date": "2024-12-22", "description": "Full Day"},
    {"date": "2024-12-23", "description": "Half Day (AM)"},
    {"date": "2024-12-24", "description": "Full Day"},
    {"date": "2024-12-25", "description": "Christmas Day"},
    {"date": "2024-12-26", "description": "Boxing Day"},
    {"date": "2024-12-27", "description": "Full Day"},
    {"date": "2024-12-28", "description": "Full Day"},
    {"date": "2024-12-29", "description": "Full Day"},
    {"date": "2024-12-30", "description": "Full Day"},
    {"date": "2024-12-31", "description": "Half Day (PM)"},
    {"date": "2025-01-01", "description": "New Year's Day"},
    {"date": "2025-01-02", "description": "Full Day"},
    {"date": "2025-01-03", "description": "Full Day"},
    {"date": "2025-01-04", "description": "Full Day"},
    {"date": "2025-01-05", "description": "Full Day"},
    {"date": "2025-01-06", "description": "Back To Work"}
]

# Create a calendar object
calendar = Calendar()

# Add each holiday as an event, excluding weekends and specific holidays
for holiday in holidays:
    event_date = datetime.strptime(holiday["date"], "%Y-%m-%d")
    day_of_week = event_date.weekday()  # 0 = Monday, 6 = Sunday

    # Skip weekends (Saturday and Sunday) and specific holidays
    if day_of_week >= 5 or holiday['description'] in ["Christmas Day", "Boxing Day", "New Year's Day"]:
        continue

    event = Event()
    
    if "Full Day" in holiday["description"]:
        event.name = "Sachin's Full day off from work"
        event.begin = event_date
        event.make_all_day()
    elif "Half Day" in holiday["description"]:
        event.name = "Sachin's Half Day from work"
        event.begin = event_date.replace(hour=9, minute=0)
        event.end = event_date.replace(hour=12, minute=0)  # Ensures 9:00 AM to 12:00 PM

    calendar.events.add(event)

# Save to an .ics file with the desired filename
with open("Sachin's_Holidays_From_Work.ics", "w") as f:
    f.writelines(calendar)

print("Calendar file 'Sachin's_Holidays_From_Work.ics' created successfully.")
