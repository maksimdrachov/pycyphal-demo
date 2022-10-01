# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/can/ExtendedArbitrationID.0.1.dsdl
#
# Generated at:  2022-10-01 11:53:15.877194 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.ExtendedArbitrationID
# Version:       0.1
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
class ExtendedArbitrationID_0_1:
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
                 value: None | int | _np_.uint32 = None) -> None:
        """
        uavcan.metatransport.can.ExtendedArbitrationID.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: truncated uint29 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        truncated uint29 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 536870911:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 536870911]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.value, 29)
        _ser_.skip_bits(3)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.metatransport.can.ExtendedArbitrationID.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> ExtendedArbitrationID_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(29)
        # Temporary _f1_ holds the value of ""
        _des_.skip_bits(3)
        self = ExtendedArbitrationID_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.metatransport.can.ExtendedArbitrationID.0.1'
        assert isinstance(self, ExtendedArbitrationID_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.metatransport.can.ExtendedArbitrationID.0.1({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8D=Ii+0{?YWT~8D-6kW0`-$HQFL=C#|VDN$Q<IP7!4LAZD5#CJGPA}WWna-r`Om<96<UtdXCYn(HkiX1Z7T85#lg+ff_nw}6'
        '&*}H^KYzy?r$6_osJY>3L=0$2Q~8y$6e5!3S&<uQ!Mj^~R+ot_HGHZI@F)Jsk^kn`T#G20VLU2nl~5IBV5!wqnIhLV3MX&-78D2m'
        'N;8QOD|5B=#=9v}fi}4DqTwbF&ekVBZp33h{gHRGgj%a5D=irR8Lzs5<VBWut#=YqJ|s6oIJK16!1$)}Ld#5ASz$(dUm4j`z_*lz'
        '9_Y)R&JyHLQcyiBe7ua{2{o2vIR`J6+}-XuP$-KwFt!~+*wNSz|Ixc8Vk}jhYCZ~dTr$yet%{~4G8iX3PrPe*Je_xQUCOysy~|yR'
        'w!43QD^)Hz4)y>)qtwN{xM}bfu_{)?YRSO0M@CCnJ&+I+J7UpbpBxGe3AMoev70A{vJadDJqhCPxJ6>}QYV0c6i7j_3pW`)sbt<w'
        'chNEZZa6)`sf|5FS@w~qK@Vm0i;)@EG!c1)`=U<jLeO-bLza8@peR`?6QZG4rs4Xbd{{j(a9DsD^_X|f)6<97`Yd`DJ&(eyybT(('
        'iJ%54Yfv@}uaXJ)W3l3Hzj(QhWgW>eA`d0#D5$|wy!i3?w1=``t^I%R-P~(wKb-FOaC<g=*Ccu2UFRkcQ)ev4u94g}P64$H%y$dG'
        '7IHnb-vmj7L>q`rw{Yf*D@kHoyuVm&x;q=W3Nor|A>H%<5oZye*GT2=2*$!rnWj|NSE?t-z_Y*nTD<(*FnrL(fEF6QWH`J`s_;&5'
        'LHl7b8QuyC8>(jr^b1rly!jn8I~h2Y1+*rj0U8$KjyS}B4+AnJ@p!7ddTdz9qJLC#$b`)V000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)