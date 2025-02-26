from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.task import CreateAndUpdateTaskSchema,TaskSchema
from models.task import Task
from datetime import datetime

#タスク追加
async def create_task(db:AsyncSession,task:CreateAndUpdateTaskSchema) ->Task:
    #入力されたタスクを辞書形式で受け取る
    new_task = Task(**task.model_dump())
    #dbに追加してコミット
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

#タスク一覧
async def get_tasks(db:AsyncSession) ->list[Task]:
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks

#タスク詳細
async def get_task_detail(db:AsyncSession,task_id:int) -> Task | None:
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalars().first()
    return task

#タスク更新
async def update_task(db:AsyncSession,
                    task_id:int,task:CreateAndUpdateTaskSchema) -> Task | None:
    #タスク詳細の関数を呼び出して取得(修正前)
    fixed_task = await get_task_detail(db=db,task_id=task_id)
    if fixed_task:
        #タイトル、内容、更新時間を変更
        fixed_task.title = task.title
        fixed_task.content = task.content
        fixed_task.update_at = datetime.now()
        await db.commit()
        await db.refresh(fixed_task)
    return fixed_task

#タスク削除
async def delete_task(db:AsyncSession,task_id:int) -> Task | None:
    task = await get_task_detail(db=db,task_id=task_id)
    if task:
        await db.delete(task)
        await db.commit()
    return task