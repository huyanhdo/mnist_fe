import streamlit as st
import requests
def main():
    PAGES = {
        'Model summary': model_summary,
        'Canvas': canvas
    }

def model_summary():
    pass 

def canvas():
    pass





if __name__ == '__main__':
    # st.sidebar(prim)
    st.sidebar.title('Digits predictor')

    st.sidebar.selectbox('Model',['Softmax regression','Neuron network',"CNN",'Softmax regression'])

    st.sidebar.selectbox('Mode',['Model summary','Canvas mode'])

    # print(st.session_state)
    # st.title('Digits predictor')



