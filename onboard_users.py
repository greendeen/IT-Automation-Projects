import csv
import json

def create_user_onboarding(csv_file):
    
    print("--- Starting User Onboarding Process ---")
    
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                dept = row['Department']
                
               
                if dept == "IT":
                    permissions = "Admin Access"
                elif dept == "Finance":
                    permissions = "Financial Records Access"
                else:
                    permissions = "Standard User Access"
                
                print(f"Success: Account created for {name}. Assigned to {dept} with {permissions}.")
                
    except FileNotFoundError:
        print("Error: CSV file not found. Please ensure 'new_hires.csv' exists.")


if __name__ == "__main__":
    create_user_onboarding('new_hires.csv')
