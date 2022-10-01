# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/scalar/Natural64.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.572060 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Natural64
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
class Natural64_1_0:
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
                 value: None | int | _np_.uint64 = None) -> None:
        """
        uavcan.primitive.scalar.Natural64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint64 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint64 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 18446744073709551615:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 18446744073709551615]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u64(max(min(self.value, 18446744073709551615), 0))
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.primitive.scalar.Natural64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Natural64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u64()
        self = Natural64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.primitive.scalar.Natural64.1.0'
        assert isinstance(self, Natural64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Natural64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YW&1)1f6yMTrTU$S<EnYm>dXRc>R1l9+EC{l8U99yc;bjsx!OTp^$Fd_7>_M>*P}t}H;h*SBx9!$S=Q4SDc`v_@'
        'm#+)I|IBwzzI4yF!V6O{FP#RXzW_I~U}aO;#_J$4-PjK<mLWR%zO@o3`0xl1aXWQc4Hf0LB8*C?3+r^HgC5DkmtepZeV`&R&!1sh'
        'W+UmmZfaDWwDjS0J;B~wuk#&`Fs(8O!D$|Y^!O34f^~ifQ}>mYM$F)>FaZHr$QZ9GKZl5E{h;=GSWEG`4ss~nzuZ<C*MS*X4}-$q'
        '4mB^q2UaygqS{Dz24{_OS+PsGy__OKop1OK(+2YaY5`7MZ1f{?)lJ<Im`Df~m}p8&9gG~(`UU=sw^L~kQEjR<PiTa+PL>d)z~gk2'
        'ebQqom~C8OT3|n|G2cX2N=g{XEYMwPDgTV-n63@T$?+iXPKevwV-oLxgz@BU1)sgHgo9EwBZ_TXwpM|8BxKcKx@#jhx@1lcqsiCL'
        'M5gM+sq=Kh1z{Jb?qj-r?tk&Lcv56PFl2GonF3EJovcGPXrxPt$7)O6Cr!Aa#t+Wyn~6sU!{r#$^_M!lIf?fvJhd;)v&LfDysC+B'
        'E8Y+*Lb69JX*dE+<6A2ogvQN=V3Czd(}<}T>DB;*(Dm@YLuxl?`_T~P_HvdwOuhbz+r6D%p3^(9(?-}^j-2RLy3X@O3mE6cQl2rA'
        'I#;hSIkr%rJe7Xro=0B%1x$2A!n*?i00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
