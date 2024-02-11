def word_count_occurence(file_path):
    word_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            
            for word in words:
                word = word.strip(',./?:;"$!%^&*(@')
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count
                    
def display_word(word_count):
    print("Word Occurence")
    print("--------------")
    for word, count in word_count.items():
        print(word, count)
        
file_path = 'word_count_text_file'
word_count = word_count_occurence(file_path)
display(word_count)