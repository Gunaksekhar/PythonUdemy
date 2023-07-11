import re
text = "If I want to find multiple matches or all the matches"

word = re.search('matches', text)
print(word.span(), "\n")

word1 = re.findall('matches', text)
print("len of the word", len(word1),word1, "\n")

for word2 in re.finditer('matches', text):
    print(word2.span(), "\n")
    print(word2.group(), "\n")

sentence = 'Just text to my number, 993-08-51-472'
print(sentence)
number_pattern = re.compile(r'\d{3}\W\d{2}\W\d{2}\W\d{3}')
nums = re.search(number_pattern,sentence)
print("pattern", nums.group(), "\n")

area = "hello all welcome to VR_Mart1 PNR_Malls"
are = re.compile((r'\w{8}'))
ar = re.search(are,area)
print(ar.group())

re = re.findall(r'^\d', 'The number is 2')
print(re)