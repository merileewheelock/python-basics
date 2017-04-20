string = "hello there!"

#Uppercase
print string.upper()

new_string = ""
for i in string:
	new_string += i.upper()
print new_string


#Capitalize
print string.capitalize()

new_string2 = string[0].capitalize() + string[1:]
print new_string2


#Backwards
reverse_string = string[::-1] #[start:stop:step]
print reverse_string

#Leetspeak REVISIT
replacements = (("A","4"), ("E","3"), ("G","6"), ("I","1"), ("O","0"), ("S","5"), ("T","7"))
paragraph = "THIS IS A STRING THAT WILL BE CONVERTED TO LEETSPEAK."
new_paragraph = paragraph
for old, new in replacements:
	new_paragraph = paragraph.replace(old, new)
print new_paragraph

#Long Long Vowels REVISIT
word = raw_input("Enter a word. ")
for vowel in word:
	if vowel == "aa":
		word = word.replace("aa", "aaaaa")
		print word
	if vowel == "ee":
		print word.replace("ee","eeeee")
	if vowel == "ii":
		print word.replace("ii","iiiii")

#Caesar Cipher REVISIT
text = "lbh zhfg hayrnea jung lbh unir yrnearq"
shift = 13
for i in text:
	if i.isalpha():
		stay_in_alphabet = ord(i) + shift
		if stayInAlphabet > ord('z'):
			stayInAlphabet -= 26
      	finalLetter = chr(stayInAlphabet)
      	text += finalLetter
print text
