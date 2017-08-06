def extract_even(l):
    l = [lo for lo in l if not lo % 2]
    return l
even_list = extract_even([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
