from app.extensions import db
from app.models import Task

class TaskService:
    @staticmethod
    def create_task(user_id, title, description = None):
        task = Task(
            user_id=user_id,
            title=title,
            description=description
        )
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def get_tasks(user_id):
        return Task.query.filter_by(user_id = user_id).all()
    
    @staticmethod
    def get_task_by_id(task_id, user_id):
        return Task.query.filter_by(id = task_id, user_id = user_id).first()
    
    @staticmethod
    def update_task(task_id, user_id, data):
        task = TaskService.get_task_by_id(task_id,user_id)

        if not task:
            return None
        
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)

        db.session.commit()
        return task
    
    @staticmethod
    def delete_task(task_id, user_id):
        task = TaskService.get_task_by_id(task_id, user_id)

        if not task:
            return None
        
        db.session.delete(task)
        db.session.commit()
        return True