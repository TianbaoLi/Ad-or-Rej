import re

in_file = open('Decommaed.csv', 'r')
out_file = open("CommaFixed.csv", 'w')

comma = re.compile(r"Overall:[0-9 ]+ ")
# \"Over(.+?),(.+?)\"

for line in in_file:
    #print line

    regex_result = comma.findall(line)
    if regex_result is None:
        continue
    for i in regex_result:
        line = line.replace(i, i.strip()+',   ')

    out_file.write(line)

in_file.close()
out_file.close()