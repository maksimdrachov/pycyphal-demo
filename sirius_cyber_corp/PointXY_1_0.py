# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/custom_data_types/sirius_cyber_corp/PointXY.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:13.356803 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     sirius_cyber_corp.PointXY
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
class PointXY_1_0:
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
                 x: None | int | float | _np_.float16 = None,
                 y: None | int | float | _np_.float16 = None) -> None:
        """
        sirius_cyber_corp.PointXY.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param x: saturated float16 x
        :param y: saturated float16 y
        """
        self._x: float
        self._y: float

        self.x = x if x is not None else 0.0  # type: ignore

        self.y = y if y is not None else 0.0  # type: ignore

    @property
    def x(self) -> float:
        """
        saturated float16 x
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._x

    @x.setter
    def x(self, x: int | float | _np_.float16) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._x = x
        else:
            raise ValueError(f'x: value {x} is not in [-65504, 65504]')

    @property
    def y(self) -> float:
        """
        saturated float16 y
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._y

    @y.setter
    def y(self, x: int | float | _np_.float16) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._y = x
        else:
            raise ValueError(f'y: value {x} is not in [-65504, 65504]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.x):
            if self.x > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.x < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.x)
        else:
            _ser_.add_aligned_f16(self.x)
        if _np_.isfinite(self.y):
            if self.y > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.y < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.y)
        else:
            _ser_.add_aligned_f16(self.y)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of sirius_cyber_corp.PointXY.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PointXY_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "x"
        _f0_ = _des_.fetch_aligned_f16()
        # Temporary _f1_ holds the value of "y"
        _f1_ = _des_.fetch_aligned_f16()
        self = PointXY_1_0(
            x=_f0_,
            y=_f1_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of sirius_cyber_corp.PointXY.1.0'
        assert isinstance(self, PointXY_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'x=%s' % self.x,
            'y=%s' % self.y,
        ])
        return f'sirius_cyber_corp.PointXY.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8DJnQ)0{?YWZEF)j5Kgh_tF;NKh5Er31Z@kREm(hmg?>33L#v`6WZAvlW>@!ak9`R_L9ic`78Vq`{$FR4w28(Z95=f&^V~c$'
        '&wQKxeLh<oJbtsRsG%}JhG~JN_=1UK3CdJnDkCfle&y6^mszLTo2q2tD(swxuVLHQQGs*tZy2G4GbpPF(~zjkq@zS(-+u^x0ri+R'
        'LKT76{QSF-eHGG~wDu#M2fvK4wOSBonF${O^_F^WqJpm<2`1^djwM8~#mL6uZc8t<$b}U>h*&(53fsS_EF&T;lC0=j9?}LtX4qJi'
        'E6M_2^Xr}K^q7_$g6}xGfJg0nI0=3Y8H)>wHJt>y0Gu3m3t=6NKR(kqv%ud#UyepLVEForgM+>2AtE`#>wcym{4Am>3%(X_8pA4i'
        'i?5HYjkLiZ@P~Z!f^YFh(*RZA+kD3n=35i}MWh;zEJ8ftO}@`}9dM_t)GWi6(QxVSp)=8E6qQO_Bxq>+CNj$DjDbTkRAOM}=i^5T'
        '0<1b9lYS@OUO^{ko&le?(0m}dlH<=t<P@lK)q`_cWmU<sd`elaf^TNdSe1{*2RY3tF$Lck$tl@S_L4Z=U}Mu;h+_lwXja%b?w-h4'
        'xQxW1dqe`*<7+XDhXR52-*fPHUkdwba6X0ONEZGMQt<b!+dxc}6D0*qsdWr|Kx%QIuS=$}ReCJ0Ih1h$g5{}S?O;kp(VYt79e#Xc'
        'rT+e*D&jzj|3do3AtDfuD>IRKGJ&z$c2Z(pO=Zua9+r-UpJ6*~{4xZVv>cWNYv~9yFBe7J0x)nt8uM`zoWwDE39){Oi@_eZL2YCJ'
        '%Gos<GlcVWiwk%^fkVciZo1&6uMKe|`2#6R<{gX#000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)