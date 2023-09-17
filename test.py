from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from PIL import Image
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
import re
import unittest
from unittest.mock import patch
from io import StringIO

# 将题目中的特殊符号换成'_'
def sanitize_filename(filename):
    # 定义需要替换的特殊字符
    illegal_chars = r'[\\/:\*\?"<>|]'
    # 使用下划线替换特殊字符
    sanitized_filename = re.sub(illegal_chars, '_', filename)
    return sanitized_filename

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
    folder_name = "test_folder"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

     # 记录成功爬取的题目数
    success = 0
    
    # 筛选洛谷的179个页面
    for i in range(1,180):
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
            
            algorithm_ = '-'.join(algorithm_)
            prefix_addr = [string for string in [difficulty, keyword, algorithm] if string]  # 过滤掉空串
            prefix_addr = '-'.join(prefix_addr)
            prefix_addr = sanitize_filename(prefix_addr)
            
            
            problem_title_ = sanitize_filename(problem_title) # 删掉特殊符号
            
            folder_path = folder_name

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # 写入题目
            print(f"正在保存{problem_id}的题目...",end = "")
            with open(os.path.join(folder_path, f'{problem_id}-{problem_title_}.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {problem_title}\n\n{problem_content}')
            print("保存成功！")

            # 写入题解
            print(f"正在保存{problem_id}的题解...",end = "")
            with open(os.path.join(folder_path, f'{problem_id}-{problem_title_}-题解.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {problem_title} - 题解\n\n{solution_content}')
                
            success += 1    
            print(f"保存成功！题号为{problem_id}，题目为{problem_title},搜索标签为{prefix_addr}")  
            print(f"成功保存{success}道题目")
            if success == count:
                print(f"爬取完毕！")
                
                # 关闭浏览器
                browser.quit()
                return
    print("没有更多满足条件的题目！")
    browser.quit()
    return

class TestLuoguFunction(unittest.TestCase):

    def setUp(self):
        # 创建临时文件夹用于保存测试结果
        self.test_folder = "test_folder"
        os.makedirs(self.test_folder, exist_ok=True)

    def tearDown(self):
        # 清除临时文件夹及其内容
        if os.path.exists(self.test_folder):
            for root, dirs, files in os.walk(self.test_folder, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.test_folder)

    @patch('sys.stdout', new_callable=StringIO)
    def test_luogu_success(self, mock_stdout):
        # 构造输入参数
        difficulty = "入门"
        keyword = ""
        algorithm = ""
        count = 1

        # 调用被测试函数
        luogu(difficulty, keyword, algorithm, count)

        # 获取函数输出结果
        output = mock_stdout.getvalue()

        # 检查是否成功保存了1道题目
        self.assertIn(f"成功保存1道题目", output)

        # 检查是否生成了对应数量的文件
        self.assertEqual(len(os.listdir(self.test_folder)), count * 2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)