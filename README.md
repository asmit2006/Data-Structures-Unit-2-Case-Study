# Case Study: Social Network Adjacency Matrix

## Objective

Represent friendship connections among users in a social network using an
**adjacency matrix**. The program builds an example undirected network and
demonstrates how to check friendships, count a user's friends, and list edges.

This is a learning demonstration with randomly generated sample data. It does
not connect to a real social network or use real users' information.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Files

- `social_network_matrix.py` — source code.
- `README.md` — project documentation.

## Run the program

```bash
python social_network_matrix.py
```

Generate a network with 8 users:

```bash
python social_network_matrix.py --users 8 --probability 0.3 --seed 42
```

For a larger network, skip printing the full matrix:

```bash
python social_network_matrix.py --users 1000 --probability 0.01 --no-matrix
```

The `--seed` option makes the generated sample repeatable. `--probability`
sets the chance that any pair of users is connected.

## What is an adjacency matrix?

For a network with `n` users, an adjacency matrix is an `n × n` table:

- `matrix[i][j] = 1` means user `i` and user `j` are friends.
- `matrix[i][j] = 0` means there is no direct friendship.
- The diagonal is `0` because users are not connected to themselves.
- Friendships are mutual, so the matrix is symmetric:
  `matrix[i][j] == matrix[j][i]`.

Example for four users:

```text
    1 2 3 4
  1 0 1 0 1
  2 1 0 1 0
  3 0 1 0 0
  4 1 0 0 0
```

In this example, User 1 is friends with Users 2 and 4.

## Main operations

- **Build matrix:** generate possible friendship links.
- **Check friendship:** inspect one matrix cell.
- **Count friends:** sum a user's row.
- **List connections:** examine only the upper triangle so each mutual
  friendship is listed once.

The implementation uses zero-based indices internally; displayed user labels
start at 1 for readability.

## Complexity analysis

Let `n` be the number of users and `m` be the number of friendship edges.

| Operation | Time complexity |
|---|---:|
| Build the matrix | `O(n²)` |
| Check whether two users are friends | `O(1)` |
| Count one user's friends | `O(n)` |
| List all friendship edges | `O(n²)` |
| Matrix storage | `O(n²)` |

## Can an adjacency matrix represent millions of users?

A full adjacency matrix is usually **not practical** for a social network with
millions of users because it requires `n²` cells even when most users have few
friends.

For example, with 1,000,000 users:

- Matrix cells: `1,000,000,000,000` (10¹²).
- At a theoretical one byte per cell: about 1 TB in decimal units, before
  overhead; a Python list-of-lists needs much more memory.

Real social networks are typically sparse graphs, so an **adjacency list** or
compressed sparse representation is generally more memory-efficient. An
adjacency matrix can still be useful for small or dense graphs and gives
constant-time direct friendship checks.

## Limitations and possible extensions

- Random friendships are simulated and do not represent actual user behavior.
- This example models undirected, unweighted friendships.
- It could be extended with named users, friend recommendations, mutual-friend
  counts, or an adjacency-list version for large sparse networks.
