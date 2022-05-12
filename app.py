from flask import Flask, request, jsonify
from datetime import datetime


# load all csv files required


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    state = request.form.get('state')
    N = request.form.get('N')
    P = request.form.get('P')
    K = request.form.get('K')
    crop1 = request.form.get('crop1')
    crop2 = request.form.get('crop2')
    crop3 = request.form.get('crop3')
    crop4 = request.form.get('crop4')
    crop5 = request.form.get('crop5')
    crop6 = request.form.get('crop6')
    crop7 = request.form.get('crop7')
    crop8 = request.form.get('crop8')

# all these crops are strings.

    currentMonth = datetime.now().month()

    ''' CASE 1: If NPK value is passed :
        you will get crop1 to crop 8
        take npk find recommendation using  NPK euclidian
        create a dictionary of 8 crops
        put recommended crop in front
        fill rest value with "Null" string
        return jsonify(result) , Result is dictionary

        Case 2 : if N , P , K is None :
        find recommedation using state and currentMonth
        create a dictionary of 8 crops
        put recommended crop in front
        fill rest value with "Null" string
        return jsonify(result) , Result is dictionary
    '''

    if N is None:
        result = {
            'crop1': 'sugarcane',
            'crop2': 'paddy',
            'crop3': 'wheat',
            'crop4': 'mango',
            'crop5': 'guava',
            'crop6': 'pineapple',
            'crop7': 'mushroom',
            'crop8': 'beans'
        }
    else:

        result = {
            'crop1': 'sugarcane',
            'crop2': 'paddy',
            'crop3': 'wheat',
            'crop4': 'mango',
            'crop5': 'guava',
            'crop6': 'Null',
            'crop7': 'mushroom',
            'crop8': 'Null'
        }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
