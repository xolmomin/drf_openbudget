import requests
from celery import shared_task

BOT_API = 'https://api.telegram.org/bot5344490283:AAF2-eAVHwVCevHdAyR4V_VKZVPcDhYB5go/sendMessage'
GROUP_ID = -620660762


@shared_task
def notify_telegram_group():
    data = {
        'chat_id': GROUP_ID,
        'text': 'Gruppaga xabar yuborildi by Celery'
    }
    response = requests.post(BOT_API, data)
    print(response.status_code, response.json())


'''
celery -A root worker -l info
celery -A root flower --port=5566


celery beat


task
redis, celery-beat

'''
