# # # import os

# # # from dotenv import load_dotenv

# # # from langchain_community.vectorstores import FAISS
# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # from langchain.chains import RetrievalQA

# # # from utils.embeddings import get_embeddings

# # # load_dotenv()

# # # def initialize_chatbot():

# # #     embeddings = get_embeddings()

# # #     db = FAISS.load_local(
# # #         "vector_db",
# # #         embeddings,
# # #         allow_dangerous_deserialization=True
# # #     )

# # #     llm = ChatGoogleGenerativeAI(
# # #         model="gemini-1.5-flash",
# # #         google_api_key=os.getenv("GOOGLE_API_KEY"),
# # #         temperature=0.3
# # #     )

# # #     qa_chain = RetrievalQA.from_chain_type(
# # #         llm=llm,
# # #         retriever=db.as_retriever(search_kwargs={"k": 3})
# # #     )

# # #     return qa_chain

# # import os
# # from dotenv import load_dotenv

# # from langchain_community.vectorstores import FAISS
# # from langchain_google_genai import ChatGoogleGenerativeAI

# # from langchain.chains.retrieval import create_retrieval_chain
# # from langchain.chains.combine_documents import create_stuff_documents_chain
# # from langchain_core.prompts import ChatPromptTemplate

# # from utils.embeddings import get_embeddings

# # load_dotenv()

# # def initialize_chatbot():

# #     # Load embeddings (YOU KEEP THIS)
# #     embeddings = get_embeddings()

# #     # Load FAISS DB
# #     db = FAISS.load_local(
# #         "vector_db",
# #         embeddings,
# #         allow_dangerous_deserialization=True
# #     )

# #     # LLM
# #     llm = ChatGoogleGenerativeAI(
# #         model="gemini-1.5-flash",
# #         google_api_key=os.getenv("GOOGLE_API_KEY"),
# #         temperature=0.3
# #     )

# #     # Retriever
# #     retriever = db.as_retriever(search_kwargs={"k": 3})

# #     # Prompt template
# #     prompt = ChatPromptTemplate.from_template("""
# #     You are a helpful assistant.
# #     Use ONLY the context below to answer.

# #     Context:
# #     {context}

# #     Question:
# #     {input}
# #     """)

# #     # RAG chain
# #     combine_docs_chain = create_stuff_documents_chain(llm, prompt)

# #     qa_chain = create_retrieval_chain(
# #         retriever,
# #         combine_docs_chain
# #     )

# #     return qa_chain

# import os
# from dotenv import load_dotenv

# from langchain_community.vectorstores import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_core.prompts import ChatPromptTemplate
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains.retrieval import create_retrieval_chain

# from utils.embeddings import get_embeddings

# load_dotenv()

# def initialize_chatbot():

#     embeddings = get_embeddings()

#     db = FAISS.load_local(
#         "vector_db",
#         embeddings,
#         allow_dangerous_deserialization=True
#     )

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         google_api_key=os.getenv("GOOGLE_API_KEY"),
#         temperature=0.3
#     )

#     retriever = db.as_retriever(search_kwargs={"k": 3})

#     prompt = ChatPromptTemplate.from_template("""
#     You are a helpful assistant.
#     Answer only from the context.

#     Context:
#     {context}

#     Question:
#     {input}
#     """)

#     combine_docs_chain = create_stuff_documents_chain(llm, prompt)

#     qa_chain = create_retrieval_chain(
#         retriever,
#         combine_docs_chain
#     )

#     return qa_chain

import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from utils.embeddings import get_embeddings

load_dotenv()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def initialize_chatbot():

    embeddings = get_embeddings()

    db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI assistant.

    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {question}
    """)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain