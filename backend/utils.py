def get_filename(filename, request):
    # Override CKEDITOR filename generation
    return f"CKEDITOR_{filename}"
