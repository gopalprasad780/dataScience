import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
header_column = ['motor','screw','pgain','vgain','class']
df = pd.read_csv('Datasets/servo.data',names=header_column)

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
vgain_slice = df[df.vgain==5]
print('The length of Vgain slice is %s'%(len(vgain_slice)))


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
motor_screw_slice = df[(df.motor =='E') & (df.screw =='E')]
print('The lengh of motor & screw slice is %s'%(len(motor_screw_slice)))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
pgain_slice = df[df.pgain == 4]
mean_vgain = pgain_slice['vgain'].mean()

print('The mean of vgain value for sample slice is %s'%mean_vgain)

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print('This will happen when we add .dtypes in dataframe : %s'%(df.dtypes))


