# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/array/Real16.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.062168 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Real16
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
class Real16_1_0:
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
                 value: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        uavcan.primitive.array.Real16.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[<=128] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.array([], _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size <= 128:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size <= 128:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 128')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 128

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[<=128] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size <= 128:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size <= 128:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 128')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 128

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 128, 'self.value: saturated float16[<=128]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Real16.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Real16_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 128:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 128')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, _len0_)
        assert len(_f0_) <= 128, 'saturated float16[<=128]'
        self = Real16_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Real16.1.0'
        assert isinstance(self, Real16_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Real16.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{`t<OKjU#78U=>Uy1W^lcr(QBvqP3QPLz;lQeawn83yDNriM;cxF)0l*E`s^&u$AkOwH>E@t2Y1m*$Z0A6(ArI%iM'
        'HSp3)FTM2ay!6t`UP`hZH*x+>Ff%p;lkeT%dFMS+KEC7Xzy58eIzQ1Vf2`81RC89-2|T;%{mm{_ot#x})ci)%3!OOH_iY%o%3&*T'
        '{xs%0@x%E1&+$)jHqxxRU1R&nmOWaw>p4I0YF_A#IypNC?6KT^$F5$v5l3lj)CrniqaM4d$oRf@|1c(rQvZm5j-x%69fpBdYK2ZS'
        '{vqB9(z;U|X?H!RTG@cI+p5^1ZG{QG=)@M`38*+a_Px!sJoB|v9|_$rlG)Ac+Gjacr{>hdUcN2htS>i?cHONu>~M3IJyyvJt!k%8'
        'Oc{n)wws|<YgC-rJsuq`u7xLIxi8s<#Kg3u{vO|tqr+A+wCfc+s63izg7ehuk-8VQDoNo7fn5%n&L-1*w|CDuBJIZY>-lSOlBrdS'
        'c5!XrE_>lvOykj^UNY-JLSlE3jHvIsdea-JJC(2Mp)=wHo0j9AqO@zer%6gux@RXit7?_1T=(1>JsU8YsqpvXINJLMFYJ>3Ef0H{'
        'BgJa?ab#|lq&ZeAHL6}Yj{4x#8ccq&#BY2ju){{MLAP#|U5}51dpkPvWusoUL#O^k*MyA3GjQsB*0St>;9jd*wS%$8Jauc-uC|=`'
        'pK+GbqFHk9^vL*vqmJFT>m$y6$9F<+D@Z@`UbUHW4*04w>3*H$%5bg@e>Jbp+nwC78&c`WNX|#AYA5j|CB7*^a__2iuKd)<g4Eue'
        'wmwG+se<(GSWfPZO*Ya<7nJVB?Rv~c2CtEJugCKYkM}&$k9N^+L3_KlbW&^ImVUH{_6pj+DKF3R+<~XY&_3EPDAU7x@R`1JfO(}u'
        'kJVud&-Xo7JRPJ%f)00mRkrU<Vvjs`EcMZ0K}Vm6fvs#i_CmSn2ptvF-;K#6`|-{T$I~(D7j%3}Ozgq-6EBsQ-l5}y-rd9(TRGp!'
        'm(E8g=v_hYJryr|vCpYjszE2|JwaxVTS4!?ayB|erl8Z^Jm%A|CzU^VE%oSqIxXnTTFpoHAYth2YpX#Y&>2DJp1CU=VX`;-e)w8z'
        '(^)zvD7&`KG)M9&JOA2i(1(;2^wD##lOx#w!nWX`^YoFRiyM1;hI3{g-QP>wR+lc&MM1e2;(?<$=JK{;qDzz$lwW%z^7D3O+w0L~'
        '$_u*s!d!49$9?=p@X-~zD(KqdXXPU2&aa)9>u(GTeN5K`-FPX^IGSTWd81hAI^7Ud*m%EWJG}8b=F>NhgFc~xpqnqv9cSS9TW<w7'
        'eM&b4-QM~fUgH{t<Sc&n*6`6Sx-IC=EAh)&ILGI2bq(|x-4Qgf{x0OVO^fBB)AsFpM`Cv@NXba4Na?IED1(fQjEam-CQKQo3R9;%'
        '@-p%&@;VJ*K*oTI0iB8{$|$NR>NJdD8N(`ub@JiM@KyLajbmKKxQcO|1cVHsLg+MwDH&5LrgWOYjEor-Gdj&-PR5*yIh_`;AY(zr'
        'f=)|VlCh*>Nv9R8$XHRa!Z;<Q6r?ny3}hr^6l64H444v31*QhmKwd&#L0&`Nz<`7S1p^ue3=}046%;iT4Gc>dRxqq#*nls=SKw>#'
        '4U9_|S1_(&+<=fE6bKE%z?6h31ydTP49rNFQ81%n#=x9}IR$eX<_s)ISWvK_VZp$Xge3(_8kP*KNLW#@qG81lt&+o9afk);pOH?x'
        'fBCP`a_Qu+_-)p5=^ZWC;W@LT<+er3r4z)jRm+*r`j*%REoW}tga27AXLkO7^#7&hk~N>{?Cy@1Thns<)F#~TXu02Mxy@%~N6Wpa'
        'mg~M>vTV!jXt`I=a^3Hv9WD1Jv|Q(1$h+Qhf9(vBmXX$3Ng%CaRYSjwex3T!&m)7f$jZp7$m&!;K}A7EL8n0s${18JsM8RJWDKbo'
        '(#eG@!&TwxX!A#=HrgspU_!=(iV2-2F)3qG#iUNtn3gfEVp^wJ%*vQmF{{%&=4H&QnAd3$i!v5fEb6q3Wf{vVmUXN$D4kZZ%9tgj'
        '6{Iz!4fIRsSJ2Pk4P^NvA*&#(p&+54pujf<1|<wC7}PLmU`WD{f*}n<23!fQ0#}1;pe>=Tpsk^8U_!!#f(Z>11|}s;DwxzTX<%By'
        'w1R03(*|ZG%qp1GFl%65!n}fc4f6&TB`hjf)Uaq^Rl%}^W&W*UnTHY!xTHVlYLV9M|3#`*X_VtA6}L)u)b~iY+A588o8Uji?vi`3'
        '8SSwujvqKl`>_)L679Dhcx|U*`Hdj7yh?m8I%qW;t)T3%q3T$^9lCL3B$ujJilbe{M$>B-li7!HHj*yKk@j8F37T=VuV(+)^lFvB'
        'F1w9U9{XeEG2gYTmnu%Jk#xOVrK(r90%xREP0DYy#5r2;_UO67BW-J~*AhR_?bPS4<np<s3mb<?1G>+0?It4(l1?~d81>3d{EPda'
        'DEG&<T@I^bW{@nk$>yXXZhGCear376*GpIP*9sTS3(4h&*uCx+y4}xPn>wfmigu;q)khxdoU--vD9xoi=9tp0&2rlP^<H<2a=!tH'
        'e<O^^AOHX'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)