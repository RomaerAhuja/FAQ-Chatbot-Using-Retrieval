import streamlit as st
import sys
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add project root to Python's module search path
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.chatbot import FAQChatbot


st.set_page_config(
    page_title="CyberFAQ | AI Cybersecurity Assistant",
    page_icon="🔐",
    layout="centered"
)


@st.cache_resource
def load_chatbot():

    return FAQChatbot()


chatbot = load_chatbot()


if "messages" not in st.session_state:

    st.session_state.messages = []


st.markdown("""
<style>

.stApp {
    background-color: #0b0f19;
    color: #ffffff;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3 {
    color: #ffffff;
}

.stChatMessage {
    border-radius: 12px;
}

.stButton button {
    border-radius: 10px;
    border: 1px solid #374151;
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.title("🔐 CyberFAQ")

    st.subheader("About")

    st.write(
        "CyberFAQ is a hybrid retrieval-based "
        "cybersecurity FAQ chatbot."
    )

    st.divider()

    st.markdown("### Technology Stack")

    st.write("""
    - Python
    - TF-IDF
    - Sentence Transformers
    - Cosine Similarity
    - Hybrid Retrieval
    - Streamlit
    """)

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.caption("FAQ Chatbot Using Retrieval")


st.title("🔐 CyberFAQ")

st.caption(
    "Your AI-powered cybersecurity knowledge assistant."
)


if not st.session_state.messages:

    st.info(
        "Welcome to CyberFAQ! Ask me anything "
        "about cybersecurity."
    )

    st.markdown("### Suggested Questions")

    suggestions = [

        "What is cybersecurity?",

        "What is phishing?",

        "What is ransomware?",

        "Explain the CIA triad."

    ]

    for question in suggestions:

        if st.button(question, use_container_width=True):

            st.session_state.pending_query = question

            st.rerun()


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            if message.get("success"):

                st.caption(
                    f"Category: {message['category']}"
                )

                st.caption(
                    f"Hybrid similarity: "
                    f"{message['similarity']:.4f}"
                )

                st.caption(
                    f"TF-IDF score: "
                    f"{message['tfidf_score']:.4f}"
                )

                st.caption(
                    f"Semantic score: "
                    f"{message['semantic_score']:.4f}"
                )

                if message.get("source"):

                    st.markdown(
                        f"[View Source]({message['source']})"
                    )


user_query = st.chat_input(
    "Ask a cybersecurity question..."
)


if "pending_query" in st.session_state:

    user_query = st.session_state.pop("pending_query")


if user_query:

    st.session_state.messages.append({

        "role": "user",

        "content": user_query

    })

    with st.chat_message("user"):

        st.markdown(user_query)

    with st.chat_message("assistant"):

        with st.spinner("Searching knowledge base..."):

            responses = chatbot.get_multiple_answers(
                user_query
            )

        successful = [
            response
            for response in responses
            if response["success"]
        ]

        if not successful:

            st.markdown(
                "Sorry, I couldn't find a relevant answer "
                "in my knowledge base."
            )

            assistant_message = {

                "role": "assistant",

                "content": (
                    "Sorry, I couldn't find a relevant "
                    "answer in my knowledge base."
                ),

                "success": False

            }

        else:

            answer_parts = []

            for response in responses:

                if response["success"]:

                    answer_parts.append(
                        f"**{response['question']}**\n\n"
                        f"{response['answer']}"
                    )

                else:

                    answer_parts.append(
                        response["message"]
                    )

            combined_answer = "\n\n---\n\n".join(
                answer_parts
            )

            st.markdown(combined_answer)

            assistant_message = {

                "role": "assistant",

                "content": combined_answer,

                "success": True,

                "category": successful[0]["category"],

                "similarity": successful[0]["similarity"],

                "tfidf_score": successful[0]["tfidf_score"],

                "semantic_score": successful[0]["semantic_score"],

                "source": successful[0]["source"]

            }

        st.session_state.messages.append(
            assistant_message
        )

    st.rerun()