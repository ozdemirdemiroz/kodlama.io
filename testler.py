from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class testler:
    def NameAndPassBos(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(1)
        user_pass_bos_mesaj=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"Kullanıcı adı ve şifre alanı boş kontrolü = {user_pass_bos_mesaj.text=='Epic sadface: Username is required'}")

    def PassBos(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(1)
        user_bos_mesaj=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"Şifre alanı boş kontrolü = {user_bos_mesaj.text=='Epic sadface: Password is required'}")

    def lockedOutUser(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("locked_out_user")
        sifre = driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(1)
        locked_out_usermesaj=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"Kullanıcı kilitli kontrolü = {locked_out_usermesaj.text=='Epic sadface: Sorry, this user has been locked out.'}")

    def kirmiziX(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(1)
        kirmiziX_iconu = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg") 
        #XPATH ile svg icon bulunamadı ,  CSS_SELECTOR ile bulunabiliyor . inspect>copy>copy Selector  
        print(f"Kırmızı X ikonu görünürlüğü kontrolü = {kirmiziX_iconu.is_displayed()}") 
        error_mesaj_X=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        error_mesaj_X.click()
        try:
            print(f"Uyarı mesajının kapatma butonuna tıklandı , X ikonu görünürlüğü kontrolü = {kirmiziX_iconu.is_displayed()}  NOK")
        except:
            print(f"Uyarı mesajının kapatma butonuna tıklandı , X ikonu Bulunamadı - OK")

    def standartUser(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(1)
        print(f" Kullanıcı adı 'standard_user' şifre 'secret_sauce' ile '/inventory.html' sayfasına yönlendirildi mi? = {driver.current_url=='https://www.saucedemo.com/inventory.html'}")

    def UrunSayisi(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(1)
        isim = driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(1)
        urunlistesi = driver.find_elements(By.CLASS_NAME, "inventory_item_description")
        print(f" Sayfadaki ürün sayısı 6 mı = {len(urunlistesi)==6}")

testClass = testler()
testClass.NameAndPassBos()
testClass.PassBos()
testClass.lockedOutUser()
testClass.kirmiziX()
testClass.standartUser()
testClass.UrunSayisi()

while True:
    continue