# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/file/Path.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.603877 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.file.Path
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Path_1_0:
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
    SEPARATOR:  int = 47
    MAX_LENGTH: int = 112

    def __init__(self,
                 path: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.file.Path.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param path: saturated uint8[<=112] path
        """
        _warnings_.warn('Data type uavcan.file.Path.1.0 is deprecated', DeprecationWarning)

        self._path: _NDArray_[_np_.uint8]

        if path is None:
            self.path = _np_.array([], _np_.uint8)
        else:
            path = path.encode() if isinstance(path, str) else path  # Implicit string encoding
            if isinstance(path, (bytes, bytearray)) and len(path) <= 112:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._path = _np_.frombuffer(path, _np_.uint8)  # type: ignore
            elif isinstance(path, _np_.ndarray) and path.dtype == _np_.uint8 and path.ndim == 1 and path.size <= 112:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._path = path
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                path = _np_.array(path, _np_.uint8).flatten()
                if not path.size <= 112:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'path: invalid array length: not {path.size} <= 112')
                self._path = path
            assert isinstance(self._path, _np_.ndarray)
            assert self._path.dtype == _np_.uint8  # type: ignore
            assert self._path.ndim == 1
            assert len(self._path) <= 112

    @property
    def path(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=112] path
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .path.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._path

    @path.setter
    def path(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 112:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._path = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 112:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._path = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 112:  # Length cannot be checked before casting and flattening
                raise ValueError(f'path: invalid array length: not {x.size} <= 112')
            self._path = x
        assert isinstance(self._path, _np_.ndarray)
        assert self._path.dtype == _np_.uint8  # type: ignore
        assert self._path.ndim == 1
        assert len(self._path) <= 112

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.path) <= 112, 'self.path: saturated uint8[<=112]'
        _ser_.add_aligned_u8(len(self.path))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.path)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 904, \
            'Bad serialization of uavcan.file.Path.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Path_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "path"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 112:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 112')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f0_) <= 112, 'saturated uint8[<=112]'
        self = Path_1_0(
            path=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 904, \
            'Bad deserialization of uavcan.file.Path.1.0'
        assert isinstance(self, Path_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'path=%s' % repr(bytes(self.path))[1:],
        ])
        return f'uavcan.file.Path.1.0({_o_0_})'

    _EXTENT_BYTES_ = 113

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?|pZEq7t5O$gXjww(YTBN>+ZPZqdM2<q=P(Rg8Nn4qOG$e>p(beAF*t^Z$?rC?=jw@Ay53Q(lQjysH-_G3GF##g{'
        '<?d#8o|$=`*;zkY`tQ<mtNvA2ib?9yEaDEV5}Eo##2G|9F?nH}@(`+XcfBnWUs~9k6cC<;wa4Ml(5+5!Epl9cs}!R|=xCtOaYuL='
        'sx}{ib;{@<Th*C+)AwhgztC^}9Uh13EEnEe6_*}dc!*#pq;a$>RHrr-Wa&J7ho`~|?kT70{S(}+6_Ze1z9-O%mfN6*UiQd(yq0qu'
        'GRQ&uDc%X`6jtTRs}b&4+1E}DHKadj4@0oW@y_yCd7jnbLcfj4Cc=51n-qe4uX=Z921IVr2Ci+<5;D~KE9{2q5_ewcRM_-+peJQq'
        'EhADP66GhMUsP{Tm-v9lX_A*8G)c%S{kCLswZA}+@)Po2;&J9e_35m<IXG78U;GZ$o8Kwlkaib8r{z_P+!Uc=CxN(09-B-hNYWPM'
        '2Fdd%|D6J?@W#$bI?WTQP*VAM_0ERTiSVFbxs{5hofb4T3+}(LU1piElb3d$<|C1n5dIC_e*3A5<(E@3Zlc%aU7?4t3k7&}Qc4Fr'
        '7l%kKI(%Cj<;D!F<}X(oMWPqnw)JSSIzy_KnIQlE0_|-*?YEm}iNeESA#~mU+hq)x(H)d!XY0wL{P|TLav!%*EP1M0D(cg;#8ZQ0'
        'wgMW@S8b$<n&U{0u3ULR@{en=5n%c5t)1R(Z|@H3|3LmKH>wY3qG4JV9OZSat=qe`0wSBCqtEidiiE7#Iql8qJFZu6eDQUl-m24m'
        '__|~|TfO`I_O0z7_I{jZBVigs{$4F!zkcHg462pq1_X~M&8Q*JU*ts@%ipAxy2N9a0+vCYlZGeNc{~P(kn+M<&s7?>tBc&3(k8%Z'
        'IPr$gGxW$*jBT}pBkr&sS<g`Xg=;uv_VL7Ho#%3K;8dPswbG36yO<=CLW*oX#g?XlQ^wfh+`<sG$MExMgx;r{k%-b!T=b?G(e>!F'
        'h{z9~j`#|f!eL65rVa)jsRY75^1=O&7F(@taEQqWF6#6cp)fZ=Th1tZ20Fockus&({@&)zi0w&WMrRX-?XObi0D-BsnR3kI+Q8T`'
        'P7~%b;UrtVwo0&0=^+8vwk{gin1un>&%CL<tTCRY3K>SI3G0$AGfCYd%naCAszg$V6b1@sA&V!qAC&`kE$Zw7l7o%a;9}O`SQnyU'
        '#8#sS!(sJIQ;exU&b;~?4<>dbQP35cm!=#_1jazQn6O0BF{aw<%1XMLFczMR5pqd=%DMys8mmqqUHhiP*gESq)D=eICOxDYMZ+x8'
        'Bv_{O0ofX^F=W=H0+`ZRp`)0y8l4O{XA4nl%M5tFGDUwia)+eE;iB?#Dt0ql5eF$Dvaur_XeJywdMi>`H-iC-!H)sWbaNx;vC8m{'
        'Xz){j;`#8i``i)V9U^gTtn=%5M*$&fhhj~`Hm!9O8&4^UjEC~-RD6+TX6)#3<cS#??S;}rikNkos;5>09qgOBtVU~QFg^wo7A2)K'
        'gyog`z%^1}OijHwHf*D}%{IShIE!*{QIJ>VwPt$UI5y)i?1(hQh%e1{T>T3Fm=w)2UdrY1QG7IbqyGUk7h<L#2><{'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)