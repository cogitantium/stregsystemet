valid_images = ['.jpg', '.png', '.jpeg']
valid_mov = ['.mp4', '.webm']


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = valid_images + valid_mov
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Hør her kammaerrat, den fil du har valgt er ikke understøttet! Valide fil efternavne er: {valid_extensions}' )
