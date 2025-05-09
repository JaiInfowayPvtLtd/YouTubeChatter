# Getting Started with Chat with YouTube Videos

This quick guide will help you get up and running with the Chat with YouTube Videos application.

## What This App Does

This app lets you have a conversation with the content of any YouTube video. Simply:
1. Enter a YouTube URL
2. Process the video
3. Ask questions about what was said in the video

## Quick Setup

### Requirements
- Python 3.6+
- OpenAI API key

### Installation

1. **Get the code**:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages**:
   ```
   pip install youtube-transcript-api openai streamlit
   ```

3. **Set your OpenAI API key**:
   ```
   # On Linux/Mac
   export OPENAI_API_KEY="your-api-key-here"
   
   # On Windows (Command Prompt)
   set OPENAI_API_KEY=your-api-key-here
   
   # On Windows (PowerShell)
   $env:OPENAI_API_KEY="your-api-key-here"
   ```

4. **Start the app**:
   ```
   streamlit run app.py
   ```

## Using the App

1. **Enter a YouTube URL** in the sidebar text box
   - Make sure the video has captions available

2. **Click "Process Video"** button
   - The app will extract the transcript
   - You'll see a success message when it's ready

3. **Ask questions** using the chat box
   - Type your question and press Enter
   - The AI will search the video content for relevant information
   - Answers appear in the chat area

## Example YouTube Videos to Try

Here are some videos that work well with this app:

- TED Talks: https://www.youtube.com/watch?v=8S0FDjFBj8o
- Educational content: https://www.youtube.com/watch?v=DHjqpvDnNGE
- Product reviews: https://www.youtube.com/watch?v=2eJdYIl-qOQ

## Tips for Better Results

- **Be specific** with your questions
- **Refer to topics** discussed in the video
- For long videos, ask about **specific sections** or topics
- If you're not getting good answers, try **rephrasing** your question

## Troubleshooting

- **"No transcript found"**: The video might not have captions or they might be disabled
- **API key errors**: Make sure your OpenAI API key is set correctly
- **Slow responses**: Large transcripts take longer to process

## Need More Help?

Check the detailed [README.md](README.md) file for complete documentation or open an issue on the project repository.