# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/pnp/cluster/390.AppendEntries.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:15.827235 UTC
# Is deprecated: no
# Fixed port ID: 390
# Full name:     uavcan.pnp.cluster.AppendEntries
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.pnp.cluster


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class AppendEntries_1_0:
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
        DEFAULT_MIN_ELECTION_TIMEOUT: int = 2
        DEFAULT_MAX_ELECTION_TIMEOUT: int = 4

        def __init__(self,
                     term:           None | int | _np_.uint32 = None,
                     prev_log_term:  None | int | _np_.uint32 = None,
                     prev_log_index: None | int | _np_.uint16 = None,
                     leader_commit:  None | int | _np_.uint16 = None,
                     entries:        None | _NDArray_[_np_.object_] | list[uavcan.pnp.cluster.Entry_1_0] = None) -> None:
            """
            uavcan.pnp.cluster.AppendEntries.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param term:           saturated uint32 term
            :param prev_log_term:  saturated uint32 prev_log_term
            :param prev_log_index: saturated uint16 prev_log_index
            :param leader_commit:  saturated uint16 leader_commit
            :param entries:        uavcan.pnp.cluster.Entry.1.0[<=1] entries
            """
            self._term:           int
            self._prev_log_term:  int
            self._prev_log_index: int
            self._leader_commit:  int
            self._entries:        _NDArray_[_np_.object_]

            self.term = term if term is not None else 0  # type: ignore

            self.prev_log_term = prev_log_term if prev_log_term is not None else 0  # type: ignore

            self.prev_log_index = prev_log_index if prev_log_index is not None else 0  # type: ignore

            self.leader_commit = leader_commit if leader_commit is not None else 0  # type: ignore

            if entries is None:
                self.entries = _np_.array([], _np_.object_)
            else:
                if isinstance(entries, _np_.ndarray) and entries.dtype == _np_.object_ and entries.ndim == 1 and entries.size <= 1:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._entries = entries
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    entries = _np_.array(entries, _np_.object_).flatten()
                    if not entries.size <= 1:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'entries: invalid array length: not {entries.size} <= 1')
                    self._entries = entries
                assert isinstance(self._entries, _np_.ndarray)
                assert self._entries.dtype == _np_.object_  # type: ignore
                assert self._entries.ndim == 1
                assert len(self._entries) <= 1

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
        def prev_log_term(self) -> int:
            """
            saturated uint32 prev_log_term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._prev_log_term

        @prev_log_term.setter
        def prev_log_term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._prev_log_term = x
            else:
                raise ValueError(f'prev_log_term: value {x} is not in [0, 4294967295]')

        @property
        def prev_log_index(self) -> int:
            """
            saturated uint16 prev_log_index
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._prev_log_index

        @prev_log_index.setter
        def prev_log_index(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._prev_log_index = x
            else:
                raise ValueError(f'prev_log_index: value {x} is not in [0, 65535]')

        @property
        def leader_commit(self) -> int:
            """
            saturated uint16 leader_commit
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._leader_commit

        @leader_commit.setter
        def leader_commit(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._leader_commit = x
            else:
                raise ValueError(f'leader_commit: value {x} is not in [0, 65535]')

        @property
        def entries(self) -> _NDArray_[_np_.object_]:
            """
            uavcan.pnp.cluster.Entry.1.0[<=1] entries
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._entries

        @entries.setter
        def entries(self, x: _NDArray_[_np_.object_] | list[uavcan.pnp.cluster.Entry_1_0]) -> None:
            if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 1:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._entries = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.object_).flatten()
                if not x.size <= 1:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'entries: invalid array length: not {x.size} <= 1')
                self._entries = x
            assert isinstance(self._entries, _np_.ndarray)
            assert self._entries.dtype == _np_.object_  # type: ignore
            assert self._entries.ndim == 1
            assert len(self._entries) <= 1

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
            _ser_.add_aligned_u32(max(min(self.prev_log_term, 4294967295), 0))
            _ser_.add_aligned_u16(max(min(self.prev_log_index, 65535), 0))
            _ser_.add_aligned_u16(max(min(self.leader_commit, 65535), 0))
            _ser_.pad_to_alignment(8)
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.entries) <= 1, 'self.entries: uavcan.pnp.cluster.Entry.1.0[<=1]'
            _ser_.add_aligned_u8(len(self.entries))
            for _elem0_ in self.entries:
                _ser_.pad_to_alignment(8)
                _elem0_._serialize_(_ser_)
                assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            _ser_.pad_to_alignment(8)
            assert 104 <= (_ser_.current_bit_length - _base_offset_) <= 280, \
                'Bad serialization of uavcan.pnp.cluster.AppendEntries.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> AppendEntries_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "term"
            _f0_ = _des_.fetch_aligned_u32()
            # Temporary _f1_ holds the value of "prev_log_term"
            _f1_ = _des_.fetch_aligned_u32()
            # Temporary _f2_ holds the value of "prev_log_index"
            _f2_ = _des_.fetch_aligned_u16()
            # Temporary _f3_ holds the value of "leader_commit"
            _f3_ = _des_.fetch_aligned_u16()
            # Temporary _f4_ holds the value of "entries"
            _des_.pad_to_alignment(8)
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 1:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 1')
            _f4_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
            for _i0_ in range(_len0_):
                _des_.pad_to_alignment(8)
                _e0_ = uavcan.pnp.cluster.Entry_1_0._deserialize_(_des_)
                assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
                _f4_[_i0_] = _e0_
            assert len(_f4_) <= 1, 'uavcan.pnp.cluster.Entry.1.0[<=1]'
            _des_.pad_to_alignment(8)
            self = AppendEntries_1_0.Request(
                term=_f0_,
                prev_log_term=_f1_,
                prev_log_index=_f2_,
                leader_commit=_f3_,
                entries=_f4_)
            _des_.pad_to_alignment(8)
            assert 104 <= (_des_.consumed_bit_length - _base_offset_) <= 280, \
                'Bad deserialization of uavcan.pnp.cluster.AppendEntries.Request.1.0'
            assert isinstance(self, AppendEntries_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'term=%s' % self.term,
                'prev_log_term=%s' % self.prev_log_term,
                'prev_log_index=%s' % self.prev_log_index,
                'leader_commit=%s' % self.leader_commit,
                'entries=%s' % _np_.array2string(self.entries, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            ])
            return f'uavcan.pnp.cluster.AppendEntries.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 390
        _EXTENT_BYTES_ = 96

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8D=Ii+0{`t>ON<=HdG00mF>G?Frbtmsi4sc`Mb65zBa(WUqAXhs9}(T+0~9F}u$58GbnR3xd%8#6J-b{12INBmIT#=VXae{+'
            'N8d6>-F)@M2y%*(Aa5j59tR%+L_lC5|6lc2O;69R#0UtGg9M0G(_PQMzVG}0>Z<*C{*Qn0T}S=bKhfO|vLLEAGLeQn3P0k_NYopx'
            'q|;5ZFc-uA@)Z$<9mocEx4UBa>2UQY!ygZ;{l!KY$08j{r@#Dep7vUKFBQ{878)_{Koiv--)!-?-i^EUR@BRKk=8GDyCM#*#(5fw'
            'tbRv)*b`Yk>{l9_BF(}i#&(z9qx`2sf6jOQVEB_^e}9ALP^a0;MK*jNI@x6gw$!k{a4i&3Fd3HH2zbsLIgWL=>fIFQ9Bx91!}sDW'
            'Y{w$F9_OMh(&;(wZ#2Wa5sA2+%c0Mp@fOeWMkfixP#)_ay=@x8YW2(T?gqYs89Bc{yff?{X=FK%1D*!OhCb;vrQ4qeLv@Dz`9_em'
            'hJ9xU51-K8$`$!E<(~DKJRzT#r*xg=ZYnk#QPOUx%JQ^4vr9FvSnZ&#7RG^i_{jB^Bf$faB4A*eP_19RBi2RA@`UA5useJ`XI<Wf'
            'C+kVd#KUgHW1hpJ)~BY^e|nc?OjEu+>_7P)ho|u59c7<O_;h+5mK!1x9TDexUF8zB?Dki7Kp*06dngacg9cdg5P<2c%{xz4{hHI1'
            '7yC!9g%3rr+dSm=3O!eB&;5M>t1fSa`S#HF01?e78}?5dn@x}d=F7{!hy4S;6Xv?dci|`X)!*Aly2C!(t&wcI(@dfekazfo=p?Wr'
            'IG<ZEN1i8XQ3zTx1b)dM^&h_@x*`vEF1M%g0LCsklzZ%EFN%1&T`mM|ZStrmhJQ4y`jtV}gqhDbI$=EYKgJAyh?ym1S1;n&sy~NC'
            'oq@lH(!H4O8Tj+`djZqE1Amd8FHu^d_xtF#tGo2~W4bi(576&rO!p7`gH-M@dhSvELzwOx_>a^3!<Zf%_(!PR6ZHHjrjHN&Cox?f'
            '_$&1O7>(~KOjic})0iF^_{TBz2L3ac9vJw~Quz~@&JTP>{Xd84GXwu5rcVw0=P`Y9;Gd#)UcmIwz&}mnIz#iRQhTeIE)4t^X`J7}'
            '^u>W+!?Zf^*DyUj@aveK8u%|^dUD{O#gq;FbC^Cm@Xup<eBi%K<9LPU^D3rC2mWg`o^O*KF3|j5r*U1RdA@<EJMh0l<9id+#ex4_'
            'n)ml;oNv+m-^TR9z`sx9mDKM;s{aY59}oPWQTlUAKcn=Ql>VC1&nf*vr#C8dlvy#Es>xh1nYT^mzR5_Fd1x}9n9R>i=I18!naTXp'
            'WPWWjpPS4Vl<9$k0d?WA@{9DWi9`W$+SiLi@S}||K!vK`Q@_@(Ut!5Qs8pCS9z{t@(fAGakw_C3uCreJAWpW*IyI5cgCw6ZxUKs2'
            'D>I_`)jncDb6UF;-alOM;Em?CjuC!5lz%P%A_I3C2yjI(ND&Nw+CSJ>N40EplQhR^-RvJ~WJxb=33w5SMwf%L>@Q&wh0S4q-))Fm'
            '9^S^MpMvDfy#(I>9(WWG%jFJ#kcFKf<t>?P!td^OYr89Xv=)H64Z#8RnxJ-#RJ1``p!-Rb0JRsj6~Gyz9Uu(3ex-h{ezuO%In2?K'
            'A8tsV!GKcqLD1!9*b>8^!aDroidYY00oG?&7uKWh-UXilY8G~S9R}731Ey@mV2xn@5EwxtEQytG>A|lw+79D3%Tri*v;~X!Hn=hO'
            'J*<_nDA__^Bzervoxi|f46xK&d^@AY(I>&$PwHoNcglZdUC|2HLyZkpypup9VZ5Hyhw`4huU1z6Q2rh*u~PBdJP2S|Gg1$4rLOQm'
            'vpj1;VAs{9hkgZ6(E*6W@PD$ahR>BWe2z4Heisd2A`M?84PPJ)pC=99Thj2kl7@Sv;T~zYM;h*thI^#p9%;Bo8t##Xd!*qWX}DL?'
            'aE~<HBMtXR!#&b)k2KsP4fjaHJ<@QGG~6Q%_ejG%(r}M7+#?P5NW(qSaE~<HBMtXR!#&b)k2KsP4fjaHJ<@QGG~6Q%_evV>k%oJu'
            ';T~zYM;h*thI^#p9%;Bo8t##Xd!*qWX}Cuk?vaLjq~RWExJMf9k%oJu;T~zYXEfY18txel_l$;nM#DX$;hxcO&uF-3G~6>9?imgD'
            'jD~wg!#$(np3!j6Xt+1%$zM^%2=@{S1IhN&H?>IYAlj(WLjDah?ECVX{8RbP#*gM4NB&t){@qXI-`|w~ApfZ<|5^Tv{9OL4{5SdU'
            '{k;(Mf<98%JM14+f$y|($={$#{o$=xu-ox%qfv!!nNXELv|u!-hbU7V!d=iIHAsqoTS=UWIP2k%+esScvQuZbVS|tfmKN1UwK25;'
            'RFV^joQF}io8bJH%@sxHiOWfh-Xh*HI>opdgHsS?+$?^1Ya1~bQ~lWZ5OTYfFG?E&X_LS8=aix`P&B3$%_!3&MW=g8(dj%X+5#!s'
            '9#S;76qPQLqRo?{?I|hRW29&YNzs-`(GHNJ?I%TZNzwL|qS7T&v_(?11yZzmQnbCKXnRP}=1Ng1BSmARXp9t%k)knDG)9WXNYNN6'
            '8Y4wxq-cy3jgg`;QZz=2#!68sBSmARXp9t%k)knDG)9WXNYNN68Y4wxq-cy3jgg`;QZz=2#z@f^DH<b1W29(|6pfLhF;X-}ipEIM'
            '7%3VfMPsCBj1-L-MPo+Mm{Bxl6pa~0V@A=KQ8Z>0jTuE_M$wp2G-ecy8AW48(U?&*W)zJXMT1OJHbjPG7y%hZk3fd9n|DfXezD}<'
            '9U{YG$-U1L85W5QZix&_CHGz-GB`wrWg^2Ok>O~`y}Lw)c_PCxBEu0P!(&7Sm&mYCBExYa!wQk%NXfk)ATm^l4D&<=hsf{(k>Mnf'
            ';RKQ4IFaEPk>Mzj;c&^lFB2JDBEu4qVV=k^M`U<~$Z(#>aF)nWCo<HC3@;KHszip<M21sDhLa^S82A1*k>LW7p-N;}Au?2m3?m}L'
            'h{!M^GK`1}BO=4dkYQxVFfwEq88VCv8AgT-BSVIfA;ZX!VPwcKGGrJTGK>rvMurR{Lxzzd!^n_fgk<<F1-sv{;Ttx5!-oIVu3-#h'
            '7=Mj8X|5C}&6VOLv-5LGancfzp+aQXUn0X|DNb4_?ffc428YP-SSe1LBQhKzG8`l_REP|Fhzw5=8J;NZ{Pq(W7KsdVr8wz0kzs|%'
            'aHO>JJ3wTp5E<r)3=WZDmB?_K$nbnAPI`vO@D!2ZNg~4$BEumf!$Bg$ej-DK$gn_U*h6HvNMyJ`WO$9p@CuRPJdxpSDNb^T3~v(|'
            'E)W^2M1~b2LxspNCNhkP3}Yh0n8+|TWEdMVj13vah74mvhOr^T*pOjt$S^i!7#lK-4H?FU3}Zuvu_43QkYQ}dFg9cu7hS_QZ1{!^'
            'nhgbXsP6)I{ki_*=1688&oJq1Yx;!fIe!jM67|>Cop#PU>}!jASUhK$+EPDxhsSO4Wk)%SjR*QLW)50!Lz@c8&Lbk(nZdGS(d<|}'
            'I~LK7#k4bnYRBT*vB-8Tww)PtI~L!LMYv-z?pTyNGdOoF(jAL+$D-Y_cy}z~9gBI#qTaE%cP#Q9i+#tU-?8|2ECU?N0mrhyu{>}r'
            '6CBG0$Fjk(d~jwM;aE;MmKBcWg=3lFSZ+9$9ggLPV;SODjyRSjj^&ACnc`TkIF>Dr<%?q(<5<o(mNky$jWc16qqw7kj0%A9vqy=z'
            'XAcX}Kw4UD+^tF}FjnxHYjgXF`UmWjWu4n&WOj0Bh;KbAe@H($NMKa&bR=#+)2L@!a_z_G3W2eLqg}D@j_KS!0;B5lX`MT2<kx<P'
            'u3*&rtnJ~1&OJk5tRSGC)49V0Mm5goZ6Bv>-4}H3l!?~ur<@7`v})U1)wv@^n(asG3Ieo7Gh4Im*6kc$(z$OD7%LbIoYT1%2#ghs'
            'u3y%<69h)p|EoH8jKHXD@ohV^3w9*0Tf1Mh_IX3+mdrsUj_OUFn<Fq*{O=GLD+t=Rbnb!yW5xfh@PSw8@0>$<`u?AQUj86Svz)c`'
            'm(gxy4qo!GBN$#HxRylvOsB<T))Wly<MeV7FrHm>UB<Rl{h6w7va0!fYpx5dvKLwPJcHi58Gfye#lu|R@lbD4ees5caW2wL9!>SW'
            '>bh6!?Rt&1!%d+Nqh`uOlV|I%vP`s+ILK<M(AJmC4nOo>zI2l{dl?J$Wbnuehn>NI%t&7>whHsYGW4tN>MzmwF&aAKoun7*57F3u'
            'n6s@AkGl8+-5G}|Z%quECom@bQmw8m!Q1s7l%`>t&)Gqk(FtY1qNJ_PMi2KZm$4d;^T|Qi%8s`+V8M@Hxq9u=y?5?5Zd||Fxcbi3'
            '%XhEey4kpU{l?W>_wM3n{>l&ablwLq+<(U0!4MC-smSnbcj^jK<&Lr-k4(={XWx3tTlh4C_tz*7@B4G-hZqka@;3f*FM0k)8tSF{'
            'I}P>zS!l$J*8N=zg-#f&^GgwlmR;YZ2R4lZRe(+%SQdUHYHnUQ^28PBbnuunm_-ypJ`gE%g@}h`#KqHKfhNAZI&c6+HZ!VK_7Z@L'
            'N@wt+S{xo*W9L>~bu0@dG+cR>^*RDU#&b2Fchps<NgGKlCb;5=CG4xlvc%R&#hDCWb&@Ps<?+k|PjXv4id?J{Z^KKxw^V2E_F58V'
            'F8O8%xCMA8U1$)d1SSAjw^G4#b&TALLqK*%aVSc7P-8sGWzuU)EQi$SboFH@HIp@Sx?6W|HKFZZ7H!vdW;5BoaGtDY5~6MhFn105'
            '%$W?^Fg1N-ovG92ILW70g)45t)cCgB;=OEQs0<kh$jL*P3<I=xI9?pI>ji_4wR8X%0pcATO_o7F>Vzob+gbpGg_}J&PXTyI2Uat{'
            'Hq`tukY!ciV2uH~-v>jrT1l!_VCLplo!!+{R3jP#ZTQ)XcnU)5W?<ncK=Xh_@Kj5$Xb03L)a<|^YTML-p&S2b$Ork)A>W^S#WItQ'
            '@m`QeWldJ)Ik_fZljk@79E!;c8-EMQ#$Vw-zrlb01OD0Vh;O3-?quTw_^1EW%dej;-K#7e^nC(sjt)7_*E-3&JNp)D!`kZm1)AT8'
            'q?pGoLG8IkDJ>i+=6IP8Y?*Hfkdssdy*L16HATRI=nggYalODlw7@l}+97H}OLa|`B*ep(#Kq3s**14L)l}_Y&smTFun@ew+l{sj'
            'CJg*y;Lc7%0~QE{YBwZ;s2a)}m8S?p&7h8QBuM&gE05hYX@S=3j%LnWae+VpL!>`cKrgkeo2a{2&19_ssiHtS#zA4Iik$)23e{jj'
            '447`3fP+B}g2rXMO{cN}-c?b%K4O^#z+|P1KAliAGi}~Vfwem>tj63r4^x;?5Q1#v?zCWi6&7o#FY3BZCMR=JBz8|;kJ-C|ry!-!'
            '3JBOeygsAv*y6x0+vYCWnN_bo%(ZUOh2zzethvpugrc3WTXCDGi8AZ=6B)Bx%4>iY<oX)V1fe;ER<m9s)m{T3%Rwtbo<e|<%gK<*'
            '&}y;}Y~X}*;8DgXW>nU|wNYpHtV+|(P#W>>R0e^bSgo-wbT>?F3Miyb>?bW*W8&>qH|}+sBCXNoBDy11o4D;Hg&3rpXh&tBsa3WL'
            '%a0ewGIR;(lawSPftuEvAWG7t18bb&a<*J-VpY*O6@VX6n~VqNYvQ;W=H!`(*1<aOhNvgS_(9JA4P$I%aJ>Wl==M6U=)@-!NT=PH'
            '9u$nnHIXycZ6<j8Dwr937V|FngIwRJ!mABvJ-vFJu8zfkvoX1}iHrQO2Y?T1u8I-BL7F#;Txt?C?t6+26Fqj_A4p_=JfRlKQlh~p'
            'n7)`jO(h-i)YQsJ(R!ekG2an<oUVN+#)lZ~Y{f2_Ok+hO02MSolh=xU@*v1eotb+iMr5(K>J$V`^nv;UkPZ}2Tn#rO6L=E{gNjzM'
            'wu0>nE)y=A38C6O4$Grd(bCb*lrG3kCQMG<MW?PtTGJ8Sy1EIc;woIJSfFZiJ&~-}RoC%i(dHPcYd`~YT8JoADUjJDo1m`{ZWMt{'
            'JlKMz6>CXMUcw+Z#6Tq3%4JR6;+t4hBMTbq@K}YAYW~1pAVtf#5eRuiSFr(Lr+U1s?mcQ9-V`!yp)2lXdRf6B>tVZ>TI^AYGnvA6'
            'f*obX7_eUf`Gz5aEwoPp?xPIEd9)4TW)w_~)-G@-+0^rbU`%hypqen0)YpM<+g7X$7KC9yEQV5BT**X%%$<0cH(*^r|840^qS>0t'
            'QW!Wx*BR(Y1WrMyXc)9JjPy#x;8BzGfx3wa@U5`~L9i8)e=qXLRU1v-%aac3oObScE;`*@Z!?wSr}c$s5#>;rfTiFMwQ#G8QA)G6'
            '05@vvAUwti+rk)!W9t}(ZsF>q2y*mxIL<Sfm9;73;%<SPaYN)&c!wRuQ%$%#DPv&>%@p<=_*X6_beOoPE5Of0d7xd~6tF!Hqp9s-'
            'n7KN-38*qgiaLlX_KLTZcbhB$U!WV$l=vq*NG7<C2U;9m(>IUQ&TI<vYYK{MssTks2#;a>x!w`w6EvAxItncfm*mMng`C{Pap?~p'
            'WF#}3s`B380|2xl0>~+Z;Zg(0)&dv<l5G`GaR=?#nbhnEY&er)mzmhmxE9hV+`MH*a3+pN@9XGGNkI&tk4qVo9OV?;jQWd~FrGwP'
            'Z4rwUM5Gv&)0}s?MYt~1POnz9lD6d*&tXkr2rgYlr^tbf1i>m1nYe?)Lkt&Vb-r7)UL$5@4+=4L!4&RH%s?vD>jpfZ#O*uuIPFv='
            'Y;QMBTxDdWlRz|`XwAYQs0q7MQbeA?`0E%q=X!Js<>e*D;o-vRzqqm&xFt__+F@10x~S`qFGep{@uLIyzB;?JQ*=(-T(v2hh*{D^'
            'FR4wL_KHrM79G?YDNGP`rxvh^9{?z9jA1T3ShZWIUBkACFT7}?l&Ma65hN~J-Xgy$)K^PxA_)u+u(JL(g5U6>2<f1lj9#Z{uLs3+'
            'TLEZB+{5Kx)$6JsyM~t`{+VPJ;*gc%uj5yY-GWh|)GgE#)lM(PKNO%v(MylGGn>LfUHiQWMNz<Rq%G7p5?Ftj6BSZhipegp?p`X!'
            'g>;K}OS=x({{+(=V6?A3vEcB)*iAqlnj{D(Q3fcW`T)1araY3em7Yvg2yyh3>Z<(pJS%@-wZ7YKz$p%cWzxV#=9%DLfmo9Sz0Ry{'
            'tWH6HOob_tzy=@;Kx-=Zf~t85R?X6>@T~%(`1N&wlEpp*ROpcqpCVK&)LwiGJEM;s_$7S}WSO4Yod9gB(ci#s9Y7iVFK#nG;{D_Q'
            'Z{@%GKD7MRO?Xf)r_br$f<kXi3Yog4$K^jK(RFV_q1&@{OOJQ1`vDaCpjcPm#+ZJ*ab>UL=<-s=H&*6mE0mt=^B%ch9*~~?lhUKI'
            'D%a$Bc|m{B!*6;22Os}7zJOx(Bj3h<<LAbuh6;%C;SFbR|7atizvE6DQvc0v`7!~MCpIqO7{2aJ0ycG%VB?lOeAu`HS+Fagxp;s!'
            'ya^_B_M!>RQEjGdsSJ-V*$ywUYW;rz_MTv)%02)9'
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
                     term:    None | int | _np_.uint32 = None,
                     success: None | bool = None) -> None:
            """
            uavcan.pnp.cluster.AppendEntries.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param term:    saturated uint32 term
            :param success: saturated bool success
            """
            self._term:    int
            self._success: bool

            self.term = term if term is not None else 0  # type: ignore

            self.success = success if success is not None else False

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
        def success(self) -> bool:
            """
            saturated bool success
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._success

        @success.setter
        def success(self, x: bool) -> None:
            self._success = bool(x)  # Cast to bool implements saturation

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
            _ser_.add_unaligned_bit(self.success)
            _ser_.pad_to_alignment(8)
            assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 40, \
                'Bad serialization of uavcan.pnp.cluster.AppendEntries.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> AppendEntries_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f5_ holds the value of "term"
            _f5_ = _des_.fetch_aligned_u32()
            # Temporary _f6_ holds the value of "success"
            _f6_ = _des_.fetch_unaligned_bit()
            self = AppendEntries_1_0.Response(
                term=_f5_,
                success=_f6_)
            _des_.pad_to_alignment(8)
            assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 40, \
                'Bad deserialization of uavcan.pnp.cluster.AppendEntries.Response.1.0'
            assert isinstance(self, AppendEntries_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'term=%s' % self.term,
                'success=%s' % self.success,
            ])
            return f'uavcan.pnp.cluster.AppendEntries.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 390
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8D=Ii+0{?YXZEqYk5WZ8>Bu!dM6&hY5(W@xo`hg`-Bq;AR1w@w|rz=HB2wC3s<i^zNwQTPxhlJFA05y^&BE@{?r!u}xlS|vI'
            'v|4*S^LS>SXZF#;zZ;94*%Pjrsc=GN%z>3$$v=3ZAY)}+nc7JYF<iO}N>;QKKTQq9!+7&?{4@5$B9mH!jo1m7?t9ymzOiuH<vi28'
            'B8Zy}pOjo@Mw_fujq_l$uZ;mMzR})FaM=i)skI~DWi|opWUUkM($7ch!<cvT&foEI46BTL3Mv{8F8)ThoKeEDR}AOBm7v5)UMoy+'
            '&zVojo)vCvDq2p+W9@-<a;!mouRV;xo-T5g71A>Wdh9XgJpwPe^Q@``M0`E051#_1uxy*ocG3}5)cGrpVt9o)&$ZxI%mY1X3S0>b'
            ')Tt_l1t#h;hE62o)%IF^jj&hm)U^VxPbGwJ=3TsoZ{dyo8OD-p$`YK5xEcB**ah43b<ZR8Mts-z3^!!it!)qXjN+Pm>UTyrL0FsX'
            'G%KbpndyeNaUC=4H&nX-W1-}vj<_FQV!Lt=1T(euOo})NSD33CTLK*@V1`p=VJUr-EMmAYB#rG2ll71~*?o_wdO$QdQeDL#I#~(J'
            'OROifH`8)zkgInERCNp+rYV#xnT2tq()A~lQuJagxERin<mkpD(Z%q_t=n7ANbmh@D@y{1KC!XJkUL7$g7!%f6Inuhf}8jbu}~<&'
            '-h8T;6Sm0FKf90N;vMOKnC<V=_K2Qvj@6V=?<^2Et%{loqfB<FP*P*!<459%``XS=Ux|`5jd{2{<U&Y2e$EMpxO2S9!`1CtC#LiZ'
            'A;X0hkqS>!H5WOW!?-+Xl;U>!T=XKFaMeKkC-(E+fh%Z^O`8@?Zc|Y6Dyh?W(1P!!#Znp(;x0w6FcKfvvr!+AYKs{tLPF~j8n^;6'
            'zmAgL-|0Xlr*XdABy*q4{bRE$lIn34FXGF1B~`MHeZZ}G-QoxPcx!+k;zxb_7;obz_$hvdpW_$!C4QA;fZHwQOOzKi%*UNa-LOt#'
            'Z~ugrA#g#T*&hTqjt8$tgLggern$x&X@u|McWo*6<{J7-Yx*@MH(zP$+bPCg9dSK|5g73DEEzm(`?*B{^H|FVvqs<mCFP#FlP@QG'
            '=fKU{H0x+O{O<*aDKz^Z4Vhx}CI$ci'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.pnp.cluster.AppendEntries.1.0()'


    _FIXED_PORT_ID_ = 390
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8D=Ii+0{`t>TZ|h=c5O<d8LIVaS+XqaVV7lD=Exjcl3%jD&RW(ZR@!<*58FxL&_#C5RF9h7-0tR##=rvJk1XtfKnR!t_LH9*'
        'BuM7dfBD_-MG)*qkOX-en`|B*3v7S{$h}p!ip?fRmW@piAQqshBD<cq&N=s1SMlSy-~Z`bj{4VsvbzyvLDXnwA`N*Ie#BdmXf)eN'
        'r<-J9E{6SGw?(=Zw#A)|t{8qcT>RefyTe+4Pcs$Y>4_|F=J>sI`g<;kDC|I$V6x<VGmK-Asv@`ZwAapiX{oUt&6szft6Gn*wRzm='
        '#@$9c>Seh|8yC7=5eJv!JPk$GxTQNC_N&b`k!E2MW4jCQQvS1{U-6yq55EV)Zt@)Jw0gP7h95vDTg=p!8uoWw2}Kl)hvhZ{o^w6H'
        't*UoZoO8GaB@Wz;vv4IA!PPhyD<Yko<E~~a%$t#jS8_S@88qJJV7*Qffc2i}AG&E8!fK6+@a!5sf*Co#GrTqIA8ckhj{}|t#fCoV'
        'wdB7392lxI?9VlWq&@6AL-_KD?p7X`jB-!=OrDfAxv1;x>84_>86_)CRarhK>swUwiq-boYGE9R`wv}jPb7FCQUn%E6RP!Vx5TnY'
        'S)Q<53U-Sx=d8=S@Xd0PGI75f@tEhZsEvu~^p9?_jA_a@hW*Fh<?t<h^NzC51^l)QToH+mhz)ReQ_K7Mhi9M<aknv)`{e-xEO`jP'
        '^yTKABddPRY07W+4_*oHi(spH$V-KutG4I<PJmUHx5Ip6=zD;OR+J6<r;N?U$N}@^<<G<Z?zh5R_jnsVQeXY;&7?c*v#lD*Hae{&'
        '3ITZsu8B?pD}wX60dwSek`{%aEkod!<o!o(iLS`Q+2yu1@4?vRGL+kQy%$A1-6$7=w$^ym6T{yd*8J)qYr)Ltnw>Bn`X6J4-^a`X'
        'va1(yY}Kz|QD@+9qjWo_+Xns|ecplT_JKc7-!D*FrRO{8v#Y!GcVW6P@ORVaJ(%tq_<O0`KKkCH`uj26Iq)B$=Lay|JMa%uxku^y'
        'Lzq4?@E^l;&%i%S&mX7p9l`YQz(0!V!GV7aQ*YoO$8`6=e}c+CiRs+HXVm{wm>wVaConxS@Sn!?v4MY*+Ia@k{R96Ljq6#OPmS7J'
        '#B|5NKTYF&4%5>Ezm92b;4fi%YT!38Jvs27$MnR&KZ7Y7_-8SFV&I>{^w_|EfyVJ7&F3Xd4-Nd6X*{ox9nRDIUZrupM)Q0fQ+MEh'
        'i^lf`rt<^;S7_efrg6SW^M4!D^8^2V8n2{&?^FFxF#UMo|A5jTQu;ZiKce&}lzu_!FLZjXTA|Eglc|}^d6RkDWZpL!X)^as<`a|o'
        'fyw;PWIi{UADPTgOy&!d`2}Tq;9x*qc&z*)eb+*wfH>{!#Uc37W*DGCHSVfUOII(kWEoT{%ovZNq^)TDI{QeZ2@985FTNKi>t&r9'
        '%jaH_&lucR<Lad;(fo2Bu|soOyA<9(Q1IZ*)`pG|zB`nEBmXi3cNz$AMKDMa3_tDfZ7!o)HoHlh<Fu~#_cybom$n5wh(xo?!CCef'
        'Fp0v}u)p&rL^t<u;<ulH<W!yq?|&CO3W(*N4!@U$ogn3HnXJL*?nZl~D|xgOfVvIA0rgs-b`bxpfVM#Q<0t`Y&uc4yGe$c=7;^Pe'
        '<80$h1Eq7Aqa#1ilstn0rRak)9a{}Qg?0GTOJX^U1z4Y9U09EXdk1_5s9D(Qbr@JD44ASJgEfNrLtq4ruq0N#r3atVXd{eQSf0Yd'
        'qb*p(H^7a#?_#ZtMaeq)BFSTR_S|^}V}PYz=NlO{jy?(2eq29mxD);>>xy=`9BOQ+;++H<3FGCYF_gb4KTs<xKa_1+Vx{6Yc@V&`'
        'rlcO8c65cVW_i|vz^<!H5B(~jA_a(K@IT*D!z(2XuaJh%ZK2@{q~Y_V;X6pf=Sai1mo&Um(r}M7+#?P5NW(qSaE~<HBMtXR!#&b)'
        'k2KsP4fjeK?vaLjq~RWExJMf9k%oJu;T~zYM;h*thI^#p9%;Bo8t##Xd!*qWX}Cuk?vaLjq~RWExJMf9k%oJu;T~zYM;h*thI^#p'
        'UP;3}(r}M7+#?P5NW(qSaE~<HBMtXR!#&b)k2KsP4fjaHJ<@QGG~6Q%_ejG%(r}M7+#?P5jD~wg!#$(np3!j6Xt-xI+%p>P84dT0'
        'hI>ZCJ)_~C(QwabxMwunGaBw04fh5;`D4l$;a)&tAlW{8U5msF(MF9H@^6u0H>5BBO#b>RuQ-nU^Pc?sPvt*cm;We#T9f}I|5^S_'
        '{)_xq`EUL05cGmRQrJ7}?^S{Cq;kohqe}hmjaaao@lB&qg>IQpl|Zy$G^mFtQyjuw&>=NQihtWloQXK=;gDC7G|XkE!EV9^ArmYu'
        's*P%6VgsloClEOgqiid|`A?fGiqNAMlNh~4JTp4QxEX^}5M|sfKDf2j42-Ehtgb<BtMWx@V<2s-+n}&tQKH5`)R-1EBTf$$pl&M#'
        'sB<K0J4n>Fk*K+)z;vEOZH`23TS?URk*Mt@QQJeJwwpw47m1onqPDXXm@bg0&6B9@AW@qmQQJ<Uwv9xsQVL8Ni5eqOV<c*fM2(TC'
        'F%mUKqQ*$n7>ODqQDY=(j6{u*s4)^XRtiiRi5eqOV<c*fM2(TCF%mUKqQ*$n7>ODqQDY=(j6{u*s4)^XMxw?@)EJ2xBT-`{YK%mU'
        'k*F~eHAbSwNYogK8Y59-Bx=lv8Z)BCjHodqYRrflGor?fs4*jI%!nE@qQ;D<F(Ycsh#E7Z#*C;jBWlcu8f02B5E+tT1Y{UJ1R2Vn'
        '-YI$d`I3ishz#>34?jm_m?tv0B{D3OJbabN;1C)15E<r)42Mb{-X${35g8sQG8`l_>?1O`M1~zDG8`i^940axEP43dM20GnVUEb)'
        '5E-5!GMpeXJV|6YMr3%L$Z&|raG>Pj_YfIeBEtfaVUEa9Au_y3WH?7;I74J;5E<%3hSNlb8j;}?k>Mnf;Y5iH#>2l&WH?V`s1X?s'
        '6B(*Rh7plrL}VBd8Ae2g5s_hJ$S^Ww7#T8*3>ij-3?oB^ks-s#kYQxVFfwEq88VCv8AgT-BSVIfA;ZX!VPwbv8S)M~<o$*a-w@*e'
        'Jt5?OXz#EIWZ3)~p;Dz3Dpg9MlG*<`rBG>s$WSFR>?)CAz7#6$DDD5ML<Wb*u&)#<Rfr4+i41#*3{@h-HX_3jBEzGl{ogJk!#t6p'
        'QVNxh5g85>84i~Af4hkcRU*S2k-;G{ED{+`5gDE?g-XYX3`d9zj}aLT5*hXr8TJwxb`cq>M1~zihHXTK*N6<~i3~3j8D1nZoFg)v'
        'DTPW7k>PD3!+9b@jmU7A$WSFRY!VqZi42=WhD{>FrXj<oA;YF2!=@p_rXj<oA;YF2!=@p_rXj<oA;YF2!=@p_rXj<oA;YF2!=@p_'
        'rXj;-$vb>Qh;Im?2~hxudO`3Tex?72Ih$F=!%RBlnmj5x<yY`XQNMPbwS}Is!7XlP@xWzbZ~fRU9<PW8o$1Us@99&S3bY<Un+nO!'
        'Ln7Ik!m?x0>{vWI7SWEyv@?Zj$Ku+t$aXBYohfuX7T=CVxMMNySd=?cICm`49gB6xqTR80cP!!^i+RVQ-m$oMEb<+TeaE8TvG{i^'
        '102f%$Fjh&Ja8-%9LojAvca)@aHbgHSWY;W6^`YFW0~PtZa9`5j^&4A8RA%uIF==j<%wgN;#jUYmMxCui(?t%Sk5?>HIC(tGiHvX'
        'xTE8YDuD6xhY7l;PYuyPT3T)Btx72{R`EO6=5`VFciV6F=-f6Vv*Xi4eCkp8{ra1|1V;5t2jli-jrvYYu6+w#B`{WTw1@4p$8~Ne'
        'fl>8&ROb#E`L%DPs~Gq`VS9K|=Z+H?s|cv4bnXCwQH}Fy+s8>;_Zgi#X##fpLZ^xVt=aY#b?%^%X8X3fiU6(C%$97s4Lir@b?!L='
        'V-@3pvpV+-fw77K_6s`qB!N-&|B}u<PGD5Fc*V}_ydBA_*6y!a`@F7m3+6-;NA-rzRS1k#|62scDuVV+ojY&9SoJ?Iyy+GCh38N{'
        '_x_)NUcQ&4S<c$}6=^pzCop-~5e#n=TuCB*xYOn_YYB!IczU@A7|&jFUB=c`{i&*Nu$p;~Ywis!veT?~jzRC;3}4&E;(o3#d#ERL'
        '?T3YNF48p~P4vF#x|bU(jXGNi*MvTmnko-Xo@u<qGSN=rAgilF>kpV6zVW?y;W}&eG8XE|;Mo-pJA(n4k)AHL3iHA;^r_+MSJL=a'
        '8am^hq!;Tq(%62Ov-J?qy!buc8HXvaj}4k9FeZFut?n+t)8!tNreT`*+CiAnQDwlQWJMj49`08!Vl^J;;}fsrGp}vHf*-qd`O1a6'
        '@7!r#yL!EO`JKxb?_9lcy?N*AwaYi|-of|%)!)+7`2f6d|G2q~A?|lmk>Mfl#9gH7EoDI-nVzA}&gGQ1@!JfZU!goa?^n(ZF&;qV'
        't^U<^^861q)C=#=8tVIJpb;}#_g5_xI$^91GDRfXc72l`*fb7Q0XlwQS@@BtyLsX46IY<q!Sl{w8c_uKK%~$WA|93z7f*u)ns{(^'
        '-~fzlYE+Btc>ouc&fr6>I6St*&Mvy@d=^S*xbiIPbp(Qp=W0Ihs5?*NHj-G3am5i!*jJrpiLH~0XES`%NwQp($HNai(rxo7a<NXl'
        '0T1y4Q-j^^wI$44^0g3f3-C_5&>&0+OaQQMr-J9|Jh>N#fb5RqP?YeX&Ulo|q_-lm98#mx)wiP5OqR?sZ^OOOg0_2Ev{9eUX0m<Z'
        'U|G#1MBNZz?mG0DGa0VH)b!bPrjDKCB%fFnuDA(P;~Q?9_p-5}GGrhiCl6sV4A9=;c!SWc7Yshu(g9oqh<9)_SqA;6qoRm!XaNuw'
        'ZuSU01>hweSj_<2Q1in;meqiRbq47E01VY`C#hP2sViI!c1KrHjc5$4z{g(1QxH-&0}Dq1ng=X`$6I<uJD@h9W(N*Y+ok~wUH!t4'
        '5Ar{Qe82LdWhR~Hot8)CS-B)%mgnT_@|D%UfMW8E)xU#e^{?^I&+*T{!=J6r`c?yQC#wSf^pCvo>Y367%hHM8C&1=tzvFzZBfUG*'
        'PoXxft-ffW`He`5dE6G%o?DdC!r5YuxB9@A`MLl(Nk!0$15j2|1RRL&P*We*3;aVHT!X3|q9(Le*K}J#+;2-<?982RbH?$eYX54^'
        'f&_qt;N{(Jv|%t|;1>gTW(^HkAQY<IkO-n`C~s7rA`CTyI?9nC={KxAcGIK{TCY2rI()?i0s#z>{!jtE)P`=N;a)bAwFab$0_hkB'
        'g`p~T24E{xgE28+x@iIq1~~{Cm+=)ko(=HQirV!N%PauKD_!*Igqo>o^L7fXow=|YbIUwTVMaj+vXQ%!g7sxstfRiDdpnsN&q<Nk'
        'J#jT=w*^l@N}&}Hu)BDVMqjqYfnBuCU9dB&UA~`d-J+YvizirXgIx;6O2Tf$D?Ck<S${2&F}tC>253R9@AHfinnP$c?KM*EH4w5K'
        'v?Amw1Sq*2519<DCJVs^PB;f1WsG7*Wer>#b%@VuG~EoP5ie0?5a@};I$K9~!^E0^Lh9&#+>$jWUSoCRUZ*9}I^8m&%VPDh+fGu5'
        'LAr@{R0f(_Woxkfc!MlMmw-M=Ng@)cWxWZaBuzT7#u+YW+r=gp6`fN7_!0H-cyPWZj+<gmo{4A~taCd=Jt@WydIo41V<Us>8T6xT'
        '?6{(1pHLv3c4K-_Fdo-L&RDmV;5DpZYVcXiyWkIUeYFbjIH2|P>UFw076Z=4<kH42@;f~Md{B2)i~tVOJW=FQlbCYf6KojkvFpAk'
        'k@@kMS}0422A^R1hV~?tbi`9vD<?(!o?6CyCipnr|4@t%G1^&=T{4-*iben`X#8wmFZRiUATxEQE|eIN#olTY5H!&T>I*<RP&{!p'
        '+=xuzO&|;^TE*H5wkx<yxM(JXTIq3E9;J$wj&`PWQ*JzAa_TNRbv4quj^LKnl{ghw;Y!5<Rh#RHWWBDsmlul_j-k2+G%%-)h(eVD'
        'nN6}W`U>Gj5!l3oby!-ll*HsE401yZM3VJf*41^su|+kqps@~*RS2o(59|d}w2d2qkVkYC8vu5y$BXI$q}JgzA;UJh;$Ehg6%4W*'
        'uJlriJu2~Rrm&r0N0~7O>{md(VTfQ0?UR7}C<AdGZ9upg1rwvS3*1T8^t>P#)0;A=CJZI@y&&AS6)S@UVHgmLq0|;vGEpFN#~$W&'
        'SQpTLTRM|ywwAIK2F}oR209XfQxGZ|2JH+Zy%I5a)Fi#9u4Dpy>nuSKtcT>^i#&4GMw9pQq=P!AoqL{(PB+)vOy&4#eIZ&zITR*f'
        'DfmMz-0Fsu(yVpBjT$=$k8#4bFvj87I)<U^xcVr99K9Wm^V!VG+Jtd&x4_M~A@V6a!;a#KCfr%dSQtVpg*^xU+{J_rV;6M^_?ajV'
        'w1t}jw&!6qu{{hkS4TGiRmMnB2QkH7@w)O>lO^B_bmN&4|73<_g8R6q#nCl=^GNN?CNRIGptz(OP*jBQ7{;IL9Z^0;lc}Yn(9&>8'
        'o(xpT$&DSCe&InzGQ+7U?+rcxKr14EoI)5bHGpg>fH5H176BEv(2kvP&5po^GZ}W7i4BcwA&tV#TV@1j?0EFPj^30M!~puZkTJ<o'
        'PQlHnpSFbYINDkfu}DEgieWj;d5i0W%R=q+>P0JQTdwmQ))a=|(yerg9LPuztP+ulJ2*VVa4}ZrTSe=2Vpevq5K|XS;ZDU2q*A?Z'
        '!1Hn3KBLD;rz&B4yJq4lBO{#zqUl6y77js8*qx9f@(jjb$GADyqf;m^FEI`e7f%25%HHIbJe{?}s)Y^F&@W$%UM}KG2k?Cjc57C2'
        'PTO3yDH@Ae(n2q(O_}zJPMa1T)EX&F5OpUOu!b)HC~S;jE<9MYTc|C=wy`gK%|s~^o$?|`T(rDJeod&imfS=V7#?6{{cZ%`;YAVB'
        'K{*+{PLo~_is`lj(2Tf;%fG1CRe$XoUWWL)$}GeoE5%>Nw-{Rmqd=(}s3)qOUW&gMpheM3kGM0N!a`m9z6nK9z;0wksCOi={xByh'
        'q_z~}U0}n#P>c)dI`O)89kBliCOg1rU%g_%;eoMRfIKuw5RRh^P(bwpZi!8JBxNf-nWzxr=qWW+`Kx(We!*&ex7~nK90tpzfsM>F'
        '!My^pCJB0-Y1>$xg8rBaQzC&4Kp245RPF^;^8&1zrBmTu1w`@7%K#;deF&(~BOyLTs931I_&Rn*FFWu}`Vz=8eQS3Du&qXa1G{wq'
        'W%L!UH9zD<<o|2sAL?SX{PA`8qFhuT)x8OY-n4~^)hC}!{klX~zX^qI&a6K9WQ*z_LZJ^!)%DGc(vz#(9Y<G@GP`!TGP6$Ukv{&B'
        'p4=}V)ju^oDwpIr`HFl)zu&`Gd;bIP0$2YFirII5tInL`^cR{cKFWvJobCNX&47O2oi?TZEpPd50h1?JuizNI?!^K&aj{_ajy;Q5'
        'eGjr=+U2Qx2x!CWU_xg*n$VowX3Cbz_V|#^c&L6ey0>Yhj3%={ox6n}wk<xyuhMlR!||#;^bdqfKc9Z0zw50e0WpjxfA0IVU(vNc'
        ')yIP*RA2QM#u_=R5|(#0z&{E83Fp2#L}dM!EmL1p7AlsQPeGxlW|FK1PiiHOt+rs+cEPkY&=9{&6Rlo?YS%ultX{^x{`Z)2<^fFk'
        'xbgs|j4HF40+3^0MuVB?uOe8<=}w`2^|#S1`})<?5=fPxCHO-${2$<-KgK_QWS8LD_bU&#2%nOa^;(Vp2BT;o$n`=100'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
