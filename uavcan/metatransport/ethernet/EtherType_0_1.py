# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/ethernet/EtherType.0.1.dsdl
#
# Generated at:  2022-10-01 11:53:15.964508 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.ethernet.EtherType
# Version:       0.1
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
class EtherType_0_1:
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
    IP_V4: int = 2048
    ARP:   int = 2054
    IP_V6: int = 34525

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.metatransport.ethernet.EtherType.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.value, 65535), 0))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.metatransport.ethernet.EtherType.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> EtherType_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u16()
        self = EtherType_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.metatransport.ethernet.EtherType.0.1'
        assert isinstance(self, EtherType_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.metatransport.ethernet.EtherType.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8D=Ii+0{@j%UvCsQ5Dy}kgivT`5K@aMrYaO7v88E(5Km3hAVpWwQv$pp%e$VtvGA@}w)d2+RH-~r70FVO;(maBfPTl0FMF4i'
        'HmbTWJN9^f^Y1tF^Zf6B^yVgCxLLQ-Nu6;ARtc?s6uE|s7pAO@QyyZtbl`1M_{PGswuX2V@4b#c#k--$D^ZgEi$;tKQDr4~;jO4#'
        'ZLH70BiIUjwv&X3Wmw{4uuhpO;#^pK(aA@#Ki5C^OMD%}MJ~LzDsMcv_>z2_5#8)n4811`v^<GwnM>gX_Y;R_nAcX7%BwNGSbbhO'
        'HL5`FRvt!Opfj+GJXfA;s74-Re}%vc;XE&mgoszewZRl9nPuCgdzw@!qc?FshO69pQAuItX`o-59DAWR7P_Gb=D9RQ40DlgFNdXV'
        'QzaWe3j$a1S|@$nU%^lCQ@q(B><;*gjfl7Kv#`KBxEs@y;jp&gQicDP@Y25UbSL!G0j`A$Lo14O>q!5klSv=u*B@*=iYXPBlgrQl'
        'E28sT`-4e5xQ6#TbX-p`n;ZWFW|G*$e*x-!y|KBzIYWZ5dWtYSZ;u(75E)*<dw3fk<3s!oziFtI5~v`B@F3&caG4L)AxNIM%9V_J'
        ';R<)Au?3Jq1Fr=&DlDd-R(T8;1~d(agLHdD#5ngQG4DCCiYj)g6tA2rCDjehn9g-uv^5HSUqWeOxL!B8Rt2{(YIJgc!cekaIG&ya'
        'b9#QL5z`5Z;iK6MWe>8ivee(`6TenD3P-V8sC?r1SQQZ8;;r!KLB~5bGi61`EXRan5{8Oc&+?Y-?(FQaeHbZ6-c#q<R^!oF<y%G|'
        'Y<FvKD_ees$}vrE82wG9Nyl6%v}Uf!9e8Gjr#yHRo>5qnD<#2_D{oj1%z}n7y<tOR+4iJPSsH>|Q!(yL$$K&_l$L-09K#3SD*yfD'
        'd;qgi3Fo<~V_;{2xVFp<b%N^llsZG(AZ7bQ4V1RACsV(`3skgIa2P%u2q{%H`o|-Dm9%?}*21>$YjN$jc(=du&gHc7>SKi1Uuts7'
        'vs6{uBqWH#BrK+FLcB=vFQ=g;0;K8NqpA|cv%diAMh$<g1poj'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
