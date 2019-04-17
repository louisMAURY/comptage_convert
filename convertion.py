list_number = []

with open("dict-conv-chiffre.txt" , "r" , encoding = "utf8") as dictionary:
    content = dictionary.readlines()





user_input_literal = input("Entrez votre numéro (en lettre): ")

def calcul(input_literal , the_dic):
    for element in the_dic:
        result = element.strip("\n")
        list_number.append(result)

    new_sentence = input_literal.replace(" " , "-")
    worklist = new_sentence.split("-")

    index_plus = 0
    for word in worklist:
        for number in list_number:
            if word == number:
                
                print(find)
            else:
                print("ERREUR")

calcul(user_input_literal , content)
