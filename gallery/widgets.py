from django.forms.widgets import FileInput


class FileMultiInput(FileInput):

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['multiple'] = 'multiple'
        super(FileMultiInput, self).__init__(attrs)

    def value_from_datadict(self, data, files, name):
        if not hasattr(files, 'getlist'):
            return []
        return files.getlist(name)
