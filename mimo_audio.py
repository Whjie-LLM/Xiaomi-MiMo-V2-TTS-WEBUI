import json
import base64
import os

def extract_mimo_audio(json_file="debug_res.json", output_mp3="mimo_voice_output.mp3"):
    # 1. 检查文件是否存在
    if not os.path.exists(json_file):
        print(f"❌ 错误：找不到文件 {json_file}")
        return

    try:
        # 2. 读取 JSON 内容
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 3. 提取 Base64 数据
        audio_base64 = data['choices'][0]['message']['audio']['data']
        
        # 4. Base64 解码为二进制流
        audio_binary = base64.b64decode(audio_base64)
        
        # 5. 写入 MP3 文件
        with open(output_mp3, "wb") as f_out:
            f_out.write(audio_binary)
            
        print(f"✅ 成功！音频已提取并保存至: {os.path.abspath(output_mp3)}")
        return output_mp3

    except KeyError as e:
        print(f"❌ 解析错误：JSON 中缺少预期的字段 {e}")
        return None
    except Exception as e:
        print(f"❌ 运行异常: {e}")
        return None

if __name__ == "__main__":
    extract_mimo_audio()