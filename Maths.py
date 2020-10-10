import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import csv
import statistics
import random
import pandas as pd 
df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()
#mean = statistics.mean(data)
#standarddeviation = statistics.stdev(data)
#print(mean,standarddeviation)
#fig = ff.create_distplot([data],['Math_score'],show_hist = False)
#fig.show()
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        #print(randomIndex)
        value = data[randomIndex]
        dataSet.append(value)
    sampleMean = statistics.mean(dataSet)
    return sampleMean
meanList = []
for i  in range (0,1000):
    setOfMeans = randomSetOfMean(100)
    meanList.append(setOfMeans)
standarddeviation1 = statistics.stdev(meanList)
mean1 = statistics.mean(meanList)
print(mean1,standarddeviation1)
#fig = ff.create_distplot([meanList],['students_marks'],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.20],mode = 'lines',name = 'mean'))
#fig.show()
ffds,fsde = mean1-standarddeviation1,mean1+standarddeviation1
sfds,ssde = mean1-(2*standarddeviation1),mean1+(2*standarddeviation1) 
tfds,tsde = mean1-(3*standarddeviation1),mean1+(3*standarddeviation1) 
#fig = ff.create_distplot([meanList],['studentMarks'],show_hist = False)
#ig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17],mode = 'lines',name = 'mean'))
#fig.add_trace(go.Scatter(x = [ffds,ffds],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
#fig.add_trace(go.Scatter(x = [fsde,fsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
#fig.add_trace(go.Scatter(x = [sfds,sfds],y = [0,0.17],mode = 'lines',name = 'standarddeviation2'))
#fig.add_trace(go.Scatter(x = [ssde,ssde],y = [0,0.17],mode = 'lines',name = 'standarddeviation2'))
#fig.add_trace(go.Scatter(x = [tfds,tfds],y = [0,0.17],mode = 'lines',name = 'standarddeviation3'))
#fig.add_trace(go.Scatter(x = [tsde,tsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation3'))
#fig.show()
#df1 = pd.read_csv('studentMarks1.csv')
#data1 = df1['Math_score'].tolist()
#sampleMean = statistics.mean(data1)
#fig = ff.create_distplot([meanList],['studentMarks'],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17],mode = 'lines',name = 'mean'))
#fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.17],mode = 'lines',name = 'mean of sample1'))
#fig.add_trace(go.Scatter(x = [fsde,fsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
#fig.show()
df2 = pd.read_csv('studentMarks2.csv')
data2 = df2['Math_score'].tolist()
sampleMean = statistics.mean(data2)
fig = ff.create_distplot([meanList],['studentMarks2'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17],mode = 'lines',name = 'mean'))
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.17],mode = 'lines',name = 'mean of sample2'))
fig.add_trace(go.Scatter(x = [fsde,fsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
fig.show()
df3 = pd.read_csv('studentMarks3.csv')
data3 = df3['Math_score'].tolist()
sampleMean = statistics.mean(data3)
fig = ff.create_distplot([meanList],['studentMarks3'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17],mode = 'lines',name = 'mean'))
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.17],mode = 'lines',name = 'mean of sample3'))
fig.add_trace(go.Scatter(x = [fsde,fsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
fig.show()
zscore = mean1-sampleMean/standarddeviation1
print(zscore)