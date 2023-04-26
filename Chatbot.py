import openai
import re
import random

#Put your open ai api key below 
openai.api_key = "OpenAi API Key"

model_engine = "text-davinci-002"
model_prompt = ("Please paraphrase the following sentence:\n"
                "Input sentence: {}"
                "\nParaphrased sentence:")

def paraphrase(sentence):
    prompt = model_prompt.format(sentence)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    paraphrased_sentences = response.choices[0].text.strip()
    paraphrased_sentences = re.sub(r"\s+", " ", paraphrased_sentences)
    paraphrased_sentences = paraphrased_sentences.replace("\n", "")
    paraphrased_sentences = paraphrased_sentences.split(".")
    paraphrased_sentences = [sentence.strip() for sentence in paraphrased_sentences]
    return paraphrased_sentences


sentence = input("Enter a sentence to paraphrase: ")
paraphrased_sentences = paraphrase(sentence)
print("Original sentence: ", sentence)
print("Paraphrased sentences: ")
for paraphrased_sentence in paraphrased_sentences:
    if paraphrased_sentence:
        print(paraphrased_sentence)
