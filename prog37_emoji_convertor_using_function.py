# make emoji insertion function

def emoji_function(message):
    words = message.split(" ")
    output = ""
    emoji = {
        ":)": "smile emoji",
        ":(": "sad emoji"
    }
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("> ")
print(emoji_function(message))
