#include <iostream>
using namespace std;

// 1. 【造户口本/接口】：定义一个抽象基类 (Abstract Base Class)
// 这就是 C++ 中的接口！它强制要求所有儿子必须实现 log 按钮。
class ILogger {
public:
    virtual void log(string message) = 0; // 纯虚函数 (只定义按钮，不写内部逻辑)
    virtual ~ILogger() {} // 虚析构函数 (释放内存防泄漏的基建)
};

// 2. 【继承户口本】：FileLogger 必须明确继承 ILogger
class FileLogger : public ILogger {
public:
    void log(string message) override {
        cout << "写入硬盘: " << message << endl;
    }
};

// 3. 【继承户口本】：DatabaseLogger 必须明确继承 ILogger
class DatabaseLogger : public ILogger {
public:
    void log(string message) override {
        cout << "插入数据库: " << message << endl;
    }
};

// 4. 【静态安检大门】：函数参数必须锁定为“父类指针”或“父类引用”！
// 如果你不写 ILogger*，而写具体的类，多态瞬间失效！
void system_record(ILogger* logger_device, string text) {
    // 物理动作：通过虚函数表 (V-Table) 在运行时寻找真实的按钮并按下
    logger_device->log(text); 
}

int main() {
    FileLogger f_log;
    DatabaseLogger db_log;

    // 实战验证：因为它们都继承了 ILogger，所以可以通过安检门
    system_record(&f_log, "服务器启动");
    system_record(&db_log, "用户登录");

    return 0;
}