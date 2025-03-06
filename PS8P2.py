def compute_batting_avg(hits, at_bats):
    return hits / at_bats if at_bats > 0 else 0

player_count = 0

response = input("Do you want to enter player data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at-bats: "))
    
    avg = compute_batting_avg(hits, at_bats)
    player_count += 1

    print(f"Player: {last_name}, Batting Average: {avg:.3f}")

    response = input("Do you want to enter another player? (Yes/No): ").strip().lower()

print(f"\nTotal number of players entered: {player_count}")
