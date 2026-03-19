#include <iostream>
using namespace std;

int main() {
    // 1. 打印一句霸气的宣言
    cout << "Hello, AI Master of RUC!" << endl;

    // 2. 验证一下指针（考研408最难点，我们先感受一下）
    int a = 100;
    int *p = &a; // p 是一个指针，指向 a 的地址

    cout << "Value of a: " << a << endl;
    cout << "Address of a: " << p << endl;
    cout << "Value via pointer: " << *p << endl;

    return 0;
}