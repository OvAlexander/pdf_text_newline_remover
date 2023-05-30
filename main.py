#the purpose of this project is to change my copied pdf text to the proper format without random newlines
#The sample text is from the great gatsby by F. Scott Fitzgerald
import re
def replace_text(text):
    pattern = r'([a-z!@#$%^&*(),.?":{}|<>])\n'
    new_str = re.sub(pattern, r'\g<1> ', data)
    return new_str

if __name__ == '__main__':
    text_file = open("data.txt", "r", encoding="utf8")
    #read whole file to a string
    data = text_file.read()
    #close file
    text_file.close()
    print(replace_text(data))
