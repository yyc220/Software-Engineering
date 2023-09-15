# [USACO1.3] 混合牛奶 Mixing Milk - 题解

第一篇题解吖
关键词：暴力，排序，AC。
先说下思想，建议看懂的自己做不要看代码，实在不会(或者被我这毫无章法的语言恶心到了的)再去看看(我那丑不拉几的)代码吧~
思路：
1，先按照单价排序，单价小的在前面； 单价一样的就把产量多的放前面；（我是用结构体做的，排序方便）
2，当还需要采购时（n不为零），我们从当前还需采购值开始，挨个减一，总价钱加上当前最小单价，当这头牛产量为零（不能再从它购买时），换一头牛（数组加一），直到购买完（n=0）为止。
3，输出总价钱，等待评测，然后AC;
下面是代码：
/*(^-^)*/
#include<cmath>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int n,m,ans;//总需求量，提供的个数，总价；

struct node
{
    int a,b;//牛奶单价和产量
}a[5005];//定义结构体

bool cmp(node a,node b)
{
    if(a.a!=b.a)return a.a<b.a;
    else return a.b>b.b;
}//好我们定义一个判断函数，条件见思路1；

int main()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    	cin>>a[i].a>>a[i].b;
    sort(a+1,a+1+m,cmp);//用刚定义的函数给它排序
    int i=1;
    while(n)//从n开始减起，直达n为零停止
    {
        if(a[i].b!=0)//当这头牛还没购买完
        {
            a[i].b--;//这头牛可购买数减一
            ans+=a[i].a;//总花费加上这头牛的单价（或者说当前最小单价）
            n--;//需求量减一
        }
        else i++;//购买完了换头牛
    }
    cout<<ans;
    return 0;
}

审核真好看！给过吧QWQ（女生学oi不容易！）
 