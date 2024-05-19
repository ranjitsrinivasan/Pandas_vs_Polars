import pandas as pd
import time

print('Load - Start')
start_time = time.perf_counter()
df = pd.read_csv("airline_delay/2019.csv")
end_time = time.perf_counter()
print('Load - End')

print("Data loading duration: ")
print(end_time-start_time)

print(df.shape)
print(df.head(5))

start_time = time.perf_counter()
df_ATL = df[df['ORIGIN']=='ATL']
end_time = time.perf_counter()
print("**********  Filter ALT Duration: *********")
print(end_time-start_time)

print('df_ALT')
print(df_ATL.shape)

start_time = time.perf_counter()
df_SFO = df[df['ORIGIN']=='SFO']
end_time = time.perf_counter()
print("**********  Filter SFO Duration: *********")
print(end_time-start_time)

print('df_SFO')
print(df_SFO.shape)

start_time = time.perf_counter()
df_groupBy = df.groupby("OP_UNIQUE_CARRIER").agg({"OP_CARRIER_FL_NUM":'count'})
end_time = time.perf_counter()

print("**********  Group By Duration: *********")
print(end_time-start_time)

# &&&&&&&&&&&&&&&&&&&&&&& ##

#Data loading Duration:
#7.084851799998432

#**********  Filter ALT Duration: *********
#0.32301280001411214

#**********  Filter SFO Duration: *********
#0.30599640001310036

#**********  Group By Duration: *********
#0.2247436000034213


