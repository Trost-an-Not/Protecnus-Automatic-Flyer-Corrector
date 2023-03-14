import openai
import pyperclip

def find_list_start(rstring):
    for index, char in enumerate(rstring):
        #print(char, index)
        if char == "1":
            return index
    return 0 #if a single liner, no enumeration, thus no need to reformat


def correct_text(prompt_suffix):
    openai.api_key = "ENTER_YOUR_KEY"

    prompt_root = "Corregir, y enumerar las frases sin redundancia:"
    prompt = prompt_root + prompt_suffix

    model = "text-davinci-003"
    response = openai.Completion.create(
      engine=model,
      prompt=prompt,
      max_tokens=1000,
      temperature=0.2
    )

    generated_text = response.choices[0].text
    #print(generated_text)


    start_index = find_list_start(generated_text) #Finds start of the list

    if start_index:
        generated_text = generated_text[start_index:] #Avoids superfluous wording

    pyperclip.copy(generated_text)
    print(generated_text)

    return generated_text

#correct_text("puerta del piso E2 fuera de posición rolos de pasillo fuera del gripper se realizo ajuste general del mecanismo de puerta de pasillo se hizo prueba equipo operativo. ")
