# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/udp/Endpoint.0.1.dsdl
#
# Generated at:  2022-10-01 11:53:15.930328 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.metatransport.udp.Endpoint
# Version:       0.1
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
class Endpoint_0_1:
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
                 ip_address:  None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 mac_address: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 port:        None | int | _np_.uint16 = None) -> None:
        """
        uavcan.metatransport.udp.Endpoint.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param ip_address:  saturated uint8[16] ip_address
        :param mac_address: saturated uint8[6] mac_address
        :param port:        saturated uint16 port
        """
        _warnings_.warn('Data type uavcan.metatransport.udp.Endpoint.0.1 is deprecated', DeprecationWarning)

        self._ip_address:  _NDArray_[_np_.uint8]
        self._mac_address: _NDArray_[_np_.uint8]
        self._port:        int

        if ip_address is None:
            self.ip_address = _np_.zeros(16, _np_.uint8)
        else:
            if isinstance(ip_address, (bytes, bytearray)) and len(ip_address) == 16:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._ip_address = _np_.frombuffer(ip_address, _np_.uint8)  # type: ignore
            elif isinstance(ip_address, _np_.ndarray) and ip_address.dtype == _np_.uint8 and ip_address.ndim == 1 and ip_address.size == 16:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._ip_address = ip_address
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                ip_address = _np_.array(ip_address, _np_.uint8).flatten()
                if not ip_address.size == 16:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'ip_address: invalid array length: not {ip_address.size} == 16')
                self._ip_address = ip_address
            assert isinstance(self._ip_address, _np_.ndarray)
            assert self._ip_address.dtype == _np_.uint8  # type: ignore
            assert self._ip_address.ndim == 1
            assert len(self._ip_address) == 16

        if mac_address is None:
            self.mac_address = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(mac_address, (bytes, bytearray)) and len(mac_address) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._mac_address = _np_.frombuffer(mac_address, _np_.uint8)  # type: ignore
            elif isinstance(mac_address, _np_.ndarray) and mac_address.dtype == _np_.uint8 and mac_address.ndim == 1 and mac_address.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._mac_address = mac_address
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                mac_address = _np_.array(mac_address, _np_.uint8).flatten()
                if not mac_address.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'mac_address: invalid array length: not {mac_address.size} == 6')
                self._mac_address = mac_address
            assert isinstance(self._mac_address, _np_.ndarray)
            assert self._mac_address.dtype == _np_.uint8  # type: ignore
            assert self._mac_address.ndim == 1
            assert len(self._mac_address) == 6

        self.port = port if port is not None else 0  # type: ignore

    @property
    def ip_address(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[16] ip_address
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 16:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._ip_address = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 16:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._ip_address = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 16:  # Length cannot be checked before casting and flattening
                raise ValueError(f'ip_address: invalid array length: not {x.size} == 16')
            self._ip_address = x
        assert isinstance(self._ip_address, _np_.ndarray)
        assert self._ip_address.dtype == _np_.uint8  # type: ignore
        assert self._ip_address.ndim == 1
        assert len(self._ip_address) == 16

    @property
    def mac_address(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[6] mac_address
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._mac_address = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._mac_address = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'mac_address: invalid array length: not {x.size} == 6')
            self._mac_address = x
        assert isinstance(self._mac_address, _np_.ndarray)
        assert self._mac_address.dtype == _np_.uint8  # type: ignore
        assert self._mac_address.ndim == 1
        assert len(self._mac_address) == 6

    @property
    def port(self) -> int:
        """
        saturated uint16 port
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._port

    @port.setter
    def port(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._port = x
        else:
            raise ValueError(f'port: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.ip_address) == 16, 'self.ip_address: saturated uint8[16]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.ip_address)
        assert len(self.mac_address) == 6, 'self.mac_address: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.mac_address)
        _ser_.add_aligned_u16(max(min(self.port, 65535), 0))
        _ser_.skip_bits(64)
        _ser_.pad_to_alignment(8)
        assert 256 <= (_ser_.current_bit_length - _base_offset_) <= 256, \
            'Bad serialization of uavcan.metatransport.udp.Endpoint.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Endpoint_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "ip_address"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 16)
        assert len(_f0_) == 16, 'saturated uint8[16]'
        # Temporary _f1_ holds the value of "mac_address"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f1_) == 6, 'saturated uint8[6]'
        # Temporary _f2_ holds the value of "port"
        _f2_ = _des_.fetch_aligned_u16()
        # Temporary _f3_ holds the value of ""
        _des_.skip_bits(64)
        self = Endpoint_0_1(
            ip_address=_f0_,
            mac_address=_f1_,
            port=_f2_)
        _des_.pad_to_alignment(8)
        assert 256 <= (_des_.consumed_bit_length - _base_offset_) <= 256, \
            'Bad deserialization of uavcan.metatransport.udp.Endpoint.0.1'
        assert isinstance(self, Endpoint_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'ip_address=%s' % _np_.array2string(self.ip_address, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'mac_address=%s' % _np_.array2string(self.mac_address, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'port=%s' % self.port,
        ])
        return f'uavcan.metatransport.udp.Endpoint.0.1({_o_0_})'

    _EXTENT_BYTES_ = 32

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8D=Ii+0{^X+TW{1x6vsEo?&cnHBizAI2!S@nG(agWB`GZunubQ)-YRQs519#G+wx_btyC!pfv9AuBQgCDed8nWHL5=Jy`Q4z'
        '?4D$^A?ZsSY4e{sbLPw$+rOE!RsHS4Sf%|}o=I9k7KFB&iB$1W{lvXc*sdQpk~mYjFy;88JT3gZNX6q;BFtNJ>4o{(ER;1j;td!-'
        'TkxjOBfBATo~Jy@k~q!nB1r6SqacY@l$&zMZHhEgab#qr9DGXcw}w?%-)r;2l%p=s^Hh07E;922L_Z*}9WPVX?kN!l-F!yefal!J'
        'G0F180n^izw@f*EPi>0eI}xqtas^GjI~#XJC>kQlDcAwIB&lksTs6UC=1G*P^+*Kwqg<?uv^U<U>#5ug+shd?1ey9g%iTsC2qTY|'
        'b8FjyaGHG=##V6%AI~fE5YlzCoJRpqgWZAN6ka(DkrM8!yk*#AS#`ZIGv)ktx?N|;Jm1?l<=EFM?>vM@(4}<C0XI%eX&n?KYc;$$'
        'R6cBaRWxFF7&*Ml?-P;oJWjituDiZe@P4FSPCpch$kqOS{qA$fT`qy&p$A16^0c+r31T&QSP1j0Sztpt^I+#yx1l1#wy?oBu`!4b'
        'v<NvyWqs&c(X5|z0JUGUD)noq1De&zK1e!5<HOV+=`6`cQ3o{}qy9MRsAd!7cZlqhG=B<pShHywpFy3_Y?k~ElYI_#TC*dl<C-0%'
        '@ne+Vanz%loj{${>?G=>W~WfcG&@cHXHct}S+xFH)Ki+BLp`q9N2o_MJ5O;gpiXHvPkCLW{VY(tOQ<!?E>oT#qh8kR6VwIG7E$Ll'
        'vr*4$b_MmEW)7;Q*;Uljnth6TQnMw>;~MSfI_jKeHz=Ra=sDb^{e4b(-J*SdfjXkumz3Xa)VgM0(Z26cp39y67r>a<OyDrWa|Uf&'
        'y72JBk+pI}B`yzwRAc~4)eU0!mVbXNg>`?;BD)novvRP=ILj>+wcC-%e~i=Tme<OK6{mqntp!i5TOtY+k1p9G_t%;?wgZUF;;FDw'
        'kw6bl5)oKDTU1%w>)O9~6`6|GEp%FJ@FW3CZ&=&F9ws~N$Qe0Dtz+^ewa&01Y02~Q0-O(Wp4H_=dAU6#7o|f!OY%CkZi2&-yw!2I'
        '-Q`Q(VUApe-^zhBRSux3LNwL)&@`}zrYg}?A)1DXraI9yu!p7zqG^n18refrooK2OP5neug=jiLG|drBhl!?HqG^U`nkJg2h^9%R'
        '=@8L0K{SmMO=CpUDA6=RG!5^eX^?2D6HPUusY)~r5Ka9=Qy<Y(A(|Yb$sw8?qRAne9HPk~njE6ZA(|Yb$sw8?qRAne9HPk~njE6Z'
        '(S>|TjctTR8{FSvNWL!btghVsFYNSw)ZI^cvim95$|@EXxY{hj`sAB63k_COG(3^ELrj!oYmfyH)LR?KnezDlcX%^a0hA|CL3ZES'
        'u=H|<YgS-A`FG)oa%NYB;(D!4@q@8n$tn4Vd?Wvoe-?1n2MDvzfo1cioN%9ErQu?tF0AyRoN}|cNPPhVp>Pup7kN2|5-QJ>!)s7<'
        'ZLXp9E!>TLSD?&!0vW?WHQwOQGt~%E?#s9d{iNl$63N5G0Ip%IcnS}$Wj7V;a0$Zl-Es(K*E>ZThS^=F!EFzPnklEYOEufEuiE&a'
        'OpcYuj4OEtS*BPFK^{%z3-b%Sf`t`)0axI}6f|?^^=FCj)idR{>jK;CfBwK_PjBjjiU3A;`yIX;NBB6Sed`RYfUwMf1hH)F&fKW='
        'RVp6_+!)<9Z%jbz|DAFb>fEHWE5rKQhv*g@qFZ=~%9jtophbq(cVK<DW8IjCAmraW(sM9R!ol2`{vMp(?>oJBq-Xl__Vm?CpIpX&'
        'y#a=b{l<`Y`yaHCjXy99000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)