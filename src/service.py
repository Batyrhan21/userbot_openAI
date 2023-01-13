import openai

from decouple import config
openai.api_key = config("OPENAI_API_KEY")


class OpenAIService:

    def openai_response(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            #  stop=["You:"]
            ) 
        return response['choices'][0]['text']