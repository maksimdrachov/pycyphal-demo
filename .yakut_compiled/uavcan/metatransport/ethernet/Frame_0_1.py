# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/ethernet/Frame.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.082346 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.ethernet.Frame
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.metatransport.ethernet


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Frame_0_1:
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
                 destination: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 source:      None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 ethertype:   None | uavcan.metatransport.ethernet.EtherType_0_1 = None,
                 payload:     None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.metatransport.ethernet.Frame.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param destination: saturated uint8[6] destination
        :param source:      saturated uint8[6] source
        :param ethertype:   uavcan.metatransport.ethernet.EtherType.0.1 ethertype
        :param payload:     saturated uint8[<=9216] payload
        """
        self._destination: _NDArray_[_np_.uint8]
        self._source:      _NDArray_[_np_.uint8]
        self._ethertype:   uavcan.metatransport.ethernet.EtherType_0_1
        self._payload:     _NDArray_[_np_.uint8]

        if destination is None:
            self.destination = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(destination, (bytes, bytearray)) and len(destination) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._destination = _np_.frombuffer(destination, _np_.uint8)  # type: ignore
            elif isinstance(destination, _np_.ndarray) and destination.dtype == _np_.uint8 and destination.ndim == 1 and destination.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._destination = destination
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                destination = _np_.array(destination, _np_.uint8).flatten()
                if not destination.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'destination: invalid array length: not {destination.size} == 6')
                self._destination = destination
            assert isinstance(self._destination, _np_.ndarray)
            assert self._destination.dtype == _np_.uint8  # type: ignore
            assert self._destination.ndim == 1
            assert len(self._destination) == 6

        if source is None:
            self.source = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(source, (bytes, bytearray)) and len(source) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._source = _np_.frombuffer(source, _np_.uint8)  # type: ignore
            elif isinstance(source, _np_.ndarray) and source.dtype == _np_.uint8 and source.ndim == 1 and source.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._source = source
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                source = _np_.array(source, _np_.uint8).flatten()
                if not source.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'source: invalid array length: not {source.size} == 6')
                self._source = source
            assert isinstance(self._source, _np_.ndarray)
            assert self._source.dtype == _np_.uint8  # type: ignore
            assert self._source.ndim == 1
            assert len(self._source) == 6

        if ethertype is None:
            self.ethertype = uavcan.metatransport.ethernet.EtherType_0_1()
        elif isinstance(ethertype, uavcan.metatransport.ethernet.EtherType_0_1):
            self.ethertype = ethertype
        else:
            raise ValueError(f'ethertype: expected uavcan.metatransport.ethernet.EtherType_0_1 '
                             f'got {type(ethertype).__name__}')

        if payload is None:
            self.payload = _np_.array([], _np_.uint8)
        else:
            payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
            if isinstance(payload, (bytes, bytearray)) and len(payload) <= 9216:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(payload, _np_.uint8)  # type: ignore
            elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 9216:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = payload
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                payload = _np_.array(payload, _np_.uint8).flatten()
                if not payload.size <= 9216:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {payload.size} <= 9216')
                self._payload = payload
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8  # type: ignore
            assert self._payload.ndim == 1
            assert len(self._payload) <= 9216

    @property
    def destination(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[6] destination
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination

    @destination.setter
    def destination(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._destination = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._destination = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'destination: invalid array length: not {x.size} == 6')
            self._destination = x
        assert isinstance(self._destination, _np_.ndarray)
        assert self._destination.dtype == _np_.uint8  # type: ignore
        assert self._destination.ndim == 1
        assert len(self._destination) == 6

    @property
    def source(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[6] source
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._source

    @source.setter
    def source(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._source = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._source = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'source: invalid array length: not {x.size} == 6')
            self._source = x
        assert isinstance(self._source, _np_.ndarray)
        assert self._source.dtype == _np_.uint8  # type: ignore
        assert self._source.ndim == 1
        assert len(self._source) == 6

    @property
    def ethertype(self) -> uavcan.metatransport.ethernet.EtherType_0_1:
        """
        uavcan.metatransport.ethernet.EtherType.0.1 ethertype
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, x: uavcan.metatransport.ethernet.EtherType_0_1) -> None:
        if isinstance(x, uavcan.metatransport.ethernet.EtherType_0_1):
            self._ethertype = x
        else:
            raise ValueError(f'ethertype: expected uavcan.metatransport.ethernet.EtherType_0_1 got {type(x).__name__}')

    @property
    def payload(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=9216] payload
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .payload.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._payload

    @payload.setter
    def payload(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 9216:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._payload = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 9216:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._payload = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 9216:  # Length cannot be checked before casting and flattening
                raise ValueError(f'payload: invalid array length: not {x.size} <= 9216')
            self._payload = x
        assert isinstance(self._payload, _np_.ndarray)
        assert self._payload.dtype == _np_.uint8  # type: ignore
        assert self._payload.ndim == 1
        assert len(self._payload) <= 9216

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.destination) == 6, 'self.destination: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.destination)
        assert len(self.source) == 6, 'self.source: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.source)
        _ser_.pad_to_alignment(8)
        self.ethertype._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.payload) <= 9216, 'self.payload: saturated uint8[<=9216]'
        _ser_.add_aligned_u16(len(self.payload))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 73856, \
            'Bad serialization of uavcan.metatransport.ethernet.Frame.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Frame_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "destination"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f0_) == 6, 'saturated uint8[6]'
        # Temporary _f1_ holds the value of "source"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f1_) == 6, 'saturated uint8[6]'
        # Temporary _f2_ holds the value of "ethertype"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.metatransport.ethernet.EtherType_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "payload"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u16()
        assert _len0_ >= 0
        if _len0_ > 9216:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 9216')
        _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f3_) <= 9216, 'saturated uint8[<=9216]'
        self = Frame_0_1(
            destination=_f0_,
            source=_f1_,
            ethertype=_f2_,
            payload=_f3_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 73856, \
            'Bad deserialization of uavcan.metatransport.ethernet.Frame.0.1'
        assert isinstance(self, Frame_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'destination=%s' % _np_.array2string(self.destination, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'source=%s' % _np_.array2string(self.source, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'ethertype=%s' % self.ethertype,
            'payload=%s' % repr(bytes(self.payload))[1:],
        ])
        return f'uavcan.metatransport.ethernet.Frame.0.1({_o_0_})'

    _EXTENT_BYTES_ = 9232

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{^{MZEsXX6y8c-wiK{Xg!mRFicpMPTG|>kAyRM)W$9YmLSobmvwNpKL+{>uGc$MXYK&llvB@N$9p7I*_`$>vhD85?'
        'iHU#0|Kgc@?{>Rwx5h6vX?Awz%$f7@JkQy?y<aqk3hAFY5jTD12Od>i3Kod>SvBAutwr@XQbKcU4lZh$)N~^GQZwdu!=AZkKeVH!'
        'kA|#{=g%jsQDdQ3=bCBBLKR0+dt3vTA=loFOs$Hv!KD&WXrW*RZsqF@TP~D)KC$<#8KO*UDXNL)%D#*KyF|8WWli6V;DO(cXg~Ft'
        'W>mW{&C^}3OUatn9Gwws+`qxY6%EsFt24KQln1=dL!CS85=$&aU1-rji;<h55-TD1XG6_bxa{;dM5{v6Abrl3ix_E*DNXB<&n-M<'
        'j?K3mxoh4PJezYzt~~ec0)|VKW}(ldztz#FN!1LZr<m1*ZrXCc>7~^`S#zotZrd0m*W15abKtVjSrHcTYaXuIN2Ayp(#?r#)~it<'
        'YMAsKuSZx6jlFy$=91}1wv+CsH4xYz@XV0~9&;^rw|k7PV(c)1c8^z*AYih&-3Wa(Sdei0z>b!S4^<U2@1=DS+VYrNur;?Ba0N{Q'
        '=De1BoN3`<xtM(>SaZG>BRn1MDoNG(fIc(ibEQR?reM*PA7Nevi)X`GcrXIT^3{{@Oujl%E&_p*@B+2~PGRt;;l=a_&cax3GXYci'
        '>Oz{`tC_*Yb_(!Xc?>S$|MYGFL#Z8QzlsuBL#$kdYaO9ImaqEE>Ah)Ka*Gs{FaU!s*1-W}+7@^1{D#~4^_jk``1$LHOz}z-IzVnh'
        'X0N-m^YqqadKWI5XIr4cUP!K7GdgHgTu3{?f|h5zGq@~S&Fvzxi!=Ee&rR?7vB?Y85hN|soqr2u-}J(K9tg<XJG|%IOilg=H)%#M'
        '@8YO$Vsh&I)TSqHMz&}gtu`~kbRGeGh+q{yf)8LF?k6Y^KF5O8nC8A+H;3r5(<kbBNQG}J<}l45fCmAmF+=*B0rwGzsx^c2DAsH9'
        'Zg&G2)pHKT@g`~&R_tJ%ttwIXv2GAG@O#{>HDh4GSs%&kbTX+TnW^L}NF98>Euwh4KSPysvlUm^h!(P}IkJf@Z_FF_Tz{>0sx?A^'
        'DU4M*A;oAK0wKH(SIw`Bxtfv9tE84gN)e`r&zA*iDXBKeY^hWt3w%W=eBE`POeY#5iHb+i37MU)Ondv6KqwNR4Z+VS4DgJoItv1#'
        'kVIUQXnD&E8ki;+R=Op8F7YWHkt!z=b-#f&WI2-LN?Iq+?#^yht9j=8B3#)aY1`O7jBLjN7-!a~|0(r{k@~}q`Ypz*t&AT`>zhuW'
        '9i%^Mj^AQ9hj0dUn_ykFYOZk79BIk<vYVgTh}#DC=gK_}#@VGV=|6!g-~b!$s{d{>Ir+!tyK%mwARVrbFR*Zh?=>X)>1rzT7=Je{'
        'Ex@Jg1=3U4Lr%HMD}Q}>Z^OI`$gpM*F`Qvn&G=#xJM1fmng&8T)hTi(!D&dA-LD))Mw8e9=@n8Im(O@OML0ZgInKagcpGNnH+TpB'
        'hTjwTY#lzYzy^Fd3SYt3@C|$m-@*6r1N>+XrN5XusRTbc+I*aH;lkK?Zz3ZO(l2|NaO^~^9D$vp?w<{b=CZCF>`@?MJUpjsv7glA'
        'mk|99_!8wejzWh>GznLUgMnkujoC_h>8<$^EiGLuEmTTN=U%_DL`#+NvAN6LxbVy7s=fDTX7-nB{{Lk;4v)$`or5)PC%l<;{x<I3'
        'Ztp(Iskm+X=gc_9-FT~U=6T!pADQu8#MIp!Q=QItoH%TG{{Zl><otvS000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
