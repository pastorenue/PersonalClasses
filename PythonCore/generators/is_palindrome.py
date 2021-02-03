import infinite_sequence

def is_palindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    
    if num == reversed_num:
        return True
    else:
        return False

# for i in infinite_sequence.infinite_sequence():
#     if is_palindrome(i):
#         print(i)
