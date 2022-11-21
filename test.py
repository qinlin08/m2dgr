import pandas as ps
print("two txt must be named by test.txt and groudtruth.txt")
trajectory_data = ps.read_csv('./test.txt',sep=' ')
groudtruth_data = ps.read_csv('./groudtruth.txt',sep=' ')
base_line = groudtruth_data.values[0,0]
set_line = trajectory_data.values[0,0]
line = trajectory_data.values[:,0]
line =line-set_line
line = line+base_line
trajectory_data.values[:,0]=line
trajectory_data.to_csv('test.txt',sep=' ',index=0,header=0)
