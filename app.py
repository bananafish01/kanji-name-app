import streamlit as st
from openai import OpenAI

# 1. アプリのタイトル表示
st.title("✨ Convert Your Name to Japanese Kanji Name")

# 2. サイドバーにAPIキーの入力欄を作る
#api_key = st.sidebar.text_input("OpenAI API Keyを入力してください", type="password")
api_key = st.secrets["OPENAI_API_KEY"] 

# 3. APIキーが入力されている場合のみ、メインの処理を行う
if api_key:
    # OpenAIクライアントの準備
    client = OpenAI(api_key=api_key)

    # 名前入力欄
    english_name = st.text_input("Enter your name (eg: Kevin Costner)")

    # ボタンが押された時の処理
    if st.button("Convert to Kanji"):
        if english_name:
            with st.spinner('AI is thinking of beautiful Kanji names...'):
                try:
                    # AIへの指示（プロンプト）
                    prompt = f"Translate the English name '{english_name}' into 3 beautiful Japanese Kanji name options. For each, provide: 1. Kanji, 2. Reading (Hiragana), 3. Meaning/Reason in Japanese."

                    # OpenAI APIを呼び出し
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    # 結果を表示
                    result = response.choices[0].message.content
                    st.success("Conversion completed!  ")
                    st.markdown("---")
                    st.write(result)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a name.")
else:
    # APIキーが未入力の時に表示するメッセージ
    st.info("左側のサイドバーに、OpenAIのAPIキーを入力してください。")