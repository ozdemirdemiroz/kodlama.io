from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait   #gerekli elemeti bekle
from selenium.webdriver.support import expected_conditions as ec  #hangi şarta göre beklenecek
import pytest
#actionchains import
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date

class Test_DemoClass:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.WaitForElementVisibility((By.ID,"user-name"))
        self.WaitForElementVisibility((By.ID,"password"))

        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) 

    #her testden sonra çağırılır
    def teardown_method(self):
        self.driver.quit() #ilgili tarayıcıyı kapatır

    
    @pytest.mark.parametrize("username,password", [("1","1"),("kullanıcı_1","pass_1")]) 
    def test_invalid_login(self, username, password):
        usernameinput=self.driver.find_element(By.ID,"user-name")
        passwordinput=self.driver.find_element(By.ID,"password")
        usernameinput.send_keys(username)
        passwordinput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID , "login-button")
        loginBtn.click()
        errormessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invald-login-{username}-{password}.png")
        assert errormessage.text=='Epic sadface: Username and password do not match any user in this service'

    def test_NameAndPassBos(self):
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        user_pass_bos_mesaj=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-user&passboş.png")
        assert user_pass_bos_mesaj.text=='Epic sadface: Username is required'

    def test_PassBos(self):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        user_bos_mesaj=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-user-standard_user-pass-boş.png")
        assert user_bos_mesaj.text=='Epic sadface: Password is required'

    def test_lockedOutUser(self):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("locked_out_user")
        sifre = self.driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        locked_out_usermesaj=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-lockedOutUser.png")
        assert locked_out_usermesaj.text=='Epic sadface: Sorry, this user has been locked out.'
        

    def test_kirmiziX(self):
        kontrol=0
        self.WaitForElementVisibility((By.ID,"login-button"))
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg"))
        kirmiziX_iconu = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg") 
        #XPATH ile svg icon bulunamadı ,  CSS_SELECTOR ile bulunabiliyor . inspect>copy>copy Selector  
        if kirmiziX_iconu.is_displayed():# yanlış girişte kırmızı X btonu gözüküyorsa
            self.driver.save_screenshot(f"{self.folderPath}/test-yanlış-giriş-kırmızıX-var.png")
            kontrol +=1
        error_mesaj_X=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        error_mesaj_X.click()
        
        try:
            kirmiziX_iconu.is_displayed()# Error X ine tıklanınca kırmızı X gözüküyorsa birşey palılmayacak . zaten buranın hata alması bekleniyor.
            
        except:
            kontrol +=1
            self.driver.save_screenshot(f"{self.folderPath}/test-ErrorX-tıklandı-kırmızıX-yok.png")# Error X i bulunamayınca hata alınacak ve burası çalışacak 
            
        assert kontrol==2


   
    def test_standard_user(self):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = self.driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.CLASS_NAME, "inventory_item_description"))
        self.driver.save_screenshot(f"{self.folderPath}/test-standard_user-giriş-OK.png")
        assert self.driver.current_url=='https://www.saucedemo.com/inventory.html'

    def test_UrunSayisi(self):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = self.driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.CLASS_NAME, "inventory_item_description"))
        urunlistesi = self.driver.find_elements(By.CLASS_NAME, "inventory_item_description")
        self.driver.save_screenshot(f"{self.folderPath}/test-ürün-listesi.png")
        assert len(urunlistesi)==6

    #yeni 1
    def test_sepet(self):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = self.driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.ID, "add-to-cart-sauce-labs-backpack"))
        addToCart1=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart2=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        addToCart3=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        addToCart4=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        addToCart5=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        addToCart6=self.driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
        sepet = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        ActionChains(self.driver).click(addToCart1).click(addToCart2).click(addToCart3).click(addToCart4).click(addToCart5).click(addToCart6).click(sepet).perform()
        self.WaitForElementVisibility((By.ID, "checkout"))
        sepetUrunSayisi=self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.driver.save_screenshot(f"{self.folderPath}/test-sepettki-urun.png")
        assert len(sepetUrunSayisi)==6


    #yeni 2
    @pytest.mark.parametrize("socialXPATH,socialLink,socialname", [("/html/body/div/div/footer/ul/li[1]/a","https://twitter.com/saucelabs","twitter"),("/html/body/div/div/footer/ul/li[2]/a", "https://www.facebook.com/saucelabs","facebook"),("/html/body/div/div/footer/ul/li[3]/a","https://www.linkedin.com/company/sauce-labs/?original_referer=","lşnkedin")])
    def test_socialHub(self,socialXPATH,socialLink,socialname):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = self.driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.XPATH, socialXPATH))
        socialMedia= self.driver.find_element(By.XPATH, socialXPATH)
        socialMedia.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])#yeni açılan tab a ageç
        self.driver.save_screenshot(f"{self.folderPath}/test-socialHub-{socialname}.png")
        assert self.driver.current_url == socialLink
    #yeni3
    def test_priceLowToHigh(self):
        isim = self.driver.find_element(By.ID,"user-name")
        isim.send_keys("standard_user")
        sifre = self.driver.find_element(By.ID,"password")
        sifre.send_keys("secret_sauce")
        giris = self.driver.find_element(By.ID,"login-button")
        giris.click()
        self.WaitForElementVisibility((By.ID, "add-to-cart-sauce-labs-backpack"))
        LtH = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        LtH.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-price-Low-To-High.png")
        fiyat=self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")#fiyatları listeye yazdırıyoruz ama $6.54 gibi değerler bunlar
        fiyatListe = [float(fiyat[i].text[1:]) for i in range(len(fiyat))]#bu fiyat listesinin  her elemanı için ilk karakteri almayacak şekilde yeni fiyatListe oluşturuldu
        fiyatListe_copy_sort=fiyatListe.copy() # bu liste ile bu listenin sort() edilmiş hali eşitse ucuzdan pahalıya sırlanmış demektir
        fiyatListe_copy_sort.sort()
        assert fiyatListe==fiyatListe_copy_sort

    def WaitForElementVisibility(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))