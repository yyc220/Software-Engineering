# [USACO1.5] 特殊的质数肋骨 Superprime Rib


          复制Markdown
         
            展开
             题目描述 农民约翰的母牛总是产生最好的肋骨。你能通过农民约翰和美国农业部标记在每根肋骨上的数字认出它们。
农民约翰确定他卖给买方的是真正的质数肋骨，是因为从右边开始切下肋骨，每次还剩下的肋骨上的数字都组成一个质数。
举例来说：7 3 3 17\ 3\ 3\ 17 3 3 1 全部肋骨上的数字 733173317331 是质数；三根肋骨 733733733 是质数；二根肋骨 737373 是质数；当然,最后一根肋骨 777 也是质数。733173317331 被叫做长度 444 的特殊质数。
写一个程序对给定的肋骨的数目 nnn，求出所有的特殊质数。111 不是质数。
 输入格式 一行一个正整数 nnn。
 输出格式 按顺序输出长度为 nnn 的特殊质数,每行一个。
  输入输出样例 输入 #1 
    复制
   4
 输出 #1 
    复制
   2333
2339
2393
2399
2939
3119
3137
3733
3739
3793
3797
5939
7193
7331
7333
7393
 说明/提示 【数据范围】
对于 100%100\%100% 的数据，1≤n≤81\le n \le 81≤n≤8。
题目翻译来自NOCOW。
USACO Training Section 1.5
 