def main():
    sort_all_words()

def sort_all_words():
    all_words = open_file()
    print_words(all_words)

def open_file():
    with open('sk_50k.txt', encoding='utf-8') as file:
        return file.readlines()

def print_words(lines):
    with open('shorter_list.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)

if __name__ == '__main__':
    main()
