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

            # working correct link
            # scrapes wiki link
            r = requests.post('https://wikiscraperproject.herokuapp.com/', data=post)

            Tempdata = r.text

            if "<!DOCTYPE html>" in Tempdata:
                return render_template("index.html", error=errors["random"])

            # weirdify scraped text
            r1 = requests.get('https://weirdifier.herokuapp.com/', data=Tempdata.encode('utf-8'))

            # display transformed wikipedia text
            return render_template('post.html', translate=r1.text, error="Success!", before=r.text)

        except:
            print("error")
            return render_template("index.html", error=errors["invalid"])

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
