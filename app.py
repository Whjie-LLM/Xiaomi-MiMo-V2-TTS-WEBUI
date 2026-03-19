import gradio as gr
from Xiaomi_MiMo_V2_TTS import generate_mimo_v2_tts
from mimo_audio import extract_mimo_audio
import os

def process_tts(text, voice, audio_format, temperature, top_p, max_tokens, presence_penalty, frequency_penalty):
    if not text.strip():
        return None, "请输入文本内容。"
    
    # 1. 调用 TTS 接口生成 JSON (debug_res.json)
    # 强制使用 mimo-v2-tts 模型
    model = "mimo-v2-tts"
    success = generate_mimo_v2_tts(
        text=text,
        model=model,
        voice=voice,
        audio_format=audio_format,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty
    )
    
    if success:
        # 2. 从 JSON 中提取音频并保存为 MP3 (文件名后缀根据格式变化)
        output_file = f"mimo_voice_output.{audio_format}"
        audio_path = extract_mimo_audio("debug_res.json", output_file)
        
        if audio_path and os.path.exists(audio_path):
            return audio_path, f"语音合成成功！使用模型: {model}, 音色: {voice}, 格式: {audio_format}"
        else:
            return None, "音频提取失败，请检查 debug_res.json 格式。"
    else:
        return None, "接口请求失败，请检查 API KEY 或网络连接。"

# 创建 Gradio 界面
with gr.Blocks(title="Mimo AI 语音合成增强版", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ Mimo AI 语音合成 (V2-TTS 增强版)")
    gr.Markdown("配置更详细的参数，定制您的专属语音。")
    
    with gr.Row():
        # 左侧配置面板
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ 音频配置")
            voice_dropdown = gr.Dropdown(
                choices=["mimo_default", "default_en", "default_zh"],
                value="mimo_default",
                label="音色选择"
            )
            format_radio = gr.Radio(
                choices=["mp3", "wav", "pcm"],
                value="mp3",
                label="音频格式"
            )
            
            with gr.Accordion("高级参数调节", open=False):
                temp_slider = gr.Slider(0, 1.5, value=0.6, step=0.1, label="Temperature (采样温度)")
                top_p_slider = gr.Slider(0.01, 1.0, value=0.95, step=0.01, label="Top P (核采样概率)")
                max_tokens_slider = gr.Slider(0, 8192, value=8192, step=128, label="Max Tokens (最大长度)")
                presence_slider = gr.Slider(-2.0, 2.0, value=0.0, step=0.1, label="Presence Penalty (话题多样性)")
                freq_slider = gr.Slider(-2.0, 2.0, value=0.0, step=0.1, label="Frequency Penalty (内容重复度)")

        # 右侧输入输出面板
        with gr.Column(scale=2):
            gr.Markdown("### 📝 文本输入与结果")
            input_text = gr.Textbox(
                label="输入文本", 
                placeholder="请输入你想转换成语音的文字...", 
                lines=10
            )
            submit_btn = gr.Button("🚀 开始合成", variant="primary")
            
            with gr.Group():
                output_audio = gr.Audio(label="生成的语音", type="filepath")
                status_msg = gr.Textbox(label="状态提示", interactive=False)

    # 绑定事件
    submit_btn.click(
        fn=process_tts,
        inputs=[
            input_text, 
            voice_dropdown, 
            format_radio, 
            temp_slider, 
            top_p_slider, 
            max_tokens_slider, 
            presence_slider, 
            freq_slider
        ],
        outputs=[output_audio, status_msg]
    )

if __name__ == "__main__":
    demo.launch()
