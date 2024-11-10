#Q.. 1729 কে রামানুজন সংখ্যা বলা হয় কেন?
# =>  1729, হার্ডি-রামানুজন সংখ্যা হল ক্ষুদ্রতম সংখ্যা যা দুটি ভিন্ন ভিন্ন কিউবের যোগফল হিসেবে দুটি ভিন্ন উপায়ে প্রকাশ করা যায় । 1729 হল 10 এবং 9-এর কিউবের সমষ্টি - 10-এর কিউব হল 1000 এবং 9-এর কিউব হল 729; দুটি সংখ্যা যোগ করলে ফলাফল 1729।

for a in range(1,31,1):
    for b in range(1,31,1):
        for c in range(1,31,1):
            for d in range(1,31,1):
                if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
                    left=a*a*a+b*b*b
                    right= c*c*c+d*d*d
                # if(left == right):
                #     print(f"{a},{b},{c},{d} , is ramanujan number")
                # else:
                #     print(f"{a},{b},{c},{d} , is not a ramanujan number")
if(left == right):
    print(f"{a},{b},{c},{d} , is ramanujan number")
else:
    print(f"{a},{b},{c},{d} , is not a ramanujan number")