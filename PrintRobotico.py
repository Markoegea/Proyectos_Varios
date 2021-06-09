import os
import asyncio
def clear(): return os.system('cls')

async def customPrint(text):
    newText = ""
    for char in text:
        newText += char
        clear()
        print(newText)
        await asyncio.sleep(0.1)
    return True

text = "Hola Mision TIC 2022 \n"
asyncio.run(customPrint(text))
#"Hola Misión TIC 2022... soy <nombre del estudiante>"
