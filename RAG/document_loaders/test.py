from langchain_docling.loader import DoclingLoader
# from langchain_text_splitters import CharacterTextSplitter
# from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

# splitter = CharacterTextSplitter(
#     separator="" # if separator not used then default split is based on new lines
#     , chunk_size = 10, chunk_overlap = 1
# )

# splitter = TokenTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 10
# )

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100, chunk_overlap = 10
)

data = DoclingLoader("RAG/document_loaders/resume.pdf")

docs = data.load()

# print(docs)
# print(len(docs))

chunks = splitter.split_documents(docs)

# print(chunks[0].page_content)
# print(len(chunks))

for chunk in chunks :
    print(chunk.page_content)