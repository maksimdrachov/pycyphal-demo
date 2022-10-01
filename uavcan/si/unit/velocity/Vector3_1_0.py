# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/velocity/Vector3.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.307521 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.velocity.Vector3
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
class Vector3_1_0:
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
                 meter_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.unit.velocity.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter_per_second: saturated float32[3] meter_per_second
        """
        self._meter_per_second: _NDArray_[_np_.float32]

        if meter_per_second is None:
            self.meter_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter_per_second, _np_.ndarray) and meter_per_second.dtype == _np_.float32 and meter_per_second.ndim == 1 and meter_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter_per_second = meter_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter_per_second = _np_.array(meter_per_second, _np_.float32).flatten()
                if not meter_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter_per_second: invalid array length: not {meter_per_second.size} == 3')
                self._meter_per_second = meter_per_second
            assert isinstance(self._meter_per_second, _np_.ndarray)
            assert self._meter_per_second.dtype == _np_.float32  # type: ignore
            assert self._meter_per_second.ndim == 1
            assert len(self._meter_per_second) == 3

    @property
    def meter_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second

    @meter_per_second.setter
    def meter_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter_per_second: invalid array length: not {x.size} == 3')
            self._meter_per_second = x
        assert isinstance(self._meter_per_second, _np_.ndarray)
        assert self._meter_per_second.dtype == _np_.float32  # type: ignore
        assert self._meter_per_second.ndim == 1
        assert len(self._meter_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.meter_per_second) == 3, 'self.meter_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter_per_second)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.velocity.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter_per_second"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            meter_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.velocity.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter_per_second=%s' % _np_.array2string(self.meter_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.unit.velocity.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YXTTc@~6fSoVQ4r&UKERXWgDa&i6yMaOnk>`?ls7ZX?hMR?*-K_-8`gwG9yF3nA_>Qz<A3uEEf&yj((KHh+jqY2'
        'oPHhu^?ST>`M9OLWQM7L7_KE%@(Ya=4@jIPd1j>L;O2I%E@E3~{;|wCT)^{FIDr*6K~kEaeW{?`n5Kb|L6J%ubh*l6Y0F@b$2QY7'
        'aMPsAwUJp0qT;6Z`sWJ>N5aZ?I0ZLLsI^)~h2;i5!!S^Poxn}BBv)(z<_=-hQer(q_hd-8*0coouqBT<+v4e=6|eoLn{CYzu6V*z'
        '+fOzGORi-it?Z)5OiN|d-pn#fB58@bECS&&;)|)VB*_>D@z_1;T!s6v;4Rv=y$Ly~e1jbXNsOf_qnce$^aJxG^blDtm@j;wX>5^8'
        'gB-W|XUyTA)#|Hj&9z#6eZAIftTmgB&1SW_v0AS-YxQQmQC;6$Yt-wj;A<6;n?ZCr^`b#I=Eg~+Fyqs!#s>h91AF@p?(Q3DdvxyN'
        'wNHT?BUuh^c~}xtCQ+tj3~q6oCmGV}!GFlPrZ_YMA}2{KBq}W$?!gYvxt0I-8zo1GUA#iS`|Uz0s>|C>n5#=w!Qm&Ygv;k9!p_G@'
        'B2x(W{ed3)!;}}PP!t2g5${<!H%L1_&S`o%x9uYGp<=?#C){#PunhJTXDI_r!!qotf~-=vcx|jnRQC4e1jLqDFgPKM=bFdVat3Ga'
        '9y#!1N%BlvA{n&Z0x?;kV~z&JNlsCJH|1YSMyP!U*YmjJzg}SbBQJ3$KH-R>aB~SgGBRN}5F+d1Jul-j7gW7q$h2RNB0}bg=7-oP'
        'mLKd6Mo;$E8QiFm*pFXnoUW^-1~=bd>!2E}23}jReqa}gpaxNDzd4AbD`O64Vq3IDAgY)Ai@Mn8snwIILm89l;XhiUwTb^3dCv^t'
        'G?Lv4_r*K>y~i|RUxDBc9C7Z~$OHfY'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
