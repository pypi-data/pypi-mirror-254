# streamlit-modal-input

Streamlit component providing a 'modal' text input widget (actually pausing the script until a string is entered and returned). Implemented using firestore for direct communication between backend and frontend. 

## Installation instructions

```sh
pip install streamlit-modal-input
```

## Usage instructions

```python
text=modal_input(
    prompt,
    firebase_credentials=None,
    firebase_config=None
)
```

Starts a firestore listener watching for changes in a specific firestore document. 
Renders a text input widget, whose output is routed to this firestore document.
Waits until the listener receives the output string.
Gets the string, closes the listener, deletes the firebase document.
Returns the string.

The python script will thus wait for the string to be received, achieving a similar behavior as regular python `input` function.

You first need to set up a firebase account and a firestore database for using this.

If you don't provide your firebase credentials and config directly to the component, it will attempt to get them from `st.secrets` (keys: `firebase_credentials` and `firebase_config`).

In such case your `secrets.toml` file should have these entries :

```toml
[firebase_credentials]
type=...
project_id=...
private_key_id=...
private_key=...
client_email=...
client_id=...
auth_uri=...
token_uri=...
auth_provider_x509_cert_url=...
client_x509_cert_url=...
universe_domain=...

[firebase_config]
apiKey=...
authDomain=...
projectId=...
storageBucket=...
messagingSenderId=...
appId=...
measurementId=...

```


## Example
```python
import streamlit as st
from streamlit_modal_input import modal_input

my_firebase_creds={
    ...
}

my_firebase_config={
    ...
}

text=modal_input(
    "Enter text here",
    firebase_credentials=my_firebase_creds,
    firebase_config=my_firebase_config
)

st.write(text)

#Or, assuming you provided yours credentials and config in st.secrets

text=modal_input("Enter text here")

st.write(text)

```