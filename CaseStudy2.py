"""
Case Study: Social Network Adjacency Matrix
-------------------------------------------
Represent friendship connections in a social network using an adjacency matrix.
This educational example demonstrates matrix construction, friendship checks,
friend counts, and memory usage. It uses a small sample network by default.

Run:
    python social_network_matrix.py
    python social_network_matrix.py --users 8 --probability 0.3 --seed 42
    python social_network_matrix.py --users 1000 --probability 0.01 --no-matrix
"""

import argparse
import random
import sys
from typing import List, Tuple


def build_adjacency_matrix(
    user_count: int, friendship_probability: float = 0.25, seed: int = 42
) -> List[List[int]]:
    """
    Build an undirected, unweighted adjacency matrix.

    matrix[i][j] == 1 means user i and user j are friends.
    matrix[i][j] == 0 means there is no friendship edge.
    The diagonal is zero because a user is not considered their own friend.
    """
    if user_count < 1:
        raise ValueError("The number of users must be at least 1.")
    if not 0 <= friendship_probability <= 1:
        raise ValueError("Friendship probability must be between 0 and 1.")

    rng = random.Random(seed)
    matrix = [[0] * user_count for _ in range(user_count)]

    # Friendship is mutual, so generate only the upper triangle and mirror it.
    for i in range(user_count):
        for j in range(i + 1, user_count):
            if rng.random() < friendship_probability:
                matrix[i][j] = 1
                matrix[j][i] = 1

    return matrix


def are_friends(matrix: List[List[int]], user_a: int, user_b: int) -> bool:
    """Return whether two zero-based user indices are directly connected."""
    _validate_user(matrix, user_a)
    _validate_user(matrix, user_b)
    return matrix[user_a][user_b] == 1


def friend_count(matrix: List[List[int]], user: int) -> int:
    """Count the direct friends of one zero-based user index."""
    _validate_user(matrix, user)
    return sum(matrix[user])


def _validate_user(matrix: List[List[int]], user: int) -> None:
    if user < 0 or user >= len(matrix):
        raise IndexError(f"User index must be between 0 and {len(matrix) - 1}.")


def list_friendships(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    """Return each friendship once, using one-based user labels."""
    return [
        (i + 1, j + 1)
        for i in range(len(matrix))
        for j in range(i + 1, len(matrix))
        if matrix[i][j] == 1
    ]


def display_matrix(matrix: List[List[int]]) -> None:
    """Print a labeled adjacency matrix; intended for small networks only."""
    size = len(matrix)
    label_width = max(3, len(str(size)) + 1)
    print(" " * label_width + " ".join(f"{i + 1:>{label_width}}" for i in range(size)))
    for i, row in enumerate(matrix):
        print(f"{i + 1:>{label_width}}" + " ".join(f"{value:>{label_width}}" for value in row))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Demonstrate a social network represented by an adjacency matrix."
    )
    parser.add_argument("--users", type=int, default=6,
                        help="number of users (default: 6)")
    parser.add_argument("--probability", type=float, default=0.3,
                        help="probability of a friendship between any pair (0 to 1)")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed for repeatable sample connections")
    parser.add_argument("--no-matrix", action="store_true",
                        help="skip printing the matrix; useful for larger networks")
    args = parser.parse_args()

    if args.users < 1:
        parser.error("--users must be at least 1")
    if not 0 <= args.probability <= 1:
        parser.error("--probability must be between 0 and 1")

    matrix = build_adjacency_matrix(args.users, args.probability, args.seed)
    friendships = list_friendships(matrix)

    print("SOCIAL NETWORK — ADJACENCY MATRIX")
    print(f"Users: {args.users}")
    print(f"Friendship probability: {args.probability:.2f}")
    if not args.no_matrix:
        print("\nAdjacency matrix (1 = friends, 0 = not friends):")
        display_matrix(matrix)

    print(f"\nTotal friendship connections: {len(friendships)}")
    print("Friendships (user labels start at 1):")
    if friendships:
        for a, b in friendships:
            print(f"  User {a} <-> User {b}")
    else:
        print("  No friendships generated.")

    example_user = 1
    print(f"\nDirect friends of User {example_user}: {friend_count(matrix, 0)}")
    if args.users >= 2:
        print(
            f"Are User 1 and User 2 friends? "
            f"{'Yes' if are_friends(matrix, 0, 1) else 'No'}"
        )

    # Python lists have substantial per-element overhead, so this is a lower
    # bound for the raw one-byte-per-cell matrix representation only.
    raw_bytes = args.users * args.users
    print(f"\nTheoretical storage at 1 byte per matrix cell: {raw_bytes:,} bytes")
    print("Note: a Python list-of-lists uses more memory than this estimate.")


if __name__ == "__main__":
    main()
