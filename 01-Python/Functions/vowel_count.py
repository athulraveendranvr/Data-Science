
# def a funtion to get vowel count in a string

def count_vowels(text):

    vowels = "AEIOUaeiou"

    count = 0

    for i in text:

        if i in vowels:

            count += 1

    return count
    
print(count_vowels("programming"))