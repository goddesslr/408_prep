import sys

print("="*60)
print("🚀 [系统启动] Python 阶段六：OOP 与工程架构极限沙盘")
print("="*60 + "\n")

# =====================================================================
# 战区一：import 寻址机制与物理隔离揭秘
# =====================================================================
print("【战区一：底层寻址雷达 (sys.path) 探测】")

# sys.path 是一个普通的 Python 列表，记录了 import 语句寻找文件的绝对物理路径
print("  [雷达扫描] 当你敲下 import numpy 时，系统将按以下顺序搜索：")
for i, path in enumerate(sys.path[:4]): # 只打印前 4 个防止刷屏
    print(f"    优先级 {i+1}: {path or '当前脚本所在目录'}")

print("\n  [黑客越权]：你可以通过 sys.path.append('/my/secret/dir') 强行篡改雷达！")
print("  这就是虚拟环境 (venv) 的底层原理：它强行把 .venv/site-packages 塞到了这个列表的最前面！\n")


# =====================================================================
# 战区二 & 三：类、__init__ 注入与封装协议
# =====================================================================
print("【战区二：类的实例化、__init__ 与 Name Mangling 封装】")

class CyberMech:
    def __init__(self, name, core_energy):
        # 此时 __new__ 已经开辟了内存，self 就是这块内存的首地址（如 0x1A2B）
        self.name = name                 # 公有属性 (Public)
        self.__core_energy = core_energy # 私有属性 (Private: 双下划线)
        print(f"  [机甲出厂] {self.name} 建造完毕，能量核心已物理锁死。")

    def attack(self):
        print(f"  [战术动作] {self.name} 消耗 10 点能量开火！剩余: {self.__core_energy - 10}")

# 1. 实例化动作
mech_01 = CyberMech("暴风赤红", 1000)

# 2. 企图访问私有变量的物理车祸
try:
    print(mech_01.__core_energy)
except AttributeError as e:
    print(f"  ❌ [绝对防御触发] 无法访问私有属性: {e}")

# 3. 架构师的降维打击：砸碎名称改写 (Name Mangling) 防爆玻璃
print(f"  🔓 [黑客强破] 强行读取底层改名后的真身: {mech_01._CyberMech__core_energy}\n")


# =====================================================================
# 战区四：继承、MRO 与 super() 的绝对单向代理
# =====================================================================
print("【战区三：MRO 线性化拓扑与 super() 代理】")

class BaseAI:
    def compute(self): print("  [BaseAI] 执行基础神经计算。")

class VisionAI(BaseAI):
    def compute(self):
        print("  [VisionAI] 提取图像特征 ->交由下级节点：", end="")
        super().compute() # 沿着 MRO 链条向后抛！

class LogicAI(BaseAI):
    def compute(self):
        print("  [LogicAI] 执行逻辑推演 ->交由下级节点：", end="")
        super().compute()

# 极其凶残的菱形多重继承
class UltimateAI(VisionAI, LogicAI):
    def compute(self):
        print("  [UltimateAI] 收到指令 ->交由下级节点：", end="")
        super().compute()

# 雷达扫描 C3 线性化 MRO 路径
print("  [底层 MRO 链条] UltimateAI.__mro__ :")
for node in UltimateAI.__mro__:
    print(f"    -> {node.__name__}")

print("\n  [物理执行链路] 调用 ultimate_ai.compute()：")
ai_boss = UltimateAI()
ai_boss.compute() 
# 极其震撼的结果：super() 让调用严格顺着 UltimateAI -> VisionAI -> LogicAI -> BaseAI 传递！
print()


# =====================================================================
# 战区五：鸭子类型 (Duck Typing) —— 抛弃血缘关系的信仰
# =====================================================================
print("【战区四：Duck Typing 结构子类型多态】")

class Samurai:
    def execute_strike(self): print("  [武士] 拔刀斩！")

class LaserCannon:
    def execute_strike(self): print("  [激光炮] 充能发射！")

class Banana:
    # 只要你身上有这个按钮，Python 解释器就敢按！绝不查户口本！
    def execute_strike(self): print("  [香蕉] 丢出一摊香蕉皮滑倒敌人！")

