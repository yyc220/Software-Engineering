# 数列分段 Section I


          复制Markdown
         
            展开
             题目描述 对于给定的一个长度为 NNN 的正整数数列 AiA_iAi​，现要将其分成连续的若干段，并且每段和不超过 MMM（可以等于MMM），问最少能将其分成多少段使得满足要求。
 输入格式 第1行包含两个正整数 N,MN,MN,M，表示了数列 AiA_iAi​ 的长度与每段和的最大值，第 222 行包含 NNN 个空格隔开的非负整数 AiA_iAi​，如题目所述。
 输出格式 一个正整数，输出最少划分的段数。
  输入输出样例 输入 #1 
    复制
   5 6
4 2 4 5 1 输出 #1 
    复制
   3 说明/提示 对于20%20\%20%的数据，有N≤10N≤10N≤10；
对于40%40\%40%的数据，有N≤1000N≤1000N≤1000；
对于100%100\%100%的数据，有N≤100000,M≤109N≤100000,M≤10^9N≤100000,M≤109，MMM大于所有数的最大值，AiA_iAi​之和不超过10910^9109。
将数列如下划分：
[4][24][51][4][2 4][5 1][4][24][51]
第一段和为444，第222段和为666，第333段和为666均满足和不超过M=6M=6M=6，并可以证明333是最少划分的段数。
 