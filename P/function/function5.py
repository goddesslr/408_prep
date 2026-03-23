class FileLogger:
    # 我没有任何父类，我只是个普通类
    def log(self, message):
        print(f"写入硬盘: {message}")

class DatabaseLogger:
    # 我也没有任何父类，但我恰好也有个叫 log 的按钮
    def log(self, message):
        print(f"插入数据库: {message}")

# 这是一个极其狂妄的函数，它不检查类型！
def system_record(logger_device, text):
    # 物理动作：不查户口本，闭着眼睛直接按 log 按钮！
    logger_device.log(text)

# 实战验证：
f_log = FileLogger()
db_log = DatabaseLogger()

# 系统完美运行！这就是鸭子类型！只要你有 log 按钮，我就认你！
system_record(f_log, "服务器启动")
system_record(db_log, "用户登录")


#self的用法举例：

import sys

print("="*60)
print("🚀 [系统启动] self 的栈帧生灭与绝对第一坑位沙盘")
print("="*60 + "\n")

# =====================================================================
# 战区一：证明 self 的死而后生 (栈帧的物理隔离)
# =====================================================================
print("【战区一：self 纸条的湮灭与重生】")

class CyberMech:
    def __init__(self):
        # 此时在一个临时的 __init__ 栈帧里
        print("  [__init__ 栈帧存活] 拿到了一张名叫 self 的纸条！")
        print(f"  [物理验证] 这张纸条指向的机甲地址是: {id(self)}")
        self.ammo = 100
        print("  [__init__ 即将结束] 帐篷即将坍塌，当前的 self 纸条即将被物理烧毁(湮灭)！\n")

    def fire(self):
        # 此时在一个全新的 fire 栈帧里
        print("  [fire 栈帧存活] 上一张纸条已经灰飞烟灭！现在系统发了一张全新的纸条，依然叫 self！")
        print(f"  [物理验证] 这张新纸条指向的机甲地址依然是: {id(self)}")
        self.ammo -= 10
        print(f"  [开火] 通过新纸条成功遥控了那台永固的机甲！剩余弹药: {self.ammo}")


# 物理验尸：
mech = CyberMech()
mech2=CyberMech()
mech.fire()
print(f"类的地址是{id(CyberMech)}")
# 结论：机甲实体在堆区里始终是同一个 (id 完全一样)，但不同函数里的 self 是生生死死的独立局部变量！


# =====================================================================
# 战区二：大逆不道的命名实验 (验证编译器只认“第一坑位”)
# =====================================================================
print("\n【战区二：打破 PEP 8，篡改 self 的名字】")

class RebelMech:
    # 架构师极其疯狂的实验：我偏不叫 self，我叫 me！
    def __init__(me, name):
        # 编译器无视了 me 这个名字，依然强行把机甲地址灌进了第一个坑位！
        me.name = name 
        print(f"  [叛逆初始化] 成功使用 'me' 作为第一形参！机甲名: {me.name}")

    # 我在另一个函数里，甚至换成 Java/C++ 的专属词汇 this！
    def attack(this):
        print(f"  [叛逆开火] 成功使用 'this' 作为第一形参！{this.name} 正在攻击！")
        
    # 甚至用最离谱的名字作为第一个参数！
    def defend(whatever_you_want_to_call_it):
        print(f"  [叛逆防御] 成功使用 'whatever' 名字！{whatever_you_want_to_call_it.name} 开启护盾！")

# 物理验尸：
rebel = RebelMech("尤里复仇号")

rebel.attack()
rebel.defend()

print("\n" + "="*60)
print("🏁 [架构师总结]：")
print("1. 物理层面上，类方法的第一个参数叫什么都可以，解释器只认【物理顺序的第一个位置】！")
print("2. 工程层面上，【绝对、永远】只能把它写成 self，这是不可触犯的工业铁律！")
print("="*60)

class NeuralNetwork:
    def extract_features(self, image_data):
        print("  [动作 1] 正在提取特征...")
        # ⚠️ 局部变量 temp_result：没有 self！
        # 只要这个函数结束，它会瞬间物理湮灭！
        temp_result = image_data * 2 
        
        # 🛡️ 状态固化：加了 self！
        # 将中间结果焊死在堆区对象的物理抽屉里！
        self.feature_map = temp_result + 10 
        print(f"  [动作 1 结束] 特征 {self.feature_map} 已固化至 self 内存！")

    def classify(self):
        print("  [动作 2] 开始分类...")
        # 跨越生死！哪怕 extract_features 的栈帧已经湮灭，
        # 我们依然能通过 self 从堆区把数据挖出来！
        final_score = self.feature_map * 100 
        print(f"  [分类成功] 最终得分: {final_score}")

