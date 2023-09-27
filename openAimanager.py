import openai

class OpenAiAgent:
    def __init__(self,apiKey,initialPrompt) -> None:
        self.apiKey = apiKey
        self.initialPrompt = initialPrompt
        
    
    def createCompletion(self,prompt):
        finalPrompt = self.initialPrompt +" "+ prompt
        response = openai.Completion.create(
            engine="davinci",  # Specify the engine (e.g., "davinci" for general text completions)
            prompt=finalPrompt,  # The text you want to complete
            max_tokens=500,  # The maximum number of tokens in the completion
            temperature=0.5,  # Controls the randomness of the output (0.2 for more focused, 1.0 for more random)
            n = 1 # Number of completions to generate
        )
        return response[0].text