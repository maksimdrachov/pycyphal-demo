# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/duration/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.343601 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.duration.Scalar
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 second:    None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.duration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param second:    saturated float32 second
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._second:    float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.second = second if second is not None else 0.0  # type: ignore

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
    def second(self) -> float:
        """
        saturated float32 second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._second

    @second.setter
    def second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._second = x
        else:
            raise ValueError(f'second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.second):
            if self.second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.second)
        else:
            _ser_.add_aligned_f32(self.second)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.duration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "second"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            second=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.duration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'second=%s' % self.second,
        ])
        return f'uavcan.si.sample.duration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?Ya>24gy5hf||7Im1CEK9cBavYINv|}E-)XItDD0BolZLI}UN{Ad9^vpE38=NcMJtWsafcQrO5f~r?Xae{V{0M#o'
        '0|{dPH1Y&Sp1?m-HPf?8$`S$ctLdYvx~lrC=3h_$b9rH``pMr+2Z0Vk$JJa(7RpbV7jnn-lPFEJG`!3gwvEbslPUgakn-|bx$;^0'
        'mvT9ubYm95JjvL;&tgYQN3$q}-9e_9kxA@q`z&Ot%xBzvt~894Vl1Ejt(BjZbexX;z5J}q=Urxul3r%GF8>6|U*gtqRhduTlROMY'
        '?##IXGt4#UqnM}%#bkcNdS_(Bo$W#F3zfw3Qyx5m0d2tHQcR24#uIS{tc&w@`{K*|NR^DFk^A7s;^SD$e$0apW5fGgoea{v>q+B='
        'JnkD&(k^)EGi}@`3Bb$O^UDt#MYzq`g1HAcg`xRd`AL~ybiv0sU@ADS=qU5xX!DWuRie3{#6g*#c7wz(cm6jqHugwx5@(Ue6-jo<'
        'u~nKF!3+^>pOchn%>$xk>~o@%h!dv3gkowyBKV9Akuj{VRvKpxmD+Jonkd<a>1F9~=T@}}157-o`3jMm1bkOQOi0RAi=}BO{kkFu'
        's_`?WP|t7+TFNw^gG3RJ6UG0WL2h9Cu1cbjc0EjArHn-27+1H5=Db?uC!klSa8McdVN~r)I9uh4tgO$$DZsgX7G@m1Gzp3MK86YY'
        '?1srf?cZ>|v)O`>kOLWjpWJ8Q<GXWngtW-|lg{SJ$ii~wC7B`X>)j3+aHjMvav-EHa0;$PYz7XwOE%k;&SQJQ?+j{3k%J@)126;@'
        '2+87@`&?_LWH_i@fI=YB=%Kd|HrNK<Vn#Y()rch1xT-P_(?JF*2m@=Nm>)`rS8Sk;iLa!V+Nlq-6+$gYzqNI@N0#Hnkb57j5U7M0'
        'VyVEM&lD6zmSVha6K?>Q6fLG~5GJh3F(eAOz^NR6)TD|;=zbp-Yr(=0GmPcd4|%IvUYpqEqd-L*2I?9$!#qGyEEy~djDf=07!pGu'
        'h}tRPBAm@<wvrgHi5cEIu_&%v=?3kJx5V3Y4DXXzs;|!U;~wpO{JUN$R`Q#_=PG&LbX9MVH;l$!oE*eXnNPWuLuLL(Lkj#bg@Qve'
        'J3$FEpH%h9!p0xb$!FonK8|Xbzh`Bb&&O9w^h|r1$MeNwJm`9Znql!2%i^lo5UmUdCE#Ebt`iT+qx`J9D-U_#Vxn9bl)e0dtCLLm'
        '9412UrVQvJpGF9!SLU-1fz=Nm;^;G=r}1}yNFT#Z0k0M!wx?wjfNvt%hwpUY4^qfnE8tO5=GW59gL~{M-p@ibKO$V%Jyr88@DPTs'
        '%&)(YYn?S`)xp@62H9=V6-<MV$Of*xujLWs<X^q|{-Xtg7O;4L4iW|AfHB81hC9yS{+feC?X{{4qL10EQdk*<!ZG5+g#!ginAMa}'
        'F~Z0Wd<fYWaOEJ#Nd$ZsSi@MpUILnctQu0TuH-(fNmNUx+?TuZSlL6r*y9dTvll{$ZZ>5zVsbdNdH%c1&-_Z7kE-u&KCJ2dl$)f`'
        'ZC|ED4<avt{6JJ6K)x(TehinBnM92`(v<59V1rWpF+cZ^1xS@YSR@$E_OcMV_u%<i(fLQYOuL2lps%O3hLX-?9-K3hF?Kl+*dYqj'
        '*y*5JP$?b9ePackuy_h_qM)bk_ax$YL8t8av>l(ZIBUn}5T^<{Z`YqeoGIu6;^~5(wd>Cz&KLB&oxgxMS<qLko<+o03VIRod_gZE'
        'o-OEQ#4`nb6>+YhSM2`Rtlg{D&NZv&b!+bp#A^k;j(D}8Zz8@{P=a`+pf?a-E$CZ_mkatM#7hNz8}VX6e~h?T(3{q;CBzE_UAF$M'
        'Af7AePpqFmMO-N8E$eT~p4YK{zk@hi&{gaI8sc<8*X=nrY&_cbJXKy#6?D^{>$Z(=*PicAop<`K#h+RHxyAP^{=(w>7Jq5+zQrAj'
        '!s4ODrxriA_=UwUEq-P3TZ`XW{JzEqGvijc(g@3q&~1eKjj+=Qq7e=o;b|j$-Uweb!k3NkRU>@c2;Vir_g2W@u?GzT+6pqg9rKXq'
        'p#jaB(era9AHzO2e00LQaP}T_R&(Mh35|?EBU=|sPeF0S`tYX7@D=%9zO>O^UGJ`Mv^O_5x}EiIw{xevwsw29z1H1mciWw{%{%Lz'
        'cDrsgmH8?AY7{HtYv?=TE*kicxFG&3zRASak@%n|el6}Vix0(b1Qj2N2cnlxXbC)Dzwx1oHLv_KKUcr=Pm;UXK0@u{vDm3;;}7D='
        'kX`(t^yC=hT!KE1jV*p5b>*`)b3wDfe-U1&%@uoe98MTQ(~sac2D|_6!9f2QbrGO0u5r;0EZP|@+Cvum!7ygb`9I3!GU_u8000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
