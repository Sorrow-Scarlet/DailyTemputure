#一键体温填报小助手
#配合win任务计划食用更佳
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=r'E:\PYScripts\webDriver\msedgedriver.exe')
#看这里，先检查以下参数是否正常，分别是{填报网址，账户，密码，电话号码，导员名}
webPageEntrance = r""
account = ""
passwd = ""
phoneNumber = ""
master = ""


def DoReport():
    #自动填充账号密码,浏览器内手动输入验证码
    driver = webdriver.Edge(service = service)
    driver.get(webPageEntrance)
    time.sleep(5)
    #Xpath绝对路径定位处理中
    driver.find_element(By.XPATH, '//*[@id="userName"]').click()
    driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(account)
    driver.find_element(By.XPATH, '//*[@id="password"]').click()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passwd)
    jsTip = """
        var span = document.createElement('span');
        span.innerHTML = '请在5秒内输入验证码！';
        span.style.position = 'absolute';
        span.style.top = '25%';
        span.style.left = '60%';
        span.style.color = '#A04354';
        span.style.fontSize = '20px';
        document.body.appendChild(span);
        setTimeout(function() {document.body.removeChild(span)},9000);
        """
    driver.execute_script(jsTip)
    time.sleep(5)#人工在5秒内输入验证码
    driver.find_element(By.XPATH,'//*[@id="root"]/span/div[3]/div[2]/div[2]/div/div[1]/div/div/form/div[5]/button').click()
    #登陆后跳转填报
    time.sleep(8)
    #光速填报手机号和导员姓名
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL10"]').click()
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL10"]').send_keys(phoneNumber)
    driver.find_element(By.XPATH,'//input[contains(@value, "在校")]').click()
    time.sleep(1)
    #填充导员并确认
    driver.find_element(By.XPATH,"//input[contains(@id, 'activeInput')]").click()
    driver.find_element(By.XPATH,"//input[contains(@id, 'activeInput')]").send_keys(master)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[contains(@id, 'activeInput')]").send_keys(Keys.ENTER)
    #自动选择早中晚三个下拉选择菜单，并且选择特定值
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL29"]/option[16]').click()
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL30"]/option[16]').click()
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL89"]/option[16]').click()
    
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="V1_CTRL132"]').click()#同意
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[4]/form/div/div[3]/div[3]/div[2]/ul/li/a').click()#提交
    
    time.sleep(5)
    driver.quit()

#主入口
if __name__ == "__main__":
    print("selenium自动控制可能有些慢，请耐心等待")
    DoReport()
    print("填报完成，请自行查看结果")
    print("若成功填报，则无法重复进入填报页面")