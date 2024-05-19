import polars as pl
import time

print('Load - Start')
start_time = time.perf_counter()
df = pl.read_csv("airline_delay/2019.csv")
end_time = time.perf_counter()
print('Load - End')

print("Data loading Duration: ")
print(end_time-start_time)

print(df.shape)
print(df.head(5))

start_time = time.perf_counter()
df_ATL = df.filter(pl.col("ORIGIN")=="ATL")
end_time = time.perf_counter()
print("**********  Filter ALT Duration: *********")
print(end_time-start_time)

print('df_ALT')
print(df_ATL.shape)

start_time = time.perf_counter()
df_SFO = df.filter(pl.col("ORIGIN")=="SFO")
end_time = time.perf_counter()
print("**********  Filter ALT Duration: *********")
print(end_time-start_time)

print('df_SFO')
print(df_SFO.shape)

start_time = time.perf_counter()
df_groupBy = df.group_by("OP_UNIQUE_CARRIER").agg(pl.col("OP_CARRIER_FL_NUM").count())
end_time = time.perf_counter()

print("**********  Group By Duration: *********")
print(end_time-start_time)

# &&&&&&&&&&&&&&&&&&&&&&& ##

#Data loading Duration:
#1.4543509999930393

#**********  Filter ALT Duration: *********
#0.03441140000359155

#**********  Filter SFO Duration: *********
#0.023032600001897663

#**********  Group By Duration: *********
#0.32506200001807883
