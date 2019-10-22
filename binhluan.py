
# Xử lí 1 bình luận mới 
import re 
from pyvi import ViTokenizer

# load các từ dừng của tiếng việt 

stopwords = []
f = open('vietnamese-stopwords.txt', 'r')
for line in f:
    line = line.rstrip()
    #print(line)
    line = line.replace(' ', '_')
    
    stopwords.append(line)
f.close()


content = "yếu xìu hôm nay hihihi học sinh Tôi yêu đất nước Việt Nam 1234 hihi số  đi học  @#$%^&*("

# bỏ các liên kết 
content = re.sub("(http|https|ftp)[\n\S]+","",content)
# loại bỏ kí tự đặc biệt và số
content = re.sub("\W|\d" ," ", content) 


                
content = content.split()

text = []

for word in content: 
    # viết thường 
    word = word.lower()
                        
content = ' '.join(text)

print(content)

# tách từ
content  = ViTokenizer.tokenize(content)

# bỏ stopword

content = content.split()

text = []

for word in content: 
    if word not in stopwords:
        text.append(word)
                        
content = ' '.join(text)








# file = open("new_comment.txt", "w+")
# file.write(content)
# file.close()