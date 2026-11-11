import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.chatbot import FAQChatbot


# Page configuration
st.set_page_config(
    page_title="CyberFAQ | AI Chatbot",
    page_icon="🔐",
    layout="centered"
)


# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return FAQChatbot()


chatbot = load_chatbot()


# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []


# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #58A6FF;
}

.subtitle {
    text-align: center;
    color: #AAB4C3;
    font-size: 15px;
}

.stChatMessage {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:

    st.title("🔐 CyberFAQ")

    st.markdown("---")

    st.subheader("About")

    st.write(
        "CyberFAQ is a retrieval-based chatbot "
        "that answers cybersecurity questions "
        "using a predefined knowledge base."
    )

    st.markdown("---")

    st.subheader("Technology")

    st.write("""
    - Python
    - Streamlit
    - Scikit-learn
    - TF-IDF
    - Cosine Similarity
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    st.caption("FAQ Chatbot Using Retrieval")


# Main heading
st.markdown(
    '<div class="title">🔐 CyberFAQ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Cybersecurity Knowledge Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# Welcome message
if not st.session_state.messages:

    st.info(
        "Welcome! Ask me anything about cybersecurity."
    )

    st.markdown("### Suggested Questions")

    suggestions = [
        "What is cybersecurity?",
        "What is phishing?",
        "What is ransomware?",
        "What is the CIA triad?"
    ]

    cols = st.columns(2)

    for index, question in enumerate(suggestions):

        with cols[index % 2]:

            if st.button(question, use_container_width=True):

                st.session_state.pending_query = question

                st.rerun()


# Display conversation history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("metadata"):

            metadata = message["metadata"]

            if metadata.get("category"):

                st.caption(
                    f"Category: {metadata['category']}"
                )

            if metadata.get("confidence") is not None:

                st.caption(
                    f"Similarity Score: "
                    f"{metadata['confidence']:.4f}"
                )

            if metadata.get("source"):

                st.markdown(
                    f"[View Source]({metadata['source']})"
                )


# Process user input
user_query = st.chat_input(
    "Ask a cybersecurity question..."
)

# Handle suggested question
if "pending_query" in st.session_state:

    user_query = st.session_state.pop("pending_query")


if user_query:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })

    # Retrieve chatbot response
    response = chatbot.get_answer(user_query)

    if response["success"]:

        answer = response["answer"]

        metadata = {
            "category": response["category"],
            "confidence": response["confidence"],
            "source": response["source"]
        }

    else:

        answer = response["message"]

        metadata = {
            "category": None,
            "confidence": response.get("confidence"),
            "source": None
        }

    # Save assistant response
    st.session_state.messages.append({

        "role": "assistant",

        "content": answer,

        "metadata": metadata

    })

    st.rerun()