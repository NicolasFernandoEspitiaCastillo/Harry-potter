Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0

quiz = [
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
     {
         "question" : "Entras en un jardín encantado. ¿Qué sería lo que más le interesaría examinar primero?",
         "options": [
            {
                "statement": "Las setas gordas rojas que parecen estar hablando entre sí", 
                "answer": "Ravenclaw"
            },
            {
                "statement": "El estanque burbujeante, en cuyas profundidades se arremolina algo luminoso",
                "answer": "Gryffindor"
            },
            {
                "statement": "El árbol de hojas de plata con manzanas doradas",
                "answer": "Slytherin"
            },
            {
                "statement": "La estatua de un viejo mago con un extraño centelleo en los ojos.",
                "answer": "Hufflepuff"
            }, 
         ]
     },
      {
         "question" : "Qué pesadilla te atemorizaría más?",
         "options": [
             
             {
                "statement": "Pararse encima de algo muy alto y darse cuenta de repente de que no hay puntos de apoyo para las manos ni para los pies, ni ninguna barrera para evitar que caiga.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Ser forzado a hablar con una voz tan tonta que casi nadie puede entenderte y todos se rien de ti.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Un ojo en el ojo de la cerradura de la habitacion oscura y sin ventanas en la que estas encerrado.",
                "answer": "Slytherin"
            },
            {
                "statement": "Despertar para descubrir que ni tus amigos ni tu familia tienen idea de quien eres.",
                "answer": "Hufflepuff"
            }, 
         ]
     },
]
def options(list):
    numeral = 0
    plantilla = ""
    while numeral < 4:
        plantilla += f"""\t {numeral+1}. {list[numeral].get("statement")} \n"""
        numeral += 1
    return plantilla


for value in quiz:
    print(f""" 
    {value.get("question")}

       {options(value.get("options"))}
    """)
    number = int(input("\t Ingrese su prespuesta: "))
    match value.get("options")[number-1].get("answer"):
        case "Gryffindor":
            Gryffindor += 1
        case "Hufflepuff":
            Hufflepuff += 1
        case "Slytherin":
            Slytherin += 1
        case "Ravenclaw":
            Ravenclaw += 1
        case _:
            print(":(")



print("Gryffindor: ", Gryffindor)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)
print("Ravenclaw: ", Ravenclaw)