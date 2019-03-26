
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template,  request, url_for, redirect
from compute import lstat_approx,nox_approx,crim_approx,ptratio_approx,rm_approx, wing_it
# ,url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    title =  "Modelling approach"
    paragraph = ["This page is dedicated to the price analysis of the Boston data set. ", "The plan is to model the housing prices with a selected number of features.The data is perfect at first glance, no nulls, no missing values nor discrepancies. Simply put, perfect. Or so it seems!", "Firstly, I have deployed a linear model from sklearn libraries with different combinations of features based on correlation and context. Now, here is where the data hit the fan. The built in solution arrived at circa 70% percent of a fit, which I conceived inadequate. Preprocessing came to mind.", "As a second iteration I have decided to individually match the variables to the target and compute a polynomial fit. This was more optimal and simple to follow, whilst yielding great effectiveness. Preprocessing maintained the profiles and normalized units as well as reducing variability and dissimilarities. Unfortunately, to avoid over fitting while maintaining the integrity of the model this seemed futile because the trend I identified with was supported by densely scattered data.", "After some thought, it occurred to me to plot pillars of each distribution. Global averages created by the dense groups of points. I have achieved this by performing K-Means on the individual variables versus the target. Following an elbow analyis of each fit according to Silhouette, Calinski-Harabasz and Distortion metrics. Some of the elbow analysis yielded results if and only if preprocessing took place such as PTRATIO and DIS. K-means is a greedy algorithm that I iterated over whilst recording the centroids of each run which I averaged to achieve global pillars of the individual distributions. Fits are only considered if a stable solution is obtained.  Then I plot my quadratic and cubic polynomials to the data. Thus, I have minimized error by reducing the effects of noise and outliers by the so called pillars of convergence", "Conclusion, the produced distributions are a great indicator of the price provided the following caveat. I assumed independence and features are therefore equally weighted in the production of the end result and the variables are bound by hard limits.The outcome is a strong predictor of price with a estimation error for a latent probability range."]

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


# @app.route('/calculate/', methods=["GET","POST"])
# def calculate_page():
#     result = ""
#     sdev = ""

#     try:
#         if request.method == "POST":

#             attempted_nox = request.form['nox']
#             attempted_rm = request.form['rm']
#             attempted_lstat = request.form['lstat']
#             attempted_crim = request.form['crim']
#             attempted_ptratio = request.form['ptratio']



#             if attempted_nox != 0:
#                 return redirect(url_for('about'))


#             else:
#                 pageType="submitted"

#                 # attempted_lstat = round(lstat_approx(float(attempted_lstat)),2)
#                 # attempted_rm = round(rm_approx(float(attempted_rm)),2)
#                 # attempted_nox = round(nox_approx(float(attempted_nox)),2)
#                 # attempted_crim = round(crim_approx(float(attempted_crim)),2)
#                 # attempted_ptratio = round(ptratio_approx(float(attempted_ptratio)),2)

#                 # price, std = wing_it(attempted_lstat, attempted_rm, attempted_nox, attempted_crim, attempted_ptratio)


#                 result = str(attempted_ptratio)
#                 sdev = str(attempted_ptratio)


#         return render_template("calculate.html", result = result, sdev=sdev )

#     except Exception as e:

#         return render_template("calculate.html", result = result, sdev= sdev)



@app.route('/calculate/', methods=["GET","POST"])
def login_page():

    error = ''
    try:

        if request.method == "POST":

            attempted_nox = request.form['nox']
            attempted_rm = request.form['rm']
            attempted_lstat = request.form['lstat']
            attempted_crim = request.form['crim']
            attempted_ptratio = request.form['ptratio']

            attempted_rm = round(rm_approx(float(attempted_rm)),2)
            attempted_lstat = round(lstat_approx(float(attempted_lstat)),2)
            # attempted_rm = round(rm_approx(float(attempted_rm)),2)
            attempted_nox = round(nox_approx(float(attempted_nox)),2)
            attempted_crim = round(crim_approx(float(attempted_crim)),2)
            attempted_ptratio = round(ptratio_approx(float(attempted_ptratio)),2)

            price, std = wing_it(attempted_lstat, attempted_rm, attempted_nox, attempted_crim, attempted_ptratio)
            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_nox == "admin" and attempted_rm == "password":
                return redirect(url_for('about'))

            else:
                error = str(attempted_rm)+" "+str(attempted_lstat)+" "+str(attempted_nox)+" "+str(attempted_crim)+" "+str(attempted_ptratio)
                error = str(round(price,2))+"  and error in sd  "+str(round(std,2))
        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)

if __name__ == "__main__":
    app.run(debug=True)













