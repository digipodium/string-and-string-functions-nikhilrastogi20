paragraph = '''this is a paragraph which is 
written just for the purpose
of providing content to let the 
average word length be calculated'''

words = paragraph.split()
average = sum(len(word) for word in words) / len(words)
print  (average)
