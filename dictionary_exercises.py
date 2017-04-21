#Exercise 1

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
#1
print phonebook_dict['Elizabeth']

#2
phonebook_dict['Kareem'] = '938-489-1234'
print phonebook_dict

#3
del phonebook_dict['Alice']
print phonebook_dict

#4
phonebook_dict['Bob'] = '968-345-2345'

#5
print phonebook_dict

#Using fixed keys


#Exercise 2

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#1
print ramit['email']

#2
print ramit['interests'][0]

#3
print ramit['friends'][0]['email']

#4
print ramit['friends'][1]['interests'][1]

#Using fixed keys


#Letter Summary
def letter_histogram(word):
	alpha = {} #dict() will also create an empty dictionary
	count_num = 1
	for letter in word:
		if letter in alpha.keys():
			alpha[letter] += 1
		else:
			alpha[letter] = count_num

	print alpha
letter_histogram("Hello")


#Word Summary
def word_histogram(paragraph):
	word_list = {}
	count_num_word = 1
	paragraph_split = paragraph.split()
	for word in paragraph_split:
		if word in word_list.keys():
			word_list[word] += 1
		else:
			word_list[word] = count_num_word
	print word_list
word_histogram("This is a paragraph that I am writing to test this thing.")


#Bonus: Max 3 Letters
def letter_histogram(word):	
	alpha = {} 
	count_num = 1
	for letter in word:
		if letter in alpha.keys():
			alpha[letter] += 1
		else:
			alpha[letter] = count_num

	return alpha

# #CHAD'S WAY:
# user_word = raw_input("Please enter a paragraph. ")
# alpha = letter_histogram(user_word)
# this_list = []
# for key, key[histo] in alpha:
# 	this_list.append([key, key[histo]])
# this_list.sort(key = lambda x: x[1]) #sort based on the 1th element (the value)
# print this_list[-1]
# print this_list[-2]
# print this_list[-3]

#YINGRONG'S WAY
a_list = []
max_key = ""
new_dict = {}
while len(new_dict.keys() <=2):
	max_number = 0
	for i in alpha:
		if alpha[i] > max_number:
			max_number = alpha[i]
			max_key = i
	del alpha[max_key]	#find the 1st, 2nd, and 3rd biggest
	new_dict[max_key] = max_number
print new_dict


# alpha_out = letter_histogram("Hello")
# print alpha_out
# sorted_alpha = [(let,num) for num,let in sorted(
# 	[(num,let) for let,num in alpha_out.items()], reverse=True
# 	)
# ]
# print sorted_alpha[0:3]

#Dictionary with letter as the key and letter_count as the object
#Find the three highest letter counts
#Find the letters corresponding to the letter_counts
#Print the top 3 letters


#Super Bonus

#Create an empty dictionary
#Scan list for number of times each object appears
#Input frequency as dictionary key
#Input object as value for corresponding frequency
#Correct spelling of "Beatles"

list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
def super_bonus(input_list):
	dictionary = {}
	item_count = 1
	for item in input_list:
		if item in dictionary.keys():
			dictionary[item] += 1
		else:
			dictionary[item] = item_count
	print dictionary
super_bonus(list1)

#Output: {
# 1: 6,
# 'The Beetles': 1,
# 3: 2,
# 4: 3,
# 65: 1,
# 9: 1,
# 'Jim': 2,
# 45: 3}

#Take value of frequency and convert to string
#Make value of frequency as string the key in new dictionary
#List keys from current dictionary and turn into object of the new dictionary

