from selenium import webdriver  #automation proceess library
from time import sleep

driver = driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/@31.4855012,74.3470166,15z") 
sleep(2) 

#xpath is stand for XML path language, uses path expression to identify and navigate nodes in an XML document can be use to 
#select  one/more nodes in the document by using absolute / relative path 

def searchplace():
    Place = driver.find_element('name','tactile-searchbox-input')
    Place.send_keys("Paris")
    submit = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()
searchplace()

def direction():
    sleep(10)
    direction = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button")
    direction.click()
direction()

def find():
    sleep(10)
    find = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
    find.send_keys("London")
    search = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()

find()

def distancetime():
    sleep(8)
    distance = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div")
    print("Total Distance: ",distance.text)
                                        
    car = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[1]/span[1]")
    print("Time Take by Vehcile: ",car.text)

    train = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[2]/div[1]/div")
    print("Time Take by Train: ",train.text)
    
    aroplane = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[3]/div/div[4]/div[1]/div/div[1]")
    print("Time Take by Aroplane: ",aroplane.text)
    
distancetime()