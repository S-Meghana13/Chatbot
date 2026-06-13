# # import streamlit as st
# # from chatbot import initialize_chatbot

# # st.set_page_config(
# #     page_title="AI Knowledge Assistant"
# # )

# # st.title("📚 AI Knowledge Assistant")

# # qa_chain = initialize_chatbot()

# # question = st.text_input(
# #     "Ask a question from your documents"
# # )

# # if question:

# #     with st.spinner("Searching..."):

# #         # answer = qa_chain.run(question)
# #         result = qa_chain.invoke({"input": question})
# #         answer = result["answer"]

# #         st.subheader("Answer")

# #         st.write(answer)

# import streamlit as st
# from chatbot import initialize_chatbot

# st.set_page_config(page_title="AI Knowledge Assistant")

# st.title("📚 AI Knowledge Assistant")

# qa_chain = initialize_chatbot()

# question = st.text_input("Ask a question from your documents")

# if question:

#     with st.spinner("Searching..."):

#         result = qa_chain.invoke({"input": question})
#         answer = result["answer"]

#         st.subheader("Answer")
#         st.write(answer)

import streamlit as st
from chatbot import initialize_chatbot

st.set_page_config(page_title="AI Knowledge Assistant")

st.title("📚 AI Knowledge Assistant")

chain = initialize_chatbot()

question = st.text_input("Ask a question from your documents")

if question:
    with st.spinner("Searching..."):
        answer = chain.invoke(question)

        st.subheader("Answer")
        st.write(answer)