import uuid
from datetime import datetime

def user_directory_path(instance, filename): 
    current_datetime = datetime.now().strftime("%Y%m%d")
    now = datetime.now()

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return '{0}/{1}/{2}/{3}'.format( now.strftime('%Y'), now.strftime('%b'), now.strftime('%d'), f'{str(current_datetime)}-{uuid.uuid3(uuid.NAMESPACE_DNS, instance.created_by.get_email_address())}-{filename}')