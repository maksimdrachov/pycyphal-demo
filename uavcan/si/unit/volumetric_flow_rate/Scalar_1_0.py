# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/volumetric_flow_rate/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.273808 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.volumetric_flow_rate.Scalar
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
                 cubic_meter_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.volumetric_flow_rate.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param cubic_meter_per_second: saturated float32 cubic_meter_per_second
        """
        self._cubic_meter_per_second: float

        self.cubic_meter_per_second = cubic_meter_per_second if cubic_meter_per_second is not None else 0.0  # type: ignore

    @property
    def cubic_meter_per_second(self) -> float:
        """
        saturated float32 cubic_meter_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._cubic_meter_per_second

    @cubic_meter_per_second.setter
    def cubic_meter_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._cubic_meter_per_second = x
        else:
            raise ValueError(f'cubic_meter_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.cubic_meter_per_second):
            if self.cubic_meter_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.cubic_meter_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.cubic_meter_per_second)
        else:
            _ser_.add_aligned_f32(self.cubic_meter_per_second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.volumetric_flow_rate.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "cubic_meter_per_second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            cubic_meter_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.volumetric_flow_rate.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'cubic_meter_per_second=%s' % self.cubic_meter_per_second,
        ])
        return f'uavcan.si.unit.volumetric_flow_rate.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YW%TE+B7+(|wK_mpi#RHrKOdR(yi_2A$y{zCy)SGEKZP{t;OecM;yCx)Z&`8om6F&c6zp~&W$|RF%=X><~J^E$#'
        '*XC^P;t8A8m|LzAVug`Z$<H)XA|Xr{mA29e2+K##c;>tjZ^xB@bJ#tF6W9rJq@)GLpLjZCv`nl_d?{Tr)XEpa8Og}8(w~T-P9#T+'
        'Drz7skfAVE>Jsu=n16q{K8M~+ul5a2AuJK<ur~8fSoi?9&G#n>!dzDh#iw&E5>6c@E)IKJd1YiFog8Au{jSo~{S9r2WYQ5O%7M$F'
        'w}mYkwT={;3&_{QM*pfjmL)GSb`V1dqxKcvKv*Z%(UMccuQ&RReF{22jy#VC9~;UX!na6E_i~Lr!gedIH#^N%y0_Qrw40qyd%x3Y'
        'Jg=vXPAl!C?Z)1Ivz?}Oh-djMp9>qzXGk})E)1#gwSwuALzpF8GYB<IqhakDwImx)<U4_UJ72X3nTyH@hGKCz3lGV$90^V;Z5)vt'
        '4#O(3+8ZV?paiKX0t)l-qhy9)`skKXKmI*O0%x9~F7J?Y#I{_}k5(2O5$1Y``)bU_RZi7YE(#6dQROp*(;G4HDjq-853BD@+y&u|'
        'm53)g4Eg<^#~`dsT$VJFdJ<I!7sXg3Ikh;j5v7YZ7)mDKEZ@m@k)BN98IP|_G8GFG-OW9O2QQ?1b+JFf?WJA9U7{-pTemf_<08`t'
        '5GOf6z-YlJ^lOxfI&G$=yGK|q(a3o>tn?}8vK;)Al=ouv&?|&Fz8S?1L#n)hAF$Kg`e`$~ZPla^^cH-Ea0^*RKjVUq;$l8}8d;Ck'
        'i$shnT3%epL!a5qXUT6VkDUc71ONa'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
