# [USACO1.2] 挤牛奶Milking Cows - 题解

P1204 [USACO1.2]挤牛奶Mixing Cows
又是一道模拟水题。
方法1：布尔数组，打标记，输出
在我的CF440A的题解里面，已经详细讲过关于布尔数组打标记的方法了。这道题目中，我们也可以用这种方法，把每一个时刻是否有人挤奶标记出来，最后用循环找到最长有人挤奶的时间和最长无人挤奶的时间。特别注意：300~900其实是601秒，题目中只有600秒。算的时候，一定从300标记到899才不会出错。
对于这种方法，我花了一个图来表示：

code：
#include <cstdio>
#include <cstring>
using namespace std;
bool timeline[1000005];
int my_max(int x, int y){
	return x > y ? x : y;
}
int my_min(int x, int y){
    return x < y ? x : y;
}
int main(){
	memset(timeline, false, sizeof(timeline));
	int n, tmpx, tmpy, maxz = -1, maxa = -1;
	scanf("%d", &n);
	for(int i = 1; i <= n; i ++){
		scanf("%d%d", &tmpx, &tmpy);
		for(int i = tmpx; i < tmpy; i ++){
			timeline[i] = true;
		}
		maxz = my_max(maxz, tmpy);
		maxa = my_min(maxa, tmpx);
	}
	int maxx = -1, maxy = -1;
	int tmpa = 0, tmpb = 0;
	for(int i = maxa; i <= maxz; i ++){
		if(timeline[i]){
			tmpa ++;
			tmpb = 0;
		} else{
			tmpa = 0;
			if(i < maxz){
				tmpb ++;
			}
		}
		maxx = my_max(maxx, tmpa);
		maxy = my_max(maxy, tmpb);
	}
	printf("%d %d", maxx, maxy);
	return 0;
}

方法2：结构体sort
上面的方法虽然稳定而简单，但是如果数据狠一些就会超时。所以，我们可以不用暴力的方法，使用减法可以算出挤奶时间和未挤奶时间。所以，代码如下（思路看注释）
#include <cstdio>
using namespace std;
int my_max(int x, int y){
	return x > y ? x : y;   //取最大值函数，<algorithm>里面的太慢了
}
int main(){
	int o;
	scanf("%d", &o);
	int maxx = -1, maxy = -1, lasttmp = 0;
	for(int i = 1; i <= o; i ++){
		int tmpx, tmpy;
		scanf("%d%d", &tmpx, &tmpy);    //边读边做，不用数组
		maxx = my_max(maxx, tmpy - tmpx);   //更新最长有人挤奶时间的最大值
		maxy = my_max(maxy, tmpx - lasttmp);//更新最长无人挤奶时间的最大值
		lasttmp = tmpy;                 //更新上一次挤奶的结束时间
	}
	printf("%d %d", maxx, maxy);        //输出
	return 0;
}

如果像我这样提交的话，结果是这样的：

为什么是错误的呢？我想了半天没想出来，于是使用了测试数据下载。第一个测试点是这样的：
1
100 200

这样的话，lasttmp是0，而且输入的数据不一定是顺序的。所以，我们需要对数据排序。如果自己手写排序的话，性能很差。所以，我们使用<algorithm>里面的sort函数对我们的数据进行排序。下面我来介绍以下sort的用法
sort在<algorithm>里面，原型有两个：
template <class RandomAccessIterator>
void sort(RandomAccessIterator first, RandomAccessIterator last);
template <class RandomAccessIterator, class Compare>
void sort(RandomAccessIterator first, RandomAccessIterator last, Compare comp);

第一种原型是对一个数组进行默认的升序排序，第二种却是对数组进行自定义规则的排序。
comp这个参数是一个函数。它对两个和数组类型相同的数进行自定义的比较，如果返回true则不交换，否则交换。对一个有10个元素的数组进行排序，是这样的：
sort(a, a + 10, cmp);

但是，这样使用sort只能排序一组数字。所以，我们使用结构体，使用自定义的cmp函数对整个数据进行排序。具体思路如下图：

但是，如何定义结构体呢？定义结构体的关键字是struct，是structure的简写。具体格式如下：
struct 结构体名{
	成员变量;
	成员函数;
};
结构体名 变量;

结构体在面向对象编程时很有用。但是，它也是sort的绝佳搭档。因为排序时，我们要对一个对象的每一条信息进行交换，而使用数组并不能实现这个功能，所以，使用结构体可以帮助我们完成很多复杂的排序问题。具体参考：

洛谷试炼场普及练习场排序与排序ex

这道题目，我们一个结构体存储每一条信息的和，进行排序，并按图上的思路输出。
#include <bits/stdc++.h>
using namespace std;
int N; 
struct node{
    int begin, end;
}m[5005];
bool cmp(node a, node b){
    return a.begin < b.begin;
}
int main(){
    scanf("%d", &N);
    for(register int i = 1; i <= N; ++ i)
        scanf("%d%d", &m[i].begin, &m[i].end);
    sort(m + 1, m + 1 + N, cmp);
    int begin = m[1].begin;
    int end = m[1].end;
    int ans1 = 0, ans2 = 0;
    for(register int i = 2; i <= N; ++ i){
        if(m[i].begin <= end)
            end = max(end, m[i].end);
        else{
            ans1 = max(ans1, end - begin);
            ans2 = max(ans2, m[i].begin - end);
            begin = m[i].begin;
            end = m[i].end;
        }
    }
    ans1 = max(ans1, end - begin);
    printf("%d %d", ans1, ans2);
    return 0;
}

P.S 这个代码是我们机房的同学写的。这道题是我们考试题目第一题，我用的是第一种方法，而他用的就是这一种。
 