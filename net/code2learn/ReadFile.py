import csv

file=open('D:\\DEVELOPMENT\\python-examples\\net\\code2learn\\resources\\sample.csv', 'r')
csvFile=csv.reader(file)
for row in csvFile:
    print(row)
file.close()

with open('D:\\DEVELOPMENT\\python-examples\\net\\code2learn\\resources\\sample.csv', 'r') as file:
    for line in file:
        print(line.strip())

with open('D:\\DEVELOPMENT\\python-examples\\net\\code2learn\\resources\\sample.csv', 'w') as file:
    file.write("New line added\n")


