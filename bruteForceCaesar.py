dictionary = open("/Users/Julio/Desktop/dict.txt", 'r')
dictionary = dictionary.read().split('\n')


def valid(phrase):
    sizeH = len(phrase)/2
    counter = 0
    for word in phrase:
        # if(counter > sizeH):
            # return True
        if word.lower() in dictionary:
            # print word
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
    # return result.replace("'", "")

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
        # print msgList[0]
        # valid(msgList)
        if(valid(msgList)):
            # print newMsg
            print "%s: %s"%(n,newMsg)   
        # if((msgList[0].lower() in dictionary) or (msgList[1].lower() in dictionary)):
            # print newMsg
        # print "%s: %s"%(n,newMsg)              


# print "Where".lower() in dictionary
# print dictionary.split('\n')
# print 'dolyl' in dictionary
msg1 = """Bmjwj mzrtw nx htshjwsji ymjwj fwj st xyfsifwix -- st tsj hfs xfd bmfy
nx ltti tw gfi, fqymtzlm dtz hfs gj xzwj ymfy jajwdtsj bnqq.
        -- Otms Pjssjym Lfqgwfnym"""

msg2 = """Ivnpsjtut bmxbzt tju bu uif dijmesfo't ubcmf.
        -- Xppez Bmmfo"""

msg3 = """Pa pzu'a uljlzzhyf av ohcl ylshapclz pu Rhuzhz Jpaf pu vykly av il buohwwf.
        -- Nyvbjov Thye"""


msgRicky = """ O ngbk g sgv ul znk Atozkj Yzgzky.  Oz'y gizagr yofk.  O yvktz rgyz yasskx
lurjotm oz.  Vkuvrk gyq sk cnkxk O robk, gtj O yge, "K6".
        -- Yzkbkt Cxomnz"""

#5 1 7
decaesar(makeOneLine(msg1))
print "-----------------------------------------"
print 
decaesar(makeOneLine(msg2))
print "-----------------------------------------"
print 
decaesar(makeOneLine(msg3))
print "-----------------------------------------"
print 

decaesar(makeOneLine(msgRicky))

#5 1 7

