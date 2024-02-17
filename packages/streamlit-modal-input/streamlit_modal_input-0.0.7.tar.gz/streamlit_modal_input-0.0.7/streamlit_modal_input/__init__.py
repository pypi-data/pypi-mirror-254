import os
import json
import streamlit.components.v1 as components
import os
from datetime import datetime
from queue import Queue
import streamlit as st
_root_=os.path.dirname(os.path.abspath(__file__))

def root_join(*args):
    return os.path.join(_root_,*args)

_RELEASE = True

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
        enabled=True
        value=''
    else:
        enabled=False
        value=st.session_state[key+'_output']

    collection="messages"
    document=datetime.now().isoformat()

    _component_func(prompt=prompt,firebase_config=firebase_client.config.to_dict(),idToken=firebase_client.user.idToken,collection=collection,document=document,value=value,enabled=enabled,key=key,default=None)

    if enabled:
        output=firebase_client.firestore.start_listening(collection,document,interval=1)
        firebase_client.firestore.delete_document(collection,document)
        st.session_state[key+'_output']=output
    else:
        output=st.session_state[key+'_output']
    return output


if not _RELEASE:
    pass




    