# 这是 C++ 绝对不敢写的函数：参数 entity 根本不指定类型！
def war_zone_deploy(entity):
    entity.execute_strike() # 盲按按钮！

print("  [无视血缘的无差别打击]：")
war_zone_deploy(Samurai())
war_zone_deploy(LaserCannon())
war_zone_deploy(Banana()) # 香蕉居然也能参战！这就是鸭子类型！

print("\n" + "="*60)

#v2版本

import sys

print("="*60)
print("🚀 [系统启动] Python OOP 底层机制与高阶基建沙盘")
print("="*60 + "\n")

# =====================================================================
# 战区一 & 三：类对象 vs 实例对象，与实例化过程 (__new__ 与 __init__)
# =====================================================================
print("【战区一 & 三：实例化生命周期与对象阶级】")

class CyberEngine:
    # 1. 真正的内存分配器 (Allocator)
    def __new__(cls, *args, **kwargs):
        print(f"  [1. __new__ 被触发] 正在向操作系统申请内存地皮，所属类: {cls.__name__}")
        # 调用最底层 object 的 __new__ 来真正划拨物理内存
        instance = super().__new__(cls) 
        print(f"  [1. __new__ 完成] 裸机甲已造出，物理门牌号: {id(instance)}")
        return instance # 必须把造好的内存地址扔出去，__init__ 才能接住！

    # 2. 状态初始化器 (Initializer)
    def __init__(self, core_temp):
        print(f"  [2. __init__ 被触发] 接收到裸机甲 (self 门牌号: {id(self)})，开始注入初始数据...")
        self.core_temp = core_temp
        print(f"  [2. __init__ 完成] 初始温度已设定为: {self.core_temp}℃\n")

# 物理动作：类本身也是个对象 (Class Object)！
print(f"  > [静态探针] CyberEngine 类图纸本身的物理门牌号: {id(CyberEngine)}")

# 物理动作：实例化 (Instantiation)
# 这一行代码，在底层极其暴力地先后触发了 __new__ 和 __init__！
engine_instance = CyberEngine(500) 


# =====================================================================
# 战区四：封装、名称改写与 @property 属性装饰器
# =====================================================================
print("【战区四：封装防线与 @property 物理拦截】")

class SecureBank:
    def __init__(self, initial_money):
        # 双下划线触发 Name Mangling (名称改写)，伪装成私有变量
        self.__vault_money = initial_money 
    
    # ---------------------------------------------------------
    # @property 装饰器：将方法伪装成属性！(Getter)
    # ---------------------------------------------------------
    @property
    def money(self):
        print("  [底层拦截 - Getter] 正在读取金库数据，执行安全审计...")
        return self.__vault_money

    # ---------------------------------------------------------
    # @money.setter：拦截赋值动作！(Setter)
    # ---------------------------------------------------------
    @money.setter
    def money(self, new_amount):
        print(f"  [底层拦截 - Setter] 企图将金库金额修改为 {new_amount}，执行安检...")
        if new_amount < 0:
            print("  ❌ [安检失败] 银行存款不能为负数！拦截非法物理突变！")
            raise ValueError("非法金额！")
        self.__vault_money = new_amount
        print("  ✅ [安检通过] 物理电荷修改成功！")

bank = SecureBank(1000)

# 1. 名称改写的视觉欺骗测试
print("  > 试图直接访问 bank.__vault_money ...")
try:
    print(bank.__vault_money)
except AttributeError as e:
    print(f"  ❌ 报错了: {e} (物理真相：编译器把它改名成了 _SecureBank__vault_money)")

# 2. @property 的极其优雅的拦截
print("\n  > 试图通过 bank.money 读取数据 (注意这里没有括号！)")
print(f"  > 读取结果: {bank.money}") # 看似是读属性，实则在底层执行了 money(self) 方法！

print("\n  > 试图通过 bank.money = -500 进行非法赋值 (注意这里是等号！)")
try:
    bank.money = -500 # 看似是赋值，实则在底层触发了 @money.setter 里的逻辑！
