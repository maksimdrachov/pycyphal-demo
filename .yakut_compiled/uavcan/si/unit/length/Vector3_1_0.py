# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/length/Vector3.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.240297 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.length.Vector3
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
class Vector3_1_0:
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
                 meter: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.unit.length.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter: saturated float32[3] meter
        """
        self._meter: _NDArray_[_np_.float32]

        if meter is None:
            self.meter = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter, _np_.ndarray) and meter.dtype == _np_.float32 and meter.ndim == 1 and meter.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter = meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter = _np_.array(meter, _np_.float32).flatten()
                if not meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter: invalid array length: not {meter.size} == 3')
                self._meter = meter
            assert isinstance(self._meter, _np_.ndarray)
            assert self._meter.dtype == _np_.float32  # type: ignore
            assert self._meter.ndim == 1
            assert len(self._meter) == 3

    @property
    def meter(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter: invalid array length: not {x.size} == 3')
            self._meter = x
        assert isinstance(self._meter, _np_.ndarray)
        assert self._meter.dtype == _np_.float32  # type: ignore
        assert self._meter.ndim == 1
        assert len(self._meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.meter) == 3, 'self.meter: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.length.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.length.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.unit.length.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YXTTc`*6kcSxiKvM2L1W}e@xgJgu=u7XtI5DhKzTEzGcDVOxuxxFc1%d*K_f{MNjUxuf1{_niwo#ZGMTpL((iod'
        'eDk&Z>vy>{c<hs`V46i9(OgLy$uBgBxJSY?&QdK62fMUqR34gK@sCBu;T)cyz%i`Z8IsT#?T>TX3u)qM>E($uUc{5G5#BxzO{(f('
        '=Shz%Ez<-<$<FPM*5}|)`K9l00(Oy5W0VYX!!>+{Ns#_Jft_hf9<ec$n}ktAiE;SsqY2?k(E{xKw(N7ZHNg1V9bGMIiSUTWJTaqW'
        '6R>1T#?r_hdMvb~l$xtq7D*rt84>~hD&h;NHY83N2l3E8*trOIVcuJ`Z95ZkQu+qF2$E<+6Gj!goahJUiD?%(&Y8RTP|?sJml`>4'
        'kJgyOKC3q>wN|a(SYNNVnzdG|x!I~#H!6*4tKMien$`8qTC>rpfV(RX>;j_8Xednq{<JNVAi|7KFA5(6Kn~3HJ=j}sq#4q=huaYa'
        'cABIa*wsl%bP)$>Btx((+dNK@RtNq=#ude(85226LLsr!qG|8#@{Ak#f4>{#2(gP-=y#`+M-f%UbtlZ#qfyS`C#?CaXF9;j%OsWw'
        '_y=x5`))Dknv_Qr1N<rHSvu25JMU*S8O&`b4_v62u`@9@Tmi<i6bmUKmDH|Wnq?9cLx~)N*b>Vc$Aa-p@sJwM;MCqGhi(>0mMTLe'
        'gN|J$I?Ywc(GYQxQEa-MbDu~C*zg@xWPit<o@32ZFHs1ea4xZ1OEEptGG;ghBJJTmE5afZG<w01UZ;sXK)Q+IT`Uf-9}5PfXNL*~'
        'dqYdC$Eg?(M^k6-j+E?Gy^81B3C7Ln3K3KzM&-nUD0(vFa4NP%M|h$-pj<S>#;`%d&g@XeWYYboeQ0grZz3C-!JkKd+x~%ghwpn#'
        '<Bv%9{s1r-q$s%r000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
