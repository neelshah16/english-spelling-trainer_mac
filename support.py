import numpy as np

def file_to_list(filename):
    try:
        with open(filename) as f:
            # with open('google-10000-english.txt') as f:
            # with open('words_alpha.txt') as f:
            itemlist = f.read().splitlines()
    except FileNotFoundError as e:
        with open(filename, 'w') as f:
            f.write("")
        itemlist = []
    return itemlist

def list_to_file(item_list, filename, mode='w'):
    with open(filename, mode) as f:
        for item in item_list:
            f.write("%s\n" % item)

def lev_distance(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

def words_diff(a, b):
    m, n = len(a), len(b)

    i_ = 0
    error_seq_main = []
    while m-i_ > 1:
        i = i_
        j = 0
        error_seq = []
        seq = ""
        first_break = False
        while n-j > 1 and m-i > 1:
            if a[i] == b[j]:
                i += 1
                j += 1

                if seq:
                    error_seq.append(seq)
                    seq = ""
            else:
                if not first_break:
                    first_break = j

                seq += b[j]
                j += 1

            if not n-j > 1 and m-i > 1:
                j -= first_break
                i += 1
                first_break = False

                # if seq:
                #     error_seq.append(seq)
                #     seq = ""

        i_ += 1
        if error_seq:
            error_seq_main.append(error_seq)

    print(error_seq_main)

if __name__ == "__main__":
    words_diff("abcdefg", "abedfgg")