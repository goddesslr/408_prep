bmi_list=[]
while True:
    height_str=input("请输入您的身高（米）：")
    height=float(height_str)
    if height<=0:
        print("数据采集结束")
        break
    weight_str=input("请输入您的体重(kg):")
    weight=float(weight_str)
    bmi=weight/(height*height)
    if bmi<18.5:
        print("过轻")
    elif 18.5<=bmi<=24.0:
        print("标准")
    else:
        print("过重")
    bmi_list.append(bmi)
count=len(bmi_list)
total=sum(bmi_list)
print(f"今天共采集了有效数据{count}份")
if count>0:
    print(f"BMI平均值为{total/count}")
else:
    print("数据采集系统存在问题，请及时检查")
    
