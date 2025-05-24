from openai import OpenAI
import os

SYSTEM_PROMPT = """
You are a professional translator fluent in Traditional Chinese and Indonesian. Automatically detect which language the input is in. If it is in Traditional Chinese, translate it into natural, conversational Indonesian. If it is in Indonesian, translate it into natural, conversational Traditional Chinese. Maintain the original tone, meaning, and style of casual everyday conversation. Respond with translated text only — no explanations or extra comments.
"""


def call_openAI(prompt):
    API_KEY = os.getenv("GPT_API_KEY")
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": [{"type": "text", "text": SYSTEM_PROMPT}],
                },
                {"role": "user", "content": f"{prompt}"},
            ],
            response_format={"type": "text"},
            temperature=0.3,
            max_completion_tokens=4096,
        )
    except Exception as e:
        print(f"API 呼叫錯誤: {e}")
        return None
    return response.choices[0].message.content


# test = post_to_json(df['post'].loc[13])
# json.loads(call_openAI(test))
