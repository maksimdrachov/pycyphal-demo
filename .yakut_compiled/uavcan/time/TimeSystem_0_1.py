# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/time/TimeSystem.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.459564 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.TimeSystem
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
class TimeSystem_0_1:
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
    MONOTONIC_SINCE_BOOT: int = 0
    TAI:                  int = 1
    APPLICATION_SPECIFIC: int = 15

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.time.TimeSystem.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: truncated uint4 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        truncated uint4 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 15:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 15]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.value, 4)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.time.TimeSystem.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TimeSystem_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(4)
        self = TimeSystem_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.time.TimeSystem.0.1'
        assert isinstance(self, TimeSystem_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.time.TimeSystem.0.1({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{@j&ZEGAi5I#3{>|C0ZU=!#YQK4<p7O&4ALP$zKIM<{-F1|bBODTmSw5z$3>RoA(w6?EMXg;(MP-!9RU+VAZPw8m)'
        'UYrDf=yBX>HJaIHo|$>{>-yjSZno-=zg5n-<#|Fa7|C+^GfQ(wXr_x&Tj?P9Ye&vhnX3$pXC;J};j`!AmvF~#P{j(g->le4##G{D'
        '0m&GDj%L<D5&RZC0b`|BLA3nlck}hj&~NqEeh<%sze<^NMy8bm8-B!)7l2uw3V!3Ugq*KHv?*tfQ5TV2<X#$CNGDJ5#P%~~<x~Oh'
        'DF;(9uV!?Wrqa<I)YOU4U&r7XvyK*;Ll8Uu=4cTpx+Pt-9YzyowDwzg8vG8mjw#LzKOg8tm5L3&al-Nn5v)_Lv*23+cdz@cu2#{<'
        'EkTHFadW<Ux4$ml6Cd<jF}S$Z#MwC<4u<35px32Gy+QX8eK;JBgZRk9p;p>yB{LE$L9A36kW_1zv|lqxOIWiqFaZPcpcBjyuEDC?'
        'j%0$VDO#BWq75n7F_0WsX_MeD(|INzF4%^%(twS{eTD0-r_A9V%NMzcU4La_SQd9J+8@u?X!mQK5VN!?Ci(FNOnkoJ;L`Y@hbe#m'
        '&swV$3u)B+P2|Ao0<(-=_$3j}mG;5j9;oD09?KHAWQjJ@z4)~EiX&|tX>?55V*xciSec?Eb-E<e$}y=d5(Pw6MGA)K2|*{LEufWK'
        '0y$Cyd`|uT{d=9=&OUy}oz8>$`vXDb82_MG*C0P-vsj9WJVP(pwB)(qi?~bx<8kAg(NPU7X*V-wo3d3FmL|et#8q9b&{fVOd>lsC'
        'oOe3nAnA-S&ZU~xIW-`-oXkCw_A(@5#r`3-Dobq~o|<4&7+@Cb7-3;>D-n;%Fk<AxF5@^-%LtMj-(%;faYzU&%UotP|JYVyS9Io0'
        'BJTRN{r}MoI|rlDlV0~=+#3$)(dbdP_qf-M6LIfg^@?3vLMA86;i!Q`?3FrJ`c#q9=n@H%@CKN-_U|syfZsl+Su~wB8W>R#aYK9|'
        'J`rDu`{G;ib%koe0S5!$4?Mi^*J;f#jTBPJ!@%F5R#zqiG~_@_hFak_<6kb*;IE93xU*5*eTmw%wuj>P422CR=Nb;Al?BK75&8t5'
        '%UL!n1<Q9i6gv3#%PPghsex&g$Jeh!61^`sdW}*PsX$F!X?D^{_LDf&!9_jWrh-`n7V8)_^+aY6ULdo7jL(q>*sx$~mRF;*Fj_>F'
        'lN9O}v&dE5J8`c-`NV9n?VFJTcdE^C((a-BFctd^y&56n<WwL<=g-BSG?j{7l|)fZbIk11g(9ug7h${CpM!t<p>$8`=Ob83ufIff'
        '89ccth@BOwMp}`VL!=pRmzeUfjJa#Gx<xM24AJr+e)8{(ngM&`kkHXOsPded+3QxZ`)9b*U;oRdc!ictgwWrrQp~fE3YT%g&f;P-'
        '-cDHLh`$|`n5p`f9aL%T*W^FtWt3y<2LJ#'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
