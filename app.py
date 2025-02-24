import json

import pandas as pd
import streamlit as st
from pycaret.classification import load_model, predict_model

st.set_page_config(
    page_title="Doctor Grade",
    page_icon="🎓",
    layout="centered",
)


# CSS injection
def inject_custom_css():
    st.markdown(
        """
        <style>
        div[data-testid="stHeadingContainer"] {
            text-align: center;
        }
        .st-emotion-cache-1cvow4s {
            text-align: center;
        }
        [data-testid="stHeadingContainer"] h1, h2 {
            font-size: 3rem !important;
        }
        /* Add button container styling */
        .predict-button-container {
            display: flex;
            justify-content: center;
            margin: 1rem 0;
        }
        .predict-button-container > div {
            width: 200px !important;
        }
        .main-container {
            padding: 2rem;
            max-width: 1200px;
        }
        .stDataFrame {
            width: 100% !important;
            max-height: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Model class
class InferenceClass:
    def __init__(self, model_path: str = "./src/models/LGBMClassifier"):
        self.model = load_model(model_name=model_path)

    def predict(self, input_df):
        predictions_data = predict_model(estimator=self.model, data=input_df)
        return predictions_data


# Data loading
def load_data():
    with open(
        "./output/ccr_teachers.json", "r", encoding="utf-8", errors="ignore"
    ) as f:
        ccr_teachers = json.load(f)

    with open(
        "./output/class_attendance.json", "r", encoding="utf-8", errors="ignore"
    ) as f:
        class_attendance = json.load(f)

    return ccr_teachers, class_attendance


# Load data at module level
ccr_teachers, class_attendance = load_data()


# State management
def initialize_session_state():
    """Initialize session state variables if they don't exist"""
    if "input_df" not in st.session_state:
        # Initialize with empty dataframe containing correct columns
        st.session_state.input_df = pd.DataFrame(
            columns=["ccr", "nome_docente", "freq_turma", "turno"]
        )
    if "ccr" not in st.session_state:
        st.session_state.ccr = None
    if "teacher" not in st.session_state:
        st.session_state.teacher = None
    if "period" not in st.session_state:
        st.session_state.period = None
    # Removed attendance initialization since select_slider handles it


def update_dataframe():
    # Create dict with current values, using empty strings for None
    input_dict = {
        "ccr": st.session_state.ccr or "",
        "nome_docente": st.session_state.teacher or "",
        "freq_turma": st.session_state.attendance,
        "turno": st.session_state.period or "",
    }
    st.session_state.input_df = pd.DataFrame([input_dict])


# Main app function
def run():
    # Inject CSS before any other content
    inject_custom_css()

    # Inicializa as variáveis de estado da sessão
    initialize_session_state()
    st.header(body="🎓 Doctor Grade")

    # Create main container
    main_container = st.container()

    with main_container:
        # Create two columns for inputs
        col1, col2 = st.columns(2)

        with col1:
            ccr = st.selectbox(
                "CCR",
                placeholder="Selecione um CCR",
                options=ccr_teachers.keys(),
                index=None,
                key="ccr",
                on_change=update_dataframe,
            )

            attendence = st.select_slider(
                "Frequência (%)",
                options=class_attendance["class_attendance"],
                value=100,
                format_func=lambda x: f"{x}%",
                key="attendance",
                on_change=update_dataframe,
            )

        with col2:
            teacher = st.selectbox(
                "Professor",
                placeholder="Selecione um professor",
                options=ccr_teachers[ccr] if ccr else [],
                index=None,
                key="teacher",
                on_change=update_dataframe,
            )

            class_period = st.selectbox(
                "Turno",
                placeholder="Selecione um turno",
                options=["NOTURNO", "VESPERTINO"],
                index=None,
                key="period",
                on_change=update_dataframe,
            )

        # Always show dataframe container
        with st.container():
            st.dataframe(
                data=st.session_state.input_df,
                use_container_width=True,
                hide_index=True,
            )

        # Center the predict button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            predict_button = st.button(
                "Prever",
                use_container_width=True,
                disabled=not all([
                    st.session_state.ccr,
                    st.session_state.teacher,
                    st.session_state.attendance,
                    st.session_state.period,
                ]),
            )

    # Results container outside main_container
    results_container = st.container()
    with results_container:
        if predict_button and st.session_state.input_df is not None:
            output_df = InferenceClass().predict(input_df=st.session_state.input_df)
            status = (
                "Aprovado" if output_df["prediction_label"][0] == 0 else "Reprovado"
            )

            # Single column for messages
            message_col = st.columns(1)[0]
            with message_col:
                st.success(
                    f"O aluno foi classificado como '{status}' com uma confiança de {output_df['prediction_score'][0] * 100:.2f}%. "
                    "Isso representa o grau de certeza do modelo na previsão, mas lembre-se: notas dependem de muitos fatores além da estatística! 📚"
                )

                st.warning(
                    "Aviso: O modelo faz previsões com base em padrões, mas o resultado real pode variar. "
                    "Ir às aulas é importante, mas o desempenho final também depende de outros fatores, como método de ensino e preparo individual. "
                    "Nem todo mundo começa do mesmo ponto — alguns já chegam com medalhas da OBMEP. 😉"
                )


# Entry point
if __name__ == "__main__":
    run()
