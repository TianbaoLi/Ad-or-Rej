import re

in_file = open('go_america_to_study_data.csv', 'r')
out_file = open("Decommaed.csv", 'w')

comma = re.compile(r"\"(.+),(.+)\"")
# \"Over(.+?),(.+?)\"

for line in in_file:
    #print line

    regex_result = comma.search(line)
    if regex_result is None:
        continue
    commaed = ','.join(str(i) for i in regex_result.groups())
    decommaed = ' '.join(str(i) for i in regex_result.groups())
    line = line.replace(commaed, decommaed)

    out_file.write(line)

in_file.close()
out_file.close()