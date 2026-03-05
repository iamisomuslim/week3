#Sum of Even Numbers
total=0
count=0
num = int(input("Enter a positive integer: "))
if num<0:
    print("Why you didnot enter a positive integer brooooo!")
else:
    for num in range(0,num+1):
        if num % 2 == 0:
            total+=num
            count+=1
        else:
            continue
    print(f"Sum of even numbers 1 to {num}: {total}")
    print(f"Count of numbers: {count}")