#include <iostream>
#include "Sales_data.h"
using namespace std;

int main(){
    Sales_data data1,data2;
    //定义相同书号
    data1.bookNo = "224510";
    data2.bookNo = "224510";
    //键盘传入购买时的价格数目自动计算收入revenue
    double price;
    cin>>price>>data1.units_sold;
    data1.revenue = price*data1.units_sold;
    cin>>price>>data2.units_sold;
    data2.revenue = price*data2.units_sold;
    //融合auto说明符相关知识
    auto total_revenue = data1.revenue + data2.revenue;
    auto total_sold = data1.units_sold + data2.units_sold;

    cout<<"书本编号:"<<data1.bookNo;
    cout<<"\n总销量:"<<total_sold;
    cout<<"\n总收入:"<<total_revenue;
    cout<<"\ndata1.revenue是"<<data1.revenue;

    decltype(total_sold) total_sold2 = total_sold;
    total_sold2 = 100;
    cout<<"\n总销量是"<<total_sold<<"\nsold2是"<<total_sold2;

    decltype((data1.revenue)) data = data1.revenue;
    data = 1000;
    cout<<"\ndata1.revenun是"<<data1.revenue<<"\ndata是"<<data<<"\n";
    return 0;
}