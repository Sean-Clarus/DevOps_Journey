# with open('dummy.txt', 'w') as wf:
#     wf.write('This is my first line')

# with open('dummy.txt', 'r') as rf:
#     print(rf.read())

# flowers = ['Jasmine', 'Rose', 'Lily', 'Daisy', 'Tulip']

# with open('flowers.txt', 'w') as list:
#     for flower in flowers:
#         list.write(flower + '\n' + '\n')

flowers = ['Jasmine', 'Rose', 'Lily', 'Daisy', 'Tulip']
with open('flowers.txt', 'w', encoding='utf-8') as f:
    for flower in flowers:
        f.write(flower+'\n'+'\n')

with open('flowers.txt', 'r') as f:
    print(f.read())



# flowers=['jasmine','rose','lily','tulip']
# with open('flowers.txt','w') as wf:
#     for flower in flowers:
#          wf.write(flower+ '\n')
# with open ('flowers.txt','r') as rf:
#    print(rf.read())