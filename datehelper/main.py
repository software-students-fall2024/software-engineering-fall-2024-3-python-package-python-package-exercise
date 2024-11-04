from datetime import date
from datehelper.core import add_days, days_between

def main():
    print("Welcome to the Date Helper!")

    year = int(input("Enter a year (e.g., 2023): "))
    month = int(input("Enter a month (1-12): "))
    day = int(input("Enter a day (1-31): "))
    days_to_add = int(input("Enter the number of days to add: "))

    input_date = date(year, month, day)

    try:
        future_date = add_days(input_date, days_to_add)
        print(f"\nStarting date: {input_date}")
        print(f"Adding {days_to_add} days...")
        print(f"New date: {future_date}")
        days_between_dates = days_between(input_date, future_date)
        print(f"Days between {input_date} and {future_date}: {days_between_dates}")

    except Exception as e:
        print(f"An error occurred: {e}")

    

    print("\nThank you for using Date Helper!")

if __name__ == "__main__":
    main()