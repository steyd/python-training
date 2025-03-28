import re

# print(re.findall("ab*c", "ac"))
# print(re.findall("ab*c", "abcd"))
# print(re.findall("ab*c", "acc"))
# print(re.findall("ab*c", "abcac"))
# print(re.findall("ab*c", "abdc"))
# print(re.findall("ab*c", "ABC"))
# print(re.findall("ab*c", "ABC", re.IGNORECASE))
# print('---------')
# print(re.findall("a.c", "abc"))
# print(re.findall("a.c", "abbc"))
# print(re.findall("a.c", "ac"))
# print(re.findall("a.c", "acc"))
# print('---------')
# print(re.findall("a.*c", "abc"))
# print(re.findall("a.*c", "abbc"))
# print(re.findall("a.*c", "ac"))
# print(re.findall("a.*c", "acc"))

#---------------------------------------------------------

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

#---------------------------------------------------------
string = "Everything is <replaced> if it's in <tags>"
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)

#---------------------------------------------------------
string = "Everything is <replaced> if it's in <tags>"
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)