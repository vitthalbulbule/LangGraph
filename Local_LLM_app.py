from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

response = llm.invoke("Explain RAG in 3 simple sentences.")
print(response.content)