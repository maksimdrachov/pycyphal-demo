# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/length/WideScalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.456178 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.WideScalar
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
                 meter:     None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.si.sample.length.WideScalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float64 meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.meter = meter if meter is not None else 0.0  # type: ignore

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
    def meter(self) -> float:
        """
        saturated float64 meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._meter = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.meter)
        _ser_.pad_to_alignment(8)
        assert 120 <= (_ser_.current_bit_length - _base_offset_) <= 120, \
            'Bad serialization of uavcan.si.sample.length.WideScalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> WideScalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_f64()
        self = WideScalar_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 120 <= (_des_.consumed_bit_length - _base_offset_) <= 120, \
            'Bad deserialization of uavcan.si.sample.length.WideScalar.1.0'
        assert isinstance(self, WideScalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % self.meter,
        ])
        return f'uavcan.si.sample.length.WideScalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 15

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?Ya>u%k~5teMry7?N}j$<dz+D&b#wHV$nY0}ztYB*)A7_r?5y_n!3S7#UE<&;ZGIspnaKU&xTff6ta<Pq`+d4vEh'
        '+Wrjs1VNu5KRd&-JdzySfcy=2XJ=+-X20F@=VO0=|I|$PuYP+pjzyd(fuIEs6aINPNT?D-c{<7kFKJt!d{`D$R8|FjG#=6RdAs&S'
        '`=@rbo(r-th52h$xD$n$BDf;LbOfstnhi^)e8yw?Fbb2fXzPVwhZch8S<7bX`QJ$SdF#*mGk<NrXzS%5EX#rqs*;NK4`BWkflamA'
        'dhRZ#NxUD>QV@q_7?c<#J2Dw$bM;jjU&&LdJRD~cEAotgPUA-~AW8_iW%F#YkA$57@9d0RzVfO#Mg>oK$#)=*mB*Rj!;HosWhEWb'
        ';&7Ulg8?stNlIGZg(#y?ltG%u5apZog$KPMT&CQCx%)VUsrgI$X<MHQAjT{Xi};|SXVn0<ww&^)$OVn^EN<&#L7YeJ=Kqe&%sgV0'
        'WK}w#1<AL_0WCpF7M6sCJCuw<A!tkl&mu}ho>CGP;GzhNF-hSwD+$j)ztb$0B{V9>!DwFaAxy7wg(^2YEle;Ogo3USE=WwbIOK$k'
        'Xt5rSMhTC?5^AmxG!s=tfp(@#&{HMo5)_IIC@JV4E2s@D-zxHS-@2HVuQNtc2#gjtiJ-JoigK_kMzB$y4Pms{;jp(Z6yAAXf?Ysx'
        'J7H2$jIzv0Mt3kx@ZVOF?@r>I&Rh06q=f83D??mS2r<65v_!}{(VtlM;mm@1ILND#=(=l>F%1iGlk74cF`R;fk(FbG+$Of!**vfo'
        ';;x`~3bLD5Neqs_10hwG(TEBW7CaeGLV!jfycE-DA#Jb>qQ#0>;I(9VB~Yt#57Ti4CP)b0z%bq8kgu$SJ|<DY1sBR>Gj|f`1s<*6'
        'xxGPFv%DmCKU^cw2^r+F0Dn<fKvPsB%$Gw3V>qPfaTJb|JnU)=g#tEEy1*axr6MVYKLlmL!X&{8W4jF#y56ZzTx`+(M5Po4COukC'
        '>i|u0qr|qr927X4L173aQ7A1Ogj4mxojk*1QclkuTVYqEbk%p+HTI4_gXf9em>iw?#~c2}C!cM!Y^}cjTUz8Vy6*Z7>W10a&hp(%'
        'Y3t)b7f@Tj)sq6<8$rV%nH{2pg-^Tw43j<{X4Q+Z<p@Uw%-@wV%-6GOi;;;zHK6s%0Uitn;|a&&E>_tkX0Y`N2qmWA6pj;(+h_Hu'
        'V2kh3IKV;$JZ?AYvw_H~BBC&n&|nk-UDWdk2_Lle;sfCIy$3k@9O!BGT_DoOa8e+ulWDjucp5`&EZ>3e(Ks59pmOUmP4l+CJgNq8'
        'j)Q^@s|4Ne6E3ViKH*v5AxvFcUwJ9lDw?7yn7g(_c3TNpC?G~;gFv3w_8HXV9~+bNj~)nmz~%uu$O|9`%sI9(obeFOZ@HTn+w0u{'
        '5eIyBCG4C+<CN^sfdd11QcWnKV}yM_@WJ?y!I6U`=PB@AEFEL}4sx&rWYv>$cO-W}Cok5;h(>&iA832HFSe<I)I3NaMc4bb*=KUt'
        'bot_UTc7wPFF)?SAJS=0*GGeV)YjxxM#MNB<WL{T>V2q}<j7CpaE4`G?B7VogNOkewCwlw=?7tqRQUrX7UJwimB8&iesPvre`{BL'
        'w-E!l*GCfzt-nwWV4o?^@RkE1+(Tg=Z#w7}H0sadx|zm5BJn8Vk;XqJzvmEV8~?Z*pO@nc5*Ow865{d3UzYkO5EmN%B;v8gKPB}~'
        'BQ7`o899Fzajx-SlXg}RUu*nxh-VuAJmRUwzkqn6@n1(=YW$0G{TtHnCF$p~wDYF)_ZH&i#=nAisqx=Ne53IR;>E_liuiitUqigm'
        '_&-8C-}vt!o@@LcBd#?5bs5(U#IudRD&t#2Jl*&|k#YVM@nqxQl<}_1{VFo<cM%sGUzPD|i1UrF%Y7I!AEw+-SJ$JBZ_9l-GQY0e'
        'pEs$y|DMF3Nqk@82NHiS@fQ+rNxUa<QzDbNC-JGoFC~5@@oS0SNc>jfcM`v!;QfVJDO~J@)n0IW;a)Fn_5$mLy<T|Q3t#raSH19c'
        'FMQJr-}b_Hz3{yhDtPR{1p(IzGQAudAkV`Ev{>#xKiBFRyvL@GPIwnC-i4dBJoJ==i|iI$WIDU?6bz@~5Z*Kuz9K)^v}R{!G{<vn'
        '&(I9hwRJ<Y9M#oKOLt7&a16~+O~bMs&s7~2(9$i}G(FF@JlE44)3IF@*XXwDxT*>d7{hgJ)p9+{a&1F*Y}<8Q&Cx7VHF4CiG}CZ('
        '(+2aVp=*Y2yRHYHnhVOV2`=DIH7vuiG~07+6})Mx<=B>`>8`Fiwr*Ocr>dT6xSpZIVpDa%nQN)82}*|Hfo=3==!Okix~_YstJ#*T'
        'x|Zb`;8izZx3ERnx~to|YHFtGz~&)X1EO^_SM@Yc_dM6tbW4TURo&KHQ`1cs?AmU3^LF)^ODR01pcd@ka1XQFnDBqGv+Td@KNY+4'
        'jD5Jle#P#svX9uWna@6E_t{2$L~ywGCck<>kZ<#PW&fAY;p>h)e1`VfW41XV(%-QsQ@)L+(vt%md>&plc-3bwCG&c5!sT#%;*X}6'
        'S_{~=KMPw-;2D&{Uj}~vxd8*i17v;+$eapP+5@G%eWh*W^&bpl4=eu%Z-Fa5M-Bi0'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
