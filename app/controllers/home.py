# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for

blueprint = Blueprint('home', __name__)

@blueprint.route('/home')
def index():
    return render_template("home/Home.html")

@blueprint.route('/signuptemplate')
def signup():
    return render_template("accounts/Signup.html")

@blueprint.route('/logintemplate')
def login():
    return render_template("accounts/Login.html")

@blueprint.route('/usertemplate')
def user_template():
    return render_template("auction/users.html")

@blueprint.route('/productformtemplate')
def product_form():
    return render_template("auction/ProductForm.html")
