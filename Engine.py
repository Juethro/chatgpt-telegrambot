import openai

def bot(textt):
    api = open("API_openai.txt", 'r').read()

    openai.api_key = api

    prompt = textt+"?"

    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return(message)
