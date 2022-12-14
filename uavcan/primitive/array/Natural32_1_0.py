# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/array/Natural32.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.049718 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Natural32
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
class Natural32_1_0:
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
                 value: None | _NDArray_[_np_.uint32] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Natural32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint32[<=64] value
        """
        self._value: _NDArray_[_np_.uint32]

        if value is None:
            self.value = _np_.array([], _np_.uint32)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.uint32 and value.ndim == 1 and value.size <= 64:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint32).flatten()
                if not value.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 64')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint32  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 64

    @property
    def value(self) -> _NDArray_[_np_.uint32]:
        """
        saturated uint32[<=64] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.uint32] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.uint32 and x.ndim == 1 and x.size <= 64:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint32).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 64')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint32  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 64, 'self.value: saturated uint32[<=64]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Natural32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Natural32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint32, _len0_)
        assert len(_f0_) <= 64, 'saturated uint32[<=64]'
        self = Natural32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Natural32.1.0'
        assert isinstance(self, Natural32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Natural32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{`t<TW{1>5MJL6A>6{H1q$ZA+?M;Lg|^!wRjH-}DHPr+$Gbkn7T$|&Z^TwY3J<M<WT{8W>3bgYGxC^!(DIhY{EW_7'
        'Z!X&qAdm#LO<vZXnQ!JhbB?|HWybVBUL7uU{<0&@wx9S>$xT=sdQtd`SBY53tu|`SMiQn>Wc?4*xK&MCG5e|AWMV>`c_E&QVrIB?'
        'uSR~S<&9RodZ`(QwJ;4wS;>oIuU)$55yp$IUJ;q?j<Prj8+8#BGV5{odP0B#h2O*rk@dM=n#N(Jm9j+qELLK*5F|3=yO2fxBAczQ'
        '@1>rbN{ZRR72uMW$o4<>$V!$USbZc7zLD16rS-ckVl`GzyZKh2v#?^34LqtR;YgkN-`7(%!s6b1eQqU8-KbMefJ0=fUXr@ChR;NB'
        'Alo-IpGd+=cgcs+MGY$aDjtYzkDH`k-S=XDX`=B~CEG%onqD<b+XBkj?yk#yBAb(w4-Vxdf+JuDPH+qqnKC#j(YjlS5|N#nU*2MJ'
        'T50;vdy#GXHca!TJ*3<2@-oeBH0c<ulq6}_Dvc<tQj?I?8q~a$cK?2p#a`No7n@|d)gYuT4X$Q;?>6dHFJ<-DhRQ|D$e7jXtQ0AJ'
        '$Guh*d2xGLr0I@&QHzP+MG<VCRD$c>X51pw{s&%tggszQmWC@)dg|7^XVh8(lsm@YuFU07u1^1IVVyQfUQieo?97t8+KN1h2Svsf'
        'IH=uEt@BBzUge;7ZN`EPG|)Mi`MoNytsWm3U~;g#xGl?kV9^?3>jIuEbl>;dIM@PPIc&>)wyf2^VjT3rHV)f+@{*NoJKl(ae%Q`o'
        'XP57;x5mN_*vVn{vO44;`@lQlVHfP?uqThz$-hlv_r5b024D||eXr#}Uh?f<RW8^I`#5|u-)G|T>8kOtA3ou5U`0+8LH>j9l@~sR'
        '0~`+Z^ozWd@3Z&L2M6I0hr@5=OHmYa<b!I!XK<K<(>-5DKR6d0q30To<$0VpF_(3ZuSq>P3dcB{n6J5H2V{Rvu2~H@4ktLAdh4DL'
        '!l7u2J-w#2;Ut{mP@G>UJqhxRomul5a2kpn&c5?H2|@Aa)`bV0fwLUWFYfIL%2`~xzZcf6E}Vn&97?O|1EC0Waa}pV1t@X2l-JlP'
        'pSR2FUJow9B@S0s-3vkz?&^l{gUfJ*!?opS<viuSG=E;MZx|Q23fDN?c(0xjny@!Flq+0^8ys#ezF&%+zR^48^9|<#H{lkCFW$R%'
        'l!5TKKMHU79KPUiXXSHvjcVMIXYtFA#t&}89S&c8P=6^4<@oxet^vM;uQ-&uz2+^Fh3r|=t9Qh4ZXLsdf@2C6R2);Wpy8N?1s%t9'
        '95!&)z+n?-O&qp}#3VWjPAcfAIH{te;iQI+j*~hTDAd9+0}CdOnOLA}3(7E!Wd)}dEUP%JVp+p!4a+)C>*!FZjgtmCCQh2@SU73H'
        'FwEkxg0l(^t2nFTu!gf54(m9pW7)uI1Is2(n^?AR+TyJWBeiv(B<B#?cJSlBMh)5Wcknu^A$wB|b$$UBHr3F&s3Cie)sXYH_v|{T'
        'A*Xi-{<CVx$^S3#zfwbT%_lm$yQzle)sRi7;-(r}riOaY%BC7xts2VTFGce0+*Cs!poa4AqfIrm5o(Bf%v-?(U1HI~DI$Tkg5wH|'
        'qpjk&infO18rnLJ>o}w1pn)?6&M7!(VxZ!TiE}CrS{P_JV-bTXEGjsqU{S>>6^j~9X;{>8O2<IQIUNRJ1_u?Kp#+2`DB(05)X}D_'
        'RLVfx#BmdC3&$;-qau`>Tm}YI$|8XS0nA}Q6%3p*uxR3xNfJoThyo)s@)=a7yMCi8vVv$;ylh~}#M7;`^I7V15&RkKO0quJXU&+&'
        '5tuJtX4~B-;WOsD%|@KMp)c-byWFJFimQwq5p$bf8i>r2A5mBl*_NS35<VM})(KI}l#3!W9wjVJMAl#Po+e?<kG*Qp7^VAWyV`CB'
        'UUb1{wT7IWwklCrbz?Ttie&l4u_~d>eAG)7mW)1)?pSsA!oat5xpb){hk+uM)5`%j@Dd^!%YiD<7!9jTybS&dUIpiai}_UTO3!3&'
        '$B^gyVSQxTM2@^SGMjRB+yd-YugDB0?&WPS{SBa1dGF*N000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
