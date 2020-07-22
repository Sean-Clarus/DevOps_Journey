import os
#File Objects

##The Basics:
# f = open("test.txt")
# print(type(f))
# print(f.readlines())

# print(sea.read(25))
# print(sea.read(5))
# print(sea.read(7))
# print(sea.tell())
# print(sea.read(25))
# sea.seek(5)
# print(sea.read(5))
clear = lambda : os.system("clear")

clear()


# # f = open("fishes.txt","r")
# # for line in f:
# # 	print(line,end="")
# # f.close()

# # with open("fishes.txt","r") as f:
# # 	print(f.read(24))
# # 	print(f.read(5))
# # 	print(f.tell())
# # 	f.seek(5)
# # 	print(f.read(26))









# # f = open("test.txt", "w")
# # f = open("test.txt", "a")
# # f = open("test.txt", "r+")
# # print(f.name)
# # print(f.mode)
# # f.close()

# ##Reading Files:
# # with open("test.txt", "r") as f:
# # 	pass

# 	##Small Files:
# 	# f_contents = f.read()
# 	# print(f_contents)

# 	##Big Files:
# 	# f_contents = f.readlines()
# 	# print(f_contents)

#     ###With the extra lines:
# 	# f_contents = f.readline()
# 	# print(f_contents)
# 	# f_contents = f.readline()
# 	# print(f_contents)

# 	###Without the extra lines:
# 	# f_contents = f.readline()
# 	# print(f_contents, end = '')
# 	# f_contents = f.readline()
# 	# print(f_contents, end = '')

# 	###Iterating through the file:
# 	# for line in f:
# 	# 	print(line, end = '')

# 	###Going Back....:
# 	# f_contents = f.read()
# 	# print(f_contents, end = '')

# 	###Printing by characters:
# 	#f_contents = f.read(100)
# 	#print(f_contents, end = '')
# 	#f_contents = f.read(100)
# 	#print(f_contents, end = '')
# 	#f_contents = f.read(100)
# 	#print(f_contents, end = '')

# 	###Iterating through small chunks:
# 	#size_to_read = 100
# 	#f_contents = f.read(size_to_read)
# 	#while len(f_contents) > 0:
# 		#print(f_contents)
# 		#f_contents = f.read(size_to_read)

# 	###Iterating through small chunks, with 10 characters:
# 	#size_to_read = 10
# 	#f_contents = f.read(size_to_read)
# 	#print(f_contents, end = '')
# 	#f.seek(0)
# 	#f_contents = f.read(size_to_read)
# 	#print(f_contents, end = '')
# 	#print(f.tell())
# 	#while len(f_contents) > 0:
# 		#print(f_contents, end = '*')
# 		#f_contents = f.read(size_to_read)
# #print(f.mode)
# #print(f.closed)
# #print(f.read())


# # RUMI Task
# ####1####
# # with open('rumi.txt','r') as f:
# # 	# print(f.read())
# # 	print(f.read(35))
# # 	print(f.read(13))
# # 	print(f.tell())
# # 	f.seek(15)
# # 	print(f.read(20))

# ####2####
# # with open('rumi.txt','r') as f:
# # 	print(f.readline(),end="")
# # 	print(f.readline(),end="")
# # 	print(f.readline(3))

# ####3#####
# # f = open('rumi.txt','r')
# # for line in f:
# # 	print(line,end="")

# # f.close()

# flowers = ['Jasmine\n','Rose\n','Lily\n','Daisy\n','Tulip']
# # print(flowers)
# # print(len(flowers))
# # with open('flowers.txt','w') as wf:
# # 	wf.writelines(flowers)
# # with open('flowers.txt','a') as af:
# # 	af.write('\nOrchid')

# # with open('flowers.txt','r') as rf:
# # 	print(rf.read())
# # 	print(rf.tell())
# # 	rf.seek(0)
# # 	print(rf.readlines())
# counter= 0
# with open('names.txt','r') as rf:
# 	counter= 0
# 	while counter < 10:
# 		print(rf.readline(),end="")
# 		counter+=1







# with open('dummy.txt','w') as wf:
# 	for fruit in fruits:
# 		wf.write(f"{b} {fruit} is a {a}\n")

# with open ('dummy.txt','r') as rf:
# 	print(rf.read())








##Writing Files:
###The Error:
#with open("test.txt", "r") as f:
	#f.write("Test")

###Writing Starts:
# with open("test2.txt", "w") as f:
# 	# pass
# 	f.write("Test")
# 	f.seek(0)
# 	f.write("Test")
# 	f.write("XX")

##Copying Files:
# with open("test.txt", "r") as rf:
# 	with open("test_copy.txt", "w") as wf:
# 		for line in rf:
# 			wf.write(line)

#Copying the/your image:

###Copying the image with chunks:
# with open("dog.jpg", "rb") as rf:
# 	with open("dog_new.jpg","wb") as wf:
# 		rf_chunk = rf.read(4096)
# 		while len(rf_chunk)>0:
# 			wf.write(rf_chunk)
# 			# print(rf_chunk)
# 			rf_chunk=rf.read(4096)

import pandas as pd
df = pd.read_csv('names.xlsx')
df['new_column'] = 'Andy'
print(df.head())
