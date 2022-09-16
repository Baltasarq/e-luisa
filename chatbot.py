# ChatBot sample (c) 2022 Baltasar MIT License <baltasarq@uvigo.es>


# Temas comprendidos
NO_CLUE = "__NIPAPA__"

themes = {
    NO_CLUE:
        "Por favor, intenta explicarte mejor.",
    ("madre", "mami", "mamá", "papa"):
        "Cuéntame más sobre tu madre...",
    ("padre", "papi", "papá", "papa"):
        "Cuéntame más sobre tu padre...",
    ("mal", "enfermo", "enferma", "herido", "herida"):
        "Lo lamento. Creo que esto es importante. Por favor, continúa.",
    ("odio", "odie", "rencor", "odia", "odiaba", "odioso", "odiosa"):
        "No creo que sea tan grave. ¿Será una sensación tuya?",
    ("amor", "desamor", "apego", "cariño", "carino", "quiere", "ama"):
        "El amor puede significar equilibrio... o desequilibrio cuando se pierde.",
    ("decir", "dijo", "dice", "dices", "dijeron"):
        "Quizás se trata de algún malentendido.",
    ("animo", "ánimo", "triste"):
        "El estado de ánimo es muy personal. Sigue...",
    ("creer", "creo", "crea"):
        "Intenta ser positivo.",
    ("muerte", "matar", "mata", "morir", "muere", "muriendo", "matando"):
        "La muerte es cierta, pero podemos elegir cómo vivir.",
    ("entender", "entiendes", "entiende", "entiendo"):
        "Que alguien crea que no se le entiende es un evidente rasgo narcisista.",
    ("familia", "familiar", "familiares"):
        "La familia no se puede elegir.",
    ("amistad", "amigo", "amiga", "amigos", "amigas"):
        "Las amistades las elige cada uno, y por tanto también son responssabilidad de cada uno.",
    ("yo", "ego"):
        "No tomes todo lo que pasa como algo personal.",
    ("eleccion", "elección", "elegir", "posibilidad", "posibilidades"):
        "Aunque las elecciones puedan parecer complicadas, es todavía peor no tener elección.",
    ("hacer", "hago", "haces"):
        "No siempre es necesario hacer algo."
}


def look_up_theme(sentence):
    """Busca el tema comprendido según el argumento 'sentence'.
        :param sentence: La frase del usuario.
        :return: El tema comprendido.
    """
        
    def look_up_in_syns(word):
        toret = ""
        
        for syns in themes.keys():
            if word in syns:
                toret = themes[syns]
                break

        return toret


    toret = ""
    words = sentence.split()

    if len(words) > 0:
        for word in words:
            toret = look_up_in_syns(word)
            if toret:
                break

    return themes[NO_CLUE] if not toret else toret


def input_sentence():
    """Devuelve la entrada del usuario.
        :return: Un str limpio de delimitadores.
    """
    TRASH_CHARS = ".,.:-()/?¿¡!"
    sentence = input("> ").strip().lower()

    # Clean
    toret = ""
    
    for ch in sentence:
        if ch not in TRASH_CHARS:
            toret += ch

    return toret


if __name__ == "__main__":
    print("E-luisa")
    print("Por favor, dime algo sobre ti. [Pulsa ENTER para salir]")
    print()

    i = 0
    sentence = input_sentence()
    while(sentence):
        answer = look_up_theme(sentence)
        print(answer)

        i += 1
        if i > 7:
            print("Temo que se haya acabado el tiempo. Gracias por venir.")
            break
        
        sentence = input_sentence()
