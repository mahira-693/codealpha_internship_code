import random

words = ["python", "developer", "hangman", "programming", "internship"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("🎯 Welcome to Hangman!")
print("Word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n💀 Game over! The word was:", word)
