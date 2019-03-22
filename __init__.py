
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template,  request, url_for, redirect
from compute import lstat_approx,nox_approx,crim_approx,ptratio_approx,rm_approx, wing_it
# ,url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    title =  "Modelling approach"
    paragraph = ['This page is dedicated to analysis of the Boston data set ', 'Upon first reading, it appears to be a supervised learning exercise with the added spice of performing a price distribution. The data is perfect at first glance, no nulls no missing values no incosistencies. Simply perfect. Or so it seems! ', 'Initially I have deployed a linear model from sklearn libraries with different combinations of features. Now, here is where the data hit the fan. The best I could squeeze out of this built in method was 70ish percent of a fit, which I deemed garbage. As a second iteration I have decided to individually match the variables to the target and perform a polynomial fit. This was a lot more attractive and simple to follow. Unfortunately to avoid overfitting while maintaining the integrity of the model this seemed futile because the trend I indentified with was supported by sparse data.','After cracking my head, I wanted to achieve a physical collapse of the data to match its narrative. I have achieved this by performming K-Means on the individual variables versus the target. Provided an elbow analyis of each fit according to metrics such as Silhouette, Calinski-Harabaz and Distortion. I have what I deemed to be a costy global convergence for each of my variables. This was not enough. I decided to do this repeatedly many times and compute the average centroids for the number of clusters deduced. Then I fit my quadratic and cubic lines to the data. So I am hovering around the average within reason. ', 'Conclusion, the produced distributions are a great indicator of the price individually. The CAVEAT my distributions have hard limits which they are bound by, also due to my decision to compute each value independently assumes independence. To react and produce a multivariable prediction, the mean of individual predictions are produced with the standard deviation as error. I have included all my work and testing in html files.']

    return render_template("index.html", title = title ,paragraph = paragraph )




@app.route('/about')
def aboutpage():

    title = "About this site"
    paragraph = ["Greg Toth" , "BSc Theoretical Physics", "+353877960411"]
    pageType = 'about'

    return render_template("index.html", title = title, paragraph = paragraph, pageType = pageType )


@app.route('/about/contact')
def contactpage():

    title = "About this site"
    paragraph = ["Contact info" , "Motivation", "Goals"]
    pageType = 'about'

    return render_template("index.html", title = title, paragraph = paragraph, pageType = pageType )


@app.errorhandler(404)
def page_not_found(e):

    return render_template("404.html")

@app.errorhandler(405)
def method_not_found(e):

    return render_template("405.html")


@app.route('/calculate/', methods=["GET","POST"])
def calculate_page():
    Result = 0
    try:
        if request.method == "POST":

            attempted_nox = request.form['nox']
            attempted_rm = request.form['rm']
            attempted_lstat = request.form['lstat']
            attempted_crim = request.form['lstat']
            attempted_ptratio = request.form['lstat']







            if attempted_ptratio==12:
                return redirect(url_for('about'))


            else:
                pageType="submitted"

                attempted_lstat = round(lstat_approx(float(attempted_lstat)),2)
                attempted_rm = round(rm_approx(float(attempted_rm)),2)
                attempted_nox = round(nox_approx(float(attempted_nox)),2)
                attempted_crim = round(crim_approx(float(attempted_crim)),2)
                attempted_ptratio = round(ptratio_approx(float(attempted_ptratio)),2)

                price, std = wing_it(attempted_lstat, attempted_rm, attempted_nox, attempted_crim, attempted_ptratio)


            price = str(price)


        return render_template("calculate.html" )

    except Exception as e:

        return render_template("calculate.html", Result = price, Sdev= std, pageType = pageType)



@app.route('/login/', methods=["GET","POST"])
def login_page():

    error = ''
    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))

            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)

if __name__ == "__main__":
    app.run(debug=True)













