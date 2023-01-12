
import openai

openai.api_key = "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"


def get_ai_response(input_text):
    return openai.Completion.create(model="text-babbage-001",
                                    prompt=input_text,
                                    temperature=1,
                                    max_tokens=256,
                                    top_p=1)

