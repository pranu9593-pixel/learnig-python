# vowels_count.py
s = input("Enter text: ").lower()
vowels = 'aeiou'
count = sum(1 for char in s if char in vowels)
print(f"Vowels count: {count}")
