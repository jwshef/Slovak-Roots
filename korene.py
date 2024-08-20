import sys

def main(all_words, bad_endings):
    sort_all_words(all_words, bad_endings)

def sort_all_words(all_words, bad_endings):
    word_list = open_file(all_words)
    simple_words = simplify(word_list, bad_endings)
    print_words(all_words)

def simplify(word_list, bad_endings):
    change_endings = open_file(bad_endings)
    for word in word_list:
        if len(word) < 4:
            reject(word)
            return
        for ending in change_endings:
            end = len(ending)
            if word[[-end]] == ending:
                reject(word)

def reject(str):
    with open('rejects.txt', 'w') as file:
                file.write(str + '\n')

def open_file(infile):
    with open(infile, encoding='utf-8') as file:
        return file.readlines()

def print_words(lines):
    with open('shorter_list.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)


if __name__ == '__main__':
    main('sk_50k.txt', 'shorter_list.txt',)
    # main(sys.argv[1], sys.argv[2])
