import tkinter as tk
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from PIL import Image
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
import re

def luogu(difficulty,keyword,algorithm,count):
    browser = webdriver.Chrome()  # 创建谷歌浏览器
    myurl = "https://www.luogu.com.cn"
    browser.get(myurl)  # 打开目标网站
    browser.maximize_window()  # 将浏览器全屏

    # 清除现有的所有 Cookie
    browser.delete_all_cookies()

    # 导入 Cookie
    with open('cookies.txt', 'r') as f:
        for line in f:
            name, value = line.strip().split('=')
            browser.add_cookie({'name': name, 'value': value})

    browser.refresh()

    # 创建存储文件夹
    folder_name = "/软工作业3/luogu_problems"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

     # 记录成功爬取的题目数
    success = 0

    # 筛选洛谷的14个页面
    for i in range(1,15):
        url = f'https://www.luogu.com.cn/problem/list?page={i}'
        browser.get(url)
        html  = browser.page_source    
        soup = BeautifulSoup(html, 'html.parser')

        # 获取题目列表
        problem_list = soup.find_all('div',class_="row")
        len_list = len(problem_list)
        for problem in problem_list[:len_list]:
            problem_id = problem.select('span')[1]['title'].strip()
            problem_title = problem.find('div',class_="title").get_text().strip()
            problem_level = problem.find('div',class_='difficulty').get_text().strip()
                
            # 题目难度不一样
            if difficulty != '' and  difficulty != problem_level:
                continue
            
            # 关键词不一样
            if keyword != '' and problem_id != keyword and problem_title != keyword:
                continue
            
            # 算法类型改为list
            algorithm_ = algorithm
            algorithm_ = algorithm_.split('，')     
                
            # 爬取题目详情页内容
            problem_url = 'https://www.luogu.com.cn/problem/' + problem_id
            browser.get(problem_url)

            # 打开算法标签
            try:
                element = browser.find_element(By.XPATH,"//span[contains(text(), '查看算法标签')]")
            except Exception: # 有的题目没有算法标签 将problem_tag设为[""]
                problem_tag = [""]
                problem_html  = browser.page_source    
                problem_soup = BeautifulSoup(problem_html, 'html.parser')                
            else:
                element.click() # 有算法标签的题目，点击查看完整标签
                # 获得算法标签
                problem_html  = browser.page_source    
                problem_soup = BeautifulSoup(problem_html, 'html.parser')                
                problem_tag = problem_soup.find('div', class_="tags-wrap multiline" )
                problem_tag = problem_tag.find_all('span')
                i = 0
                for tag in problem_tag:
                    problem_tag[i] = tag.get_text()
                    i += 1                
            # 标签不一样
            if not all(item in problem_tag for item in algorithm_) and algorithm_ != [""]:
                continue
           
            # 获取题目内容     
            print(f"正在爬取{problem_id}的题目...",end = "")
            problem_content = problem_soup.find('div',class_="card problem-card padding-default").get_text()
            print("爬取成功！")

            # 爬取答案内容
            print(f"正在爬取{problem_id}的题解...",end = "")
            problem_solution_url = 'https://www.luogu.com.cn/problem/solution/'+problem_id
            browser.get(problem_solution_url)
            problem_solution_html  = browser.page_source
            problem_solution_soup = BeautifulSoup(problem_solution_html, 'html.parser')

            # 获取题目答案
            solution_content = problem_solution_soup.find('div',class_='main').get_text()
            print("爬取成功！")

            ## 存储题目和题解内容为markdown文件
            #获得保存路径
            prefix_addr = ''
            if difficulty != '':
                prefix_addr += '-' + difficulty.replace('/',',')
            if keyword != '':
                prefix_addr += '-' + keyword
            if algorithm_ != [""]:
                prefix_addr += '-' + '-'.join(algorithm_)
            if prefix_addr[0] == '-':
                prefix_addr = prefix_addr[1:]
            
            problem_id_ = problem_id.replace('/',',')
            problem_title_ = problem_title.replace('/',',')
            folder_path = os.path.join(folder_name, f'{prefix_addr}',f'{problem_id_}-{problem_title_}')

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # 写入题目
            print(f"正在保存{problem_id}的题目...",end = "")
            with open(os.path.join(folder_path, f'{problem_id_}-{problem_title_}.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {problem_title}\n\n{problem_content}')
            print("保存成功！")

            # 写入题解
            print(f"正在保存{problem_id}的题解...",end = "")
            with open(os.path.join(folder_path, f'{problem_id_}-{problem_title_}-题解.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {problem_title} - 题解\n\n{solution_content}')
                
            success += 1    
            print(f"保存成功！题号为{problem_id}，题目为{problem_title},搜索标签为{prefix_addr}")  
            print(f"成功保存{success}道题目")
            if success == count:
                print(f"爬取完毕！")
                
                # 关闭浏览器
                browser.quit()
                return
    browser.quit()
    return

def filter_luogu():
    # 获取用户输入的筛选条件
    difficulty = difficulty_var.get()
    keyword = keyword_var.get()
    algorithm = algorithm_var.get() 
    
    # 在这里编写爬虫程序，根据筛选条件爬取洛谷题目
    luogu(difficulty,keyword,algorithm,1) # "1"表示爬取1道题目


# 创建GUI窗口
window = tk.Tk()
window.title("洛谷爬虫")

# 难度选择下拉菜单
difficulty_label = tk.Label(window, text="题目难度：")
difficulty_label.grid(column=0, row=0, padx=10, pady=10)
difficulty_var = tk.StringVar(window)
difficulty_choices = ["", "暂无评定","入门", "普及−", "普及/提高−",
                      "普及+/提高", "提高+/省选−", "省选/NOI−", "NOI/NOI+/CTSC"]
difficulty_var.set(difficulty_choices[0])  # 默认选中第一个选项
difficulty_dropdown = tk.OptionMenu(window, difficulty_var, *difficulty_choices)
difficulty_dropdown.grid(column=1, row=0)

# 关键词输入框
keyword_label = tk.Label(window, text="关键词：")
keyword_label.grid(column=0, row=1, padx=10, pady=10)
keyword_var = tk.StringVar(window)
keyword_entry = tk.Entry(window, textvariable=keyword_var)
keyword_entry.grid(column=1, row=1)

# 算法标签输入框
algorithm_label = tk.Label(window, text="算法标签：")
algorithm_label.grid(column=0, row=2, padx=10, pady=10)
algorithm_var = tk.StringVar(window)
algorithm_entry = tk.Entry(window, textvariable=algorithm_var)
algorithm_entry.grid(column=1, row=2)

# 筛选按钮
filter_button = tk.Button(window, text="筛选", command=filter_luogu)
filter_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# 运行GUI窗口
window.mainloop()

if __name__ == '__main__':
    filter_luogu()