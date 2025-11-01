import numpy as np

temps = np.array([
    [14, 16, 15, 18, 20, 21, 19],  # Tehran
    [20, 22, 23, 25, 27, 28, 26],  # Shiraz
    [10, 12, 13, 14, 15, 16, 15]   # Mashhad
])

def show_data(data):
    for i in data:
        print(f"\033[92m{i}\033[0m")
        print(data[i])


def process_data(data):
    mean = np.mean(temps, axis=1)

    mean_per_day = np.mean(temps, axis=0)

    most_hot_city = np.argmax(mean)
    most_cold_city = np.argmin(mean)

    res = {
        "mean": mean,
        "mean_per_day": mean_per_day,
        "most_hot_city": most_hot_city,
        "most_cold_city": most_cold_city,
    }

    return res
def main():
    data = process_data(temps)
    show_data(data)


main()
