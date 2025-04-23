import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
# st.set_page_config(
#     page_title="Streamlit デモ",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ============================================
# タイトルと説明
# ============================================
st.title("Streamlit 初心者向けデモ")

# 投稿日・更新日
created_date = "2025-04-17"
updated_date = "2025-04-23"

st.markdown(f"""
<span style='color: black; font-size: 14px;'>
📅 投稿日: {created_date}　　🛠 最終更新: {updated_date}
</span>
""", unsafe_allow_html=True)

st.markdown("\n")
st.markdown("このページでは、Streamlitの基本UIを実際に体験しながら学べます。")

st.markdown("---")

# ============================================
# サイドバー 
# ============================================
# st.sidebar.header("デモのガイド")
# st.sidebar.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。")

# いいねボタンとSNS共有ボタン
st.sidebar.markdown("""
<style>
.like-btn {
    display: inline-block;
    padding: 8px 16px;
    margin-bottom: 10px;
    background-color: #ffcc00;
    color: #333;
    font-weight: bold;
    border-radius: 25px;
    text-align: center;
    cursor: pointer;  /* 修正: カーソルをポインターに変更 */
    user-select: none;
}
.sns-btn {
    display: inline-block;
    padding: 8px 12px;
    margin: 4px 4px 0 0;
    background-color: #1DA1F2;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;  /* 修正: カーソルをポインターに変更 */
    user-select: none;
}
</style>

<span class="like-btn">👍 いいね！</span>

### 🔗 SNSで共有する
<div>
    <span class="sns-btn">X</span>
    <span class="sns-btn" style="background-color:#4267B2;">Facebook</span>
    <span class="sns-btn" style="background-color:#25D366;">LINE</span>
</div>
""", unsafe_allow_html=True)


# ============================================
# 基本的なUI要素
# ============================================
st.header("基本的なUI要素")
st.markdown("---")

# テキスト入力
st.subheader("テキスト入力")
name = st.text_input("あなたの名前", "ゲスト")
st.write(f"こんにちは、{name}さん！")

st.markdown("---")

# ボタン
st.subheader("ボタン")
if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")

st.markdown("---")

# チェックボックス
st.subheader("チェックボックス")
if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
    st.info("これは隠れたコンテンツです！")

st.markdown("---")

# スライダー
st.subheader("スライダー")
age = st.slider("年齢", 0, 100, 25)
st.write(f"あなたの年齢: {age}")

st.markdown("---")

# セレクトボックス
st.subheader("セレクトボックス")
option = st.selectbox(
    "好きなプログラミング言語は?",
    ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
)
st.write(f"あなたは{option}を選びました")

st.markdown("---")

# ============================================
# レイアウト
# ============================================
st.header("レイアウト")
st.markdown("---")

# カラム
st.subheader("カラムレイアウト")
col1, col2 = st.columns(2)
with col1:
    st.write("これは左カラムです")
    st.number_input("数値を入力", value=10)
with col2:
    st.write("これは右カラムです")
    st.metric("メトリクス", "42", "2%")

st.markdown("---")

# タブ
st.subheader("タブ")
tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
with tab1:
    st.write("これは第1タブの内容です")
with tab2:
    st.write("これは第2タブの内容です")

st.markdown("---")

# エクスパンダー
st.subheader("エクスパンダー")
with st.expander("詳細を表示"):
    st.write("これはエクスパンダー内の隠れたコンテンツです")
    st.code("print('Hello, Streamlit！')")

st.markdown("---")

# ============================================
# データ表示
# ============================================
st.header("データの表示")
st.markdown("---")

# サンプルデータフレームを作成
df = pd.DataFrame({
    '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
    '年齢': [25, 30, 22, 28, 33],
    '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']
})

# st.markdown("---")

# データフレーム表示
st.subheader("データフレーム")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# テーブル表示
st.subheader("テーブル")
st.table(df)

st.markdown("---")

# メトリクス表示
st.subheader("メトリクス")
col1, col2, col3 = st.columns(3)
col1.metric("温度", "23°C", "1.5°C")
col2.metric("湿度", "45%", "-5%")
col3.metric("気圧", "1013hPa", "0.1hPa")

st.markdown("---")

# ============================================
# グラフ表示
# ============================================
st.header("グラフの表示")
st.markdown("---")

# ラインチャート
st.subheader("ラインチャート")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])
st.line_chart(chart_data)

# バーチャート
st.subheader("バーチャート")
chart_data = pd.DataFrame({
    'カテゴリ': ['A', 'B', 'C', 'D'],
    '値': [10, 25, 15, 30]
}).set_index('カテゴリ')
st.bar_chart(chart_data)

st.markdown("---")

# ============================================
# インタラクティブ機能
# ============================================
st.header("インタラクティブ機能")
st.markdown("---")

# プログレスバー
st.subheader("プログレスバー")
progress = st.progress(0)
if st.button("進捗をシミュレート"):
    for i in range(101):
        time.sleep(0.01)
        progress.progress(i / 100)
    st.balloons()

st.markdown("---")

# ファイルアップロード
st.subheader("ファイルアップロード")
uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
if uploaded_file is not None:
    # ファイルのデータを表示
    bytes_data = uploaded_file.getvalue()
    st.write(f"ファイルサイズ: {len(bytes_data)} bytes")
    
    # CSVの場合はデータフレームとして読み込む
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("CSVデータのプレビュー:")
        st.dataframe(df.head())

st.markdown("---")

# ============================================
# カスタマイズ
# ============================================
st.header("スタイルのカスタマイズ")
st.markdown("---")

# カスタムCSS
st.markdown("""
<style>
.big-font {
    font-size:20px ！important;
    font-weight: bold;
    color: #0066cc;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">これはカスタムCSSでスタイリングされたテキストです！</p>', unsafe_allow_html=True)



# ============================================
# デモの使用方法
# ============================================
# st.divider()
# st.subheader("このデモの使い方")
# st.markdown("""
# 1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
# 2. 確認したい機能のコメントを解除します（先頭の#を削除）
# 3. 変更を保存して、ブラウザで結果を確認します
# 4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
# """)

# st.code("""
# # コメントアウトされた例:
# # if st.button("クリックしてください"):
# #     st.success("ボタンがクリックされました！")

# # コメントを解除した例:
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")
# """)