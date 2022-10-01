# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/velocity/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.247855 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.velocity.Scalar
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
                 meter_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.velocity.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter_per_second: saturated float32 meter_per_second
        """
        self._meter_per_second: float

        self.meter_per_second = meter_per_second if meter_per_second is not None else 0.0  # type: ignore

    @property
    def meter_per_second(self) -> float:
        """
        saturated float32 meter_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second

    @meter_per_second.setter
    def meter_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._meter_per_second = x
        else:
            raise ValueError(f'meter_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.meter_per_second):
            if self.meter_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.meter_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.meter_per_second)
        else:
            _ser_.add_aligned_f32(self.meter_per_second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.velocity.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter_per_second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            meter_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.velocity.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter_per_second=%s' % self.meter_per_second,
        ])
        return f'uavcan.si.unit.velocity.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YWOHUL*5MC5m1Q7|ui-~d)I5_STm#ZdwS;38{H`D3qZgx8MOi%i;*)buJgGQ20G@<;zR<qzDhDjz<HTCHFzWVy>'
        '{O`H>+Qk!|mKC>LCBzCNsghr4szgGV&P#2j6A)I9obk+gBi>h~fOFVAg%j8b3#6bq#-DgPX0%AGOnf0-G8RfR>8j+2QAG`eB{CMq'
        'N?kx!3-yne_BjmZ2DR^S3Sos%=Zs9f6Ba(fZ8QB%g0Rq+Lh;!w%Y;)$iHif?R$dyJODD&eaj&m5b^pRyA*pmkiDKk37;IrnMy(^c'
        '<^r<K@Mw5d9?O!~7(0j|gi-qj?;vav>uABL;ny4ez&<%0AupcCgO3em4&hs*rGIH-kFeeDG+Mn@yR)~~?sZ$eUU$FOY`$!Cn!R?X'
        '*XcI*_FLUfrvdRSpJof;VJ@67q{P<>rV9>Xo^Z_|)G&dDjccTmw3;sK1hVaH-6B{nN+TF`g2P#OK#t`^a8hdHh~#h>)``{LFo6Lj'
        'NJ$Y&sK<|zDZ&_{HYUUP_Z+F4dx0DIfNUeG)tr8|GUtdb(_{3@idAJs)pIU#4dHR=QzaQOV&qjkezrNRUYu$P!W}CSPt+3<b)_f>'
        'Yg0`n&7_gU9fOP1Z;*^y9MXuw#ifrW6L6O8WV=X7s<7{~D@n{&gNg2@58?hR>E2xUN9bOPBitprgs^p66I<n}Mo>7(0fI!q#kIc0'
        ')ljF+Ok#_KWfEnZ^~2hbaxRO}e@WROMi0G0nAOcFb{JFT1^k4a!PYOE;@v8zjbO0kQ-qt#BB~b+I*CR-Dj1oL)yqUoN?Kf8zeAte'
        ')ThZG@9cYG3<LlG'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
