# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/torque/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.401418 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.torque.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


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
                 timestamp:    None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 newton_meter: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.torque.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:    uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param newton_meter: saturated float32 newton_meter
        """
        self._timestamp:    uavcan.time.SynchronizedTimestamp_1_0
        self._newton_meter: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.newton_meter = newton_meter if newton_meter is not None else 0.0  # type: ignore

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

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
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
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
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.torque.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "newton_meter"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            newton_meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.torque.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'newton_meter=%s' % self.newton_meter,
        ])
        return f'uavcan.si.sample.torque.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?Ya>24gy5hf||CUuySEK9cBavYI#v|}E-)XIsID0BolZLI}MN{Ad9^vpE38=NcMJtWsafcQrO5f~r?Xae{V{0M#o'
        '0}1T>H1Y&Sp1?m-HPf?8$`S$ctLdYvx~lrC=3h_$^PR=9>L-6Q9RxZE9anQDStvhcUdSESPogx@((p20d}vhWn@sUXgOr!g%GJ-x'
        'zmzNaq#Lsc=C5UJ-)FI-rK4Gt!funOKWE%|=(CWiGM{nxxzaL;OEH#D|JKUSN;*!*{$74o=JPHyMoBL-T$g_W)h}^sxT?%2?@As9'
        'BWLE^fEnf*^iWLHgJLqjZhbQ{0)GavFH{oCPkHbN2DAZpOEE2G8&AXnSQqE)_NABkkt!KUBlp3NrN^<B{g?+I#)kK~IvJvQ*OSH#'
        'dE7Umq+RgRXWF<?5`dSl=a(Kdig25=4RiN#3Pba^@{=;Z;DV2Fz*KNt(NX5X(dHxRt3-1@iGwmf?FNZo?)-0JZ0wQXB+ep_E0XMz'
        'W2-bVf*B&%J|`*Dng>M7*ylti5hqN63B}ZaMDQ6KB4b!ztu)RYDz)RFG*Pk-(<{>9&dq8S2AFtE^Hm}>3HYvrn2?mK7E9Am`piJi'
        '9fE57Oexee+=7-e&F3Id#N$M9C?0KK`>sl&k#;>yU!{yh;22joiRQdo<R_q4r*Kdi_hD4+OE_EQima^9!70GGeHLaMy)+4l`96jT'
        '{_KXyLG9mgzO&VWkdOlzfS=rF;NyF9bA+_W#*@z0$;iTT<|UaS8ynpY8E~fbO>!WlFK`MjMQjERxkI+vmCj>(!S4)eN0Eah3j;6&'
        '76{4WnEPC7rerv%U4TL$(&(YL5H{Eb-eN{NVAY5u)3~ZK57R*gDhLB>pqL*@h*xZ&j)||NmfEQgvmHV$NWZmxr$<)e#E`omtP-e%'
        '7-Ffwp3f8%MV4Z`ZV_()mlQ3gY!D`_$}uDgn82wVf7GOkMCg7W7Hh%65HpPB)(?5BT3(yj<)c7F90uwdHN!kWQ7juQ3ygun*%%T-'
        'Ac)#2;Ub*LXSS0VuZbDnJFz6LS?N0MinqkubPVs4Sgx<m^y41wef+y#DOU3vzvn7>-gH%OkT;CRUYs1nPMJ@+l|yCzMnekxFol9c'
        'GCM&DGoMuT$->4T(aC4w$Ucs0n7?afn9s-8O7u*7naA^`V?5}3gPLFQ6f5G2*c7b{2qoZP6s{8w%A@>@yDJZQ;9{a&8I-;JysMK;'
        '`5Y!f?xqarBA-SGrB~*&4}jATAK>USpr`S7fk+?2O#!bKBethy6o79c*@y3R;15#BTr1#FQs!6F%!7OED&EgRG(RF-*gaMAEbtJ9'
        '4tl~1xz<^C)*OsoX^`EPT){N>h-~26`&u4BPX5)a?>|}~XaS1{=pa!*4j6MRW4PlC?yosW)LyH)Ao`fiDutC%C>$eBTsTmWgjr1q'
        '6(fx7z=x210ap%!oJ7EPfi;Zf>m{HG$f_ab>Pqgznnbm9%6+*jkCi?2i#_fjHG3h1=tfgEBPNGKo9DmFeBoEpd{liu<incIPq|52'
        '=Hz8c^dRyQ$PYyIKIF@C<i~J18Fb@ON1Aed0c=o;Kjvp2umGv@2a5#5*<Kbx_Z~byD?0xuS7^7;9`yCJ)=<)!%!6}AGR7_k0y{)u'
        '8ao|S3o51KxNoeW6BbV)P89UC{hmY|FX)sVpSI&O7H94F9O6_#=k59h#F>IFBAzbj8N2>0;(S5R+4=K`lLdXn>RCd3rJxrO&lU6{'
        ';+cY8LR={5tB7+2y=?ctX6;_FcCK1IuUmU>AYLu#HN-0geG~Duf)d2b1-*{=YC+#Zyj0L1Azm!#+lUtm`eVeUg5I!xEhC;U=!*4k'
        '74d9A-?4uF1aYyTH?6-ddtS%-{Vw8cLD#JR>xk0@-LU7_wDD-$^Hg~~RnRSau3I*~U3<RUb>8WF7Jq8-XBOYL_;ZWDu=q=h_bl#M'
        '6c!IHKDGF{#V;&=Y4IzI-&*|6;`cS)pBcBp<wjU(gl;3;YlNLf5RGuy2u~Z~^G5ih5x#7MuNvXoM)<A~zPCaKk3DD*&{mM??U;u='
        '4-IJ6jGmvX`55-G;iD7Yg|l~|vzil6NoZsQ8rg<eehP{s)`vGuhOfx?^X1L<+D3O{v%R&o+3jp}yPezJ_4Qk8?e*?vyW8%pZ{6PL'
        'wA*!~smw3L{J<o!8*z9*fCu6m=sw~On)zCs7ylLi$;9@N_@F0#E$*#|55;c;6(5QFqL)u-32a}#^FgRz`elB$e(Rqkc=7NEb&JPh'
        'r>2fSh$lma@rTlrW2|!#dO0??_=WV9&(`b(4Fms8c%e2|?9p*JWeANwg5MbI{<{YQ{bTe+fWElKMLV!)XS8S!nd}F{m^J7B7z(WB'
        'H4Oj&'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
