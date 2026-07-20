from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import Optional
from key import api_key
import json

class PlanSteps(BaseModel):
    step_name: str

class ExecuteTask(BaseModel):
    task_name: str
    action_performed: str
    summary: str
    simulated_data: Optional[str] =  None


def callmodel(prompt, schema):
    response = chat.send_message(prompt, config=types.GenerateContentConfig(
            response_schema=schema,
            response_mime_type="application/json",
            system_instruction="Answer within 30 words"
    ))
    return response.text


def plan_goal():
    plan_prompt = "Break the goal into clear, numbered steps"
    plans = callmodel(plan_prompt, list[PlanSteps])
    plans = json.loads(plans)
    steps = [ plan['step_name'].strip() for plan in plans if plan['step_name'].strip() ]
    return steps


def execute_step(step):
    print("----------")
    action_prompt = f"Execute this task : {step}. Describe what you did and summarize the result. Simulate the task if required."
    result = callmodel(action_prompt, ExecuteTask)
    result = json.loads(result)

    print("Task : ", result['task_name'])
    print("Action : ", result['action_performed'])
    print("Summary : ", result['summary'])

    if result['simulated_data']:
        print("Data : ", result['simulated_data'].strip())
        print("----------")
    

def run_agent():
    steps = plan_goal()
    for step in steps:
         execute_step(step)
    print("\n completed steps \n ")



if __name__ == "__main__":
    client = genai.Client(api_key=api_key)
    model="gemini-3.1-flash-lite"
    chat = client.chats.create(model=model)
    goal = "Book a ticket from Bangalore to San Francisco"
    print(f"Goal : {goal}")
    modified_goal =  f""" You are a virtual agent expert in booking tickets. Your goal is {goal}
                        For now acknowledge the goal, going forward I will be asking you to create a goal and execute the goal
                        """

    chat.send_message(modified_goal)
    run_agent()

# run -> plan steps -> execute steps
