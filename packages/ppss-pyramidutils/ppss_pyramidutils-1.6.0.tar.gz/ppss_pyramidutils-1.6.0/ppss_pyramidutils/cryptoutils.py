from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
import json

import logging
l = logging.getLogger(__name__)

from .jsonutils import jsonwalker


class CASTTABLE:
    __code2type = {0: str, 1: int, 2: float}

    __type2code = {
        int: 1,
        float: 2,
    }

    @staticmethod
    def gettype(code):
        return CASTTABLE.__code2type.get(int(code), str)

    @staticmethod
    def getcode(datatype):
        code = CASTTABLE.__type2code.get(datatype, None)
        if code is None:
            return ""
        return str(code).rjust(2, "0")

    # def getencoded(value,encrypted):
    #     code = CASTTABLE.getcode(value)
    #     if code:
    #         return "$".join([code,encrypted])

    # def getdecoded(value):
    #     parts = "$".split(value)
    #     if len(parts)==2:
    #         casttype = CASTTABLE.get(int(parts[0] ),str)
    #     decrypted_value = casttype(self.engine.decrypt(parts[-1]))
    #     return decrypted_value


class CryptUtil:
    def __init__(
        self,
        key=None,
        engine=None,
        padding=None,
    ) -> None:
        self._key = key
        if not engine:
            engine = AesEngine
        self.engine = engine()
        if isinstance(self.engine, AesEngine):
            self.engine._set_padding_mechanism(padding)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    def _update_key(self):
        key = self._key() if callable(self._key) else self._key
        self.engine._update_key(key)

    def encryptval(self, value: any,preformat = None,postformat = None) -> str:
        """
        try to encrypt the value, regardless of what it is. Adds a CODE$ at the beginning if a number type is recognised to allow cast back
        """
        try:
            self._update_key()
            v = self.engine.encrypt(value if preformat is None else preformat(value))
            if code := CASTTABLE.getcode(type(value)):
                v = code + "$" + v
            l.info(f"{value} becomes {v} with code {code}")
            return v if postformat is None else postformat(v)

        except Exception as e:
            l.exception(f"******************exception while processing {value}:\n{e}")

    def decryptval(self, value) -> any:
        """
        Stringify value, try to get 'CODE$' part, decrypt the rest of the string and cast it according to CODE, if present
        """
        self._update_key()
        parts = str(value).split(
            "$"
        )  # value should already be a str, but plain uncrypted object may be other things
        casttype = None
        if len(parts) == 2:
            casttype = CASTTABLE.gettype(int(parts[0]))
        try:
            decrypted_value = self.engine.decrypt(parts[-1])
        except Exception as e:
            # can't decrypt, it was a old plain value
            l.debug("can't decrypt, sending back the plain value")
            return value

        if casttype:
            decrypted_value = casttype(decrypted_value)
        return decrypted_value

    def encryptRecursive(self, value: any, preformat = None, postformat = None ) -> str:
        """
        Recursively walk through value and crypt elemets separately and json dump it to string
        """        
        self._update_key()
        l.info("CryptUtil.encrypt()")
        w = jsonwalker(lambda val: self.encryptval(val,preformat,postformat))
        newstruct = json.dumps(w.walk(value))
        l.info(f"encrypted in {newstruct}")
        return newstruct

    def decryptRecursive(self, value):
        """
        JSON parse Value and recursively walk through it and decrypt elemets separately
        """ 
        w = jsonwalker(self.decryptval)
        try:
            val = json.loads(value)
        except Exception:
            val = {}
        newstruct = w.walk(val)
        l.info("CryptUtil.decrypt()")
        return newstruct