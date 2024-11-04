numbers = [34, 5, 60, 24, 5, 99]
print(numbers)

def bubble_sort(n):
    steps = 0
    for j in range(0, len(n)-1):
        for i in range(0, len(n)-1):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]

                steps += 1

    print(n)
    print(str(steps) + " steps to complete.")

bubble_sort(numbers)