import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager


words_to_search = ["MS dhoni", "Virat Kohli","Ind vs Aus","BGT 2024", "Rohit Sharma", "Corona Virus", "Whatsapp social Media", "llb full form", "mba full form", "Gurukul", "Quantum Physics", "Sulphur in body", "iron in body", "Gautam Gambhir", "Ruturaj Gaikwad", "Shivam Dube", "Ravindra Jadeja", "Jaiswal", "Shubman Gill", "Ravi Ashwin", "Sarfaraz Khan", "Axar patel", "Washington Sundar", "Kuldeep yadav", "Jasprit Bumrah", "Akash Deep", "Mohammad Siraj", "Mohammad Shami", "Hardik Pandya","Sanju Samson", "Chahal", "Dhruv Jurel", "Rinku Singh", "Surya Kumar yadav", "Abishek Sharma", "Ishan Kishan", "Bachelor of technology", "compuetr science And engineering", "Chandihgarh university", "Hp Pavilion", "Narendra Modi", "Jitesh Sharma", "Arshdeep Singh", "Shikhar Dhawan", "Sachin Tendulkar", "Rahul Dravid", "India Won CWC", "India Won t20 Wc", "Kapil dev", "Anil Kumble", "Akash Chopra"]

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://www.bing.com/?form=ML2W4X&OCID=ML2W4X&PUBL=RewardsDO&CREA=ML2W4X")

def search_word(word):
    search_box = driver.find_element("name", "q")  
    search_box.clear()
    search_box.send_keys(word)
    search_box.send_keys(Keys.RETURN)


for word in words_to_search:
    search_word(word)
    time.sleep(5) 

driver.quit()