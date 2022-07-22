from flask import Flask, request,jsonify, render_template
from data import *
from reg import *

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        ticker = request.form.get("ticker")
        period = request.form.get("period")
        df = modifyData(ticker, period)
        if df.empty == True:
            return ("Wrong ticker. Enter correct one.")
        else:
            return jsonify("mean_squared_error:{} and r2_score for the model: {}", model(df))

    else:
        pass
    
#Running the app
if __name__ == '__main__':
    app.run(debug=True)