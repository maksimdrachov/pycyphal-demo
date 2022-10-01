# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/node/Health.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.659980 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.Health
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Health_1_0:
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
    NOMINAL:  int = 0
    ADVISORY: int = 1
    CAUTION:  int = 2
    WARNING:  int = 3

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.node.Health.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint2 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint2 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 3:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 3]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 3), 0), 2)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.node.Health.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Health_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(2)
        self = Health_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.node.Health.1.0'
        assert isinstance(self, Health_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.Health.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{@j&Yi}Gi6y1a-*=}j8lByCQs4D?VD4ETJhg3dog91^KO~|7>BxHHUp0%mR9@(CKAR*BYAVsnSQp|7QZ*sklWRo_a'
        'Mq0(Yw(mXX+<T9IyYctO_1f^yKP(5-Qkh`Oj383{LQ=^Roav&}RyY>??IUNZ%vFXR4@wr!!t#soYgqDgSdjwu->OJABPvmvvg8{^'
        'q~pQYahDk@v<kfD7oLsRXJKb%r}js95&SJooHHV=9JApk2zL#T^HagkZ3!mn1%L*o#1ZTws_U+oMijz{E}U3AQC4&mqua`{4l|e8'
        '+`_4FSTfZC_&c)@JR{cO0!RgZ-#<8*1d7*^P1xIuTfnIHdpHdKKDLf1N(`M2bXui+&d+s;tN_6cOm!A~Ex@mLe0@`^c*mWC;EVjh'
        'c=h(qEPsc;&mWE=EVTFcw%e`Uz#sY5W6sd9K8h)aghhF!G6(t!)j_4vB{On>mXt1pB62wiejbkzyf;ya^-IHSEXpN~>W3r-B65O>'
        'KlV3sLx$lk>~D?Nu<vJ9L!@p~fcU}xF{rn`dbWMEfA~YB@J|b622y53qLLVBBgYKtMLN2IPmT;x9fq_)?h;w1GF?IW45Nr3;0Gsi'
        'A|x~?oFooW%`8&dfex$-HyZK2tx`L%juj|3x<H^$u1yiuB5Dw`31^Xk&Rub$VCQn$1nBc*tOMWhGi$Fwcww`3a=g9Yj(oev|HXp*'
        'JjDWfD3){zqfl^&vW_7X&c}v~x`0kr#N`M*Wux9kGS-s38vgq0!2hmw*xqh`9pV3Y8NRLZe2hJZ0hGW%PBfd~uT-2r<n)Be5TyXp'
        'Dzcaye+lBoIYj0crz`@egOS}tsEFU=%lt$BCI5nN@u&P-zE{BjQwBxPh+{OI`a3umeMWJqjl+V5w!eq1u1v;YLo!^FXj2REpA>2E'
        'HxIz>`UmmXGq8i1Ciu+>cnLK9?SeeFqM*?FTzBDnImiYjhjyW?(80f3R;d&jHmp<0nEt|-;P(8;9%1^UK?Z+!WRb~QvYNzM3@+No'
        'BId*bC<6jV3+sxEg;W0Mdofe1wNmTi+)dSh4}*Z9QQKj;6SSQVrzNJDsBTeFNheAuMV#9%%pA<e5|~66nrCWPG1t@PIU1+7%bzr2'
        '!NzI8rd(x_<+_p-CMA~)&<saww4+C<A%t}+)AKb-8r|q}g5{*KrKQw8`=o&ocdoQgn$2FXmq^k}GHn!-GGVl8X1QrP)_2XdPn+u-'
        '$=b&H`js0wAxTGfn_#Y00pje6)DSah7K{qgY|*Z;+6?ffFd5XxG+Uc^{j*`9m9?a#Iba&~?&r~>Qwc@;XyTI>UJg}pSHB1U=2PKz'
        'hu@Fbxsm%fur7l~*9EbIBGu3_Q1(6OAb6`{`hC!iIBhQ8q<Nfi0WTi6{_X*x6cl~w5bwv`b|rz?;OZ`a{AXC&nf=SA@F16?2w|sQ'
        'rN9&F1IxG|{kT|&Zyo3p@i*f8K-BQfZi9KkI41uBR9i+cH3$Fz'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)