import time

Song = ["Row", "row", "row", "your", "boat", "Gently", "down", "the", "stream", "Merrily", "merrily", "merrily", "merrily", "Life", "is", "but", "a", "dream",
        "Row", "row", "row", "your", "boat", "Gently", "down", "the", "stream", "Merrily", "merrily", "merrily", "merrily", "Life", "is", "but", "a", "dream",
        "Row", "row", "row", "your", "boat", "Gently", "down", "the", "stream", "Merrily", "merrily", "merrily", "merrily", "Life", "is", "but", "a", "dream",
        "Row", "row", "row", "your", "boat", "Gently", "down", "the", "stream", "Merrily", "merrily", "merrily", "merrily", "Life", "is", "but", "a", "dream"]

def Remake():
    try:
        for s in range(0, len(Song) + 1):
            time.sleep(0.3)
            print(Song)
            if len(Song) == -1:
                break
            del Song[-1]
    except IndexError:
        print("\nNo Words Left in the Song")

Remake()