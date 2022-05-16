import itertools
from tqdm import tqdm

def senbetsu(inp_line, line_of_all):
    tmp = []
    for loa in line_of_all:
        for num, (i, l) in enumerate(zip(inp_line, loa)):
            if i != l and i != 0:
                break
            if num == 8:
                tmp.append(loa)
    return tmp

def has_duplicates(seq):
    return len(seq) != len(set(seq))

def compare_inp(input_m, matrix):
    for inp, mat in zip(input_m, matrix):
        for i, m in zip(inp, mat):
            if i == 0:
                return True
            elif i == m:
                return True
            else:
                return False

def check_by_verticle(input_m, matrix):
    v_size = len(matrix)
    for i in range(0, 9):
        v_line = [matrix[v][i] for v in range(v_size)]

        if has_duplicates(v_line):
            return False

    return True


def solv_main(inp):
    all_list = [list(i) for i in itertools.permutations(range(1, 10))]
    predict_list = [
        senbetsu(inp[i], all_list) for i in range(0, 9)
    ]
    candidate = [len(n) for n in predict_list]
    bar = tqdm(total=candidate[0])
    print(f"各行の候補数: {candidate}")
    for l0 in predict_list[0]:
        bar.update(1)
        for l1 in predict_list[1]:
            if not check_by_verticle(inp, [l1]):
                continue
            for l2 in predict_list[2]:
                if not check_by_verticle(inp, [l1, l2]):
                    continue
                for l3 in predict_list[3]:
                    if not check_by_verticle(inp, [l1, l2, l3]):
                        continue
                    for l4 in predict_list[4]:
                        if not check_by_verticle(inp, [l1, l2, l3, l4]):
                            continue
                        for l5 in predict_list[5]:
                            if not check_by_verticle(inp, [l1, l2, l3, l4, l5]):
                                continue
                            for l6 in predict_list[6]:
                                if not check_by_verticle(inp, [l1, l2, l3, l4, l5, l6]):
                                    continue
                                for l7 in predict_list[7]:
                                    if not check_by_verticle(inp, [l1, l2, l3, l4, l5, l6, l7]):
                                        continue
                                    for l8 in predict_list[8]:
                                        if not check_by_verticle(inp, [l1, l2, l3, l4, l5, l6, l7, l8]):
                                            continue
                                        matrix = [
                                            l0,l1,l2,l3,l4,l5,l6,l7,l8
                                        ]
                                        if check_by_verticle(inp, matrix):
                                            print("Done\n")
                                            for m in matrix:
                                                print(m)


if __name__ == "__main__":
    inp = [
        [1, 8, 0, 0, 4, 0, 2, 0, 7],
        [0, 2, 0, 0, 7, 0, 1, 9, 0],
        [0, 0, 3, 0, 2, 0, 0, 0, 4],
        [2, 1, 0, 4, 0, 3, 0, 0, 0],
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 5, 1, 0, 6, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    solv_main(inp)
