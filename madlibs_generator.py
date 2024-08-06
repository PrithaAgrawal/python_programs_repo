with open("story.txt","r") as f:
    story = f.read()

words = set()
starting_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        starting_word = i 

    if char == target_end and starting_word != -1:
        word = story[starting_word: i + 1]
        words.add(word)
        starting_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for" + word + ":")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)



