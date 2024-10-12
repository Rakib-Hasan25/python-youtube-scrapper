from flask import Flask,request,jsonify
import scraper
app= Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/gets-video",methods=['POST'])
def gets_video():
     data = request.get_json() # data come as json object
     video_title = data.get('title')  # Directly use .get to avoid KeyError in case 'title' key doesn't exist  
     print(video_title)
     videoarray = scraper.fetchvideo(video_title)
     return jsonify({'videoList':videoarray})     



if(__name__=="__main__"):
    app.run(debug=True)
