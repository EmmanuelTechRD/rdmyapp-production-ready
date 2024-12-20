import uuid

def media_upload_location(instance, filename):
    extension = str(filename).split('.', 1)
    
    return f'blog/{uuid.uuid4()}.{extension[1]}'