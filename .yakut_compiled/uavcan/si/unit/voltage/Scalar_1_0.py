# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/voltage/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.280416 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.voltage.Scalar
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
class Scalar_1_0:
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
                 volt: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.voltage.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param volt: saturated float32 volt
        """
        self._volt: float

        self.volt = volt if volt is not None else 0.0  # type: ignore

    @property
    def volt(self) -> float:
        """
        saturated float32 volt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._volt

    @volt.setter
    def volt(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._volt = x
        else:
            raise ValueError(f'volt: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.volt):
            if self.volt > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.volt < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.volt)
        else:
            _ser_.add_aligned_f32(self.volt)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.voltage.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "volt"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            volt=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.voltage.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'volt=%s' % self.volt,
        ])
        return f'uavcan.si.unit.voltage.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YW%T5$Q6dmL#h=f4g7$Yl%h3!0gaM)@xn-QFdx-*sPu41ZU^&|D@Oq-C%LL*5fnsEJ6f52PJ;2?(HbltkobMC1x'
        '3%`EPH!eT_xU89BDk6q!NtOIe6U8Hv7Fk&sX*u}yW2;?io#yZAlEVe;oxv&W`bCn{4E>KBtx}ptMn*1|HmV9`>4-<iDOFU1Um+FO'
        'Mix1UhF|_LJzv0JZqWD!XW-WewN}f-S#IDX+&0qRAn=QQ$rYQ8vPu}Wl-MxeZRw?!nY6OPh`W7NQ2Q^MHIhh66wgOiz+eYUrqo!H'
        '6^w(}_78?v=^-t8g}%e!LKuy&@D}_wF_z|xYIeQQcdV1q5z^vVXndk+Y7xFcTKdy7*6>d|akJfPcjEp1POsbU^|}YWR_jGGZuL5G'
        'FYdPX58B;0ZbIng60ztP0?ptT2rE+X4ZNg&>l%?HsVDn61@TmD8U)CAsd-8*XK?QClM^}SjFg48L^3$?o5U1OryL!Mlak{2emVS<'
        'OmOre%3(YVw--p)+;iN*dt?}qtY`F-kr_igqNva=>$ENfRnHjD3h)n0mnfMM%|}j!_Ooqa_R>T?;O`iTc!Gqm?^HzKHzqQQT2V6!'
        'YXuwF-Xek;oKf@KhCNp@<!~-`#U3(}C@lNrN(HlRV4%HegTMDu+Six%F`837_<2&4;CF5-V(Kg@5ED*vh!|00VUur4uBk2bOjS!H'
        '6%v&y`hH_b8I$?wzaTLP-Xo_FW_{C(6)LJ6haa#z*!gJ^d`{)05DZpaf^ajL2f^Zjj>BO&h!%+s*{g()OPXK4xFeUC#3j)mVCU|M'
        '{sRC2'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
