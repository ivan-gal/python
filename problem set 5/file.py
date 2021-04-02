import string
shift = 1
magic = {}
lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)

for i in range(len(lower_list)):
    try:
        magic[lower_list[i]] = lower_list[i + shift]
    except IndexError:
        magic[lower_list[i]] = lower_list[i + shift - 26]
for i in range(len(upper_list)):
    try:
        magic[upper_list[i]] = upper_list[i + shift]
    except IndexError:
        magic[upper_list[i]] = upper_list[i + shift - 26]

print(magic)
