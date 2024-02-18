import streamlit.components.v1 as components
import os
from datetime import datetime
from objdict_bf import objdict
from firebase_user import FirebaseClient
import time

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component("streamlit_modal_input",url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_modal_input", path=build_dir)
    

def modal_input(prompt='',client=None,key=None):

    if not key:
        key='modal_input'

    if not key+'_output' in st.session_state:
        st.session_state[key+'_output']=None

    if st.session_state[key+'_output'] is None:
        value=''
    else:
        value=st.session_state[key+'_output']

    config=client.config
    user=client.user
    collection="messages"
    document=user.email
    
    if not key in st.session_state:
        listener=client.firestore.listener(collection,document,interval=0.5)
        listener.start()
        _component_func(prompt=prompt,projectId=config.projectId,apiKey=config.apiKey,idToken=user.idToken,collection=collection,document=document,value=value,enabled=True,key=key,default=None)
        data=listener.get_data()
        listener.stop()
        output=data.content
        st.session_state[key+'_output']=output
    else:
        _component_func(prompt=prompt,projectId=config.projectId,apiKey=config.apiKey,idToken=user.idToken,collection=collection,document=document,value=value,enabled=False,key=key,default=None)
        output=st.session_state[key+'_output']
    return output


if not _RELEASE:

    import streamlit as st
    
    state=st.session_state

    if not 'client' in state:
        config=objdict.load("app_config.json")
        state.client=FirebaseClient(config,verbose=True)
        state.client.auth.sign_in("bferrand.maths@gmail.com","baptor314")

    txt=modal_input(client=state.client,key='modal_input')
    
    st.write(txt)

    st.button("click me")






    
