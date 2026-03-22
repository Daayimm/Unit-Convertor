from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LENGTH_TO_METER =  {
      'millimeter': 0.001,
      'centimeter': 0.01,
      'meter': 1,
      'kilometer': 1000,
      'inch': 0.0254,
      'foot': 0.3048,
      'yard': 0.9144,
      'mile': 1609.344
  }


WEIGHT_TO_KILOGRAM = {
    'milligram': 0.000001,
    'gram': 0.001,                                                                                  
    'kilogram': 1,
    'ounce': 0.0283495,                                                                       
    'pound': 0.453592
}


@app.route('/')
def home():
    return render_template('LengthConvertor.html')

@app.route('/length')
def length():
    return render_template('LengthConvertor.html')

@app.route('/weight')
def weight():
    return render_template('WeightConvertor.html')

@app.route('/temp')
def temp():
    return render_template('TempConvertor.html')

@app.route('/result')
def result():
    return render_template('resultPage.html')



@app.route('/convert/length', methods =['POST']) 
def lengthConvert():
    data = request.json
    value = float(data['value'])
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    
    in_meters = value * LENGTH_TO_METER[from_unit]
    result =  in_meters / LENGTH_TO_METER[to_unit]
    return jsonify({'result':result})




@app.route(('/convert/weight'),methods = ["POST"])
def weightConvert():
    data = request.json
    value = float(data["value"])
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    
    in_kilo = value * WEIGHT_TO_KILOGRAM[from_unit]
    result =  in_kilo / WEIGHT_TO_KILOGRAM[to_unit]
   
    return jsonify({'result': result})  
    
@app.route('/convert/temp',methods=["POST"])
def tempConvertor():
    data = request.json
    value = float(data["value"])
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    
    in_celcius = ConvertToCelcius(value,from_unit)
    result = ConvertToUnit(in_celcius,to_unit)
    return jsonify({'result':result})


    
    
def ConvertToCelcius(value,from_unit):
    if from_unit == 'celcius':
        return value
    elif from_unit == 'fahrenheit':
       return (value-32) * (5/9) 
   
    elif from_unit == 'kelvin':
       return value- 273.15  
    
def ConvertToUnit(value,to_unit):
    if to_unit == 'celcius':
        return value
    elif to_unit =='fahrenheit':
        return (value* 9/5) + 32
    elif to_unit == 'kelvin':
        return value + 273.15



if __name__ == '__main__':
      app.run(debug=True)    
    
    