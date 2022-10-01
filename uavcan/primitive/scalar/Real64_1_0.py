# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/scalar/Real64.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.016660 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Real64
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
class Real64_1_0:
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
                 value: None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.primitive.scalar.Real64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float64 value
        """
        self._value: float

        self.value = value if value is not None else 0.0  # type: ignore

    @property
    def value(self) -> float:
        """
        saturated float64 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._value = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.value)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.primitive.scalar.Real64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Real64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_f64()
        self = Real64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.primitive.scalar.Real64.1.0'
        assert isinstance(self, Real64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Real64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YXU5gw=6rIJ)ZcL0JB={oeJn0(Eq`s@#r=YkmW7Z{65hN7V-IeLWp6;f*dYBOc=0Pz~ps?lt_14ZNyGC}Psk(jd'
        'J@;eI>EEvXBc_wHU--D&mP1+3^<aBvYWJ(jYdhCPyXxA(c^kv6r@kKxKlb+fZD-?Y{Oo0X5f8&uH)aL?k4CdDOf&C#w{qUC?R+Rq'
        'ZTk5WYihw_xUSc>A6(nSY7!29JinjD#ol7_M|>H>O>MmIT|Rm{#AorUp56q-Fg<d%E-!kyp-bb9_Nl?E(%<wK!@EayYy5x5xv6vK'
        'b#0rauj1knKo(~3dexRTR`<dOC$G~}+Wc$qJx(qdWAb}^62m<`c+-@oFE0cA2{<dWY@8p<RQP#s3J>ECu$H6qJ7E08_a+l8Gbu8P'
        'DN}+_%q3EoaUvO^l46M%<w9l(NdzY+Trrkqf@dnjl1ZUZ${_+tg%DAkDk%_G8Rtq+B85;=VTn0IEWM>1GpYy^0M97FlnA9VFtLJQ'
        '#h?T{h;k}97MT(Vs$s;X;2aZ0kQ9V*mLZfOsxnF-nIQ?q6i13d5TzMlr)rc?0a1jIj43R*LW=W@LRCUxS{M;VS40rRFk=#ihh`~s'
        'E3rZu&PbLig$YN{J0b!rh6z)ED^yI&AM<J&rfXA=u;XjGY>ODsHyc=Qy`A;8>+N70pJ*_1jkimn;Fq(XACUX^IsIbx`PumlP)xXc'
        'iHbVk?kN5uR-aaP2B1ipunOaC8DE9>^>eqerS96^YgfkOa7PdA*cTQYwbh*g0)&Hf)GmiV{{$4ZIZ1C%fpB{dfyX}pM}Z5sR_2$%'
        'tx8}-)vm$rw#BxqO#Ps=t2TxYyD_g_p?kX=>s0=N?~uK}Qy^5h#PR)|3S+pv)8QP?(LCuQ`b5{ex-tW_*u!FyP}Z)n@l|ygCTW9t'
        '4X~fQ*3ku@A=1BX$MD`)&VPGmKLzt#QQ;lkb}`JZ0vWceyoH&dmB%n6s5EKeyUzB;xBZ1K_jOS@(0X+gZl9R4bj|XALDeF8kH;DY'
        '-oEVxgdH>fiie9we-Al)kh&dETwEV>7<c8GBzd@)O}ZQ;*~6k!_6=<}ooUX#S;u2O<YPYn7i2tt!a)T900'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
