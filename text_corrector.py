import openai
import pyperclip

def correct_text(prompt_suffix):
    openai.api_key = "key"

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

    pyperclip.copy(generated_text)
    print(generated_text)

    generated_text = generated_text[2:]

    return generated_text

correct_text("ELEVADOR DETENIDO EN EL PISO 5 CON PUERTAS CERRADA. SE REALIZO REVISION  MANTENIA FALLA ELECTRONICA EN EL DRIVE. SE NORMALIZO FUNCIONAMIENTO  SE VERIFICO  FUNCIONAMIENTO  ELEVADOR QUEDA OPERATIVO.")
