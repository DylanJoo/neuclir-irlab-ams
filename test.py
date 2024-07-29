import re

def citation_fixing(x):
    # cite with the word 'document'
    incorrect_citations = re.findall(r'Document \[\d+\]', x)
    for item in incorrect_citations:
        cite = re.findall(r'\[\d+\]', item) # extract number
        x = x.replace(item, f"{cite}")

    # cite after punctuation --> cite before punc
    incorrect_citations = re.findall(r"\.\s*\[\d+\](?:\[\d+\])?", x)
    for item in incorrect_citations:
        cite = re.findall(r'\[\d+\](?:\[\d+\])?', item)[0] # extract number
        x = x.replace(item, f" {cite}.")
    return x


a = "hello world [1][2][3]. Example 2. [2][4] Example 3. [10]"

print(a)
print(citation_fixing(a))
