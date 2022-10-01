# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/array/Integer32.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.031425 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Integer32
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
class Integer32_1_0:
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
                 value: None | _NDArray_[_np_.int32] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Integer32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int32[<=64] value
        """
        self._value: _NDArray_[_np_.int32]

        if value is None:
            self.value = _np_.array([], _np_.int32)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.int32 and value.ndim == 1 and value.size <= 64:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.int32).flatten()
                if not value.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 64')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.int32  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 64

    @property
    def value(self) -> _NDArray_[_np_.int32]:
        """
        saturated int32[<=64] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.int32] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.int32 and x.ndim == 1 and x.size <= 64:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.int32).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 64')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.int32  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 64, 'self.value: saturated int32[<=64]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Integer32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.int32, _len0_)
        assert len(_f0_) <= 64, 'saturated int32[<=64]'
        self = Integer32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Integer32.1.0'
        assert isinstance(self, Integer32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Integer32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{`t<OLG)e6rO%Jga9Et6ckzn9A3j)5MLvfR;=Se1a)V1dZsVwE_xo--IHRhvMMgLV%4qkR&m*9nV*qm{(`#6GCTi*'
        '=gv$XV;CTigi@2ubf3p}zI*QNp80a7%*THnEp-0)v1U8W!ldM9ERBOC{voI&tmIc4wPquWb0+!ly*zDI^H$2fX*ZdCBv1b&f0RXT'
        '`SqYiey<fwR)cz}nZ~s^k0)6vNYkKQ`l6n*36@^DEV=7XvNVeubr}`7^Ih-ykpvA2zsR2?AM%4dPvc4}XPNw74q~+&B)Ro@%#v`0'
        '%}zfI^1#m(MSf&Jy5c4Iq3;5+lI2TQpU9(6l(m0p!#+z`jn(rW-T*qwE0%oZUOZ7}VQ<a-XhVJ_&i$lQOoB&Lt3j6gwMNKfbeJE!'
        'vjn5kN}rMsm5bU__*veSe7~RNK|Ku8a5d0$tHO5>QZuN=d0Rr6@9Vkz`>Hiv>V!Y~Z9N-EE;<Ho<VD9pQ>CJl3f1&0NhbNJrA4n4'
        'rS<3kyqA2}tvK(t@*dsxkh$SEnshh@fn@DkrIEx{$w!gZ8r0I9&cs(umIiqvU1^@}SEHCVI=aRWeA=j2gPhf$7^<3~B2!kU6I7)5'
        'J-1s)5~S@lk+we>BrPU?lSObvR*A0nnsJk|4&4pv6YMT)vOFF{>49Gh9#YFG;a0~OeWtKH!s_&|7T0O>)CGlM!R3zH?N$<~e9%;E'
        'L4e--G&-O3Ea(Evp3PdefdQrfyL+#zYp2f#7T5yZUfzy1K5%G_uyZ+|EObBg#5mXiI|c0O`dn3Ocwih1!7c&2`*6uhwmnbHfnnG!'
        'U~iA_$TMSM59}4NZ%rNYkbU&I@?iw_3E1C_HOaqA<sNwMTo{G@0uDZr19{1JXkA!v01gUxZK==1<@I&v!y$N0z~O<MD1!V)UI-Un'
        'hr<Hi=<64G3GdAp#)Bj9hJd3_<x5c%bL^#Rz?*PXfY&=;Z@n}Y9HZwNj(2gqr!iM`-`<dV@D>~waAK+EsvS`MIk{mq;B7b|;M6ns'
        'gfcverr38jv^JcCQv!-h>!c?^ow3s!UIX5NqJT5cy-v!Y__LeB15U#k0q0is_5@)TSMTrnO{)uM;hccdy81v_lyhNIIl*}-3Aos;'
        'u~$8Bmo~i~T!4!LF0Z>6lu3D4wuB#Cg3AJ~u01Q~2>asFdAYV_T;K{^74Ys0^^CG9_xhG{g=_GxfEz3Cmtv=H^p1IN%Xz?cxFO)?'
        '3-^u?DF6Le!W-U$n*u%<d=9TtjT`DLe)!7x!Ta!mfRA3Pzl1^<AHUKyz=!aWfO4<bqD69%J!}T`j%4myr?8;ml!gTzr*teBIAvhL'
        '#3>WUEnKj0+{OhP#~mUugPw*n8hSd;=;#?ZW1wf^jEMybb#ThUf{jx)7U<f6GR$FF!#NGhI?m}>HgL|svWashdKBv7jD?<!Gd6k-'
        '&Nwg*3plRff`;QdF6cOJ;DUkUCN7v*ws6kEvW;^#mK~gPM61F`ZGBCW^Deq>bnjoIhFtYKc$3wTyRC*gzW@u{YG_l`kh{TZ$a~g%'
        'b`#W)*S`b*SvBN!|1a>rQbTIZCpx>kt%jD=kV{#`Z8fw;4fUUuZ8fxBHPn5-6v?-DTMfO08tQ%@ZL6WJP(##X(TX0^B^Di=B@*ar'
        'IIY1nx;jql=o&a}pljl^iSs6oSvYUuqK0EOMmo;hxTxcpgOP#r4l$U;qK2~?7ImD}v1s6|fkhK%O^i%jG+_+paZJN`0-$V4r91=2'
        'OmqpAN?GXIIBlcr;IxB_RD`g}Wno0691=JX!6HUf!NOS!i#E>MB!Se7D6+WKok4Na4;xj<3$j%S_~@!Rs9$M!C#*lp==W$O<3oPP'
        'nkiEwuu%TWcl-C_hb;7)jWqY;P~PSve%5HERYs14`OP4YBzM$D5?3VOai@{R5AP`JBU$9y1<9>%GnQtO57&YRSzHU#pc*wM>Au;n'
        'wwqCqoDW&8q2{TrN)lK7lufh}ReojIO4)XI08ABD4MeTpuyx<^7`Sw)bg`s{fihQ9%~3xJG9sC(F)PuSjH^uk8vPOd8I__--KpBu'
        'zRBF4J3$!6^@%kTIr84%E@5@t65Lk5$c!G}?zX-3H^udlxB4Cc00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
