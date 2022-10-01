# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/temperature/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.272403 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.temperature.Scalar
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
                 kelvin: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.temperature.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param kelvin: saturated float32 kelvin
        """
        self._kelvin: float

        self.kelvin = kelvin if kelvin is not None else 0.0  # type: ignore

    @property
    def kelvin(self) -> float:
        """
        saturated float32 kelvin
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kelvin

    @kelvin.setter
    def kelvin(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kelvin = x
        else:
            raise ValueError(f'kelvin: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.kelvin):
            if self.kelvin > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kelvin < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kelvin)
        else:
            _ser_.add_aligned_f32(self.kelvin)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.temperature.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "kelvin"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            kelvin=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.temperature.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'kelvin=%s' % self.kelvin,
        ])
        return f'uavcan.si.unit.temperature.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YWOHUL*5MJc52qGa6FCN5;z`=1Jvp8He*~<!UM7^0#&vdiXq34l)Om<92<e-tH6HO?8u8GyV;39^(OjTFa*Y#C>'
        '{bk|T@A<~$b5F{eX(j`rxe`>0&oq`iAW4yxg%*Z`TRS$&CdMlMzAiaj!rnQY!LC~*In6Ns)Y2-Ud7wpLb72C*vyv<73xeZ>N~*vu'
        'lZq=XiX760Yks`4FJUk@XnccnaI1tGqeN^C*YFAMYU^(jxW&HUlFiy#A&eSIjPLQT@=}RR7*S!y{k|-y`IpfuiG?AO=OdHCU>hM5'
        'stw5s#v$EukA~OfzASi+u|pq18jY{;4%`;ehUSbab`$73;$(D$qp{3ie4=P#kiN#T^sj8ha68?w)rmUYaDTrW^*T}1JBZrtm#wfJ'
        'b;Bs^wf7G?y)bNnzsttyqFXxUvJyGC1;UC1Tmz4(+q^MK64%o$ok6;jZfK;)c&T_o4QFuS9+DF==8TkuGDI*qavMY!RwWz*l9Q4m'
        '0oU|DDPnAXh@uz|{plqRZ0-f_;RDVXxvXXMREvxuqqL~dFYBZ(Q!1Y`o)zF8mo}CnA&QTz^w-b!h1E+_5rMm>1@iGiLQ&k161erL'
        'n1XiD3jA`x_?d5#lxpl#@!a@rS0dqXk?y8@IF(o;^s{R%%yxo_=C%*+!7E|jO#EYXuT<gYNl}8^z6(UxSzI75?Bo!6qSE|6-%i>t'
        ')J$7TBuNG8HSN3gA!SVDqyLi9fsY<pi8SlmQADVyv>blG?qK_;j`2~IQy>^D+ZgF)s0EZQ8g%T9rk5@b+gGm;J}zlKd3Q%P*0GI)'
        'KZzSYt_TDG00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
