
def entityNameAndCountryExtraction(recognizedText):
    for text in recognizedText:
        openParanthesisIdx = text.find("(")
        resultDictionary["entityName"].append(text[:openParanthesisIdx])
        closedParanthesisIdx = text.find(")")
        resultDictionary["country"].append(text[openParanthesisIdx+1:closedParanthesisIdx])
    return resultDictionary




recognizedText = ['Penna Banking Inc. (Barbados) \x0c', 'Animas Transaction services Inc. (Ohio) \x0c', 'Urastar Golden oppurtnity Corp. (British Columbia) \x0c', 'Urastar Golden Animas oppurtnity Transaction Corp. services (British Inc, (Ohio) Columbia)  Penna Banking Inc. (Barbados)    \x0c', 'Anico El MINES LIMITED (Ohio) (NYSE, TSX: AEM) \x0c', 'Anico El MINES LIMITED (Ohio) (NYSE, TSX: AEM)    \x0c']
resultDictionary = {"country":[],"entityName":[]}
entityNameAndCountryExtraction(recognizedText)
print(resultDictionary)
