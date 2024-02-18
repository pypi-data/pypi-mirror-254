# streamlit-modal-input

Streamlit component providing a 'modal' text input widget (actually pausing the script until a string is entered and returned). Implemented using the [firebase-user](https://github.com/B4PT0R/firebase_user) package to establish direct communication between the python backend and the React frontend. 

It is meant first and foremost as a target widget for stdin redirection in case you wish to embed a live python interpreter in your streamlit app. 

Routing the interpreter's output to display widgets is fairly easy, but due to how Streamlit works, redirecting stdin to a widget in the app and achieving the expected blocking behavior was not that simple...

## Installation instructions

```sh
pip install streamlit-modal-input
```

## Usage instructions

This widget is meant to be used with the firebase-user package as follows.

You first declare a firebase user client with your firebase app json configuration file and authenticate your user:

```python
from firebase_user import FirebaseClient

if 'firebase_client' not in st.session_state:
    with open("app_config.json",'r') as f:
        config=json.load(f)
    st.session_state.firebase_client=FirebaseClient(config)
    st.session_state.firebase_client.auth.sign_in(user_email,user_password)

```
Then you can call the modal input widget, passing it the authenticated client.

```python
text=modal_input(
    prompt,
    firebase_client=st.session_state.firebase_client,
    key="my_modal_input"
    )
```

This will start a firestore listener thread watching for changes in a specific firestore document (collection='streamlit_modal_input',document=user.email). 

Obviously your user should have the suitable permissions to read and write to this document in your firestore security rules.

A custom input widget is then rendered on the frontend, whose output is routed to this firestore document (via the firebase REST API).

The main python script will wait for the listener to receive the string before resuming execution, achieving a similar behavior as regular python `input` function.

Note that this is a one-shot input: After the initial string has been received, the result will be memorized in session_state and subsequent reruns will show a disabled widget returning the same string again.

## Example
```python
import streamlit as st
from streamlit_modal_input import modal_input
from firebase_user import FirebaseClient

if 'firebase_client' not in st.session_state:
    with open("app_config.json",'r') as f:
        config=json.load(f)
    st.session_state.firebase_client=FirebaseClient(config)
    st.session_state.firebase_client.auth.sign_in(user_email,user_password)


text=modal_input(
    prompt,
    firebase_client=st.session_state.firebase_client,
    key="my_modal_input"
    )

#The rest of the script will execute only when the input string has been received from the frontend

st.write(text)

#Now click the button below to trigger a rerun and see what happens : the widget gets disabled, but still returns the same string you entered at first pass.

st.button("Rerun")


```