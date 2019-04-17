with open("dict-conv-chiffre.txt" , "r" , encoding = "utf8") as dictionary:
    content = dictionary.readlines()

# The function remove de \n in element on "content" list
def rm_return(the_dic):
    for i in the_dic:
        result = i.strip("\n")
        print(result)
    return result

rm_return(content)