except ValueError:
    pass

print("\n  > 试图通过 bank.money = 5000 进行合法赋值")
bank.money = 5000
print(f"  > 最新金库数据: {bank.money}\n")


# =====================================================================
# 战区五：方法解析顺序 (MRO) 与 鸭子类型 (Duck Typing)
# =====================================================================
print("【战区五(模块4)：继承与 MRO 线性化法则】")

class BaseAI:
    def process(self): print("  [BaseAI] 执行基础计算。")

class VisionAI(BaseAI):
    def process(self):
        print("  [VisionAI] 提取视觉特征 -> 转交 super(): ", end="")
        super().process() # super 绝对不是指亲爹，而是指 MRO 链上的下一个节点！

class AudioAI(BaseAI):
    def process(self):
        print("  [AudioAI] 提取音频特征 -> 转交 super(): ", end="")
        super().process()

class OmniAI(VisionAI, AudioAI): # 菱形多重继承
    def process(self):
        print("  [OmniAI] 收到多模态任务 -> 转交 super(): ", end="")
        super().process()

# 极其冷酷的 MRO 链条扫描
print(f"  > OmniAI 的 MRO 寻址链条: {[cls.__name__ for cls in OmniAI.__mro__]}")
print("  > 开始执行 OmniAI().process():")
OmniAI().process() 
# 结论：super() 严格顺着 OmniAI -> VisionAI -> AudioAI -> BaseAI 执行，绝不重复！

print("\n【战区五(模块5)：鸭子类型 (无视血缘的物理调用)】")

class Tank:
    def fire(self): print("  [Tank] 发射 120mm 滑膛炮！")

class Sniper:
    def fire(self): print("  [Sniper] 发射 7.62mm 穿甲弹！")

class MagicWand:
    def fire(self): print("  [MagicWand] 发射大火球术！") # 它根本不是正规军，但它有 fire 按钮！

# 这是一个极其狂妄的函数：不检查类型！只要有 fire 按钮我就敢按！
def battlefield_attack(unit):
    unit.fire()

print("  > 只要能开火(拥有 fire 方法)，管你是坦克还是魔法棒，统统上战场！")
battlefield_attack(Tank())
battlefield_attack(Sniper())
battlefield_attack(MagicWand()) # 鸭子类型的终极体现！

print("\n=======================================================")

#拦截机制

import sys

print("="*60)
print("🚀 [系统启动] 属性拦截与海关安检仪：物理沙盘")
print("="*60 + "\n")

class Student:
    def __init__(self):
        # 初始状态，金库里放着绝对安全的纯净电荷 100
        self.__score = 100 
        print(f"  [金库初始化] 当前真实分数已锁定为: {self.__score}")

    @property
    def score(self):
        # 读拦截：获取数据
        return self.__score

    @score.setter
    def score(self, new_value):
        # 写拦截：海关安检大门！
        # 每当外部出现 stu.score = xxx 时，xxx 就会作为 new_value 被传到这里！
        print(f"  🛂 [海关安检] 收到外部传入的数据: {new_value}，开始扫描...")
        
        if new_value < 0:
            # 异常输入：拉响警报，强行切断控制流！
            print("  🚨 [警报] 发现负数炸弹！拦截成功，当场击毙！数据未受污染！")
            raise ValueError("分数绝对不能为负数！")
        else:
            # 合法输入：放行，亲自拿着数据进入金库，物理覆盖旧数据！
            print(f"  ✅ [放行] 数据合法！正在物理抹杀旧数据，写入新数据 {new_value}...")
            self.__score = new_value

# =====================================================================
# 实战演习
# =====================================================================
stu = Student()
print("-" * 50)

# 场景 1：合法修改 (测试 100 -> 99 的物理覆盖)
print("【场景 1：输入合法的 99】")
# 看似普通的等号赋值，实则瞬间触发了 @score.setter 安检仪！
stu.score = 99 
print(f"  [验尸报告] 此时系统中的真实分数是: {stu.score} (原本的 100 已被彻底抹杀！)\n")

