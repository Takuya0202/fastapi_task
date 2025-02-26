from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from routers.task import router as task_router

#fastapiインスタンスの作成
app=FastAPI()

#CORS設定
app.add_middleware(
    CORSMiddleware,
    #許可するオリジンの設定
    allow_origins=["http://127.0.0.1:5500"],
    #認証情報を含むリクエストの許可
    allow_credentials=True,
    #許可するメソッドの設定
    allow_methods=["*"],
    #許可するヘッダー
    allow_headers=["*"]
)

#ルータ
app.include_router(task_router)
#バリデーションエラー
@app.exception_handler(ValidationError)
async def validation_exception_handler(exc:ValidationError):
    #validationエラーが発生した時のjsonレスポンス
    return JSONResponse(
        status_code=422,
        content={
            #pydanticが提供するエラーコード
            "detail":exc.errors(),
            #バリデーションエラーが発生した時の入力エラー
            'body':exc.model,\
        }
    )
    
