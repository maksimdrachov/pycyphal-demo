# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/metatransport/serial/Fragment.0.1.dsdl
#
# Generated at:  2022-10-01 12:13:28.089911 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.metatransport.serial.Fragment
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
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Fragment_0_1:
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
    CAPACITY_BYTES: int = 256

    def __init__(self,
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 data:      None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.metatransport.serial.Fragment.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param data:      saturated uint8[<=256] data
        """
        _warnings_.warn('Data type uavcan.metatransport.serial.Fragment.0.1 is deprecated', DeprecationWarning)

        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._data:      _NDArray_[_np_.uint8]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if data is None:
            self.data = _np_.array([], _np_.uint8)
        else:
            data = data.encode() if isinstance(data, str) else data  # Implicit string encoding
            if isinstance(data, (bytes, bytearray)) and len(data) <= 256:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._data = _np_.frombuffer(data, _np_.uint8)  # type: ignore
            elif isinstance(data, _np_.ndarray) and data.dtype == _np_.uint8 and data.ndim == 1 and data.size <= 256:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._data = data
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                data = _np_.array(data, _np_.uint8).flatten()
                if not data.size <= 256:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'data: invalid array length: not {data.size} <= 256')
                self._data = data
            assert isinstance(self._data, _np_.ndarray)
            assert self._data.dtype == _np_.uint8  # type: ignore
            assert self._data.ndim == 1
            assert len(self._data) <= 256

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
    def data(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=256] data
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .data.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data

    @data.setter
    def data(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 256:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._data = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 256:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._data = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 256:  # Length cannot be checked before casting and flattening
                raise ValueError(f'data: invalid array length: not {x.size} <= 256')
            self._data = x
        assert isinstance(self._data, _np_.ndarray)
        assert self._data.dtype == _np_.uint8  # type: ignore
        assert self._data.ndim == 1
        assert len(self._data) <= 256

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.data) <= 256, 'self.data: saturated uint8[<=256]'
        _ser_.add_aligned_u16(len(self.data))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.data)
        _ser_.pad_to_alignment(8)
        assert 72 <= (_ser_.current_bit_length - _base_offset_) <= 2120, \
            'Bad serialization of uavcan.metatransport.serial.Fragment.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Fragment_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "data"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u16()
        assert _len0_ >= 0
        if _len0_ > 256:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 256')
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f1_) <= 256, 'saturated uint8[<=256]'
        self = Fragment_0_1(
            timestamp=_f0_,
            data=_f1_)
        _des_.pad_to_alignment(8)
        assert 72 <= (_des_.consumed_bit_length - _base_offset_) <= 2120, \
            'Bad deserialization of uavcan.metatransport.serial.Fragment.0.1'
        assert isinstance(self, Fragment_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'data=%s' % repr(bytes(self.data))[1:],
        ])
        return f'uavcan.metatransport.serial.Fragment.0.1({_o_0_})'

    _EXTENT_BYTES_ = 265

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8=q@;80{`t=O>7+3k)Hk^Qa>J9wnbaA-L_?En22La7Ui*HXQ?PL=)4p|SaO!xpNx8Dp7`3F>7MQGp*RM1!5nr$0}X5g?ge<%'
        'kw+bQ)RDjjyFBtpAi#pyla4%YRrebX#}XaMkz{Nl0b;#=KUMXr>V5T!d@K5YT%Rap|Kc}0y=K^KRcav*T&LxJ<<wieQfv6_jvu-a'
        'Pvc|PqoCV}x&gn@>+tlObo}?}Kd0r`sCiBs$Io`1rH12G+B|Zi!12P4A4HX$UFFljS!i=FO5<W}i3g$Ud#NbI)^B9{o0Jup@^9(y'
        ')A&fuiK4)*cOxFA|A+z(QEh)#8XKRwywx12G+JvqkyDFEPod_W!ie9J8b)rLSFZQGh6sGm{faklU`H4^?M^BzF~Ss9AWg(klrBng'
        '`N_ld=mc)tjoc;F<K!1!=q`A?`I#5-1s)6=>PW5bMzt3A79x?dDr(tq!l>5vo2ccP_?5XnBU)CuhGRfOXd2~T)6diRr5ft!HJzY&'
        'kkQxOI&SSq+ie7X$Q!=bOk=&)^c(5?|Eh(;4Z&@%+phD#_HWq-W`%YnoX8f=61O`}81kkax?Y3Zq2K1V6QGE|33_(hC%@UQhx4<U'
        'QDu~v%6??(2krt6m)#1lT*zjTf$h2z@^RY@?IyqFqD|}$4<?*Wr{y-B2z_3$iA|#$1jJ{52}$aPd=wpJ*SQ_=f9j%daQUskZx6VK'
        '`|it_*=<ye2N&#+^K4SXN4^+>Ueom!us2w8ac`L_ZYF&ccY(?+Ijt@yEhFFd_!5~3f81*Mw{!jW$EU7Lph@i8ZWHz74F`4nXmr%J'
        'C+thVo4PV=S)A_F{cdDmx>TLAd)x`a3-)c{HUtfI&~s6*VqdkdT+VnNSc`ghF?Is`w%=_vQ4mV7?XKtX1`k6ga9h1x1q=k+jlz9x'
        '(QLR3wIz>Cq0~tD-H>Kw;&HgyMHaS$(vUG<cF|s5gmG*)0ylKSO1_zEEsO=XF>&qctX=l}$o}-_<M#e>4()~$U{G{BWUmkGdJhjN'
        'N$fbimhWUfMn@qYR5HbH^j&4QN&N+!915q^A`erzEwuPVHa!<{iw_Ld=Gc+PXteJK42ts+g$3ClpivJUW1|tnN{R>JcwD^Zdvr{q'
        '{c|TyiZ^8IEmjq8i?ggi=SiH;kB;@lESvrH-_E9DJU;h#Jn+9QI*T{-8(Cw~^KW~VG&XCQLTUVZ9~Ag<2Lq14YzPvHpJ(yuwEFsp'
        'sdxmp+@RhN$3K;A9FLXBlr#(L-8zp?9>Bp`y_cgb?V>DR6Yq<OE&@uEqfk6fyqSI-AFthVmwB^Bj;guMbT&Rw3;k};;5g9YwT^>u'
        '5nDuBZas}h<`CJJ=cxA^geT=a1kx|?q@Y&E+RkF=wwtJ%@R#tr(`)oP=(&j|Z~JL{y3?)WIj#kKq1z(y1Hi@AW{$InLu9%%e&eB7'
        'Te(=7tdQ-}h|uk1O*kRyNN7-#=QaHree$2P`S~XaHc6o1K{)UO1P8J?g)yFS2hVSG+Yc5evI7zxkeRtK6N-ToiJ=3B4E$C%hlC6f'
        '26FI2xC;W092(hgBi=QoU<%*5kDL&!`k<U0$t9fQ2NPk3H{4t9fw0GXvB)a~&Gi<V=v+T+21t&Zj=ue!#z%kVM!(9wuk-zwj<uTK'
        'Nn`skCSk8#_t8ISRX~49jQlkoPABq%K}Irb4S{Hoihqb-m~)y0l@Cl34vo%sTP@56-yRiH|DKjvH3{pO*E>0floh*m+-KYMD9d5P'
        'S*C_XnGU0cm@<Xd6%wXOsu5Karps@GsFE;K_FJ;QDCvmoA0=ug?1-FylxQ(w$B60)J1*zHK=eq$N^<-JQ6ph5N<JrvzL>C=h?Wxe'
        'GSTA+dxhxHgq<Qfny@js{#7aWH7Vz`<a0*Kd!6X%guOxZwS>J%^wosfM8^{L7SU4)dz<Jh344d=%LzM6^reKoOY~&I&Plz_6Frfz'
        'vea*!=nDz^k<|0YM2{uxg4B0H?zbZKevjx#!X~Bu7l~R4yCnDVzO=_>xu49hTEec#eSIM9Tb29!F!wwANYbB3`mv;+NcvMr|3=bj'
        'NoORTmsCi)Ea|GGYm%-@x*_SNq}!72O1hU*C@Qis)^C*ijcUI!({If88=~J>?l)HZjkSJbz2DgAH#Yl??S5mo-`JClE?)L9L10=T'
        'q?dhl!g)+UBhldcIUW}%j}0!Jrw_UO27%K{<5R!ED*^T75OI}yhcBJSYP`kirY3L0gH%|=RCr08U&X^Zf;Z8Q({Q6+3I!#8u@5G<'
        '=vw{2!V)e#mn{@ui1{1`{$Bj<09?F`Ntm*d_fXs+aRfVv^mM-$3kRU2gitcX>eT0sx4=K=9Ui%df!JaOF{nANILNG+WEO6*f@njb'
        'D7-_F2WyW9&?oC-8l46+|5mAO4UI8_PR|f34UI92PTT1Idh97mw0dA38=;eWG#@LHtYe4HV@K$eA0Oh2y+<X|9lC}cBeW<<84?G-'
        'b2fW{@aDw_B;iO&;^v=R&ra-PYXN5!aiov2kF=JZBusqep*rB`OA?<SnHPJRFn6qP>5|0r$6C)$5strhs7^RzOy-5h=F48CoN;Ez'
        'UN|}?^UC+)$4;{|G9MkPFU~q6bJh2j!Cq%?$UK+Xc0b$wSsdA$%$C`*!0hkRpQOL@MC7rz*xNEAlgtBtAS=E5#AL8{*jbtB3*Wsn'
        'oc}h>J^w^yvv=7!d9$E>N}r8CaT)A9E6W?pBkdDcl;zFliR;0}*^lIHDfjJJ<XJxG--)Ltm;IPskT<hOwgaxZAa8L`O(!<ND)NSy'
        '$3Z!dgo{sIDtnJj%Dd=eSp-*3%Dd}R*N<Ifm*o9;IASg!@5z4DOg%GQ*!%3Vyq`a|&2aT)d8dD7y0R&DrC&enN7p39*N4ws5B9-+'
        '?ee{BhaCDf&okGXeaJqNb=Je<@G{D%QY?P*gXzb9!akO@-}kmJa`{-+jX&5P*eC3#vSuBMS*qT|AF^&Js8G<MU}Ay6icnOcsKcHC'
        'MU$1Fq(VuDlF7zkOocHW#!T3=m<_fHwhp$*%1~CJtV7vklQ5~mqz;oNt3p+Ust#3?O~bSb(>hF>YzAgjn9*UzWOFd5!ki9sCYy(O'
        '73OuAH`z_NslrViZkkMhP(kP*OxA&p3LPCfCR>JO6_#~aHrWcSsIa2Lipf@CRfSa@R!x>bqC%oWVzM<@Q(;YqHIv<eJ1X4K;f~4H'
        'VO@oF9o9{D7w)QXSBJYM+kg!fHgwo9**&<Y!aW`CnQRj_RoK*F(_~w)rNWjDTPE9vZ56h4*f!Y??5MD#!;Z;zVOND+9d=E2AMUGg'
        'Ux)i9+k-t7_RyYaT?Gmn6bvX>SlmNVgCZK)f|3Fy4N3--EUfimOoK54#w@TEur;s^uq`b8p{zmKfU*UX3QTG+X~3ifRRyXVR1K(F'
        'Fs;C}2Ga&iTQH-*j0Q6X%vdm|z?=qi2FzJ7ufV(p^9IaYa8rSs8r(GCrUgO)p@A?!SkO_Rqd~`jjs?pKENifAz_JA^3an_bV!(<8'
        's|u`Yuxh}n1&IQQ28jWQ1#1edX|QI%ngw?hxTC=x1MXO`uE4qm>jtb_a94r58r(JDt_2$kY-q4yz=j3)6u76sJp=Apu&KbN2Ac+K'
        'TCk<SmIhk}Y+10az_tc^8f+V|ZNZKLI~wd5uw%il0=pXQ8nA1@eFg4oaNmIY7VIfWx6VT<qDxprm;OH$(M2kro)^*2polKzc6eSy'
        'KZPP1ui&|LpJ)+n|Ea|M6pCnj*bjfPMYKKm#m8Sw5lwqOi=4~D{{5>iqRA%Zek43EqQ6x{4@b=NBKmQQ=p1FrI97UIME@B@be@%-'
        '7tzn6h#nx~!6N!#35|6#6pQ^DT9q}liG>GM(o{re#kBrImeE)~V;xP!wEplin#yNcNk1>6|5D57yoSbN`jN|M`R9I}9vG!!T>LkF'
        'UU<kGwUPV}^ZDzv<JYdvUA^|%jo;RO_S+l3xSp*OQ=%&W%q>2NwM$c12G7RCRbujA;>4FdrBD!CU;Yb{FTcVcU2$zy{CrmYLd=xK'
        'XX2NFiC<xS&&J1wUhJl^nLjm1;}iW?yOqhx#lcf8ah;xJeSOt#h_1Itum1w)wtNc6mm7lqVBgFhCfbgj^BTM$tk~D{o|fw^hIZ4>'
        'p4Elj4h?2c2k9*rJseo#tzQ1rG?&wMdi3%S#SI>(hVECql0N(yLSw%*==)<n?SJUm!NX?O#3EC&Cj(W{#{V8p{=+PG?Bu@#nGtQ6'
        'DGs_9>8;a){p5+t{{a{1!?Rv3000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