# 场景 2：非法修改 (测试防御机制)
print("【场景 2：输入非法的负数炸弹 -50】")
try:
    stu.score = -50 
except ValueError as e:
    print(f"  [系统日志] 捕获到安检处抛出的击毙报告: {e}")

print(f"  [最终验尸报告] 此时系统中的真实分数依然是: {stu.score} (99 得到了完美的物理保护！)")

print("\n" + "="*60)

#self作用

import sys

print("="*60)
print("🚀 [系统启动] self 的多维工程角色与物理基建沙盘")
print("="*60 + "\n")

# =====================================================================
# 外部全局基建：模拟一个宏大的指挥中心
# =====================================================================
class CommandCenter:
    registered_mechs = [] # 记录所有注册机甲的门牌号

    @classmethod
    def register(cls, mech_instance):
        cls.registered_mechs.append(mech_instance)
        print(f"  [指挥中心] 接收到钥匙！成功注册机甲: {mech_instance.name}")

    @classmethod
    def broadcast_attack(cls):
        print("\n  [指挥中心] 警报！向所有注册机甲下达最高开火指令！")
        for mech in cls.registered_mechs:
            mech.fire() # 指挥官拿着之前存好的 self (备用钥匙) 远程遥控开火！

# =====================================================================
# 核心战区：机甲图纸
# =====================================================================
class MechArmor:
    def __init__(self, name):
        # 【角色 1：状态固化锚点】
        # 强行把传入的局部变量 name，焊死在机甲堆区的肚子里！
        self.name = name 
        self.ammo = 0
        self.is_ready = False
        print(f"  [建造完毕] {self.name} 出厂。门牌号: {id(self)}")

        # 【角色 4：身份的跨维移交】
        # 极其震撼的动作：把自己（self）当成一份礼物/钥匙，交到外面的指挥中心！
        CommandCenter.register(self)

    # ---------------------------------------------------------
    # 内部动作齿轮
    # ---------------------------------------------------------
    def load_ammo(self, amount):
        self.ammo += amount
        print(f"  [{self.name}] 装填弹药 {amount} 发。当前弹药: {self.ammo}")
        # 【角色 3：链式调用的基石】
        # 动作干完了，把自己的真身门牌号再次抛出去！
        return self 

    def enable_safety_off(self):
        self.is_ready = True
        print(f"  [{self.name}] 物理保险已解除！")
        # 【角色 3：链式调用的基石】
        return self 

    def fire(self):
        # 【角色 2：内部齿轮的传动轴】
        # 在开火前，机甲必须自己检查自己的状态。
        # 它通过 self.check_status() 唤醒了自己肚子里的另一个函数！
        if self.check_status():
            self.ammo -= 1
            print(f"  💥 [{self.name}] 开火轰炸！剩余弹药: {self.ammo}")

    def check_status(self):
        """内部安检雷达"""
        if not self.is_ready:
            print(f"  ❌ [{self.name}] 警告：保险未解除，拒绝开火！")
            return False
        if self.ammo <= 0:
            print(f"  ❌ [{self.name}] 警告：弹药耗尽！")
            return False
        return True


# =====================================================================
# 终极物理演习
# =====================================================================
print("\n【战区演习：链式狂飙与身份移交】")

# 1. 建造机甲（触发 __init__，并自动将 self 移交给指挥中心）
mech_a = MechArmor("暴风赤红")
mech_b = MechArmor("危险流浪者")

print("\n  >>> 测试链式调用 (Fluent Interface) <<<")
# 2. 极其优雅的链式操作！
# 因为 load_ammo 执行完 return 了 self，所以紧接着可以点出 .enable_safety_off()！
# 这种写法在 Pandas 洗数据和 PyTorch 设置模型时是绝对的工业标准！
mech_a.load_ammo(10).enable_safety_off()

mech_b.load_ammo(5).enable_safety_off()

print("\n  >>> 测试指挥中心远程遥控 (身份移交的威力) <<<")
# 3. 指挥中心发威
# 刚才在 __init__ 里移交的 self 钥匙，现在派上用场了！
CommandCenter.broadcast_attack()

print("\n" + "="*60)