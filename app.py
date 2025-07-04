import os
import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from rag_utils import YoutubeVideoRAG

# Page configuration
st.set_page_config(
    page_title="Chat with YouTube Videos",
    page_icon="📽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Check for API key
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    st.error("⚠️ No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "rag_engine" not in st.session_state:
    st.session_state.rag_engine = None
if "video_url" not in st.session_state:
    st.session_state.video_url = ""
if "video_id" not in st.session_state:
    st.session_state.video_id = ""
if "video_processed" not in st.session_state:
    st.session_state.video_processed = False

def extract_video_id(url):
    """Extract YouTube video ID from URL."""
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    
    youtube_match = re.match(youtube_regex, url)
    if youtube_match:
        return youtube_match.group(6)
    return None

def get_transcript(video_id):
    """Get transcript from YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([t["text"] for t in transcript_list])
        return transcript_text
    except (TranscriptsDisabled, NoTranscriptFound):
        return None
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None

def process_video():
    """Process the YouTube video."""
    video_url = st.session_state.video_url
    
    if not video_url:
        st.warning("Please enter a YouTube video URL")
        return
    
    video_id = extract_video_id(video_url)
    if not video_id:
        st.error("Invalid YouTube URL. Please enter a valid YouTube video URL.")
        return
    
    st.session_state.video_id = video_id
    
    with st.spinner("Extracting video transcript..."):
        transcript = get_transcript(video_id)
        
    if not transcript:
        st.error("Unable to extract transcript for this video. The video might not have captions or they might be disabled.")
        return
    
    with st.spinner("Processing transcript with RAG..."):
        try:
            st.session_state.rag_engine = YoutubeVideoRAG(transcript, openai_api_key)
            st.session_state.video_processed = True
            st.session_state.chat_history = []
            st.success("Video processed successfully! You can now ask questions about the content.")
        except Exception as e:
            st.error(f"Error processing video: {str(e)}")

def handle_chat_input():
    """Handle chat input from user."""
    user_question = st.session_state.user_input
    
    if not user_question:
        return
    
    # Add user question to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    
    # Get response from RAG
    with st.spinner("Generating response..."):
        try:
            response = st.session_state.rag_engine.query(user_question)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
        except Exception as e:
            error_message = f"Error generating response: {str(e)}"
            st.session_state.chat_history.append({"role": "assistant", "content": error_message})
    
    # Clear input
    st.session_state.user_input = ""

# Sidebar
with st.sidebar:
    st.title("📽️ Chat with YouTube Videos")
    st.write("Chat with video content using RAG and OpenAI's GPT-4o")
    
    st.subheader("Enter YouTube URL")
    video_url = st.text_input("Paste URL here:", key="video_url", 
                              help="Enter the URL of a YouTube video you want to chat with")
    
    process_button = st.button("Process Video", on_click=process_video)
    
    if st.session_state.video_processed:
        st.success("Video Ready!")
        if st.session_state.video_id:
            st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")
    
    st.divider()
    st.markdown("""
    ### How it works
    1. Enter a YouTube video URL
    2. Wait for the transcript to be processed
    3. Ask questions about the video content
    4. Get AI-powered answers based on the video content
    
    This app uses RAG (Retrieval Augmented Generation) to provide accurate answers based on the video content.
    """)

# Main content
st.title("Chat with YouTube Videos")

if not st.session_state.video_processed:
    st.info("👈 Start by entering a YouTube URL in the sidebar and click 'Process Video'")
    
    # Example section
    st.markdown("### Example questions you can ask:")
    st.markdown("""
    Once you've processed a video, you can ask questions like:
    - What is the main topic of this video?
    - Can you summarize the key points?
    - What did the presenter say about [specific topic]?
    - Explain the concept discussed at the beginning of the video.
    """)
else:
    # Chat interface
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Assistant:** {message['content']}")
    
    # User input
    st.text_input("Ask a question about the video:", key="user_input", on_change=handle_chat_input)
