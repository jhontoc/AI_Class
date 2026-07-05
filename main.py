
import requests

def generate_x_post(usr_input: str) ->str:
prompt = f"""
        you are an expert social media manager
        your task is to generate a welcome greeting for this person
        <usr_input>
        {usr_input}
        </usr_input>
"""
payload = {
        "model":"gpt-4o",
        "input": prompt

}

response = requests.post(
        "https://ai-chat.cisco.com/bridgeit-platform/api/home"
        json=payload,
        headers={
            "content-Type": "application/json",
            "Authorization": f"Bearer "
        }
)

CISCO_AZURE_ENDPOINT = "https://chat-ai.cisco.com"
app_key = os.getenv('APP_KEY')


llm = AzureChatOpenAI(
            deployment_name="gpt-5-nano",
            azure_endpoint=CISCO_AZURE_ENDPOINT,
            api_key="x",
            http_client=httpx.Client(auth=ApiKeyAuth()),
            api_version="2023-08-01-preview",
            model_kwargs=dict(user=f'{{"appkey": "{app_key}"}}')
    )


agent_prompt = """
        You are a helpful ACI Agent that helps network engineers to find information about Endpoints in the ACI32aci1001000.

        Provide answers using emojis and in markdown format when possible
"""

agent = create_agent(llm,
                    [get_endpoint_location, get_aci_routes, list_tenants, create_tenant],
                    system_prompt=agent_prompt)



def main():
    print("Hello from ai-class!")


if __name__ == "__main__":
    main()
