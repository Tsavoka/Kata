# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the
# input string.

def duplicate_count(text):
    text = text.lower()
    print(text)
    counted = []
    for i in text:
        if text.count(i) > 1:
            if i not in counted:
                counted.append(i)
    return len(counted)



print(duplicate_count("aA11"))  # 'a' '1'
