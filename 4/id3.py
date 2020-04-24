from math import log2
import random
import csv


def parse_csv(filename, offset=0):
    with open(filename) as f:
        reader = csv.reader(f, skipinitialspace=True)
        rows = list(reader)
    return rows[offset], rows[offset + 1:]


def rewrite_table(rows):
    return [list(enumerate(row)) for row in rows]


def split_table(rows, idx):
    vals_set = set([r[idx] for r in rows])
    branches = []
    for val in vals_set:
        subrows = [r[:idx] + r[idx + 1:] for r in rows if r[idx] == val]
        branches.append((val, subrows))
    return branches


def most_frequent(lst):
    return max(set(lst), key=lst.count)


def gen_tree(rows, select_attr):
    target_vals = [r[-1] for r in rows]
    if len(rows[0]) == 1 or len(set(target_vals)) == 1:
        return most_frequent(target_vals)
    tree = []
    branches = split_table(rows, select_attr(rows))
    for v, r in branches:
        tree.append((v, gen_tree(r, select_attr)))
    return tree


def gen_code(title, tree):
    def dfs(tree, depth):
        tab = " " * (depth * 4)
        code = []
        if isinstance(tree, list):
            for t in tree:
                val, idx = t[0]
                code.append(tab + 'if data["%s"] == "%s":' % (title[val], idx))
                block = dfs(t[1], depth + 1)
                code += block if isinstance(block, list) else [block]
        else:
            code.append(tab + 'return "%s"' % tree[1])
        return code
    return "\n".join(dfs(tree, 0))


def select_random_attr(rows):
    return random.choice(rows)


def entropy(rows):
    # TODO
    pass


def average_entropy(rows, attr):
    # TODO
    pass


def select_best_attr(rows):
    # TODO
    pass


title, rows = parse_csv("learn.csv", offset=1)
rows = rewrite_table(rows)
t = gen_tree(rows, select_random_attr)
print(gen_code(title, t))
