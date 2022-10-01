# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/array/Natural16.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.601628 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Natural16
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
class Natural16_1_0:
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
                 value: None | _NDArray_[_np_.uint16] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Natural16.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16[<=128] value
        """
        self._value: _NDArray_[_np_.uint16]

        if value is None:
            self.value = _np_.array([], _np_.uint16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.uint16 and value.ndim == 1 and value.size <= 128:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint16).flatten()
                if not value.size <= 128:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 128')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 128

    @property
    def value(self) -> _NDArray_[_np_.uint16]:
        """
        saturated uint16[<=128] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.uint16] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.uint16 and x.ndim == 1 and x.size <= 128:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint16).flatten()
            if not x.size <= 128:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 128')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 128

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 128, 'self.value: saturated uint16[<=128]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Natural16.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Natural16_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 128:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 128')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint16, _len0_)
        assert len(_f0_) <= 128, 'saturated uint16[<=128]'
        self = Natural16_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Natural16.1.0'
        assert isinstance(self, Natural16_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Natural16.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{`t<OKcn073KVC%d%<9AH{ZJ#<3kbv1$4n=3BM~3Kh4<VVyeArWg&$iDnRf2E(C16$qd#S}4E(eSoHbmRf45rIuQ1'
        'sa@5bmRf45W$%#GFScyUmSnV*K#23+z31NZ?t6UH(VbBL`7E92{DfD$@k+B&&6-Wycde@XSF2RDvu3$b^BPSzu%od5yTEUigO+dq'
        'dEB$3sp#g<(N9q()Xch7V|%(~jg_r>*7Mz(8@OY3*7AL8Jp06Aj8(n+C<>G2nC&;+Mm=&8q49n1c`71_5`T|=j>10E3Ig9PwF0{t'
        '{UzFs)uvMvYQJ~wYGsSfakF9tmKnqp!%MrsV_s2s;d_f`dFGFHeKc@>8_(`sTEA&m?V4Q=dhvFlv$^6Z9C%i5x}$Zw@`rk0kJ|pu'
        'cztHc4a{mMT|_A+Teg~kS!-16$hjDvFKz^iVcExQLu}##CH@vYjl#2LGqCCv%dcz?G}$VJ$2gK_mEB-GqKWWK&t(1(7pF_!x!fh;'
        'T%n|scCL~XhjgyTXw@uLn^AaUV|iP_d8NUx$5D9VcW%%v+IKwcEiY8ehR4TXw;;{&TB%WW%UmSbwFVb2;NAb$vwbUQ_*+HN&9dY2'
        'mOA&tbB`PKvK83%7rMrajy-+5&SxdV{->U_s#VJ$f6h}k$E<40j{Xs4C@GpH=V7lHc}87$YSl;Wr?zJY?rxNRG;3CyOUr;lXVQ5b'
        '$4YUmPW@_boi{0dU^gU^p%L$Dt7^q~l49S4Ai4Lhbl&;Y%YxM2oVGbf3aNth?pThWjU6`9NEejs;f_6LBZJpS$2ajj!{fde`q42u'
        'F6czpmW*@t@9IZ=bVAU{9dUV<=T5y8L;ZA8P^!oG^ecVo6xWr`JeP+pJU{SScsfmI1fA{rs%$?IW6!-dmImmopz|-}z*e?h*i$Sz'
        'N9P3%b}^}VKi=Cjo-WX!po_b5Vh^@odZW1X9$gf4c}Kn2%JJTR<9Kw5E(`kLrF_|oeXhJ!4tk$H5R~rKR?vrU9gVI~TF}*Qob=1M'
        '$C*FcmwfagT@`d~Bj>g~h%0n`-*V7LbWPBWSMCZU((KK?AMa~!x=uF)Wj5BCWF()moBN)FKBkPIPhNYSj9~vy4}=HZq)!Ch+S=P|'
        '95b_he{UaHUiy@73CixN4vb>Vode}Ww<#+qw{au#=k4x+=c7B66LfFSwO}OU?jH(2x=Z&2J$U}C+~U}|jq~#G(74cjdLZc08`X@_'
        'jQ#9Txza;=Bq+aizhpXf<2&Z_L+3%CQC`p&Z(KW$!1yoU32*wGz7X`)?&t6U=g7xr@#}ZSkG`a@1by>X_2noW<2Ubg4fHjABdD->'
        '7xHb>VsU7<J*(c4$Q=t3G7>5hI_nEcAtfWFBBfIrX&Gr1X`OP&$;he5=~O^LMnOeEry`0niYkgajbKE^h>8)NJa{rZ6`oELn2<4{'
        'VnQbYAw#GTI?Z54#*B&?o#rqnV@}1KP77F&v7ll>rzI@OSW>a1(+XB(tf*MgX$@;K)>N!9PYDSH2@MGYDG4bBDGezDX$ffsX$@%u'
        'ISDxhISn}j1qlTO1q}rQMF~X(MGZv*BN9dwjA$4!;7RZlcp5wd6A~sAOlX)eAS4I{LW3|cBVk6tjD{Hla}wqh%xRc2upnVU!GeYb'
        '14|N?6f9|2GO!|HMZt=O6$5J$))cI1STjVcWV2TMmIZSW$)xkA{~9fqjQ@&1U@ezC(sG?Tr;fDTfoQp8%y?h5T>4et5(l8=(mVIy'
        'e^$$-JO4lW|I%{tny+<s_ejfaXgU7W#<f4va=+4YJI~6ImfNeA>)tOJwxy1=+*@e5?)TA=mOBhB*SQOM*IUk1XNaVXq|QnLNfqlF'
        '24xKDG>AbS8I(arMn*+Or#$j1@-p%|4Pi*ekcuIlhA}K-SjDhT4jdVd3P(qqUoy4PR%sHGGA30_>NJgM8Ph7Jb(+Pjj9C@4I?ZEV'
        '#=MGooffeuV^PJTPRm%9v8-ZQr&X-VSXHsAW1UIqw2pP=EFq~NsUc}#P{N>sK_+h?!!HRL1sM%_33&y1elRd3VMxJ{h9LvP5{4BF'
        'YZx}*NN^N58XN;{32g;!4Q&IH5+)T)YM3-IEn!;0w1#N|vl3<%%xai5FfU<V!Muif1B((C6)b94G_WjTS;4Y~WdrL9Rwb<RZw;$F'
        'lvu#U{W(VqwQm0}RLx4G9EFLfRkFf?ZQW+GG~VrF{}eg@a!xnHKC@zbz8$w8E733EN%IG{ZC6aM;RmK$iJpX~&1R$Jmu)swZPT*?'
        'Ckl=Dt?HJd@K~|Yblb&vb}Gt*(w!*Oo;7X18HN2d>&K>BtN2#gX^ipM8!wN0j#a%~v1^UEYuzeU-LmQ1qpfP3eygR;XuaEJ=M3B0'
        '&RVafeP*-Sp1qsRW#dL{6vUn50n@RXOwx~=*-T^1E!)vA&a(4w=azG)+tIwYqbqu<XjLk1ee}6*C|e(eNsiSqN0e;sl*rE1lWy6w'
        '{{aRf9v5IB000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
