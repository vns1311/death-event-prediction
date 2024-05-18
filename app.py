import gradio
import joblib
import numpy as np

# Load your trained model

model = joblib.load('xgboost-model.pkl')

# Function for prediction

def predict_death_event(age: int, 
                        anaemia: bool,
                        creatinine_phosphokinase: float,
                        diabetes: bool,
                        ejection_fraction: float,
                        high_blood_pressure: int,
                        platelets: float,
                        serum_creatinine: float,
                        serum_sodium: float,
                        sex: bool,
                        smoking: bool,
                        time: int):
    sex_feat = 0 if sex == 'Woman' else 1
    feat_list = [age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, 
                 serum_creatinine,serum_sodium, sex_feat, smoking, time]
    print(feat_list)
    response = model.predict([feat_list])
    response_proba = model.predict_proba([feat_list])
    print(response)
    print(response_proba[0,0] if response[0] == 0 else response_proba[0,1])
    return int(response[0]), float(response_proba[0,0] if response[0] == 0 else response_proba[0,1])


# Gradio interface to generate UI link
title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gradio.Interface(fn = predict_death_event,
                         inputs =[
                              gradio.Slider(0, 100, value=40, label="Age", info="Provide the age"),
                              gradio.Radio([False, True], label="Anaemia", info="Decrease of red blood cells or hemoglobin"),
                              gradio.Slider(23, 7861, value=23, label="Creatinine phosphokinase (CPK)", info=" Level of the CPK enzyme in the blood"),
                              gradio.Radio([False, True], label="Diabetes", info="If the patient has diabetes"),
                              gradio.Slider(0, 100, value=14, label="Ejection fraction", info="Percentage of blood leaving the heart at each contraction"),
                              gradio.Radio([False, True], label="High Blood Pressure", info=" If a patient has hypertension"),
                              gradio.Slider(0, 850000, value=25000, label="Platelets", info="Platelets in blood"),
                              gradio.Slider(0, 10, value=0.5, label="Serum creatinine", info=" Level of creatinine in the blood"),
                              gradio.Slider(2, 200, value=113, label="Serum sodium", info=" Level of sodium in the blood"),
                              gradio.Radio(["Woman", "Man"], label="Sex", info="Select Gender"),
                              gradio.Radio([False, True], label="Smoker", info="Smoker or not?"),
                              gradio.Slider(2, 300, value=4, label="Time", info="Select follow-up period"),
                         ],
                         outputs = ["number", "number"],
                         title = title,
                         description = description,
                         allow_flagging='never')

iface.launch(share = False, quiet=False, debug=True, server_name="0.0.0.0", server_port = 8001)  # server_name="0.0.0.0", server_port = 8001   # Ref: https://www.gradio.app/docs/interface