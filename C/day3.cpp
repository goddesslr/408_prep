#include <stdio.h>
 void fake(int w) {
    printf("接收到输入数据：%d\n",w);
    w = w + 10;
    printf("函数作用后数据变为：%d\n",w);
 }
 void real(int *p){
    printf("接收到输入数据：%d\n",*p);
    *p = *p + 10;
    printf("函数作用后数据变为：%d\n",*p);
 }

 int main(){
    int weight=70;
    printf("函数fake正在作用...\n");
    fake(weight);
    printf("数据为：%d",weight);
    
    printf("\n函数real正在作用...\n");
    real(&weight);
    printf("数据为:%d\n",weight);
    return 0;
 }
