import json

import pandas as pd
import streamlit as st
from pycaret.classification import load_model, predict_model

st.set_page_config(
    page_title="Doctor Grade",
)

model = load_model("./src/models/LGBMClassifier")
with open("./output/ccr_teachers.json", "r", encoding="utf-8", errors="ignore") as f:
    ccr_teachers = json.load(f)

with open(
    "./output/class_attendance.json", "r", encoding="utf-8", errors="ignore"
) as f:
    class_attendance = json.load(f)


def predict(model, input_df):
    predictions_data = predict_model(estimator=model, data=input_df)
    return predictions_data


def run():
    ccr = st.selectbox(
        "CCR",
        placeholder="Selecione um CCR",
        options=ccr_teachers.keys(),
        index=None,
    )

    teacher = st.selectbox(
        "Professor",
        placeholder="Selecione um professor",
        options=ccr_teachers[ccr] if ccr else [],
        index=None,
    )

    attendence = st.select_slider(
        "Frequência (%)",
        options=class_attendance["class_attendance"],
        value=100,
        format_func=lambda x: f"{x}%",
    )

    class_period = st.selectbox(
        "Turno",
        placeholder="Selecione um turno",
        options=["NOTURNO", "VESPERTINO"],
        index=None,
    )

    input_dict = {
        "ccr": ccr,
        "nome_docente": teacher,
        "freq_turma": attendence,
        "turno": class_period,
    }

    input_df = pd.DataFrame([input_dict])

    if st.button("Prever"):
        output_df = predict(model=model, input_df=input_df)

        status = "Aprovado" if output_df["prediction_label"][0] == 0 else "Reprovado"

        st.success(
            f"O aluno foi classificado como '{status}' com uma confiança de {output_df['prediction_score'][0] * 100:.2f}%. "
            "Isso representa o grau de certeza do modelo na previsão, mas lembre-se: notas dependem de muitos fatores além da estatística! 📚"
        )

        st.warning(
            "Aviso: O modelo faz previsões com base em padrões, mas o resultado real pode variar. "
            "Ir às aulas é importante, mas o desempenho final também depende de outros fatores, como método de ensino e preparo individual. "
            "Nem todo mundo começa do mesmo ponto – alguns já chegam com medalhas da OBMEP. 😉"
        )


if __name__ == "__main__":
    run()
