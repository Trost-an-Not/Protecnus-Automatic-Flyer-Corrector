import openai
import pyperclip

def find_list_start(rstring):
    for index, char in enumerate(rstring):
        #print(char, index)
        if char == "1":
            return index
    return 0 #if a single liner, no enumeration, thus no need to reformat


def correct_text(prompt_suffix):
    openai.api_key = "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"

    prompt_root = "Corregir, y ENUMERAR las frases, sin comentarios  por parte de la inteligencia artificial:"
    prompt = prompt_root + prompt_suffix

    conversation = []
    conversation.append({"role":"system", "content" : prompt})
    print(conversation)

    model = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
      model=model,
      messages=conversation,
      temperature=0.1
    )

    generated_text = response.choices[-1].message.content
    #print(generated_text)


    start_index = find_list_start(generated_text) #Finds start of the list

    if start_index:
        generated_text = generated_text[start_index:] #Avoids superfluous wording

    pyperclip.copy(generated_text)
    print(generated_text)

    return generated_text

correct_text("se buscara firma una vez completados todos los mantenimientos")
