# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * i)
# for i in range(n-1, 0, -1):
#     print(" " * (n-i) + "*" * i)
# Pyramid star pattern

rows = 5

# Increasing part
for i in range(1, rows + 1):
    print("*" * i)

# Decreasing part
for i in range(rows - 1, 0, -1):
    print("*" * i)
