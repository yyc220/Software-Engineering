# [USACO1.3] 混合牛奶 Mixing Milk


          复制Markdown
         
            展开
             题目描述 由于乳制品产业利润很低，所以降低原材料（牛奶）价格就变得十分重要。帮助 Marry 乳业找到最优的牛奶采购方案。
Marry 乳业从一些奶农手中采购牛奶，并且每一位奶农为乳制品加工企业提供的价格可能相同。此外，就像每头奶牛每天只能挤出固定数量的奶，每位奶农每天能提供的牛奶数量是一定的。每天 Marry 乳业可以从奶农手中采购到小于或者等于奶农最大产量的整数数量的牛奶。
给出 Marry 乳业每天对牛奶的需求量，还有每位奶农提供的牛奶单价和产量。计算采购足够数量的牛奶所需的最小花费。
注：每天所有奶农的总产量大于 Marry 乳业的需求量。
 输入格式 第一行二个整数 n,mn,mn,m，表示需要牛奶的总量，和提供牛奶的农民个数。
接下来 mmm 行，每行两个整数 pi,aip_i,a_ipi​,ai​，表示第 iii 个农民牛奶的单价，和农民 iii 一天最多能卖出的牛奶量。
 输出格式 单独的一行包含单独的一个整数，表示 Marry 的牛奶制造公司拿到所需的牛奶所要的最小费用。
  输入输出样例 输入 #1 
    复制
   100 5
5 20
9 40
3 10
8 80
6 30
 输出 #1 
    复制
   630
 说明/提示 【数据范围】
对于 100%100\%100% 的数据：
0≤n,ai≤2×1060 \le n,a_i \le 2 \times 10^60≤n,ai​≤2×106，0≤m≤50000\le m \le 50000≤m≤5000，0≤pi≤10000 \le p_i \le 10000≤pi​≤1000
题目翻译来自 NOCOW。
USACO Training Section 1.3
 