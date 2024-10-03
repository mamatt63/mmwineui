import streamlit as st
import requests
import json

MMWINEAPI = "https://mmwineapi-bkd8dug2axhpezct.francecentral-01.azurewebsites.net/"

BUTTON_HINT = "How good is it?"
BUTTON_DEFAULT_RESPONSE = "Click here to know 🍷"

def onclick_handler():
    response = requests.post(
        f"{MMWINEAPI}/predict",
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        json={'alcohol': st.session_state["alcohol"], 'volatile_acidity': st.session_state["volatile_acidity"]},
    )

    json_data = json.loads(response.json())
    if json_data["prediction"] == 1:
        result_string = f'Super good! (~{json_data["probability"][json_data["prediction"]]:.{0}f}%)'
    else:
        result_string = f'Smells not so good! (~{json_data["probability"][json_data["prediction"]]:.{0}f}%)'
    st.session_state["result"] = f"{BUTTON_HINT} {result_string}"

# this is the main function in which we define our webpage  
def main():
    st.markdown("# Wine Quality Prediction App 🍷🍇")
    st.markdown("### This app is meant to predict red wine quality " +
            "according to different chemical")

    volatile_acidity = st.slider('Volatile Acidity', 0.0, 2.0, 0.319, 0.001, key="volatile_acidity")
    st.text(f"User selected volatile acidity: {volatile_acidity}")
    alcohol = st.slider('Alcohol', 0.0, 16.0, 11.634, 0.01, key="alcohol")
    st.text(f"User selected alcohol: {alcohol}")

    if "result" in st.session_state:
        st.button(st.session_state["result"], on_click=onclick_handler, key="button_result")
    else:
        st.button(f"{BUTTON_HINT} {BUTTON_DEFAULT_RESPONSE}", on_click=onclick_handler, key="button_result")


# Init code
if __name__=='__main__': 
    main()
