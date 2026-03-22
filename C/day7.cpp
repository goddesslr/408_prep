#include <iostream>
#include <cstdlib>

using namespace std;

// 1. 全局数据区 (.data & .bss)
int global_init = 42;      // .data 段
int global_uninit;         // .bss 段 (OS 会自动填 0)

// 2. 只读区 (.rodata)
const int global_const = 99;

// 函数机器码存放在 .text 段
void dummy_function() {}

int main() {
    cout << "====== OS 虚拟内存物理拓扑测绘雷达 ======\n\n";
    // 3. 局部栈区 (Stack Segment) - 向下生长
int stack_var1 = 10;
int stack_var2 = 20;

// 4. 动态堆区 (Heap Segment) - 向上生长
int* heap_var1 = new int(100);
int* heap_var2 = new int(); // 带括号：强制清零打扫

cout << "【高纬度空间：栈区 (Stack)】 -> 极高地址，向下生长" << endl;
cout << "  局部变量1 地址: " << &stack_var1 << endl;
cout << "  局部变量2 地址: " << &stack_var2 << " (地址变小)\n" << endl;

cout << "【荒野空间：堆区 (Heap)】 -> 较低地址，向上生长" << endl;
cout << "  动态地皮1 地址: " << heap_var1 << endl;
cout << "  动态地皮2 地址: " << heap_var2 << " (地址变大)\n" << endl;

cout << "【永固空间：数据区 (.data / .bss)】 -> 低地址" << endl;
cout << "  已初始化全局变量 (.data) : " << &global_init << endl;
cout << "  未初始化全局变量 (.bss)  : " << &global_uninit << "\n" << endl;

cout << "【深渊只读区：.rodata 与 .text】 -> 极低地址，绝对只读" << endl;
cout << "  const 全局常量 (.rodata) : " << &global_const << endl;
cout << "  函数执行代码 (.text)     : " << (void*)dummy_function << "\n" << endl;

// 清理堆区内存，防止 Memory Leak
delete heap_var1;
delete heap_var2;

return 0;
}