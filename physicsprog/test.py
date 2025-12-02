import csv
import numpy as np
import matplotlib.pyplot as plt
def read_sound_data(data1):

    # Read numeric data, skipping the header row
    data = np.loadtxt(data1, delimiter=",", skiprows=1, dtype=float)

    # Separate length and trial columns
    lengths = data[:, 0]
    trials = data[:, 1:]

    # 1/L
    inv_length = 1.0 / lengths

    # Average of trials
    averages = np.mean(trials, axis=1)

    # Mean absolute deviation from the average
    mean_dev = np.mean(np.abs(trials - averages[:, np.newaxis]), axis=1)

    # Standard deviation of trials (population std)
    st_dev = np.std(trials, axis=1)

    # Max and Min across trials
    max_vals = np.max(trials, axis=1)
    min_vals = np.min(trials, axis=1)

    # Delta = Max - Min
    delta = max_vals - min_vals

    # Count of trials per row
    count = np.full_like(averages, trials.shape[1])

    # Stack into one (n, 8) array
    stats = np.column_stack(
        (inv_length, averages, mean_dev, st_dev, max_vals, min_vals, delta, count)
    )

    print(data, stats)

