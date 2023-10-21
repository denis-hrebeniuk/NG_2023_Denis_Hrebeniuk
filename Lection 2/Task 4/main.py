text = input("Enter any text in English: ")
vowels = ["a", "e", "i", "o", "u", "y"]

vowels_in_text = ""
for letter in text:
    if letter.lower() in vowels:
        vowels_in_text += letter

print(f"All the vowel letters in your sentence: {vowels_in_text}")