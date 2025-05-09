# 📽️ Chat with YouTube Videos

This application allows you to chat with YouTube video content using OpenAI's GPT-4o model. It extracts the transcript from YouTube videos and uses AI to provide accurate answers to your questions based on the video content.

## Features

- **YouTube Transcript Extraction**: Automatically extracts the transcript from any YouTube video with available captions
- **AI-Powered Answers**: Uses OpenAI's GPT-4o model to understand and answer questions about the video content
- **Interactive Chat Interface**: User-friendly interface to ask questions and receive answers
- **Context-Aware Responses**: Responses are based specifically on the video content

## How It Works

The application uses a simple form of Retrieval Augmented Generation (RAG) to provide accurate answers:

1. **Transcript Extraction**: When you enter a YouTube URL, the app extracts the video's transcript using the YouTube Transcript API
2. **Context Processing**: The transcript is processed and prepared for the AI model
3. **Question Answering**: When you ask a question, the app sends the question along with the relevant transcript to OpenAI's GPT-4o model
4. **Response Generation**: The AI generates a response based on the actual content of the video

## Implementation Details

### Core Components

- **Streamlit**: Powers the web interface and user interactions
- **YouTube Transcript API**: Extracts transcripts from YouTube videos
- **OpenAI API**: Provides the AI capabilities for understanding and answering questions
- **RAG Implementation**: A custom implementation that provides the video transcript as context to the AI model

### Technical Architecture

The application consists of these main components:

1. **Main App (app.py)**: Contains the Streamlit interface, video processing logic, and chat handling
2. **RAG Utilities (rag_utils.py)**: Implements the YoutubeVideoRAG class that interfaces with OpenAI to process transcripts and generate answers

### Data Flow

1. User inputs a YouTube URL
2. App extracts the video ID and fetches the transcript
3. Transcript is processed and stored in the RAG engine
4. User asks questions through the chat interface
5. Questions are sent to the RAG engine along with the transcript context
6. AI-generated answers are displayed in the chat

## How to Use

### Prerequisites

- Python 3.6 or higher
- OpenAI API key

### Setup

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```
   pip install youtube-transcript-api openai streamlit
   ```

3. **Set Up OpenAI API Key**:
   Create an environment variable named `OPENAI_API_KEY` with your OpenAI API key

4. **Run the Application**:
   ```
   streamlit run app.py
   ```

### Usage Instructions

1. **Enter a YouTube URL**: Paste the URL of any YouTube video with available captions in the sidebar
2. **Process the Video**: Click the "Process Video" button to extract and process the transcript
3. **Ask Questions**: Once the video is processed, type your questions in the chat box
4. **Get Answers**: The AI will provide answers based on the content of the video

### Example Questions

- "What is the main topic of this video?"
- "Can you summarize the key points?"
- "What did the speaker say about [specific topic]?"
- "Explain the concept discussed at [specific timestamp]."

## Limitations

- Only works with YouTube videos that have available transcripts/captions
- The accuracy of answers depends on the quality and completeness of the transcript
- Maximum transcript length is limited (16,000 tokens) to fit within OpenAI's context window

## Technical Implementation Notes

### YoutubeVideoRAG Class

This is the core class that handles the RAG functionality:

- Initializes with a transcript and OpenAI API key
- Provides a `query` method to ask questions about the video
- Includes a `summarize` method to generate an overall summary of the video content

### YouTube Transcript Extraction

The transcript extraction uses the YouTube Transcript API and includes:

- Error handling for videos without transcripts
- Proper formatting of the extracted text
- URL parsing to extract the YouTube video ID

### Streamlit Interface

The Streamlit interface provides:

- A sidebar for video input and processing
- A main area for chat interaction
- Help text and example questions
- Visual feedback on the processing status

## Future Improvements

- Add support for multiple languages
- Implement chunk-based retrieval for longer videos
- Add visual elements extraction and analysis
- Support for user accounts and saved conversations
- Integration with additional video platforms