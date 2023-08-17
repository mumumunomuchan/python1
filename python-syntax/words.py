# this should print "HELLO", "HEY", "YO", and "YES"

def print_upper_words3(words, must_start_with):
    for word in words:
         for letter in must_start_with:
              if word.startswith(letter):
                   print(word.upper())
                   break

print_upper_words3(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])
