# Tower of hanoi proper version
# Recursive solution with step counter

def tower_of_hanoi(n, source, target, auxiliary, steps=None):
    if steps is None:
        steps = []

    if n == 1:
        steps.append(f"Move disk 1 from {source} to {target}")
        return steps

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target, steps)

    # Move the nth disk from source to target
    steps.append(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source, steps)

    return steps


# Driver code
num_disks = int(input("Enter number of disks: "))
moves = tower_of_hanoi(num_disks, "A", "C", "B")

print(f"\nTotal moves required: {len(moves)}")
for move in moves:
    print(move)
