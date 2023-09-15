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
#     print(type(algorithm))
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

    for i in range(1,180):
        url = f'https://www.luogu.com.cn/problem/list?page={i}'
        browser.get(url)
        html  = browser.page_source    
        soup = BeautifulSoup(html, 'html.parser')

        # 获取题目列表
        problem_list = soup.find_all('div',class_="row")

        for problem in problem_list[:50]:
            problem_id = problem.select('span')[1]['title'].strip()
            problem_title = problem.find('div',class_="title").get_text().strip()
            problem_level = problem.find('div',class_='difficulty').get_text().strip()
                
#             print(problem_id,problem_title,problem_level)
            if difficulty != '' and  difficulty != problem_level:
                continue
            
            # keyword填写id或name
            if keyword != '' and (problem_id != keyword or problem_title != keyword):
                continue

            algorithm_ = algorithm
            algorithm_ = algorithm_.split('，')     
                
            # 爬取题目详情页内容
            problem_url = 'https://www.luogu.com.cn/problem/' + problem_id
            browser.get(problem_url)

            # 打开算法标签
            try:
                element = browser.find_element(By.XPATH,"//span[contains(text(), '查看算法标签')]")
            except Exception:
                problem_tag = [""]
                problem_html  = browser.page_source    
                problem_soup = BeautifulSoup(problem_html, 'html.parser')                
            else:
                element.click()
                # 获得算法标签
                problem_html  = browser.page_source    
                problem_soup = BeautifulSoup(problem_html, 'html.parser')                
                problem_tag = problem_soup.find('div', class_="tags-wrap multiline" )
                problem_tag = problem_tag.find_all('span')
                i = 0
                for tag in problem_tag:
                    problem_tag[i] = tag.get_text()
                    i += 1
            #     print(problem_tag)
                

            if not all(item in problem_tag for item in algorithm_) and algorithm_ != [""]:
                continue
           
            # 获取题目内容     
            print(f"正在爬取{problem_id}的题目...",end = "")
            problem_content = problem_soup.find('div',class_="card problem-card padding-default").get_text()
            print("爬取成功！")
        #     print(problem_content)

            # 爬取答案内容
            print(f"正在爬取{problem_id}的题解...",end = "")
            problem_solution_url = 'https://www.luogu.com.cn/problem/solution/'+problem_id
            browser.get(problem_solution_url)
            problem_solution_html  = browser.page_source
            problem_solution_soup = BeautifulSoup(problem_solution_html, 'html.parser')

        #     # 获取题目答案
            solution_content = problem_solution_soup.find('div',class_='main').get_text()
        #     print(solution_content)
            print("爬取成功！")

        # # 存储题目和题解内容为markdown文件
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
        #     print(folder_path)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
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


def TestLuogu():

    level = "普及−"
    algorithm = "NOIp 提高组"
    keyword = ""
    count = 3
    print(f"爬取洛谷题目难度为{level},算法为{algorithm}的{count}道题目")
    # 调用被测试的函数
    luogu(level, keyword, algorithm,count)


if __name__ == '__main__':
    TestLuogu()