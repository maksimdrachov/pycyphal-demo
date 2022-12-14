# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/duration/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.227638 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.duration.Scalar
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
                 second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.duration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param second: saturated float32 second
        """
        self._second: float

        self.second = second if second is not None else 0.0  # type: ignore

    @property
    def second(self) -> float:
        """
        saturated float32 second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._second

    @second.setter
    def second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._second = x
        else:
            raise ValueError(f'second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.second):
            if self.second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.second)
        else:
            _ser_.add_aligned_f32(self.second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.duration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.duration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'second=%s' % self.second,
        ])
        return f'uavcan.si.unit.duration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YWOHUL*5MJadh=f4Am?$TKgX2DCaky%-mlfQIdNZA#>1L-x&-A1pn;jDpIcOy5L=(#2>eXr%T*NS!sp@)keP4b3'
        'W$xGS*~aDPpH?+9Oh&|TEvOWqX)1X{GF4Q{2+P5*9$D=&>ok8~R~#;2_Y6*9$Ip|J78rlx=qRIQWJKgjVI$@=wL+EAQAQ=z;FrjV'
        'YlA0{H~iwqEBgZaGyTRlI0L^zsI^+8&T<2v;I5heCV`*t2`<@mmSw`IrNo8-?<%jfD1;Rw%(&l^irRnStdLY#B6&HqIrO)%Wk!u9'
        'g<>4?P5)?cT^`D!*BCnpA%xNR3h%&g5@Tt}sAe}CeaAip9U?D|g^Q0h%>p?FY3W_r*u!sk;$}N(cjCRhPSR~BNq0YKwO%&kR?>-+'
        'xZB#>Z+GLk3E?i6=JS5R@Jy8q{2XB_1K+@7>NjpsNz!_<qEpDX^L2v|8Lu?YsO1dK{X=pr#+;E#X-foyL%&XpaysJ}kepN$0r<u6'
        'lOo082dIegAe>$xVKXmq4<C?Y#Ijn@6C(<Sh;lVTzpAsk%Bg(Lc%i^Qu3RcbMl>Hf8Lpr13#%6<3Ic!62*eXqg!EkN2>jYaNl`0m'
        'Mq#sH1K}Garv``AytHA}Bav}9&v)`&q$HKt_t~`&rVGJDd)o*9;FYj%F8w2PuO#7TiK@VF-POd@MXC@KPI7=CQD$M<w-v{+m7WS~'
        'fn>QrvF1I$HlU1&a`<0T-Vf13ClO|SJBl4fR5}hnV5h(J)1>&Ks!1d0FS!)q7NQKAMT3rmu^4oVOo!@a!p9XYFCX2ZOHJz1=ns}F'
        'yH)}O000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
