# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/duration/WideScalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.341862 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.duration.WideScalar
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
class WideScalar_1_0:
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
                 second:    None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.si.sample.duration.WideScalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param second:    saturated float64 second
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
        saturated float64 second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._second

    @second.setter
    def second(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._second = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.second)
        _ser_.pad_to_alignment(8)
        assert 120 <= (_ser_.current_bit_length - _base_offset_) <= 120, \
            'Bad serialization of uavcan.si.sample.duration.WideScalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> WideScalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "second"
        _f1_ = _des_.fetch_aligned_f64()
        self = WideScalar_1_0(
            timestamp=_f0_,
            second=_f1_)
        _des_.pad_to_alignment(8)
        assert 120 <= (_des_.consumed_bit_length - _base_offset_) <= 120, \
            'Bad deserialization of uavcan.si.sample.duration.WideScalar.1.0'
        assert isinstance(self, WideScalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'second=%s' % self.second,
        ])
        return f'uavcan.si.sample.duration.WideScalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 15

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?Ya>u%k~5te+>)z`>&96NE=scTEE#qfSfo5rqF!zp9Mi0ww`#RLzzI=c`rr(9Cf2~eQ<(ZU7@lz>?vkB~>mBLryC'
        '_Gi#12>Jy1*%_YYk>uD0<Zrk;J2N{o`|X}TAN%|5Q#0Ma`t8v;7IC5kf)+eX_~+pup-K?t=_nVxq-}ljVOdmBSrzorctqRh?b;XZ'
        'pW4;>c#wrD%wMa*ohZx{!4(mvBUl|*MOgAYQ$FJ{eHevFShV#*utN(0qb-}M=YJ#R=dC~M&-}IhqOF&Muq+Ecs7fl@KY)W*gf`V`'
        '>*IGhP2&BKmV!7e!=S`C*^$X0J6>Ov5tclq%ENIMu_Dj-=QMr<1EPeWTQ<)Y`$*Uc@XpT2<twj>V^r{zmwX4}Sb3ZYKFnzRQC89+'
        'Ee<DYIT-LVNN6@JS?jwHWfY1sNb?w?e6zmrpf`lelshnYAEz)ie`!B$>vI9bn8jfcA2jr=8o<_;Qyvw$pi!R1ZG9|=^QhhY-;tS_'
        'M~srJN(Zzc`4%~#B}mD_lCW@xl2IrGjfvn{M2W~#O2PtM6k#zYDST!n;Th<6nx(RYM&&pd%?mz+=~b>!<z}aa2_}P3&^5vZiRl)H'
        'oRASM*2B>#;nAck2%3qiqCh*-CFrRVbO{PY29y-^j}_DgmTwh#x^G=f%hwqrDFjA~n?z9BDMdNh6(iUv&xSBs>~Ppy7YgsZFTpM#'
        'xScSmC`MW4B%?c+CirhF$#*C5P3J9p9a2Jep_L)7D1;c_TUsJyo#;<2`*3DKJsjj!Np#({$e4zOxJh;yj~GtD(a6fNLT(e=>}(!b'
        '3vpM_I|bRzt0V?T;DL}T%V<P}2n(K!Cm}#15MGLDw2(Gf2GL?gEbv;gyb`F@xrgbv0uv+zZ(x}2amZIzLLZZ;;DQTfvY9&x^a798'
        '@7&%Xt65%>yC1F*=!6V%S%AMNETAc>5$4MwgE1UZ^f(H~Ngj4JhC%@!C|%%>`cjb;!ykgOU}2JAg|Xd+30?2hCoZ<=exgze1Ct&t'
        'r*(j)xKUzTU=9kL&7d#@k|>lG4#KH=;ZC06F)63#j;*jOQo8E9>>YN^pTYCQZcL8O{NoLO<CD)eTDDeS|1B-@7hQM#26e-1Y-jmy'
        'rnL23&;``iZ}p@=_eRigNM?s9Vd2xRKf|PthgtO^Y&pVF0rPjI4D<D@+G1p4Pz`9ka)1Ye!Fa;5xQkVGi5YCY0z!!?IECXx<Mvs7'
        'D%j$CG!C#(0gu~_`fMQbs)#5|Bs3U>Ko|8qLc#}az4!o_eeVH|J_mZ5eHV!IF`N{L>SP*j3!cUh8_Rd#do+&5BdFYZOw+urFORAL'
        'oa3ON!zw}d`-BUt=O#Q0JcOxh>nktiT18V-1#{Py$ZjhE3kAf8Y!Jxv+CGDt{9|Ks{?P+L57<0F2YCVHfH}uDhBF?*`7L+zVtc(i'
        'AmV_}u7sUaXq=KAI&fehPpSzebd0d?2R;}dGB|RO<U9qwi=|_1-$4$RfUJ5_?vCUR=;Xz^7}1Dt@dIrS_r*3<keUYxr09CzHv3Et'
        'n=W7cZtD}j<mJcR_d`1E>H27pkJ_5N%7_@JgB<DuS-lVSk{tO79L})Ji~SpEE{GVgLCbz$pMDU=NR>ZOVj<3MR0-VP;}>U{^|yA_'
        'cN;N)dwn#q(E1D20QQ;k3~xCQ!aWq`@uq`rL8JaGuA6E6BNC4y9%=kz^7}aAY~#<#@p(DEAaPNSFCoq~{<73Rfw<84ClQY|{wb+{'
        '8gaSt&&c_+h{qfMHECxB@wLW3hj^y(&m*2{{0oRD8vk{~rN+M~*S{hCUXp$;OFM5$e{UgPZu~2Vmm2?V#5WqBAYN?ztB9{R{yT^l'
        '8vjR#=NtbT;<?8EG2%+&Uzc&+Ks?*{t1`Yd#M6!c6B*}E5l=S$O&RaH+^-_zeiw1E@l_eWhB)8&y4;5$^I^*Ubag%2__o}aBlGLZ'
        '{dtqR`|nBonZ%z<d|%=(Bz_?Amc)A!HzhKOdlH{Y{8Hjq62F%Cjl^#yekbw!3Ep3rmBPhdSnUP37w+}KW-qW_*z1L-z3^o(eANqI'
        '_rf>5@NF-A*9+fEp@PRATo7=rAk)jS0rEUtK#S%6^K-49!Fz1_=!AFS;$65|%R^5|xX5n7MW(YGPr+~+4&hBx;Vbg}O>1^$MsqyJ'
        '_6*H1U0XLa%TZm;v~<VR4ad+N)if;I@m$qW0WIBfP1Eyi%X2-=F&*1gagA=Pj;pHhfH7RhRxQ`FEY~)4$F^O^)f~+-RTD=IOEV2u'
        'H*GL)8oFlaw(ENEskxx+n&1NdRKqeHOS3)KR>7O5T8?d5n(peVW9z16daCNFhU*zREH+gKoVk|jnxJGD9@s{2hHluPrR%z9x|(gd'
        's%u%E0bX?jb_-jCt-HFdtEOg}4s0HRH6U6?b5&3CbkB2LO}A8tUDa*PH8tII!LIFgH*Z&uIr)rcYwX`}5wqKv@qe+i?7!?k6}$6{'
        'eYnAX#qO=LkJzu7&pu}N*+zXtaJcv;KYZX;?|=FL1MmO%Ieg=>htJRhd(1W`T>3lqWJ<ZwRC;oNhR?&}25<Z9rF>p5PUswNQ2gEW'
        'QfmR*_Ge+23A}_-_{+fWKQ~}tc!1Au0iRQWN_(KRx39E~)c%8EY-8pBavCNhOb!45'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)