# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/scalar/Integer8.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:15.996169 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer8
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
class Integer8_1_0:
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
                 value: None | int | _np_.int8 = None) -> None:
        """
        uavcan.primitive.scalar.Integer8.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int8 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated int8 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.int8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -128 <= x <= 127:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-128, 127]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i8(max(min(self.value, 127), -128))
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.primitive.scalar.Integer8.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer8_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i8()
        self = Integer8_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.primitive.scalar.Integer8.1.0'
        assert isinstance(self, Integer8_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer8.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8D=Ii+0{?YWOKTKC5Z;h%5)&VU1TP+p9wZ(d_2$Wg0YTQRi&1aV^rPHv?3ro$vFr!|b5IO4D5U%s{z$8{Nj63@m+6}7dVG)h'
        'y7c?cV(;Y1cU`A~vK0&94Y%eC7Zxfe+uF6kM8JGwKl&tN^6;*6fXDdo5D#!C_gTYh%5Nt=k-Vv#H?@go0#%UQa$mh_B8<U5!@SBS'
        ';Dc!!)V;j&;q-irgM~rwJ04<QXFNu4M2ZmbBVM)D`6bN#mj<kwZ?nb}kDSG_;#KA68)DwrH{%A>>5BgXTW7*VW}z8Jje}KcEqREn'
        'ZWW;3%C|>nZAw|SOS!$0A~?No_!jdP3z0X9dv&qVk0f+I_b1#Yn!m(UD>3&l37$7Epl70+@p^!ITW<u~MuGDnc?5+=`6l~hrl6Q>'
        'ePl-AFmJHXCNF^!7MSBSE3cH7H3IXs5y?0mm9NKyZQ(Id_nv48By7z;2U9E0rEVt_yH0jabNfg^-D1AulCVZH594IZ_&LQ?y*!hh'
        'CS0I(c_uyadnSJMw0cq%F)$WxHksyumh{lXqRzxfz$1N6-zQ3hrM?f&w3~BB7vtp^^Ys@dzCMZfDLhp#FS6E=C$DM}x>~dZiZ<CJ'
        'kmQU=R(#{Y^Vs^i2bP)ChWw?U=UXGLlxfEQUDCTHJ4}`kcbBu&VJ7uY+!?I?3W9zDH)}+mN`m0lrYZKK1D}?|O0gI*U8>g@OdW4d'
        '{*z%6K_pTA1y1GK?Y9E}00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
