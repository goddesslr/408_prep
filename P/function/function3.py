import sys
import math
from datetime import datetime
r=10
area = math.pi*math.pow(r,2)
print(f"面积为{area:.2f}")

current_time = datetime.now()
print(f"当前系统时间时{current_time}")
#推导式的用法
row_data=[{'name':'A','grade':90},{'name':'B','grade':58},{'name':'C','grade':68}]
pass_students=[student['name'] for student in row_data if student['grade']>=60]

print(f"考试通过的学生名单：{pass_students}")

student_dict={student['name']:student['grade'] for student in row_data}

print(f"成绩单是{student_dict}")

#异常处理机制
def test(number):
    try:
        print(f"正在进行{number}被1000除的计算")
        result=1000/number
    except ZeroDivisionError as a:
        print(f"遇到除0异常：{a}")
    else:
        print(f"计算成功结果为{result}")
    finally:
        print("释放物理资源")
test(2)
test(0)

#上下文管理器与IO
file_name='number_1.txt'
with open(file_name,'w',encoding='utf-8') as f:
    f.write("通过上下文管理器导入文件\n")
    f.write("结束后自动关闭文件")
    print(f"成功向硬盘写入文件：{file_name}")
 

print(f"检测是否关闭了文件，结果：{f.closed}")

print("【战区四：文件 I/O 权限模式大满贯】")

file_name = "test_sandbox_output.txt"

# 模式 1: "w" (Write) - 极其暴力的物理覆盖！如果文件存在，瞬间清零！
print("  > 正在以 'w' (覆盖写) 模式打开...")
with open(file_name, "w", encoding="utf-8") as f:
    f.write("这是第一行数据 (W模式写入)。\n")
    # f 不是 open 本身，它是 TextIOWrapper 文件对象，write 是它的普通方法。

# 模式 2: "a" (Append) - 游标瞬间定位到末尾，追加电荷！
print("  > 正在以 'a' (追加写) 模式打开...")
with open(file_name, "a", encoding="utf-8") as f:
    f.write("这是第二行数据 (A模式追加，绝对不破坏第一行)。\n")

# 模式 3: "r" (Read) - 只读模式，获取文本数据
print("  > 正在以 'r' (只读) 模式提取数据...")
with open(file_name, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"  [读取到的纯文本]:\n{content}")

# 模式 4: "rb" (Read Binary) - 剥离人类滤镜，读取原始 01 字节流！
print("  > 正在以 'rb' (纯物理二进制) 模式提取数据...")
with open(file_name, "rb") as f:
    binary_data = f.read()
    print(f"  [读取到的底层 Bytes]: {binary_data}\n")


# =====================================================================
# 战区五：揭秘上下文协议 (自己造一个 with 拦截器！)
# =====================================================================
print("【战区五：上下文管理协议 (绝对不止 open 独有)】")

class MySecurityDoor:
    """任何实现了 __enter__ 和 __exit__ 的类，都是合法的上下文管理器！"""
    
    def __enter__(self):
        print("  🔒 [__enter__ 触发] 安全门已锁死，拦截外部干扰，进入无菌实验室！")
        return "安全许可证" # 这个返回值会交给 as 后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  🔓 [__exit__ 触发] 实验结束，安全门自动解锁，资源物理回收！")
        # 即使 with 块里发生了崩溃，这里也 10000% 绝对会执行！

# 亲自使用自己打造的上下文管理器机甲
with MySecurityDoor() as license:
    print(f"  🧪 正在实验室内进行高危操作... (已获取凭证: {license})")

        
