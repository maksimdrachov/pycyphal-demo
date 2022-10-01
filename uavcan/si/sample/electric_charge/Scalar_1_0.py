# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/electric_charge/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.378528 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.electric_charge.Scalar
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
                 coulomb:   None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.electric_charge.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param coulomb:   saturated float32 coulomb
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._coulomb:   float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.coulomb = coulomb if coulomb is not None else 0.0  # type: ignore

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
    def coulomb(self) -> float:
        """
        saturated float32 coulomb
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._coulomb

    @coulomb.setter
    def coulomb(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._coulomb = x
        else:
            raise ValueError(f'coulomb: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.coulomb):
            if self.coulomb > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.coulomb < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.coulomb)
        else:
            _ser_.add_aligned_f32(self.coulomb)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.electric_charge.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "coulomb"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            coulomb=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.electric_charge.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'coulomb=%s' % self.coulomb,
        ])
        return f'uavcan.si.sample.electric_charge.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?Ya>24gy5hf||7Im1CEK9cB@*$FmcFbd!S~+nXg^nP*t+ilD4v|BHo|)!$gL9?3XUR1XApVg+1O~_engD(TKY|~@'
        'K!VsmjXZ&oC-Bcy&GaluSt3AwHGNc7S5<%2{Oieo-dq@~e)8ATVW5N1aWz+xh4OReh1_xdBuW!44KMSB2S#PS$rOJ$OnLdVT=}B>'
        'OSzm+x-pAjeko%EpT&-rj%HB`yLrfcqonWpf~h`t9{4O|s?2BH0asckaVf^~>CdeEw4~#7?C<3lWj^mR0~@`}a9#chY`nm`(W)|^'
        'yd!xS9C|h92Fx(mpsQk{9u$-LHS4625%@EVeW8+Ae$Io3FrW?iU5aTj+jt^Qfpu}#ZeM(nAE}a&G;#obEIx|0?8iL#FgCo;)$v%('
        'yPh;|$m6~dCGCQjKGVjHk^sDXHNSYjQH0x^EttE9Qy7}Rm7kXRc^7<)1EzwbiViXljy4}jUnQFRNgR~<NjFIRa{GT1V`C2mCvg^e'
        'T#;ml99gA_5zG+52Arf!YaS3SW1kb9M4T`MCKOXc62WI|h>T%<wbD3qsML;w(nQHVOfO4^J2$FT7+~Tt%~y!jB;Y#|VnR}`S}aXN'
        '=`#a4cL=KSGo?_^XbW1(G@pY+5swqa|C~W?VEc|rqC@R^l)g$CiNG<gZV=6Rwa8CEuTJ5hGVa5u8b~-><%+DV&%r6cxd96^j$WFC'
        '#C(8Zf<HT9vRC^zn(u73AS7f@2H+?68Tk0_+#De-vi`WUc|5YPoOwxR$ohJ>Lx!9weS_=?=?k2K+Yy_gLvEAJcBS*kUhq4E+EHXL'
        '$-)2(fdxXcIOaarnkg9$YZssph%|cSErboWfw!2E4p=oJ$uzF2%)@k$feOOF8Yt%b65<sbsAJ+Qsik)6!)%363({|G-R_a)I5FhT'
        '2P*_BA%<8gu;()cMUkZ#ubadh!X-tEDI10ft8xs90!nZy#~(JSA`!aZhs9d3FvJXFx%ETds+QL#cKBhSA`Sy}jhay&peU9MmIcN@'
        ';cN_vArM6ElyDJF=QCSLjMv1B?wwc^SFLo7cEuawEjotxNi5Y@XZlf(_CEPtuM{i!_1|-qJZrkDH^>`CV>eFrVyDcf+{&Rcf2|<}'
        'zMn$DA(<VcgqcsP`eb3_kLcvHaAY4xHO$|!GR)`Wt0j7-z0BkJ;t?Kny<ttXc#36lS!{?_280rDFbda+2jxM2+TD@+Ja92lt_;dv'
        'e$LfNrhE<)A$L;-bdgUZgwiYX+5155`}cA5DbUmSJ3yq5;HH3A3lZDZG77*qkqqEF9s0u*GS>=tl$80EH1psdyNdU-5X~PFF6^GF'
        'c@}sGLs#ZkpUbt*nzQO)>`H^|w&)6`!AE2R*WTCi0CMuLUVZ=30znH{JU|DD0&>8ZV;RF8XK;VbUZQqe)dkT<Y*s0(j6&fUaqPl@'
        'f+WmpN~jp&&<=bE*%xr-AjnAsd>2^5SiW8Ynt-etQm(G#0M;a`rBm+99eJeep<nEB2dUW$Aw<`kvN>dOIJ9~8yUb7hMw*YS?+1KT'
        ')A<QENz0tPNQoXsUIO`nsNREoS&sY!E+;dII_yYO(42t{O7X}1%zYLhRsLj=U^v^$Lg?PZXJ<v{ALTOb7TSZpp4J*lI+J;D&Pc}C'
        '<v?KjC`@CggK9ygbR74M6?DSl3B-wlp0wYSh~ovFvg6Zse8%Fe9iKy-D(Jjje+qG?pbLm63wqkFKZ7`5(6e^_9O7g_U$S}@5nn3k'
        'dBn2?y?}VSpcfHO74&7qxq@D@`(LqkFIziTte#h`z1I-06!a?M<$}JB_)0+u;-!LKLwvcQZy;VQ=$nWa3i=k}`GUTUxLDBZ)~_YR'
        'a|K<t{;eRMDd^9vpFc-jDCiCAZ_A$7v3|dUI9t$F>;D?!bV1kcIW}xO+V(tEUQZNs)1K?5jc?bU?^d06`mV)aSp22M_bmR(;`<hV'
        'ZSk(fZHvO<zQrdNzqI(3#jh=XWAS^7KUn;+#(Oj4R=Cs%%Z<=&gu9Kf-3X!)_8Z|zBYfEiUp2zljqpt)eBTH^G{TQo$l$RD4FcK<'
        'GQA!1kmsQR&6>mK=Sn_?eQfmTgm>ZW9q6p)*i#Z38G%N&E|#8v;)wO(O_Sj(^1Xa%qrJM`UEgSLZf<lt>)meWR(Eaf=4yMbyV35p'
        'J8PS_);sNX-Dv9m2TzVLi99eazJ<mkZli_&h;!n<;=4?29f%Kl;<w`NviMMZB&hgU+!MWgLQ5d}`mJB)XP$ZO!$|$!KTh)E!2uc('
        'kHmIOAAb;!M=axyq{l~?=K}O|Y;f^&DJ-9@84Q{R{;Tj@ZLZj*<8aatntuepG1&cg4+i>2D2xDwagB?%VbS*CqFrROpA2K>oc{xR'
        '`#lRn4FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
