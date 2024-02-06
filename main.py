from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.firefox.service import Service

import pandas
import smtplib

def send_email(t, l):
    my_email = "paul.goldberger75@outlook.com"
    password = "here's my password"
    to_email = "kevin.mchugh281@gmail.com"

    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject: {t}A new listing showing up at Off Campus Housing\n\n"
                                f"title: {t},"
                                f"link: {l}"
                            )

# enter your desired webpage here:
input_url = "https://www.brownuniversityoffcampus.com/housing/price-under+1600/extras-Exclude+Sublets,Furnished"
driver = webdriver.Firefox()
driver.get(input_url)

webpage = driver.page_source

soup = BeautifulSoup(webpage, 'html.parser')
tag_info = soup.find_all(name="a", class_="card-anchor")
# original_data = []
#
# for tag in tag_info:
#     listing_title = tag.get_text()
#     listing_o_link = tag.get("href")
#     listing_link = "https://www.brownuniversityoffcampus.com" + listing_o_link
#     detail = {"title": listing_title,
#               "website": listing_link
#               }
#     original_data.append(detail)
#
# data = pandas.DataFrame(original_data)
# data.to_csv("original_data.csv")

data = pandas.read_csv("original_data.csv")
comparable_list = data.to_dict(orient="records")
title_list = [item["title"] for item in comparable_list]


for tag in tag_info:
    listing_title = tag.get_text()
    listing_o_link = tag.get("href")
    listing_link = "https://www.brownuniversityoffcampus.com" + listing_o_link
    try:
        if listing_title not in title_list:
            new_df = pandas.DataFrame(
                {
                    "title": [listing_title],
                    "website": [listing_link]
                }
            )
            print(new_df)
            new_df.to_csv("original_data.csv", mode="a", index=True, header=False)
            send_email(t=listing_title, l=listing_link)
    except:
        print("something wrong here at BROWN-HOUSING-MAIL-ALERT. terminate the program")



