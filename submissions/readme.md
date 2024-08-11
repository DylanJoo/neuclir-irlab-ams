# Submission runs
---
## Post-hoc citation
- `irlab-ams-poscite`
    * Query rewriting by ChatGPT: [data/gptqr-test-all.json](data/gptqr-test-all.json).
    * Singe-stage retrieval: ColBERT (sentence as query) top-2 
- `irlab-ams-poscite-v`
    * Query rewriting by ChatGPT: [data/gptqr-test-all.json](data/gptqr-test-all.json).
    * Multi-stage retrieval-reranking
        * ColBERT (statement as query) top-30 retrieval
        * Aggregate total retrieved documents
        * XNLI re-ranking

## Standard RAG
- `irlab-ams-std-translate-llama-70B`
    * ColBERT top-10 retrieval
    * Google translate
    * Direct prompting

- `irlab-ams-std-translate-llama-8B`
    * ColBERT top-10 retrieval
    * Google translate
    * Direct prompting
