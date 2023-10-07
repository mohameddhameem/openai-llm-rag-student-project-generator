import streamlit as st
import openai
import pandas as pd
import PyPDF2

# Replace with your OpenAI API key
api_key = "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"

# Initialize a conversation
conversation = [
    {"role": "system", "content": "You are a document generator."},
]

# Start the conversation with an initial message
def start_conversation():
    return [
        {"role": "system", "content": "You are a document generator."},
        {"role": "user", "content": "Generate a document based on the following data:"},
    ]

# Generate a document incrementally based on user prompts and chat responses
def generate_document_incrementally(conversation, user_prompt, reference_document, api_key):
    conversation.append({"role": "user", "content": user_prompt})

    if reference_document:
        conversation.append({"role": "system", "content": "Reference Document"})
        conversation.append({"role": "user", "content": reference_document})

    # Generate a response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        api_key=api_key,
    )

    # Extract the model's reply
    model_reply = response['choices'][0]['message']['content']

    return model_reply

# Streamlit UI
st.title("Incremental Document Generator")

# Initialize the conversation
conversation = start_conversation()

# User prompt input
user_prompt = st.text_input("User Prompt:")

# File upload for reference document
st.subheader("Upload a Reference Document (CSV or PDF)")
reference_document = None
file_type = None
uploaded_file = st.file_uploader("Choose a file...", type=["csv", "pdf"])
if uploaded_file:
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        reference_document = text
    elif file_type == "text/csv":
        df = pd.read_csv(uploaded_file)
        reference_document = df.to_string(index=False)

# Option to choose reference document
if reference_document:
    use_reference = st.checkbox("Use Reference Document")
else:
    use_reference = False

# Display a preview of the selected document
if reference_document and use_reference:
    st.subheader("Preview of the Reference Document")
    if file_type == "application/pdf":
        st.text(reference_document)  # Display PDF text
    elif file_type == "text/csv":
        st.text(reference_document)  # Display CSV text

if user_prompt:
    model_reply = generate_document_incrementally(conversation, user_prompt, reference_document if use_reference else None, api_key)
    st.write("Model:", model_reply)

    accept_response = st.radio("Do you accept this response?", ("Yes", "No"))
    if accept_response == "No":
        new_prompt = st.text_input("Provide a new prompt:")
        if new_prompt:
            conversation.append({"role": "user", "content": new_prompt})
    else:
        user_continue = st.radio("Do you want to continue?", ("Yes", "No"))
        if user_continue == "No":
            st.write("Conversation Ended")
