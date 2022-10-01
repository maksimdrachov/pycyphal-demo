# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/can/RTR.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.135079 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.RTR
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.metatransport.can


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class RTR_0_1:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 arbitration_id: None | uavcan.metatransport.can.ArbitrationID_0_1 = None) -> None:
        """
        uavcan.metatransport.can.RTR.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param arbitration_id: uavcan.metatransport.can.ArbitrationID.0.1 arbitration_id
        """
        self._arbitration_id: uavcan.metatransport.can.ArbitrationID_0_1

        if arbitration_id is None:
            self.arbitration_id = uavcan.metatransport.can.ArbitrationID_0_1()
        elif isinstance(arbitration_id, uavcan.metatransport.can.ArbitrationID_0_1):
            self.arbitration_id = arbitration_id
        else:
            raise ValueError(f'arbitration_id: expected uavcan.metatransport.can.ArbitrationID_0_1 '
                             f'got {type(arbitration_id).__name__}')

    @property
    def arbitration_id(self) -> uavcan.metatransport.can.ArbitrationID_0_1:
        """
        uavcan.metatransport.can.ArbitrationID.0.1 arbitration_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._arbitration_id

    @arbitration_id.setter
    def arbitration_id(self, x: uavcan.metatransport.can.ArbitrationID_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.ArbitrationID_0_1):
            self._arbitration_id = x
        else:
            raise ValueError(f'arbitration_id: expected uavcan.metatransport.can.ArbitrationID_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.arbitration_id._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 40, \
            'Bad serialization of uavcan.metatransport.can.RTR.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> RTR_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "arbitration_id"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.metatransport.can.ArbitrationID_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = RTR_0_1(
            arbitration_id=_f0_)
        _des_.pad_to_alignment(8)
        assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 40, \
            'Bad deserialization of uavcan.metatransport.can.RTR.0.1'
        assert isinstance(self, RTR_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'arbitration_id=%s' % self.arbitration_id,
        ])
        return f'uavcan.metatransport.can.RTR.0.1({_o_0_})'

    _EXTENT_BYTES_ = 5

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{`urU2h!K8OQhi#a`P<Ok5iBz|%GjCxk3<l2Ryzk_1B1C2pEG0U{dB?i~A!yKl_Qx^^X`a?vW0M#562Qn=)z61TnM'
        'Bk&F2s@L=zaLF^f{}Zp*c0k;ABPIW{^K$mg%=!K1nc4ik@UNv4nc<)Kx&D?HdhNOs>cDr~{@>hYTi2aduhZ{^ex#Fl?p72GTG1fT'
        'x3~H_d6=B~B>6Z|anb3z9a(>T;BK_sZoQ);HwxTt*zW~VJzaA1_RS=&I2$?${a!aQnYerx?T1Mt)5!ia`6P*F9XE;szd49>nA}Sa'
        '8qwp8lDK%q*KKcSBr}fZMy?a3!;>$m-s#F$>>8{o#wQOP=Eb1t%aTZTy7pFL%BE_^W@`6j-$UqQ(c~WY_QHX^U2;SHqkBB)VEcjJ'
        '@gsjj4tDWQH}u!K+Pl_`^qLNKUxZmlzR79p?pkD$#;lx*mK#P+r{~G3I2kY9upOnl)i2As>**>v{n>vca&?|^!pQA<Zs3h~^kC4G'
        'V=QjC?SYJ-;CQ`O5@!-wIv>|=xSr>C*LGh6Ih14jAIe70_hc5_l^7qoIo&uK%D0#c=DfKuXzF-zY#unxt<mg~4bPbqp&X~D`+;t`'
        'k@k`Y@w~I@Z)(p;&$=W1uf&I)ur~-=T2{2R(|6@4;&K{oznR3<8#0+UZ=_2f%2~_4B$Mclj5Cz!-EsdC`W-KDTc)=mpZi;_t-f*F'
        'XFT2MCGj);L9^|*oItM)+UeKtOg7oOG@1u#H{&xQiSxsy$M(#I`q}z&Jv~oJl%D@Z$GD*kH_+WEJ#ia;OD7M^`S{54@)_BUeNWc-'
        'tG*8E>6K`<<x5Z6Gre=kWZ!7=a}w7s`O&+>&$r|w&U~DAdi^BkgE|SfI?bLOu?+6IoB_Fx>B#@o*K!EGU}x%;oR;xr3YZV#1<Z*('
        '8yUxZ__*~!eDrd!n_j~1zFo%EQIB#il9ZC2J>9WB7FGuBwi|5i*}LS7=If`4YRqnjO)*b@G%T6ygQlFkj^9lgk%qgOHp(d{a#7R1'
        '8`*Tf%yuJ}W_G)gPcygOD5RO+ZWOV+lxA_eQBJe4-Kb!F72D5XyIJ&C8;z$ihnz<)AP*rABaa{#kxwCyBA1XqLq3iCIr13t8RT&!'
        'A)iG)hh*e0kiSI!3V8zgYvf7f^GJm}g?s^d8u=pf46=@V33(Q|j68=tkGz2V4f18=Z;`JcUq${7`5N-~$k&l?Apd}T6L}T+9?~E;'
        'k@u00kY6CbM1F<*2Kg=WyHQ@RWYKuqHk56=VjEX&<2~Cjwy|j&_if{mZG2%HU)si3w(*T^d}|xup)rtKh2HFouhQEwmNm^sBRNOu'
        'f};YF7DxZJ!DdtbZtcM&Gl5A4nB;&-ZUU1GFew6)959&yCKX^(0wx7uk^?3gV6p&A=7Gr^FsV&oG6PJiz@!39%D|)qOp3sy08H}0'
        'BnM2gz$61q7??0HVPL|*gn<bI69y&>Oc<CjFkxWAz=VMb0}}=&3``i9Ffd_Y!oY-q2?G-bCJam%m@qJ5V8XzJfe8Z>1||$l7??0H'
        'VPL|*gn<bI69y&>Oc<CjFkxWA78ACZu*HNeCTuZbiwRpy*kZyK6SkPJ#e^*;Y%yVr30q9qV#3=4^EDbxv(cywrZh}xn9?9Lgw5eI'
        'LZK-IZZaz2_kB>RANZj3_NEkqp7wtH<Cj9~bc4)`=B!!X^_+r1y!?3c*X)Bve%FJBdE?_`{omP4X8m*dCp2$9Fc(+MCG)m2SIj%+'
        's<~$VXd32Sb3J}`-!bkk;mx0i<@&i-_mu1Ambp6`!u$KyvOCMxMw_i4RP~PEl}YZ(qN40jMI<VseN;4Azh<GL!bJU=g^G$3^=lO>'
        'Dnms@s3;E=Wuc;ZsAvu<s!i0dGf+_#Dyl$5WvHkG6&0bP0#uZTigHj<7And>MFbTQR76k_K}7@=5mZD_5kW-+6%kZKP!T~z1Qiif'
        'L{JeyMFbTQR76k_K}7@=5mZD_5kW-+6%kZKP!T~z1QiifL{JeyMFbTQR76k_K}7@=5mZD_5kW-+6%kZKP!T~z1QiifL{>#)RYX=r'
        'WK~2~MPyY(Rz+l0L{>#)RYX=rWK~2~MPyY(Rz+l0L{>#KS+wS-MeFo7J-tm&i`FR(QyLB^S}Pi5T{2b@s`W=w4w~cZ|IJBh_?ff^'
        'Pbv+Uey}7we)-}GuLf>Mv%9k`ucq(K>q)%eMDCh1{DfaFcFNnzsJy)|qy0%W<oFG-lGcmkFJb3~KaWhlJ{|3NZ~Z@V;M4o()EHA^'
        '42>~DK?w@#2`FSIP{;s<0#GPUpilq`nTf}&0#L{Tg&I(p0SXnMPyz}CppXL!8KAHT6pjFe!$9E>P*?y8^FUz^DAXo?CYS*VRiID-'
        '3T2>B0t!W-Pyh;fppXL!S)h;s3JNGFprC+)0tyN!D4?K#f&vN(C@7$yfPw-F3MeR`pn!q`3JNGFprC+)0tyN!D4?K#f&vN(C@7$y'
        'fPw-F3MeR`pn!q`3JNGFprC+)vM4Bvg0d(mi-NK!D2sx!C@719vM4Bvg0d(mi-NK!D2sx!C@719vM8wWQgTYel!pI%8c<5kkCk@m'
        'e?%A+l<x2y<5EHD$-_^4!C1R_`{sVN<Lj5(ZW#J44s@p%X&$~g?f7B(W1TGfXrRN0Rks(hr&s;1_IR}ya9VI)dF#{<zIj~#pOm<J'
        'aW-GCjE<}RJ*XfQnIR+q00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
