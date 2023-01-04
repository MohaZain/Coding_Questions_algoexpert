def generateDocument(characters, document):
    # Write your code here.

    for let,doc in zip(characters,document):
        if doc not in characters:
            return False
        if characters.count(let) < document.count(let):
            return False
    return True
