# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/pnp/cluster/391.RequestVote.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.051341 UTC
# Is deprecated: no
# Fixed port ID: 391
# Full name:     uavcan.pnp.cluster.RequestVote
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


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class RequestVote_1_0:
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
                     term:           None | int | _np_.uint32 = None,
                     last_log_term:  None | int | _np_.uint32 = None,
                     last_log_index: None | int | _np_.uint16 = None) -> None:
            """
            uavcan.pnp.cluster.RequestVote.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param term:           saturated uint32 term
            :param last_log_term:  saturated uint32 last_log_term
            :param last_log_index: saturated uint16 last_log_index
            """
            self._term:           int
            self._last_log_term:  int
            self._last_log_index: int

            self.term = term if term is not None else 0  # type: ignore

            self.last_log_term = last_log_term if last_log_term is not None else 0  # type: ignore

            self.last_log_index = last_log_index if last_log_index is not None else 0  # type: ignore

        @property
        def term(self) -> int:
            """
            saturated uint32 term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._term

        @term.setter
        def term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._term = x
            else:
                raise ValueError(f'term: value {x} is not in [0, 4294967295]')

        @property
        def last_log_term(self) -> int:
            """
            saturated uint32 last_log_term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._last_log_term

        @last_log_term.setter
        def last_log_term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._last_log_term = x
            else:
                raise ValueError(f'last_log_term: value {x} is not in [0, 4294967295]')

        @property
        def last_log_index(self) -> int:
            """
            saturated uint16 last_log_index
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._last_log_index

        @last_log_index.setter
        def last_log_index(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._last_log_index = x
            else:
                raise ValueError(f'last_log_index: value {x} is not in [0, 65535]')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
            _ser_.add_aligned_u32(max(min(self.last_log_term, 4294967295), 0))
            _ser_.add_aligned_u16(max(min(self.last_log_index, 65535), 0))
            _ser_.pad_to_alignment(8)
            assert 80 <= (_ser_.current_bit_length - _base_offset_) <= 80, \
                'Bad serialization of uavcan.pnp.cluster.RequestVote.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> RequestVote_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "term"
            _f0_ = _des_.fetch_aligned_u32()
            # Temporary _f1_ holds the value of "last_log_term"
            _f1_ = _des_.fetch_aligned_u32()
            # Temporary _f2_ holds the value of "last_log_index"
            _f2_ = _des_.fetch_aligned_u16()
            self = RequestVote_1_0.Request(
                term=_f0_,
                last_log_term=_f1_,
                last_log_index=_f2_)
            _des_.pad_to_alignment(8)
            assert 80 <= (_des_.consumed_bit_length - _base_offset_) <= 80, \
                'Bad deserialization of uavcan.pnp.cluster.RequestVote.Request.1.0'
            assert isinstance(self, RequestVote_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'term=%s' % self.term,
                'last_log_term=%s' % self.last_log_term,
                'last_log_index=%s' % self.last_log_index,
            ])
            return f'uavcan.pnp.cluster.RequestVote.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 391
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8=q@;80{?YYZEqYk5Wc8sk|s?_6&i{v=prB-5?LBmfOu~kC{#x-$F<ETkmcQ-+*tK`7u$Q>AtALNK&@nnNHO2}sf>5?a(TH('
            '(T-o9@ys*N%srp|_pSL>{pW6%<IH3-W(Kt2QvAUa2{B8Hyey2c;N9|fAVp4Q_GDawKky&E@PGQYn`1&L&>mZE`LWeiYAX$=uUuw|'
            '=j39&;=`1yxKw4F%F0;KaUXuGz}Vfw!jbLW0vm!hqENx>{O+NB;5##&*5CexcT0?0t3^^-F#cD1VoLnSx4gUjP=L%%f?8x5x18A!'
            '=`?t$L&joAH&&l2BL)hxN6Nwg^yv(jSRyQwpavFwCnD!5H<sl^1|HvZYrP{!0Tyr3*>*Uhj9P#BzIU%PW4X$>&L$nbtP)&wvqV$w'
            '-7L$B)Vr3a%^S_LcoT0OT5oqEyp8YTdktn;hUaB5U^N)m@q;O_l}XsOW0+7Gj0or2eb@sX*&?zCQJ?SGsN^N>>=inKQ7O6NmZ}p|'
            'T;NtG>cWz7Q}^)D`?!W5VH-DbqawC4C^e*<#N=POYiv)9AY)~rEfbmVy6emol}>>UB(Rbb7j8a$q)5EG(j!TZdSUl~xS#o$iu;rb'
            'XGo+ue`Z9UX`W&+q;)w?$0c&PkwIQ~cdM)tDN?3kP|5K8i3kWi*XYx`OQcYG@ld1Q-Mstx<|(Ca#&_Z%7;i)MRvB_bVQNq|C}=2B'
            '@Gprxe1gJ6!FxnsPRwZ=6?-RCriC(~Oht!sP-tN>kE5OhZXnW=#MeIVmnEp|dqoU`sSA*S<wBY`$Rm-I!upYrPh><9*|Tf!u09a<'
            'r+WREmWM)imsmlGN7I~`ah?>!AEmrad{Uc)((jNQxGnVLOh{2sv*C_=t;e%WsKL2Q#Ldsg){eWeRj42cb)idlrSV7%hjyPp?q1;S'
            'm)b%$?IuOlt)%37eD0k&HsrDb|Br8XqJ5LlC@Px-X!ukK(VPnvI-CqX3dVfsauQQOFEZ)~uIg#krH(3^K=hF}FbP(jdpM;3-|1i+'
            'F4^Gt{PrYv<rv$eOT9_#LUn%IB%zye39sS`UJop+QR{60-aXrj_{l5$w2PnN7j66!zrwHa8~hgU;eC97TS43SkaUbcP?j*F;#j}^'
            'e8#O&|2Dq`nj!FvKJ^$qGmYNq%!J|A43{6V(<IcLQmC_Bol?geeXa)3hZ3xqCb?%#MeYz_($~U%O-I$mA;lgz>MVr)*1oC9s(B5E'
            '|6Onxpz;4Pz+87I2LJ#'
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
                     term:         None | int | _np_.uint32 = None,
                     vote_granted: None | bool = None) -> None:
            """
            uavcan.pnp.cluster.RequestVote.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param term:         saturated uint32 term
            :param vote_granted: saturated bool vote_granted
            """
            self._term:         int
            self._vote_granted: bool

            self.term = term if term is not None else 0  # type: ignore

            self.vote_granted = vote_granted if vote_granted is not None else False

        @property
        def term(self) -> int:
            """
            saturated uint32 term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._term

        @term.setter
        def term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._term = x
            else:
                raise ValueError(f'term: value {x} is not in [0, 4294967295]')

        @property
        def vote_granted(self) -> bool:
            """
            saturated bool vote_granted
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._vote_granted

        @vote_granted.setter
        def vote_granted(self, x: bool) -> None:
            self._vote_granted = bool(x)  # Cast to bool implements saturation

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
            _ser_.add_unaligned_bit(self.vote_granted)
            _ser_.pad_to_alignment(8)
            assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 40, \
                'Bad serialization of uavcan.pnp.cluster.RequestVote.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> RequestVote_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f3_ holds the value of "term"
            _f3_ = _des_.fetch_aligned_u32()
            # Temporary _f4_ holds the value of "vote_granted"
            _f4_ = _des_.fetch_unaligned_bit()
            self = RequestVote_1_0.Response(
                term=_f3_,
                vote_granted=_f4_)
            _des_.pad_to_alignment(8)
            assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 40, \
                'Bad deserialization of uavcan.pnp.cluster.RequestVote.Response.1.0'
            assert isinstance(self, RequestVote_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'term=%s' % self.term,
                'vote_granted=%s' % self.vote_granted,
            ])
            return f'uavcan.pnp.cluster.RequestVote.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 391
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8=q@;80{?YX?{6G65WQ2=Bu!FE6&i|)=v9>T_`s4<Bq+btR3KP#oUXJ&Ldf#2CpV^Ed$GNz91>Fd0n|vAh!pdkKb7%qnp|je'
            '(rLY8&-2WCZ}!Q;KW{E}X1{Q~o(d;a#vEA5mHeF-3Nlujsy0q~h~eUWP_m+>_;Ff8JdE!?jeo>`SY%Rbun{}q;sbA+(l-`PA34u7'
            'uL$B+!zU%zS*`1=RE_gsvl0B(fb)-x2U@$@Xh$cP*#xYUMkm;%M@Q?!n0NEeU-4-StBiYZWzl$W@fW(|j0TQR#c=*>2}+z)wZa7V'
            'ocUDhS?RS+Ez1d=SbwOU9BUBYY7b+ur(0ZQh4f5;9(#;=kHAarJgba=h;M|A;d7vrmTlACPTHc5I)BDd46iZgxfa}td7x)afh%Ew'
            'c&cJpV8WC!bRq?>wAbQQ!d|^+i~_Dt6@+i)UA&HO<IVjU#@d7kW@F2#coA_k^hdA@w&zXHBlJdm*Y|2(Q)JiJ9_-bMYwn5kjIM*Q'
            'K1Vkzrmddons;ymGwe4+fPmUU$rJv5c!llCJrJxm)-x&MAY5k7G`0lVP{3+V?S-ZEP_l^O!jNpXH%!q(qO<!x>GhDbaAdrSKX$Sb'
            'mX~NI^j=TPX^mXHC!jJhT&tTx$&y(ZH!59!qAO)Dww{aO9J!8eJn~%(SMS`tead~ev#l(7Ao?W8Iz#TLObgm4Q%qzD@fmL7EfS(o'
            'guMCOGADx3LI3~v7}oAd|NZR!0lgk66wWb2_4LjHanq_W)D~5;Lv4~FlNvveLfjiWKYk@jvNh)6(vS-w_4tKDIK-XfRUWQv8=Z90'
            'FNF*jT109*4c1)dXb$7jpizq3=?mG5Y{FFo@$cBrdk3zdQLfvvXn31~$g8AI6G98VmljKDN=Uhsy~4<PT+gO`K*lX*pa==AOK9K<'
            '#QX+I`u|EBDjgc<%S{URDcnB}yCNAMS8)wr#mlLa4eSGM&AS#q*vC5q{189t<HvXxKfzD&GyELCz%TKuWCPr8C10Yth%g^_o^-<o'
            'S-t%fT86*{J!T&fymmZ$J(|56c{hzV-b_<`AHQi^`EHKTpW4vRskr%06K|&!dws<97)DTomuK1Fam(ixCCp<jAIylr0ZOVpv6C;S'
            'c;~>)XqqvaHvfIeW=hTe17!8P1}6pp00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.pnp.cluster.RequestVote.1.0()'


    _FIXED_PORT_ID_ = 391
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8=q@;80{^X6-)|d55RTO}ar2`|6&er`;VMvYp*2mB5Wghaq%9yf!E(|_2%**9-Nv)(dGFZWGjR&2eE=G1fru>cm3ZX=^`U*@'
        'g?|cxcwqL<iJjPPp%5v$z1{g{cE0&$&bNnu{B3L~`!mlctx$zgnJ6YXjrcb8BUUCs+(=@@HM3@Xjmaht*m^5rcF&%@W52K^Gf5=-'
        'G-XN??e<~FOkQCTZy+Q*Y&k->5KLw!Yg(p(PUR72$BCc~47HHbW<W(b5lK0SQl*(J*YYqMv1a>gYl@`Fq~ft~UPm|D>pfd3REEB`'
        'ckt4LYAv~+YNqTb7-B%42UgY`zs6Y<b}ltWLaJ$=-XM4)UB<kL7Be@5;&s8o4}@lQCJ$#gPJFIO#6(?#t$64>pvYY#4w1WgGh5wv'
        '<Y47xJX>)`n9<Nzwr0&!L}@BQD#LC^cT*px%rMf_ux6NqabV4m#m#5)u<#ss?bQnv4_<^4oXs(lkqaNib&`SM6*xBlHr)+7c>v=g'
        'WLt<cr5f90($lf0fq6B$sl9|IxU(5ck8LFp6;xw&%6KnkX1eM^{8nCf7wBb}gGD$GufxR@*$P=ASwK-tcE_9~n|zCfB#EUaJhZFk'
        '6j5<11BM3?BMC(=%&2=r+_&aL6{WjXb-R1Wec@Fs?hP!QvSzYDZz|phB@G~M;(O8xS_#nTe8?KHHFHVoM?64r*VD*_?}z}=Be_1U'
        'Ife?wh;5Bp^UP~+E*?_qV);VZ3C3zyy%_>j;WZ@_+9}Ajlf8@N!8&l|Iqx1mDKaOu7jJf`3}T^}P$?cp^;mKZjj~sb7*))Z-Na`;'
        'E++{S;Z=bQGnEw}WSa6wm7P5N2vb<t7jj2Ncq4uE-I|FduCHhBYxvq0vN=X#OxzpfM70`zjQnBBE669di7WkwC<m%z**y~i;Mi=i'
        'Zl<a<47sTH7{N!daj;r9r<Y^l1R?smG$(S8$gpeoF6763ywPk0;UG)A)oL0=RJMBJjF2XcQf9xmrHZ$!d>lndo&XM?)JK{dT(}O$'
        '1>JIsQP<@tCWjs)*b!7@(`pqvO6M2(Y~LGGK5SPm!7cp%91p&9MlI*Kce@)qeSoc^QMDUeOnbML@46YL;S`*PS;xX0w%$bsZyaq!'
        'cxwmVUWIqy-4a}a%diB?a0RZyHFyu+ciM&u>KLwLmTU`)qwUJ=f|<qs&A$bb0HYy3@~_0<X|zx&xZ#!$mldey39St%)KRVuspIJy'
        '6?Il)3DbO#<Zk8_xqyIfU&Y;wj_p;rg?D!xRf=wZXjf%qWxTq>dwmWa6z7v<Dsi3KPII(<voV-xucpjPkNvjgE^MbLkDcPf{fGCw'
        '8DENH91`NtM+nh{9KDmFCz=?S)Fl;e%>LU^o@?a++=pM`;Xl>Mx&CE-k{<1m!+x81D0Q!Yn-mV(<O~{}>1~q|ZkLX>$uFIX+=qux'
        'n)tU)T;Cn3<PZN{`}f+bpZ<SgqekW*t=hg~Eh28T{p+w-oIm4fQ67jrJ8pCO2mB6y!Jj#&E8i3z$?A?9JE>p(8{3m9+RX|800'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
