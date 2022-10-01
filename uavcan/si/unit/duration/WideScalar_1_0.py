# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/duration/WideScalar.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.231336 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.duration.WideScalar
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
class WideScalar_1_0:
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
                 second: None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.si.unit.duration.WideScalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param second: saturated float64 second
        """
        self._second: float

        self.second = second if second is not None else 0.0  # type: ignore

    @property
    def second(self) -> float:
        """
        saturated float64 second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._second

    @second.setter
    def second(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._second = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.second)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.si.unit.duration.WideScalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> WideScalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "second"
        _f0_ = _des_.fetch_aligned_f64()
        self = WideScalar_1_0(
            second=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.si.unit.duration.WideScalar.1.0'
        assert isinstance(self, WideScalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'second=%s' % self.second,
        ])
        return f'uavcan.si.unit.duration.WideScalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{?YXOOM?&6utwUnbK0Anu-kz5DS<t2!7kyRUpmg(qY8#+91n`-HAnR5+%;nT%<~L0iu#6kjDI9j_1KGMH4BC?Q_m|'
        '9{#@kdgt%=b{CgV{BYRV$+m@_+~`f~e=$|-3SIZBp`UzkDLyz2<6MV%bl+|UmoC!d7wLIAjJvusE3kh&n{{ovV)Dh@`B2z-G{N^>'
        '@q@SSv^K37Q@pF!Zk*sWHH*0a{q_1HEq9iS-_wf}?`spn=&L!nDgBggtLtB<6nBrjYwfn4d)k^{bjU^C7CwxA<%3^?$6H5jZ^D0D'
        'y00rAbnCja(4^%PfUM0F^s2WmHIL%^CpY0atoRaaPqPWySp1g0N%4`Mg6XUo?W;h40M5#s!E9!m6F(bGod-0*SdOmOfbk>WSuC(D'
        'r6?(;ObJ3Umq=m8iDZOIiX~!{3t1{85qvq}im|d3yi_HYObUf^3=v2wgoxr)NrAX3Iah)bDTI;=OUxN!`IK_Zs3J@NJfj3tB9tm&'
        'ixoI41}Wf0lvByED3w5v4I?fE=a?vhq#%s55}^`NRZ;@M3`t0)I8qFpC@ldyXQPA)@FIkiOku$lQk<6*vJwj2LW|J4B7z`>8I#aF'
        '6icC6i4`hwNy<_wOgMtt5fNB1Oqc>(p;8|HTs6CKZ*q0t*%a?++t(>B;Ml~2SGc9C%@uE-r{>e<;RJVX-7vb^1ZUIB_>O+&&z;pn'
        'KL+h>I*t$Z)X!t>z|cB97`V~6pFgdy;5JV{Cg&&l^a2>P^EnXnJ0Klg?t_*2dGad@SKRb#*bkd}Gc>0C%(_*d;s?WAwZ7J)JDb~_'
        'eoJ78-n)`jif>FF`pMD)zTAi_#e=Q93S6Kf(>;aE!UNry2?`xu7c&3XzIN$lbJ#qFu~aQ!e{!RaEla^MyuMHI?Js=z>T-Vy+iRV~'
        'H+4Ux_|a`3(`Hrm&=^$m6dDEX<%+)^9F*RVTea=!y78dk<|w{<VyyMu+5eoHWwsvAEws6L-3kb6)6OpanGTmv{+cTI%?wvSX?b_9'
        'pxu@4vXEh6&huhFiy5Y!qwi^VKA7(EPjoz2Q#Dt`KirTd(i;T;00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
