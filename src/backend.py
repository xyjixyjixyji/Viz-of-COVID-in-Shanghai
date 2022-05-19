from flask import *
from datetime import timedelta
from timeseries import return_dictionaries

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT']= timedelta(seconds=1)

@app.route("/")
def index():
    region_qz, pred_qz, region_wzz, pred_wzz = return_dictionaries()
    return render_template('index.html',
                            qz=region_qz,
                            wzz=region_wzz,
                            p_qz=pred_qz,
                            p_wzz=pred_wzz)
    
@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/district")
def district():
    return render_template('district.html')

@app.route("/sentiment")
def sentiment():
    return render_template('sentiment.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5290)
