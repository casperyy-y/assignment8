def compute_mpg(miles, gallons):
    return miles / gallons if gallons > 0 else 0

trip_count = 0

response = input("Do you want to enter trip data? (Yes/No): ").strip().lower()
while response == "yes":
    destination = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    
    mpg = compute_mpg(miles, gallons)
    trip_count += 1

    print(f"Destination: {destination}, MPG: {mpg:.2f}")

    response = input("Do you want to enter another trip? (Yes/No): ").strip().lower()

print(f"\nTotal number of trips entered: {trip_count}")
