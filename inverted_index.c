#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct PostNode {
    int target_chunk_id;
    struct PostNode* next;
} PostNode;

typedef struct {
    PostNode* heads[26];
} InvertedIndex;

#ifdef _WIN32
    __declspec(dllexport) InvertedIndex* init_index();
    __declspec(dllexport) void map_token(InvertedIndex* idx, const char* token, int chunk_id);
    __declspec(dllexport) void gather_chunks(InvertedIndex* idx, const char* token, int* out_array, int* out_count);
#endif

InvertedIndex* init_index() {
    InvertedIndex* idx = (InvertedIndex*)malloc(sizeof(InvertedIndex));
    for (int i = 0; i < 26; i++) idx->heads[i] = NULL;
    return idx;
}

void map_token(InvertedIndex* idx, const char* token, int chunk_id) {
    int bucket = (token[0] >= 'a' && token[0] <= 'z') ? (token[0] - 'a') : 0;
    PostNode* node = (PostNode*)malloc(sizeof(PostNode));
    node->target_chunk_id = chunk_id;
    node->next = idx->heads[bucket];
    idx->heads[bucket] = node;
}

void gather_chunks(InvertedIndex* idx, const char* token, int* out_array, int* out_count) {
    int bucket = (token[0] >= 'a' && token[0] <= 'z') ? (token[0] - 'a') : 0;
    PostNode* curr = idx->heads[bucket];
    int count = 0;
    while (curr && count < 10) {
        out_array[count++] = curr->target_chunk_id;
        curr = curr->next;
    }
    *out_count = count;
}
