from datetime import datetime

def session_stats(request):
    login_time = request.session.get('login_time')
    duration = None
    
    if login_time:
        # Перетворюємо рядок назад у об'єкт datetime
        login_dt = datetime.fromisoformat(login_time)
        delta = datetime.now() - login_dt
        
        # Рахуємо хвилини
        minutes = delta.total_seconds() // 60
        duration = int(minutes)
        
    return {
        'login_time_dt': login_dt if login_time else None,
        'session_duration': duration
    }
