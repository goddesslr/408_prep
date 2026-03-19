#include <stdio.h>
int main(){
    int age=20;
    float gpa=3.8;
    char grade='A';
printf("我的年龄是%d \n",age);
printf("我目标的gpa是%f,成绩是%c \n",gpa,grade);
    int num1,num2,sum;
    printf("\n请输入数字：");
    scanf("%d %d",&num1,&num2);
    sum=num1+num2;
    printf("这两个数字之和为:%d + %d=%d\n",num1,num2,sum);
return 0;
}