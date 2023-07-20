from transliterate import translit
from num2words import num2words


def get_translit():
    text = f"""

Ladies and gentlemen, I'm {get_words_from_nums(78)} years old and I finally got {get_words_from_nums(15)} minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.

More than {get_words_from_nums(3)} years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last {get_words_from_nums(40)}. When I was {get_words_from_nums(8)}...
"""
    return translit(text, 'ru')


def get_words_from_nums(num):
    word = num2words(num)
    return word


def main():
    get_translit()
    print(get_translit())


if __name__ == '__main__':
    main()
