

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)

    print(line)


def split_and_join2(line):
    # write your code here
    return "-".join(line.split())


print(split_and_join('this is a string'))

print(split_and_join2('this is a yezzy firm'))
