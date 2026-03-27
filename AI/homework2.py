count=0
def test(n,s1,s2,s3):
    global count
    if n == 1 :
        print(f"{s1}->{s3}")
        count+=1
        return
    test(n-1,s1,s3,s2)
    count+=1
    print(f"{s1}->{s3}")
    test(n-1,s2,s1,s3)
n = int(input("输入汉诺塔的层数为："))
test(n,'A','B','C')
print(f"汉诺塔层数为{n},A到C总移动次数为{count}")
