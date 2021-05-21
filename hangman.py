import random

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def read_file():
    WORDS = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            WORDS.append(line.replace("\n", ""))
    return WORDS


def random_word(words):
    idx = random.randint(0, len(words) - 1)
    return words[idx]


def main():

    print("* - * - * - * - * - * - * - * - *- *- *")
    print("B I E N V E N I D O  A  H A N G M A N")
    print("* - * - * - * - * - * - * - * - *- *- *")
    print("\n")
    print("¡Adivina la palabra oculta!")

    tries = 0
    words = read_file()
    current_word = random_word(words)
    hidden_word = ['-' for i in current_word]
    print(hidden_word)

    try:
        while True:
            current_letter = input("Ingresa una letra: ")
            for i in range(len(NUMBERS)):
                if current_letter == NUMBERS[i]:
                    raise ValueError("No ingreses números, solamente letras, por favor") 
            
            letter_indexes = []
            for idx in range(len(current_word)):
                if current_letter == current_word[idx]:
                    letter_indexes.append(idx)

            if len(letter_indexes) == 0:
                tries += 1

                if tries == 7:
                    print(hidden_word)
                    print("")
                    print("¡Perdiste! La palabra correta era {}".format(current_word))
                    break

            else:
                for idx in letter_indexes:
                    hidden_word[idx] = current_letter
                print(hidden_word)
                letter_indexes = []

            try:
                hidden_word.index("-")
            except ValueError:
                print("¡Ganaste! La palabra era {}".format(current_word))
                break

    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
