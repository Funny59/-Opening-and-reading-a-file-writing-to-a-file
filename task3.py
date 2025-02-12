from pprint import pprint

files = ['1.txt', '2.txt', '3.txt']

fileNamesAndCount = {}
for fileName in files:
    with open(fileName) as f:
        data = f.read()
        fileNamesAndCount.update({fileName : len(data.split('\n'))})

with open('output.txt', 'w') as f:
    for fileName in sorted(fileNamesAndCount.items(), key=lambda item: item[1]):
        f.write(fileName[0] + '\n')
        f.write(str(fileName[1]) + '\n')
        with open(fileName[0]) as ff:
            data = ff.read()
            f.write(data + '\n')