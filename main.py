import streamlit as st
import openai
import pandas as pd
import PyPDF2
#from PyPDF2 import PageObject

# Replace with your OpenAI API key
api_key = ""

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

# Generate a document incrementally based on user prompts, chat responses, and retrieval results
def generate_document_incrementally(conversation, user_prompt, reference_documents, retrieval_query, api_key):
    conversation.append({"role": "user", "content": user_prompt})

    if retrieval_query:
        # Include a retrieval message in the conversation
        conversation.append({"role": "system", "content": "Retrieval"})
        conversation.append({"role": "user", "content": retrieval_query})

    for doc in reference_documents:
        conversation.append({"role": "system", "content": "Reference Document"})
        conversation.append({"role": "user", "content": doc})

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
st.title("Incremental Document Generator with Retrieval and Multiple Reference Documents")

# Initialize the conversation
conversation = start_conversation()

# User prompt input
user_prompt = st.text_input("User Prompt:")

# Retrieval query input
retrieval_query = st.text_input("Retrieval Query (Optional):")

# File upload for multiple reference documents
st.subheader("Upload Multiple Reference Documents (CSV or PDF)")
reference_documents = []
file_types = []
uploaded_files = st.file_uploader("Choose files...", type=["csv", "pdf"], accept_multiple_files=True)
for uploaded_file in uploaded_files:
    file_type = uploaded_file.type
    file_types.append(file_type)
    if file_type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            #page = PageObject.create_page(pdf_reader.pages[page_num])
            text += page.extract_text()
        reference_documents.append(text)
    elif file_type == "text/csv":
        df = pd.read_csv(uploaded_file)
        reference_documents.append(df.to_html(index=False))  # Convert CSV to HTML table

# Options to choose reference documents
if reference_documents:
    st.subheader("Select Reference Documents to Use")
    selected_reference_documents = st.multiselect("Select reference documents to include:", list(range(len(reference_documents))))
else:
    selected_reference_documents = []

# Display previews of selected reference documents
if reference_documents and selected_reference_documents:
    st.subheader("Previews of Selected Reference Documents (Right Side)")
    for idx in selected_reference_documents:
        if file_types[idx] == "application/pdf":
            st.image(uploaded_files[idx], use_column_width=True)  # Display PDF as an image
        elif file_types[idx] == "text/csv":
            st.write(reference_documents[idx], unsafe_allow_html=True)  # Display HTML table

if user_prompt:
    selected_reference_docs = [reference_documents[idx] for idx in selected_reference_documents]
    model_reply = generate_document_incrementally(
        conversation, user_prompt, selected_reference_docs, retrieval_query, api_key
    )

    # Display generated document text on the left side
    st.subheader("Generated Document (Left Side)")
    st.write(model_reply)

    accept_response = st.radio("Do you accept this response?", ("Yes", "No"))
    if accept_response == "No":
        new_prompt = st.text_input("Provide a new prompt:")
        if new_prompt:
            conversation.append({"role": "user", "content": new_prompt})
    else:
        user_continue = st.radio("Do you want to continue?", ("Yes", "No"))
        if user_continue == "No":
            st.write("Conversation Ended")
