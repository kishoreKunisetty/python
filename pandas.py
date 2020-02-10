#this is a practice for pandas.
# i feel it like a excel sheet only.
#stastics can also be done using pandas.
# files can be imported and exported in pandas.

#series datastructure examples in pandas
import pandas as pd
pd.Series(['kishore','is','my','name'])

#reindexing
import pandas as pd
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
cities=pd.DataFrame({'city':city_names,'population':population})
cities.reindex([0, 2, 1])

#these are the examples of DataFrame data structures of pandas
#for printing a table of 20 rows and 5 columns
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5))
print(df)

#for printing a table of names and numbers
import pandas as pd
df=pd.DataFrame({"names":['kishore','ram'],"numbers":['12','16']})#list of names can be predefined and used in dataframes
print(df)

#
