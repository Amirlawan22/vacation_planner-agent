from google.adk.agents import LlmAgent,Agent
from google.adk.tools import AgentTool


# hotel sub-agent
hotels_expert = LlmAgent(
    name="hotels_expert",
    model="gemini-2.0-flash",
    description="Suggests hotels in a specified destination based on the user's input",
    instruction="Recommend hotels for the user's vacation.",
    tools=[]
)

# activities sub_agent
activities_expert = LlmAgent(
    name="activities_expert",
    model="gemini-2.0-flash",
    description="Suggests popular and unique activities in a specified city given by the user",
    instruction="Given the user's travel destination and any specific request, provide highly relevant and fun activities for that location.",
    tools=[]
)

# places sub_agent
places_to_visit_expert = LlmAgent(
    name="places_to_visit_expert",
    model="gemini-2.0-flash",
    description="Suggests must-see places and attractions. based on user input",
    instruction="Given the user's travel destination and any specific request, provide highly relevant, must-see places and attractions for that location.",
    tools=[]
)

# Main vacation planner agent coordinates the sub-agents
root_agent = Agent(
    name="vacation_planner",
    model="gemini-2.0-flash",
    description="Plans vacations, recommends hotels, places to visit, and activities.",
    instruction="Give vacation recommendations using specialists.",
    tools=[AgentTool(hotels_expert), AgentTool(places_to_visit_expert), AgentTool(activities_expert)],
    sub_agents=[hotels_expert, places_to_visit_expert, activities_expert]
)
