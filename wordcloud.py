import pickle
import json
import csv
from collections import OrderedDict
# importing package
import matplotlib.pyplot as plt
import numpy as np
"""
usa_adj_before_2000
usa_adj_after_2000
india_adj_after_2000
"""



def get_word_cloud_words(top_words, frequency_list, csv_file):
    final_frequncy_list_male = []
    # For male words
    list_str_male = ''
    for word in top_words['M'].keys():
        if frequency_list['M'][word] is not None:
            freq = frequency_list['M'][word]
            for _ in range(freq):
                list_str_male += word + ', '
                final_frequncy_list_male.append(word)

    # print(list_str_male)
    with open(csv_file + '_male.txt', 'w') as text_file:
        text_file.write(list_str_male)

    # ##################### Female

    final_frequncy_list_male = []
    # For female words
    list_str_male = ''
    for word in top_words['F'].keys():
        # print(f'Word : { word }')
        if frequency_list['F'][word] is not None:
            freq = frequency_list['F'][word]
            for _ in range(freq):
                list_str_male += word + ', '
                final_frequncy_list_male.append(word)

    # print(list_str_male)
    with open(csv_file + '_female.txt', 'w') as text_file:
        text_file.write(list_str_male)


def get_male_female_word_count(top_words, frequency_list, isGraph=True):
    word_counts = {'M': OrderedDict(), 'F': OrderedDict()}

    if not isGraph:
        for word in top_words['M'].keys():
            if frequency_list['F'][word] is not None and frequency_list['M'][word] is not None:
                word_dict = {}
                word_dict['m_num'] = frequency_list['M'][word]
                word_dict['f_num'] = frequency_list['F'][word]
                word_counts['M'][word] = word_dict

        for word in top_words['F'].keys():
            if frequency_list['F'][word] is not None and frequency_list['M'][word] is not None:
                word_dict = {}
                word_dict['m_num'] = frequency_list['M'][word]
                word_dict['f_num'] = frequency_list['F'][word]
                word_counts['F'][word] = word_dict
        return word_counts
    else:
        for word in top_words['M']:
            if frequency_list['F'][word] is not None and frequency_list['M'][word] is not None:
                word_dict = {}
                word_dict['m_num'] = frequency_list['M'][word]
                word_dict['f_num'] = frequency_list['F'][word]
                word_counts['M'][word] = word_dict

        for word in top_words['F']:
            if frequency_list['F'][word] is not None and frequency_list['M'][word] is not None:
                word_dict = {}
                word_dict['m_num'] = frequency_list['M'][word]
                word_dict['f_num'] = frequency_list['F'][word]
                word_counts['F'][word] = word_dict

        return word_counts
    # print(word_counts)


def plot_graphs(word_counts):

    # create data
    # print('\n\n', word_counts)

    male_y_axis = []
    female_y_axis = []
    x_axis = []
    width = 0.2

    # male dominating words
    for word in word_counts.keys():
        m_num = word_counts[word]['m_num']
        f_num = word_counts[word]['f_num']
        total = f_num + m_num
        m_num = int((m_num / total)*100)
        f_num = int((f_num / total)*100)
        male_y_axis.append(m_num)
        female_y_axis.append(f_num)
        x_axis.append(word)

    x = np.arange(len(x_axis))
    plt.bar(x-0.2, male_y_axis, width, color='#f1b814')
    plt.bar(x, female_y_axis, width, color='#bd1e51')
    plt.xticks(x, x_axis)

    plt.xlabel("Words")
    plt.ylabel("Percent")
    plt.legend(["Male", "Female"])
    plt.show()


if __name__ == '__main__':
    data_for = 'usa_adj_after_2000'
    pickle_file = f'pickle_files/{data_for}.pkl'
    odds_ratio_file = f'odd_ratio/{data_for}.json'
    csv_file = f'output/{data_for}'
    graph_words_file = 'odd_ratio/graph_words.json'

    pkl_file = open(pickle_file, 'rb')

    f = open(odds_ratio_file)
    top_words = json.load(f)
    f.close()

    frequency_list = pickle.load(pkl_file)
    get_word_cloud_words(top_words, frequency_list, csv_file)

    f = open(graph_words_file)
    graph_words = json.load(f)
    f.close()

    word_counts = get_male_female_word_count(graph_words[data_for],frequency_list)

    plot_graphs(word_counts['M'])
    plot_graphs(word_counts['F'])
