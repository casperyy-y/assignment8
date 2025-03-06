def get_pay_rate(job_code):
    rates = {"L": 25, "A": 30, "J": 50}
    return rates.get(job_code.upper(), 0)  # Default to 0 if job code is invalid

total_gross_pay = 0

response = input("Do you want to enter employee data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ").strip().upper()
    hours_worked = float(input("Enter hours worked: "))

    pay_rate = get_pay_rate(job_code)
    if pay_rate == 0:
        print("Invalid job code entered.")
    else:
        if hours_worked > 40:
            regular_pay = 40 * pay_rate
            overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
            gross_pay = regular_pay + overtime_pay
        else:
            gross_pay = hours_worked * pay_rate
        
        total_gross_pay += gross_pay
        print(f"Employee: {last_name}, Gross Pay: ${gross_pay:.2f}")

    response = input("Do you want to enter another employee? (Yes/No): ").strip().lower()

print(f"\nTotal gross pay for all employees: ${total_gross_pay:.2f}")
