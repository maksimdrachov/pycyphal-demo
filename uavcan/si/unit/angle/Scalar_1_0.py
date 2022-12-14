# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/angle/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.302212 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.angle.Scalar
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
class Scalar_1_0:
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
                 radian: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.angle.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param radian: saturated float32 radian
        """
        self._radian: float

        self.radian = radian if radian is not None else 0.0  # type: ignore

    @property
    def radian(self) -> float:
        """
        saturated float32 radian
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian

    @radian.setter
    def radian(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian = x
        else:
            raise ValueError(f'radian: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.radian):
            if self.radian > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian)
        else:
            _ser_.add_aligned_f32(self.radian)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.angle.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "radian"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            radian=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.angle.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'radian=%s' % self.radian,
        ])
        return f'uavcan.si.unit.angle.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YWOHUL*5MJadh=f4Ac#xC8!Eqn6xLh^a%L;Bpy_rtUbhFd3=aGJFc1=j+ppm2#O(=h;|G?^9a1p~?rmCyz>-ws`'
        '{<84v_k3;g`6tzw8?GW|gqEP>XGoNYSX$;)X`~hC*H5f=sdZYs8&?7^asM38aL+HY0&<E!b}&q#h>VO}A#DW3fDlenP@vJTu%XaK'
        'mIY=tzx?6KzQo>Kul5bk(XTPER?Ea$Veli~)zIH0^ow076rVM+$~ahHHgtDad8K78tsGLu{jMs({>x>JCDJk_ih<3rw?mLA7|ZgK'
        '3(U6tqyBYyD2rZE>?nkYM(r!UMZe9Ag@S|TH-WwrP7VVaisRwpQw^yl`i92Ry|M|z@3!K4v(s$F2M4WAyV>cq4?B&<i+bGXwBk<O'
        'ZX6so+i_gSaF<K6MZcthODNDUFkYtUYjg~L>&7TqGM?_|471&A(-1{2DlJm5g5!mM$WG-*a8{MtGRg7SZ!%LloeByl!73mEemVS<'
        'OsM%j$zjwFr<XLax#zTp_cUYTvYx{yBXdrSvT{g%HBQG>2I?6Xc}W7PT%u&kv=}%QuAl9Ts+XqnL4VIk;u9o9&=V1%-<ZlMYDD!Y'
        'tQBpT_7=;)P={I+HtcyQQ-K%RUbav3NECrSy;i|&8<c2o`{*CMl=k(+KOy%@4}PAN75bgKK+HH#N@7Hv91%m(SlHy7N@%d9o~dey'
        'rI{q9W?jG02hL?N_%A8zh3K(UM00#QN(e(xPT&vR>+SqB2|cH33WU8Cmk`}t7D2FNz$h5YL9{gHP`%2;sDfhh;*MQn5|>1O04(v+'
        '>-+-%00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
