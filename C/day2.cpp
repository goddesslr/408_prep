#include <stdio.h>
int main(){
    float bmi_list[100];
    float bmi,height,weight;
    int count=0;
    while(1){
        printf("请输入身高(米):\n");
        scanf("%f",&height);
        if(height<=0){
            printf("数据采集结束\n");
            break;
        }else{
            printf("请输入体重(kg):");
            scanf("%f",&weight);
            bmi=weight/(height*height);
            if(bmi<18.5){
                printf("过轻\n");
            }else if(bmi>=18.5 && bmi<=24.0){
                printf("标准\n");
            }else{printf("过重\n");
            }
            bmi_list[count]=bmi;
            count++;
        }
    }
    printf("今天共采集了%d个有效样本！\n",count);
    printf("收集到的BMI数据如下：\n");
    for(int i=0;i<count;i++){
        printf("第%d份数据为%f\n",i+1,bmi_list[i]);
    }
    return 0;
}
