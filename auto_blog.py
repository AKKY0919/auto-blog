import os
import openai
import requests
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# 環境変数からAPIキーとWordPress情報を取得
wp_url = os.getenv("WP_URL")
wp_username = os.getenv("WP_USERNAME")
wp_password = os.getenv("WP_PASSWORD")
openai_api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API 設定
openai.api_key = openai_api_key

# ブログ記事を生成
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short blog post about AI and fashion trends."}
    ]
)

blog_content = response["choices"][0]["message"]["content"]

# WordPress へ投稿
wp_client = Client(wp_url + "/xmlrpc.php", wp_username, wp_password)
post = WordPressPost()
post.title = "AI and Fashion Trends"
post.content = blog_content
post.post_status = "publish"

wp_client.call(NewPost(post))

print("✅ 投稿が完了しました！")

