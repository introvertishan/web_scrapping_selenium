from django.shortcuts import render
from django.core.paginator import Paginator
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# blank array to store all objects
all_data_object = []
all_company_object = []

# class which makes object for all the data which is received from angel.co
class alldata(object):
    """docstring for alldata"""

    def __init__(self, imgsrc, link, name, bio, city, industry, invetments, followers):
        self.imgsrc = imgsrc
        self.link = link
        self.name = name
        self.bio = bio
        self.city = city
        self.industry = industry
        self.invetments = invetments
        self.followers = followers

    def __str__(self):
        return self.name

# class which makes object for all the company data which is received from angel.co
class all_data_company(object):
    """docstring for all_data_company"""

    def __init__(self, imgsrc, link, name, bio, date, city, market, website_link, website_text, employee, raised):
        self.imgsrc = imgsrc
        self.link = link
        self.name = name
        self.bio = bio
        self.date = date
        self.city = city
        self.market = market
        self.website_link = website_link
        self.website_text = website_text
        self.employee = employee
        self.raised = raised

    def __str__(self):
        return self.name

# function to make objects of company data
def all_for(arr,n):
    for i in arr[n:]:
        all_photos = i.find_elements_by_class_name("photo")
        images = all_photos[0].find_elements_by_tag_name('img')
        final_img_src = images[0].get_attribute('src')  # final source

        all_hrefs = i.find_elements_by_class_name("name")
        hrefs = all_hrefs[0].find_elements_by_tag_name('a')
        final_link_href = hrefs[0].get_attribute('href')  # final links

        all_names = i.find_elements_by_class_name("name")
        names = all_names[0].find_elements_by_tag_name('a')
        final_name = names[0].text  # final name

        all_bios = i.find_elements_by_class_name("text")
        all_bio = all_bios[0].find_elements_by_class_name("pitch")
        all_final_bio = all_bio[0].text

        all_joined_dates = i.find_elements_by_class_name("joined")
        all_joined_date = all_joined_dates[0].find_elements_by_class_name("value")
        all_final_date = all_joined_date[0].text

        all_cities = i.find_elements_by_class_name("location")
        all_city = all_cities[0].find_elements_by_class_name("tag")
        all_city_hrefs = all_city[0].find_elements_by_tag_name('a')
        all_city_link = all_city_hrefs[0].text

        all_markets = i.find_elements_by_class_name("market")
        all_market = all_markets[0].find_elements_by_class_name("tag")
        all_market_text = all_market[0].find_elements_by_tag_name('a')
        final_market = all_market_text[0].text

        all_websites = i.find_elements_by_class_name("website")
        all_website = all_websites[0].find_elements_by_tag_name('a')
        all_website_href = all_website[0].get_attribute('href')  # final links
        all_web_text = all_website[0].text

        all_employees = i.find_elements_by_class_name("company_size")
        all_employee = all_employees[0].find_elements_by_class_name("value")
        all_final_employee = all_employee[0].text

        all_raised = i.find_elements_by_class_name("raised")
        all_raise = all_raised[0].find_elements_by_class_name("value")
        all_final_raise = all_raise[0].text

        # print(final_img_src, final_link_href, final_name, all_final_bio,
        #       all_final_date,
        #       all_city_link,
        #       final_market, all_website_href, all_web_text, all_final_employee,
        #       all_final_raise)
        # print("-----------------------------------------------------------------------------------------")

        final_data_company = all_data_company(final_img_src, final_link_href, final_name, all_final_bio,
                                              all_final_date,
                                              all_city_link,
                                              final_market, all_website_href, all_web_text, all_final_employee,
                                              all_final_raise)

        all_company_object.append(final_data_company)


# function which invokes the selenium browser
def landing(n):
    driver = init_driver()
    if n == 1:
        lookup(driver)
    else:
        company_lookup(driver)
    time.sleep(2)
    driver.quit()


# function which invokes the selenium browser
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 10)
    return driver

# getting all company data from angel.co
def company_lookup(driver):
    driver.get("https://angel.co/companies?locations[]=1647-India")
    try:
        all_tags = driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "results")))
        loaded_data = all_tags.find_elements_by_class_name("dc59")
        all_for(loaded_data,1)
        x= driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more")))
        x.click()
        all_new_tags = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".frs86 .frs86")))
        all_new_loaded = all_new_tags.find_elements_by_class_name("dc59")
        all_for(all_new_loaded,0)

        y= driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more")))
        y.click()
        all_new_new_tags = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".frs86 .frs86 .frs86")))
        all_new_new_loaded = all_new_new_tags.find_elements_by_class_name("dc59")
        all_for(all_new_new_loaded,0)

        # z= driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more")))
        # z.click()
        # all_new_new_new_tags = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".frs86 .frs86 .frs86 .frs86")))
        # all_new_new_new_loaded = all_new_new_new_tags.find_elements_by_class_name("dc59")
        # all_for(all_new_new_new_loaded,0)

    except TimeoutException:
        print("Something went wrong")


# getting all investors data from angel.co
def lookup(driver):
    driver.get("https://angel.co/india/investors")
    try:
        all_tags = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "with_data")))
        loaded_data = all_tags.find_elements_by_class_name("frw44")

        for i in loaded_data:

            all_photos = i.find_elements_by_class_name("photo")
            images = all_photos[0].find_elements_by_tag_name('img')
            final_img_src = images[0].get_attribute('src')  # final source

            all_hrefs = i.find_elements_by_class_name("name")
            hrefs = all_hrefs[0].find_elements_by_tag_name('a')
            final_link_href = hrefs[0].get_attribute('href')  # final links

            all_names = i.find_elements_by_class_name("name")
            names = all_names[0].find_elements_by_tag_name('a')
            final_name = names[0].text  # final name

            all_bio = i.find_elements_by_class_name("blurb")
            final_bio = all_bio[0].text  # final bio

            all_citynindustry = i.find_elements_by_class_name("tags")
            city = all_citynindustry[0].find_elements_by_tag_name('a')
            count = 0
            final_city = ""
            final_industry = ""

            for ci in city:
                if count == 0:
                    final_city = ci.text
                    count = count + 1
                else:
                    final_industry = ci.text
                    count = 0

            no_invetments = i.find_elements_by_class_name("investments")
            final_investments = no_invetments[0].text

            no_followers = i.find_elements_by_class_name("followers")
            final_followers = no_followers[0].text

            # print(final_img_src,final_link_href,final_name,final_bio,final_city,final_industry,final_investments,final_followers)
            # print("-----------------------------------------------------------------")

            final_data = alldata(final_img_src, final_link_href, final_name, final_bio, final_city, final_industry,
                                 final_investments, final_followers)

            all_data_object.append(final_data)

        print(all_data_object)

    except TimeoutException:
        print("kuch went wrong")


# Create your views here.
def home(request):
    landing(1)
    return render(request, 'home.html', {'all_data_object': all_data_object})


def companies(request):
    landing(2)
    print(len(all_company_object))
    # page = request.GET.get('page',1)
    # paginator = Paginator(all_company_object, 10)
    # try:
    #     all_record = paginator.page(page)
    # except PageNotAnInteger:
    #     all_record = paginator.page(1)
    # except EmptyPage:
    #     all_record = paginator.page(paginator.num_pages)
    return render(request, 'company.html', {'all_company_object': all_company_object})


def mainpage(request):
    return render(request,'main.html')
