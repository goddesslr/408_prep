import sys
import time

#第一部分复盘：函数定义，内存位置的确定及传参验证
#定义函数:
def test1(weight,height,age=20):
    print("bmi计算引擎启动")
    bmi = weight/(height*height)
    GPA=3.88
    Uni="RUC"
    return GPA,Uni,bmi
#打印函数内存位置:
address=id(test1)
print(f"函数内存位置为:{address}")
w = input("请输入您的体重（kg）：")
h = input("请输入您的身高（米）:")
#位置传参测试
bmi_result=test1(float(w),float(h))
bmi_result2=test1(float(h),float(w))
bmi_result3=test1(height=float(h),weight=float(w))

print(f"正确位置传参结果为{bmi_result},错误位置传参结果为{bmi_result2},关键字传参结果为{bmi_result3},各自分别的内存位置为：{id(bmi_result)},{id(bmi_result2)},{id(bmi_result3)}")
print(f"各结果对应的类型为{type(bmi_result)},{type(bmi_result2)},{type(bmi_result3)}")

#拆解返回元组

G,U,BMI=bmi_result
print(f"所在大学为：{U}")
print(f"成绩为{G}")
print(f"BMI为:{BMI}")

#验证默认值陷阱即列表，字典等可变量默认机制

def test2(lx,nation=[]):
    nation.append(lx)
    return nation

#测试不清除默认值：

result1=test2('China')
print(f"第一次输入后列表为：{result1}，地址为：{id(result1)}")
result2=test2('America')
print(f"第二次输入后列表为:{result2}，地址为：{id(result2)}")

#正确做法：清除默认值之后：

def test2_v2(lx,nation=None):
    if nation is None:
        nation=[]
    nation.append(lx)
    return nation

result3=test2_v2('China')
print(f"第一次输入后列表为：{result3}，地址为：{id(result3)}")
result4=test2_v2('America')
print(f"第一次输入后列表为：{result4}，地址为：{id(result4)}")

#测试高级传参*args **kwargs：

def test3(*h,**k):
    print(f"元组传参为{h}")
    print(f"字典传参为{k}")

test3('64kg','a','b',76,'76','v',Kwj=10,kyj='2',kjj='L')

io1=[1,2,4]
io2={"K":'yy',"Y":'kk'}    
test3(64,*io1,**io2)  


#全局变量与局部变量
TEST=1000
def test4():
    TEST=200
    TEST += 100
    return TEST
test4()
print(f"函数作用后，TEST变为{TEST}")
def test5():
    global TEST
    print(f"全局变量TEST为：{TEST}")
    TEST+=100
test5()
print(f"函数作用后，TEST变为{TEST}")

#__name__的隔离作用

print(f"当前系统分配给文件的名牌__name__为{__name__}")

if __name__ == '__main__':
    print("正在测试中.....")
else:
    pass

print("本次沙盘到此结束")   


  