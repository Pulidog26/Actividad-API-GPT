class Resumentexto:
    model_openai = "gpt-3.5-turbo"

    

    def __init__(self, api_key):
        self.api_key = api_key

    
    def resumeTranslate(self, text, language):
        from openai import OpenAI
        client = OpenAI(api_key = self.api_key)
        response = client.chat.completions.create(
            model = self.model_openai,
            messages = [
            {"role": "system", "content": "Resume and translate a text in approximately 10 sentences"},
            {"role": "user", "content": "Text to resume and translate into " + language + ": \n" + text},
            ]
        )
        respuesta = response.choices[0].message.content
        client.close()
        return respuesta