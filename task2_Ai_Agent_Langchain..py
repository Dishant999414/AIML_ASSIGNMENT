from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


template = PromptTemplate.from_template("""
You are a helpful AI assistant.

User Message:
{message}

Your Task:
- Understand user input
- Generate a friendly and relevant response
- Keep your answer simple and clear

Reply:
""")


parser = StrOutputParser()


agent = template | model | parser

def run_agent():
    print("AI Agent Started. Type 'exit' to stop.\n")
    
    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Agent Stopped.")
            break

        response = agent.invoke({"message": user_input})
        print("\nAI:", response, "\n")


if __name__ == "__main__":
    run_agent()

