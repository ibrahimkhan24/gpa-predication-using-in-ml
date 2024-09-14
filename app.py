from flask import Flask, url_for, render_template
from forms import InputForm
import pandas as pd
import joblib
#from custom_transformer import OutlierCap

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
# import model
model = joblib.load("linear_regression.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Students Performance Prediction Model")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            Family_size=[form.Family_size.data],
            Parent_Edu_level=[form.Parent_Edu_level.data],
            Guardian=[form.Guardian.data],
            Travel_time=[form.Travel_time.data],
            Std_hr_per_week=[form.Std_hr_per_week.data],
            Attendance=[form.Attendance.data],
            Activities=[form.Activities.data],
            Internet_access=[form.Internet_access.data],
            Family_support=[form.Family_support.data],
            Extra_tutor=[form.Extra_tutor.data],
            Parent_relationship_with_teacher=[form.Parent_relationship_with_teacher.data],
            interest_in_field=[form.interest_in_field.data],
            quizzes_per_semester=[form.quizzes_per_semester.data]
        ))
        prediction = model.predict(x_new)[0]
        if prediction > 4:
            prediction = 4
        message = f"The predicted GPA is {prediction}"
    else:
        message = "Please provide valid inputs"
    
    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
