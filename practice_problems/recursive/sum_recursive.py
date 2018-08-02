def sum_recursive(current_number, accumulated_sum):
    if current_number == 11:
        return accumulated_sum
    return sum_recursive(current_number + 1, accumulated_sum + current_number)

print(sum_recursive(1, 0))
