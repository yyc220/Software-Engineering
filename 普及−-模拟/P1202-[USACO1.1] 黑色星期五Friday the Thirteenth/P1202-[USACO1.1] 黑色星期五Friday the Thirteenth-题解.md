# [USACO1.1] 黑色星期五Friday the Thirteenth - 题解

真~模拟

很耿直的想法

写一个函数判断是否闰年

主方法里开一个n次的for循环，然后再开24个for循环，每12个分别对应平（闰）年的每一个月

巨长：600+行（比我用Java模拟BigInteger类还长）

#include<cstdio>

using namespace std;

bool isLeapYear(int year){
    if(year == 1900 || year == 2000 || year == 2100 || year == 2200 || year == 2300 || year == 2400 || year == 2500){
        if(year % 400 == 0){
            return true;
        }
    }else if(year % 4 == 0){
        return true;
    }
    
    return false;
}

int main(){
    int n;
    scanf("%d",&n);
    
    int ans[7] = {};
    
    int day = 1;
    for(int i = 1900;i < 1900 + n;i++){
        if(isLeapYear(i) == false){
            for(int j = 0;j < 31;j++){//平年1月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
            
            for(int j = 0;j < 28;j++){//平年2月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//平年3月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//平年4月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//平年5月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//平年6月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//平年7月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//平年8月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//平年9月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//平年10月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//平年11月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//平年12月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        }else{
            for(int j = 0;j < 31;j++){//闰年1月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
            
            for(int j = 0;j < 29;j++){//闰年2月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//闰年3月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//闰年4月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//闰年5月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//闰年6月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//闰年7月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//闰年8月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//闰年9月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//闰年10月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 30;j++){//闰年11月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        
            for(int j = 0;j < 31;j++){//闰年12月 
                if(j == 13){
                    if(day == 1){
                        ans[day - 1]++;
                    }else if(day == 2){
                        ans[day - 1]++;
                    }else if(day == 3){
                        ans[day - 1]++;
                    }else if(day == 4){
                        ans[day - 1]++;
                    }else if(day == 5){
                        ans[day - 1]++;
                    }else if(day == 6){
                        ans[day - 1]++;
                    }else if(day == 7){
                        ans[day - 1]++;
                    }
                }
                
                day++;
            
                if(day > 7){
                    day = 1;
                }
            }
        }
    }

    printf("%d ",ans[6]);
    printf("%d ",ans[0]);
    printf("%d ",ans[1]);
    printf("%d ",ans[2]);
    printf("%d ",ans[3]);
    printf("%d ",ans[4]);
    printf("%d ",ans[5]);
    
    return 0;
}

 