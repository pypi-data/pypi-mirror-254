from django import forms


class TrixRichText(forms.Textarea):
    template_name = 'trixeditor/widgets/trix.html'

    def __init__(self, attrs=None):
        default_attrs = {}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    class Media:
        js = ['widgets/js/trix.umd.min.js']
        css = {
            'all': ['widgets/css/trix.css'],
        }
