from flask import Flask , request , jsonify

app = Flask(__name__)


@app.route('/xyz' , methods=['GET','POST'])   # @ is for annotation
def test():
    if(request.method == 'POST'):    #only the post method will pass
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/biswa' ,methods=['POST'])
def test1():
    if(request.method == 'POST'):    #only the post method will pass
        a = request.json['num3']
        b = request.json['num4']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/biswa/das' ,methods=['POST'])
def test2():
    if(request.method == 'POST'):    #only the post method will pass
        a = request.json['num4']
        b = request.json['num5']
        result = a+b
        return jsonify(str(result))

@app.route('/abcxyz' ,methods=['POST'])
def test3():
    if(request.method == 'POST'):    #only the post method will pass
        a = request.json['biswa']
        b = request.json['das']
        result = a+b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run()