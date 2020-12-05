import pandas as pd
import numpy as np
import textClassification
recognizedText = ['Penna Banking Inc. (Barbados) \x0c', 'Animas Transaction services Inc. (Ohio) \x0c', 'Urastar Golden oppurtnity Corp. (British Columbia) \x0c', 'Urastar Golden Animas oppurtnity Transaction Corp. services (British Inc, (Ohio) Columbia)  Penna Banking Inc. (Barbados)    \x0c', 'Anico El MINES LIMITED (Ohio) (NYSE, TSX: AEM) \x0c', 'Anico El MINES LIMITED (Ohio) (NYSE, TSX: AEM)    \x0c']
def writeToExcel(recognizedText):
    df = pd.DataFrame(textClassification.entityNameAndCountryExtraction(recognizedText))
    print(df)

    df.to_excel("Samples/dataFrameOutput.xlsx",sheet_name='Sheet_name_1',)