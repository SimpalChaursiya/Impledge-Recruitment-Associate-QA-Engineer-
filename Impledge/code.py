import time

def is_compound_word(word, word_set, memo):
    if word in memo:
        return memo[word]
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_set:
            if suffix in word_set or is_compound_word(suffix, word_set, memo):
                memo[word] = True
                return True
    memo[word] = False
    return False

def find_longest_compound_words(file_path):
    start_time = time.time()
    
    # Read and store words
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    
    word_set = set(words)
    memo = {}
    compound_words = []

    for word in words:
        if is_compound_word(word, word_set, memo):
            compound_words.append(word)
    
    compound_words.sort(key=lambda x: len(x), reverse=True)
    
    end_time = time.time()
    processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return {
        "longest": compound_words[0] if len(compound_words) > 0 else None,
        "second_longest": compound_words[1] if len(compound_words) > 1 else None,
        "time_taken_ms": processing_time
    }

# Example Usage
file_path_1 = "Input_01.txt"
file_path_2 = "Input_02.txt"

result_1 = find_longest_compound_words(file_path_1)
result_2 = find_longest_compound_words(file_path_2)

print("Input_01 Results:", result_1)
print("Input_02 Results:", result_2)
