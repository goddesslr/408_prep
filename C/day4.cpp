#include <stdio.h>
void cad(int arr[]){
    printf("在子函数中数组体积退化为了：%zu\n",sizeof(arr));
    arr[0]=9999;
}

int main(){
    int my_arr[5]={1,2,3,4,5};
    printf("在主函数中数组体积为：%zu\n",sizeof(my_arr));
    int* p=my_arr;
    printf("my_arr的值为：%p\n",my_arr);
    printf("my_arr[0]的值为：%p\n",&my_arr[0]);

    printf("p对应数据为：%d，地址为%p\n",*p,p);
    p=p+1;
    printf("p+1对应数据为:%d,地址为%p\n",*p,p);
    p=p+3;
    printf("p+3对应数据为：%d，地址为%p\n",*p,p);
    cad(my_arr);
    printf("子函数作用后my_arr[0]为：%d",my_arr[0]);
    printf("my_arr[3]在底层解释为*(my_arr+3),值分别为:%d,%d\n",my_arr[3],*(my_arr+3));
    return 0;
}



