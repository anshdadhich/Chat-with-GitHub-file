from code_chunker.Chunker import CodeChunker

def chunks(file_data,file_extention):
    chunker = CodeChunker(file_extention,encoding_name = "gpt-4")
    chunk = chunker.chunk(file_data,token_limit = 500)
    return chunk
