from flask import Flask, redirect, url_for, render_template, request, send_file
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    errors = {"invalid": "Wikipedia link is invalid. Please try again.",
                "empty": "Wikipedia link was not entered.",
                "general": "Wikipedia link led to search result. Please enter a link to a specified article.",
                "random": "Error has occured. Please try again."}

    print(errors)

    if request.method == "POST":

        try:
            # preps url link
            post = {"url": request.form['url'].strip()}

            # test
            print(post)

            # # empty link
            if post["url"] == "":
                return render_template('index.html', error=errors["empty"])

            # # not wiki link
            elif "wikipedia.org/wiki/" not in post["url"]:
                return render_template('index.html', error=errors["invalid"])

            # # if general link
            # else:
            #     print("123456")
            #     uClient = uReq(post["url"])
            #     page_html = uClient.read()
            #     uClient.close()
            #     page_soup = soup(page_html, "html.parser")
            #
            #     # scrape following html tags
            #     page_body = page_soup.body.findAll(['b'])
            #     print(page_body)
            #
            #     for x in page_body:
            #         if x == "Wikipedia does not have an article with this exact name.":
            #             return render_template('index.html', error=errors["general"])

            # working correct link
            # scrapes wiki link
            r = requests.post('https://wikiscraperproject.herokuapp.com/', data=post)

            # text test
            # print(type(r))
            # Tempdata = r.text
            # print(type(Tempdata))
            # print(Tempdata)


            # weirdify scraped text
            r1 = requests.get('https://weirdifier.herokuapp.com/', data=Tempdata.encode('utf-8'))
            # print(r1)
            # print(r1.text)

            # display transformed wikipedia text
            return render_template('index.html', translate=r1.text, error="Success!")

        except:
            print("error")
            return render_template("index.html", error=errors["invalid"])

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
