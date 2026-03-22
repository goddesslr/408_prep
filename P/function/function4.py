class Soldier:
    pass # 只要这句话执行完毕，内存里就真实存在了一台印钞机！

# 验证类对象的物理存在 (它有自己的物理门牌号，证明它绝非虚无！)
print(id(Soldier)) # 例如输出: 140735328912304

# 造出两张钞票 (实例对象)
s1 = Soldier()
s2 = Soldier()
print(id(s1))
print(id(s2))
# 编译器自动为实例写好的底层属性：
print(s1.__class__) # 输出: <class '__main__.Soldier'> (指向那台实体印钞机)
print(s1.__dict__)  # 输出: {} (自己的数据抽屉，目前是空的)

class DatabaseConnection:
    # 类级别的变量（长在印钞机本身身上的抽屉），用来记录“地皮是否已经买过了”
    _instance= None 

    # 1. 拦截内存分配器！
    def __new__(cls, *args, **kwargs):
        # 物理安检：如果 _instance 是空的，说明还没买过地皮
        if cls._instance is None:
            print("[底层动作] 第一次呼叫，向系统申请物理内存...")
            # 呼叫最底层的 object 真正去买地皮，并把门牌号存起来
            cls._instance = super().__new__(cls)
        else:
            print("[底层动作] 发现已有内存！拒绝申请新地皮，返回旧门牌号！")
        
        # 无论如何，返回的永远是同一张门牌号！
        return cls._instance

    # 2. 初始化器 (接收 __new__ 传过来的门牌号 self)
    def __init__(self):
        self.connected = True

# --- 物理车祸/奇迹验证 ---
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"DatabaseConnection的地址是{id(DatabaseConnection)}")
print(f"db1 的物理门牌号: {id(db1)}")
print(f"db2 的物理门牌号: {id(db2)}")

# 1. 继承体系：Father 是父类，Son 继承 Father
class Father:
    def __init__(self):
        self.money = 100       # 普通变量
        self.__secret = "存折" # 伪私有变量

class Son(Father):
    def __init__(self):
        # 继承的体现：呼叫父类的初始化，把父类的家产搬进我的内存
        super().__init__()
        
        # 企图覆盖同名变量！
        self.money = 0         
        self.__secret = "漫画" 

# --- 物理验尸 ---
s = Son()
# 查看对象最底层的物理抽屉（__dict__）
print(s.__dict__)
# 输出揭秘: {'money': 0, '_Father__secret': '存折', '_Son__secret': '漫画'}

# 架构师判决：
# 1. 普通的 money 被子类的 0 无情物理覆盖了！
# 2. 父类的 __secret 和子类的 __secret 因为名称改写，变成了两个独立的物理盒子，完美共存！

class Student:
    
    def __init__(self):
        self.__score = 100
    
    # 1. 拦截读取 (Getter)
    @property
    def score(self):
        return self.__score
    
    # 2. 拦截写入 (Setter)
    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("分数不能为负！")
        self.__score = value
        
    # 3. 拦截物理删除 (Deleter) -> 新知识点！
    @score.deleter
    def score(self):
        print("[底层警告] 企图删除核心数据！已被拦截，强行将分数置为 0！")
        self.__score = 0

stu = Student()
stu.score = 10  # 触发 Setter
print(stu.score) # 触发 Getter

# 物理动作：企图从内存中删除属性
del stu.score    # 触发 Deleter！
print(stu.score) # 打印结果为 0，系统存活！
