from index_bridge import IndexBridge

if __name__ == "__main__":
    lexical_index = IndexBridge()

    # Map text keywords down to structural source files
    lexical_index.index_word("kernel", 801)
    lexical_index.index_word("kubernetes", 802)

    query_term = "kernel"
    matched_references = lexical_index.search_word(query_term)

    print("=== INVERTEDINDIRECTION-RAG HYBRID TARGETER ===")
    print(f"[*] Lexical Pointer Query for '{query_term}' returned Document Shards: {matched_references}")
