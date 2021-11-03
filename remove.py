filename = 'yelp_labelled.txt'

def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string

try:
    with open(filename,'r',encoding="utf-8") as f:
        data = f.read()
    with open(filename,"w+",encoding="utf-8") as f:
        f.write(remove_punc(data).lower())
    print("Removed punctuations from the file", filename)
except FileNotFoundError:
    print("File not found")