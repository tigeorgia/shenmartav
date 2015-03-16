"""
Resources smsregister
"""
__docformat__ = 'epytext en'

from apps.smsregister.models import SMSRegister
from .common import CommonModelResource
from Crypto.Cipher import DES3
from settings import SMS_API_KEY
import binascii
import json



class SMSRegisterResource (CommonModelResource):
    class Meta:
        queryset = SMSRegister.objects.all()

    def obj_create(self, bundle, **kwargs):
        test = super(SMSRegisterResource, self).obj_create(bundle, user=bundle.request.user)
        print test
        return test

    def dehydrate(self, bundle):
        encrypted = self.encrypt(json.dumps(bundle.data))
        print encrypted

        return encrypted


    def encrypt(self, raw_string):
        keyText = SMS_API_KEY
        encryptor = DES3.new( keyText, DES3.MODE_CFB, '00000000')
        encrypted_string = encryptor.encrypt(raw_string)
        return binascii.b2a_base64(encrypted_string)

    def alter_list_data_to_serialize(self, request, data):
        return data['objects']
