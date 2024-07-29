# closebook prompt
closebook_instruction = """
Write a journalistic report for the given request within {LIMIT} words. The request contains a problem statement and the requester background (some information might help customize the report). Use an unbiased and journalistic tone. Always write the report based on facts.
""".strip()

rag_instruction = """
Write a journalistic report for the given request using only the provided documents as references (some of which might be irrelevant). Always cite at least one document for every sentences in the report and cite at most two documents per sentence. Follow the citation format of square brackets to indicate the cited documents (e.g., [1] for citing the first document; [1][2] for citing the first two documents). Note the given request contains a problem statement and the requester background (it might help customize the report). The length of report should be within one paragraph (around {LIMIT} words). Do not add any disclaimers, notes or references in the report.""".strip()

# rag_instruction = "Write an engaging report for the given request using only the provided documents as references (some of which might be irrelevant). Always cite at least one document for every sentences in the report. Use the citation format of square brackets to indicate the cited documents (e.g., [n] for citing the n-th document). When citing multiple documents, cite the most relevant two only with the citation format of [n][m]. The given report request contains a problem statement and their background (it might help customize the contents). Compile the report into a single paragraph within {LIMIT} words, excluding disclaimers, notes, or references."

doc_prompt_template = "Document [{ID}]: {P}\n"
demo_prompt_template = "{INST}\n\n\nRequest:\nProblem statement: {PS}\nRequester background: {BG}\n\n{D}\nReport: {R}"
rag_prompt_template = "{INST}\n\n\n{DEMO}Request:\nProblem statement: {PS}\nRequester background: {BG}\n\n{D}\nReport: {R}"
closebook_prompt_template = "{INST}\n\nRequest:\nProblem statement: {PS}\nRequester background: {BG}\n\nReport: {R}"

def apply_docs_prompt(doc_items, ndoc=None, field='text', max_length=None):
    p = ""
    for idx, doc_item in enumerate(doc_items[:ndoc]):
        p_doc = doc_prompt_template
        p_doc = p_doc.replace("{ID}", str(idx+1))
        if field == 'translation':
            truncated_doc = " ".join(doc_item[field].split()[:max_length])
        else:
            truncated_doc = doc_item[field][:max_length]
        p_doc = p_doc.replace("{P}", truncated_doc)
        p += p_doc
    return p

def display_nextlines(texts):
    texts = texts.replace('\n', '\\n')
    return texts

def apply_demo_prompt(PS, BG, LIMIT=100, D="", R="", INST=""):
    p = demo_prompt_template
    p = p.replace("{INST}", INST).replace("{LIMIT}", str(LIMIT//10)).strip()
    p = p.replace("{PS}", PS).replace("{BG}", BG)
    p = p.replace("{D}", D).replace("{R}", R)
    return p

def apply_rag_prompt(PS, BG, LIMIT=100, D="", R="", INST=""):
    p = rag_prompt_template
    p = p.replace("{INST}", INST).replace("{LIMIT}", str(LIMIT//10)).strip()
    p = p.replace("{PS}", PS).replace("{BG}", BG)
    p = p.replace("{D}", D).replace("{R}", R)
    return p

def apply_closebook_prompt(PS, BG, LIMIT=100, R="", INST=""):
    p = closebook_prompt_template
    p = p.replace("{INST}", INST).replace("{LIMIT}", str(LIMIT//10)).strip()
    p = p.replace("{PS}", PS).replace("{BG}", BG)
    p = p.replace("{R}", R)
    return p
