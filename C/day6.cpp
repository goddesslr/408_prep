#include <iostream>
using namespace std;
int main(){
    //验证auto忽略顶层const
    const int a1=55;
    auto b1 = a1;
    b1 = 44;
    int *const a2 = &b1;// int *const a2 = &a1本身就是错的因为a1 是 const int，所以 &a1 是一把“只读钥匙（底层 const）”，而a2是顶层const二者不匹配就直接报错
    auto b2 = a2;
    int a3 = 100;
    b2 = &a3;
    cout<<"a1的值是"<<a1<<"\na2的值是"<<a2<<"\nb1的值是"<<b1<<"\nb2的值是"<<b2;
    cout<<"只要b1的值和a1不一样，a2的值和b2的值不一样就成功";
    const int* b3 = &a3;
    auto c1=b3;
    //这里不可以用*c1改变a3的值即*c1=50是错误的
    const int* b4 = &a1;
    auto c2 = b4;
    //这里也不能用*c2 = 50改变a1的值都说明了底层const不能被省略
    const int & b5= a3;
    const int & b6 = a1;
    auto c3= b5;
    auto c4= b6;
    //这里的c3，c4忽略顶层变为了普通int变量
    cout<<a1<<a3<<b5<<b6<<c3<<c4<<"\n";
    return 0;
}