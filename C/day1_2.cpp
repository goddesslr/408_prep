#include <stdio.h>
int main() {
    float height,weight,bmi;
    printf("请输入您的身高(单位：米)：");
    scanf("%f",&height);
    printf("请输入您的体重（单位：Kg）：");
    scanf("%f",&weight);
    bmi=weight/(height*height);
    printf("您的BMI指数为:%f\n",bmi);
    if(bmi < 18.5){
        printf("过轻\n");
    }else if (bmi >= 18.5 && bmi<24.0) {
        printf("标准\n");
    }else {
        printf("过重\n");
    }
    return 0;
}