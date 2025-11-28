import os
import sys

import numpy as np


def load_data(name):
    return np.load(name)
def save_data(name, data):
    np.save(name, data)

def process_data(data):

    mean = np.mean(data[:, 2:], axis=0)

    summ = np.sum(data[:, 2:], axis=0)

    special_students = data[data[:, 2] > 80]

    sorted_ids = np.argsort(data[:, 2][::-1])
    data_sorted = data[sorted_ids]

    avg_per_student = np.mean(data[:, 2:], axis=1)
    top_students = data[avg_per_student > 80]

    reshaped = data.reshape(5, -1, data.shape[1])
    group_means = np.mean(reshaped, axis=1)

    transposed = data.T
    lessons_means = np.mean(transposed, axis=1)

    res = {
        "mean": mean,
        "summ": summ,
        "data_sorted": data_sorted,
        "top_students": top_students,
        "special_students": special_students,
        "group_means": group_means,
        "lessons_means": lessons_means,
    }

    return res

def clear_terminal():
    os.system("cls||clear")


def show_data(data):
    for i in data:
        print(f"\033[91m{i}\033[0m" + ":")
        print(data[i])
        print("\033[92m=======================\033[0m")

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "-clear":
        clear_terminal()

    loaded_data = load_data("students_data.npy")
    processed_data = process_data(loaded_data)
    show_data(processed_data)

    # 🔹 تمرین 1: keepdims=True
    mean_normal = np.mean(loaded_data[:, 2:], axis=0)
    mean_keep = np.mean(loaded_data[:, 2:], axis=0, keepdims=True)

    print("mean_normal.shape:", mean_normal.shape)
    print("mean_normal:", mean_normal)
    print("-------------------------")
    print("mean_keep.shape:", mean_keep.shape)
    print("mean_keep:", mean_keep)
    print("=========================")


main()