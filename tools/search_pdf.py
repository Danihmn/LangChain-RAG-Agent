from langchain_core.tools import tool

from vector_store import retriever


@tool(
    "search_pdf",
    description="Search PDF",
    response_format="content_and_artifact"
)
def search_pdf(query):
    retrieved_information = retriever.invoke(query)
    content = "\n\n".join(
        f"[Page {p.metadata['page']}]\n({p.page_content})" for p in retrieved_information
    )
    return content, retrieved_information
