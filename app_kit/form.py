#coding: utf-8
__author__ = 'moon'
from django import \
    forms
from django.core.validators import\
    RegexValidator
from django.utils.translation import \
    ugettext as _


from django_summernote.widgets import \
    SummernoteWidget, \
    SummernoteInplaceWidget
from django_summernote import \
    fields as summer_fields

from app_kit.models import \
    Kit_Post,\
    Kit_Detailm,\
    Kit_Photo

# Create your models here.
Numeric = RegexValidator(
    r'^[0-9]$', message = _(u'숫자만 입력해주세요')
)

Tel_Numeric = RegexValidator(
    r'^[0-9]{8,16}$', message = _(u'지역번호를 포함해서 숫자만 입력해주세요.')
)

CATEGORY_SELECT =((1,'for Baby'),
                  (2,'for Home'),
                  (3, 'for Funny'),
                  (4, 'for Art'),
                  (5, 'for Fashion'),
                  (6,'for Tast'),
                  (7, 'for Beauty'),)

class KitCreateForm(forms.ModelForm):

    category_error= {'required':_(u"카테고리를 한개이상 선택해주세요"), }
    title_error= {'required':_(u"제목을 입력해주세요"), }
    price_error= {'required':_(u"가격 입력해주세요,"),
                  'invalid':_(u"숫자만 입력해주세요")}
    describe_error= {'required':_(u"제품 특징을 입해주세요."),
                     'max_length':_(u"500자 이하로 입력해주세요"),}
    contact_tel_error= {'required':_(u"연락처를 입력해주세요"),
                        'invalid':_(u"숫자만 입력해주세요")}
    address_error= {'required':_(u"판매처 주소를 입력해주세요"), }


    category = forms.MultipleChoiceField(required=True,
                                         widget=forms.CheckboxSelectMultiple,
                                         choices=CATEGORY_SELECT,
                                         error_messages=category_error)
    title = forms.CharField(error_messages=title_error)
    price = forms.IntegerField(error_messages=price_error,)
    describe = forms.CharField(max_length=500, error_messages=describe_error,)
    contact_tel = forms.IntegerField(error_messages=contact_tel_error)
    address = forms.CharField(error_messages=address_error)

    class Meta:
        model = Kit_Post
        fields = ('category', 'title','price','describe','contact_tel', 'address',)


class KitPicCreateForm(forms.ModelForm):

    photo_error ={'required':u"한개 이상의 사진을 입력해 주세요",
                  'invalid':u'',
    }

    class_photo = forms.DateField(error_messages=photo_error)

    class Meta :
        model = Kit_Photo
        fields = ('class_photo',)

class KitDetailForm(forms.ModelForm):

    kit_detail_error={'required':_(u"상세한 정보를 입력해주세요"),}

    kit_detail = summer_fields.SummernoteTextFormField(error_messages=kit_detail_error,
                                                        label='')

    class Meta :
        model = Kit_Detailm
        fields=('kit_detail',)
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }