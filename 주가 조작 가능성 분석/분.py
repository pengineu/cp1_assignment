import matplotlib.pyplot as plt
import numpy as np
import collections

data = np.load("./Intel_Stock_History_from_1980_03_17.npy")
log_data = np.log10(data)
digits = log_data.astype(np.int32)
normalize = data / 10**digits
first_num = normalize.astype(np.int32)
print(len(data))
unique ,count_data = np.unique(first_num, return_counts=True)
percentage_data = count_data / len(data)
# plt.bar(unique, percentage_data)
# plt.show()

time = 1

# def difference(data, time):
#     compare_data = data.copy()
#     data = list(data)
#     compare_data = collections.deque(compare_data)
#     for i in range(time):
#         compare_data.popleft()
#         data.pop()
#     data = np.array(data)
#     compare_data = np.array(compare_data)
#     data = data - compare_data
#     return data
#
# first_data = difference(data, time)
# second_data = difference(first_data, time)
# third_data = difference(second_data, time)
# fourth_data = difference(third_data, time)
#
#
# plt.plot(first_data)
# plt.show()
#
#
# from statsmodels.tsa.stattools import adfuller
# print(adfuller(data))
# print(adfuller(first_data))




# plt.plot(second_data)
# plt.show()
#
# plt.plot(third_data)
# plt.show()
#
# plt.plot(fourth_data)
# plt.show()

# mu = np.mean(data)
# std = np.std(data)
# z_score = (data - mu) / std
# plt.plot(np.abs(z_score))
# plt.show()
#
benford = []
for i in range(1, 10):
    benford.append(np.log10(1 + 1/i))
benford = np.array(benford)
#
# print(percentage_data - benford)

# dev = np.abs(percentage_data - benford)
#
# plt.errorbar(benford, benford, yerr=dev)
# plt.show()

from scipy.stats import chisquare

print(chisquare(percentage_data, f_exp=benford))