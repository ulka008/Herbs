#from io import BytesIO
#import pandas as pd
#import requests
#r = requests.get('https://colab.research.google.com/drive/16hKfEpLjZ3w5eXgEUzOM8qtucFronpPY?authuser=1#scrollTo=6COADZnAL7PU&line=9&uniqifier=1&output=csv')
#data = r.content
#df = pd.read_csv(BytesIO(data), index_col=0,)
#df.head()
##parse_dates=['Quradate']
##https://colab.research.google.com/drive/16hKfEpLjZ3w5eXgEUzOM8qtucFronpPY?authuser=1#scrollTo=6COADZnAL7PU&line=9&uniqifier=1 - CSV File
##/content/drive/MyDrive/Plants_python/Maturity.gsheet



import pandas as pd
##!pip install pandas


df = pd.read_excel("/content/Maturity.xlsx")
print (df)


x = list(df['Name: '])
y = list(df['Days to Maturity'])