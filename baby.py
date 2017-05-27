from random import choice

questions = ["Why the sky is blue ?", "Why is there a face on the moon?", "where are the dinosaurs ?"]

question = choice(questions)
answer = input(question).strip().lower()

while answer!= 'just because':
    answer = input("why ?:").strip()

print("Oh ok...")
