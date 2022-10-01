# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/magnetic_field_strength/Vector3.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.387534 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.magnetic_field_strength.Vector3
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 tesla:     None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.magnetic_field_strength.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param tesla:     saturated float32[3] tesla
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._tesla:     _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if tesla is None:
            self.tesla = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(tesla, _np_.ndarray) and tesla.dtype == _np_.float32 and tesla.ndim == 1 and tesla.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._tesla = tesla
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                tesla = _np_.array(tesla, _np_.float32).flatten()
                if not tesla.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'tesla: invalid array length: not {tesla.size} == 3')
                self._tesla = tesla
            assert isinstance(self._tesla, _np_.ndarray)
            assert self._tesla.dtype == _np_.float32  # type: ignore
            assert self._tesla.ndim == 1
            assert len(self._tesla) == 3

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
    def tesla(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] tesla
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tesla

    @tesla.setter
    def tesla(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._tesla = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'tesla: invalid array length: not {x.size} == 3')
            self._tesla = x
        assert isinstance(self._tesla, _np_.ndarray)
        assert self._tesla.dtype == _np_.float32  # type: ignore
        assert self._tesla.ndim == 1
        assert len(self._tesla) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.tesla) == 3, 'self.tesla: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.tesla)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.magnetic_field_strength.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "tesla"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            tesla=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.magnetic_field_strength.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'tesla=%s' % _np_.array2string(self.tesla, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.magnetic_field_strength.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YaNpBp-6(%Wh7paBXEXi`oaYWM5w7Cs6a^fTk9YS_lV?m1}IEg#e-NmT_drMU{$uVFcJ|qx<2Hb!;fPR91f`5X6'
        '1a^+T=VIiNtB-!Kr+S8zNdeUNy0-V~E#Is8+sS_p&kj}p^4HRCpo7qHHCK{_@>Ax8+;RORN)s&&FY}p4MrFRq6o1@JdHK9t{Ji|E'
        'T*yb=m_;zZl(8M3#g3MaW>E^eBi4zzk-obnc^J6bC?0o=a6aO`Nz`hYPq;f=X_>^O7|O>#vhwqi4%4B3l%JRRw9AZ9(#s6j<)1;>'
        'F=qBxmHFr<DjS$L<p#_!*PzW}q&Fx=^BdM$BO~rS>c+lMNi09*!DATE1};#FaWPq2B2IyJamH?+JI;<&$w(Tx19r?kiM53L2k*s('
        'cepz2v}xCq#tkcfl(Yp_`b--)N&>L*T7L0CeGqPQHel{PPN8f5UOp`I^WaSu2TTPA58BT>xY~3ieU)hLCvi~bC*2_N%cuVv85(*l'
        'IEk~!<BB9(<iILTj9`Wcw!=xvwB`ZPGWI#qNyG_Lph7X#B@ukahR7J!S1XM(g@@X4I5bhR1JeuA;m)mU6*`!BO!Gw|H3|5Z1fP(U'
        's|HKcQ2NY3%pHQq_?c38PJat($~2#XKoO4<#s8W?Y+(DAN}|E(x*xvkFcN`bT-_p?^J<Zwz_~hwi^{kIqiRRO-6~ULrF{x+0mkjH'
        'Fym;YNl46h&`t2)R+#Me?CZ}r*BjsxvMU3yllu&8e0yq&kOo=#q`7|Bv#^|bNoL5(N~=k_oGE>a><Z}%oPsimP1hlJ$@*G#=7GIn'
        'cLuqm$ZnE_0Vo0ugk*8deXccAGVJzDfJ7kD=)Se!HrNK%Vnmvt)rch1xT;bQ(?JGD5C+=dV7@28U$KEaCcctdYNvOZjSzA{`i+gd'
        'ZL$z2hHSpONFWnp@TCHMK2wksS&II;O}s7?DQZkvH%wR+V+a&*gHsv)xDFMG(EJW8)`Ep0Mi|qr6Y@s2yr*J|4;&S780h7w>Bj+*'
        'V%}g{pbr$z#t;|+PSj2bg)o~>Y$P$3iRss!m=o8nbc43U>*5VMg!Lrmd!;k}q)po&{-Irp#r)>STqQ57uJR4yhThnYlik=U^D(zF'
        'sLWrjNrCUBkZ?$5hbUp<VU?dOtnCrad=jqg<EV!DO)JBEKD<<-W!lR;p3fcNLD%c{7#DA`Ag+j2(a3;M0uD-{oOn>~=d-}MdpvM4'
        'P_7Khc7E2?Nv3=b6Crm~26T~+BZSf`^T`Lm@_P?(^f}Pe@LNEnPoPr3s+ovwYZ(P#n@D!xJMH@26e8CMc$Ad+)im><j$Oq&S%~Tf'
        'gbTaJdOQm}gsv;|>ql~}v+OK6=)2M&yUn?RX|NI5z_s;S?n6xe)$Y|lY9OcqlLzP^Q9uspb4+8XaR&8kb`!PTs0u_M&{>7BQVNM<'
        '#G!(N1ClW7Q9{KC13mB|WJf^Bfs>O6_%5)DF@3!RP6D#3Nx3S?9axj7hEBOJx8#Aehkmim9i(P21Q*?`(`LZraB1`McbT91oira*'
        '-;a1dr}GnTl9o9+?hxILyaeI{UcC?TvK;v#6eoiwJm^Sct}lQMO7W-s^aB<kRsLj=U^v^(!VtQ_%d?{SMY%v*h4!GYr@a$OI+1yB'
        '&q&7D<v?J2D2!vLgKWV==`ijaD(HyC6Nn=PJ!!v35r+#pX2-|v_=LqtJ3fUtR?um?{uJUwL1z$87IfCGKaDtD&@*=aEaGTE&)IY4'
        '5YH9#JmQ&xUO=2J=taa+1-*ngRnW_J|0`DS6|3i}J?EO$_bTGmf?h|wQqb2BUnwX-yj;*5h?ffbI^xBG{tWR#LEk_;U(lZ;&K2~g'
        'wQC;nY(W>SeT#^v3;L$D^B0IS1-)hMZP@!d*6z0uCkwh{?O#S5FX)QB$Ex+mn!QgI*AoR@xA(ej{oAtlyVHw1ecR$ME&j^lI~IR!'
        '@i!KKYw@1Nrxu09J&VsQzOeYE#jh-WZSgyc-&_2lhxaFjt#G*(7HXkY3-@Z_X)TCa*sFzSweX@AzO03>YT@fz_^uYduZ171kilaQ'
        '8U(ZzWO_U1A<shtnlyvw=VCsDeQfaPyn4*zS1HzoC*dYCevcpS;?Ut2=Zwokj?Xmv6uy>EZbF+jhgLyXB+wOC#QZa`65sFAWcVa~'
        'C!b$kTUu$YtgfxEueO>ityc3+YkB$h(%N!sb*;75TwcGk(p+2XbuB3RNqEtw%$KHH(i7r|c-kY0KZ;KdaLKucJcVBfM>EohyNz3!'
        '=p5h|QdFJ_>0d+yfAME!%^zC)yWRKWC^Sl-7qKY5h5jk-qQY;)S@D1IpG<7*i+9`N_u}4ycu%}9sQ5tK7wvpROXyd<-!5f->6l+H'
        'Wq!u~emUH<#G`%GcJxjCzI5>R7vOz@4Ld%PlF@_6$e<Q~`W$(hE4Jxy<&GA(qlNCMydeI|HIBZ3(HDc!ZKUI$45Q1O9|0bP4C4$A'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
