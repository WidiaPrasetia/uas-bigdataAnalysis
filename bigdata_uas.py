import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_excel('Covid-19-di-Indonesia.xlsx', sheet_name='Sheet1')
# group =data.groupby(data.iloc[:, 0])[['Kasus']]
# print(group.mean())


data_sorted = data.sort_values(by = ['Kematian'])
test = data_sorted.head(10)
case = ['Kasus', 'Sembuh', 'Kematian']
prov = (test.iloc[:, 0])
df2 = test.groupby(test.iloc[:, 0]).agg('mean')
df2.plot(kind='bar')
plt.title('Data Nasional COVID-19 di Indonesia dengan Kasus Kematian terendah per tanggal 1 Juni 2020', fontsize=10)
plt.xticks(rotation='horizontal')
plt.xlabel('Provinsi(10 paling rendah)', labelpad=20, fontsize=15)
# plt.legend(bbox_to_anchor=(1,1))
plt.show()

# data_sorted = data.sort_values(by = ['Kasus'], ascending=False)
# test = data_sorted.head(10)
# case = ['Kasus', 'Sembuh', 'Kematian']
# prov = (test.iloc[:, 0])
# df2 = test.groupby(test.iloc[:, 0]).agg('mean')
# df2.plot(kind='bar')
# plt.title('Data Nasional COVID-19 di Indonesia dengan Kasus Kematian terendah per tanggal 1 Juni 2020', fontsize=10)
# plt.xticks(rotation='horizontal')
# plt.xlabel('Provinsi(10 paling rendah)', labelpad=20, fontsize=15)
# # plt.legend(bbox_to_anchor=(1,1))
# plt.show()

# data_sorted = data.sort_values(by = ['Sembuh'], ascending=False)
# test = data_sorted.head(10)
# case = ['Kasus', 'Sembuh', 'Kematian']
# prov = (test.iloc[:, 0])
# df2 = test.groupby(test.iloc[:, 0]).agg('mean')
# df2.plot(kind='bar')
# plt.title('Data Nasional COVID-19 di Indonesia dengan Kasus Kematian terendah per tanggal 1 Juni 2020', fontsize=10)
# plt.xticks(rotation='horizontal')
# plt.xlabel('Provinsi(10 paling rendah)', labelpad=20, fontsize=15)
# # plt.legend(bbox_to_anchor=(1,1))
# plt.show()


# x = test.iloc[:, 0]
# y = test['Kematian']
# plt.bar(x, y)
# plt.show()

