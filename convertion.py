list_number = []

with open("dict-conv-chiffre.txt" , "r" , encoding = "utf8") as dictionary:
    content = dictionary.readlines()


def find(number_find):
    list_number_finds = []
    list_number_finds.append(number_find)
    print(list_number_finds)


user_input_literal = input("Entrez votre numéro (en lettre): ")

def lecture(input_literal , the_dic):
    for element in the_dic:
        result = element.strip("\n")
        list_number.append(result)

    new_sentence = input_literal.replace(" " , "-")
    worklist = new_sentence.split("-")

    index_plus = 0
    for word in worklist:
        for number in list_number:
            if word == number:
                find(word)
            else:
                print("ERREUR")

lecture(user_input_literal , content)