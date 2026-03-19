import os
import json
import requests

def generate_mimo_v2_tts(
    text, 
    model="mimo-v2-tts", 
    voice="mimo_default", 
    audio_format="mp3",
    temperature=0.6,
    top_p=0.95,
    max_tokens=8192,
    presence_penalty=0.0,
    frequency_penalty=0.0
):
    # 1. 基础配置
    API_KEY = "填入你自己的api密钥"
    url = "https://api.xiaomimimo.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 2. 构造符合文档要求的请求体
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user", 
                "content": "请帮我朗读以下内容"
            },
            {
                "role": "assistant", 
                "content": text
            }
        ],
        "audio": {
            "format": audio_format,
            "voice": voice
        },
        "temperature": temperature,
        "top_p": top_p,
        "max_completion_tokens": max_tokens,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stream": False
    }

    print(f"正在通过 Chat 接口触发 {model} TTS 合成 (音色: {voice}, 格式: {audio_format})...")

    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            # 保存完整 JSON 供调试
            with open("debug_res.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            print(f"✅ 收到响应，已保存至 debug_res.json")
            return True
        else:
            print(f"❌ 报错 {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 运行异常: {e}")
        return False

if __name__ == "__main__":
    my_text = "你好，我是小米自研的智能语音代理，现在正在为你测试语音输出。"
    generate_mimo_v2_tts(my_text)