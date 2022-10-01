# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/file/407.Modify.1.1.dsdl
#
# Generated at:  2022-10-01 11:53:16.585564 UTC
# Is deprecated: no
# Fixed port ID: 407
# Full name:     uavcan.file.Modify
# Version:       1.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.file


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Modify_1_1:
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
                     preserve_source:       None | bool = None,
                     overwrite_destination: None | bool = None,
                     source:                None | uavcan.file.Path_2_0 = None,
                     destination:           None | uavcan.file.Path_2_0 = None) -> None:
            """
            uavcan.file.Modify.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param preserve_source:       saturated bool preserve_source
            :param overwrite_destination: saturated bool overwrite_destination
            :param source:                uavcan.file.Path.2.0 source
            :param destination:           uavcan.file.Path.2.0 destination
            """
            self._preserve_source:       bool
            self._overwrite_destination: bool
            self._source:                uavcan.file.Path_2_0
            self._destination:           uavcan.file.Path_2_0

            self.preserve_source = preserve_source if preserve_source is not None else False

            self.overwrite_destination = overwrite_destination if overwrite_destination is not None else False

            if source is None:
                self.source = uavcan.file.Path_2_0()
            elif isinstance(source, uavcan.file.Path_2_0):
                self.source = source
            else:
                raise ValueError(f'source: expected uavcan.file.Path_2_0 '
                                 f'got {type(source).__name__}')

            if destination is None:
                self.destination = uavcan.file.Path_2_0()
            elif isinstance(destination, uavcan.file.Path_2_0):
                self.destination = destination
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_2_0 '
                                 f'got {type(destination).__name__}')

        @property
        def preserve_source(self) -> bool:
            """
            saturated bool preserve_source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._preserve_source

        @preserve_source.setter
        def preserve_source(self, x: bool) -> None:
            self._preserve_source = bool(x)  # Cast to bool implements saturation

        @property
        def overwrite_destination(self) -> bool:
            """
            saturated bool overwrite_destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._overwrite_destination

        @overwrite_destination.setter
        def overwrite_destination(self, x: bool) -> None:
            self._overwrite_destination = bool(x)  # Cast to bool implements saturation

        @property
        def source(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._source

        @source.setter
        def source(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._source = x
            else:
                raise ValueError(f'source: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        @property
        def destination(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._destination

        @destination.setter
        def destination(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._destination = x
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_unaligned_bit(self.preserve_source)
            _ser_.add_unaligned_bit(self.overwrite_destination)
            _ser_.skip_bits(30)
            _ser_.pad_to_alignment(8)
            self.source._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.destination._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 4128, \
                'Bad serialization of uavcan.file.Modify.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Modify_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "preserve_source"
            _f0_ = _des_.fetch_unaligned_bit()
            # Temporary _f1_ holds the value of "overwrite_destination"
            _f1_ = _des_.fetch_unaligned_bit()
            # Temporary _f2_ holds the value of ""
            _des_.skip_bits(30)
            # Temporary _f3_ holds the value of "source"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f4_ holds the value of "destination"
            _des_.pad_to_alignment(8)
            _f4_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_1.Request(
                preserve_source=_f0_,
                overwrite_destination=_f1_,
                source=_f3_,
                destination=_f4_)
            _des_.pad_to_alignment(8)
            assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 4128, \
                'Bad deserialization of uavcan.file.Modify.Request.1.1'
            assert isinstance(self, Modify_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'preserve_source=%s' % self.preserve_source,
                'overwrite_destination=%s' % self.overwrite_destination,
                'source=%s' % self.source,
                'destination=%s' % self.destination,
            ])
            return f'uavcan.file.Modify.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 600

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8EGjr-0{_ie-ESR76~A^<+qq7fG$v_jMLHOWt|ez}s#Ym|!cA+4ZtNPziGui8=I+kDGxC0QclO#FsiKwmXrz^hl;s5h5??J3'
            'JRl(<Duk3jg+G8No)9naJ2QK)_g>pYJRs4k^4^(q&YX|m`OTTWcjm``Uuv0u%9oPD&-}n~Gm$DDs0X|k2*>r}Fo`pzMOB`EQv@o+'
            'r@vPuqIz7dykEUrb;>zcMUhA=*(%T9(P{4KJQb57PrDHhVd90H4?P|^eFfWFv9J1tvn$@oMW(BA!5xY;Q*lI==I_<tkE`xXcjgDx'
            '`&GH<a;;O<%eBa=Z^7&-K98lU^65<_0{_U7w(E1vT}|Gdrk<n}r5ZwF@r^hR1dk@8S#*0!yMc%XTEaUR^?0V;F!n_yKV4qg85tlo'
            '=O*^HXbX|FzF+ND<)_?C^T_9^-!$|v@5y#~AxQ<?845Rx^VEY6XIww_s`5*3#w?08OGOwD1=CV6E8(!aneds8nHMJoQ&FY`_gUO$'
            '5LD5?sbKiBbzMF$U#!2bc4y>E@^kX@_T0-bnjWO6uIr;3D&pEy;##?Wt8Y$gEHiPaGM%lCoKc$fL_bc2L|Ep$rSjYk_kA2cSpfNb'
            '`NGLrAI8cD2JYccGu!a<YDNyW;ETL55z2i1)h;hKakaydO?gf})1B?M2srXtfaOT9eDM_6q$w||^0|8)t5~^h>aszrll4FEia>-S'
            '(iTT3`O@7eQ-etOw<0YDBAt*&2n#mVALPCAEWna*PwArS{;RxHSKsYZnreHuCiFhrogvg%?K5sK$g1+%D1syWAQ(OUyDHDUp|p+T'
            '4t~}il~1{GQkCp9BUusl;y?j(OIs)~@<T;`I}s_@aoTKrPbw5we!aYWGmbp2MRcMl1x=Evh^TKNe_=Zh0-hGfB<I{A4{}lcsOoeV'
            '9-;EzsFU$+Xg#;fqk-5JiO}jam-gL|A0o9-=vxG-ku8(IP(|oN`heKhKjzDMYTP{F5be&8XzNjimKKKzj|>BC=RE;Oa#Ulu)mo4T'
            '4MF(;yJQ(4Jd+sUS(Gl73rGp|xo&`es<ajoP(6F+t(}eCjlH*bjlNXnXGX<=A7BJ>WP+I%c1@;vFm4o8p6#dHqg5beVYB|memVQf'
            'jfya29R2Qpa;Cktao@fD*7jHSzFK=De^?(O%krt0Uww6KOq5FvPIh~R<#{stuKcq6o_r4pd6a`OeSt6tA%69+d<Jko6uz6psdmx!'
            '+vT%0-MQ4ku1RD$Pk#c{1AKOH1s$5cevBf|tby1;dMV;OAM*W7g+8K{@ese0!YdNVgX=z^TcOwU9-!=|Vt^Xs_@fH|+H;mSK(cf$'
            'wCN1zWoO-?<X4*5ddZbMgG(tjJW;a(D?gOi?*DV9)!GIr68RF*w>KDBVOfE-kdgOHL>{Q$2P?C?dz-I0Y!6HtM?t{=bLF#4z%W6W'
            'sm!n}So8oF1Iq%QNw&PUOlC9iC>b_u9W1VZdHaZ;Sf8}g7&n8jkYSiASclev*t2Afo8UkyPtp;-=qu0^>lO9}p_?XMaoW2A$pNse'
            'U3e`r))CIYVatw#;}E^MeMb7=dGi|$2t-l}Iy}%a&Ib~PaZtz$=1FQ-irqw((_DbF&=*7Gl5om8WJE-W+7tfD>utuavkjZNBvufL'
            '1{5Q=nMIm73skgEYc|(7GO(@)xOAYP$d9t>oNn+aTd-<YMuv}eYU?LjuH>$~Yun=f1W8?}FTP{sgxzmq$Vu#W)m_LZNu|jpbM@_i'
            '?9O`~n~Re-G)V~g6WafRydqa+NB&8^CjTry&gD-Z%Aak^pUYo#<S*r~<gev#<cIPj`P*{omGv8=3G9pbcZ_%WyAOcvzs<E;TRc*U'
            'X&MAhH$6U@07nhe!eJXp5-5?4N`k3ilt4v42q~1=i~;cb=#qMzs0|t;gv>@opcDiwvaLk|Wd1;5tp`{7eMkv^6$i#nyS+Dt@u*zL'
            'JMa`5Be5xhff{NNDi4dWpGR<Xw1lge93Tv3c|x3I8l+8L=8-Sbpdi#VLdUTiM%9d5v<VU+=Y(+%eS`)VVG_iJ?X^1C2wafWqY~CQ'
            ';lO~pui-vTUsy2bn!}J$+*Y9c2X@}WAfBn73dmtJH7HNOfyg&^Vdk_qVM-iwoGVtRPXWAnI;aiz(>QGO|El@+uoG#VIFK57(`KTC'
            'x)yED5Hu2l3)>EvI2|)zU!|Eg%8@z8n!&!Ux{oPIo8d4|KtuGBzye)l>^6{apfa%v(_n7}-&m$mDKRL<xg6yWag1`a3MK<Rv2lt}'
            'H{*p7!1#fZGTuJ&c0_{KBjYJetY%zRnv`*cHb+~-&>3KsBx#I0g&-{B13_tO6R8Cz&^k3Wz53v}z%a}BVABdrS*&|#5Tv%xvFKZh'
            '$xuu|y4VlfI4dEXtzxFf3W7*gwm$+ilA-xNTnB%Fs5~#uBMl60A(FM5$TwK-P9i+?a^qcKNv{rjVtS_yV#c}?YjHmowh7E|Z!s}$'
            'AKQKu04ZXYw1Av^tFV5+2jhnb6j3XR#^$_n;_;`1@$<wd$hbAdC;L>J)`W6xV^@(E<i3e2x^B*)Don5wREjaRShV9RBcfu<;XXv!'
            '^<;U4XeQ1*IhE(>oSGmokBDPc04#LT@X{{Y$U6j;wK4gv5m~OR8gz!l&#J!0wF<@9)jaXZ)oGK{HAL#o(Y9Hp;{4xdjj>H2A~Vwi'
            'o=4y#9Ew?k;P45UJuxGb$vu|(afUa6hjHVbkd%|XI^{P1!}#lH?K@V?qle7@pJemRGehsEKXzx#oG~MZ_-{039FwyzoLLCX9tn+f'
            'r<R+#SI4>xLaeE4=bNeJ-&^4hrXIF%TzY!F7GJ03i^s*M*6r{l7xDPNXdnGoFbu6@82b3X9gyT-#>0?&f;XZ#q&BFwo?I%gfS&CC'
            '2uodw+W>#2-|Y<Vsju1h)QPxiR<W5)Hu>U>>aTaU?$4h1o|XAFGVtV*d6O<Q-=rpQwE5Q)Hc8d_H^AOM8~qai00'
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
                     error: None | uavcan.file.Error_1_0 = None) -> None:
            """
            uavcan.file.Modify.Response.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error: uavcan.file.Error.1.0 error
            """
            self._error: uavcan.file.Error_1_0

            if error is None:
                self.error = uavcan.file.Error_1_0()
            elif isinstance(error, uavcan.file.Error_1_0):
                self.error = error
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 '
                                 f'got {type(error).__name__}')

        @property
        def error(self) -> uavcan.file.Error_1_0:
            """
            uavcan.file.Error.1.0 error
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._error

        @error.setter
        def error(self, x: uavcan.file.Error_1_0) -> None:
            if isinstance(x, uavcan.file.Error_1_0):
                self._error = x
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
                'Bad serialization of uavcan.file.Modify.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Modify_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f5_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f5_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_1.Response(
                error=_f5_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.file.Modify.Response.1.1'
            assert isinstance(self, Modify_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
            ])
            return f'uavcan.file.Modify.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8EGjr-0{@j(TWcFf6t>bhmL1!5aN`C_$(BOu&}4mU;?kGk%5o60cU9R+C?yQDyJMZftKDUHR<#0!<RK-Y0|{jE(5K#@_db+D'
            'p`oSpp$|<8E&WA3qm^Yjk!d9(Yj!T*`Q}`{vp0@D7#|yIf8^<?<t3hPl7z*a`usX|d}b0iY(!zg1ygcjmHE7ZLvO1UF?C;^y{X<)'
            'v+@|>LBL`KLvmtM#HlONm>t|QOaj_Kh!;}YbZKC2bHv^VJ-*#Ct1OAaAi>o<X|g!sVW6Q#u5`xtRXJDAy{~R6d7MxoV(z4ZCF+_w'
            'jB|IBlEZ79`QAQ}G2&4{iO}p|B%6dWd7_tBF^)sL%{WY=;UR4pPF%xnCp+6u9cDL*wR?CI?M~N%gx3S+l>)))EI#Ot<HX^D_$;Uk'
            'P~|CP<<dluM(81{m*h-k4@e&~3%ItSm(UYKw^UWh=SU)G;L+IY1-hL&c$MKM^;2YUlz5@5<dDMIX_+sei}8%;l7Lh2a%Xg=JO!`7'
            't8gwuIAWI-m@tQd?O?sQcVD&}#VpZbIdI#2l?t4r{vJ9k%hBzax_UOj^|j6z*JW;A=}ROI8e8};E)zAYY}r>WQmj_(YMT};!y6qV'
            'a7hkdyl`RZ!T^Y)mc2#R?3%UO2Q9Za08+kWA4)4X2&IXYLZP_1Nmh$iso0O!k%grJ;KoY`RjL*XTXywrM3a|FCNs|&SQe}iVfh*{'
            'qu$)RF_y9s1_m`ED!>pxg%O235Q!l|ob`CjToJ}C^#q&6g+VS?vaYPGmsSb>uN5_&<)T?fI=a>jEei%uj35*SCL8yR?J!0v%n&rL'
            'Gm-5|S_x8ripC(pnp`Wb7s-}wll7JA<zhc4FD?(_WV^OS>@~7kSt;~Kdwmcm>7?AORVsFMtA7S8?ZYuS-J^rVX=UQ7Vb8;9xCo1I'
            '84B<gY`{Bk6&O$mVF#{56K=sxxC<Y^hwvap74jICvr920)EzlVw)rmeNEF6`a8FtC1WCd)b{Ww@AUa8u9ML~Mca$8hU|-m+=-K<I'
            'X}LL6+ZqZY*84<*?j*e7Vbw#}#OJ8xwj!YZd5<+hYy(m1_}nEitEav;zpu)8`dB8$C}G;Jl9O#gHW$o!Q>%~?S^}pD&;&WfED&0T'
            'o7`pU4rbS!#S)$48q6HS=92ot2)8kxds4{=BNn$c%hXEg_-OXbp2+P>DguiqpOqYclZ*BC^Cs)+seFcnk&?z?AW5s?gm`CUzJWf#'
            'mZ7cNZ5r5ZdYY*V96J^~l+RYE=kcKa)F${<uUe_^)428IDlFesv*oFKiG%$#$`DjJpE`KY1`l+*!2#XXgAv_wFamh2oY%*O?j_ia'
            'P~~aR?!8v(v=bQH3d_18W@hS8_y`UC4KoRRatA)O;4}Dq7QTQl;VbwWzJYJyJ30N@{PJFlU%<a^=-~U??fm`$e#{8}1V4B0^;>uJ'
            '3;dy3!y~Me$N2pdcmCDo1IMvHPwBo4Gyj7P{L^C@ug!J^=8f98k&`o61=(v&OaOHef3mlO{ZcisRL_=ky8g0)?MwZkJc&(KS5we8'
            'wsJHJEoQ9JuM@xbgv-Ei9e{eiN`pG9vWN+OSfcD?VVuVUy;%8sZ5KVV;4$7$`>h+>wgXwxS^T)qqCRT=3$W%s6Bh~q00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Modify.1.1()'


    _FIXED_PORT_ID_ = 407
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8EGjr-0{_if>u(%a75BPH>}>OJ6OvYq8m>ZB+0<F*(U5{#Rj#ux*2cSLZKnlPhS{0Bd#^n^Gt9&Grl7W{MYS|ii!v4B6QxK%'
        'd3@jl5)z`SkoW@-h|l~1`~iqB@H_X;?#@1(V5Ca4>h<iMbI(1`-#KUc#*z0wyfC5uNj~d$?9g^fM#uwcI`XdBaCphEyteO!GU93S'
        '@H!86q{TNnK2PtZb8n{KNoSLjM!>%n^Dr_Z+7}ba$y?l!Z5*)&DUTV_b$Osj)}tV{qBt00cGPgqHm-U+Hg_!3Ej1-%SoLh#?3C*I'
        'nlza<c6bm<&m~S%ce3YuX{Aspd@p?yf*NKN1+o!GJWO8&+XHm#QKiYzWyu}8FG$g_&B)X$9dz6eNK3gxrg_ox9B#UU+B|GDWMnwp'
        'ZAAjofvIJ}PHoSIoh~Nl*SZYoSZN9GR_PTqnRq*`r^#oGFfv`+4D39k{kS1cC#U^@L!2FMgkBt2kl~17dsdo!@s`J2FJb|2dpn#('
        'f-_A~Vw)kiS>!Rx^E*tsVZ=?Fc})gF>9$HK7(cE>7f%S5J$<fH5KoF(F{kf62d2Sp0Ph+$ydhmPQl5A^xw6t!x8=4O-;-e!&Ub~8'
        '5o_?K7jOZ!)P0X7C)P~c#`S{^5KknJkGJ}cCvC*Q9sJ2#8**L@Nx%unBAy#i<wW*$I+@AG)tU)wiburR%4B7N0!N%ju=LL*7Y+!U'
        'ATT>=^5`8CyV$v{{IW>9!>Pd?-sWyMH7+J+H{DRSTyC$p5pVHefF3GLYg4}yH<IHB7T>gF)JZG<PR?ZBH=1Ooj9+!&+*6eTMU6gv'
        '#ArBSnmpCjpdUX_CK~>oCMRB$k=A1!KQoDvhYZh86Lt`ju+wgMjzrL%U4?^TA98xl=Ybh{K|b*<A>mx{jpW>t=UQgO-La&kG*JfJ'
        'rMw0G>1ymaX3!a-JZ9{ePR!GH)7i@Od+_`>Gh<jd^=RF6TfEMF9?645+BVwe9!!e^+d6{WE-z)jwset)^Z>Hee@-P+l(?~Dg0xZ~'
        '(uwy%q%`02O;;gMHEwVSau?osZFOQ=d^<-dUdLPFj37MXtH9Gy`dBgzlTe;Vx!@mitqutsJ-%LETdXf`)avTIaFZvx&Vd|21QKKb'
        'nWpQ?(x%f(6gN5E3`~o55h2sd*)!fJlh52tDTb7wZ#_tu;_Bin#_e+TrHwCV(ugFxLVQ1Y=-Q1NJ!U*Po5N(I(a|_hOusA2Vqd&1'
        'ekk6LftWUj8WbURx}TgvxbJb>@Vy{1koMK&kqqt(%3wnoGMS=3j%*-&)=;YUR9@eMlM4#~c7R?0Jx{jH?NGLDXe+!O{PsIm#}}q^'
        '*+%H5$o05^P)0Fp!N<71UjT6Wn8po&EZvLKbVuo0=}L)=pGJh%XANP75GkO94|S<b_r=q%{HriAQ3WUx_!7_;7a4J3VF!C{M$$9x'
        'T7Z5VsLVDumY*%L4IruKIvs{Emo^JI7*hx{87h<oiteH?u+T9>!7eRaBDNuLlo+eMS!~V$d7IFmP@hf(9x8(^VPUZ9uvyx3JWGQ$'
        'D#5OhmY^$a-jskT*68R8LX{?%D;4V;#zA0dzL1)SY?hZ=C3dM)!gbJIRiEy8;Jo^c1VluV31&?v5?<UAV2q2}W`|jV(v@^qn#I%?'
        ';4b9F4s1zr%4UfPccHb#?YS=%8N19Dwds6Mg2-)=j;6LO%w#f0y4$p;ZH+4(EeeN7yAlV@zEw*HGwfRnT-8pOasN%meJtlxyez(^'
        ')8f?ukUE_ez7cT3TN6!=uV1H?>39%S@>p^#tNtT3?*+Vkc(6hf1s6Y}_n#LR#8q)w{6Rb~J`o?s;>Y{q!>ag+`01?pnfST*Nc=+l'
        'Qv6E%Iyw8ym7CoT>?;24#k=^;JBaOn9GjR}HC^eeq=Dj8>G6;caQHCjl-Q#0JCcW8m!K=?8c@;?iWIVJ$Pn<`$das`$QUXn6qz}X'
        ';E>}mSEm*c5c^$;y#_>SHbKShd0gm~ip7my7<b(TyCa_3iixM3ph6A4XiE#5;2*mXw7Z2;Oaf30g|SbVq!Oe^QpT>$1E)h#lT#hn'
        'E~=xd<)W7W5fY9o;gCm2aNhPEucLD<Q`Q9*gjuVEJ(J=<1$8rm_|$!2L*1(`gGEuT0Qq-yzlVlBlnv>Sz({I99)|#~t!iOdDlUT+'
        '-!pM9pC7&j;cW)3jBzvY+PVCnSI-vSxDjq_i3oO!R7Z*95ignyO2aTH*t*HY?dbWMG6*Ae*j4vvHh8bSZlg<zRC5^nfFYVVut9~4'
        '-9{wr%8<{4HPBl^HWo(k6mNBUw(QyudUS0w4<rLTv7U+GHzkE4K>GogGPBs1whMw<A|)wxtg2m>5gkSe&9}A+p+kh3?*|@g3Wc!n'
        'b~%};NTB8@MKjZ6@M;6+9EB{si&ZKxsbk$jg21#*6Pvb%m=Mn7bQbU1Mcn06oXw-B#}1STWVqc8Xc!|hw;?+43qWOAUhGDQ!BuFo'
        'umpPp<<@;}A(wM=fd;)y?Sbx{UJx>7nV6B=9@j~rntL4+z4X!PM+(qE^pZLt2WJ)5bj((75WzwCinP%-&)qmWN+>zUjv&3%<oA~;'
        'V;xbHM_PC3T25>$t=!A%9`eEfI^jsC2Q50<QOXFY*roP1NZDoo(j38z7h7V;&cilUN}wO%BVIsQM4g<JdQ)pYOQEvR1HT0V%ei?K'
        'oo&KrnU(QKws}v~*tbd4VV1)_gz44QI$4JF{PeBH*fJs_RNVu{Bj6D(MXy2OaG#hRYmq_Yj+nk@;bp`_FY(40WxP}eRP*2Up89)S'
        'lL;DR{{JZRGf#o$r{7l!s?R8h*YIDr%^0E66V4=vCi_I)vqRhYvln}38HiZ^tnP1ywtuUMXVLYr=~3$8{fztyZO@F75AEybNz7pQ'
        'Kc|QO3uuOJpc(r3unm&<W3L$!f5ME&_b3h0)lbeO=K)XpLs(!4R0I4Op4%DbsXKa}8XH%6FXpYu1}EMyd)irjWpeC1EACcdfltn;'
        'nRGfolPbH>%fF9#sYc;bn2At@+>mGDPi40ib01bNjQwDzkELBRkNqU`Nd9Cw2+#<tZ!(3k-(+&Oo5|0jNA=f$tPOtaLFALQ%9xS0'
        'aOM8f?*NOFo7GCS_HxxI*XzA;JkRau7jE3Re&Y}vk5_9O#&T`5dTX3)*ABsHdZl)tScSugbaHWNsl2{!+$vXB%HzbEyn6i*>`ttJ'
        ')k?j*v{9>nmA)Ciuu|eBl%I$iA}S8l9xkZbj_DW8r~+oy=%}eI9Gc0}A!)8%J&bZI)jNx~S8f?tH_If>%`zt0d0hnQ14Xx|&@(vo'
        'm$@RC>+?s%IE=GSEw9`z8ymHnaeJ};QhA(_uiZS1k!zb9Ms3+xUt3%n&+Xa67>R;%eRFNCR^J#O0oVKNG<a@ZD@;smm1wz1%XL~7'
        'X?dQO3N0_uvPsKVXfbH{IxUhGPD@0KPs{7Hyhh7DEpO9ukCu0_+-G(@rQifZ>y`Z2x(`P$41A9PP{mF}O}05Oxb`~82bcXk<j&}F'
        'sw>Y7%G%6$WF^?*8t@csnPk1Kk4Uknu!R3r&3Wztl5KqeR-@A7gxGqLC^CpvH~(*fY#jsb>KlcvDdP9()i@OMgG<~Sh5MAa4+;l5'
        ';>>9MO8ebGzx+&tb}IWHULzk}wisy+_zilMFZa=9>n~)`KhyFzTK?J#-qjxz?ql42>MY_$=|4nxO|7jP000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
