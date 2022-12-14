# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/can/Error.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.109423 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.Error
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
class Error_0_1:
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
    def __init__(self) -> None:
        """
        uavcan.metatransport.can.Error.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        """
        pass

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.skip_bits(32)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.metatransport.can.Error.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Error_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of ""
        _des_.skip_bits(32)
        self = Error_0_1(
                )
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.metatransport.can.Error.0.1'
        assert isinstance(self, Error_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
        ])
        return f'uavcan.metatransport.can.Error.0.1({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YWO=}cE5Z$mzHb#wzw*+)f5)Y1glYj>my{xW_F}X?8Jzd#p?3r%*W7!b|a}fd!3S0gH|ESfQ%?HuUrK`HSs$RWU'
        '^L_RApMG!gr3bc?Uh0y0aEfd7l?x3et4w2!R{=2H-VZKTAv*ZfS-?3yI>v9fo7Py%8;akLd|L6gY#{L9c<Zfkq0BdLoHGv72AhKO'
        '%CuPb(%^7u&vDoruKd7bOg9-1!6^{~c>IjlVLE?=>DHJ_soKd~1zKJ}+GLUk&O*kSw*OycYLp~Qhjd(?hd>Awn1*%|Y8)0`)N84S'
        'X_ZM+VZ9v%Pxmh2WTHEre~~J|I;eO6i6?1`9jO^emU&>*Y?SUYZ=$P!0ved*)FBP>p_RaNV@yoX#`$(mL##Z(w01zCJ#pXgFJ3j$'
        '@v1gc@@-djw&wb=gvManu~BGMF$a^VbNdSdD0}@>nOx?wHkkU0+pUE@<<s(6nTf)HACYFPxhIGY+K`!>stWL=-bn|qUyce9eE~VE'
        'aF9#w6`(>5uHbE<+CVuZE!Vm$CeVV*h?eh<9FbL!!3(K8ZIj?_1!X2!Xu|sNOsxwQsC~HVlk~4tc(?HP$vsoA&y2-XTvx<*jW9$M'
        '&G(*&qg}{AKiCYBR`h&<)>&06+Nk<@y0cude;(B@a&#26=B~RMr3zE7Bj8Wm9Tva5pzXJ(g>bkL1&!ONmi8+fe3p#?Ym6lIa`q;J'
        'nI)O>4>F3vizv#!4da4`t^)u7'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
