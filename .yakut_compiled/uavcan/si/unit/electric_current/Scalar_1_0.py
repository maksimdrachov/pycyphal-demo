# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/si/unit/electric_current/Scalar.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.226522 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.electric_current.Scalar
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
                 ampere: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.electric_current.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param ampere: saturated float32 ampere
        """
        self._ampere: float

        self.ampere = ampere if ampere is not None else 0.0  # type: ignore

    @property
    def ampere(self) -> float:
        """
        saturated float32 ampere
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ampere

    @ampere.setter
    def ampere(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._ampere = x
        else:
            raise ValueError(f'ampere: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.ampere):
            if self.ampere > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.ampere < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.ampere)
        else:
            _ser_.add_aligned_f32(self.ampere)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.electric_current.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "ampere"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            ampere=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.electric_current.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'ampere=%s' % self.ampere,
        ])
        return f'uavcan.si.unit.electric_current.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{?YWOHUL*5MC5m1Q7|uiw8OJI5_TO7Kf`Qds)Gas5jH;>27v9_B_&$&5j9)95j-2q6y{ywVDMNG0bJEx~jgeuj=cs'
        '^S_((jmytJt7>kziii<fQYF98REdbNGOtP_tpLAzY_((7Y4N_U1YE%08JxndUmyj|F~05Sn9(9KGIE8qkx+tJEg4}>Yf;$fm{CPF'
        '_$4wH+Q_nitl^s<uj~sL%ncgf;SBr=p%yDsXN7@Ja93}ClfW<ZrBHm<(=y@IQes1+ca>LK=F-YBW<2PtlG=Z1t&mh&qC_#W84R`%'
        'l2KzxUUC81rhhWLE)QkVYm6O+5YlLTgLmLJiLtccRP&oaKM*IUBb<-p;o=ibnML{r$I`#D5yS6v<5nl>bmRT~Zqn-{N$((Ow_mp6'
        'cG8WLxYyo4==9>a1>r82W($6i=9SQhIZt@Wz&G%i`i&c-BxyZe)hT2<*}6fBTvS>xY6XXL|A?H(iQuFvwI!0nkzXgKbeahaC_yTU'
        '1bj36luWVtAu3}s45t@3u(=nwhYvVo<g%L6&qn4P8D-@d{i<ell~MJai@XH?v~sCJX=pKWDqKI?7gjG$l?48tk;o^g3H;;RdIG;T'
        'RaDfDT2a_A*f97Fl2L=rhMchSv19_yv)ybDN0TbV-@X>aY%!Q<Z~NdMzLNIMrGJd>l{EZ)QdZ!%?gBA&o|Z@sJ2^zMD7UcGx40Z?'
        'OFa|VB4L?C(Pn+WHl&=(V)S29HVDxpr;uiSJBkQns+@qIushiLWm0@u)f5N@OD;vaxh#Tq(V&xHG=qL|;-Pw(h)G3@%g1-*Qj@wg'
        '`U6kkvgQ&5000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)