
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




def read_sound_data(data1):
    # Read numeric data, skipping the header row
    data = np.loadtxt(data1, delimiter=",", skiprows=1, dtype=float)

    # Separate length and trial columns
    lengths = data[:, 0]
    trials = data[:, 1:]

    # 1/L
    inv_length = 1.0 / lengths


    averages = np.mean(trials, axis=1)


    mean_dev = np.mean(np.abs(trials - averages[:, np.newaxis]), axis=1)


    st_dev = np.std(trials, axis=1)

    max_vals = np.max(trials, axis=1)
    min_vals = np.min(trials, axis=1)


    delta = max_vals - min_vals


    count = np.full_like(averages, trials.shape[1])


    stats = np.column_stack(
        (inv_length, averages, mean_dev, st_dev, max_vals, min_vals, delta, count)
    )


df = pd.read_csv('data1.csv')


trial_cols = df.columns[1:]
df['average'] = df[trial_cols].astype(float).mean(axis=1)

z_linear = np.polyfit(1/df[df.columns[0]], df['average'], 1)
p_linear = np.poly1d(z_linear)

plt.scatter(1/df[df.columns[0]], df['average'])
plt.xlabel('1/Length')
plt.ylabel('Average')
plt.title('1/Length vs Average')
plt.errorbar(1/df[df.columns[0]], df['average'], yerr=df[trial_cols].astype(float).std(axis=1), fmt='o', elinewidth=1, capsize=2)
plt.plot(1/df[df.columns[0]], p_linear(1/df[df.columns[0]]), "r--")
plt.grid(True)
plt.show()
