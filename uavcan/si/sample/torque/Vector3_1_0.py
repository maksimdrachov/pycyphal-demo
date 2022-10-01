# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/sample/torque/Vector3.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.334152 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.torque.Vector3
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
                 timestamp:    None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 newton_meter: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.torque.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:    uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param newton_meter: saturated float32[3] newton_meter
        """
        self._timestamp:    uavcan.time.SynchronizedTimestamp_1_0
        self._newton_meter: _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if newton_meter is None:
            self.newton_meter = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(newton_meter, _np_.ndarray) and newton_meter.dtype == _np_.float32 and newton_meter.ndim == 1 and newton_meter.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._newton_meter = newton_meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                newton_meter = _np_.array(newton_meter, _np_.float32).flatten()
                if not newton_meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'newton_meter: invalid array length: not {newton_meter.size} == 3')
                self._newton_meter = newton_meter
            assert isinstance(self._newton_meter, _np_.ndarray)
            assert self._newton_meter.dtype == _np_.float32  # type: ignore
            assert self._newton_meter.ndim == 1
            assert len(self._newton_meter) == 3

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
    def newton_meter(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] newton_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton_meter

    @newton_meter.setter
    def newton_meter(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._newton_meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'newton_meter: invalid array length: not {x.size} == 3')
            self._newton_meter = x
        assert isinstance(self._newton_meter, _np_.ndarray)
        assert self._newton_meter.dtype == _np_.float32  # type: ignore
        assert self._newton_meter.ndim == 1
        assert len(self._newton_meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.newton_meter) == 3, 'self.newton_meter: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.newton_meter)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.torque.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "newton_meter"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            newton_meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.torque.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'newton_meter=%s' % _np_.array2string(self.newton_meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.torque.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YaS#KQ25hf||CUsGgWl5G=jw6zZcFb$3l@ljX=n!(+S_?WHA%`bDGtKP==Sp`E$u(dgen=n!17rYA0R0621pfpB'
        'F`PX5JwRaOC9i%=)ojo1Ql<n@UrirX)zwvB_5S(f-~Tf|QvJ)Xr`<pYq2p?<Bn#yy%nP~W`bm@~S{h#F^N)<me3L2uxSR6wdAa;q'
        '`DwY7kGnC8VE%f>_IwsQS~{9VDeN|h`cuZ8kGK!gdYMnTdt7Om#HAR?CqJ_C^OBCzk-wIomHDj8j8W3d4A<o!K=&)W>aQyE@omY&'
        'VBpP+8!*FMgD#4(-k=!IZ&>GyjJWft8~Z{fvHXMwk6}O?@V69`V!HN3%z<@r#%^DDl^>~+ku-7-{8)GrYuSl;@P2G~hpVG8nsq&C'
        '+>pl|BTCu=FMXzs8zljFc{RWIpjL$2oGqBUk5d?$zmyNl{JaZ3#sO2ou%g4vgQLwx(pQP*ei8>|e$ovRzkK@Nv5}F-f|EFlJg!Kx'
        'LxxsqVgxfpusu#vrZo?Uma)%?P9jd20uzd<E{WhXHblm-zFKLV8B}V=L20672d0;#!<}2zDhx33nC8nwY7+1r2{9olR}Ge?q4b%7'
        'J9h}G@iV1RPk#$q$~2#Wiy|H;ibM8j1KW305)HKL{`FPLNCb{?b&F`ut3`eSdUXm1m2n3~)t-d2Rj$a&`V5=`oZDkz#?ecYkeKgb'
        'nBc#iFxl_<*Pm~0HXtNqUk2bO_Zj&3&ddxU4YKxebMt6qVL9`X%#gLUR+Dr&Q~DO!7t$9v1yvE7u0!sU&5cUu&|dI6gWOSMKgq%X'
        '41ongvN+~G*P1CAc6%;BA`oeG-&+V9Yy)rcMw(#Nh$PdvsxlALK?W)a18bm|A4rH-Y#@(`ucVgR=^bV(gj|q*W9x34EX9c-+wUzC'
        '$b=YTslcAk6eLBKV!Un>uM0(r7E{&@6IR_ZToh1&Q#t;)zA6%-`yE)U1q(yGVNAD9$Q#x2o{1ek2vo#jpqHbje-Drpiw4sIW1w(0'
        'hKnH(MD3JN2&eL?tt7@WG5xv|3*wrUZqSx^Q@lk-u%5(XuXHA#v}yap-?U4yoZtK{SINt!t9*ld!)WZr$$spV`Gi|JROWBgq`(hS'
        'NH`?3Ba|@pu*y#s*8YfQJ`G3qaa6<nwv}N%A6+TYGwo#_&liSx(Dk}Kg2huTiOXVLG%_HRfP+yeCmxiC`6+it9`L}$i*jX9w)3;D'
        'PBP_lm<YL>GN6lm5+RgcnNL3eQa^ZrqtAh!M&AY^eFBvNUd=~rSIZ~>-$b$p-)YzHrf_qOfJaH0Ur93$>eyAhlZ9x0K)A4bqQ|qq'
        'Lm0X;zjiFwI;+l#gRv_OvfF|ym<At_4P0BV<ssb3Kia+eM+*ckVDbPRBnrp@V~%MIHO`=Z&3>YG8&!emA)D0|Rz@Llj5tzopdbme'
        '9wk(aFt7t3LUsg{90WOufbRlp7}M8FKogKvP0CeC?!lTwHFU~-xg&?t9{R;DcaWOB5JGgbPMZOf!=cT~-(^1cOKCo+z8~>^PUk1w'
        'BrS9DDkZubc?sMPMD;%0m*vP0p*R^d;Xy~5aD4%6P>SE@rysBYsq%Y^1jE^O7KYFbUY-@rzm-e0RcH_TdfL-a(y7dYb4D`8E(ZcT'
        'Kw%O)9b^kCrK7lSq@ZIKPauvJ^rZbBM;tBagdLx><5L!=?f4AhL_ufm`Z>g@g3cqJEa)k_{xsrjLC@IvvxwsbJ!kbSAf7AedBigX'
        'y?}VCpcfJ63i=x2OhGT%{jXcQm#v*ER?k&y?+wH&1-*uNxuDk(UoR*@yj0K|h_4m&O~i`@{Q=^Ig1&`#zMwxuTqx*G>(?UU*@7-v'
        '|CSL?7xYKg&mSYs7xb3(w_(rgSij#!oG$2!^?wy{vY>1B9P2h78}>Zay`CuOrajkf8{d{a-<{sQ(|0WX#NtmazH9Mk7JqK>7Z&eX'
        'd}>ixJh1r8;tPwPTl~V}mlnUV_^rk7dU$_o)C!ksVW}2cwQ#Q%p4Nh>g@amnRtqm`;qzMfq87fag>P!%+gkX}3K=~1pg}-eL8iB3'
        '9`ZaiplLIBelF)D*vAHs&MU8Y{3^w|@Fd(u#_#dNT^u_4;+%JR$nlwGpTbx3>1}A!=Ey4OiUhjinpk`WUPi0~52OsAr0?d7>l-U;'
        't+n-y&CT^zbFI~C-f69_-d@>QZLM##HkzxOch;I48@;XtML!KM+LZaybW3_dJP}WOB=I}(@er4sd&pC6<nfF&=I-KFCOSj>LW(L<'
        'A^oF>;4l8PtocKWuiE`M&c%G+B(WQDcnLu$#Xq5qio0m{YjIZmPy8zrTZiJkw)mB}w<O*dzZO({AnuEHKBgtKt==yd5PH8^%KVJ|'
        ')pE2|iARU1{P^?veQEg27vNQbZ8|=dh%s)+!_fNh2hXwET(L_>t01%>2rUdkb$0P@u5t7QjJ_C*?ji|)Zx{pR{2vOPKgRJ5000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
