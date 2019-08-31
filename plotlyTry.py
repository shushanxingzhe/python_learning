import pandas as pd
import cufflinks as cf

cf.go_offline(connected=False)

data = {
        'Team':['LA','NY','SF','HT'],
        'First Score': [100, 90, 65, 95],
        'Second Score': [30, 45, 68, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [86, 76, 50, 65]}

df = pd.DataFrame(data)
df = df.sort_values(by=['First Score'])
df.iplot(x='Team')
