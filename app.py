# save this as app.py
from flask import Flask, escape, request, render_template
import pickle

model = pickle.load(open("model_pickle.pkl", 'rb'))

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# @app.route('/analysis')
# def analysis():
#     return render_template("stroke.html")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        gender = request.form['gender']
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        disease = int(request.form['disease'])
        married = request.form['married']
        work = request.form['work']
        residence = request.form['residence']
        glucose = float(request.form['glucose'])
        bmi = float(request.form['bmi'])
        smoking = request.form['smoking']

        # gender
        if (gender == "Male"):
            gender_male=1
            gender_other=0
        elif(gender == "Other"):
            gender_male = 0
            gender_other = 1
        else:
            gender_male=0
            gender_other=0
        
        # married
        if(married=="Yes"):
            married_yes = 1
        else:
            married_yes=0

        # work  type
        if(work=='Self-employed'):
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 1
            work_type_children=0
        elif(work == 'Private'):
            work_type_Never_worked = 0
            work_type_Private = 1
            work_type_Self_employed = 0
            work_type_children=0
        elif(work=="children"):
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children=1
        elif(work=="Never_worked"):
            work_type_Never_worked = 1
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children=0
        else:
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children=0

        # residence type
        if (residence=="Urban"):
            Residence_type_Urban=1
        else:
            Residence_type_Urban=0

        # smoking sttaus
        if(smoking=='formerly smoked'):
            smoking_status_formerly_smoked = 1
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0
        elif(smoking == 'smokes'):
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 1
        elif(smoking=="never smoked"):
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 1
            smoking_status_smokes = 0
        else:
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0

        feature = [[age, hypertension, disease, glucose,married_yes]]

        prediction = model.predict(feature)[0]
        print(prediction) 
        # 
        if prediction==0:
            prediction = "YES" 
        else:
            prediction = "NO" 

        return render_template("index.html", prediction_text="Chance of Stroke Prediction is --> {}".format(prediction))   
         

    else:
        return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)
