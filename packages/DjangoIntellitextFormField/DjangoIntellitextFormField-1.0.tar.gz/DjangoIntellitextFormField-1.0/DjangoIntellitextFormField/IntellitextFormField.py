from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms import Form, ModelForm, CharField, widgets
from typing import Dict
from django.db.models.query import QuerySet
import logging

logger = logging.getLogger(__name__)


class IntellitextBaseForm(Form):
    """For use with non ModelForm form classes and acts as a base class for IntellitextModelForm."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'intellitext_fields' in kwargs:
            if isinstance(kwargs['intellitext_fields'], dict) and len(kwargs['intellitext_fields']) > 0:
                self.intellitext_fields: dict = self._validate_intellitext_dict(kwargs['intellitext_fields'])
            else:
                raise AttributeError("intellitext_fields attribute cannot be None or empty, and must be a dictionary.")
        else:
            self.intellitext_fields: dict or None = None

        self._CheckSubclass(cls=self)

    def _CheckSubclass(self, cls):
        if not issubclass(cls.__class__, (IntellitextBaseForm, IntellitextModelForm)):
            if self.intellitext_fields:
                return self.intellitext_fields
            else:
                raise AttributeError("intellitext_fields attribute cannot be None or empty, and must be a dictionary.")

    @staticmethod
    def _validate_intellitext_dict(candidates: dict):
        for x in candidates.keys():
            if 'list' in candidates[x].keys():
                pass
            else:
                raise AttributeError(f'intellitext_fields must be a dictionary of dicts with the "list" key.'
                                     f' This Error stems from {x}')
        return candidates

    def _update_intellitext_attrs(self):
        """This updates the attributes (specifically the list attr)
         for each intellitext field that is currently in self.fields.
         It should be added to the __init__ method of any form subclasses."""
        for f in self.fields:
            if f in self.intellitext_fields.keys():
                self.fields[f].widget.attrs.update(self.intellitext_fields[f].items())

    def _process_raw(self, intf: str, model_name: str, data: dict, raw) -> Dict[str, int]:
        """
        Responsible for re-keying data and translating FKs where appropriate.
        Can and should be overridden in any new subclasses.

        Parameters:
        - intf (str): IntellitextField (name).
        - model_name (str): Name of the model being processed.
        - data (dict): Dictionary containing data to be processed.
        - raw: Raw data value to be processed.

        Returns:
        Dict[str, int]: Processed data dictionary with keys and corresponding primary key integers.

        Raises:
        Exception: Any unexpected error encountered during processing.

        Note:
        - This method is responsible for re-keying data and translating foreign keys (FKs) where applicable.
        - It can be overridden in new subclasses to customize processing behavior.


        Example:
            elif 'AccountSearch' == intf and model_name != 'Accounts':
                name = raw.split('-')[0].strip()
                # THE SPACES ARE IMPORTANT SO THAT -000 isn't seen as the last - in the string
                acc_num = raw.split(' - ')[-1].strip()
                data.update({'Account_id': Accounts.objects.all().get(NameOnAccount=name,
                                                                      AccountNumber=acc_num).pk})
            return data
        """
        raise NotImplementedError("_process_raw must be overwritten in a subclass first.")

    def _intellitext_to_form(self, model_name=None):
        """Updates the form with the appropriate form values based on the intellitext info given.
        If there is none, then the data is passed back as is."""
        data = None
        try:
            data = self.cleaned_data
            for intf in self.intellitext_fields:
                if intf in self.fields:
                    # raw value of the field
                    raw = self.data.get(intf)
                    # self._process_raw is responsible for re-keying data and translating FKs where appropriate
                    data = self._process_raw(intf, model_name, data, raw)
                    # remove the Intellitext dummy field
                    data.pop(intf)
            return data
        except Exception as e:
            self.add_error(None, e)
            return data

    def clean(self):
        data = self._intellitext_to_form()
        # noinspection PyAttributeOutsideInit
        self.cleaned_data = {**self.cleaned_data, **data}

        return self.cleaned_data


class IntellitextModelForm(IntellitextBaseForm, ModelForm):
    """ subclasses IntellitextBaseForm to get all the Intellitext stuff,
    but also subclasses ModelForm so that its Meta etc. is present."""

    def _check_for_model_uniqueness(self):
        try:
            if self._meta.model.objects.filter(**self.cleaned_data):
                raise ValidationError(f"A {self.instance._meta.object_name} with that data already exists!")
            else:
                pass
        except ValidationError as e:
            self.add_error(None, e)

    def clean(self):
        data = self._intellitext_to_form(model_name=self.instance._meta.object_name)
        # noinspection PyAttributeOutsideInit
        self.cleaned_data = {**self.cleaned_data, **data}

        return self.cleaned_data

    def save(self, commit=True):
        # this if block is ripped right from ModelForm.save()
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate."
                % (
                    self.instance._meta.object_name,
                    "created" if self.instance._state.adding else "changed",
                )
            )

        try:
            # added the if commit logic so that save.commit could be false for M2M instances
            if commit:
                # create a new instance and save it
                # noinspection PyProtectedMember
                if self.instance._state.adding:  # adding = creating new
                    # create a new instance with the cleaned data
                    self.instance = self.instance._meta.model(**self.cleaned_data)
                # if the instance is not a new instance
                # set pk_to_use = self.instance.pk so that it can be used with the new instance
                # populate a new instance with the existing data,
                # then set the new instances PK equal to the old instances PK
                else:
                    logger.info(f"updating record with PK = {self.instance.pk}")
                    pk_to_use = self.instance.pk
                    # create a new instance with the cleaned data
                    self.instance = self.instance._meta.model(**self.cleaned_data)
                    self.instance.pk = pk_to_use
                    logger.info(f"updated successfully.")
            if commit:
                self.instance.save()
                self._save_m2m()
            else:
                self.save_m2m = self._save_m2m
        except IntegrityError as e:
            self.add_error(None, e)

        return self.instance


class IntellitextField(CharField):
    """
    subclasses CharField and overrides widget_attrs()
    function so the attributes are automatically added,
    except 'list' which can be added through the IntellitextBaseForm._update_intellitext_attrs() method
    """

    def __init__(self, *args, **kwargs):
        self.widget = widgets.TextInput
        super().__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs.update(
            {'type': "text",
             'Placeholder': "Please Enter a value",
             'class': "form-control",
             'style': "width:200px;text-align:center"}
        )
        return attrs


def get_intellitext_choices() -> Dict[str, QuerySet]:
    """
    should be used to return a dictionary of QuerySet's
    which can then be referenced in other parts of the code
    (ie views/intellitext html stubs).
    :return:
    :rtype:
    """
    raise NotImplementedError("used here as a stub, needs to be reimplemented to be used")
