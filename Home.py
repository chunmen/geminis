import streamlit as st
    
st.set_page_config(
    page_title="Gemini",
    page_icon="👋",
)


st.sidebar.success("Select a demo above.")
st.write("# Welcome to Gemini Streamlit! 👋")



st.markdown(
'''    
    Gemini demo
'''
)
#st.session_state.key = "AIzaSyDIhOkFHdO9gxEbgqIsSDEa96iXMRBJWa8"
#st.write("The key is:", st.session_state.key)
if "key" not in st.session_state:
    st.session_state.key ="AIzaSyDIhOkFHdO9gxEbgqIsSDEa96iXMRBJWa8"
    #st.session_state.key = None

##key = st.sidebar.text_input("Your key", type="password")
key =  st.session_state.key
if not key:
    st.info("Please add your key to continue.")
    st.stop()
else:
    st.session_state.key=key

