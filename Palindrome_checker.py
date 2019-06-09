samplePhrase = "Malayalam"
givenphrase = input("\nPlease input a phrase:(Press ENTER to use the sample phrase) ")
if givenphrase == " " or not givenphrase.strip():
    print("\nThe sample phrase is: {0}".format(samplePhrase))
    phrase = samplePhrase
else:
    phrase = givenphrase

string = phrase.lower()
if string == string[:: -1]:
    print("\nWow!, The Phrase is a Palindrome")
else:
    print("\nSorry, The given phrase is not a Palindrome")
