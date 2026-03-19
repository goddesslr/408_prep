#include <iostream>
using namespace std;
extern const int max_level=100;
 int main(){
    //定义const变量看看能否更改const常量来改变值
    int a = 10;
    const int &p1 = a;
    int p2 = p1;
    //const int b;
    //p1=p1+1或者p1=20都会报错
    p2=20;
    //用普通引用修改值const变量值也会改变
    cout<<"const变量此时值为"<<p1<<"\n";
    //验证底层临时量促使的跨变量引用
    float c = 3.659;
    const int& d = c;
    cout<<"d的真实地址为"<<&d<<"d的值为"<<d<<"c的地址为"<<&c<<"c的值为"<<c<<"\n";
    //验证指向常量的指针不能改变真实值但是可以储存不同地址
    const int* p3 = &a;
    cout<<"指向常量的指针p3储存地址为"<<&p3<<"\n";
    //*p3=40;会报错
    int g = 100;
    p3 = &g;
    cout<<"指向常量的指p3储存地址为"<<&p3<<"\n";
    //验证const指针可以修改数据但是不可以更换储存地址
    int *const p4 = &a;
    *p4 = 1000;
    cout<<"const指针P4储存地址为"<<&p4<<"实际值为"<<a<<"\n";
    //p4 = &g;会报错
    return 0;

 }
