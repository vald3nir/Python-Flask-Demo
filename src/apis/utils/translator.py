from googletrans import Translator

def translate_text(message):
    translator = Translator()
    result = translator.translate(message, src='en', dest='pt')
    return result.text