# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/node/IOStatistics.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.670065 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.IOStatistics
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
class IOStatistics_0_1:
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
                 num_emitted:  None | int | _np_.uint64 = None,
                 num_received: None | int | _np_.uint64 = None,
                 num_errored:  None | int | _np_.uint64 = None) -> None:
        """
        uavcan.node.IOStatistics.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param num_emitted:  truncated uint40 num_emitted
        :param num_received: truncated uint40 num_received
        :param num_errored:  truncated uint40 num_errored
        """
        self._num_emitted:  int
        self._num_received: int
        self._num_errored:  int

        self.num_emitted = num_emitted if num_emitted is not None else 0  # type: ignore

        self.num_received = num_received if num_received is not None else 0  # type: ignore

        self.num_errored = num_errored if num_errored is not None else 0  # type: ignore

    @property
    def num_emitted(self) -> int:
        """
        truncated uint40 num_emitted
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_emitted

    @num_emitted.setter
    def num_emitted(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_emitted = x
        else:
            raise ValueError(f'num_emitted: value {x} is not in [0, 1099511627775]')

    @property
    def num_received(self) -> int:
        """
        truncated uint40 num_received
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_received

    @num_received.setter
    def num_received(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_received = x
        else:
            raise ValueError(f'num_received: value {x} is not in [0, 1099511627775]')

    @property
    def num_errored(self) -> int:
        """
        truncated uint40 num_errored
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_errored

    @num_errored.setter
    def num_errored(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_errored = x
        else:
            raise ValueError(f'num_errored: value {x} is not in [0, 1099511627775]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.num_emitted, 40)
        _ser_.add_aligned_unsigned(self.num_received, 40)
        _ser_.add_aligned_unsigned(self.num_errored, 40)
        _ser_.pad_to_alignment(8)
        assert 120 <= (_ser_.current_bit_length - _base_offset_) <= 120, \
            'Bad serialization of uavcan.node.IOStatistics.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> IOStatistics_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "num_emitted"
        _f0_ = _des_.fetch_aligned_unsigned(40)
        # Temporary _f1_ holds the value of "num_received"
        _f1_ = _des_.fetch_aligned_unsigned(40)
        # Temporary _f2_ holds the value of "num_errored"
        _f2_ = _des_.fetch_aligned_unsigned(40)
        self = IOStatistics_0_1(
            num_emitted=_f0_,
            num_received=_f1_,
            num_errored=_f2_)
        _des_.pad_to_alignment(8)
        assert 120 <= (_des_.consumed_bit_length - _base_offset_) <= 120, \
            'Bad deserialization of uavcan.node.IOStatistics.0.1'
        assert isinstance(self, IOStatistics_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'num_emitted=%s' % self.num_emitted,
            'num_received=%s' % self.num_received,
            'num_errored=%s' % self.num_errored,
        ])
        return f'uavcan.node.IOStatistics.0.1({_o_0_})'

    _EXTENT_BYTES_ = 15

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{@j&|7#pY6u)4Tw3k*}(iXpfomS8*B-@Jm2WUY|uT7$9RRkGkXW!jS-JMzI%iV23u|FsT1{5;>;$Q2V-Midr62XIG'
        'XZF4KdEY+o?Jt-99BlU5U$|2@g)PdAS}>B8@+Hel$SBuUt*vwr!?h!4Ja^u}v!;f467Ro?KgB^<r;1f5f77!GXDU;=fNbyJ$T26a'
        'libE|nNGl1sZ|ucu=(};d=iJf;o5KURSa8{IcH?<9oYCif?g2Lsa6c@pGzo<Wf*;0FvqA%v0Y?d8(B#wC#bRgTv<6*Q0yrOV=({B'
        'X^ZC4(Gt|yi8xH)oLNUJOf8C=;r8JID4AuCQ1&#5Fr&3!<5w}<q}DN2FjK4o9s69Yhb`qR3TW=2h~W|~G>>8DnE--<91PJTVm;?z'
        '?Z}s9L*}{!ltZ6jvxqp?yGX^hxII6;H5`by#k=B8=jLj1V}JujSwwL+?EZ&~h2H=4(WPRHHl2&VzR*)rF@-UwmzD@N0irqg1~syN'
        'iU4MeJ5s<%D)gjPisfFbeve?uh(HJ@pdriv;o7T|dOFLhE}_BzSu)#g5un)VdsSi{#MZ#&NOG3)nG1<VBr}y3Qa%v2S7=7_rXz03'
        'i-;TI1M!~N756<hzknJm!cv2d!|QY;XHd{u8%Jdk_rncpwKp74Py($Pwl-|0M=A3dt{mdP%nsAr6Qt7G1LW#+<RQ+%wTk^<WmOo)'
        'g`VKOZg^7*R$?}lj^Ul!=cVM>wy`gh`z5E*dZQaK<V+f|7;dc&S@tmdFiV_|E)j5>3T81hgY`;7Fp(VMvAFx~V6E5tlq}duEV$Hw'
        'F(@1qPNb^6d!W6;M^fs*SvhY6cGL;xI`y{DR%l-qL}`S<86TB;n)UZagprRQ?jrRUhD2Hf=ca97;u$J8q>^Qc&EZ-VI|P-dct6EK'
        'ee&~1pO6Nau^p&d3R_ayokSHfVWo%8cxqVPDiNp2OE5a?x2$Vb>}t3<AnQ~5Q-NJ<aZ*`RpvEgD)i_JjnU`4k_ZRDAIm}p8_wRcQ'
        'S3i^PNqaxS>wKMr*Ql;zAQyqyrph(89lQ1vX@JWr5&WRW5<6{{OKF303>63Mad_j96$OTPMoAoqC#R>!;npLq5|7onkl{*)h$Kl%'
        'cg6C{bI`tNPvX0aG%>1uTqevkXZ&o?w*K+=I2aE8usMDZ>Mj9Xm_ElcS5l=tiw8DKht0HWaR!ogpTewWs{Ll{<KB7E1yU{0z~-VJ'
        '9*Q6FZ&2Wpl1{*9U!QL~L#5fO?PY)VwatB={S9Wn4Y)H0000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
