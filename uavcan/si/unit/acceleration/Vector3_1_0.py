# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/acceleration/Vector3.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.259101 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.acceleration.Vector3
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
class Vector3_1_0:
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
                 meter_per_second_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.unit.acceleration.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter_per_second_per_second: saturated float32[3] meter_per_second_per_second
        """
        self._meter_per_second_per_second: _NDArray_[_np_.float32]

        if meter_per_second_per_second is None:
            self.meter_per_second_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter_per_second_per_second, _np_.ndarray) and meter_per_second_per_second.dtype == _np_.float32 and meter_per_second_per_second.ndim == 1 and meter_per_second_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter_per_second_per_second = meter_per_second_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter_per_second_per_second = _np_.array(meter_per_second_per_second, _np_.float32).flatten()
                if not meter_per_second_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter_per_second_per_second: invalid array length: not {meter_per_second_per_second.size} == 3')
                self._meter_per_second_per_second = meter_per_second_per_second
            assert isinstance(self._meter_per_second_per_second, _np_.ndarray)
            assert self._meter_per_second_per_second.dtype == _np_.float32  # type: ignore
            assert self._meter_per_second_per_second.ndim == 1
            assert len(self._meter_per_second_per_second) == 3

    @property
    def meter_per_second_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second_per_second

    @meter_per_second_per_second.setter
    def meter_per_second_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter_per_second_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter_per_second_per_second: invalid array length: not {x.size} == 3')
            self._meter_per_second_per_second = x
        assert isinstance(self._meter_per_second_per_second, _np_.ndarray)
        assert self._meter_per_second_per_second.dtype == _np_.float32  # type: ignore
        assert self._meter_per_second_per_second.ndim == 1
        assert len(self._meter_per_second_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.meter_per_second_per_second) == 3, 'self.meter_per_second_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.acceleration.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter_per_second_per_second"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            meter_per_second_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.acceleration.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter_per_second_per_second=%s' % _np_.array2string(self.meter_per_second_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.unit.acceleration.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YXTTfIm5MJ&eq9Vozd62|J@xkL>Vew5(R+9rrKzTEzr!Cutb4%N^*<(T?4;o3DNW%EP{7FvPMJ~!Fo1Jzp{pR~-'
        '_Urhs-{Y0Dk9(Y#-0(OcMrcK2^@T>U2nfrPJTuA)aC19W7t9t~d@OSTr||p;4q@3%kd!9qe^SsMqiJANP^8KRlra$tO|8n(U{^4k'
        '=?1uI(i7U?708O4+8x@b5RQbE?{EZemQZW8iV7<Xe1@BV{S5*)(NQAi7l3XNPAw(YqjZZmq-#w}a1T1FFZjAhyH>vTS65q`BiKPA'
        'Qadbm1D0H?L|N6th?!2DQG2z@EQypQ@!2B~E+IZfjU`FO1;|J4;nsP&PYd3nZ^OHglgc;PMv%l<nsTc7<w8HOPC~oLbiw_@`<gOO'
        'wLy+MLmO+jXN_jH-mW*AD=Uq5tKM$6*4nk&YPDHwH=6BctG2RMZ#A1$@NX57n?ZCrWy+Qij=6CX#aQv_dE*xVkOO=D4DR+DWe0Tb'
        ';BiQS8zWf`Zt12Xrc9zNRt((2hDb7`)r0?#`{Bv-1(B14Nrg(wmb<?#a$(i~<3`B=VwbNl?(Sw0$5fZsgRoYQ#)W{NupBO(m<T%`'
        'Cy7cS-17$Qdt=IrRKye$!Vw=?IWb7P=;t&&o7>GI@~LvdEhfSWP4F4)iDfCjWCB*?8MaqJf~i}$G~pyF2kUbPa$U|F92PEeEf}?e'
        '!?C+V_WgvCJkypa4x4VCn5@uDpd%I}r#K33%KyYF!ZFywZS8OQ+f!s><Rz}hC!AK)a4w+-MkO3)LuNfZ=Ort1N#hqBN%xylL?{B$'
        'qKhr#^A~G`*^`6q1~+OH_Tx7k)xNyr;O-5#Jg5cLz)KC*&+h_})F4vr7YVWS6ccbPH{_-aWbI52*_5jT@dm1GQO;G`{YP5#w(&0{'
        'AGjf$M(#V|o_vSj_gE$z3KIMQaKv`T+XMgr'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
