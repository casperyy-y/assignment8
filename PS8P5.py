def compute_tuition(credits, district_code):
    rate = 250 if district_code.upper() == "I" else 550
    return credits * rate

total_tuition = 0

response = input("Do you want to enter student data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter student last name: ")
    district_code = input("Enter district code (I/O): ").strip().upper()
    credits = int(input("Enter credit hours: "))

    tuition = compute_tuition(credits, district_code)
    total_tuition += tuition

    print(f"Student: {last_name}, Tuition Owed: ${tuition:.2f}")

    response = input("Do you want to enter another student? (Yes/No): ").strip().lower()

print(f"\nTotal tuition owed for all students: ${total_tuition:.2f}")
