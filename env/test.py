from flask import Flask, redirect, url_for, render_template, request, send_file
import requests


error = "Wikipedia does not have an article with this exact name."

url = {'url': "https://en.wikipedia.org/wiki/Drake_(musician)"}
post = {'url': "https://en.wikipedia.org/wiki/Drake_(musician)", 'language': "Japanese"}
print(post['url'], post['language'])

r = requests.post('https://wikiscraperproject.herokuapp.com/', data=url)
print(r.text)
print(r)
