# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.632202 UTC
# Is deprecated: yes
# Fixed port ID: 435
# Full name:     uavcan.node.ExecuteCommand
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ExecuteCommand_1_0:
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
        COMMAND_RESTART:                 int = 65535
        COMMAND_POWER_OFF:               int = 65534
        COMMAND_BEGIN_SOFTWARE_UPDATE:   int = 65533
        COMMAND_FACTORY_RESET:           int = 65532
        COMMAND_EMERGENCY_STOP:          int = 65531
        COMMAND_STORE_PERSISTENT_STATES: int = 65530

        def __init__(self,
                     command:   None | int | _np_.uint16 = None,
                     parameter: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.node.ExecuteCommand.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param command:   saturated uint16 command
            :param parameter: saturated uint8[<=112] parameter
            """
            _warnings_.warn('Data type uavcan.node.ExecuteCommand.Request.1.0 is deprecated', DeprecationWarning)

            self._command:   int
            self._parameter: _NDArray_[_np_.uint8]

            self.command = command if command is not None else 0  # type: ignore

            if parameter is None:
                self.parameter = _np_.array([], _np_.uint8)
            else:
                parameter = parameter.encode() if isinstance(parameter, str) else parameter  # Implicit string encoding
                if isinstance(parameter, (bytes, bytearray)) and len(parameter) <= 112:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._parameter = _np_.frombuffer(parameter, _np_.uint8)  # type: ignore
                elif isinstance(parameter, _np_.ndarray) and parameter.dtype == _np_.uint8 and parameter.ndim == 1 and parameter.size <= 112:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._parameter = parameter
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    parameter = _np_.array(parameter, _np_.uint8).flatten()
                    if not parameter.size <= 112:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'parameter: invalid array length: not {parameter.size} <= 112')
                    self._parameter = parameter
                assert isinstance(self._parameter, _np_.ndarray)
                assert self._parameter.dtype == _np_.uint8  # type: ignore
                assert self._parameter.ndim == 1
                assert len(self._parameter) <= 112

        @property
        def command(self) -> int:
            """
            saturated uint16 command
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._command

        @command.setter
        def command(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._command = x
            else:
                raise ValueError(f'command: value {x} is not in [0, 65535]')

        @property
        def parameter(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=112] parameter
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .parameter.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._parameter

        @parameter.setter
        def parameter(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 112:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._parameter = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 112:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._parameter = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 112:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'parameter: invalid array length: not {x.size} <= 112')
                self._parameter = x
            assert isinstance(self._parameter, _np_.ndarray)
            assert self._parameter.dtype == _np_.uint8  # type: ignore
            assert self._parameter.ndim == 1
            assert len(self._parameter) <= 112

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.command, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.parameter) <= 112, 'self.parameter: saturated uint8[<=112]'
            _ser_.add_aligned_u8(len(self.parameter))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.parameter)
            _ser_.pad_to_alignment(8)
            assert 24 <= (_ser_.current_bit_length - _base_offset_) <= 920, \
                'Bad serialization of uavcan.node.ExecuteCommand.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> ExecuteCommand_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "command"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "parameter"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 112:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 112')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 112, 'saturated uint8[<=112]'
            self = ExecuteCommand_1_0.Request(
                command=_f0_,
                parameter=_f1_)
            _des_.pad_to_alignment(8)
            assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 920, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Request.1.0'
            assert isinstance(self, ExecuteCommand_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'command=%s' % self.command,
                'parameter=%s' % repr(bytes(self.parameter))[1:],
            ])
            return f'uavcan.node.ExecuteCommand.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8=q@;80{`t>O>EpomKNFmk!d@Y<JghM<GA8DPHRT$$p1>5WGu^4Y}Aw_NOJ7iNkFrk)gom!$>EQr4zPgdunQju40po?a#>7{'
            'Ic9D-2AE5Z!Jcvqu)t1$J!}pOYz}+a_o_&Cx73O)$96C~HejloeD&)6eDBqJUB!Dl{^g%84v2rr3BPTIrc={H9@vIse`wSlUeg<1'
            '%lAS%;#so)8h7j#d^DHZKF>bNMt-0DeO66&>9*_gAhQON{fki$H=;P;y(Bwz*JuHYld-YdFx;B!nY=c=&Kq&Wr@U6naLw8R|6R<('
            'C`$(QRUU-4=OV}5@8zFA%BVsI{xSP~mh9DyC<^R43=Xpofc+M-msDA@bH?V5*%3(7O(Qb&2&LR=xF4Xl_9{>uy6J}YvdhgIZp4>)'
            '(5u~Ey>3Uk!`<b`%IFX<Zx~^uw?N6vI+`4rFBsvl+7vuv_y{x__=jvEOJ2~!2rOU(W;dhzaoy6A-3@7;EZL!(UL#BXXECQGe!#~}'
            '-n2n1l2e7m2skk!5?P!?o=?1{_!t=OGAGr7y3QSMZKS5X$6eD4LIN%!@)?W=5dtG<kCIjKbS(6F!*1G*&K$NYnAW{0@>;|<f@s4$'
            'piU6k?lNfxK=2_CymGQW>_W?M9O8Nri9=3ole-ZRfZK^t_f|PMclOf7OSKHlaabDM8cvRF;qf3a+FA1Adj{NvJHHmDoW#4mF59nj'
            'hqquR2?6U^&iN%eXq~WLu}*>YlRe-^-)PuTJEMN`eC`;%iBRf0?q#Z=L*?ildff@L<a8lv$F(4IwDEhE?7M15Qr<=QnoF8gbkENc'
            'vK5oC-Ku+z4Y)YOc*_GjL=Y@<J`aq@3%X;pVc8G>)~}MoQ=Z!}BJTDjMWvB4;4X$1&>xtM9R~ohiE@{|YB({^{*YDaU>eq~$=n#%'
            'VAP8X2!#di^T^&xq`P{{SO?R>fM1K7)?C3$*so=~5F+>i$k@F~vKwP6b_^U(6{H<Vsha<-h`*2|)RgYX@9iw_(F)y>(p~bqil2A)'
            'Jfl15u9Obu<MwQNMt6f;R4d2B9r(VtFCE=OwUq9Y&jxX>{aez}y>wqnpX=cZcj4ZF9~?vX)8|q;l+TgUgAb&p2k1~rpWieSJc0X%'
            '9%?*2NS{yX3zBvRJl}_74?px+dWgP|(j$FkfT!^6#clDThv|`&4i}aNS&nXdJbjT4r}SrA$^;bf{MaM$rAO({Qu^~Ad%;uScl?q0'
            '(PQ-IDShb&<pnCBIq{?BpvUP;DJ7+CQR<g}G)H=Zl9Zm5e8>;UkF&q>SmvWI(~~JZRm|Dt2ei_wk8KY63O$w5(+~6vj37V_w68tZ'
            'x#_F)bV{p*p1IFP9{U{hHCj#SFCJP?7y<OZd?Iqt5&Daij&^)|3V2q#{X6!==B2-+qbaRz%MLIK#=QPSWujxWmeTPK4yqCfXP)@1'
            '^mRI((zDyP2#kbr=bnmu^b9?l(({`UGYY)N3)EbAYO>IC^n6M$K9bE~G>pCURAr?X=*5&y^rCAV@%6@2mxErS6DfW3k!=SYVEpBu'
            'L~i;9eKVzRZH>e8FvkR9@$H{XK6;tHmC|>9lzo8<@c7kFssnwSzLU}`n=lLBkD*=X>%QTNUl{}i8&K&W8&v5K8&c^o8&)Y{M5R?$'
            'Rp~ezSLp<sQ0WzRMWxr-b(PMud6nK~w^e$F-BGE<ES37qSLr%iSLr==Po?+SeU+vxRq4m<W0iiwK2hnX>{FF~#y(T&=j?Npe!;#_'
            '>6h$Fm43y(Qt8+1Yn6V(zESD7>|2$7$G%hP_w0L>4Jd4&!Uh#KSYbm78>+Bjg$-92Q5dPPs=}%jHm<Po3Y$>aM1@^Z*p&*quCVJB'
            'Hm|Vx3cIba+ZA?4VRtIbQkYd?zQX(pTUXe6h22x2*JAe-mMZLHg?*y1PZjo=!ai5n7Yh4QVP7fiYlVHIux}Oiox;9X(zwo{|NAX8'
            '!SA#C73+h)n*MAM>+&bupADkKfAjqrR-*&Y`m-m}p9$MO_Wq1KDCa+c{*3hc;s0%aMmjz9-%NjoI-e5Web%29{h7qUv;M4qf7Xkb'
            'XZ_iB`?CUF;}T!b`m;yu&*ZA~tUr4i{TbR?Ry28kX8jRv_q1f#kPUBW$*>`tc!-t^8?yDk-j?isWm{btZlqaSvd1?9qs1fKq(7bf'
            '+aw920Jmq$+a!#A-?6z#B2R4O=9{xMvIJk6UeGck0^f=40<|CTNNgSwJ1i*6echUdLy8UU&MvR%m0P@#1>?jnDyiDbt`~4(M<b(z'
            'uQ#|a_KhPktK)cU@a;{FkTEhf$JpfTHT~-JyEkU_#krZKTaydZ`px-klS|XMIeaJ?obp_pxZFLhTEksCv_s|2E|}y%!Ea%DacOd4'
            '2@P{^f!94xZk~%13fim}p}3%Y=(YN3)iT<|3&bDPF5th5ZQOx}Pht}s_sYG%1Ph~Kjk}!iW|KFf%Y@gKYonxTG$Jo(BRP+1nKhRj'
            'FSdI5I@meHUnP2uA`C7F(;H5qB#hb941f>Z4dMAr{u!PpJ1<_iaPC5eo6-Ub|M4KR94yQ-KX+?-L7$tMLBssrq7_Hr!8NzE&1KSz'
            '1NagUqtO5{$(o&S;@3IxJ&?QZa1y(b?T9hHw+6J}_b3j;5d@=gmw;*@zV%<Z9@c+LfzNM4;Nw4x3+wdlf7J#CuJYyl&_d`nqcuDv'
            '5&NbA&h-ONh#!ZDyZm@c({^}mfg1w<9gKsU@A6PUI6v=jvW%dUIiSVS3K;{P=xTUwWY}&fEn!4f5oRu5>qum`jAej5%#Dx1jA(Gj'
            'GfXsBTT0J^Rp2L%RfsT!m~|sf3LkaH9a7p2-bbUky5J&VEke-~d-E92;hNz~DFe>|RdY4vG?)OijubUbyXnK2fQzVwPlCE*uF-Ch'
            'tJ2<lL;{85(E+son#Bc*><Gb80!J7i_nEeZ&uZjGQ)&StP0m|jC%aX!812qua#Ap9z*ivpINks+cy8fIjR%2;jxu>jieoZ4WFQJb'
            '&k$8<^yn$*#OVf7mEnAK@|q6mWNDh%%`#L(mW+b{Oz5;V&mA-4s4cRo0eROnxhvCZ5SM1OqmW<}uL5@vNZ8a3ZO9`aR_umG6ZAt4'
            'p$AHg)HJY!;cmn<3^SYnoZf~pFm}yoORMC*Afe^OfLWvN1v2XuBawBH!Gxs>up*8|wb*r#s+*NOLIhg0@Dx#wEto;B3Lv$>wJisQ'
            '5EnVnbN3Z;);S`%1N>19oUmru4GU(#(?K~k1esi{q;pKNcynrMdT~)mj^SpzF&A@rpx_4FXaYAJ^K^hNBA$RC3^Ro{Lp)m5aALEF'
            'sz4r1;{~T)D++AEk_d?nJlZ9QCeUF-QV^+cV7OruCMzrrfo;31-ra`|V3^70z|(ZvUFj7cYiQk^KjNerJ3v$Q9gda@cr#yxEX*v8'
            '7*9XRsE74kIs(tc5j@x=Zneb1?8?<2=>R9N3?Me+5K<MuPP=7EFLotXkV1M<+Q;k*IauukBRnHVs!{_?pC|FgNsPSilY-Yd0I?2Q'
            'k7%F(o4Yo>G11q^{6nePmup{bLAe_OYybss*|k4JyrGd=UI^tt8{p8&S3S#E6&b6HVw~I#09nAxDLfe>31nKFq2E%ZRr9bCrG}t_'
            'Oi&V8u(V=&_R+K;7Gyekf(<Qfghgn{C~+kd%U-s|j8(&SjJoaEkacpo(RIvj00tpcAk{l~+D>SPQ+41D66diaHEP;HOGqOM9xf?D'
            'JZQ+pVa_r;B5|Jc%0Ze)SR$vOq`Xz<rdZpc<`U5ktAyc10FY%X4@por@QjAV<-x{sc>sOaxZ{k#65vX?QSVW0t%PGg?&!?eb-{oV'
            'lLCAYPLTb8aMd>CUGM=e#QmX?<G0SWelSGA91k31g!vK44U>zx`6{OTCT1RK-LZf>7%E*kUqgM%Rin(`H8KNO<?9A|f3#R-Hst*#'
            'I2@U|=0+hvAuQ4GTMq<BwK6RWqx99SvxZ8G)$#x_oY318B{t^5RxiXb>Z8*726h|`8Je=h#!A8LRwxHzC(1DVeWPdTDQyR(mLU>Y'
            'HH=}o$UT7W8@q9>sATeLq%cj1=dRid>$4HSwYCL}WKR^Ks~UNQgo_;}URih(sFnz1N?fnYc^gn<m4!pmE6GIDuLM4~jS~29Q3B6Q'
            'PA$zX{03W^Y0=R9c|op9g&|%Obwtx%j`Mm?RN;BDELst$YK+*43TK6+iosrVHhEP53FKPLi=naG-~m>+kYS2~uB!zKi_ws&mbuFV'
            'yCHKWOv%Ht3UL76Att^?R|D18I%l_Gog;;HrrGquyVJ8%zkv#EZXV6^&r@Q_=q|KcP(<R2?Lei3xfS)mY76sLRP-~sXcz%Ac@xwr'
            'p=B#5vH;xQ+zfT>Qq-nkADKOYVLxrpY(v`<g|?t0MDG0b!s3m^rRmuvS(YwhLo}rh4D_@$(3yy1`<;l%(|RCtX_3f#vD0a9#4%u5'
            'G|IH?<C%R}KwylpTc{QN4phIZ9>gmK8cqOFS0l5c>J}&0JB1xch9S9$6*1z-!zH=_#NZ{b4vD+`(Lk(803ofr5y2u0KiUG&I0+Fc'
            'LY6yyBx~^&Mnca_m{44f`PB#@4POU2A(M=Xg;sNg2IzW6M3ne}1ENB9>ag&RlHNL2P;~wLQmiW2Ttbib?gOGk6E!36X}5ZQYT#}d'
            '2VHfzP!%%|I@K&!pwi!_$3yqEs8dyRl-EiZG<fb6B<Ks(@e-;$In?!*hF)*WH$V`wuUbc}f48dEe_DUB{@40`Ww$aguu{Rx^LTj<'
            'FURq66faf0oPtZ7?A1+<l{u#S?0)i`-n7@bspD#-+h#VK9MnTEhV-FhBG)mIXUT5-<Jk2q*)#8j_WC^D{V1y@%IjIO^Cm0^VV3NN'
            '&OWqTW&pK@w+i3=cBAcEhBIaY6td))AJ<{A(gVI6i`Ay{`Us5PB};`Y*@3nM>htF=Y<#=rOl`b|zw2ZXzVUHLw~P=3#IVxy`Y^i>'
            'Dd|r)dSWqOu8NS%(*zNnDx@m(NKfGf$x3(-8<-8RhSao4#QmmUurTaAUjp?qv1=UKSgaA2V?ZasPevmk6MrI<l@f%Ld}9MZ4=|Xp'
            'E=w4^)AI(vfqBEk4r<fMe|XxVn~_6r;JXIp-IeR$?~<hZ-GHGqtS5tDIl(%kN{q)&hOGDD{|7+y$62^>RUSqew%%tSSIXNfw}2@f'
            'jQc#2Ka*N}t$o&zbr3~40{Hw3V6##p@@RoWzVbR;e+-aU&cOBl%2~M1uAIZ$7vWM}xr84l@bU&;-o(pgyu5{%xAF20To6GklgPq4'
            'y>b=)CcAaMjwv!@clIPlAWGzWT7hnHtXMX^t3qJOxFna1zRv4*O1Je%?^_;A`KMcKRO$N;hxOZ8F!Y^0Xz1eXPADucJcJML^?8Ux'
            'YySt%%q#_*HUIz'
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
        STATUS_SUCCESS:        int = 0
        STATUS_FAILURE:        int = 1
        STATUS_NOT_AUTHORIZED: int = 2
        STATUS_BAD_COMMAND:    int = 3
        STATUS_BAD_PARAMETER:  int = 4
        STATUS_BAD_STATE:      int = 5
        STATUS_INTERNAL_ERROR: int = 6

        def __init__(self,
                     status: None | int | _np_.uint8 = None) -> None:
            """
            uavcan.node.ExecuteCommand.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param status: saturated uint8 status
            """
            _warnings_.warn('Data type uavcan.node.ExecuteCommand.Response.1.0 is deprecated', DeprecationWarning)

            self._status: int

            self.status = status if status is not None else 0  # type: ignore

        @property
        def status(self) -> int:
            """
            saturated uint8 status
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._status

        @status.setter
        def status(self, x: int | _np_.uint8) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 255:
                self._status = x
            else:
                raise ValueError(f'status: value {x} is not in [0, 255]')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u8(max(min(self.status, 255), 0))
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
                'Bad serialization of uavcan.node.ExecuteCommand.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> ExecuteCommand_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "status"
            _f2_ = _des_.fetch_aligned_u8()
            self = ExecuteCommand_1_0.Response(
                status=_f2_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Response.1.0'
            assert isinstance(self, ExecuteCommand_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'status=%s' % self.status,
            ])
            return f'uavcan.node.ExecuteCommand.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8=q@;80{@*>|8EpU6mKJxYoQ1h@C#AaR7oN6EEbH3CVE`2*c`n!cUOKeX(qEfuYHs5?XEksN6!QUCScVuq6~?~#P9>Zi1B~)'
            '&F;0m9yFoeFE_h0^XBtD?=zpbcaJ=NHa?R7%!Q;UlnBdAK`MDDzu|reWfsJpBvw*`HIwrY$_@=hyO)4{WG~&bckGNAV={^$wK!rX'
            'TRP1Gou#mU$x#;Z4uzP`csJltIf@08Yg-Ux8me)p!y{2{f=c2@(W(;bLaJmOxsb<h^~aBFeY8IEz}~awIOAHU(x=_Zu2K90!0)cI'
            '=IDZiQ0yU^V1jGTw1auj_9S)b$}X*#T8)(4h(Ihx8a5!^pWboiOU*)vHZ<CLiGl}QY1W}EExu{at?UGH+saj%TXIvB(a3$<wB`&`'
            'nke9@7!0(X`8Z+5Xi8_wnj=iafi-Wn5xf*s7HThE_jLaBbp}e8Ep3=Gr7E#V;q)#(d;`z-NAJ{2cmb#Jy(0L@R=d((ZL!vBwOVVn'
            'EM7ETOY@X!?8T`EMTLZ?vLFDZ*0V6|St@v!hZ(W*_6~2bl@KIXrhTlHnq1R69_~QFSu?(#^1!{Nlu8TzG0mINS?kD9J|VmGvcMNA'
            'i#J!BH3$6DYMh0_i(>65mx4>cu_Hjq)a8?D5;J(g?lRv|#{&dGz;LdQ5I-@aR}KN?Y#&Nvxy>r8?Jt*`i(l2|9ir)Zh$NjXGVpZl'
            'g*@1FCF7aKI3<zgnGc=((IHNLt$*_M$~>zsFD+FX`LT2DJx$Q*L2<u4sq&;Zqxg2@xXFpik|cK39)>Y@2pDGuV60S{m8Dv{)^tEV'
            'cR<_`p<^N8DS3c~)FTJz)1N7txGgp2l~NEwFaUWN)YU_PIyC^w4ReXyaDaj=O(DufqG9I>IYaV93<XCCq$J_K{HaLADkAUzVAuYK'
            'ToxO|QloN{)tb%aoUR3jE~c|{VR#C2p(5`>asNONHRNU<kGw3RD_4-U&Sgl3>%~Ey*>m7N-USC{YQQ*|-z!|%fqWm&VHq#u7x)?0'
            '@dn<)CURWE5D{;q%E;mb&>auB6U(+a$=2l-2<Ftoq_7QhnyENT1E7fzSi;G`%rW;DO5d9C6>1_|EAH(hGR)Br$&pvdZOH^CJA6~g'
            'jvy<*xJ%DTFX$!6!w&>>Vr$MPnIFo4rLd8O?)W|Drrl#jM<IK3C8X6?=dKNRmMi7ivhyjco!L$?<ca_~5jex|$^h&(@jv1`)(<J@'
            '#T{SUb7NYmho7xEab4=0`Ev_){nos~;=~&7pdhN(@ngz}pe#{_eIr=T3m>P0eKkNyJq!OZudZ+*WVG?zBK*tEHprKG+8dt5*<b8T'
            'z4TD|)KZfo0=1{ir#w3{a-E6>e9H}vxo$=LI{XvP&v}%0-A3l;x}Lz}cmhx1X==BmmCK})8>Epn(uV^4_GL7Lcen9g1HZ%jGxz|%'
            '$8G!pf5e~A;Lolw_>hW#zY-GI(o`F}ba&L8BiR)n9VtWLg8uTBJ#f1`x?S(qN1e!vJN6qsF4F%U{~TcHEcHbv-{^&OoAH8eQic1X'
            'z^4NYdc@$qP_H+6v;j>>K+A(_w^=YdOB<dJRf918-N0v*AO3TP$an8Y9xD8o$OhG)eDZ=xx3&Bqz((QQwFv+K'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.node.ExecuteCommand.1.0()'


    _FIXED_PORT_ID_ = 435
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8=q@;80{`thOKcoRcI+8_Mx!5PS)Y|wa;>DbhZZ@e^<T>$QRGk}%0)6m%9a-!w0fp%*iH3xclyJRfdtwhSul%6GKhNt?*ajI'
        '@WDV1aS&i(<m4a-;KLq_oQ#}&G_ZT{AwZl%fV@}L-Sgp467_R7D*-C@RKKcv|4&u*oh`rk)tdw2U-W{zs{6WCR(<Z7nq|JP)hu3C'
        '>rT^kd^6y2v~!MoOJ<$Vuev<`ARhW@{HJj#+O2y0PeSeoYJmO5K(u>;TV@l6=-rUpRMWP(CqU)`FRTZl*E88x)z+G@)QM1As%v)H'
        'c645@tnhjm@NuWv)NH+6mCMCZL0#gWZ#p*4xc!~v`Gc4$bl_+4PXS?73j)uq!C*iBW0-ye8Z)Rk+B#`+OK&4oRCO)TBxxHBcRi%m'
        'Tmp#wH*DWru(>{E2Yi8h-PG+=Yi6KY++GNbm=40^bq)B|1R`VOcyw?!od}1O$Kf5rS3uFgU&hrqdS3Md;DF}oofEBvHDhnIy)M}k'
        'M_W|gsmIZO%_XqJ_4tU+8z!Jd5-6W&9w%Br0)vylaf#CqkDg{Pa8gR4Yus{{hswowxUD;$Pe3F@zJu|Af~R?_!(>Uk9r0aWHydWX'
        'y@qLvNo!6JI8EYeUeL1+kmCiWy+9fs0KCsVCtIw~biSck7O|axggz&x&g}pIK<q@TIZK?JJ#+EG#c~YnI3gKt9E*-_AaT#rR^#Z<'
        'I~w#t&)b5PW7ylP-Q40$SSitNlFWRP7K~Fy$ru9eM>{}{u2wgL)tI``bBSQo2C7ouaW7H@1u92xQEQeTM=z$BwnYm_2fe@JXxCLU'
        'koeBQ&jiybuR3lVk&PztSDQ7*GC?o)Gv0K74*?j<jLSVOaJ)_%ts5p7fH4sr7<cTt7I3>SC=!j39=Fl70DkXuXjz~T>mawOOPUq('
        '_;2D8EwucaF_|!93Pv5OqAFCm%L8*Gly0j{Z3S2h1O7;K8uRH~f`3iZ1{1*t0AqLZ(RQ?{(9&=`RS<TdMRUpDy!Z=FBG;l@lD@53'
        'AI;M(ExJwq&f)X+u6J}R-PWRoWZaH*@91{Gix#u-&;!4B_JyN6Xt70i$#(@@Yxjn5bSK@_qI<gLg<j~}d(Sa+H{H{sgUK2#y6?Ww'
        'bT1uj(dX8!1aF{!{{xMu`{;8m`n-hQ0`GU>*aHtdmhPv|x9GvXIKW$YcW6^{(F62giylrn4Y+)7)8pwOdbmZ8Y={#;!26>QH81@h'
        'J<_7z@8TD{h53#>^nCOv{eFuczbC!`1u!o>(i-#_J>H@u<1J$SgGZi`zCcNfo{;m9d*P3(pL{Iq(I3zgEqW?lvqKKZr5`@FHRwrt'
        'szqPCuVi2Z0ce1I>9MX&e@I_!(NaohBD0~#z6O1XmRj`X2c{E70Q~7Ef(IR<FSqD$TehcQ&Qhm*N1oWa^fVoA(ekGF0Ha{cD^C<B'
        'Izr1WI@;EQlGKD(pZKcu6*}6YXEx0d7zyLfJ{A1vtMp8Zo?EXm!!Y+~sx{}I8ZPuKJ=dZa9*So$8pd9Hs<_hg^g@eX>ejAN)UO{s'
        'bv)=rdZ|TUduZOl3^4xkcY-(l5q+&iU*A{{&%qj(P#53$&hVp`>FX`}<|FYJW`Q~0`c7$}Z_qbe^vXJ&1?h)SuJaXFv&AlhfM5eT'
        'T40479b|(!dYB!~QNl=$mRKoAN7-nOUSgMW^a{I@qu1H>9GzveIeL@b%+XuyR*o9X$WfQMIl97Da`X<nlcQ^FEk|3dm7^cB4|DV`'
        'yPKmQvyXH16ZT1te#$=0(a+dtIr=&KJV(D^U*zbQ?8_YeihY%%U$d`s^c(g~j(*F&&9MQ64dhutVTC*!RM=pi9ah-kJR=Gtc~(+b'
        'DbGd~HkxOb6m}`kt|;tEo?Tbi^*ozZ*leENRM^ctyQQ#Od1ffg$TL@AZl0|uY$ea`C{Sy$HHEbl_MyV=D(qv0eWI{W7516JK3CWm'
        '3j0!FUn%Tsg?*#2Z<SV9<52(If+ARBYk8ygdsCkkFfV_?^;rQi{)4a2FdH3sR-ZkQ`b_ZlvDathem?&R)Muny4*zfKGt#c9|6uAf'
        'r1_MP?z8$Vt<R($Jgd+8*Js@t^Q=DGY<-q$*QnI5XZ6`b)@L#*J*&^2Mtz37mKjY_pBW!PcUMV<1=-=Ak_-#7OAk<zVL`U?`&*K&'
        '<u_H8;X#_QH`?K9p4Q|69@3wV{(X%2frrPlSvT=R*R@QplfV%Nxyj*dnasnFhT}E0fWU8J+5qi(JP?P6#Pn0h>|D28#3AW{cKei9'
        'cd{eiz<_b$6qS_B1>5mBF@vFD!dL3t73ao*Sk<zeW%%`4k&qEGKEv49^n`k~a&2l_otv4Qe|M}}QE$vnjLlc@aQJXk7<X)3I6FNp'
        '8OJ(KXa}>CU0})HbiQh3ZhovfkBqrf<u%8Vhv(vkLUGy&5M3bNcbfgEYHF**@x&jb4zEm@cmfYk;t(9q${kM!4kKf=+nn%5gV%%0'
        'gqIh}!=$0r1IJrMa2}LnV?H{T9`*7S;Iogr5?xmj3RS^+%}R-cF*_O_%mckXyq`>-;eE9A!uj)O&&PNuEmYyR_hZYxlr6I}?^den'
        '%;Y38=ErkJ7=Q$q?Tj~<Nh9>&hexz}9nd7pW^#yM<HU6U@0!I)Xa}Yx#<<Qhz=GU^&=Xe>wEArVqyhTIe<pMo|1A+dw+V!g-CHk='
        '(>MRFI52RPFC>>1e5VmC<0XmE)in^V>p24b&_}&XuBS9ii<hfh6Z+rQaS-!u?h6%8?mL{wEa*g{(Bf)^w1KvD)g3#~Oxu^7&;lbh'
        'Gn+5BF*2Ll0;oN#jjw@?$Z*TibY$16#GZRgFrT<qA<PtP)((mi`JmJ8e0is*4@EOIF^g1dVTz78n@4;0mo-;n={XjVnvf}%K?hK5'
        'V^J;^Z@4hV<HBm;NkF&RHQb4EN%ETyNk!p!bpZLlY;d7PW`N3(DUM)3BD3NKGAom*hNJ>U>YO)$Pi8ZnVz|?f$wh&s9$y6O<JbXG'
        'aO_l)MecbH3QFfbNw3KyDg#ysboxk2y^Br(CvG>8k~HV5V-qU4llclU8=0vHFBy6su+Um9I`)Vj2CKrGYT$Quo!io_dSS*!Gw=yo'
        '@e<4q2nn9rz6pK=&<br|YXE&XgYN(lL**iHLbH2y8ir|>2SQ(kF)(&nTa{c%WI=qx2|;JIn&U~YmyX1#Qx7IMl`1Rh(Qq-eErjZv'
        'N?suXDw=qUDA6rgK}H3@TIjVY2l-$ZiJ~XsOYy96)a16}4;MiQ%Z6DuU<JG#lt6=#$zUagqm#KC<KvaNIe|Hvn`wt!tmOcKJ$h3V'
        'dc)CAdnh8}2o;23x{#)iSF7q)sHawy+=S!lOx;`*x&<K-92-cq1CgT84lR&~NP0cZ_8YKR%4slc(_V6JKd=GAN-l>vb!)Z5z2fU4'
        'ayOYD^`sG608?@;j-2y&BZ)!=dX{>Kx1XfdLwuKlz&mjSFE)v;rU=ZojQ$7*dIDhpbu;wARe{<S-!-HZI~*%uA*Cq!qxV%gh<0Kk'
        'ydy_Sk^*#}C$QrLT3+W(!Rs6pu?AER6@dUYGg0Yv^kp*pKxFovwJ)_m+>}r@Pz7hfHs42mLnbvHAJTzUP={s`^$cxEc&yBdadFcF'
        '&4RhCRFXb|fTzV3`h}umDKRUNY6vLs1R0P4p%vY;i>w8-z|+YaY{+5FPfbf&i7h8F%mrgaThdHRtC^MwUMImDMaRrK=pdL1xOxk3'
        '+X?D$skXWU#)<7niW;WZ6xfJ_hf4?_FB)=jnKSc_2%Px5Y*0}+Ea6iSQ{Jp`UBouXxrDVtl+dgI6lB3jOcKcT9Ib9}d9g7I4?yoS'
        'x2z!u0k*^&=^idFXX@B*b`)l4+rU7nlS28xoWT15;F77yUXTF>;{K|V=x>b|`>7!!W;q}r%}=gK_AD;e=1b`E8|Zl?cSk&Kp{aEE'
        '{36nuMUBjVm&qjPDqqo1`on3I>GAsw5I9a|>%B+-L71Z9uPzlFE@p07Fr_bT?HDRKR!$5=vwUZrm6+%Yo82mgRv%>C*RbNKOVgAo'
        'Hf9QXCqaoKwyg}!-_^Q8PsTe)wKU<tN`468B9Q=!Z)9pB&18~nBxOye&mFlJ=4V5o*ToIgNY+FFimIMuNEqzU@yf)TK(<7{Q)0Z%'
        ')~!R5l_d^ott1^yzZCfFCQ{%7X$m|!Ha<U7eGf~TiYRFQwJM`h%7~Xl9?>ut!X)1lS$N_s(^3So8ZESfR9HSKp|PixO_CLW1DObU'
        'IyAKF+`|kPJWQI<b(BDUIvPCH0=Kzm)}^n6CAptvAr|PjkB+b2Q9$+O&Y4Yc=U~d63aeDFRi?+^gA8qE7TNQ+<052qCR$BMA~9lH'
        'kSU>WMLICsLcbNH^-O{qTEJvd1hrFWSqcg-0R8KWp*COA+!XjDy(diAkJ?u^LG24EwLl|S?rfzxH#Ik3nVy$v=^PeB<GF!>uCfLy'
        '6LD?7Z83>k_oOdP9eKCzw96ZD4Ok|P(rvqVXCDFxj1heEi)p<B+3%7A_KJpv3xL&?$+XD2#m)70Vh5O^Nv@lUXkp-Bh^_-LNXe;z'
        '<IXk>L`(t|Ds~nkm}KFjDHIwPA;Lw-bf*tyP2NOH=voOKip|l#Y96@Z>wqVCl3@{Oi?*NuMQ;g<5*r*~6|z!?z&lL3^H>4VvHg-p'
        '6)Y~HM!R+&D=CVck$06_U0V&@_Cv2D4;Q4O=Ru+BSp>@DtvlSeUkch;MVt6yCW1Ooq=Eo_RdqB|RUYl{_)0^qt;#PzP-R~>jv8MZ'
        'BgQwz?-mthV8HmF#a-}cv4G7XZ1!Vw0-NL5j9@baO&IM|b&kn7di;1T+M_ni6|SookW^ETr=xwU?}Xq%RP^O4`tms1j(;q(7Dqc~'
        '9p7A;#oiC%Qlz{RM_X?|Oz`7qHx&22+0;EqH=HH-?XK2WT|=`*bkK%4I_icsh*zq|7eWzm+Fy{s=xs7vh@&mYPJljl_I&RLF0YnH'
        '%eb`@2l&y)e$~)?KoBiUO;W^o4ZPAnPIZ}M60uUNOgse<#VU9!6iQd_1^!A15o?&9uS3ekF;x9^n^<Uhjw^NbGBL{>Dp^bu7D7-^'
        '&_HRBpq#i%D3c|yDEZL_=sjq{8^#r>3FBQK0qmXCbS$FQUH*r+Z8$22PUGhWS??kPd1oM<p9c)K{9051&WWjGs)Ts+WYEyye+_^>'
        'nud;R@;=I8Lt`K2v+l*8z@)Sg_IV|DN{vBdpK-uAh^QO|75yFPW+Bta<Eb9<#dFX;qAo99fOc*1BDB+sm$3UXG^NGY@$n68-o)lD'
        'Y_4E4hRs!M#-TwaTAaiwjMIzP;BT~D<tykYV|HstbPx<hey!!H2FJW*-4`na0>|qzaP*a5r(8M(K)S#6crSVS2^&`We#v3nng(9q'
        '+JU@IZ}9kn=|V{O@=l+Z;v<kfYP$Q9puas?t!V5@p7us3@A*}k93Hm?d!$bgEp!IaZ5U}nA5(-Q^Kt_S6QcARCz+Ir50ZX+zp3_M'
        '*u62QCc6SSC7F}S0}+Y5jQbdmFtmu0y~nXCqxX*geb<{Dn|k|3756`*%i|(&ph3&LLsa|V^0|*G8D^?=EEek-n8@+5>e72rd36)0'
        '97s@^o|#w2Zp>ewsZRa4GJzPKoZvQY3F$I}6d@BmR|vJAmwdw1yYiV$to&TEGVaDD`4BF9cD`#Xrz8DBqHo){z3q6CQK_TrMdR!y'
        '(0INBjoGp47^}=zs))#2;)EnUap~A5mepC31++Kbd~V52%k*2o9;D7~0;$0cq(n-H2wj`+$ns>S>+~cCf-Np??*+ZJeme!}MeO`T'
        'sLRweaA|t%ZM9OZ&Ioo*B6b~n)G`qgn=Zm^xTw#<K<t3pe8rW_!YUYZAg3-UTZi0*cCM1T^Tjpvu782eUt{xgY<`K&FR=Lto4eTj'
        '12%t;%|B!FYi#}vn}5OP3v7P#n0<US&_B#>94OKIc1FAcgvdfqz+3!t3|gscl%)SWBlvDc=C3p2e$yHM{x36Z@jtLvhlbrz7CF-S'
        '<YFHky+`P~que9(-BtRBJ}`+R8^^W2;jDn)3nvaPP8iVn)$HP*ArtmS1uqMVDNtLYTcA2z%we+~o2|KSsjz=i9z`yHl_V=+t^B{$'
        '6|V@TJ^%m'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
