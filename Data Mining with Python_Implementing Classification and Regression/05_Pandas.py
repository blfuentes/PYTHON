import pandas as pd
print(pd.__version__)

names = ['student1', 'student2', 'student3', 'student4','student5']
marks_percentage = [80,70, 60, 90, 65]

studentsDataset = list(zip(names, marks_percentage))
print(studentsDataset)
df = pd.DataFrame(data = studentsDataset, columns = ['Names', 'marks_percentage'])
print(df)

#path = 'students.csv'
#df1 = pd.read_csv(path)

df.to_csv('students.csv')

df['marks_percentage'].max()
sorted = df.sort_values(['marks_percentage'], ascending = False)
print(sorted.head())

print(list(df.columns.values))

print(df.describe())
