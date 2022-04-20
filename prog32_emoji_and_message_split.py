# emoji insertion
# message split

message = input("> ")
words = message.split(" ")
# this makes a list of string of each word
# in bracket whatever is passed is used as seperator
# if nothing is passed then it uses space as seperator
print(words)

output = ""
emoji = {
    ":)": "smile emoji",
    ":(": "sad emoji"
}
for word in words:
    output += emoji.get(word, word) + " "
    # by default it gives the word ( if no emoji)
print(output)
