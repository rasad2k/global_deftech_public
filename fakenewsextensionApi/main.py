from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
import pandas as pd 
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence


app = Flask(__name__)
cors = CORS(app=app)


@app.route('/create/',methods=['POST'])
def hello_world():
    print(request.json)
    if not request.json or not 'string' in request.json:
        return 'ERROR',404
    data = {
        'string': request.json['string'] 
    }

    max_len = 200

    df = pd.read_csv('dataset.csv',delimiter=',',encoding='latin-1')
    x = df.review
    token = Tokenizer(num_words=200)
    token.fit_on_texts(x)
    tex=list(data.values())

    model = keras.models.load_model("my_model.h5")

    seq_tex = token.texts_to_sequences(tex)
    matrix_tex = sequence.pad_sequences(seq_tex,maxlen=max_len)
    print(matrix_tex)
    y_pre=model.predict(matrix_tex)
    print("lmao", y_pre)
    return jsonify(str(y_pre)), 201

    



if __name__ == "__main__":
    app.run(debug=True)
