file_read = open('codingal.txt', 'r')
print("file in read mode-")
print(file_read.read())
file_read.close()

file_write= open('codingal.txt', 'w')

file_write.write("file in write mode...")
file_write.write("hi!! I am a chicken. I am 2 years old")
file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write("\n file in read mode ....")
file_append.write("anshul seeappend mode")
file_append.close()