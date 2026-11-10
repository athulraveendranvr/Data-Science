# wap to rev a string until the first occurence of p if there is no p reverse the entire string

def rev(text):

    for i in text:

        if i == "p":

            text_before_p = text[0:text.index(i)]

            reversed_text = text_before_p[::-1]

            text_after_p = text[text.index(i)::]

            result = reversed_text + text_after_p

            return result

            break

    else:

        reversed_text = text[::-1]

        return reversed_text
    
print(rev("hellopython"))

# we can write this in single step

# text[0:text.index(i)][::-1] + text[text.index(i)::]

#write this inside the if
        
