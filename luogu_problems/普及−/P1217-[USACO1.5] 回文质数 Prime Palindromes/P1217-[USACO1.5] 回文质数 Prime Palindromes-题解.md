# [USACO1.5] 回文质数 Prime Palindromes - 题解

这题吗……
我用的不是制造回文数，是从a找到b。那怎么会不超时呢？
1、我从奇数开始找，每次+2；
2、我发现，没有偶数位的回文质数！省了一大把的时间啊！
虽说还是很慢，不过很好写就是了！哈哈。
下面列核心的三个判断：
    bool ok(int k)   //回文数
    {     
        int a[10],i=0;     
        while (k>0){a[i]=k%10;k/=10;i++;}
        for(int j=0;j<i;j++)if(a[j]!=a[i-j-1])return false;   
        return true;     
    }
    bool ws(int k)  //位数
    {
        if(k>=10 && k<100 && k!=11 || k>=1000 && k<10000)return false;
        if(k>=100000 && k<1000000 || k>=10000000 && k<100000000)return false;
        return true;
    }
    bool ss(int k)   //素数
    {     
        for(int i=3;i*i<=k;i+=2)if(k%i==0)return false;     
        return true;
    }
更优的方法是制造回文数，这个我就不说了。给个赞吧！

 