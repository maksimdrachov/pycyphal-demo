# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/node/7509.Heartbeat.1.0.dsdl
#
# Generated at:  2022-10-01 11:53:16.137715 UTC
# Is deprecated: no
# Fixed port ID: 7509
# Full name:     uavcan.node.Heartbeat
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Heartbeat_1_0:
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
    MAX_PUBLICATION_PERIOD: int = 1
    OFFLINE_TIMEOUT:        int = 3

    def __init__(self,
                 uptime:                      None | int | _np_.uint32 = None,
                 health:                      None | uavcan.node.Health_1_0 = None,
                 mode:                        None | uavcan.node.Mode_1_0 = None,
                 vendor_specific_status_code: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.node.Heartbeat.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param uptime:                      saturated uint32 uptime
        :param health:                      uavcan.node.Health.1.0 health
        :param mode:                        uavcan.node.Mode.1.0 mode
        :param vendor_specific_status_code: saturated uint8 vendor_specific_status_code
        """
        self._uptime:                      int
        self._health:                      uavcan.node.Health_1_0
        self._mode:                        uavcan.node.Mode_1_0
        self._vendor_specific_status_code: int

        self.uptime = uptime if uptime is not None else 0  # type: ignore

        if health is None:
            self.health = uavcan.node.Health_1_0()
        elif isinstance(health, uavcan.node.Health_1_0):
            self.health = health
        else:
            raise ValueError(f'health: expected uavcan.node.Health_1_0 '
                             f'got {type(health).__name__}')

        if mode is None:
            self.mode = uavcan.node.Mode_1_0()
        elif isinstance(mode, uavcan.node.Mode_1_0):
            self.mode = mode
        else:
            raise ValueError(f'mode: expected uavcan.node.Mode_1_0 '
                             f'got {type(mode).__name__}')

        self.vendor_specific_status_code = vendor_specific_status_code if vendor_specific_status_code is not None else 0  # type: ignore

    @property
    def uptime(self) -> int:
        """
        saturated uint32 uptime
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._uptime

    @uptime.setter
    def uptime(self, x: int | _np_.uint32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._uptime = x
        else:
            raise ValueError(f'uptime: value {x} is not in [0, 4294967295]')

    @property
    def health(self) -> uavcan.node.Health_1_0:
        """
        uavcan.node.Health.1.0 health
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._health

    @health.setter
    def health(self, x: uavcan.node.Health_1_0) -> None:
        if isinstance(x, uavcan.node.Health_1_0):
            self._health = x
        else:
            raise ValueError(f'health: expected uavcan.node.Health_1_0 got {type(x).__name__}')

    @property
    def mode(self) -> uavcan.node.Mode_1_0:
        """
        uavcan.node.Mode.1.0 mode
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._mode

    @mode.setter
    def mode(self, x: uavcan.node.Mode_1_0) -> None:
        if isinstance(x, uavcan.node.Mode_1_0):
            self._mode = x
        else:
            raise ValueError(f'mode: expected uavcan.node.Mode_1_0 got {type(x).__name__}')

    @property
    def vendor_specific_status_code(self) -> int:
        """
        saturated uint8 vendor_specific_status_code
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._vendor_specific_status_code

    @vendor_specific_status_code.setter
    def vendor_specific_status_code(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 255:
            self._vendor_specific_status_code = x
        else:
            raise ValueError(f'vendor_specific_status_code: value {x} is not in [0, 255]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u32(max(min(self.uptime, 4294967295), 0))
        _ser_.pad_to_alignment(8)
        self.health._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.mode._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.add_aligned_u8(max(min(self.vendor_specific_status_code, 255), 0))
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
            'Bad serialization of uavcan.node.Heartbeat.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Heartbeat_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "uptime"
        _f0_ = _des_.fetch_aligned_u32()
        # Temporary _f1_ holds the value of "health"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.node.Health_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "mode"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.node.Mode_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "vendor_specific_status_code"
        _f3_ = _des_.fetch_aligned_u8()
        self = Heartbeat_1_0(
            uptime=_f0_,
            health=_f1_,
            mode=_f2_,
            vendor_specific_status_code=_f3_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
            'Bad deserialization of uavcan.node.Heartbeat.1.0'
        assert isinstance(self, Heartbeat_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'uptime=%s' % self.uptime,
            'health=%s' % self.health,
            'mode=%s' % self.mode,
            'vendor_specific_status_code=%s' % self.vendor_specific_status_code,
        ])
        return f'uavcan.node.Heartbeat.1.0({_o_0_})'

    _FIXED_PORT_ID_ = 7509
    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8EGjr-0{`t<TXP)66_$LHyuO05fH;Q6fU`=Zkz`{qhB#SdDQwnSsbq;5Qq<5p)4Sc$?DS-&XIGmP34}6b7n8y%214<es#JJO'
        'Ri5|(dEh7T6Zi!bm8YE3-Lu-2B^+1rme}R_di#3%oYUv#cMg2~*_jdjCwnsL`H3GmZo*<g1Myqh2$<t~vK`4pD3)i(uCYM0q3N&n'
        'B9?!YPrjSKotLvit_VXG=X@kPc0<Lfr_z`WPdVs@v<+LFPHD%Zp%Y4<Ij=Grs|KSg&&J&jixVM3++^%E+x{r8jn+oq&)?0nBQ8}c'
        '7L8P~B!3fj+=JZytUNooC|KZc(@=7Ks;H}wu)UT?F<ww~V8*HSFcGbg`PERd7K?{3bi{24<pwNlDW2B|Z0^xSxox;t&L7VvR*H>q'
        'nKKV#OE?5K8o8CP=Gh}|qG;&T*dN^JcG}>j>`)phf!sRa`qIm9o*Eq)`E|lP8TxOQ);J?(oS3eJcrpbNW0G*020jTH@RCUQGy~an'
        '2(BombVU%5m{E@tr8kP8Qwx=dko<n`;`5{jQc0#tX(U6^<pO8oVKBq)4}|v!Rb+N+(f%Q@xd`-*C|DvAI0L4|pejyj8Tw;AkdQVk'
        '^_gOxg4wVKg^6vc>^e>d7Q*2ygjujzhXyGl0i#hu8r0kD0^1TN2WFi%;^2?*G21F-5AV>i02s@U^5car@rOWv23DT2ttV>x_>=r;'
        '{>&XMg@gLkoS)A|@T61O_`D2JXsWLTdoLcVFE3T=mFu{C)(8NeQOH7t%xR{fr$E6)*dkFZK?XsOltbATAq^&-9A1<;JUd&cDcg#G'
        'Gx#colyrQR;zl$mXyRA1!_AoL?GqSZv~3vAMrU)>y`%vozHq-Aj90F`R=u&j`Z`|W?-k<3aHK~A644l*vQ{R%j!fZSlf*P^F(PBF'
        '1lyNoq18N)Cnaz{n9-yn00UtZz?YyEp;W*JP}@+IaD9?Cl3t=%n>1tDCcvMjjN8a98ususp-@q1Fs)UyU?->qzsf6?4}38joqK=_'
        'kIh%s*Q(2Pyl-diyKX@@25te57)3fjBRnJuO5Td85A)F?AYXt_iNL0z9v*`>F6Qyk-O0c3Amsn5vRbd!e}Uw`F-(4vHk+3ACRo4#'
        'ZV(haE9g%{G=N0O;wG9(0hbQ(7RB^?NW9o5k!7a_Y_!|x8IzBsKF4SI%ltC0^I!7U`8xOcTPavjpMlUl3U58XlO1=PVvG51BxB_Y'
        'Kd)yGxrt0;kHJ8|+=#+6&c+Y|(a5vIE8vy3R<QRYu*ah_VDQ($n1j+EYtzj{w0%&0E<5l$>Uq70gSz-&Z1U_(lr{q4xiM>{0Up2Y'
        '7-01wV?Mz8q5;XX6UKx%bIz=TZ!uSBzfZYftbnK(7>quoBRrPh;pcA(FxHhuqVU}f$bjojfT74+EpCTYo7*PSavdyW8YmHgDDd5O'
        ';LXAND1(vc2yH)$(U7UGj5morI+>g*p}_1hV5U@>6b3tH&A?b(R*Xn<G;EQm>B0A94n=D;e88krT9g6!ljKT?5Ux~|T$!2acDqhM'
        'yN)O0kOhIm{B*`^#xsg-shPRwW-eTG<}O~iuwzA&Ql}+5GvM6PHZbS9Xv8$`&9s>>=uE}$h(yLccV5IE$S0nu%)1vZ>5Zo6oXBsY'
        '<I}qPJi5q6075%o*vV~Y3Q|!!f9KiJSA@E*f8StzL!Rw-Wt3-RuT7F(yCFeiK<rDPK@cq9@yozBs$@JE2zgvU$id&wPOMPh2aet|'
        'iGP5j^)!H+^>&W(s~_g&+P=F<10tfx?2y;S(+1oV<O5A?&@F6?VXy)G!A)zUxNhWbZJ)*cW}n&t`}-i`{=2n9wtoz9^lok3jvq!G'
        'zgsI=JYw;v#bXwaTRdU$q{W9UK5X%n#YZfjwm4z&QHzgReB9y>ES|CWLyKoEK4I}mi^Sqn7SCCH+Tt@7pS5`2;*TtrElyhevBjTQ'
        'oU%A=(XlvVan|CT#S0cMT71spC5z8ne8J*ni!WNdV(}%5FI)Vn#j6&7X7T41U$uDCBDc6@@wUZJEq-qC3yWV`{L13j7QZ#PG(Kt@'
        'j}?t_(YRbRUM(6oiv}+mTSen`(fG7zd|ouZC>mcDjjxKv*G1!7+ejhahKPuUI!&;B4ecl)eC9UhJD-)&5z@jM4;x2q0!5<D@1C*b'
        '$-!7sNAUk$B)NarNRnUL!;=q9KeD{Cuv)=T#Keyib#xg4k=j_Gm2PX2cX;Ca1b0J69Iw`^Yt_p2>Km0J<f&Ifa5g#<(zaEg_s8h8'
        'g>mOghF5JH-7^~uiMF=cib4EJn>q)<;605VG!h$Tz*41JUt6eG>hlXo+PMX%<xCL>KG9JibyMI1g61^D8ET3!<vnQRG<4jF8_SDp'
        '5Irrp>nqnPYx>CfI_r`|HWj2AY^EvVHa76;4Tcg3qz>+EyxWjc>7H1pK52-N{da{*d=u!{I0T`>#y<QU!Os|eCh+qxexAb5S^P}l'
        'rwpHzx9{+<&Lxk_JmHF`yu-VEi}$i)sGP$w3V$2ok<7y<FswSL`qb!sX_cXahpT8Eg<O(`a7B_PDBTd^KFsAIf&ib4A!-pgBoXsO'
        '6Y>EY6#jw#(cJVFzuot9f9kjXJmB5-gLmT}qf_Ib)W-Q=;NPeJcVYkYE-dBW?6BhpOfltr_OBr;ey=X0Lh6t{;n-~ydkyVX6DvTV'
        '$3AK*XgAJmu@E*0NC5d}pi@^yA<hCLXEIXz0-9;8>lQ4a4H;vWKrmavKz+I&B{ygyl2V%Bu^k!<i9t6$4YZ^B1%XX$Qi#uYc$jTd'
        'G;U0hsr;OQ6xf%sTRbn<_$t@4oLF6sOu9cs%*^RxrpY3#Ys2Ya7r|=kln-(S-G%0g7IPrRZPR2^)3uw4JUK|$#8Ty^yR!bu_3FHK'
        '7%q6I>hd)tNexw|OlD;~2yjYBACeFn1UkiMTOI?ZXiuWkUdOB{=9%ghO!T;}CUhZ~X2VsbJxuF;yvxvCPAo4jUa!^{+_mb`!t(kW'
        'UgCHCOW2$&pot=F&<P53=psa)jIJ(Hc}#S4c5ez9wopaeSSQdriG>N;l2ZePvj!&RAyxs<cgkin0JXcXo8Zs#3H~iFZ@dQ{fd6~r'
        '4tj%I`1ue&AK>RR{Cv{)5KHT4ck>aCzHn*w#qFx=F5cp1ci%wvI;c{EiK}^A!aOG#g74>|#iz}K>K7LDV=}^ri;Fg7t(fe=%^MIb'
        'XqAAB)+v=L(4N=%xh)dvm7I2%^-|N-YlLbq^qW*5>##~;-n$J;te~JDlVDv)z#`HHX1zweuyhsloKk)J1Yc@p+i_5t28kq_q3ptI'
        'PslkM%COhQhpmY_H#wlteIlfx!yXBDLcR8xd3v@NH%9>=<L2h(X8V89&o)E|>7c3ALXgVh(3m)Qr6i&XJFw)642O3Qk!%pbEn*0O'
        'wIar)q!)TTmSGXTm6?v2pfz8qPlKIeeo-?>CUwyVh7t)%s&~Pvi!Nfdk%2T-5@qe_^U?U(qOF#Gsc!a}?qWU52Gwmi8WLHg*&5It'
        '633dJ7mEhY(EMV<a=L#IaeE+vK0Pl(H0j~4nRs^CB;qj(@&5|Gd$)~$z`M~uHvS2%?`!^G$U_E09s(f`!H|c4Q-_W_EWzF~^p>}K'
        'i^;>?8&}{!Gk+EaW(Vhwrn__x5-|=$n6;N-(&c;48tyhum>+?B=cLJVCU_al&#k`EL3{H(o2ZSy!i2sx+V~s%%Elnm13|02_Et9G'
        '`u4w|Viyz-45|6=oB>-;z}7!i8$}yxEdFj<wTlezk=LNQJ-UhxX_ZAxiM>ico2D>xbcgJb?V7zKz}~lzy+y>DXg(W}pi;bZ?;tL9'
        '{sY&>x38re000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
