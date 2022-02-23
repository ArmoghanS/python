from statistics import mode


def encoder(phrase):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    words=phrase.split()
    encoded_words=[]

    for word in words:
        word.replace(" ","")
        new_word=""
        for letter in word.lower():
            i=alphabet.index(letter)+1
            new_word+=alphabet[-i]
        encoded_words+=" "
        encoded_words+=new_word
    
    encoded_phrase="".join(encoded_words)
    print(encoded_phrase)
    return encoded_phrase

def decoder(phrase):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    words=phrase.split()
    decoded_words=[]
    for word in words:
        word.replace(" ","")
        new_word=""
        for letter in word.lower():
            i=alphabet.index(letter)+1
            new_word+=alphabet[-i]
        decoded_words+=" "
        decoded_words+=new_word
    
    decoded_phrase="".join(decoded_words)
    print(decoded_phrase)




encoded=encoder(input("Please input phrase to be encoded: "))
decoded=decoder(encoded)



