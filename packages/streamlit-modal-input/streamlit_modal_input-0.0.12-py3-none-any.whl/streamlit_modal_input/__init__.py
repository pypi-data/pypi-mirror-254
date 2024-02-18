import streamlit.components.v1 as components
import os
import streamlit as st

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component("streamlit_modal_input",url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_modal_input", path=build_dir)
    

def modal_input(prompt='',firebase_client=None,key=None):

    if not key:
        key='modal_input'

    if not key+'_output' in st.session_state:
        st.session_state[key+'_output']=None

    if st.session_state[key+'_output'] is None:
        value=''
    else:
        value=st.session_state[key+'_output']

    config=firebase_client.config
    user=firebase_client.user
    collection="streamlit_modal_input"
    document=user.email
    
    if not key in st.session_state:
        listener=firebase_client.firestore.listener(collection,document,interval=0.5,timeout=300)
        listener.start()
        _component_func(prompt=prompt,projectId=config.projectId,apiKey=config.apiKey,idToken=user.idToken,collection=collection,document=document,value=value,enabled=True,key=key,default=None)
        data=listener.get_data()
        listener.stop()
        firebase_client.firestore.delete_document(collection,document)
        output=data.content
        st.session_state[key+'_output']=output
    else:
        _component_func(prompt=prompt,projectId=config.projectId,apiKey=config.apiKey,idToken=user.idToken,collection=collection,document=document,value=value,enabled=False,key=key,default=None)
        output=st.session_state[key+'_output']
    return output


if not _RELEASE:
    pass






    
