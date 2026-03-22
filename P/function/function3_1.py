import inspect

print("="*60)
print("🚀 [系统启动] Python 函数内省 (Introspection) 透视仪")
print("="*60 + "\n")

###### 构造一个包含所有复杂特征的函数实体

def core_engine(target_ip: str, port: int = 8080, *, auth_token: str = "NONE") -> bool:
    """
    建立底层核心通信连接。
    (此字符串将被刻入 __doc__ 抽屉)
    """
    connection_status = True # 局部变量
    return connection_status

print("【学术内省：元数据抽屉强行读取】")

###### 1. 标识符与说明书

print(f"  __name__ (标识符) : {core_engine.__name__}")
print(f"  __doc__  (说明书) : {core_engine.__doc__.strip()}")

###### 2. 默认值地雷区

print(f"  __defaults__   (定位参数默认值)   : {core_engine.__defaults__}")
print(f"  __kwdefaults__ (强制关键字默认值) : {core_engine.__kwdefaults__}")

###### 3. 类型提示安检门 (FastAPI 核心机制)

print(f"  __annotations__(类型提示字典)     : {core_engine.__annotations__}")

###### 4. 深渊字节码对象

code_object = core_engine.__code__
print(f"  __code__.co_varnames (局部变量表) : {code_object.co_varnames}")

print("\n" + "="*60)

