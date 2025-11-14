import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

hablar("Hola mundo")
hablar("Soy un programa que habla")
hablar("Estoy aprendiendo a usar la síntesis de voz")