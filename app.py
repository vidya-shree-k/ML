from flask import Flask,render_template,request,session


from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib


app = Flask(__name__)





@app.route('/')
def index():  # put application's code here
    return render_template('index.html')







@app.route('/prediction')
def prediction():  # put application's code here
        return render_template('prediction.html')

@app.route('/prediction1', methods=['POST', 'GET'])
def pred():
        global X_train, X_test, y_train, y_test
        a = []
        if request.method == "POST":
            v3 = request.form['v3']
            v4 = request.form['v4']
            v7 = request.form['v7']
            v9 = request.form['v9']
            v10 = request.form['v10']
            v11 = request.form['v11']
            v12 = request.form['v12']
            v14 = request.form['v14']
            v16 = request.form['v16']
            v17 = request.form['v17']
            a.extend([v3, v4, v7, v9, v10, v11, v12, v14, v16, v17])


            model = joblib.load('datamodel12.pkl')

            y_pred = model.predict([a])
            #acc3 = accuracy_score(y_test, y_pred)
            return render_template('prediction.html', op=y_pred,msg1="done")
        return render_template('prediction.html', msg1="notdone")












if __name__ == '__main__':
    app.secret_key='sairam'
    app.run(debug=True)