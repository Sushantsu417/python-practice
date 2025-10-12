import threading

total_words = 0
lock = threading.Lock()

def count_words(filename):
    global total_words
    with open(filename, 'r') as f:
        text = f.read()
        word_count = len(text.split())
    with lock:
        total_words += word_count
        print(f"{filename}: {word_count} words")

files = ['file1.txt', 'file2.txt', 'file3.txt']

threads = []
for file in files:
    t = threading.Thread(target=count_words, args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nTotal words in all files: {total_words}")
