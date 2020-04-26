#im port pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#create 2D array of table given above
data = [['E001','M',34,123, 'Normal',350],
        ['E002','F',40,114,'Overweight,450'],
        ['E003','F',37,135,'Obesity',169],
        ['E004','M',30,139,'Underweight',189],
        ['E005','F',44,177,'Underwight',183],
        ['E006','M',36,121,'Normal',80],
        ['E007','M',32,133,'Obesity',166],
        ['E008','F',26,140,'Normal',120],
        ['E009','M',32,133,'Normal',75],
        ['E010','M',36,133,'Underwight',40]]
#dataframe created with
#the above data array
df = pd.DataFrame(data, columns = ['EMPID','Gender',
                                   'Age','Sales',
                                   'BMI','Income'])
#create histogram for numeric data
df.hist()

#show plot
plt.show()