"""
Simple LangGraph Echo Agent

A basic agent that echoes user messages with a friendly greeting.
This demonstrates LangGraph basics without requiring an LLM API key.
"""

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
import os
from datetime import datetime

# State definition
class State(TypedDict):
    """The state of the agent graph."""
    messages: Annotated[list, add_messages]
    timestamp: str
    message_count: int

# Node functions
def echo_node(state: State) -> dict:
    """
    Echo the user's message with a friendly greeting.
    
    This is a simple node that doesn't use an LLM - it just
    processes the input and returns a response.
    """
    messages = state.get("messages", [])
    message_count = state.get("message_count", 0) + 1
    
    if not messages:
        return {
            "messages": [{"role": "assistant", "content": "Hello! Send me a message and I'll echo it back."}],
            "timestamp": datetime.now().isoformat(),
            "message_count": message_count
        }
    
    last_message = messages[-1]
    user_content = last_message.get("content", "")
    
    # Simple processing - echo with greeting
    response = f"🤖 Echo Agent [Message #{message_count}]: You said '{user_content}'"
    
    # Add some basic command handling
    if "hello" in user_content.lower():
        response = f"👋 Hello! Nice to meet you! (Message #{message_count})"
    elif "help" in user_content.lower():
        response = f"ℹ️ I'm a simple echo agent. I repeat what you say! Try: hello, status, or any message. (Message #{message_count})"
    elif "status" in user_content.lower():
        response = f"✅ Agent Status: Running | Messages processed: {message_count} | Time: {datetime.now().strftime('%H:%M:%S')}"
    elif "bye" in user_content.lower() or "goodbye" in user_content.lower():
        response = f"👋 Goodbye! Thanks for chatting! (Message #{message_count})"
    
    return {
        "messages": [{"role": "assistant", "content": response}],
        "timestamp": datetime.now().isoformat(),
        "message_count": message_count
    }

def greeting_node(state: State) -> dict:
    """Initial greeting node."""
    return {
        "messages": [{"role": "assistant", "content": "👋 Welcome to Test Project 1 Echo Agent! Type 'help' for commands."}],
        "timestamp": datetime.now().isoformat(),
        "message_count": 0
    }

# Build the graph
def create_graph():
    """Create and compile the LangGraph agent."""
    workflow = StateGraph(State)
    
    # Add nodes
    workflow.add_node("greeting", greeting_node)
    workflow.add_node("echo", echo_node)
    
    # Add edges
    workflow.add_edge(START, "greeting")
    workflow.add_edge("greeting", "echo")
    workflow.add_edge("echo", END)
    
    # Compile
    return workflow.compile()

# Create the graph instance
graph = create_graph()

# For testing locally
if __name__ == "__main__":
    print("🚀 Test Project 1 - Echo Agent")
    print("=" * 50)
    print("\nTesting the agent locally...\n")
    
    # Test cases
    test_messages = [
        "Hello!",
        "help",
        "What's the weather?",
        "status",
        "goodbye"
    ]
    
    for msg in test_messages:
        print(f"👤 User: {msg}")
        
        result = graph.invoke({
            "messages": [{"role": "user", "content": msg}],
            "timestamp": datetime.now().isoformat(),
            "message_count": 0
        })
        
        last_response = result["messages"][-1]["content"]
        print(f"🤖 Agent: {last_response}")
        print(f"   Timestamp: {result['timestamp']}")
        print(f"   Message Count: {result['message_count']}\n")
    
    print("✅ Local testing complete!")
