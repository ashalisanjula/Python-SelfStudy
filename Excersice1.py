givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
class TextAnalyzer(object):

    def __init__(self,text):

        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
    
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    
    def freqAll(self):

        wordList = self.fmtText.split(' ')

        freqMap = {}

        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap
    
    def freqOf(self,word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        

analyzed = TextAnalyzer(givenstring)
print("Formatted Text:", analyzed.fmtText)

freqMap = analyzed.freqAll()
print(freqMap)

word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")