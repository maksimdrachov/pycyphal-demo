# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/diagnostic/Severity.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.208030 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.diagnostic.Severity
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
class Severity_1_0:
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
    TRACE:    int = 0
    DEBUG:    int = 1
    INFO:     int = 2
    NOTICE:   int = 3
    WARNING:  int = 4
    ERROR:    int = 5
    CRITICAL: int = 6
    ALERT:    int = 7

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.diagnostic.Severity.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint3 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint3 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 7:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 7]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 7), 0), 3)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.diagnostic.Severity.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Severity_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(3)
        self = Severity_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.diagnostic.Severity.1.0'
        assert isinstance(self, Severity_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.diagnostic.Severity.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{^vE-)|f>5KfflN3W%*N>zy>sF46AYP+-)=tG~<kW^8cOSq=c2hhs9J9oD5+AG_8$$=`-2aqaR0;%Si7ydZ@3}!a>'
        'BWW7a2sJP9tv%!Kn;Fl1znuH?%EhVXFI=w%g)3B&I<S%}`4i6+Bx!ES$~fsEhIbx&Tj##Eusf(AzKqMy<FmLFW>d{e+`m@ye$I7L'
        'NZ!-Nd6_4Vp^x7DAcln$S56uo#Z;L8cDQ~SH>WqJev8jzxR7%1t;}i<F8+XSPXIJN6~pYh1XWCcw9<lmo_a!el6hriDZT9DiNz<{'
        '$)1K{Lwo3fJ<94rnn|B3&^<5W<_tQ|x$|jh3W(xLxVkfPL}tk<?rqT)GMf4|c4D}aI?r{%ZE@Jqi#ijtVYbgzjR?-Ag~{X7f2OCV'
        'b_Fmuj22V4P|R}Ole)*c)|Biv^M>8K$@T<TV9M;V#)o4TDhm#@r;oSBE|zL7F>@9%_+?gtbG!%cCPPRqA$#JuIek53{~GIrHTmR<'
        'l^RN;W$swlSmuvmcZ^$T70{I!UX}quOIRD@(`+za^rgcMq=eTfDCvGv`>OV=E0sr2$h(AGa4lU)uob$Xk2R*#k)Z<xxo^?kr9`fX'
        'YK(zE0cOYJ9V77f$17&KL&)R-k6=t1_F#|E*po`NGGJAmDd_|hO$3j)LSTmt$pRTOS638SqPbK^mt!G7v7AIKfJ<Rv)o3aYKdv{i'
        'D6S4y?`_VAYvMz3eON5Jot4$KC_W1Pts@Mio7{@;jxMd~I-}Kq6?GHCf@qkE0-Ut4#s<s@j3v{?kIzfZIEEdc5*b&RV2^K;;yG|0'
        '$|Q!lbXc$-j2;#2H{|f#ktem#8QP9`i5ua3*YcdcI^16$u5mw1-;VTBT!u71J~awouRVD3kfNZ*QSgHMhB=oF3vUgk37jy-Bl)Ct'
        'a=a*s!^8<wE2>e3S)v|+YYZQBd98ec1Vl1qBJPIiJ7<7=Zlk@vO^E$N(9N@v8Y{CLh4+;rVxt$A!`ndq`5BPUwYPUS4r;DG9edMG'
        '-Y)pNX8=F{-Abpu(Qazx=P?xQbBK?g1kW@PQCPCnju6ovx0-fxqYK$o>S-KC-C|4v^r;-aI7_v!bvoOfrgmP#pt1%pD-Xbfwb<?6'
        'F7z+Y0DWP#vw_94^5~@a(>yk{JIW$Qd@{$v`X5BN+T#N^;&Y6|S7(X;%A>W;E-`r4#$M7zXbmPpQs7tyOAK;p^SX3R)epN-0VQFR'
        'WeF&QJc7a@q{;Tb=)5t9dt(j|77q!gG#ea<Fyg|*Ww9(i5%<MCu`V8nZ^V}PUOW{&kqaxdcqRrl%A0~FKk|Yiz6h7nuH1(rr6i@Y'
        'i0yDWb*8pC;D&;<;wWCiJpEHLi{bnZio*RJ`uY;Z()4Gj#-7k<MwwXhADt`<?DWF)@pm=I2Nh18TNoS@!~4xF%~K1#TG90r)rQt{'
        '2O=_t)<j0eaCsyolRL@ngho*GB(fG$!5xCL7-JH8eVIdifoWT6+Lp{mjcO9>vEXSknve*~6kh!4XtYh#8hZ4v{*K||1L+?%zaPVR'
        'eutUVR57rVoVY=m8AVhUw=fE*M(OtLX4o1#QJr&XE+lGN@mF|vhZhAtm}7^;-?ZDVmEv~r>aMu)dtBO_`NL%>xvK*YadV;0kSFRS'
        'T+)K?(_)^~Earglw`inu-Kg?*ol%J;{{j&$Li`^L000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
