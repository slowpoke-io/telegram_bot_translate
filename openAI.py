from openai import OpenAI
import os

SYSTEM_PROMPT = """
You are a professional translator fluent in Traditional Chinese and Indonesian. Automatically detect which language the input is in. If it is in Traditional Chinese, translate it into natural, conversational Indonesian. If it is in Indonesian, translate it into natural, conversational Traditional Chinese. Maintain the original tone, meaning, and style of casual everyday conversation. Respond with translated text only — no explanations or extra comments.
"""
SYSTEM_PROMPT = """
你是一位專業的翻譯員，精通繁體中文與印尼文。請自動判斷輸入文字的語言：
如果是繁體中文，請將其翻譯為自然流暢、口語化的印尼文。
如果是印尼文，請將其翻譯為自然流暢、口語化的繁體中文。
請保留原文的語氣、語意與風格，讓翻譯聽起來像日常對話。
僅輸出翻譯後的內容，不要有任何說明或多餘文字
"""


def call_openAI(prompt):
    API_KEY = os.getenv("GPT_API_KEY")
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": [{"type": "text", "text": SYSTEM_PROMPT}],
                },
                {"role": "user", "content": f"{prompt}"},
            ],
            # response_format={"type": "text"},
            temperature=0.4,
            max_completion_tokens=4096,
        )
    except Exception as e:
        print(f"API 呼叫錯誤: {e}")
        return None
    return response.choices[0].message.content


# test = post_to_json(df['post'].loc[13])
# json.loads(call_openAI(test))
