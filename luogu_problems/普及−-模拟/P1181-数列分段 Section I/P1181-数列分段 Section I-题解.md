# 数列分段 Section I - 题解

#很简单的一道暴力题这道题有两种方法，一种是边读边做，一种是读完数组再做。这两种方法对新手来说都很简单，不过边读边做相对简单一点。
##注意：ans一开始的初值必须为1，因为最后一段是加不进去的，所以初值一定要为1。
##代码如下：
#include <cstdio>//头文件准备
using namespace std;
int n,m,ans=1;//ans的初值要为1
int main(){
    scanf ("%d %d",&n,&m);
    int k=0;
    while (n--){//完全的边读边做
        int a;
        scanf ("%d",&a);//读入a
        if (k+a<=m){//判断k+a是否大于m，如果大于，ans要加1，然后a独立为一段；如果小于等于，k就要加上a
            k+=a;
        }
        else{
            ans++;
            k=a;
        }
    }
    printf ("%d\n",ans);//做完之后输出，结束
    while (1);//反抄袭
}
#珍爱生命，拒绝抄袭！

 