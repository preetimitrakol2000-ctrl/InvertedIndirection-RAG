#ifndef INVERTED_INDEX_H
#define INVERTED_INDEX_H

typedef struct PostNode PostNode;
typedef struct InvertedIndex InvertedIndex;

InvertedIndex* init_index();
void map_token(InvertedIndex* idx, const char* token, int chunk_id);
void gather_chunks(InvertedIndex* idx, const char* token, int* out_array, int* out_count);

#endif
