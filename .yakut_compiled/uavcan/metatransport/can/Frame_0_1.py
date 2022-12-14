# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/can/Frame.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.120048 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.Frame
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_
import uavcan.metatransport.can
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Frame_0_1:
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
                 timestamp:     None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 manifestation: None | uavcan.metatransport.can.Manifestation_0_1 = None) -> None:
        """
        uavcan.metatransport.can.Frame.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:     uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param manifestation: uavcan.metatransport.can.Manifestation.0.1 manifestation
        """
        _warnings_.warn('Data type uavcan.metatransport.can.Frame.0.1 is deprecated', DeprecationWarning)

        self._timestamp:     uavcan.time.SynchronizedTimestamp_1_0
        self._manifestation: uavcan.metatransport.can.Manifestation_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if manifestation is None:
            self.manifestation = uavcan.metatransport.can.Manifestation_0_1()
        elif isinstance(manifestation, uavcan.metatransport.can.Manifestation_0_1):
            self.manifestation = manifestation
        else:
            raise ValueError(f'manifestation: expected uavcan.metatransport.can.Manifestation_0_1 '
                             f'got {type(manifestation).__name__}')

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def manifestation(self) -> uavcan.metatransport.can.Manifestation_0_1:
        """
        uavcan.metatransport.can.Manifestation.0.1 manifestation
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._manifestation

    @manifestation.setter
    def manifestation(self, x: uavcan.metatransport.can.Manifestation_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.Manifestation_0_1):
            self._manifestation = x
        else:
            raise ValueError(f'manifestation: expected uavcan.metatransport.can.Manifestation_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.manifestation._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 624, \
            'Bad serialization of uavcan.metatransport.can.Frame.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Frame_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "manifestation"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.metatransport.can.Manifestation_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Frame_0_1(
            timestamp=_f0_,
            manifestation=_f1_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 624, \
            'Bad deserialization of uavcan.metatransport.can.Frame.0.1'
        assert isinstance(self, Frame_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'manifestation=%s' % self.manifestation,
        ])
        return f'uavcan.metatransport.can.Frame.0.1({_o_0_})'

    _EXTENT_BYTES_ = 78

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{`t@OKcohcI|GGVw0s0C0RBtxuj=XmWs02L&=s*d;F0<W6-H-jo@E6pG>>hT~syQzv+)e4iLbDAORh8kOtfVwDgio'
        '1IdDmEW8Q`WRP)?4Uv_BY=|HMW|0N6O74AiUv*V=z5cPAmh3WMRr7sMy{dcazVlw)`fU8~PV7hcfAtHcjZ7tzOQb4hIcwyyzcp5J'
        'W+Ig?=1av&wrV!($3Cc*Yw2pOY<{>=GMisC=YH4x^QKmxNEM7c<e#q@_tHiokvFSGwQLkBrDD07z?65(yg)p4&n#E6#X{4H)F(ft'
        '-(NKKh#vi`=I@$yC1q5r<?KqWYF3(m22D#qIi;HQiFdPRF4F=toyr(hBUMF&R?JScChAWUwrVzSCO+6Gq^)wXko~Qh`4AE+RU=<&'
        'T9ek49@Qg=#5xMSTQgMsv<ye7oXuye*?WNF^hbqC_HMz<yjQ52cg?bQh?LYywwlVBg}YU&sV@S`v{9+1^2H3Ge5(HV9nlb0OS}zv'
        'Nz8(wiT-8t{bv2K6ksf5jB>`^(C4)kI5j1oO_z%mGhHlXn)UHirkHLn|7R=``Oq?1p_X4U%dEJ{T%{_kY8h2#8TU+9GAb1_!z$TA'
        '+GLet-eg7@x+ojv4VH&L3ssgaKzUxWnwZ8$DIFRuma}&uTgxWQ#8qAj2birG6?2YdD=cHKW?@WN$t=$srBW`NHmY#V6AYV4*UDvV'
        '$Ekun)hgyRTqw3;va<P`8eAKwzFIEkTdh}|%f}mIc>rdXud<41@<Qn%v<o+1A(JiKh1BxBESwvMlI6Wm!&v~hdq%EiBFbu!70i1$'
        'Oz_WYu6W<Z=j7kGIS)g^?q@TA(@YzH@s;Um#^%}eU*EXt9a$)DtQ2cicK!O|4Ypw#<;qod-^!*f%qqc^t8OINo9yO`yiHeKz+HoT'
        'r_AmbYq<<`1U)cTD-_JMS*aN1Y;MDb05<~5Rx1u#7&fQ|Xz_~NfL^Osu~xxSynD#b)SwAwKyT2nxt@jbDpcV<X6bUalC31{lX*J_'
        '_d+&3|Mr`=nN}!P*}Lz|F~^WAENztGrl^&0yk24}8(^f^W69Xa6%Brk;X;9-CphpA#ie3-gnt(bS1co!!z+xp+ufWw&x_k#teUNX'
        '%A1g2-=kIMI>1eFxr(<1jzJl73vgi=3}PkG1VcDpkH1|kpqW%1yR%MP=jqqe`l9uWby1I?Jz1A+)0zC}wto9(e|o!V&DAgc!Ymj4'
        'UGw`5t{aZVr-kDELZVqelH!1xbybjpxn6=B4#~_z3Gw&&{b}R`9_vPZ3QjqVsTIh7mwrQjJ-X0DWR;cLidjGH;=$C)hRv^d7MgX|'
        'dcm5n0ik3}=oHM!%rrl*A5X1j*Ud}{FH|a<Y2L1%OjU}ta@vH9oS7;aKo|8%Jmj(~&HB_G;Pmx7nED0KQ}jnbq#uE$0IFko<I_qu'
        'p8;%E@gDqL+DLDd;L6Qs%zUv~KUb=)fE}mG=G|HjyKfOL)IMVKEbtHx9Xt~Pxi)bvv5>&AYgUonPNyuR0vM4EQe>~q&*7T<^KIMy'
        'u?L1d;LQVcP%HyE;F#lW3^s0n{Z{W6%b(731F5+B<d=|l3O7#G@)#U6P|VeAO5lvp>IeR?vUe>oIT++(9{4Up9pml0QiPU(tOO}@'
        'le`CIiskuA$xLTgv##47o)@2*38dzg91PJVaoe<*98S9G|GQZ~`c}63Q~vh{rgKl%$5O>ov(99VR5tP}MYujNs!6zB#F0M(<20(p'
        'a_fn7B$c*+4Vu=k>L>0P8Kla#LY9HKw`;i^JPrK0){VbyYWiZMvI5WblHEd6kJnb<JoDKCKIPztv5r3`@ks}F3pT1pv0kL1$LKhQ'
        '$5=xjr@trg7;WfBD1DOB<8+*&^l3aEY3K@-KZ?hALqCSc@rHh!%Adfa($Hrp|0EtK8u}?}=QJKqHT1{uIMdM2;PH4ve;kiT8~PJ?'
        'oNnl|RR2lp_bl~uj@o&O`cv_EuA!gD<JpFO0gq2MbcV;-hW<1jpJ?dM;PLT>{wyBPH1vyje5|2AhsV<m{Sx82jK`A=T_b#Rcs$Y2'
        'uMp1X@p!DEUnRWrbiN6~{Ubb1HS`6-e+`e54gETu#|tzbFVgw&>pIrZZ_;_aMB}?i=l8OG-St=K_+vW0O2^me_&OcmpyMq%F41wB'
        'jusu)>9|S92Xx$`<2D_4=(tPAJv#2&$7DQ8KW4=bP5f9CKbFLgW%0ujKi0*MP4VM__^~B^Y>OW|;>WJ|u_u1)(~lZBd+>mO#|kn%'
        'rL7>(!vkol+HybV>Jfa7IZh||$WtE`ppwUxgi4pBes<C*WLL30{#4-(ExFb{ht}m8%f0rWl*?f5{#M{Ydz1*n>w1Hmd^XrkzE^}t'
        'Qa%1L9Ngyu&tz7CQLz4C%~^k_tr*sukoflJ);qVYpIA$p^`7-7mTvvjN?Nz!vE;@FG{~Pa$2mrLm|SZ;POJ~`(eV*_F)OtSGqD6d'
        'E}+^g%!FqEcn{z^pwm>apU=SZcg+IQ8*sc`-u6u3hru%7F4f8_1~|xxruC7vY=i%$^=pSE)6TEEE^cJNjn=0~iB?W$Rv!K@^h|&;'
        '9|4a02ylW3Fh&G8?IXY=M1bQ&fH5M#2oc~3BEaKBfX9dcj}ieYM1a#ofKxsKoFoD~LIgNL1UOCvI7S2*BLa*P0Y-=b84(~O0%Syh'
        'j0lhs0Wu;$Mg+)+02vV=BLZYZfQ$%`5dktHKt=?}hyWQ8AR_`~M1YJ4kP!hgB0xq2$cO+L5g;Q1WJG|B2#^s0G9o}m1jvX084(~O'
        '0%Syhj0lhs0Wu;$Mg+)+02vV=BLZYZfJ_h|69mWv0Wv{=Ob{Rw1jqydGC_b$5Fir-$OHj0L4ZsUAQJ@01OYNZfUHroeosFH>rI$8'
        'vw+i$R%%<E<}ye$JeS$cd3mwLT^FR>^$vJ)@4nNK0{^WCLVeSo3nQxc-szE0uSi>a3+A}Jx7eDwC@^!mB<3s=_Uyx^OzS_K;(LNq'
        '&$v0&L{441AB{xTD)3K5La)|;S^r%>+lDWQSWjKM#%HeJXv5W7&6?%ztoUn}KY0dbX*g{u1UjbmDcdiFsQ?N<T{%{<IX22URsoJx'
        '0ysA6<Jd8ulR4qz*fF1z86}R55XUOSu?lgl;&U<;;#h?^Rw0g6h+`EW$123J3URDL9IFt=D#Wo0ajZfds}RR3#IXu-tU?^C5XUOS'
        'u?lglLL93Q$123J3URDL9IFt=D#Wo0ajfEVG8N)jg*a9rj#Y?b72;ThI94H!RfuC1;#h?^Rw0g6h+`GvScN!NA&ymuV-@09g*a9r'
        'j#Y?b72;ThI94H!RfuC1;#h?^Rw0g6h+`GvScN!N5ge-sj#UK5DuQDb!Lf?qSVeHGA~;qN9IFV9RRqT>f@2lIv5MeWMR2SlI93rH'
        '3qMvo=5Yqh!>ok<N9ccq{s-Dd=#7Wg5L$!R8z0A|7vWC^IkXA6La<)t!ssAQt=gAUJJ#;hejNj+_8((ioZ9n&7y}*K>n{)P*slFG'
        'c-Q=owZDO1y|}Kb+jUiekklSr*C-LvxX*Qs5+P0aT-PZgq)8&A2_mF1BBUr0(s3fBV?;<teXi>?5z-V9Qk)2Bk_hPt5z+(^(l`;)'
        'm`@*#5+Oy1kW?Zhl?X{CLQ;v4R3apm2uUSEQi+gMA|#avNhLy3iI7wxB$WtBB|=h(kW?Zhl?X{CLQ;v4R3apm2uUSEQi+gMA|#av'
        'NhLy3iI7wxB$WtBB|=h(kW?Zhl?X{CLQ;v4R3apm2uUSEQi+gMA|#avNhLy3iI7wxB$WtB6@;V;LQ(}Gse+JHK}f0~BvlZSDhNpx'
        'gro{WQUxKYf{;`}NU9(tRS=RY2uT%$r21XgvCwr5AJ*Z+I&@t_YY44D;=0C7a_*Wg$531Qd-M!HMa}bn$KaoTfIn-Ue8k7Q`i4)T'
        'PHnFV8LhHx6&Jt~&H9N{)wrADf6>mfmY*B9{oG9ed;n+C{bY=z<LH)DkMU(fzmzKKuKfj$#P4Ac!pCVyAR&Qp0<ld&15?mCm_pQN'
        '3K24eaWaJopDB!!DMWm;u5mJjD4D`hGKFd1u9PEW3gcu7F*1b+nZju@g;Qh-C&?6M$P`YHDI6zLI7X&$)VE+TO{OqKrVuAnm?Tp;'
        'LZ&c5rZ7&XFh-^jBU6ZyDMZK=G%^K^OhF@4(8v@tG6juHK_gSp$P_d(1&vHWBU8}G6f`mgjZ8r!Q_#p1G%^K^OhF@4(8v@tG6juH'
        'K_gSp$P_d(1&vHWBU8}G6f`mgjZ8r!Q_#p1G%^K^OhF@4(1a;y!W1-N3YstlO_+ivOhFT-pb1mZgehpk6f|K9nlJ@Tn1UuuK@+B+'
        '2~*I7DQIrbGPH)!8h-HBK%V7smz#$hYW?zP{hZ{@gmT%~Xx5+j*nm_>vG;GjiK*T<0*<B3oQd1$10BZe++oDUaHC|Tv(=5Jeye^;'
        'Z1fz+(d^f$eBynhaMyg_ESc4;Yzyh9_6E;eK4lZz;*1ip^2tc71EoatXq&&u)ATV%;*7vwf?}LJeFDwWLpPp0eG<)h+NlpIaj}Z;'
        'FQ-pAK5GR267&>UPFIjVj(ggLR6$|VI{Gn3VvRTi*RiyI0*UNYTThTPLxkA1zJAi#*cyRSamW!HTzjgkpT-TTj|XCa+{cJ`du~fV'
        'gBxCF#YhXH?yJ831a6`|E5!sQW{L3oZdZR2H|##;886746{7VZ?dj+Ar|3Z=#S5jLqKDAHedwxwUd(K8Y@Myf2WnBj;LMLAI_rcV'
        'dw+H){pnBZ&(Nb5`*d9g9Hr-m)`$MAevuyGk<MoZ<)6W_mxtQ7{+xbExD1d=*KBU+edw1RSEQ%&gc`zS89EMqPQOBKkbP}0LYtcV'
        '`p%E6U;TOgD!E)ej|0@YO77XnFzNGpf?PlQKG5tt;o8W1)qkWfkdxWhh(OH+a!N;zPrs&LC&$-&$6STB7sOq2<Iu3^FX%6l<K6d|'
        'LG2gGSwA$a`VIZ2czMIQyB6^Ndil_C=r1`hjtn$*(1Lj3<j`^JFYB++1S<GGd=dIs#C!3z?+l;*WBpZ{)D1ko(8{YcA^gtHL4Qqu'
        'ohGB6d)9e<2vcu))0e&JOFZX}ooBW3KJn-3%QUU^=37*vB+6{M%X}7GN?)fbafFxHgj{fUp^gTn7NO=6lwF4U7Svd$X|uQN11SBa'
        'to*jT{1(*sDyYs*_d459>uZ0#-QMf%K+SL5b@%$Oy9>3y74`QAufGQ^{1Mt9i2)i(MxuSUv+r(c*4Gj=jg2K|qJy=kb!-p1!zPm~'
        '+Fz@SeY6S?u;JuFw70gG25uW*Ve`pb(at?A52*)$ik&3yM1%XWM$!+!x4TMy5_R{seki@cNnwY{QWX2#boH71Y((9{nYH))Ah2fu'
        'M4cxaqwRmI=l%gIK}dc%Y!urELIEd1K$2e_9LvtovB2pOoaEPoAlf|?L~!B+D)~)sxc0s?TrebVXvuE_(Ct5b=wQSMVDgWMktB2n'
        'V=@wZNMOR~d6ClMZ`{f!<ByU!9Y;}e#Nu?^*_QD`7N=2)i-h9zNW^JAwnG=ES+@!A2*hdTy$;`7ahkOj6n-$`G@kQCesx1}T8Pv3'
        'eGrP%!Q!;{jtRx-e#L2VcP-fWS13*oC{Ei?rBIwc3~?IA+V*JN;xtOckpOYJmEJB++p=;*Do%UzgT-kfO-H(j({_nXy@8h2MV$7Q'
        '?JiCSm+vf2cdjEBr+cdxEKc`Vw_ThbtiD&AMp3ZecGf*D?UOj|Y6-PIXslOpx~)A;+8*k5)MPhtx~<j4K3eS}PPetaG;rGzak{OC'
        '<stRp6Q|qyu}0DlYG1r7w>Z5|;`GRSa|v1dBu?`_QO1I9vC~Z<4-Ki?c7bo7#A#p8s7!6Pw5gHyztuzk4}1^?5~n+&*gg=7zQyT|'
        'Saybvr3Z1kBck0yK@=!Xcf_^#o#8@V)q(bHFuMJR51m(>-Y0RoB}{+T0-21*JPd%!^eAvTDD{00&USTLgyq0s#NPKBuT4ZEYiWF&'
        'Z{`U6bA6)AdyOaTD0o3HG@iv58sB}#j(BXp*hq1_haU7|ZG1cuaROb0FPVfdnf%~iGFf|TLcEQ;VC9nw;VM-4ibT*W5;M+A&fzN5'
        'a95#lwjFUuI9!DaSD_x(RVdVQHShKP!LLGT;!X%xp(L+J*mq303N`2|RQQTSxC-^Cy&{1tr;B*k@`=?ghbj4rs<R4p%PEiROn1Zz'
        'm1XCB!gDb%&ex7+JgZP5ztbv|Sc76vLW44KDl-$X3bhHjy{<xuvJas2m-6!4vhrKJM(0&1d7aLyP~GdvSD{*CV6WE5>-M$^)xEy&'
        '6$!pMJ!pLUU4?R5LQy|%?>8T?Jx$sk>WI8al<3(2t57|(ih?^e+}|ox-)*CSj#}caX!jnLhtxw)t5DK@T-s<`Kim4Ew4aWvP_BEh'
        '^{&D&dka{FayC=<Hkf!LeAR6*ds~I_^^7uf+}R&J+WxnC>K`?58^V{-QJ~m95DKoulMa7yEIUKRf-3?D=j-U;h;|PJ(SWN^J>e2o'
        '%aIKMSI?_ZZgkEPk8E{k<miG|q1-P>&=BGpl)yL>6E8?4XJhsXRFcI2t_E0Rh;z$@bRp&fYcE4}2iyBnloJ~4kyEL|Kt7>L9jeq1'
        'PavOArT%^g@(JIS2vzFARqBP-T@$L*J*w2szVlF}4g>i-!YZ|`HwUZKm>#53W8NnnRBAiFvr283`7Bha4@IT!zy85hYDplUfmLcr'
        'AfHZ3X%8y3B#=+{R(nvXC4qeUZM%a?EeYgv@E&>#<TDDDnpETc_CP+PP^sO$1qJfypi&16X3zSp=(a;3pROwP$olU^rEcvgKY&Wz'
        '5ykd_Q1q=*cf_(YR4hHJ)EyD+9tt8^ARjrdy}ob_TL<>2!27a5KAlzSLq;bF<kL;1b~I}J!Dv)!nWXMjsrOqiOibdt45?L&)n7mN'
        'R<_E@M%84M``K#RVyijhE;G{A>^-w7`ON7>>1R&yHHx=$Mx~NXclx;Lni-8mdiZw0+RX`iZ9-dn8GZ)F{$G0)a`gDxYwZPw736;{'
        '*}`#$_tqhfzkchXRR6J5XXSs4W=~T+EB-V)3Q+mQ?5S5(KSt=Lp~g%{1%Hg!SNQzyv`4A8TWweAZIrY!5D-$|MrzOQ+)BHR)SgMY'
        '6?Vibke<Qx4(ho;3s`}u&UsYvI7f8~=cgVe9PuJrm|IH1)H9Bl@ah*_YV{F*CLFIzon{;{;dQ<cD-RjZ0JjJArIs4*L48@IN4=;e'
        'q1tWST5F`QxN&Q(k$&EdTWgK<RX1*}HQMuT+?qh{D4#ZNO(1vFO&hl+kaq|z?ncg)r0ea-dHM_O$a(sU?Z|ohjdtWb{boCIp8irh'
        'a-QBHY_-7d#8`O6i`_~8u@}3O{;C(dlm40)yOaL97rT@Gh8Me&exUHhGakhwAbnkuz9~t6AW7enq;E^ocO>b%lJq@E`hIY_6SlW4'
        'V^)@-$ubsY8B4N^Wm$$L%UG9XY|1ho$TGHM8QZdq9a+Y%EMrfWu`kJR!aBBPw4x~LOAncAARL2EudWHlV6q3-z~>lXx-VGbc%QC;'
        '+c7xN!8H($!IaN6aJTAq4Q!<Cu7NwCq1!QVFT%SW1NY*)+c7xR#WnD_F)r7@>&UcR1Fs{~at*ve0vTcUy9SIf`&|P@nEkGSY!RC2'
        '&jz{%D6I#%1}KLIxd#5lU!P-uxUY!waXAKv+x~K>*D-KDTF)elt3Jm7aVNz2yBq_=ZGU;x>lh$zNnkgxWAKFI8h9Op#~s(e>lmDI'
        'Tm!FT@R;KocpZb&j%(m`3{E+&K@0hUaB8GM!+cJS;~My!8pk#8IW>-J;B#sm*TCo0IIe-usc~Eb#IEtX#aZGQFnCleIFvVVlrMc<'
        'lD;WPe;`TUlB91-(sv~3yOQ)hN&0?py7-!Gd&aCRLz87J$}*N@8OyQ^OO~-N%h;4<JdkB<$uhQO89TC!U0KGSEMs4iA-<;Dp3xzM'
        'g+3XHti6Z-JROIBemdDDgvDbn?IkFV#W~6g16hQDEW$t*habq|<4IQ_3%&GE?+}jTJsS|i!lNQ~oCvgfl<fo-y}9-Zcbo`BA$8L3'
        '7aW$89VP<yWMzuiJ{ho^mmGJpZX1V<f_DG5?bfx=#ohzL_kDPF<Jw61UK3{`fLNyiCr$&N=(xi+3N24@q^F_fC!LAFIPdW|?O|!{'
        'mPNdX*4~H0ckc%5fJMCa1PdoF=bec_jGrsEi><bHu%i1u$)_%e_-xmSKolkdNBHywQJ=$hF4^r|q#h7AN6k6xY2E`~J;cpX2Tla='
        '%3b#2z9L5Bk{9>$V#@WL7xz^$(ia0_0X)kmUeC9X6IVXNN9IZkIdNwckjM177INvXMS&dm_?!Uj7l>sA@&x4JMBqHJu0TEy*l{AD'
        'IvSxsew9xI#7@64KH`WRrvWb@@|$)$&+rky!lwb(5&28@h{pi^6kuNf<kt|n^u6uNfZfLZ5+Gkh?402*L5~7A?vpxCjQ<>97r1Xg'
        'x=K#~L@sc@=-L^EqpkpU8~Gw)e_dd2Azwu7Z-`N!<I?~{zKGZde18{rMJ@1sQQloqpEx_ByzlJdE+~6{llMJcU-|<{`j#YpTavyb'
        'N#B*E?@7}4gVX7G7?3e5%g|&Qi?WO*S;n#~!;)pJ%Q7})84qL`Te6I8S;memV^@~3C(GEEWRO1)kl}fO=#lXbyeo*Ickq4n4v?pZ'
        ';~n4=BFH<y9=?0;V2p4-@AD2?&se{A5CiOpd+rhQ4g~T!z9adh$2;)vmw(i~1Npw`B}xswgU~y8sJ#P{36JuPTWPVuYOa1EaQ9ZB'
        'SnaZd>nZ6DuJ=EDzisDMuN$`vR4&(kH5G}h{Q~}}bdoENLPtR|<!eHwESvcvoEJxz&q7kM0BOIenUyNj@C-BNYPMiz*lMxN>=?as'
        'U4={`OvXcDG8865VNz>R%Q@TLQf_-ok-hcEG_-K>bEJrWUwZ?WE`Et2xbGk#yorDQ6aIRCimzmBN~z)Tq*2JOLcg3|f=J>ew0By<'
        'C>Kj+xtcXAtZErm1{}s#OqQo6fFFQ2s+P%CYL!HD?f=I5*(BQI3P^{Iqo>FHh5u)57DJNH;i67vN@&9D(F+?fj^)Cz5n<SfM>uRm'
        'gii^EA2y=Pi>P7Ph%jtKUtuFWSC$8n(8910Vc3WcVIu<W7?fVZun}R{h(iq<A-NAx01U%M4E+<E?eeF+OH#f#YKxx~e!(Syq5x`#'
        'i&&-*5)00bNpD?|kBU{v**%G6KJ&D)?l0$rjkv{w6)f>^1$TnWZUvWp;FSK-TYkHj@>^8nE4$84tIpSfwYG!n?Y7t3p_<=xtJ^hf'
        '#5NCb@!f=t80-_9@~{zuePXkR&;`Q`ZY&E?FpS{Fox&dsC%AF%J%quHdkP!j>-JEC8;`92tpmOKf0)6Idw<1$^udh}9&TXR!Hq`~'
        '0O8=ljYk)lVci{**9#8Nx<0W<U(9WNq?b7$76c#KT`utp!!HYunZdb&H)}Tvee&;hZsJ)s?6?yYsDq!6eJXGscouL1JBa-oguRQ1'
        'zeT8f7(3#R{!eU1VmNm37-F>JM9ju)oGfO?hY)CaT!@|k>+1+P05HP+lE<6q1@L|gGK{J74x?t}lZ)Xu_`EW8>*dBDvP_L5Jrl~*'
        'Bax}&eD~H&_zk{Lrhdr3!52n1ZkMV3u|z_d`nvPdv-^$-zri=?H~8Eyb%!!__zk{CFS>E-Wqv1pxs|@e1?)QkFZ6#xQng08%f1);'
        'Tlp51@J2Ug&R6*SrFcu8=*F$@$90cxEXwv8-MGE{mi|?6ot^G=wqaIxOB&s{dp&t{V|QI4=LXm9{0+XK`rp%U@XhkLkNu0^i+!|;'
        'YQaLZ_qLY?ZW}e5p~%!d^nf}Cbuze2-K`(EYuo$jO{S*aTq4tOdh1`NmUPSYap_<VQKlYE|9#2SB5v-`QEVRo#a6Th1ZB5_V%Zro'
        '7Fz{$0?iJ9Xm`YjcA{QTBax|ximT^u@bRF*QG6`g7R~iq<Pss;x{Zs=x4MQ3HV5dSvxVVpaa(aomqSBUcgNO=xwy;4;$1?AOhZC1'
        'myWsG%k^U}`L0J>(TzDuN2}&2ZNb`xIUD2O;Y7H$aP0sU@r`W(TVHTA|HW9ph#kBXk6A$GA&v!V?}zw8sXCOZL#aBHsza$dl&Ymt'
        'wHELac(|iFl&V9idQ>~AL#aBHsvlLUy6uB6vMG`0gD)eR5=ka;o*5CJ$B8$5kLBI3)p~-BTK{65T>Ex960yGN_-5|$ck!Lupf_@V'
        'j&I~%Pb@I!Wqf)+w``WmX2mSf%e?GED_ddN3V$WHS}e`y%zI|ej!9bGD48r<VA*Pg6`*dVWTefZ$0oH>&J=Oc%ESLKL$rQ>ySB3S'
        'ug=@JpTOL)6mxQ%3chq4*u?(>I1pmV8u$PJ'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
