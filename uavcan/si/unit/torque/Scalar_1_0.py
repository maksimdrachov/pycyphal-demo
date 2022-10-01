# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/torque/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.268745 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.torque.Scalar
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
                 newton_meter: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.torque.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param newton_meter: saturated float32 newton_meter
        """
        self._newton_meter: float

        self.newton_meter = newton_meter if newton_meter is not None else 0.0  # type: ignore

    @property
    def newton_meter(self) -> float:
        """
        saturated float32 newton_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton_meter

    @newton_meter.setter
    def newton_meter(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._newton_meter = x
        else:
            raise ValueError(f'newton_meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.newton_meter):
            if self.newton_meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.newton_meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.newton_meter)
        else:
            _ser_.add_aligned_f32(self.newton_meter)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.torque.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "newton_meter"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            newton_meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.torque.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'newton_meter=%s' % self.newton_meter,
        ])
        return f'uavcan.si.unit.torque.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YWOHUL*5MJc5$U{OPUNn)Dz`=1Jv$$L}*~<!UM7^0#&vdiXv1g|3$GT%eA_t8mooGV&W4&3;f{PgDGF4rVuJ5a_'
        'zs&vmJzKl@{3BH{!(>DZ*Mds%nI@7)BrS7Q8euv3)g!B2YMth9D#hU(c2D61cKkdkXpZrRj*e1VL`Foe5H_-<{^)pglu}7G_(d|}'
        '+K94%tmf<QF70#Z&-82G;1v8aq1I}VILi&ZhubFln*@HoC%9zONtOtsmJ%DryRBSlkqawEm~po!OKSfGvrH0UiR8u5X3*clmMJxs'
        '<R#;fZTkCztMX75y};N(2qBExS9lG6lNd`2Mm4+M=sWhw=@40QEL?o7X=)L^L0Wp3Humt_?YPnEw%YODUc1|Ab-SJYZnOEU5jVT-'
        'xEptxd;6_U95*1`<&tdPuN3@~Een!!%aP<c!panU4TIEgTqBeu)nrX4kZot{27xlJG*7AJ49@&LaxBK25mjnS1cO7rPE6@^$}u20'
        'Q50eLdiY6^AcO&`Vmt_^=SbVkQ{2W|WEv5z=JbORIYV4oIYM7mX{9nMpD>=6;2$WLNRblFhfap;r(477g^7y5-!TI51SR3&L`&e;'
        'CTfbBQ6mc51sh1;AQ?3{qUMDS>mG@e!&$bI?IIzG#IBF8#4ue7Cfb`m_?73vzP#{{(7lv}pCzRNzja#^Q{_pCkZ_U%gosiL3w@=y'
        'ra1UiTni-41PV6m`LzLMOccZalCpk?9y*CItD8~mFrpHP_yIfpt)C{rSEVM6pugx6gqw>Z=oSq+4n{p_7kLiVON5UVEiNA3p-W8S'
        'lIRbjqDVvp1ONa'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
