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


#Backwards (3 different ways below)
reverse_string = string[::-1] #[start:stop:step] Copy the list and start at the end
print reverse_string

char_in_string = []
for character in string:
	char_in_string.append(character)
char_in_string.reverse()
print("".join(char_in_string))

reverse_list = list(string) #WIll convert data type into list
reverse_list.reverse()
print("".join(reverse_list))


#Leetspeak 
leetspeak = {	#Made a dictionary
	"A": "4",
	"E": "3",
	"G": "6",
	"I": "1",
	"O": "0",
	"S": "5",
	"T": "7"
	}
paragraph = "THIS IS A STRING THAT WILL BE CONVERTED TO LEETSPEAK."
for old, new in leetspeak.items():	#naming the two elements in the dictionary old and new
	paragraph = paragraph.replace(old, new)
print paragraph


#Long Long Vowels
def call(my_pet):
	vowels = "aeiouAEIOU"
	for vowel in vowels:
		my_pet = my_pet.replace(vowel, vowel *4)
	print my_pet
call("dog")

string_to_test = "Spoon"
result = ""
current = ""
previous = ""
for i in range(0, len(string_to_test)):
	current = string_to_test[i]
	if (current == previous):
		result = result + 4 * current
	else:
		result = result + current
	previous = current
print result


#Caesar Cipher
message = "lbh zhfg hayrnea jung lbh unir yrnearq!"
decrypted = "abcdefghijklmnopqrstuvwxyz"
encrypted = "nopqrstuvwxyzabcdefghijklm"
message_list = list(message)
decrypted_list = list(decrypted)
encrypted_list = list(encrypted)
decrypted_message = []

def decrypt_function(encrypted_letter):
	try:
		number = encrypted_list.index(encrypted_letter)
	except ValueError: #This will take care of the spaces and exclamation point
		#Do this!
		decrypted_message.append(encrypted_letter)
	else:
		decrypted_message.append(decrypted_list[number])
#index = will go through a list and look for the index of the number

for i in range(0, len(message_list)):
	decrypt_function(message_list[i])

final_decrypted_message = "".join(decrypted_message)
print final_decrypted_message

