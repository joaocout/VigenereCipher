import os


def read_file(file_path: str) -> list[str]:
    f = open(file_path, "r", encoding='utf-8')
    lines = f.read().splitlines()
    f.close()
    return lines


def is_a_valid_letter(letter: str) -> bool:
    lowercase_letter = letter.lower()

    # check if letter is between a and z
    if ord(lowercase_letter) >= ord("a") and ord(lowercase_letter) <= ord("z"):
        return True

    return False


def vigenere(text: list[str], key: str, mode: str):
    result_lines: list[str] = []
    key_index = 0

    for line in text:
        result_line: str = ""

        for letter in line:
            if is_a_valid_letter(letter):

                # letter values should go from 0 to 25, so we pass it to ascii, and subtract 'a'
                letter_value = ord(letter.lower()) - ord("a")

                # shift key is always lowercase, and each letter should also go from 0 to 25
                # so we only need to subtract 'a' (97)
                shift_value = ord(key.lower()[key_index]) - ord("a")
                key_index = (key_index + 1) % len(key)

                new_value = 0
                if mode == "enc":
                    # adding the shift value if it's encryption
                    new_value = (letter_value + shift_value) % 26
                else:
                    # subtracting the shift value if it's decryption
                    new_value = (letter_value - shift_value) % 26

                # adding 'a' back to value, so we go from 0-25 back to a-z ascii
                result_letter = chr(new_value + ord('a'))

                # if the original was uppercased, we pass the result to upppercase
                result_letter = result_letter.upper() if letter.isupper() else result_letter

                result_line += result_letter

            else:
                result_line += letter

        result_lines.append(result_line)

    return result_lines


def main():
    file_name = os.path.join(os.path.dirname(
        __file__), os.pardir, 'resources/desafio2.txt')

    key = "TEMPORAL"

    text = read_file(file_name)

    # text = vigenere(text, key, "enc")
    # print(text)

    text = vigenere(text, key, "dec")
    print(text)


if __name__ == "__main__":
    main()
