# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/node/port/SubjectID.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.183330 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.SubjectID
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
class SubjectID_1_0:
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
    MAX: int = 8191

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.node.port.SubjectID.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint13 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint13 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 8191:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 8191]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 8191), 0), 13)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.node.port.SubjectID.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> SubjectID_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(13)
        self = SubjectID_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.node.port.SubjectID.1.0'
        assert isinstance(self, SubjectID_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.port.SubjectID.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YWT~8D-6kWnDEa0NJghY(8m}r26QQq)TF(hOKH+-lsrfH|$ZFRoVcGeve6M4{tq=_b6|F5_E2^i*OZhLx9&%O8b'
        'NBQs9a;g8hwXEQVM*%THD;lY9ltm&SVH#(tQC5JfomicRHrL{`$OK%%<~e+a4ObxvjS*kXX*Z-vkfdA$S*mStlC#euv<Gj%RY_N9'
        'qtXOq$<4kW#+T5XYL<S%Ik*Kvt<{R<Rv7q%w6_Qvp8{9eS0dsQA@hV&ONsUBZcER!ij`GeJW)SOjOrwUA0$?EguY(Y0%6LMNF*IA'
        'p;<%nkQz&3EDq$dTWO7md|I%F*rA88qS8+|2DeO%r3t5+UnRQ8nXI@<mqs}%C=;HB;7WkIi>|ttCO*fGMaa5b8AcD9HMuGu%e4W+'
        '^x><IAlKy+H$#SGk46QHUZ#cd{k>Lh^_W`RqtS?7Zn?R(rlH?8i0=<$#9euJ=j9IgLJZ59aP=$GA*>io-0Nz{CAle|=GZST@ZOMG'
        '!QsL!lD6szPP`9@;&9}ah)HuD3IrlSGK$@Bv;G$;25zo}F6*`Y?j?4A>N$@03`d8;YBBv{RLoJHOuM+wim=EejkdXnQ*aNnoJA@m'
        'T6FTrUq7({X3q><i6wbo;?FArcYo~7U?+GH_|Ad#bE^|c4a(CZvEDmf6$-eJ>uz_Lv5hH>Qz;snCLLiKc(TDoTcME}tY}z7OeR9r'
        'R$;&4fuA#rP|CB>geHc-8|=+BxI3?vecNB3h_M^oG)XgXjoU~}5wjHgfF&GaU(oRW_IH`k)TVl3>=_bDh0jJFySpvQxk@_!9g-hB'
        'dXz^I)x}LzZvBRhX6=t*_^Pu312n5S!#ZP?K=YmtXwL_;{=wi>y#9IbOq%o`{!z}nv4VdE(oije1ONa'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
