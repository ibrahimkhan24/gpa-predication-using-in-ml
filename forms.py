import pandas as pd
from flask_wtf import FlaskForm
from wtforms import(
    SelectField,
    IntegerField,
    BooleanField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    NumberRange
)

#getting data

df=pd.read_csv("Final Year Project/student_data.csv",na_values=["nan"])
#df1=df.rename(columns={'previous_semester_GPA':'GPA'},inplace=True)
# df is the dataset that we train model 
drop_col=df.drop(columns=["GPA"])



class InputForm(FlaskForm):
    Family_size=IntegerField(
        label="Family_Size",
        validators=[DataRequired(), NumberRange(1,50)]
   )
    Parent_Edu_level=SelectField(
        label="Parent_Edu_Level",
        choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('High School', 'High School'), ('PhD', 'PhD')],
        validators=[DataRequired()]
    )
    Guardian=SelectField(
        label="Guardian",
        choices=[('Father', 'Father'), ('Mother', 'Mother')],
        validators=[DataRequired()]
    )
    Travel_time=IntegerField(
        label="Travel_Time",
        validators=[DataRequired(), NumberRange(1,180)]
    )
    Std_hr_per_week=IntegerField(
       label="Std_Hr_Per_Week",
       validators=[DataRequired(), NumberRange(1,50)]
    )
    Attendance=IntegerField(
       label="Attendance",
       validators=[DataRequired(), NumberRange(1,100)]
    )
    Activities=SelectField(
        label="Activities",
        choices=[('Sports', 'Sports'), ('Gaming', 'Gaming'), ('Other', 'Other')],
        validators=[DataRequired()]
    )
    Internet_access=SelectField(
       label="Internet_Access",
       choices=[('Yes', 'Yes'), ('No', 'No')],
       validators=[DataRequired()]
    )
    Family_support=SelectField(
       label="Family_Support",
       choices=[('Yes', 'Yes'), ('No', 'No')],
       validators=[DataRequired()]
    )
    Extra_tutor=SelectField(
       label="Extra_Tutor",
       choices=[('Yes', 'Yes'), ('No', 'No')],
       validators=[DataRequired()]
    )
    Parent_relationship_with_teacher=SelectField(
       label="Parrent_Relationship_with_teachers",
       choices=[('Yes', 'Yes'), ('No', 'No')],
       validators=[DataRequired()]
    )
    interest_in_field=SelectField(
       label="Interest_in_Field",
       choices=[('Yes', 'Yes'), ('No', 'No')],
       validators=[DataRequired()]
    )
    quizzes_per_semester=IntegerField(
       label="Quizzes_Per_Semester",
       validators=[DataRequired(), NumberRange(1,24)]
   )
    submit=SubmitField(label="Predict")