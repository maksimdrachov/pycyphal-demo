# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/primitive/array/Natural64.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.053279 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Natural64
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
class Natural64_1_0:
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
                 value: None | _NDArray_[_np_.uint64] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Natural64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint64[<=32] value
        """
        self._value: _NDArray_[_np_.uint64]

        if value is None:
            self.value = _np_.array([], _np_.uint64)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.uint64 and value.ndim == 1 and value.size <= 32:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint64).flatten()
                if not value.size <= 32:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 32')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint64  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 32

    @property
    def value(self) -> _NDArray_[_np_.uint64]:
        """
        saturated uint64[<=32] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.uint64] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.uint64 and x.ndim == 1 and x.size <= 32:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint64).flatten()
            if not x.size <= 32:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 32')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint64  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 32

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 32, 'self.value: saturated uint64[<=32]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Natural64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Natural64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 32:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 32')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint64, _len0_)
        assert len(_f0_) <= 32, 'saturated uint64[<=32]'
        self = Natural64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Natural64.1.0'
        assert isinstance(self, Natural64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Natural64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8EGjr-0{`t<S#R6M7S=90wqrYvv!_wBDybtcNnAHwu5JSqE>0(P)8(xoC~;~Mr52Es5fv!lKHLizAaDtI?*H+l|3TY-(=!~7'
        'hLo&0Uiwg=hG3C1XZy}MGx~<yDg6KYYnkXTxYg~Op6S$dkGi(u*gqK!ht~9Fr`7Fvwoh3w{k8A*ntsov-}Jkb?Xicyu%B5qDC%va'
        'h4Yo3vE4M<wXSQoY~S9dHN$m{e(j}!I)=0Mlm(i;O<m9Kw3(F&%HPG;dknIW`7is01(Ukr`>x&S`P5_IvvE-kgji7g%%+a1qB*CV'
        'hHvOT4>7ntMxDpSg3I3-IEo`*(Ds&Z{hN=bp-t=5p)K0>V|!!586alC{I_k--fC0x^R`d7sGGJosW)t2cOrKT>KJU(@O-`1F)6dI'
        '1(!CZA+A<?fpdgUVS+OMVXs(lQTKeKZ5pnbG_>1m1QTefYcy@Y&!7@qh^O=)cydJW)(sJabqh4BV%>%;H)-AD+6BGgcr3Ut;VI*Y'
        ')E~ZQ!PKX=FOv2(-p25Pyx!?z8;mpJ^;?aOV>dBLgtj`EJRht7WtX~!-*HuvN_x|>v82|MVBtll-86jKK2(&0=8`ULW3N<Ee&%J*'
        'aSXRVB3aV64W~!h|5z2Y&}&%F;$*C&*5y}5dyBrJUFzH8Li$l}8Lu(5s8Ejvtry%@9c@MVYuRlq62Cw(lF@=PuWHXRxISdLY$k+U'
        '{GE@!vFmdo6ymYsU<~q52%#kIbNsrTnu8*gLeOHpiIF)dBSttk(8m$HpFC6!Cg5BMQ({izzNW{@!6ZzDa6V-hM{#WCjXE$5=R=r{'
        '<DENF7G_{JgbO2na0bWc-%20m;6ex&g=_)mr?~FITkFC+TnypTp)uer&Rss1Em(j{AzTqUv%DTxkF5`v;YtYC#>RvaIDh>_cHt^q'
        '3*km8UpR~QZl2g4T!$MWyz|C*Q3_>loyrH?gm*%y#QpW|scpe6sDyA^*r~iJa_;xeus`MPEq%eea65#%(qAI`JU920{Un-EETh(A'
        '+i(Z&hH(GLI$$&vlt$SHX`ku*%|u$Gcy31eu|K#6_d}>kOd9H7FFhQ^BJD~f^HDs)s?3qJiZ<Z^R6}_5)>u#j<=+$XM|HwbO(YKP'
        '6CT2&5Edn#yXd)^uG3?QO?I7@$e8q@kV!wc2R<Icd$1Tn?O5305!YFgI{8SeJn*e@x{%7Lz$ZLM*x)hLLRgmj6ZZd#vZ?AMa>mgt'
        'MA2N0;*mAt_C&4_30ho&<q%enjR$I6@5$loc(`iAD=Ds3906i_nyi_Ivr{;;tm^hG*^|RnQ>#kGDLXN)7mpQI;b{nKC&DRo-<SKY'
        'THi^WYK^JBR2Wy`2|R^ouol9)T5na<UFK`<gS2hg`LgHbZXqqp{MC5%V1?U-_hCJR=O@O87Eu2~m1hx2vO~pQB4QDh6l-tLn-R(='
        'j*rwnd3R7xj`bpXx&rIGrXQ=`6)SOKu*b|r5ii6wRl64V_aO4MjGoru1NbO}Pfmpyo^u=jI-}pCy7+zT;h}-P?i%gr=oF2SOcr*?'
        'PL^bHBvT+e_`!=j*~ybkk?a&nrbKp1BvU3kWvIhGsb|T4meg~kULgDUKTr1YQ$X5E>P50&B=r*6FOhng?3cq{gCbx45)TcVMANLV'
        '{x*D8<6Zw3^I7d5J{#qE_8&g`m+)EbjQMQksNL)kK3h73|BYju!+f@q&VGW=j#^J*Ih<Xdj?ZSt_)KR{{w@qNLB(e)(Mfq6pG{*K'
        '<$X5>RwcVUIiDRybW|rC&SyCu#f?V!Y;M3Q)v04PkuPaq;gUWcor=$92i#Ljoe_lRB%4j<Q!s|b1fSJVvYO(vNsg?lB=W`4s56IR'
        '$Y;xEN7wIgwT4e0f{m@ld^TCL#i(k_DL$Kxn2+kl;fkftANL2GnPXhxeDVzVY_c<xYdeWltuMveS0tm2`K(xP)rhl?@>ykD_Pp$N'
        '$&{t#ID==*XL%eV%OZ+ocZxkk#3AY^7`uprGwbIupB4M$oB3=OC1lr%HK<O@@*E~AdS}qJ+}~2<YaKp3Lq2=#-=E?0bj)Y9uxIVz'
        '1<}f67r_xNOLnucOSBx(3S<{QIdV`S8%1(ZBpW4iP$C;;a!@8(p6upf0}jYWmK<csMviP0$N~P(lY>0bie$G)v=Z4ZA!|hv%b(L)'
        '#h@sj0|y1&>@-=BVZDYC%qQMD=#9R3pYb!ZezWGhU{W_}*QNY1w8?%A&g(zeuc@hbJFc(WCVLso>0YPjHYrXxRPP$T#ey>ba_j~R'
        'CN?{s{d$v+?y+i+U1CA;TaUUP3#MDfkDlE!U88Arw(-8(Z}z*E;XF2JtHa-3^cs%c)LpvObGUo;Y6G=P;&lspNW6Y1#;-Om3|_j_'
        'R%**N{y?7j{0+jqZW$g1>GGEv7{<2Ur0iGgck2&p(OMEuwpUY6$7ePT)3n=LBTvO~b}i7*Ry55(>!ptg*4|5z_S&D^5l!4^8UO$'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
