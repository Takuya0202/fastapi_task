from pydantic import BaseModel,Field

#タスクを追加するときのスキーマ
class CreateAndUpdateTaskSchema(BaseModel):
    #タスクのタイトル
    title:str = Field(...,
                    description="タスクのタイトル.必須項目、一文字以上最大二十文字まで",
                    example="筋トレ",
                    min_length=1,
                    max_length=20)
    #タスクの内容
    content:str = Field(default='',
                        description='タスクの詳細。任意の項目',
                        example="腹筋トレーニング")

#タスクの情報を渡すときのスキーマ
class TaskSchema(CreateAndUpdateTaskSchema):
    #タスクのid
    id:int = Field(...,
                description="タスクのid。dbから自動でゲットする",
                example="1")

#タスクの追加や更新、削除ができた際にレスポンスするスキーマ
class ResponseSchema(BaseModel):
    message:str = Field(...,
                        description="処理結果のmessage",
                        example="タスクの追加に成功しました")