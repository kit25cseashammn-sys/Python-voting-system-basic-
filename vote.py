import os

candidates = ["Alice", "Bob", "Charlie"]

VOTERS_FILE = "voters.txt"
VOTES_FILE = "votes.txt"

def load_voters():
    if not os.path.exists(VOTERS_FILE):
        return set()
    with open(VOTERS_FILE, "r") as f:
        return set(name.strip().lower() for name in f)

def load_votes():
    votes = {}
    if os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, "r") as f:
            for line in f:
                name, candidate = line.strip().split(",")
                votes[name] = candidate
    return votes

def save_vote(name, candidate):
    with open(VOTES_FILE, "a") as f:
        f.write(f"{name},{candidate}\n")

def vote():
    voters = load_voters()
    votes = load_votes()

    name = input("Enter your name: ").strip().lower()

    if name not in voters:
        print("You are not eligible to vote.")
        return

    if name in votes:
        print("You have already voted.")
        return

    print("\nCandidates:")
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")

    try:
        choice = int(input("Choose your candidate number: "))
        if choice < 1 or choice > len(candidates):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_candidate = candidates[choice - 1]

    save_vote(name, selected_candidate)
    print(f"Vote cast successfully for {selected_candidate}!")

def show_results():
    votes = load_votes()
    result = {candidate: 0 for candidate in candidates}

    for candidate in votes.values():
        if candidate in result:
            result[candidate] += 1

    print("\nVoting Results:")
    for candidate, count in result.items():
        print(f"{candidate}: {count} votes")

def main():
    while True:
        print("\n==== Voting System ====")
        print("1. Vote")
        print("2. Show Results")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            vote()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
