import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write an email to my boss for resignation?"
    },
    {
      "role": "assistant",
      "content": "Subject: Resignation - Departure from [Company Name]\n\nDear [Boss's Name],\n\nI hope this email finds you well. I am writing to inform you about my decision to resign from my position at [Company Name]. It has been both a privilege and a pleasure working alongside such an incredible team under your leadership.\n\nAfter much consideration and reflection, I have come to the conclusion that it is time for me to explore new opportunities and challenges in my career. My last day at [Company Name] will be [date], in line with the notice period mentioned in my employment contract.\n\nThroughout my tenure at [Company Name], I have gained valuable experience, knowledge, and skills that have contributed to my professional growth. The guidance and support provided by yourself and the entire management team have been instrumental in my success.\n\nI would like to express my gratitude for the opportunities I have been given to contribute to the growth and success of the company. I have enjoyed being part of the team and witnessing the achievements we have accomplished together. I firmly believe that the company will continue to thrive and achieve even greater heights under your leadership.\n\nDuring the remaining period of my employment, I am committed to ensuring a smooth transition. I am prepared to assist with any necessary handover procedures and provide training or"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "chatcmpl-7kyR1JR1a1xE0otsUXPLPgc32Ik0i",
  "object": "chat.completion",
  "created": 1691429755,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "support to my replacement. Please let me know how I can best contribute to this process.\n\nI would also be grateful for any advice or suggestions you may have as I embark on this new chapter of my career. Your mentorship and guidance have been invaluable to me, and I will carry the lessons I have learned here with me throughout my professional journey.\n\nI would like to take this opportunity to thank you personally for your support, encouragement, and trust in me. Working under your leadership has been inspiring, and I appreciate the opportunities I have had to grow both professionally and personally.\n\nI will always look back on my time at [Company Name] with fond memories and a deep sense of gratitude. I will miss working with the amazing team here, but I am excited about the new challenges and opportunities that lie ahead.\n\nPlease let me know how I can assist in the transition process, and I will be more than happy to coordinate with you and the team. I am available to discuss any outstanding assignments or expectations you may have during this period.\n\nOnce again, thank you for everything, and I wish you and the entire team at [Company Name] continued success in all your future endeavors.\n\nYours sincerely,\n\n[Your Name]"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 276,
    "completion_tokens": 244,
    "total_tokens": 520
  }
}
'''
