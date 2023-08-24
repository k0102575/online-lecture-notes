import openai
from dotenv import dotenv_values
import argparse

# env 세팅
config = dotenv_values("../.env")
openai.api_key = config["OPENAI_API_KEY"]

# 색상, bold 처리 함수
def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end


def main():
    # 설명
    parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-4")

    # 옵션 이름 및 타입
    parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality", default="friendly and helpful")

    # 변수로 설정
    args = parser.parse_args()

    # 챗봇 성격 입력을 위한 inital 입력
    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    # 메시지 리스트
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            # 유저 입력 부분
            user_input = input(bold(blue("You: ")))
            # 질문 메시지 저장
            messages.append({"role": "user", "content": user_input})

            # API 호출
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )  

            # 응답 메시지 저장
            messages.append(res["choices"][0]["message"].to_dict())
            # 응답 메시지 출력
            print(bold(red("Assistant: ")),res["choices"][0]["message"]["content"])

        # Ctrl + C 눌렀을때 종료 문구 출력
        except KeyboardInterrupt:
            print("Exiting...")
            break

    print(res)

if __name__ == "__main__":
    main()
