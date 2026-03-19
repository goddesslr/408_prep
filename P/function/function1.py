# ====== Python 函数物理引擎沙盘 ======

# =====================================================================
# 战区一：函数的物理铸造与隐式打包
# =====================================================================
print("【第一战区：函数的物理铸造与内存分配】")

# 1. 'def' 是执行语句！此时在内存中开辟了一块代码区，名为 'analyze_data'
def analyze_data(data):
    # 这是局部作用域（房间内）
    length = len(data)
    max_val = max(data)
    
    # 物理动作：看似返回了两个值，实际上底层造了一个 Tuple (length, max_val) 扔出去
    return length, max_val 

# 2. 函数也是个物理对象！我们可以查它的门牌号和类型！
print(f"  函数真身的门牌号: {id(analyze_data)}")
print(f"  函数的物理类型: {type(analyze_data)}")

# 3. 拉下电闸执行，并接收隐式的元组拆包
my_data = [10, 50, 20, 99, 5]
# 右边扔出一个包裹 (5, 99)，左边的 l 和 m 瞬间将包裹撕开并认领
l, m = analyze_data(my_data) 
print(f"  运行结果 -> 长度: {l}, 最大值: {m}\n")
print("-" * 50)


# =====================================================================
# 战区二：参数注入阀门（位置 vs 关键字）
# =====================================================================
print("【第二战区：参数的精准制导注入】")

def build_neural_layer(in_nodes, out_nodes, activation="ReLU"):
    print(f"  [构建网络层] 输入节点:{in_nodes} | 输出节点:{out_nodes} | 激活函数:{activation}")

# 方式A：传统位置传参（容易记错顺序）
print("  > 方式 A: 位置传参")
build_neural_layer(128, 256, "Sigmoid")

# 方式B：工业级关键字传参（无视顺序，绝对精准，AI框架首选！）
print("  > 方式 B: 关键字传参 (顺序彻底打乱也绝对安全)")
build_neural_layer(activation="Tanh", out_nodes=64, in_nodes=32)
print("-" * 50)


# =====================================================================
# 战区三：💣 史诗级灾难 —— 默认参数的可变陷阱
# =====================================================================
print("【第三战区：默认参数陷阱物理验尸】")

# 💀 灾难版本：厂房门口放了一个永远不消失的“共享盒子” []
def bad_append(item, data_list=[]):
    data_list.append(item)
    return data_list

print("  [执行错误函数]")
res1 = bad_append("苹果")
print(f"  第 1 次调用后: {res1}  (门牌号: {id(res1)})")

res2 = bad_append("香蕉")
print(f"  第 2 次调用后: {res2}  (门牌号: {id(res2)})")
print("  !!! 灾难发生 !!! 它们用的居然是同一个物理盒子！\n")


# 🛡️ 工业级解药：使用 None 作为占位符，在厂房【内部】现造盒子！
def good_append(item, data_list=None):
    if data_list is None:
        data_list = [] # 每次调用，在函数内部划拨一块全新的内存地皮
    data_list.append(item)
    return data_list

print("  [执行工业级安全函数]")
safe1 = good_append("苹果")
print(f"  第 1 次调用后: {safe1}  (门牌号: {id(safe1)})")

safe2 = good_append("香蕉")
print(f"  第 2 次调用后: {safe2}  (门牌号: {id(safe2)})")
print("  [防线生效] 它们被完美隔离在了不同的物理盒子里！")

print("\n=======================================================")