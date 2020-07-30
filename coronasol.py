from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
file=open('model.pkl','rb')
clf=pickle.load(file)
file.close()
@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        dict1=request.form
        fever=int(dict1['Fever'])
        age=int(dict1['Age'])
        pain=int(dict1['bodyPain'])
        runnynose=int(dict1['runnose'])
        difbreath=int(dict1['difBreath'])
        inputFeatures=[fever,pain,age,runnynose,difbreath]
        infProb=clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html',inf=infProb*100)
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)