from dataclasses import dataclass
from typing import List, Optional, Tuple, Union, Dict
from nltk import sent_tokenize 
from copy import copy
import random

def normalize_texts(texts):
    texts = unicodedata.normalize('NFKC', texts)
    texts = texts.strip()
    pattern = re.compile(r"\s+")
    texts = re.sub(pattern, ' ', texts).strip()
    pattern = re.compile(r"\n")
    texts = re.sub(pattern, ' ', texts).strip()
    return texts

def citation_removal(texts):
    pass

@dataclass
class ReportGenOutput:
    request_id: str
    run_id: str
    collection_ids: List[str]
    raw_report: Optional[str] = None
    cited_report: Optional[str] = None
    references: Dict[str, str] = None
    texts: List[str] = None
    citations: List[str] = None
    """ hard coded the maximum reference numbert = 2 """

    def __post_init__(self):
        if (self.raw_report is None) and (self.cited_report is not None):
            self.cited_report = normalize_texts(self.cited_report)
            self.raw_report = citation_removal(self.cited_report)
            # [NOTE] some of the texts may lack citations

        if self.texts is None:
            self.texts = sent_tokenize(self.raw_report)
        if self.citations is None:
            self.citations = [[] for _ in range(len(self.texts))]

    def finalize(self):
        sentences = []
        for text, citation in zip(self.texts, self.citations):
            sentences.append({"text": text, "citations": citation})

        return {
            "request_id": self.request_id,
            "run_id": self.run_id,
            "collection_ids": self.collection_ids,
            "sentences": sentences
        }

    ## the functions for post-cite
    def get_snippets(self, max_word_length=100):
        """ return a list of snippets as query """
        sentences = copy(self.texts)
        snippets = [""]

        while len(snippets[-1].split()) < max_word_length:

            sentence = sentences.pop(0)
            chunk = snippets[-1] + sentence

            if len(chunk.split()) < max_word_length:
                snippets[-1] = chunk
            else:
                snippets.append(sentence)

            if len(sentences) == 0:
                break

        return snippets

    def get_references(self):
        """ return a list of reference ids"""
        assert self.references is not None, 'please add referecnes first'
        reference_mapping = {v: k for k, v in self.references.items()}
        cited_references = []
        for citations in self.citations:
            cited_references.append([reference_mapping[c] for c in citations[:2]])
        return cited_references

    def set_references(self, docids, shuffle=False):
        if shuffle:
            random.shuffle(docids)
        self.references = {str(i+1): docid for i, docid in enumerate(docids)}

    def set_citations(self, idx_text, docids=None, referenceids=None):
        if docids is None:
            docids = []
            for referenceid in referenceids:
                docids.append( self.references[referenceid] )

        self.citations[idx_text] = docids

