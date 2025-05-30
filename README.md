# fastapi_task
fastapiとaiomysqlを使った非同期apiです<br>

詳しい情報は<a href="https://zenn.dev/amethyst/articles/7434635f3bd2fc" target="_blank">こちら</a>にまとめましたのでご覧ください<br>
## 技術スタック
<img src="https://img.shields.io/badge/Fastapi-green?logo=fastapi&logoColor=white" style="width:100px ; height:30px"></img>
<img src="https://img.shields.io/badge/sqlalchemy-red?logo=sqlalchemy&logoColor=black" style="width:100px ; height:30px"></img>
<img src="https://img.shields.io/badge/Mysql-lightgrey?logo=mysql&logoColor=white" style="width:100px ; height:30px"></img>
<img src="https://img.shields.io/badge/Docker-blue?logo=Docker&logoColor=white" style="width:100px ; height:30px"></img>
## セットアップ方法
```:bash
git clone https://github.com/Takuya0202/fastapi_task.git
cp .env.example .env
```
上を実行後、`.env`に情報を記載<br>
`.env`完成後以下を実行<br>
```:bash
docker compose up -d --build
docker compose exec back bash
python init_database.py
```
実行後 http://localhost:8000/docs にアクセス<br>
こちらでapiの動きを確認できます。postmanみたいなものです。以上で終わります
