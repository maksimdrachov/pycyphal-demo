# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/scalar/Integer32.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:15.990743 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer32
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
class Integer32_1_0:
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
                 value: None | int | _np_.int32 = None) -> None:
        """
        uavcan.primitive.scalar.Integer32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int32 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated int32 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.int32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -2147483648 <= x <= 2147483647:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-2147483648, 2147483647]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i32(max(min(self.value, 2147483647), -2147483648))
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.primitive.scalar.Integer32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i32()
        self = Integer32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.primitive.scalar.Integer32.1.0'
        assert isinstance(self, Integer32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8D=Ii+0{?YWOKTKC5Z;h%5)&W91TP-kc#wE-jC%KAK#(<YG3rg4?&)&7v1g{~$Fd^?%t0~Gps?lN@HbkW-DG1VbD6HGuBz`*'
        '^L6R>pT*AUlkVA8dT9#g!D(*v7cLAGtZXXVcpU)Kjl<w#8KQ%Ctp%Lm!(%+coz!JDuPDDA`KaV|VV$mY&?6{($qjeKt2)3C+_R^c'
        'R@n%g*G-M8lU6>=&J*k}^gG}27}GlAAvi5!0FNK>Dp=>2Fm+#QFmeuOjY%Fj3mM~8<>wGFZ5--h4RVI@UuNq}=)err!=SL=qt+$&'
        'fmMwJR9orJ;H*t9EA}Y2pHoDq^9|o(+G0NNT5=~ZHu@2T>Zb09n@IDQm~2W+9gKpf%?s?AXs5y+q3Wp(PiQ1q2PF?6@g&`3pY#|c'
        'vyBT(OFT#$%s0`MKnVlPa+;M^^2=y}>DqvN91rr>32|F^Owzq4Sv)yg@y}jY((zI?BZ_TXwpMZTNJ7<Mx@)5_x?~Q9(d6-SiK%*d'
        '>N`!iAnWqfdrY^_-7lULyG3>bLl$R~DeeiSgF0k;M!Ez%QQPW1X(9|YesE^qTs*oMF2|UzztG|JX?#fG%)Ye98jGoSRTJM<q9Im<'
        'WS>~lY6RNFHx?WZjhipQGAos)1yj${tpS%(*TerVslA*%h=wS)m$TGi>h(|D>GytlL4SdrHp2dD6hybub>1&J@Nqt@<Q*fabM+d7'
        'vE}vYk8%)&7f}>{0e$WpRJj8H00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)