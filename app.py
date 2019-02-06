#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:39:16 2019

@author: Fabiana
"""

#########################################################

# CHAPTER 17 - DEPLOYING MY FIRST APP

########################################################


#-----------------------------
# Task 1 - Create my app
#-----------------------------


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")




if __name__ == "__main__":
    app.run(debug=True) 





 