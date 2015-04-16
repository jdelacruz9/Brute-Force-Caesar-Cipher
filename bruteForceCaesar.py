dictionary = open("dict.txt", 'r')
dictionary = dictionary.read().split('\n')


def valid(phrase):
    sizeH = len(phrase)/2
    counter = 0
    for word in phrase:
        if word.lower() in dictionary:
            counter = counter + 1
    if(counter > sizeH):
        return True
    else:
        return False

def makeOneLine(phrase):
    phrase = phrase.splitlines()
    result = ""
    for item in phrase:
        result = result + item

    return result

def decaesar(message):
    for n in range(1,27):
        newMsg = ""
        for letter in message:
            asciiNum = ord(letter)
            if(asciiNum >= 65 and asciiNum <= 90):
                asciiNum = (((asciiNum - 65)-n)+26)%26 + 65
                newLetter = chr(asciiNum)
                newMsg = newMsg + newLetter
            elif(asciiNum >= 97 and asciiNum <= 122):
                asciiNum = (((asciiNum - 97)-n)+26)%26 + 97
                newLetter = chr(asciiNum)
                newMsg = newMsg + newLetter
            else:
                newMsg = newMsg + letter
        msgList = newMsg.split(' ')
        if(valid(msgList)):
            print "%s: %s"%(n,newMsg)            

msg1 = """Bmjwj mzrtw nx htshjwsji ymjwj fwj st xyfsifwix -- st tsj hfs xfd bmfy
nx ltti tw gfi, fqymtzlm dtz hfs gj xzwj ymfy jajwdtsj bnqq.
        -- Otms Pjssjym Lfqgwfnym"""

msg2 = """Ivnpsjtut bmxbzt tju bu uif dijmesfo't ubcmf.
        -- Xppez Bmmfo"""

msg3 = """Pa pzu'a uljlzzhyf av ohcl ylshapclz pu Rhuzhz Jpaf pu vykly av il buohwwf.
        -- Nyvbjov Thye"""

decaesar(makeOneLine(msg1))
print "-----------------------------------------"
print 
decaesar(makeOneLine(msg2))
print "-----------------------------------------"
print 
decaesar(makeOneLine(msg3))
print "-----------------------------------------"
print 

