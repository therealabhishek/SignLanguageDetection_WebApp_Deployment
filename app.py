from signLanguage.logger import logging
from signLanguage.exception import SignException
import os,sys
from signLanguage.pipeline.training_pipeline import Trainpipeline
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64
from signLanguage.constants.application import APP_HOST, APP_PORT
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin


#if __name__ == '__main__':
#    obj = Trainpipeline()
#    obj.run_pipeline()
#    print("Executed Successfully.")


app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train")
def trainRoute():
    obj = Trainpipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)



@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera Starting!!"

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
    #app.run(host="127.0.0.1", port="8080")
