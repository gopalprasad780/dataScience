import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
url = "http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2"

df = pd.read_html(url, header=1)[0]

print(df)

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..

header = df.columns.tolist()
header[-4:] = ['G','A']*2


df.columns = header
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df.dropna(axis=0, thresh=4)



# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=['RK'],axis=1)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reindex()


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
print(df.dtypes)


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..

