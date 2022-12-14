# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/acceleration/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.503231 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.acceleration.Scalar
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
                 timestamp:                   None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter_per_second_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.acceleration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                   uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter_per_second_per_second: saturated float32 meter_per_second_per_second
        """
        self._timestamp:                   uavcan.time.SynchronizedTimestamp_1_0
        self._meter_per_second_per_second: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.meter_per_second_per_second = meter_per_second_per_second if meter_per_second_per_second is not None else 0.0  # type: ignore

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
    def meter_per_second_per_second(self) -> float:
        """
        saturated float32 meter_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second_per_second

    @meter_per_second_per_second.setter
    def meter_per_second_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._meter_per_second_per_second = x
        else:
            raise ValueError(f'meter_per_second_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.meter_per_second_per_second):
            if self.meter_per_second_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.meter_per_second_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.meter_per_second_per_second)
        else:
            _ser_.add_aligned_f32(self.meter_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.acceleration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter_per_second_per_second"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            meter_per_second_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.acceleration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter_per_second_per_second=%s' % self.meter_per_second_per_second,
        ])
        return f'uavcan.si.sample.acceleration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?Ya+io1k5hW?{F6v@RvMkwh%TYu!(T>R_ms&Y-5{0%Pr>(VMN(qsR20b&)?FQ$T?jDkBAVB<(Km-QJ0Ga^)1b>1*'
        '!9ao}k4C=0$QSrARWm)yr7RI3PfcH{s;jC`HUE72?;kFVRX_RL=^)TS=(w6I$wK)V^Fr>peiEgLmWG%4!nRSFZ!*On4^mz}FIPS<'
        '|5PsLlWxo+n7^5^eV@gSmX2mo3cH!_^N=fMWD+~uJ`0&D^BH%aD-9#17|W-BZRO`B9j9Y|Ek7^wd6yZZq?Z}4%RhjDSGYD@RpyiT'
        'B@csRm*(7n8Ri=FQ%ux@VluyBJv1`n&h{Yog-T-i84n)AfHvTCDW=72<B2!}*2Q_deeqR(q)JB8$bIl*@ky*@Kjy(lvEhBLP6le;'
        '^`vn_9`}tXX&1conKo{e1mNYH`Q=BABHZR|!Q4Zf!qEJs{Itw3y5M6RFcpj{I?6ma+I%E^m1yoKaZu)`-5~MHo&QaYjXf5e#98EV'
        'MUq`IvPu&pm?47gbCNQxc|f#`eNJ=|al#asP)rR-1fQ`XGKTflO5@C-QacVx6D9jFy(}H>+^$w(fQiR6Um;SHfbU9(2}!wXu`~^('
        'UsnV{HGZZP>KSf9OPS_#kSOADqWB*($PH}YRY`QLT@TY&DI*a$#?@`2Ij<J^3Fy@+98|`A7*+cc&Q`f1E9-M`3UF?pg&9XLO+sS6'
        'k70s8yJ2!r`!}5LY_=dI<Uj`CC-)in_}<(cAuZB=+SxoASy;}zBr~Ml?smw4Go^2n10j8ZQ*bq6GjPZ~vbj;|9N7zgXHYwe93)v7'
        'fFZCzNEXN3=UOu*!$Iu=6atY(550x3!8Y&~GtvR8MkJZWRh4;|4l+<d7+3?v{7^!?Vgq$dd?mHiPJNiI5NbjCt*v`KvK%Ld-2Y&O'
        'KqbTwO9l3Prl2UY6ytS=cmuekXfb7jFkw}WAyL2wPUZOHCRHRt_xrF|3l@f$VJx?P$XnI&+QcqD4phWppsrCf%mWm~lEJdT7$}^L'
        'Au$AksGSln!r6RgD~a)%nBlz>i{iSKZqTlHN8F@ic%Q^leRZav^l0ys-}FkclHd9*SILW}t9paHVKnyQ<REs+e9EmHD)YA*Qs9Rv'
        '6daP-2}+pxw5m@QHvWiCJ_|?oaa6<neJjI!KE7I_XWGj=o-dB@pz954mc>&ni>qQ?v@#%+fP+!EPCO`&^0V%)Jmi6kiE?F7_VNp^'
        'PBP_lm<YL>GN6lm8X=Tkna@4~W<Pv{qtAh!#@_`ZeF8THyjqCZo|aJnzKLWXzSDs}NFj5rfJaH0UrRF&?y;+QKMT?PG2z1QshVej'
        'hcI+ye*L9f>#RAe4#uuD$Zm_SU>bZxHgN5IEsr24|LE2CA1x5HfW-rJkSHJrj5(Gu+;Il?*Bm5juT@<TJz}#;VPzBw$A}Xb4iqF|'
        'R#QU72*-BdL&&~>D+fVNBH+8g8piVV63_%>)sS*^CHG-XqFOrTzTA}~We@#gk2^@sUI-z&)s)RKlf$9Si{E8_=9kiZTzzlzVNK_!'
        '+$1e?@+u{I5P1pY2cr5A@?|;llN5V#qK-S#l<Ny%gHrrHKlg|QNR{7PBpA;2vJkrW;Kf<d`CGY6yM^|kucx(!lFnovoHLR!b~zB('
        'Aqvyj>7ZIrDILdsV+EbCcnWc%pr`HkB;t5Mr|kH&9iOo{YscphrwTf6*PlV0Dd+;?>4KiM>(3$17xcWHzkoPd(ATV<Ma0(%dJ*w_'
        'K`$YmE$C&$GX;Geaju|O?EW{b-K*BlHLK@MYws<@YX!ZIc(tH!Bfe2kf_SB%HxOSh=sSp)3;F}ZO9j1&c(I^AL|iQBE$i13;)Q}P'
        'TmM!N&lU7X*3Ta!E)?{(^|xiu>sY_vMVu|@s`Y;jak`*wdyaJ*j}3dCDzB#sx@pgK$Hup7&v&=ZJAKdMPb~h_;`<hVX7T41e_`=~'
        '#T|>n;-ST77Qe9grNyr-er@p^i{D!OuEvKm<5sxR2+NJoZG;Dnu+s>l5e^&SStESW2wyhBSB>y>BYe{c-!{T`R><J72Mq$+3NpPN'
        '^N{DE0nM7@=jTd3hJ9@K=!AFS?0x90=EPGH8X18`))q_8Kyk$S@TSS|75RR?w7#+0?zY!AHaFM1op!g|x!YY^yR*8n)?MG|Zgkc*'
        '@3uP|8+D_p%wLN*yc}G(*=|jVBO*8?{teAY+(WDX5*NgO#eXufbtFFMi4VntW$}^tm7wBd@lf>g2`z#A>&HJZ*XZ-V%+J;T0Gwof'
        'v3-OV#1pYo^U3eT(;@BnL+R-V6<vY`j~y?5DW~PLHKjop!T%jzs?8O9bR3Qz!fPOc-x%!vvj+qH5l$n(X<Xx?9ayw;yl4;U?R&$R'
        'O6UKC<Htl$4FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
