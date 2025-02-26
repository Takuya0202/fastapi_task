from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.task import CreateAndUpdateTaskSchema,TaskSchema,ResponseSchema
import cruds.task as crud_task
from db import get_session

#ルータの作成
router = APIRouter(tags=["Tasks"],prefix="/tasks")

#タスク追加のエンドポイント
@router.post('/',response_model=ResponseSchema)
async def create_task(task:CreateAndUpdateTaskSchema,db:AsyncSession = Depends(get_session)):
    try:
        await crud_task.create_task(db=db,task=task)
        return ResponseSchema(message="タスクの追加に成功しました")
    except Exception as e:
        raise HTTPException(status_code=400,detail="タスクの追加に失敗しました")
    
#タスク一覧のエンドポイント
@router.get('/',response_model=list[TaskSchema])
async def get_tasks(db:AsyncSession = Depends(get_session)):
    tasks = await crud_task.get_tasks(db=db)
    return tasks

#タスク詳細のエンドポイント
@router.get('/{task_id}',response_model=TaskSchema)
async def get_task_detail(task_id:int,db:AsyncSession = Depends(get_session)): 
    task = await crud_task.get_task_detail(db=db,task_id=task_id)
    #タスクがなかった場合
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    return task

#タスク更新のエンドポイント
#一言　引数の順番が大事。task_idとtaskはdbの後に書くとエラーが出る
@router.put('/{task_id}',response_model=ResponseSchema)
async def update_task(task_id:int,task:CreateAndUpdateTaskSchema,
                    db:AsyncSession = Depends(get_session),):
    fixed_task = await crud_task.update_task(db=db,task=task,task_id=task_id)
    #タスクがなかった時
    if not fixed_task:
        raise HTTPException(status_code=404,detail="task not found")
    return ResponseSchema(message="タスクの更新に成功しました")
    
#タスク削除
@router.delete('/{task_id}',response_model=ResponseSchema)
async def delete_task(task_id:int,db:AsyncSession = Depends(get_session)):
    task = await crud_task.delete_task(db=db,task_id=task_id)
    #タスクが見つからなかった時
    if not task:
        raise HTTPException(status_code=404,detail='task not found')
    return ResponseSchema(message='タスクの削除に成功しました')