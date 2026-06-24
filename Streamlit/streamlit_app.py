import streamlit as st
from utils import SentimentAnalyser

# Load Model
analyser_object = SentimentAnalyser(
    model_path="Streamlit/IMDB/SVM_model.joblib",
    vector_path="Streamlit/IMDB/Word2Vec_imdb_250.joblib"
)

# Page Config
st.set_page_config(
    page_title="Movie Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

# Header
st.title("🎬 Movie Review Sentiment Analyzer")

st.markdown(
    """
    Enter your movie review below and let AI determine whether the sentiment is
    **Positive 😊** or **Negative 😞**.
    """
)

# Input
user_review = st.text_area(
    "✍️ Enter your review:",
    height=250,
    placeholder="Write or paste your movie review here..."
)

# Live statistics
char_count = len(user_review)
word_count = len(user_review.split())

col1, col2 = st.columns(2)

with col1:
    st.metric("📝 Characters", char_count)

with col2:
    st.metric("📖 Words", word_count)

# Button
btn_click = st.button(
    "🔍 Analyze Sentiment",
    use_container_width=True
)

# Prediction
sentiment = ""

if btn_click:

    if len(user_review) > 50:

        with st.spinner("Analyzing your review..."):

            sentiment = analyser_object.prediction_pipeline(
                user_input=user_review
            )

    else:
        st.warning("⚠️ Please enter at least 50 characters.")

# Output
if sentiment:

    st.divider()

    if sentiment == "Positive":
        st.success("✅ Positive Review")
        st.balloons()

    else:
        st.error("❌ Negative Review")

    # Result Card
    with st.container(border=True):

        st.subheader("📊 Analysis Result")

        icon = "😊" if sentiment == "Positive" else "😞"

        st.markdown(
            f"""
            ### {icon} Sentiment: **{sentiment}**
            """
        )

    # Review Preview
    with st.expander("📄 Review Preview"):
        st.write(user_review)

    # Summary Message
    if sentiment == "Positive":
        st.info(
            "The review contains generally positive opinions and favorable expressions."
        )
    else:
        st.info(
            "The review contains generally negative opinions and unfavorable expressions."
        )

# Footer
st.markdown("---")
st.caption("Built with Streamlit • Word2Vec • SVM")