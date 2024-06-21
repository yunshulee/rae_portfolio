import streamlit as st
from PIL import Image
import exchange_rate as exR

st.sidebar.header("Login")
user_id = st.sidebar.text_input("ID", value="", max_chars=15)
user_pw = st.sidebar.text_input("Password", value="", type='password')

if user_id == "shuvlee" and user_pw == '17485':
    st.sidebar.header("Rae's portfolio")
    
    # sel_options=["",'17 is Right here!', 'Girl with a Pearl Earring', 'The Starry Night', 'The Scream of Nature', 'The tree of life', '월하정인']
    # name_painter=["", 'Going Seventeen','Johannes Vermeer', 'Vincent Van Gogh', 'Edvard Munch', 'Gustav Klimt', '신윤복']
    # user_opt = st.sidebar.selectbox("What's your favorite fine arts?", sel_options, index=1)
    # sel_index = sel_options.index(user_opt)
    # st.sidebar.write("The seleted fine art is ", user_opt)
    # st.sidebar.write("The painter of selected fine art is ", name_painter[sel_index])

    menu = st.sidebar.radio("Selcet the Menu", ['Exchange Rate Inquiry', 'EDA Inquiry', 'AI Classfication & Prediction'], index = None)

    if menu == 'Exchange Rate Inquiry':
        exR.exchange_main()
        st.sidebar.write("Exchange Rate Inquiry")
    elif menu == 'EDA Inquiry':
        st.sidebar.write("EDA Inquiry")
    elif menu == 'AI Classfication & Prediction':
        st.sidebar.write('AI Classfication & Prediction')
    else:
        st.sidebar.write("Please selcet the menu :)")

    # main
    st.subheader(menu, divider='rainbow')
    