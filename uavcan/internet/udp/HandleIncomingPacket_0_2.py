# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.2.dsdl
#
# Generated at:  2022-10-01 11:53:16.517181 UTC
# Is deprecated: no
# Fixed port ID: 500
# Full name:     uavcan.internet.udp.HandleIncomingPacket
# Version:       0.2
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


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class HandleIncomingPacket_0_2:
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
                     session_id: None | int | _np_.uint16 = None,
                     payload:    None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.internet.udp.HandleIncomingPacket.Request.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param session_id: saturated uint16 session_id
            :param payload:    saturated uint8[<=508] payload
            """
            self._session_id: int
            self._payload:    _NDArray_[_np_.uint8]

            self.session_id = session_id if session_id is not None else 0  # type: ignore

            if payload is None:
                self.payload = _np_.array([], _np_.uint8)
            else:
                payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
                if isinstance(payload, (bytes, bytearray)) and len(payload) <= 508:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._payload = _np_.frombuffer(payload, _np_.uint8)  # type: ignore
                elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 508:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._payload = payload
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    payload = _np_.array(payload, _np_.uint8).flatten()
                    if not payload.size <= 508:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'payload: invalid array length: not {payload.size} <= 508')
                    self._payload = payload
                assert isinstance(self._payload, _np_.ndarray)
                assert self._payload.dtype == _np_.uint8  # type: ignore
                assert self._payload.ndim == 1
                assert len(self._payload) <= 508

        @property
        def session_id(self) -> int:
            """
            saturated uint16 session_id
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._session_id

        @session_id.setter
        def session_id(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._session_id = x
            else:
                raise ValueError(f'session_id: value {x} is not in [0, 65535]')

        @property
        def payload(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=508] payload
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .payload.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._payload

        @payload.setter
        def payload(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 508:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 508:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 508:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {x.size} <= 508')
                self._payload = x
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8  # type: ignore
            assert self._payload.ndim == 1
            assert len(self._payload) <= 508

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.session_id, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.payload) <= 508, 'self.payload: saturated uint8[<=508]'
            _ser_.add_aligned_u16(len(self.payload))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 4096, \
                'Bad serialization of uavcan.internet.udp.HandleIncomingPacket.Request.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> HandleIncomingPacket_0_2.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "session_id"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "payload"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u16()
            assert _len0_ >= 0
            if _len0_ > 508:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 508')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 508, 'saturated uint8[<=508]'
            self = HandleIncomingPacket_0_2.Request(
                session_id=_f0_,
                payload=_f1_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 4096, \
                'Bad deserialization of uavcan.internet.udp.HandleIncomingPacket.Request.0.2'
            assert isinstance(self, HandleIncomingPacket_0_2.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'session_id=%s' % self.session_id,
                'payload=%s' % repr(bytes(self.payload))[1:],
            ])
            return f'uavcan.internet.udp.HandleIncomingPacket.Request.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 500
        _EXTENT_BYTES_ = 600

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8EGjr-0{?|rZEqb%6}C&7q??AM2~9zj=v0L&mCVIdlopUcZbB5xv12(-Td7p5xw~`k4BnmD&dlEHTZBYDfLdt<m9qSw{*?X%'
            'KEO9V@SK_5`(j^1q}ccF&dWK^InQ&>@t-gK<6pNn!oTK?YL>ga7^F^E#S8TX9~NSeW~Qu+Q(m;q_4}ewB|hfIvr4qj+jpL|e`@bG'
            'ms6#+u&vx^u0Qd%&U|gf>XH{z%}X4yUGquC^+0JatQLMy=hfgL*Lfj!HLg;6e8{sCyf_k{*TVU>xtdOdb;@Wu|H?<*=jZL-#@-8m'
            'ZJ)KxwUm2r)v)%$wV&a#3p|;xYMU1yC{g4K^O7{@o~NE{zG!=8$#*ruirY`MQ)4aiUAQq8cGcHw=}`H!5PIxoyLS_ZXWaR;G`VQy'
            '51KoN{Xw*Ca1ZbH=@ohOm-eV_zLz==M7YhD5Bjnm%A`r0aO8ig^0v8@<|b>Ke;-Tb*oZu0PV%B)nbDpr&Ab%M0e3dxMJ@1^dp6~c'
            ')lTGWI1BF!lktLSSiq)IXy$~@5ryzBGu8@MnfS!ier)g|sX~NsO24jzQGARG;1GM<E$iaQf_2e=se*Asanb$Wu#)>shUf8OCz7f1'
            'k}2=HmE@Z^^@A38yc!Xg-)~;OAmrBaS=+q!5yw+Jc@(hRp{J`cyPk?dltTNM1M>Cm<R9)`m2b$m<c|P<^AZ9H-<6-W`~TT&Zgrta'
            '1N7%M-o(Z?_cke{ar>ooSh%)%yEk<aTv+YTes7zXKU6*%`~+V+Q=9LkrfM5@(IIYD4o#tu7Pt3BX#j*rx;(Cg<=)t3&Sp}90`j-b'
            'tM`n~xEFfuQu3NsTA_(tSbyW7E(&gE=T=@$LzvsYw|Dn$e(i>Grvu|YcD;7Q^;jH<N_cgVNhfK^PYGM>cod$>$8^|L92NkCK7b|k'
            'f!2L{qq#z~stZmB>}}H8jj#8v#@{uVCr&G_gJ2xgLjjXMMO=Qr|IZupvvoTp$1=JLRJ&5~Sz$OJdi#@yn;RRy8;wLpv}N6kF11NH'
            '=9xV*b_(Jmy+_uRT_Tsp3nq>83`#Zx%H<$=djF6`9=XWNp0lN~fvK9kxBUS~0#RdT)ZYn$%;=unnyQK<a;A*Tqjd>1w5+wtLM$0H'
            'R8^GL19l`v!V<-f9^7N^|MF)H62sp8`7gG~W_)2v|0EX`xMsyfiRmD@568xqmz{y)G!wWn=t4&WGR!ZFkE!vC%u_ClFmx;@@hbz%'
            'iMXP<y`<Uca2BfrrOJ=x9Vz798Y&8Ftf0iq+pn7Mf@P;7Pb*_RiQhr<O6p8)Gl3U{NGlGFq?mbGs3EfU5Jl_ske)tAZf*V)qW=`)'
            '00Lew`H53yZh0on1mCM!Hme|<@V_)Iw4@$_L8%pEWEQSp6bJ0S94i>=QeVTsNmQ}6dGo#P?e(>6d+_dn=-PVH_uHxD4hCD28<;dv'
            'nP|U6mi_Iejg62}y`BO?s}R@aWPv{Wm|T1%wM>-z-OeaRL1mA24k+Y2>T9<o>gc`TG8@)zkQ^3*JId59MQBwnMoI^!#wh<!m5({Z'
            '#sX~s4mA_<N=*Bm)qD|=gGxwY#wr^m$$~-QQ~-nYK@}=F?B%ROC%%MSNV1Q(!B?#TZw%7S#u9QOLcQ=7)Q3lo@f`An<){E#2@0f{'
            'Qsp8{9PJQgRhStrw>j*?y;%k#aE*(RTb@oJ|KjJa5-u@4U*!p%ppEY@6?qa7EeC8T&jX?`VYUUh!A{%PP}t&Cl;DMByqNNt>uO=n'
            'YW&0(vTi9Z=PgN0CA4E9LBp{yxgzG&6j9N+Q&XD;T0{9sA>EntXjf&8H<>90Y&X8^1ETcAbQ%LW6D|QHTW6Tg5L$>ldL2)?VM4l2'
            '#G1|mDQ#y9#XQ(KW}bq@R9T8#frEq>fjZ@i+)2m*it+LBqY%N<N?Cz?+Vx8+gbhKk5EQ?fXG_UVAn86R3`Cfakk&rB8x*DwWheM_'
            'lF@`gGEX|_NmZy(6g&DHnu!1q1v;;@=r`y_c{v)XEU-iho^J&y9zyES7ll<w0}4%y#~De7!V$wA#RiReFR_Z0!PAzG7-S@V5NKFA'
            'QGrjW&ngFqGqQPZW{4{MARR#@FHi{vY;g;Bt}c667tNc4SZM;?Xuy~i3g^1$8L?I%U?L>QY+frvguO{};VDaW^u5EnPey7-VOqd<'
            'My{5;s(Q|JWoO<JciN?FO#K+r5>=HdD{Mwzje0Xk9@LhMDuYcbxK)GgHWc6~Ii_5=z<_8aJS4<mkfn-50^A$0njgfRB)T3k`BiuL'
            '3TCTKuZwV$fF8C|0^C1%!l)d&6~Ws*oC^wIb%@?50-I1n&(B#x$ZRc<5%&aINInUTHi!vpODguzH!+8GPQt~7F=`|`Xnvq(Bvzf!'
            'bj!^ePWNv7|EYue`v7)VQu+*zbW32EH7M0Avx34$)vPXu0ESY;8Y<S<gxgVkkcEzxAnjm1tsQZs120Xj13RS3bJQ1_Y7221)iBzh'
            'tkO16X#ro<7DZZ2e59<*mvKBVjJVt{Ca}I3fsD#n>YWN8Um!IW*pR3V;cHIwBB@+JihTBQFj@j9IKOV(dT6E;Qp8?}E>D-Oj=sfQ'
            'hy_S2WIO4{u!S`6dC6j-W^aKX3c=|5&>A>6Wy7?EaLtK6KOmG}+%d8uoSdV%ghwH9l69t0=#WMzR<UylZQohcly+WF2fnMjhSUW_'
            ')-Ufkp74C4Tnt;Uv}gqg-3y{KXypg;*KrW}&B`=$<B)*S<8xCC-Y(WXh+B7QZdyEjHvhCd<Iup=Tt!<L&TaQL>uy-Vf6OXjGLav~'
            '5r$!e*;smv0j6H_JPtDQntWN_l&_ExcjR3m$IE@TRA0$I9LN)??@A*p`MI>xNiS<TkyC0{<rip8<sUI=g-*e@``_GZ?w~o3e+sfG'
            'l`#A|JN`0^zwd{^cRhy7*ev6~RtLx9?$gKnpS-YkDwLld!0T^rk=Okk=YsnID|-3unwPY7@L!S>apwOL000'
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
        def __init__(self) -> None:
            """
            uavcan.internet.udp.HandleIncomingPacket.Response.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.internet.udp.HandleIncomingPacket.Response.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> HandleIncomingPacket_0_2.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = HandleIncomingPacket_0_2.Response(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.internet.udp.HandleIncomingPacket.Response.0.2'
            assert isinstance(self, HandleIncomingPacket_0_2.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.internet.udp.HandleIncomingPacket.Response.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 500
        _EXTENT_BYTES_ = 63

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8EGjr-0{?YWTWb?R6i#jJ)my1n@z$zPQ_yV{d=eC`f)X1;y}ZdVyK~GLx|v;OW<w$r?1NHaK%vLK=5O)QGf4}n+Pv&c&TYQS'
            '`8@IS*F<gb3rl5RIh7~Efz>kCpJbXtBC?`W7EXJhaQYeKy2D5HwqFA6)9NnmP(4fvZ46k#S~&g2+bZ*wg`+7ag^?X@aj%lyOqxU+'
            '57vNBDpe*gq)|D%G(1Y1c1vd49M}R^7RGVSwCI9$x-fCT)cb?;J~e8M6JKeU!km!aTb))O9DSg$Fme}Ze>i$4<|!yGWRelkw{S*$'
            ')ICt5EUXt=Q8Ua7S5!6w4&)$8>5;-z{Ny^NFw<fldad~HK0_K?qj2&aljWG1j@)*-qpZxZ=<>bnXZ;doepf-Kpm3$E(p+c4Lc7Z2'
            'c%h`1!ZSx)Jvk(Wksi`QVVsGfaO1)H`v2)!PwppCF7mV$5u<ecU<<}a{kl2>+6xmx6&ZyZ@hQ!D(#oO6srDiV)Aq>e{_i`5Q%|*j'
            'HMqaw>w%16TonAM<>Q*TekUy$CckHsVY7ogEA_erD}7-{{gR>172$d~+mcE#s(+I3L5w!5JeRirca%GHWnKY&r+TCI!=>zza@dF('
            '(^blFnJP9&Jjh-=Oo>jRnEO~gE1*|OGq6#!N?lr|IE!<53eVyE2f~FN!VBMUv56P)aviVWRlJ7RaS5042HwP5k#bzw!`oQrzR>f`'
            'I&J<Q3yW;9;f7d&AQgY2#B|(ll{O~pE@v#f<M*@;sF!SkHrS)<GdIFDHI^AcCY_IvfbdmVY#la=WyuD|He-l)Wb8}y$9dsAyGU9!'
            '+Gvk)ui~A-3|zzeBg|jeC`{ZF^Ir+W%uqqL8}C~k9}ZhQigGNo97kGR+>)jZTTp`6$N6D<DAQvu80|IvW1!8GCO&0)abt(oJ&+uq'
            'vvS}Lf|pMG8;qsNA82#tx#0u=00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.internet.udp.HandleIncomingPacket.0.2()'


    _FIXED_PORT_ID_ = 500
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8EGjr-0{^vGU5^|`6`eJXz3IeR$HorA0t$g52kc=J5xxWhV`ID;?`B!AqacAgHQhB^g}b|&s_L1Y03vxHilr8b<jy1f4IX&$'
        'Pst+!A@Kkb4?J*gRrh@C&YI)_OWx_}`nvbrd(OQzZ=e3~{YyRnul_<gO>LU>V=Ii}nR<&4GtrL|otN4wCz|@1d%}!WBKD`HXdX2$'
        'z0>@rxmur#jre6HtcxAJm%aMjEs?1lOVZ_;XJS<p!uToooT(C5nIoG$6&F0mQJWPXC%ovZ!U<Cd*RRsDe}@-oCbkNgq>6)Go;<+7'
        'UO2p|*W<A;R_TKFKl^(7{HPi92B+R_-hufsch0C`<%Dg1j>Asycs8r4pSrC?md?$K;*>ic96f1yX~=gq#*B;i3#$$ak#50_17VhZ'
        'eI_0%7iXe4aIzVk$L0wKin&gK;^*tjyWK{#tbY?@+cZQT{jS+->QBek0TFJ}#f{#phH|5htgz&NtkR}F9j7{J>VNG^W!Z>4Vpj4j'
        'V~H*tR|RuYFbmw-m}iy1SMJz^TUJ?-vf<Q^XFA~-D_{YeNKr5=iWE`sV~I9K*iwf#x^f2^4^inOgk8FMIgH{5H~<c@*V<`q9GSN+'
        '7%)*VZYWMV-)WX}mq`CU9Bf52QBE@DY&(;D6Nj$f0FTcG#O3GeD<_297(Q+47hdOhi#K;YmN)3_(PS5y$VJg5J8O6T(qLVFSzeVd'
        '0si`F1QNb0H*L26vsPbdLlb-Gk1afpg)a`)D5PQe>3Epgrhc(Absk(;?T&tL>SuqbTrl_^zP6^;pNe(a)a;~9>@*+hOd%~UZi`$4'
        '2#0ietrUhkZ5BD3NCgVWTlJ-zx=6Sa#mcGVHO(}lAaY^;#!i)G+)R(nJQMpcH}5xB2j@SqLwUOeV+*TZ*yF{4*b}92>LimM#5q4C'
        'Y_Z}e{;k}n&DOD*2N3!Ime2#u`)H#+OSGyoP8$r?Xm0O=!Fu?tz&vqS^1=(oPBj!T=}p9iZ~tRM4p*&^BTS>SK((_apJti^qOZPj'
        'XRX)!(P$(RqAhC&+SDfHm}T}zn+b@E^d1?Vw~3r<Cz#aMF(}y(DChm?{;gdWcw_@FJI?0Xc%~NY)y;2#BoH;GN8Onq$dt}WjV{YT'
        'BCGSjJen6lL-VRoiH{|NhN_a%y3h8+NEo8n-tC+0o8Nw!L1Ne|U;oA?*^Dnt71vWyf@?;Mm6-ISTX5{a@Vqrp93}!MdR=H~K!&+R'
        '@zE7N$UJ3}07J`i62IKDoQNyxiwl|^52v9zP^x@IUXj0$*DI(ftTBQTGi@H$&w*u!B8^LJ9Esmf{d{b7WfFmbOvELJMpDe2%+wHB'
        'yNlv>xJz#zA-C4P2GPF{aR33&<@|wFd1`nf^%&pFX)-M#obW%_4YZ^hf<Y*M2gocOKQ9hgeI`^e)TOS5fs?3WP5s4JH#b+;vd#W0'
        'eWGjQNZ&8Ul3N&TNN#K>z0G^bvfn@5>-m)G^b{Bxg}5#z3-sBA<l;-IrGwmWwMH=tD!Y4QheFPSzP3|>j^6YxvtecX(QYQVrA%#8'
        'gl45;qzcc}5alPTe8?eoAkYS2Q#~fH#H3qU&L$B#sDxztKqdVsnls4n3Sf{vs6si1y_~h^gh9xKB>RXPeAycCMkC!!C?OAouNTgM'
        '`tZmyo<hDb9TnhOgaWB2RJjNfODjZPW_pUlO$z&PZjyiqyuiW8Ek`?$f8n{UgbPehmw7@v6xwx%iZlv{=6!Y}O+BJ8VS0^Gd!<ZQ'
        'Lt%?kL4xO&@od7UwylLJtMC_J$hw8N9JeIWr6?@(3F^0n$t5wTqKJytor>Bt&>G553Tcn*N2^MsolbPtXIo*c3y3Ply44uSnXnNc'
        'xpsu<455X{qt|hy8``JqSghzQkkV#4SInIo`^-_Wn96gJDsYhSB2Xt>kvkDNKr!Cmzw0A-SSllsPg`z5g|NU27J}lI^K2ox38bP6'
        '3Ih?wB&3xK?s|pkLfHyF?W7CBAeto|^rXzxD2N?B`)0xeM1fALB=`-wQC^NlD)B6lf~VKK6b~VF=!^U;qydE{#N&vhL*a<wmSTej'
        'zLQu*%HU{8OAIm+e+V?p94pT!)Mu3f#3|W4Gt);EevpnJk|(GH1GYGYTU+HFtn=p0LaYh`T^E2c$rSdr!82m5K){4gkm;;e`UpE6'
        'rNU8`6v6iv>n<6o9ffHg-zmA8^RnzX)0UlCOWbOgG9mRtNOM$Gs;saXeKqP$Ke}BRGAj2rDeqPVwi{o7C*+v2{s0Z4<?xUYgF%KW'
        '5(#i;z;b>NbE4pSz~npa=1Z6@H@!B%kpp_zN(pdl=N_YSXqN<UYj-9nfYl;;qX29~4Lv_*2_bWBfs8oE(?asGZ?r*7SesL^hrWp!'
        'tTPhM4-8Qw*+KIIH6yWVg{GaZS8%#><A2{esK57Mw<V>^;6S$sh8c}g%@QLhd{oV<d<bADMU19mjYT*e#RpkvX$sN~*3;Y(M>_Ca'
        'SA}PXRB4L(Lbu;c90oNE_D9RK^;DX}7qmr@784&SE7L_Bj|(FXck>%qSByYLr498?8IaGA8gpz&)Q0dirTZeOoJWd$cHv^Q0FHNl'
        ')phHRo=`{;dm-99U9>v*7IGmJATgKisJn*ErGd{%7V|ax8u+0QjJ6N0fP+=W-?k908PR7O`0|T0Mn?FZQ#6<G$R|#;$}|cc(g?*W'
        'bS}Q_JBpertP|9MZxwArYCR&Wr?(uBcsf=#gsoFrv;u_g3DM~{@_X_J;UaQ#={B>mOTZKd$8IqgozEMDr8{(Qn!kN__Oy7%p$k*J'
        'j<(S6+YHvK_OgQixU2Y^iTrW6!hprwy@l5w4%Vv`@54n#o|n(dOY$-qaYbGiGF$AkW${qz9a&0yRXSP8v7E?5IhAk8U&&unyDEQ+'
        ')>OWYo0jhsT(kZ7LVX#{dH5;F#8krYarFAjaQ*$Rzxb}ka1onD9N6;3@u%(6&$iz<wenUd-`s)Mk1vqd-965F_dQlL_|b|%f1!LX'
        '?tW!x%|F|o7RhJZr;YmMPw<mf*sSRQC#XLjz;*A0R9l@aJp!qVdJj3$I~w#qe{vh-WBG^ef3L|u{vV?_`2G`uh_g=);%82+4k99S'
        '_2WjUnKNPb(~(@KyMFsqXG16~{;(wfgwb^~3#=b*DfCzQ7x{Pjw?Luof37_d--kq^YS{lT7k@c=niT*5'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