# 实战演练
model = NeuralNetwork()
model.extract_features(5) # 计算出 20 并存入 self
model.classify()          # 成功取出 20 进行下一步计算

class Artillery:
    def __init__(self):
        self.ammo = 0

    def load_ammo(self):
        print("  [内部齿轮运转] 成功装填 1 发穿甲弹！")
        self.ammo += 1

    def fire(self):
        # 🚨 致命错误演示：如果这里直接写 load_ammo()，系统会报 NameError！
        # 必须通过 self 这个物理传动轴，唤醒同一个类内部的其他方法！
        print("  [接收指令] 准备开火，启动装填程序...")
        self.load_ammo() 
        
        if self.ammo > 0:
            print("  💥 [开火] 轰炸目标！")
            self.ammo -= 1

# 实战演练
cannon = Artillery()
cannon.fire() # 外部只调了 fire，但在内部，fire 通过 self 成功驱动了 load_ammo！

class DummyTensor:
    def __init__(self, name):
        self.name = name
        self.device = "CPU"
        self.is_training = False

    def train(self):
        self.is_training = True
        print(f"  [{self.name}] 切换至: 训练模式")
        # ⚡ 绝对核心：干完活，把自己的内存首地址重新抛出去！
        return self 

    def to_cuda(self):
        self.device = "GPU"
        print(f"  [{self.name}] 物理转移至: CUDA 显存")
        return self # 再次把门牌号抛出去！

    def float(self):
        print(f"  [{self.name}] 数据精度转换: Float32")
        return self # 抛出！

# 实战演练：大厂最经典的链式狂飙！
tensor = DummyTensor("图像矩阵")
print(">>> 开始执行神级链式调用 <<<")
# 一口气完成三个高危物理动作！
tensor.train().to_cuda().float() 

# 全局层面的控制系统
class GlobalEventLoop:
    active_listeners = [] # 存储所有交出备用钥匙的机甲
    
    @classmethod
    def register(cls, obj_reference):
        cls.active_listeners.append(obj_reference)
        print(f"  [系统广播] 已成功收录对象钥匙！")

    @classmethod
    def trigger_all(cls):
        print("\n  [系统广播] 发动全局唤醒！")
        for obj in cls.active_listeners:
            obj.wake_up() # 指挥中心拿着 self 钥匙，远程强行调用对象的方法！

# 机甲实体
class AutoBot:
    def __init__(self, serial_num):
        self.serial_num = serial_num
        print(f"  [出厂] 汽车人 {self.serial_num} 已激活。")
        # ⚡ 绝对核心动作：跨维移交身份！
        # 把自己 (self) 打包成一个参数，扔给外面的系统！
        GlobalEventLoop.register(self)

    def wake_up(self):
        print(f"  🤖 汽车人 {self.serial_num} 收到全局指令，变形出发！")

# 实战演练
# 只是单纯地实例化对象
bot1 = AutoBot("擎天柱")
bot2 = AutoBot("大黄蜂")

# 指挥中心发动总攻！
# bot1 和 bot2 根本没有自己调用 wake_up，是系统拿着它们的 self 钥匙远程按下的！
GlobalEventLoop.trigger_all()


print("="*60)
print("接下来验证mro顺序")
print("="*60)

class A:
    def say(self): print("  [到达顶点 A]")


class F(A):
    def say(self):
        print("[到达F]->准备调用super")
        super().say()
        
class B(A):
    def say(self): 
        print("  [到达 B] -> 准备调用 super")
        super().say()

class C(A):
    def say(self): 
        print("  [到达 C] -> 准备调用 super")
        super().say()
        

class D(F,C,B): # D 同时继承 B 和 C,F
    def say(self): 
        print("  [到达 D] -> 准备调用 super")
        super().say()

# 1. 启动 MRO 测绘雷达
print("【MRO 物理寻址链条】:")
print([cls.__name__ for cls in D.__mro__])
# 打印出: ['D', 'B', 'C', 'A', 'object'] (这就是那条绝对单行道！)

# 2. 观察 super() 极其诡异的跳跃动作
print("\n【多重继承的 super() 跳跃】:")
d = D()
d.say()

# 架构师验尸报告：
# 1. D 调用 super() -> 去了 B (合理，B 是第一个爹)
# 2. B 调用 super() -> 去了 C！
# 震惊吗？B 的亲爹明明是 A，但它竟然跳到了 C！
# 物理真相：因为在 MRO 链条 ['D', 'B', 'C', 'A'] 中，B 的下一个节点是 C！这就是 super 的绝对真相！
#参数和填入的顺序有关系
