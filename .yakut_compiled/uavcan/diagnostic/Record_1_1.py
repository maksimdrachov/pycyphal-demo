# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/diagnostic/8184.Record.1.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.427841 UTC
# Is deprecated: no
# Fixed port ID: 8184
# Full name:     uavcan.diagnostic.Record
# Version:       1.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.diagnostic
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Record_1_1:
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
                 severity:  None | uavcan.diagnostic.Severity_1_0 = None,
                 text:      None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.diagnostic.Record.1.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param severity:  uavcan.diagnostic.Severity.1.0 severity
        :param text:      saturated uint8[<=255] text
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._severity:  uavcan.diagnostic.Severity_1_0
        self._text:      _NDArray_[_np_.uint8]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if severity is None:
            self.severity = uavcan.diagnostic.Severity_1_0()
        elif isinstance(severity, uavcan.diagnostic.Severity_1_0):
            self.severity = severity
        else:
            raise ValueError(f'severity: expected uavcan.diagnostic.Severity_1_0 '
                             f'got {type(severity).__name__}')

        if text is None:
            self.text = _np_.array([], _np_.uint8)
        else:
            text = text.encode() if isinstance(text, str) else text  # Implicit string encoding
            if isinstance(text, (bytes, bytearray)) and len(text) <= 255:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._text = _np_.frombuffer(text, _np_.uint8)  # type: ignore
            elif isinstance(text, _np_.ndarray) and text.dtype == _np_.uint8 and text.ndim == 1 and text.size <= 255:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._text = text
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                text = _np_.array(text, _np_.uint8).flatten()
                if not text.size <= 255:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'text: invalid array length: not {text.size} <= 255')
                self._text = text
            assert isinstance(self._text, _np_.ndarray)
            assert self._text.dtype == _np_.uint8  # type: ignore
            assert self._text.ndim == 1
            assert len(self._text) <= 255

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
    def severity(self) -> uavcan.diagnostic.Severity_1_0:
        """
        uavcan.diagnostic.Severity.1.0 severity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._severity

    @severity.setter
    def severity(self, x: uavcan.diagnostic.Severity_1_0) -> None:
        if isinstance(x, uavcan.diagnostic.Severity_1_0):
            self._severity = x
        else:
            raise ValueError(f'severity: expected uavcan.diagnostic.Severity_1_0 got {type(x).__name__}')

    @property
    def text(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=255] text
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .text.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._text

    @text.setter
    def text(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 255:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._text = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 255:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._text = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 255:  # Length cannot be checked before casting and flattening
                raise ValueError(f'text: invalid array length: not {x.size} <= 255')
            self._text = x
        assert isinstance(self._text, _np_.ndarray)
        assert self._text.dtype == _np_.uint8  # type: ignore
        assert self._text.ndim == 1
        assert len(self._text) <= 255

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.severity._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.text) <= 255, 'self.text: saturated uint8[<=255]'
        _ser_.add_aligned_u8(len(self.text))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.text)
        _ser_.pad_to_alignment(8)
        assert 72 <= (_ser_.current_bit_length - _base_offset_) <= 2112, \
            'Bad serialization of uavcan.diagnostic.Record.1.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Record_1_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "severity"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.diagnostic.Severity_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "text"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 255:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
        _f2_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f2_) <= 255, 'saturated uint8[<=255]'
        self = Record_1_1(
            timestamp=_f0_,
            severity=_f1_,
            text=_f2_)
        _des_.pad_to_alignment(8)
        assert 72 <= (_des_.consumed_bit_length - _base_offset_) <= 2112, \
            'Bad deserialization of uavcan.diagnostic.Record.1.1'
        assert isinstance(self, Record_1_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'severity=%s' % self.severity,
            'text=%s' % repr(bytes(self.text))[1:],
        ])
        return f'uavcan.diagnostic.Record.1.1({_o_0_})'

    _FIXED_PORT_ID_ = 8184
    _EXTENT_BYTES_ = 300

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8=q@;80{^vHO>Er86_(;3jn;p0{2M!oCr#r>jl|fFf7JZ6b`(2y8LeE|PK*HQhD(k#BXLQFLrU5d0g^)t8z5Q&W`Ueq6zCy`'
        '0==d{fnEdjR1^hr>7gjl20ir9lY1!A_lA$$)k?DCpfO;++4+6%&HMXCA8h^E-ya(?|FUCI*VCSFwX}$p<E!_awlA!f8+M{lt3(vp'
        'u2+SxI?(j4cOy~UDaJo6-Y>?o?JX4qA}-`mw(D9Fr*4wQV(pY|t-$HP7Kc-3*>wWTQ_eyV>O{HLoN&X~D>Bwv7O_@gfcuQRLG3$*'
        'J!}vExcIQhcC?%%iB&sIgf8BOO*i4Vo>gSqE-B%AJvJIG&q<tCg1pI*vQsv)CyA>>b%b@T8@MtK1N9!r2^~6dI#D5a%H6=p5ON~-'
        '!s+q=EkC>&A5o0TQp>={z8is73xV*i1c_J>@ml5VXth<+@<p(a$ikiiE?q|_txo6xmrrH~uT~r3GHV*fW^f2q^P^&}$o98@$G~%9'
        'uYaT4X&Xe_(NS(3YS3{2I^NpyLbtg2&xeMFu1mp#w9^(b59fK`EX@<?BwRYnf=7<l!sA*6uHZWC2=2siMC`;}-hrP%!c_qC&CJAV'
        ';HK0Mn})GkfZ;J^32Va4LIv}-qs2H^ntNhiflhcN;z=ipeC0X`+_}YZ8#j$(+^1fGC#706;G%e2@L0T?!rj2~`8e$KcGvawnay|y'
        '7!&aX*Fu;{U~I9_5eTY+1?Y{J706~-QRegpNCC_(JANvV%OvE1SVlF$XWkE2O8)BcGiN73C45DBz^8B>;PHh<gY!v#>IY}euGK6|'
        'ciLf^@KdLz&hV~qVm-lEq;e$=MR0RT*WwrW+0$mvzO}%23bqsTl`!=^I0#PQJO#gVh1O22{BFqt7y?&`uDJ!Z!7|_$Z{!S|n#eHK'
        'ILjOl!(Iwoa0gC<jm4@0eFX{FF?VC7m9|P@rhTvl<xWmtX!5ZjO!%c&$2nL+0J@CfJlBcADAEY^b&j{Y;G}qB<aGVeF?S3X1u?)f'
        'j9;&=ig%Fx1(>X*<NJ8SXl@I>m^9PNBj!a<Q5^vtrHv-_J%CX>lb~6k4q_Y);9@u^QCkH#!oG}6hXJ}tQv01eET5v*aeGQWBggF_'
        '^d~t{y3WXrrrn%<vsp+hJN}l4!@;ACy}`YqHkN{LC9n#Jg@&Obd%Ow?Vl@JT!(g^1B(OPSpN?PgBVWiyL1Y(uHH=@PHjHP(Cko_D'
        'x6`)B_VvZVR=Zn9R+M5=9+Ok@R0;vb6L2WFlkke$+3wc7S`}UkFRG=yqM7Y&=`f950Rz5hMGl0EYy^p~+C?^c6$1Y1RqVY3;c56e'
        '2&6Z_Q-G^o9cM|ajt9KSa2b9_UAG&-%}siu6BgOgC~bouw_>r7`gnXV;KJ(dWt@dLgsLmDCpL_=)=BGxg}N&ejBfi{($T;pMuQgl'
        'YjGRy<PXi#|M3KlC!p~_I0$114ybc9WAJeY{5M$%<E2UCAiD2NbA{$mFq}lLaX8o@^wTmVn269j2YyJkAi?E8$zccLoks_w`L;vY'
        '34&D>l#NR+!<;al)RA!2yy`Q1$QMh(!qD9IK}E+av*|^05IPzBU1U37QOWD(_cc-5bhf1xMn%Rq+eCLe?GWw<v^oR#MKN*~oYP6d'
        'xId%25~4vNoovrl$HP#$ZjzkG(PrxVkPQY$<qJP8#_XwFw;``b<qn0-(l*H1Q2}N-XgI6b7{N>j)`FYb!?<oJw;v+91?fY%y_J4%'
        'Lpq$>+o^wq`Wewt>Te+3p4&TU{!XMUw|61kn%lc+{vM<|a{FN#--~oxZa+f%>_hrUZtq9>aBd$!x;wWIBHfwWhmbaM`!KD4l+Hau'
        '=NzSd9;5RfM|w23pFnyfw~rxxG`Bg@!@2z=(nGoZ4WtKi`zfRca{HS|_viN0NcZLTapLP4q<eFFjQATzx+k~4MSMPsbXRUq5WkZo'
        'uSI-6hjcWzPZ0knk&fi{DU#!P(#L6%=M2&<xqX)8I!F4QBKf{u-n&irZ@)<NC894A{SMLZ5<O4!GSQnvCDB!)w}^g3^kbr*5dD<s'
        'XGA|IdbgxAY?vB{tHxN>n5r6=tH#Z$A*;q})woqPKB^iYSB+1q#-~-|v#RlV)woNI6pB4a5Rg_d(o<g><2)pw(WF;?TG=mVqcUOi'
        '1uZJRs`$1pv_Y_g5ZQT=zlZ5d%|pRJMORs?^>(5(8V1XvtIeij74lD2&8<jL9tDvVvIuMsB@tF<VYmc!i{lEDX6u@`ued(4zU04#'
        '^^{7w_o}M<a`P6*&F8ADysgZy(z^Nia9PD_+Kv0r@Hx~A3mEoIS$M*fBUn0!Sa2+d%yQk!5ZF0cZ!wkzs)G_jp)g(t=?M(s4Gj6~'
        'mt$|=`VCfF+{g<T*9jo#2FleYS0w9rhinjwMpYKKg()_hQ0tok?s&@zGaQHn$M~YGv(qGkf)WxrlzAw3N4QY^DBVG}eb@p!Q%v8u'
        'PzztUNdwP@IIKFrRm}r3C7?dR>#dl7v6rc!nk!kx9YmSdP<p7h2E|xWzTbdq%v1wf3eRY8%~rrz|3X}W^_xy3Q!c^&W1iAbRYGbV'
        'H^z1HzNT?~?!xp%^p)kAHB3Xkt`8#kU`mBBfE4bfMr|H)9!98B;~QNnNU^x9=7YOAplN`VxY(q;(j!YZvmousmnr|rSNf~AFTwn)'
        '7hk#Y8Zz(K%$rIR8FrL8Jc&b4sL(PDv9hrmn~RC+CKXFU3>@@{$Q0UL1UydaC+k=~`2Z|$z0$liiySAfiNF}R3c!Xsl~x9>n^(R8'
        '!QyM+{L}+*zP&kn{Yq&n>HT>(j{o&C|NH|mKl0{<x#pFov6UaztdxP-)Vu8f1@QrBVBi3bR-8D%5v*$s$kq3gq4Mim2oc;@hSLvX'
        '?HA|fX6KCUY#>1thj3V@WM0HE#HFv7^)nB^I-8!m0>*RU_09B;uRs8?*Gd6c8ZsY(>aQ+{<F7c7oJpQ_LY#dN{a<+f;@owV;Qc1V'
        'l6iW1F`RgiK%ra!30xJsX-6BYr)UH)&%7`I=z)Zu08@#1E<lvDxj0{1hI2ifD=#76f0cic|B!!^|Caxf|CRq)WRUb1x8i3Xe)iz!'
        '3H%(v&p3Xb#?NW|oPbX%FW;6|n(}*cW=uBath_3}FX!a7tkEk-ifnIHlB@-v@+Jb!F%u$spsgoYT?Uj7SA~2_zFkW5j&y67B<q&n'
        '2adJ?IFb=!BKfY(WDNiHmqtKa1`yEj00Lr!fEXblHh_Q_As|Kwhz%ehMhJ)z0%C-K7$G1=2#65^Vgm?>5dva_fEXblMhJ)z0%C-K'
        '7$G1=2#65^VuXMgAs|Kwh!Fx}gn$?!AVvs?5dva_fEXblMhJ)z0%C-K*Z=}zgn$?!AVvs?5dva_fEXblMhJ)z0%C-K7$G1=2#65^'
        'VuXMgAs|Kwh~=sLBQ+`*z;s<MTiMW>GCMoE$rE@SJKZ8X^o9ey&{IAXT)^J7PtUtrqO2q7O}rN_SQ##E0c0O-xlZJ`$btPu_DJ=j'
        'U<#oP*F9_2ZR`wAc3?UT@M$X8@bLjp!?%Z61o+6m#$_0~O#fDg<}g;xiAW@BvzLse@}1#}0r$hbjOz`_c;@cNTHhmIg1cx!B+}%e'
        'Gehhi)9ALgCSo<go01d`Id)i$rpd{EccTBrvx<sKB1*VpdScUvLah~C+yocq$p}~C%dHl5K~h--*2WYp|0EACW)Sn_pBI0N@$V;f'
        '{F}LZY+VFgd<llL{Zl8WPSYP@Ao!ge41Tw&;3rdv{FAY8JhUhyRUHr!Ir!m%!CjahpyUBi*fqI4jX@YdK@BRjPz5UK6TSusoZeNj'
        'fYJ%%PZjn+#r=b8-M9El5X}5o{1vp&ivAz-y*gS?LA0JiQ!p35I1P(RBRLNP=j#EOKb)@bUi^7I|1ucWdDg$6JYb-|G%dLU;PS&I'
        'Og;!#jJNyMFMjcN@TsqP@%Ly8BQ3a82nNN>JEPgbmPdc?i(3+I9mt@s^LzXH272xHK)%MC7k^z%9$WkkG-oD;@8z-YjG}fb57d2*'
        '%3<__4MuUX^*<v5^+NF+000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)