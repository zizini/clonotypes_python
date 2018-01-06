# 
#Eirini- Maria Tampaki
# 15/12/2017
#
# Python Exercise
# Part 1
#
# Minimum Reached Runtime :
#			cleaned_data_vol1.csv: 0.6997416019439697
#			cleaned_data_vol2.csv: 0.6837320327758789
#
#


# The necessary imports
import time
import pandas as pd

#Start time
start = time.time()

# Read files
filePath = '/home/jovyan/work/assignment_datasets/cleaned_data_vol1.csv'
#filePath = '/home/jovyan/work/assignment_datasets/cleaned_data_vol2.csv'
frame = pd.DataFrame()
frame = pd.read_csv(filePath, sep='\t', index_col=0, usecols=[0,3,20])

# Dataframe outline
total=len(frame)
frame.describe()

#Create group
group = frame.groupby(['V-GENE','AA JUNCTION'])
result=pd.DataFrame(group.size(),columns=['Reads']).reset_index()

#Order group by reads
orderedOutput=result.sort_values(['Reads'], ascending=False, kind='quicksort').reset_index(drop=True)

#Calculate reads/total
orderedOutput['Reads/Total']=orderedOutput['Reads'].apply(str)+'/'+str(total)

#Frequency %
pd.options.display.float_format = '{:,.4f}'.format
orderedOutput['Frequency %']= 100 * (orderedOutput[['Reads']]/total)


orderedOutput.index = np.arange(1,len(orderedOutput)+1)

# Save to file
outpoutFile = './tampaki_output_v1.csv'
#outpoutFile = './tampaki_output_v2.csv'
orderedOutput.to_csv(outpoutFile, sep='\t')

#Calculate runtime
stop = time.time()
print('Runtime: ' + str(stop-start))



# Confirmation code
# 
#
#import pandas as pd
#
# Read output file
# filePath = './tampaki_output_v1.csv'
# filePath = './tampaki_output_v2.csv'
# frame = pd.DataFrame()
# frame = pd.read_csv(filePath, sep='\t', index_col=0)
#
# Dataframe outline
# frame.describe()
# frame.head()