# the purpose of this project is to change my copied pdf text to the proper format without random newlines
# The sample text is from the great gatsby by F. Scott Fitzgerald
import re


def replace_text(text):
    pattern = r'([a-z!@#$%^&*(),.?":{}|<>])\n'
    new_str = re.sub(pattern, r'\g<1> ', data)
    new_str = re.sub(r"\s\n", r' ', new_str)
    pattern = r'([a-z!@#$%^&*(),.?":{}|<>])\n\n'
    new_str = re.sub(pattern, r'\g<1> ', new_str)
    pattern = r'([a-z!@#$%^&*(),.?":{}|<>])\n'
    new_str = re.sub(pattern, r'\g<1> ', new_str)
    new_str = re.sub(r"\s\n", r' ', new_str)
    return new_str


if __name__ == '__main__':
    text_file = open("data.txt", "r", encoding="utf8")
    new_text_file = open("new_data.txt", "w", encoding="utf8")
    # read whole file to a string
    data = text_file.read()
    # close file
    text_file.close()
    new_text_file.write(replace_text(data))
    print(replace_text(data))
    new_text_file.close()
