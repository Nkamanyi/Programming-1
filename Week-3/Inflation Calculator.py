"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Nkamanyi Martin Asungu Chatutie
Email: Chatutie.Nkamanyimartin@tuni.fi
Student no: K440302

Project: Inflation Calculator
"""

def main():

    inflation_rates = []

    while True:
        input_value = input(f"Enter inflation rate for month {len(inflation_rates)+1}: ")

        if not input_value:
            break

        try:
            value = float(input_value)
        except ValueError:
            print("Error: please enter a valid number.")
            continue

        inflation_rates.append(value)

    if len(inflation_rates) < 2:
        print("Error: at least 2 monthly inflation rates must be entered.")

    else:
        max_diff = max([(inflation_rates[i] - inflation_rates[i-1]) for i in range(1, len(inflation_rates))])
        print(f"Maximum inflation rate change was {max_diff:.1f} points.")

main()