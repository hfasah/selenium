''' 
driver.get('https://www.w3schools.com/python/')
driver.maximize_window()
topics = driver.find_elements_by_tag_name('a')
file = open('topics.txt','a')
for i in topics:
    if i.text[0:6] == 'Python' and i.text != ' ':
        print(i.text)
        file.write(f'{i.text} \n')

file.close()
print('Successfully completed')
'''

# selenium 3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.w3schools.com/html/html_forms.asp')
driver.maximize_window()

topics = driver.find_elements_by_tag_name('a')
file = open('topics.txt','a')
for i in topics:
    if i.text [0:4] == 'HTML' and i.text != ' ':
        print(i.text)
        file.write(f'{i.text}, \n')
    
file.close()
print('Sucess')
    