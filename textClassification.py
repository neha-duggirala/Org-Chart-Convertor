resultDictionary = {"country":[],"entityName":[]}

def entityNameAndCountryExtraction(recognizedText):
    for text in recognizedText:
        openParanthesisIdx = text.find("(")
        resultDictionary["entityName"].append(text[:openParanthesisIdx])
        closedParanthesisIdx = text.find(")")
        resultDictionary["country"].append(text[openParanthesisIdx+1:closedParanthesisIdx])
    return resultDictionary




