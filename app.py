import gradio as gr
# ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

import joblib
loaded_model = joblib.load('trained_model.pkl')
def predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):

#def predict(preg, plas, pres, skin, test, mass, pedi, age):
 #[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal), int(target)]])
 
 result = loaded_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])

 

 if result[0] == 1:
      return "The person has a heart condition."
 else:
      return "The person does not have a heart condition."

   # return str(result)

demo = gr.Interface(
    fn=predict,
    inputs=["text","text", "text", "text", "text", "text", "text", "text","text", "text", "text", "text", "text"],
    outputs=["text"],
)
demo.launch(debug=True)