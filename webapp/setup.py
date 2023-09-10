from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


@app.route('/')
def home():
        return render_template("index.html")




@app.route('/croprecommendation', methods=['GET', 'POST'])
def cr():
    if request.method == 'POST':

        return redirect(url_for('',))
    return render_template('croprec.html')



if __name__== "__main__":
    app.run(debug=True)