# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/node/port/ServiceIDList.0.1.dsdl
#
# Generated at:  2022-10-01 11:53:16.180176 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.ServiceIDList
# Version:       0.1
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
class ServiceIDList_0_1:
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
    CAPACITY: int = 512

    def __init__(self,
                 mask: None | _NDArray_[_np_.bool_] | list[bool] = None) -> None:
        """
        uavcan.node.port.ServiceIDList.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param mask: saturated bool[512] mask
        """
        self._mask: _NDArray_[_np_.bool_]

        if mask is None:
            self.mask = _np_.zeros(512, _np_.bool_)
        else:
            if isinstance(mask, _np_.ndarray) and mask.dtype == _np_.bool_ and mask.ndim == 1 and mask.size == 512:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._mask = mask
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                mask = _np_.array(mask, _np_.bool_).flatten()
                if not mask.size == 512:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'mask: invalid array length: not {mask.size} == 512')
                self._mask = mask
            assert isinstance(self._mask, _np_.ndarray)
            assert self._mask.dtype == _np_.bool_  # type: ignore
            assert self._mask.ndim == 1
            assert len(self._mask) == 512

    @property
    def mask(self) -> _NDArray_[_np_.bool_]:
        """
        saturated bool[512] mask
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._mask

    @mask.setter
    def mask(self, x: _NDArray_[_np_.bool_] | list[bool]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.bool_ and x.ndim == 1 and x.size == 512:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._mask = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.bool_).flatten()
            if not x.size == 512:  # Length cannot be checked before casting and flattening
                raise ValueError(f'mask: invalid array length: not {x.size} == 512')
            self._mask = x
        assert isinstance(self._mask, _np_.ndarray)
        assert self._mask.dtype == _np_.bool_  # type: ignore
        assert self._mask.ndim == 1
        assert len(self._mask) == 512

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.mask) == 512, 'self.mask: saturated bool[512]'
        _ser_.add_aligned_array_of_bits(self.mask)
        _ser_.pad_to_alignment(8)
        assert 512 <= (_ser_.current_bit_length - _base_offset_) <= 512, \
            'Bad serialization of uavcan.node.port.ServiceIDList.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> ServiceIDList_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "mask"
        _f0_ = _des_.fetch_aligned_array_of_bits(512)
        assert len(_f0_) == 512, 'saturated bool[512]'
        self = ServiceIDList_0_1(
            mask=_f0_)
        _des_.pad_to_alignment(8)
        assert 512 <= (_des_.consumed_bit_length - _base_offset_) <= 512, \
            'Bad deserialization of uavcan.node.port.ServiceIDList.0.1'
        assert isinstance(self, ServiceIDList_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'mask=%s' % _np_.array2string(self.mask, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.node.port.ServiceIDList.0.1({_o_0_})'

    _EXTENT_BYTES_ = 128

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8EGjr-0{?wh>u(e{5KqD-xx66ZAW$BSTV8>Z4Ua<UlZK>`B10O5P_-Ybm2cOHt?cct?A>b)sS<o>MOsU&iunhswo=~(sr~yp'
        'v**AaC5@u|)}DvQ<C)*&UghzVp`P-`Or@<*hmq%Nt|W`(T~?2{=Lbn6O|;CoHDe1rk`4F_*IFsJkL=m|_Def$27DRETv^d$#%^aS'
        '53*eGZk2vNW({!hYR;Mgi@i7rxtAs?^KNt1lmTB_xG8mJP1SF5rDYPMx4}=`_ajStXz$ndzBMC0%Q7YFdB(N<99-`b_cJYP`WGdS'
        '!so#Z`ytDipJ9aN=q~0;v6eLl7UdQXZ}NB}6LYxLeXTK{N4&w~%sJa7mQ-QdWD_(-ZX`*>S={Ys#IMWDkIG{#?S%*frZc|*S+Ziv'
        'Os?!WKr?S1WVcX+Y5B^oLYThJSR67Hb~@V5>t+Z%r7VzH%iikgGZnucX=_gJ#Q9tsLe5@XTQhn?X6@VGhNX+w?D3P-8nT-c-D=d6'
        'NCwu_Zt+F}S;*iKKTf$~S)w}YCJ+)HMqD=gS9!`a`EtEJe-ncj*FbUKavnuYwO-T$XH6F6+&;9^w71Z8xO>HK$k<)G!M4h;K}>2M'
        'F?39OQMsp}eGc~^_7$|^*8Ofh;Bc_*oK~HD2(enwVJ9C!94P3h+aE*hFX&#k-skkjo&AJc?|1SV;{JjjKpZXTLAO8Y{2p?6*zLdK'
        '^o}^YqliZedd$g>Bi0J~syk;2alD|!o&Or*L_uG7@)L-Y1wHBPPa#ef^tAJT#@%NckrebS;(>ymbNX)}o+;>g#A5}WasE9Q_blSM'
        'f?ja;7u|W6+&wP4INn4&U(hRvCklGi-Rmvq@0vUBZNzH@eFyPELElB3F6evC|NDrC3;Kb(_jPCYVf+3$^cmkuSzK}q>_LGPc^zv<'
        '44X=W=}ilz6DCl}pRNf`WE}D>qIjyfhNjmf!_5#r<+|jGlojZaHI;KRGeex(Y_56ekwq5ia+}rLyK%X1;jo&i&L=Up@UtG97Kfqn'
        'Yj+^FjhKf^amF{e>S7IXl8%d0;;cCLpbWS=KesYBzqIz572ld3D{h$MI~@wQgjn#JU1U^UEjyD%J3hf?XkD=YcY!9Vi|!lbX3v$2'
        'mn^ak=7*bF2M_!8R-4~3s&B-kcq|^~Kx!doDqt`$?6%qKuOpZG$ojqv?XsEhb&{)qgCOF5%7C)WAVMVT)(ow{*x6da-A6zIy|X~%'
        'cYs$RuCWH&)UpvmbRucOI&B55RIq3!1inE|&+EWHzTz9u>TvvX!UyYt_6&lj#VG`U5m__YHHo|n-bD|SXEP+&nlG4!5EXL0ZY$bt'
        '$n(=V5`j8N)`{EhC<yHhuL-FM{4xT`YQjt)fqUs0E$?yy+=+EYzL1$9I%#l%MWdQLBpP@dYmUGy;AN>P7H{y5qh^*C(6@{O#X%<='
        '24zOpbDY26rz!EpQ6G&{m1IefM4lDr#ccbzFNrIzmP&42VPPoajsGw(NUy?VPTOKjt59zX$jBezpG9!=V0ou+#E2Lb<6;6vGZex@'
        'F23(93h~3X_;FeMBz~S2zldMOZ{m0Hhxk+cC7y_<m}&7hWL5kFJk7T<$Rm(;#Y{pawg2-_zThkbDCe#C?pY@g=!7%07wfa#54+s)'
        'AT%0QWc<>ZgyRxN5<D~hZy~O`u4wa#u6MaQw2II1e}ikl-z*0Yy$1%JzN+Pb5(~5kQ&_<i?hF-O=8|ia5|EOYNYU8)7YE+2X1oai'
        '00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)