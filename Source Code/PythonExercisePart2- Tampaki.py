# 
#Eirini- Maria Tampaki
# 15/12/2017
#
# Python Exercise
# Part 2
#
# Minimum Reached Runtime :  1.0103940963745117
#
#


# The necessary imports
import time
import pandas as pd

start = time.time()

# Read file 'cleaned_data_vol1.csv'
filePath = '/home/jovyan/work/assignment_datasets/cleaned_data_vol1.csv'
frame1 = pd.DataFrame()
frame1 = pd.read_csv(filePath, sep='\t', index_col=0, usecols=[0,3,20])

# Read file 'cleaned_data_vol2.csv'
filePath = '/home/jovyan/work/assignment_datasets/cleaned_data_vol2.csv'
frame2 = pd.DataFrame()
frame2 = pd.read_csv(filePath, sep='\t', index_col=0, usecols=[0,3,20])

# Dataframe outline
total1=len(frame1)
total2=len(frame2)

#Create groups
group1 = frame1.groupby(['V-GENE','AA JUNCTION'])
result1=pd.DataFrame(group1.size(),columns=['Reads1']).reset_index()

group2 = frame2.groupby(['V-GENE','AA JUNCTION'])
result2=pd.DataFrame(group2.size(),columns=['Reads2']).reset_index()

#Order group by reads
orderedOutput1=result1.sort_values(['Reads1'], ascending=False, kind='quicksort').reset_index(drop=True)
orderedOutput2=result2.sort_values(['Reads2'], ascending=False, kind='quicksort').reset_index(drop=True)

#Calculate reads/total
orderedOutput1['Reads1/Total1']=orderedOutput1['Reads1'].apply(str)+'/'+str(total1)
orderedOutput2['Reads2/Total2']=orderedOutput2['Reads2'].apply(str)+'/'+str(total2)

#Frequency %
pd.options.display.float_format = '{:,.4f}'.format
orderedOutput1['Relative Frequency1 %']= 100 * (orderedOutput1[['Reads1']]/total1)
orderedOutput2['Relative Frequency2 %']= 100 * (orderedOutput2[['Reads2']]/total2)

#Merge orderedOutput1 and orderedOutput1
publicOutput=pd.merge(orderedOutput1, orderedOutput2, on=['V-GENE','AA JUNCTION'], how='inner')
publicOutput['Mean Frequency %']=(publicOutput['Relative Frequency1 %']+publicOutput['Relative Frequency2 %'])/2

publicOutput.index = np.arange(1,len(publicOutput)+1)

# Save to file
outpoutFile = './tampaki_publicOutput.csv'
publicOutput.to_csv(outpoutFile, sep='\t')

stop = time.time()
print('Runtime: ' + str(stop-start))

# Confirmation code
# 
#
#import pandas as pd
#
# Read output file
# filePath = './tampaki_publicOutput.csv'
# frame = pd.DataFrame()
# frame = pd.read_csv(filePath, sep='\t', index_col=0)
#
# Dataframe outline
# frame.describe()
# frame.head()