# import csv
### FILE READ
# with open('names.csv','r') as f:
    # print(f.readlines())
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    # content = f.readline()
    # next(f)
    # line=f.readline()
    # c=1
    # while line:
    #     print(f"{c}: {line}",end='')
    #     line = f.readline()
    #     c+=1

    # next(f)
    # for c,line in enumerate(f):
    #     print(c+1,line[:7],end="\n")


### CSV READ
import os
os.system('clear')

import csv

# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter=',')
#     for line in csv_reader:
#         print(line[1:3])



# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # next(csv_reader)
#     with open('new_new_names.csv','w') as new_file:
#         csv_writer=csv.writer(new_file,delimiter=':')
#         for line in csv_reader:
#             csv_writer.writerow(line)




with open('names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open('new_names_new.csv','w') as new_file:
        csv_writer = csv.DictWriter(new_file,fieldnames=['first_name','last_name'],delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)