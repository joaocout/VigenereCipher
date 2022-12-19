# Joao Pedro Assuncao Coutinho - 180019813

letter_frequency = {
    "a": 14.63,
    "b": 1.04,
    "c": 3.88,
    "d": 4.99,
    "e": 12.57,
    "f": 1.02,
    "g": 1.30,
    "h": 1.28,
    "i": 6.18,
    "j": 0.40,
    "k": 0.02,
    "l": 2.78,
    "m": 4.74,
    "n": 5.05,
    "o": 10.73,
    "p": 2.52,
    "q": 1.20,
    "r": 6.53,
    "s": 7.81,
    "t": 4.34,
    "u": 4.63,
    "v": 1.67,
    "w": 0.01,
    "x": 0.21,
    "y": 0.01,
    "z": 0.47
}

pt_letter_prob = [val for val in letter_frequency.values()]


def get_factors(n: int) -> list[int]:
    factors: list[int] = []

    for i in range(3, n - 1):
        if n % i == 0:
            factors.append(i)

    return factors


def read_file(file_path: str) -> list[str]:
    f = open(file_path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines


def index_of_coincidence(text: str) -> float:
    frequencies = []

    # for letter between a and z
    for i in range(ord("A"), ord("Z")):
        frequencies.append(text.count(chr(i))/len(text))

    result: float = 0
    for f in frequencies:
        result += f*f

    return result


def vigenere_discover_key(text: list[str]) -> str:
    # processing text, so it's easir to work with
    processed_text = " ".join(text)
    processed_text = ''.join(i for i in processed_text if i.isalpha()).upper()

    probable_key_sizes = {}

    trigrams: list[str] = []

    # generating possible trigrams
    for i in range(len(processed_text) - 2):
        trigrams.append(processed_text[i:i+3])

    # creating a set with unique trigrams found
    trigrams_set = set(trigrams)

    # for each unique trigram found, we search for the positions of them in our trigrams list
    for unique_trigram in trigrams_set:
        found_in_pos: list[int] = []

        for i in range(len(trigrams)):
            if unique_trigram == trigrams[i]:
                found_in_pos.append(i)

        if (len(found_in_pos) >= 2):
            for i in range(len(found_in_pos) - 1):
                distance = found_in_pos[i+1] - found_in_pos[i]

                for factor in get_factors(distance):
                    if factor in probable_key_sizes:
                        probable_key_sizes[factor] += 1
                    else:
                        probable_key_sizes[factor] = 1

    # getting most probable key_size
    probable_key_sizes = dict(sorted(
        probable_key_sizes.items(), key=lambda item: item[1], reverse=True))

    key_size = list(probable_key_sizes.keys())[0]
    key = ""
    # iterating from 0 to key_size
    for i in range(key_size):

        # we can calculate letter frequencies of this part
        part = processed_text[i::key_size]

        frequencies = []

        for j in range(ord("A"), ord("Z") + 1):
            frequencies.append(part.count(chr(j))/len(part) * 100)

        # here we get the shift value
        value: float = 99999.9
        shifts = 0

        # testing for all possible shifts
        for test in range(0, 26):

            temp_value: float = 0

            for j in range(0, 26):
                temp_value += abs(pt_letter_prob[j] - frequencies[j])

            if temp_value < value:
                value = temp_value
                shifts = test

            frequencies.append(frequencies.pop(0))

        key += chr(shifts + ord("A"))

    return key


def main():
    text = read_file("desafio1.txt")
    print(vigenere_discover_key(text))


if __name__ == "__main__":
    main()
