def f(a,i):#函数体，找出所有你要找的数的位置，并以列表形式返回
    b=[]#定义空列表，存储位置
    c=False#后面用于判断是否找到需要找到的数
    low=0#初始位置
    high=len(a)-1#high是最后一个位置
    while(low<(high-1)):
        mid=int((low+high)/2)#二分
        if(a[high]==i):
            m=high
            while(a[high]==i and high>=0):
                b.append(high)#找到后，并把附近所有的相同数加到列表b里面
                high=high-1
            high=m+1
            while( high<=(len(a)-1) and a[high]==i):
                b.append(high)
                high=high+1
            c=True
            break#找到全部的位置后，跳出循环
        if(a[low]==i):
            m=low
            while(a[low]==i and low>=0):
                b.append(low)
                low=low-1
            low=m+1
            while(a[low]==i and low<=(len(a)-1)):
                b.append(low)
                low=low+1
            c=True
            break
        if(a[mid]==i):
            m=mid
            while(a[mid]==i and mid>=0):
                b.append(mid)
                mid=mid-1
            mid=m+1
            while(a[mid]==i and mid<=(len(a)-1)):
                b.append(mid)
                mid=mid+1
            c=True
            break
        elif(a[mid]>i):#缩小查找范围，再次执行循环
            high=mid
        elif(a[mid]<i):
            low=mid
    if(c):#c为True时候，说明已经找到了，为Flase，说明没有找到
        return(sorted(b))#排序b后返回列表

    else:
        return(0)#返回0
stu=input("请输入要被查找的序列，并以逗号隔开，例如 1,2,3,4 可以不按照大小顺序：")
stu1=eval(stu)#将stu的值返回到元组stu1中
stu2=list(stu1)#将stu1强行转化为列表stu2
a=sorted(stu2)#将stu2从小到大排序返回a
print("重新排序过的序列:",a)
i=int(input("请输入你要查找到数："))
b=f(a,i)#调用函数
if b==0:
    print('没有找到')
else:
    for i in range(0,len(b)):
        print("经过重新从小到大排序，你要找的数在列表中的第{0}个位置".format(b[i]))
    
