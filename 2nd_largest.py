s = input("Enter the any string:- ")
largest = -1
second_largest = -1
for ch in s:
   if '0' <= ch <= '9':
            num = ord(ch) - ord('0')

            # Update largest and second largest manually
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num

print(second_largest)