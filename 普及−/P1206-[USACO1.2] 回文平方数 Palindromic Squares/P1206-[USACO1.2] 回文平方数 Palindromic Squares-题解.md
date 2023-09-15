# [USACO1.2] 回文平方数 Palindromic Squares - 题解

给大家介绍一种C++11特有的方法：构造函数。
构造函数，就是在初始化结构体的过程中，通过调用node name(data)的方法来初始化一个结构体。虽然有重载=运算符大法，但是本人更加偏向于构造函数，因为这样便于编写和理解。
构造一个node结构体存储B进制数，我们只需要编写node的构造函数（就是将10进制整数转化为B进制数字的函数），一个输出函数，还有判断这个进制数是否是回文数的函数。
代码如下（请留意代码中的注释）：
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int b;
inline char c(int x){if(x>=0&&x<=9)return x+'0';return x-10+'A';}
struct node
{
    int l,a[20];//进制数最大长度为17
    node(int x){for(l=0;x;l++)a[l]=x%b,x/=b;}//转换进制数，其中a[l-1]是最高位，a[0]是最低位
    void out(){for(int i=l-1;i>=0;i--)printf("%c",c(a[i]));}//从高到低依次输出
    bool tf(){for(int i=0;i<l;i++)if(a[i]!=a[l-i-1])return false;return true;}//判断这个数字是否是回文数，注意可以通过i<=l/2来加速，减少冗余运算
};
int main()
{
    scanf("%d",&b);
    for(int i=1;i<=300;i++)//从1到300暴力枚举
    {
        node n(i*i);//将i*i转化为进制为b的整数
        if(n.tf()){node m(i);m.out();putchar(' ');n.out();putchar('\n');}//如果n是一个b进制下的回文数，输出答案
    }
    return 0;
}

 