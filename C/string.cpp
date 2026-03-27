#include <iostream>
#include <string>
#include <cctype>
#include <sstream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 //四种初始化
    string str1="cpoy";
    string str2("happy");
    string str3(5,'A');
    string str4{"666"};
    int num1(3.13);
    //int num2{3.13}报错;
    float num3(3);
    float num4{3};
    cout<<"str1是"<<str1<<"\nstr2是"<<str2<<"\nstr3是"<<str3<<"\nstr4是"<<str4<<"\n";
    cout<<num1<<" "<<" "<<num3<<" "<<num4<<"\n";
    string str5 = "I love anni";
    cout<<str5<<"\n";
    for(auto c : str5 ){
    c=toupper(c);
    }
    cout<<str5<<"\n";
    for(auto&c : str5){
        c=toupper(c);
    }
    cout<<str5<<"\n";
    string str7;
    cout<<"请输入句子：\n";
    getline(cin,str7);
    cout<<str7<<"\n";
    string str6;
    cout<<"请输入文字：\n";
    cin>>str6;
    cout<<str6<<"\n";
    auto count1=str5.size();
    cout<<"str5有多少字符"<<count1<<"\n";
    string word_data = "i love you 3000 times";
    stringstream ss(word_data);
    string word;
    int count = 1;
    while(ss>>word){
        cout<<"第"<<count<<"次"<<"输入的词是["<<word<<"]\n";
        count++;
        cout<<"此时count值是"<<count<<"\n";
    }
    cout<<"此时count值是"<<count<<"\n";
    cout<<word<<"\n";
    return 0;

}