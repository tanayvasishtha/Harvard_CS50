import emoji

user_ans = input("Input: ")

output = emoji.emojize(user_ans)
emoji_alias = emoji.emojize(user_ans, language = "alias")

if output != user_ans:
    print(output)
else:
    print(emoji_alias)
