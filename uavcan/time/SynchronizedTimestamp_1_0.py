# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/time/SynchronizedTimestamp.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:15.805684 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.SynchronizedTimestamp
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
class SynchronizedTimestamp_1_0:
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
    UNKNOWN: int = 0

    def __init__(self,
                 microsecond: None | int | _np_.uint64 = None) -> None:
        """
        uavcan.time.SynchronizedTimestamp.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param microsecond: truncated uint56 microsecond
        """
        self._microsecond: int

        self.microsecond = microsecond if microsecond is not None else 0  # type: ignore

    @property
    def microsecond(self) -> int:
        """
        truncated uint56 microsecond
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._microsecond

    @microsecond.setter
    def microsecond(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 72057594037927935:
            self._microsecond = x
        else:
            raise ValueError(f'microsecond: value {x} is not in [0, 72057594037927935]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.microsecond, 56)
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
            'Bad serialization of uavcan.time.SynchronizedTimestamp.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> SynchronizedTimestamp_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "microsecond"
        _f0_ = _des_.fetch_aligned_unsigned(56)
        self = SynchronizedTimestamp_1_0(
            microsecond=_f0_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
            'Bad deserialization of uavcan.time.SynchronizedTimestamp.1.0'
        assert isinstance(self, SynchronizedTimestamp_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'microsecond=%s' % self.microsecond,
        ])
        return f'uavcan.time.SynchronizedTimestamp.1.0({_o_0_})'

    _EXTENT_BYTES_ = 7

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8D=Ii+0{?YYU2haO6ir$nVJTE72&tc#hti<3Q;M1p^^K-Ns<tc<1o|PhBhSp;wUrrr>W@tpsZx1pB_vC&g!`-dPx>o*JiFOV'
        'XvxFI<9mJY@xA9B|9a-HyX!06U%1vzD_hlBZplbq%V)f(Da%XUwAxBXF<gA?j4z!xv_EYrzKl1Y$6w-RIGZcpz<%BHNy$~_WJB5G'
        'sVarhN<O1%9~;*3rj21epOCRqt0-2&+SB>^WgM&yR(_AqW4MrW=Zq}8BO8B2^w;28c*St`zNETZ;_2lTcRY6q<m-;NMmEyP2|PBQ'
        'C@aT`s;`x!F`3hsyO0;s<u$3X6LGME;3c;%Z*)abTnShAjsvA**)D7kk}2KjxA-WAD>-hiDsHNifnNARoDCNmSsHDr)T)Z%OkU|S'
        'e)rECD=YhgnDR|QhUpPI;boZ<+%dr?#9D4GRm@6N60^D?#tl*!Zl<ikr*cdx_;;Qz>!qOceFW7;j$z)E8D+ORuhceHa7#Ctw5+0$'
        'L`_&rrqA29mL+#+RmM`7(i@ZFERLj1-ck?kX9Y1sKYMf>$45pt%jkANiY^#y0F2BnW{EndQX{TyaZ#zp*fkT0yLC`xm%WEu0NjMv'
        'o)Su@nW9N56MjauKAhoO*tfR(C<!~16>w6?f$@u8kFh?x^V8P$>B_>L7uq{^=g!U+n-Vwn7CRKO6v@=0b8eckdu;pjF6N1|!0o{u'
        '!w$8tD<nb&#=KHglC|8(dOCvuA~5Of0ximhV?diavW2WpXm68OmmcQIBLw5fhQM?rQ7`4dV^$hzrOjrS*{#6^S@w7D4cVsBj@|$2'
        'CIb@`YH5(K<OZbhZK~H@R!lKlDPzm0wdP%q(J0Jt)&bu?ZWU`1{4t!Z;B}okoai>Lso%NJQjBO>sD`jH<EUHo0i^iYC0e8!m}FIG'
        '3_}rZ7BL8y!uqaOX-wQ=?!<<;I$ymr*b(oF_XjI!p2W4;=&U^%4u%iE9Y%3I-1vcvel>N+H}ox4<3Q;{mBnx_?*PT{!LcaNQ47K)'
        '4LT(W>yJ8q^7<H$=!f&Ta+!85?Dywu*u(1Wn2_1R7Zf&5$X8xWXUdpv!Ng_piTKDvP%1)Fj1yJyMYxoY<PlYQYE&+(I1HC_tGy`+'
        'hMMx0LoUKv`d7;$hVy$+<D<Q_`x5fB`YH792_^-oE;jtY%BBJ~p(prmr{%Oo=lT^jI)?XJUto@NLt|g3^h=$@>2ovnh7P6D#qi<('
        'DtPu;b~{V8i!Q0#MlQGo#-s-Md|u-V^yKg1Z2nUQmNF#rKn}ElIHZ~<8e_&e=GPr+bI|Vw#Gc66wXjPH;y7_?;1EF9ekKW>A}sUZ'
        'L&&kf$f3x(f!<Z~#EHIzMkI*Uu_$*VIf0KhecMtgNAd*i@m?HImZZ6;QKB2iv{@=SF700Zj^V8@rTeD)eoPBahc|PL7m&R!h@Cct'
        'Mt@M%2k6&aBOhWoxzlF(BAv@i0X2wXKfJxit0a~GaT4Dr>(JLVUV~SyqW?$S9PIpQ3p~f|EJ7Tt`vUiDq)M+G7W^nJ*3wG{wj}($'
        'G%gsj#QUKy65+Fd0gxdc$wCMK00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)