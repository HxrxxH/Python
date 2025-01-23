def validate_pattern(entered_pattern,correct_pattern):
    return entered_pattern==correct_pattern

correct_pattern=[1,2,3,6,9]
print("Enter your unlock pattern(eg:1,2,3,6,9)")
entered_pattern=list(map(int,input().split()))


if validate_pattern(entered_pattern,correct_pattern):
    print("phone unlocked")

else:
    print("Incorrect pattern , try again ")