#include <stdio.h>
#include <iostream>

int main(){
    int i = 42;
    const int &r1=i;
    int& r2 = i;
    r2=3;
    std::cout<<"i现在的值是\n"<<i<<"r2的值是\n"<<r2<<"r1的值是\n"<<r1;
    //验证auto跳过引用和顶层const
    const int r3 = 20;
    auto a = r3;
    a=25;
    std::cout<<"r3的值是"<<r3<<"\na的值是"<<a;
    int *const r4 =&i;
    auto b = r4;
    *b=30;
    std::cout<<"r4的值是"<<r4<<"\nb的值是"<<b<<"\ni的值是"<<i;
    return 0;
}



