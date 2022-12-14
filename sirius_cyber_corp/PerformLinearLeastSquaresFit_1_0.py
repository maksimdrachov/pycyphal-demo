# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/custom_data_types/sirius_cyber_corp/PerformLinearLeastSquaresFit.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:13.194829 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     sirius_cyber_corp.PerformLinearLeastSquaresFit
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import sirius_cyber_corp


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PerformLinearLeastSquaresFit_1_0:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
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
                     points: None | _NDArray_[_np_.object_] | list[sirius_cyber_corp.PointXY_1_0] = None) -> None:
            """
            sirius_cyber_corp.PerformLinearLeastSquaresFit.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param points: sirius_cyber_corp.PointXY.1.0[<=63] points
            """
            self._points: _NDArray_[_np_.object_]

            if points is None:
                self.points = _np_.array([], _np_.object_)
            else:
                if isinstance(points, _np_.ndarray) and points.dtype == _np_.object_ and points.ndim == 1 and points.size <= 63:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._points = points
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    points = _np_.array(points, _np_.object_).flatten()
                    if not points.size <= 63:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'points: invalid array length: not {points.size} <= 63')
                    self._points = points
                assert isinstance(self._points, _np_.ndarray)
                assert self._points.dtype == _np_.object_  # type: ignore
                assert self._points.ndim == 1
                assert len(self._points) <= 63

        @property
        def points(self) -> _NDArray_[_np_.object_]:
            """
            sirius_cyber_corp.PointXY.1.0[<=63] points
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._points

        @points.setter
        def points(self, x: _NDArray_[_np_.object_] | list[sirius_cyber_corp.PointXY_1_0]) -> None:
            if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 63:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._points = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.object_).flatten()
                if not x.size <= 63:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'points: invalid array length: not {x.size} <= 63')
                self._points = x
            assert isinstance(self._points, _np_.ndarray)
            assert self._points.dtype == _np_.object_  # type: ignore
            assert self._points.ndim == 1
            assert len(self._points) <= 63

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.points) <= 63, 'self.points: sirius_cyber_corp.PointXY.1.0[<=63]'
            _ser_.add_aligned_u8(len(self.points))
            for _elem0_ in self.points:
                _ser_.pad_to_alignment(8)
                _elem0_._serialize_(_ser_)
                assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2024, \
                'Bad serialization of sirius_cyber_corp.PerformLinearLeastSquaresFit.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> PerformLinearLeastSquaresFit_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "points"
            _des_.pad_to_alignment(8)
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 63:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 63')
            _f0_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
            for _i0_ in range(_len0_):
                _des_.pad_to_alignment(8)
                _e0_ = sirius_cyber_corp.PointXY_1_0._deserialize_(_des_)
                assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
                _f0_[_i0_] = _e0_
            assert len(_f0_) <= 63, 'sirius_cyber_corp.PointXY.1.0[<=63]'
            _des_.pad_to_alignment(8)
            self = PerformLinearLeastSquaresFit_1_0.Request(
                points=_f0_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2024, \
                'Bad deserialization of sirius_cyber_corp.PerformLinearLeastSquaresFit.Request.1.0'
            assert isinstance(self, PerformLinearLeastSquaresFit_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'points=%s' % _np_.array2string(self.points, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            ])
            return f'sirius_cyber_corp.PerformLinearLeastSquaresFit.Request.1.0({_o_0_})'

        _EXTENT_BYTES_ = 1024

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8DJnQ)0{@*=OK%)S5MB%0yNTn(#>4?}U@jq!gf|a}4+IoJj3HX@X0a3VkesGxrgp3Gywcrc?F2_k4j>y^N<^9?5*LKTuj0th'
            'pn4znZtMk#xlB)YS9N_~eP7R$$zOh~l)8_3D=R`3MpdRj3Lc3^+>fBjf;7%jB{Wzwy9$wrX&BxsGO#b~<)`+sT{6>5Bne21B{RFJ'
            'Wgh5U!swPMmhhNTtSBKxu2@j`ASt)Zs!fosRL1Kf0WQ~pE4}$J=MvPK(A5oin1j;RRM;*^CDO#5Qr_y1U)b72t@ML^YRwGeT1(;Q'
            '8kF6(<KP@_vSw;cKolO;c$$S=bEaM4=FKtTQu4x@3tOCKX=WXgw#JX#>?q(_1`))N=w3c7_vZ1mdE*2MQjzE{zp{7+&kg|L{5EYr'
            '-w%6z9G*<Nj)+|<`P5pJay?qc4D*F%QMXE4n<I<?5zOK=q?#_7#pWQ~g;j6UTHP%XuchzphBdD-rFjx^84f4fr#vxlCqn0;JGdoz'
            'ps62<`n1*`Qw}q=a^uF;_pHm5`viTWW6dNB)4-aNn>j>>m;0l4YIC@Z*YNs2zKbiz6BHJ2;s?18W?`t`%rAQSaw*=&i@1s(=7c?j'
            'OhUj(u=c>5Wi8QxkY%aVOoX;!=9x-!82~Lrz%owAOxe96;S;JR$-dKcvoDCri7SNXK9Nr#XJfvjL>v-SOn2!!D}o|J9xaCur`F5|'
            'xzcHTq$i4*Kh}0@=K77VUaMZMy6#%-NMB&c71bl1eCWho5r92#z==ISqGWFm#BkIU+NfXtw&u*oLiaSfNuPaLm{(Xzr+ed)s3P{$'
            'NKls+>V$`+<{El81IcwNhkYNQAP3<CbFRt5P$cbRn=rs{4o45n`P*sY8j_rt(wypLB;eMm|0oiMa-3`AQN(3&EP9&l@+b%U%r4dD'
            'o-3a&jjUG|T@$%a<i#SPzSEm`oEyr{2zkUQxK?pdrRR#I4V{c9-TS3Ms>{2{u`|dD%E#{-xL5P=@lYH-aho62D*5<j<x>@ek!L&*'
            'y0Eod=G6i7Eq599FN;fN;XW16P9VIKXlR2RaW%Q5LN2*dn{dV;uh5ZS;Mcu6w})8U=}je$%V8K5f-%yT3mZIX!v<ua#kgMY^jNz^'
            '0o-A%m2j{ASNS-~E<se`Uj6U#$sCZAr!yyg)weUpPpG!vaZ%x?2l!b7@8J3p*0F(iv5BAKhPn8!zljn5;MP9gG~eDsp}f9(JRSs)'
            'Y2|S*5=wh%%e%hnbxZJqG?k<g5+yAsp(lZUUy1TGf=5{Na!Y86a>shDJn3F;6a=l72n0D)Rqe^_A8GdIfi8wv86pE`=;EJq7d|fj'
            'ClmO`Ax8X@6bv15leYDeXBO$g>;0f5L*OC3dV2clP&Xdw=Gp&Hj5n&7U;Crq>ZM8gd|6w43s6mC)ZrGrF$Ssr1BnyyB$WsN00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
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
                     slope:       None | int | float | _np_.float64 = None,
                     y_intercept: None | int | float | _np_.float64 = None) -> None:
            """
            sirius_cyber_corp.PerformLinearLeastSquaresFit.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param slope:       saturated float64 slope
            :param y_intercept: saturated float64 y_intercept
            """
            self._slope:       float
            self._y_intercept: float

            self.slope = slope if slope is not None else 0.0  # type: ignore

            self.y_intercept = y_intercept if y_intercept is not None else 0.0  # type: ignore

        @property
        def slope(self) -> float:
            """
            saturated float64 slope
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._slope

        @slope.setter
        def slope(self, x: int | float | _np_.float64) -> None:
            """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
            self._slope = float(x)  # Range check not required

        @property
        def y_intercept(self) -> float:
            """
            saturated float64 y_intercept
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._y_intercept

        @y_intercept.setter
        def y_intercept(self, x: int | float | _np_.float64) -> None:
            """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
            self._y_intercept = float(x)  # Range check not required

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            # Saturation not required due to compatible native representation of "saturated float64"
            _ser_.add_aligned_f64(self.slope)
            # Saturation not required due to compatible native representation of "saturated float64"
            _ser_.add_aligned_f64(self.y_intercept)
            _ser_.pad_to_alignment(8)
            assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 128, \
                'Bad serialization of sirius_cyber_corp.PerformLinearLeastSquaresFit.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> PerformLinearLeastSquaresFit_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f1_ holds the value of "slope"
            _f1_ = _des_.fetch_aligned_f64()
            # Temporary _f2_ holds the value of "y_intercept"
            _f2_ = _des_.fetch_aligned_f64()
            self = PerformLinearLeastSquaresFit_1_0.Response(
                slope=_f1_,
                y_intercept=_f2_)
            _des_.pad_to_alignment(8)
            assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 128, \
                'Bad deserialization of sirius_cyber_corp.PerformLinearLeastSquaresFit.Response.1.0'
            assert isinstance(self, PerformLinearLeastSquaresFit_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'slope=%s' % self.slope,
                'y_intercept=%s' % self.y_intercept,
            ])
            return f'sirius_cyber_corp.PerformLinearLeastSquaresFit.Response.1.0({_o_0_})'

        _EXTENT_BYTES_ = 64

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8DJnQ)0{`t*TW=gS6y8A7q)AJOLIVhi20>Af=*Hu@c|d~Dl!$7Rbd?g|r81rwXKgySdOT4U38{SmrP4@5iuncnQI2<$X45ph'
            '@XAW7@#UQFobTA@^Rp{|{XN?m{o32rFs;+9OKYwq%jB;t&Ulw5WnPuF)ZDZ;?(<CMFigK6R@@w$&z_s#%u0Ke%A(-Ph)#RskycHj'
            '8^zC?Ow)qp01?(w$)={sFy;!dRn_ftwO6WqQx=@5P0nil=xM_guQ#Ob?(n)QiyAy<={{GrEDIZE=7*E<vFT0qI)9kwrk$ruYbE1G'
            '^V&Ryn3oWGX=U2!4au|gEXz5XGR>&AsbA(^DO&=$4;I%pvXbfZMCWNNHO+W2(8BcA05SnaG%r(b#QW`1|J2>Ob=P5U%WeUW&hKW&'
            'wC~Vbvm#|Godh}roSY2`shiXW-cu~mz`usNY@Cb%<0pTr({aKm3?kQYJrZEo@k2x$&&Q#M-OzPH<hgzjMg)ZjzCQMe=S5NAM<jAW'
            'FANB>J~%)jK?oDyC1HSk68Sy}TpR`g35gRrzK1-!>iUl766^&4@447<aX?4}Q-^>t@gM~Jk?Xsm?*tJE5JYp39|pefV1iK?V9)m='
            'gd*gU$i?97p%8)*9}y3XTsH!28_mUT09F{|$RkeR6GVJJav>^qfh|x3>I4TEd5-6WKpv8HA=}U)C~_hkMT9umN02+hfkQk8djxO;'
            'Vr=o7Sj@H4bynKrze3Y8F>S}L-WngScu#zAGWxK$CT@$5#V3d2j#&A>?*F~+^FvS(%~irHZNy#CZDQUoPV_X5hhq`3_5WNfi9oD2'
            '&~GWP6i*nal6ld-Mfc<ZPia*uO=W7f+XY&e4WPnC#%aZ%o7x%s$z%+j)CX-l=-bs}=-#PS5QSZ6cxbE}IeSveJcafW<vz@-VKS@)'
            '%kHK;FHO6UG_@}CGsys-g$wd#+B^R$a84I>t;`s0yMK`iRzs4C7uxF1zD&3|wAFz77-taS(^FMCQwK2Aug*<-{hrjDqxmD4p6FBi'
            'CM_YQ<;y_oVIG&6gnPfZ1tdZ9tg<|;xMI3glZu}R3Cbz@?ae+*Q&|iy7>Ql6^K#U0Z>^VwJ*DEcknOcGA`rLQJ>mJ|1jfznCd-%_'
            'Uhuw3_gU6(^QT$qtsT`dycX3sEqEWA7>bw6!pboW*nu6)SV?X&X1(VqKd4wSdQi6EG7d(d;+Io2UdJNuJrf1|OW1g7jk4Zsb8)$j'
            '?PV78;<|WSELbK>VwH<<^3ICrh4^Ayd?~(K5nqcn@r}4A*2R7Ct-S)`yYX?)Ku%CBZMHgZv`cWw$1ks<g0mDpqc;j3l*L`hdr<K7'
            '0W{Bmt8=dr$kZ~()JMH3+h!nEklX{YIi~k;qR5ZOOF!F$C)qCp`*WxG?hY#ke1}(D%ge6Dlam^Q!z9-1(Wp52wkUv;typi?u6K^='
            'QRzliwwueZ*|e_Re*oaf9HFiV000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'sirius_cyber_corp.PerformLinearLeastSquaresFit.1.0()'


    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8DJnQ)0{`t--D@0G6yMaQNxu_gTeOG+(h{Xz=X>tpL(>leb-OVpZLMe-?#$fHz3J@CbmmUT7D^ML(!zj+UJ-m0d=a64fc_gk'
        'NMFRhh<}CW?nic$?6$U`PbOqO?mg$+^E)5EGuhbt&38vC?Vs|Uv=!!IRP}O_F&wcw*pEon3zBA<<ct$h9$Y5b8VktPR!YQU@!qDm'
        'D`v~XUPf*gB<CKN>$FlHzC<F{1eI{R<UWtZG0EB@%RDOrUSvCrje9X}!clh4GFIeX(DF$JK4fWikz|b|YhGb7!PympbH04Lz!}Ns'
        '8LuvNToC1?w??v@C9ynZ;(GV_v8avJDqo3B0O4WIGv*hZ<l?3n1$#?Kl;iV^L}A~@173(Z?w~DCj!@4s+!E!9>ljvH<qC;cI6W^{'
        'cSesyq)Fml^bU2_>Cy7dAt6Xu%x`=q=ro<_0iwrmg7{lqwYNv%Ni&%dwgxWmpN|sEx4UuB^BMP|wwIzd1sDSeu-8mN@aar>e6go4'
        ')v6a^uP(PBu9f>@NtADRImdB`vvAPR1F+M?D>36mC=YIAIN*?v9P%{ZeFhulxNTXgDWs*s2k2w#qTK6+Ng&FKT-icLtKBE9Hbr%6'
        'Q|AFi^uyf-T7u5e^My~!nSp$JeydYo(!@FXKD|sY6o5S>X+{DJ1uGtwN4y4GC!v=n8TVKy7RqTaPl_xcun`e2#el4wkhh5WfNBxi'
        'V|`JsK88q+eE@i_LGS_O;U>P7vt|fTX|e|IX)9=@6h~)6(o94-9TYiFn*DkLo#|a^7v)qp@l~y=R%LbtmqDNLD9*v3OqNgH=}qxa'
        '0*C1N5g0q&D~5hjK#=cz7v-S~jCX2u8D6_(QNHFSaJn+eNZxAtNyH#aGj+fNr6v>laY{1GlWef>1InO-Xiy$q#9_$dm0d!VQnK|F'
        'l*cY6u}nxj)MUB8V-bK0S^a&@)d3qv7m6stS!<W}K5q?21rcA1+1k{j+y~M~J8l6@6g~v6$zsSm-0`~Xh6&jSMT9}QHYv3#k8&t&'
        'vYz6&%`Xd3b$8mv>D``HlKXUHfo|3m`sIKgy)T9D)h3J4+qn;307jhRfbo{7ohx7OMZO`)s7n@S%9(56z)DQQ%P}V_B-_^2&?S@5'
        'C1!0*HU{(x9Qg(HI)3^CQA;~Zxs2r?j7fm8EiEUOaJ)j6NJ=;xmFrubsGS3ahQwH_(9Qbq6T4Bi0|Xv!*8iLs9s}s)eW@({yxY#0'
        'egwY#NKfYU%0pUTpbPYqS-M1*=~a4-UZ<ayr=B||w)GGF`~jUSSFci*E8Xr<a1fA`=L%LLmUAU(DEcL(?Sc{{Nd`3nMG4z+sAL4j'
        'SDY)H5(TjEvkk^UOCGB<invW~phOxC7BJ}0yefuAzhAT8_Ud9FDg(iwQ$YO3B;nJOFN_5JX$vEL0u@Zwp_{m<SCsNN5MF0MXC5Uu'
        'gj=Vc9&Oc)0(J8$6{BpgnD4t!Kh!IG;dN(ibz1;@8c`i`QyJADN8rOFPhpynuKN?+(+&(wQRk&UBswNVFVwR`r_bEL^toY;RVtd}'
        'I<{+QhKX$5&@4wqnrZ2dsT+==IjU(`w&NnzQQ>as7BWrOwJjI9nqxXPQl*Y=s}53C9a#o)Y}G=pWg*+p9ot3@(j3h)Ra34SmS!4A'
        'H*GL)8oFlaHbO4EY6ygp2}i)6YFLJ2X|{`O6;9Js%Yiwm=}1={TQ@D!RaI9tkZb6mY^n|%hAb7CAY>RW*p{amx?zKquIsLeG}}Td'
        'vMkqtQ*{H-0z`n0bX!+V%`_bV56&9kt)n5;)m+_m5z=&+&+x0;8ZtHAL}1rO{eeB6M~O^fyUYKN_<s=bgDv<P2L_OQ*ZWwKoH9%Q'
        'pik*v^jYx_h~@l?7;QLX43iw>hB?V1_v9=FDx8BEIk&}xyW~1kWCMgY`a(S#-M-vq(ck*5{ggg?70^G|D|_fK{~}!i;ODUAp69XU'
        'o{^)p`f^k_lmREf&P4bBz1`jVE9_2YTMRl-RI8_;V^`mmmsxo^4VM?iT7JnsDg5f+y<F>tr49f9'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
