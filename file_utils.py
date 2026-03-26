def read_lines(filename: str) -> list:

    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


def write_lines(filename: str, lines: list[str]) -> bool:

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return True


def count_words(filename: str) -> dict:

    word_count = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()

            for word in words:
                word = word.lower().strip(",")
                word_count[word] = word_count.get(word, 0) + 1

    return word_count
