# number bracelet
# generate sequence of number bracelet, entries 0 to 9
# the next number is the sum of previous two then take mod 10

# all possible starting two numbers (0,0) to (9,9), total 100 such tuples
N = []
for i in range(10):
    for j in range(10):
        N.append((i, j))


def make_bracelet(starting_nums):
    a, b = starting_nums
    array = [a, b]
    for i in range(0, 200):
        # 200 is chosen as upperbound, as note any pair of numbers directly affects the next pair, and as there are at most 100 numbers 00-99 then the maximum period of the braclet is 2*100
        x = (array[i] + array[i + 1]) % 10
        array.append(x)
    return array


def group_bracelets(your_bracelet):
    # sets of starting tuples that gives the "same" bracelet
    tuple_all = set([tuple(your_bracelet[i:i + 2]) for i in range(0, len(your_bracelet) - 3, 1)])
    # print(tuple_all)
    return tuple_all


def generate_bracelets():
    all_bracelets = []
    for num in N:
        new_bracelet = make_bracelet(num)
        equi_classes = group_bracelets(new_bracelet)

        # check if this whole equi_class has already been contained in any current bracelets stored in the list
        if all(equi_classes != group_bracelets(each) for each in all_bracelets):
            all_bracelets.append(new_bracelet)
            yield new_bracelet, equi_classes


generate_bracelets()

for i, (new_bracelet, equi_classes) in enumerate(generate_bracelets()):
    print(f"Unique bracelet {i + 1}: Equivalence Class: {equi_classes}")
