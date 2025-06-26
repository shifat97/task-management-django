from django import forms
from tasks.models import Task

class StyledFormMixin:
    DEFAULT_CLASSES = "border border-gray-300 w-full rounded-md shadow-sm focus:border-rose-300 outline-none p-4"

    def apply_style_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    "class": self.DEFAULT_CLASSES,
                    "placeholder": f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": f"{self.DEFAULT_CLASSES}",
                    "placeholder": f"Enter {field.label.lower()}",
                    "rows": 5,
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "p-2 rounded-md mt-2 mb-2",
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": ""
                })


class TaskModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        # To use all fields of Task
        # fields= '__all__'

        fields = ["title", "description", "due_date", "assigned_to"]
        widgets = {
            "due_date": forms.SelectDateWidget,
            "assigned_to": forms.CheckboxSelectMultiple
        }

        # widgets = {
        #     "title": forms.TextInput(attrs={
        #         "class": "border border-gray-300 w-full rounded-md shadow-sm focus:border-rose-300 outline-none p-4",
        #         "placeholder": "Enter the title",
        #         "type": "text"
        #     }),
        #     "description": forms.Textarea(attrs={
        #         "class": "border border-gray-300 w-full rounded-md shadow-sm focus:border-rose-300 outline-none p-4",
        #         "placeholder": "Enter description",
        #         "type": "text"
        #     }),
        #     "due_date": forms.SelectDateWidget(attrs={
        #         "class": "p-2 rounded-md mt-2 mb-2"
        #     }),
        #     "assigned_to": forms.CheckboxSelectMultiple,
        # }

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.apply_style_widgets()