words = ["python", "Java", "c++", "Rust", "go"]
new_words = [word.upper() for word in words if len(word) > 3]
print(*new_words)
