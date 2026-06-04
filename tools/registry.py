from tools.file_tools import read_file
from tools.rag_tools import search as search_docs


TOOLS = {
    "read_file": read_file,
    "search_docs": search_docs
}
