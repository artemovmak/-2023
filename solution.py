import numpy as np
from sys import argv
import os

dir_1 = argv[1]
dir_2 = argv[2]
parameter = int(argv[3])

if dir_1[-1] != '/':
    dir_1 = dir_1 + '/'
    
if dir_2[-1] != '/':
    dir_2 = dir_2 + '/'


def open_files(first_f, second_f):
    with open(dir_1 + first_f, 'r') as file_in:
        data = file_in.read().replace('\n', '')
        data_1 = data.replace(' ', '')
    with open(dir_2 + second_f, 'r') as file_n:
        data = file_n.read().replace('\n', '')
        data_2 = data.replace(' ', '')
    return data_1, data_2


def get_dist(data_1, data_2):
    length = max(len(data_1), len(data_2))
    return 100 - round((levenshtein(data_1, data_2) / length) * 100, 2)


def levenshtein(seq_1, seq_2):
    size_x = len(seq_1) + 1
    size_y = len(seq_2) + 1
    leven_arr = np.zeros((size_x, size_y))
    for x in range(size_x):
        leven_arr[x, 0] = x
    for y in range(size_y):
        leven_arr[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq_1[x - 1] == seq_2[y - 1]:
                leven_arr[x, y] = min(leven_arr[x - 1, y] + 1, leven_arr[x - 1, y - 1], leven_arr[x, y - 1] + 1)
            else:
                leven_arr[x, y] = min(leven_arr[x - 1, y] + 1, leven_arr[x - 1, y - 1] + 1, leven_arr[x, y - 1] + 1)

    return leven_arr[size_x - 1, size_y - 1]


def find_unique_files(dir_name, arr1, arr2, idx):
    output = []

    for filename in os.listdir(dir_name):
        flag = False
        for item in arr1:
            if filename == item[idx]:
                flag = True
                break
        for item in arr2:
            if filename == item[idx]:
                flag = True
                break
        if not flag:
            output.append(filename)
    return output


def find_similarity():
    sim = []
    eq = []
    d = []
    for first_filename in os.listdir(dir_1):
        for second_filename in os.listdir(dir_2):
            data_1, data_2 = open_files(first_filename, second_filename)
            r = get_dist(data_1, data_2)
            if r == 100:
                eq.append([first_filename, second_filename])
            elif r > parameter:
                sim.append([first_filename, second_filename])
                d.append(r)
    return eq, sim, d


def show_eq(eq_arr):
    for item in eq_arr:
        print(dir_1 + str(item[0]) + ' - ' + dir_2 + str(item[1]))
        

def show_sim(sim_arr, destination):
    for i, item in enumerate(sim_arr):
        print(dir_1 + str(item[0]) + ' - ' + dir_2 + str(item[1]) + ' - ' + str(destination[i]))
 
       
def show_only_one(one_arr, direc):
    for item in one_arr:
        print(direc + item)


equal, similar, dists = find_similarity()

first = find_unique_files(dir_1, equal, similar, 0)
second = find_unique_files(dir_2, equal, similar, 1)

print("This files are equal:")
show_eq(equal)

print("This files are similar:")
show_sim(similar, dists)

print("This files are only in first directory:")
show_only_one(first, dir_1)

print("This files are only in second directory:")
show_only_one(second, dir_2)
