import os
from openai import OpenAI

class YoutubeVideoRAG:
    """Class to handle RAG for YouTube video transcripts using OpenAI directly."""
    
    def __init__(self, transcript, api_key=None):
        """
        Initialize the RAG engine with the transcript.
        
        Args:
            transcript (str): The transcript text from the YouTube video
            api_key (str, optional): OpenAI API key. Defaults to None.
        """
        self.transcript = transcript
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=self.api_key)
        
        # Truncate if transcript is too long
        max_tokens = 16000  # Maximum context length for gpt-4o
        self.truncated_transcript = self.transcript[:max_tokens]
    
    def query(self, question):
        """
        Query using OpenAI with the transcript as context.
        
        Args:
            question (str): The question to ask about the video content
            
        Returns:
            str: The answer to the question
        """
        try:
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024
                messages=[
                    {"role": "system", "content": """You are an AI assistant specialized in analyzing YouTube video content.
                    Answer the question based on the transcript provided.
                    Be detailed and specific, referring to the actual content from the video.
                    If the answer is not in the transcript, politely state that you don't have that information from the video.
                    Format your responses in a clear and readable way."""},
                    {"role": "user", "content": f"Here is the transcript of a YouTube video:\n\n{self.truncated_transcript}\n\nBased on this transcript, please answer the following question: {question}"}
                ],
                max_tokens=1000
            )
            
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error querying OpenAI: {str(e)}")
    
    def summarize(self):
        """
        Generate a summary of the video content.
        
        Returns:
            str: A summary of the video content
        """
        try:
            # Generate summary
            response = self.client.chat.completions.create(
                model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video content."},
                    {"role": "user", "content": f"Please provide a concise summary of the following video transcript. Focus on the main topics and key points:\n\n{self.truncated_transcript}"}
                ],
                max_tokens=1000
            )
            
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")
