# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /Users/maksimdrachov/pycyphal-demo/public_regulated_data_types/uavcan/pnp/cluster/8164.Discovery.1.0.dsdl
#
# Generated at:  2022-10-01 12:13:28.043459 UTC
# Is deprecated: no
# Fixed port ID: 8164
# Full name:     uavcan.pnp.cluster.Discovery
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
class Discovery_1_0:
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
    BROADCASTING_PERIOD: int = 1
    MAX_CLUSTER_SIZE:    int = 5

    def __init__(self,
                 configured_cluster_size: None | int | _np_.uint8 = None,
                 known_nodes:             None | _NDArray_[_np_.object_] | list[uavcan.node.ID_1_0] = None) -> None:
        """
        uavcan.pnp.cluster.Discovery.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param configured_cluster_size: saturated uint3 configured_cluster_size
        :param known_nodes:             uavcan.node.ID.1.0[<=5] known_nodes
        """
        self._configured_cluster_size: int
        self._known_nodes:             _NDArray_[_np_.object_]

        self.configured_cluster_size = configured_cluster_size if configured_cluster_size is not None else 0  # type: ignore

        if known_nodes is None:
            self.known_nodes = _np_.array([], _np_.object_)
        else:
            if isinstance(known_nodes, _np_.ndarray) and known_nodes.dtype == _np_.object_ and known_nodes.ndim == 1 and known_nodes.size <= 5:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._known_nodes = known_nodes
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                known_nodes = _np_.array(known_nodes, _np_.object_).flatten()
                if not known_nodes.size <= 5:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'known_nodes: invalid array length: not {known_nodes.size} <= 5')
                self._known_nodes = known_nodes
            assert isinstance(self._known_nodes, _np_.ndarray)
            assert self._known_nodes.dtype == _np_.object_  # type: ignore
            assert self._known_nodes.ndim == 1
            assert len(self._known_nodes) <= 5

    @property
    def configured_cluster_size(self) -> int:
        """
        saturated uint3 configured_cluster_size
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._configured_cluster_size

    @configured_cluster_size.setter
    def configured_cluster_size(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 7:
            self._configured_cluster_size = x
        else:
            raise ValueError(f'configured_cluster_size: value {x} is not in [0, 7]')

    @property
    def known_nodes(self) -> _NDArray_[_np_.object_]:
        """
        uavcan.node.ID.1.0[<=5] known_nodes
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._known_nodes

    @known_nodes.setter
    def known_nodes(self, x: _NDArray_[_np_.object_] | list[uavcan.node.ID_1_0]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 5:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._known_nodes = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.object_).flatten()
            if not x.size <= 5:  # Length cannot be checked before casting and flattening
                raise ValueError(f'known_nodes: invalid array length: not {x.size} <= 5')
            self._known_nodes = x
        assert isinstance(self._known_nodes, _np_.ndarray)
        assert self._known_nodes.dtype == _np_.object_  # type: ignore
        assert self._known_nodes.ndim == 1
        assert len(self._known_nodes) <= 5

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.configured_cluster_size, 7), 0), 3)
        _ser_.skip_bits(5)
        _ser_.pad_to_alignment(8)
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.known_nodes) <= 5, 'self.known_nodes: uavcan.node.ID.1.0[<=5]'
        _ser_.add_aligned_u8(len(self.known_nodes))
        for _elem0_ in self.known_nodes:
            _ser_.pad_to_alignment(8)
            _elem0_._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.pnp.cluster.Discovery.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Discovery_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "configured_cluster_size"
        _f0_ = _des_.fetch_aligned_unsigned(3)
        # Temporary _f1_ holds the value of ""
        _des_.skip_bits(5)
        # Temporary _f2_ holds the value of "known_nodes"
        _des_.pad_to_alignment(8)
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 5:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 5')
        _f2_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
        for _i0_ in range(_len0_):
            _des_.pad_to_alignment(8)
            _e0_ = uavcan.node.ID_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            _f2_[_i0_] = _e0_
        assert len(_f2_) <= 5, 'uavcan.node.ID.1.0[<=5]'
        _des_.pad_to_alignment(8)
        self = Discovery_1_0(
            configured_cluster_size=_f0_,
            known_nodes=_f2_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.pnp.cluster.Discovery.1.0'
        assert isinstance(self, Discovery_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'configured_cluster_size=%s' % self.configured_cluster_size,
            'known_nodes=%s' % _np_.array2string(self.known_nodes, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.pnp.cluster.Discovery.1.0({_o_0_})'

    _FIXED_PORT_ID_ = 8164
    _EXTENT_BYTES_ = 96

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8=q@;80{^vHTW{RP72ef)wX4;|vSdrLB}=qr%j?_5c5_kEw6SA3u`rgc%9pB_fZ>v}8p>Rf=5S?gfB;Q_26jN8Ld~N23Hb?m'
        '>uX-~7N9_Z0)0q<{(wC8oSDPD*iv4C>S4d(;mq*NH|Koh8U5kVU-ypZ)L*g?wjJqsHB<7)wLJF|tM2idX$Q?PkZ#P=WORjlZWEf$'
        'gLcT%7wP%W(ofTBGHANK&!bf2lF|Ed)UxAN#QVDxP2Xz56mu<W$F}@h=!Z4iYsr{LwG~&|!48kwX;L-;r5pG-SLqS8U!*M0a-XN4'
        'rOB{q#c|};TQQgEM=<dLUUzz>N$~@hdrsGtis@LfWya{=LBqoc*Xiy+kI9F=bhmu&tokwE;!*#)hRwPgn;!SKVv(`}Om15;Hk*ON'
        'Q*k_*TF)lJVYQoZZw+t3igJHSH`3&&DPzlbtjOt|=y|IyD#^4R_ziapxO7b7%9QRW;L{<~3G6i4eIU5ux0-bx89~FaJTI`VIEbX-'
        '`bG@*Xp~_|qdS)o=$n%J4zOQ&AY5teSY8WE0_HI4T;GQcGb}p_q{OLvrmv;o-()hfZaI$YZ}sylW|9;8le!bQ4s7uwfL;>CJS$3E'
        'Z!Q%};wnsitTWT>0lOPT7DUVRBMYoxxua;if!6-*88x}bo7|7}c8e0tTuH_#5PjH=+UiOwM#NYaW#Y(3Y1aucORae}E*8Y1IP*+x'
        'Pf>A3K3mCTPh^_)wvKmL-HNy_Axs<|MjYtlPWn6<GaK$M>}nW9u?eKyO^%o{Xhk-M8y+`93xXgiA$V>*O@`JX19#Wa`T|y!e+{Dg'
        'Ay6VAC!5w|={B9nvPG~1*J0akhp>;A9o`I5V6av9T-%KJR?EZ3ccULh4{8=5qL2qjuho^>)!LOBlAgvGpp&MsBsdfyiSWoB*XHSS'
        'v6TFMg*RNELu?p0_A-pDU_3UhUANh4Vnn$P#T5h?tRLgekF)S=Vf1-zh#w=4EMFoQhG(@gBp=}@X?Vd?2;Nv&zH#;1vH?Co5I(iq'
        'k|u8ik&4XDcv-7#@CJ?vbO?vsb{j6x4l<&;Hv^c&^&3GAv#9O?2TNIubrTR48ozv<CL`~=v5vI+a7i(i6wDw@6XT#sWV=}pU;}{3'
        'HP{e{VD#l)$RkXpUJbQ{3uz=iP7YIEz0yf=ynDChc~;bZ`7X?$1M<&lm5uMoI*4hgCrVklRfpv^T|Z^x*syl7Q9_-9sKB{d9>?YO'
        '*Z^SxF~7$S(RGoo2N4hLu@d6I9xK!RA;i)is~`^Uv0=pG9vh+lqlkq)Hb&zP(|qGJ{)qOQO%P5J9wj_RI7K*3I74`x@C4y3;T+*f'
        '!g<04LWA%W;c3D}!ZU<t36}`Z5mpJ$6J8*^NO+0xGGUGIHNq=|R|&5X{*3T-!Z!%tBz%i-nec7GcL;w@_%7iu2!BcV9^rMu+k~5h'
        'f^e7c8R3_NUlD#y_zmHAgx?eXpmD97r^ZaysAi4jtZ_SQY-SCSHFmScv#jxD*7z!Ge4RDE$r|5fjqkI@57cPEtD5hIARPFGLAJWA'
        'L!u19J3O>(H*Tk_m`r5p+`!iyy+^vQgfhGmPO&_`%=L@mH{$pDwPuQXPud>48Tcsw{=WH-&&2cxmBp_b@mNpcqhDpn<-Vz=H!OdP'
        'Z-Ai2?m=SmSm$^V2H4=#6P6PZTNe^DJ<HgAGd>3|!GV{uUfEayvv^Qn4|Eiua}RTVD6<q;k(I!6tp=(;8^r5jeU1H#Y=~7zA9AeR'
        '(TJRyZxHT|kXm%cWB<ebPc6QrAUQU|M%frU+|d%8y8_m+j;iEfTnTKW9eqJd8Tw>8gYyrvVK&Z=km6vE3eLfflJ=liL#odNsZb8u'
        'Wm2M?VgUP3lO|#RL3{?AB6Y$(6}UdePLNJ%Kj0Z`h7>EOxEN=XIBLGj20Rr#S?IC>zM>}vc|wYoV}@pfEs(aMMX|x=N#)R@*kC6~'
        '@6e+7U~{B=Xwi(!k_MvXkn;ZosUcdBlW}&ObWzVUj;lGJU6<H7&B}%Dyi1yui<za!&LS_Qp882=H20S?OMxvSFQlmY*{Ahxyp~z='
        '?3CWaE7|@Sq_lV!S-FC|T<bE0mU&WNw2UgtNz!4>9a`o{k<l`&EVHD|noYEvAeBbTkg^;nz0P>Kg3P?#Wd<$Nq~V$wv`mqjYi7`L'
        'jC5TygO;PD@R}L4Op?}XX3#Q0s;`+r%MsFl#SFW$*Am}m9j>bm>mZ6;qJWe^KsNuc0#fV<h)(w(6Og=0Ce=d;NEuUy1SGH08<T#x'
        'Pe7Cmkbsm?d|=~1EJ#4gBp_OvXzq!A`N;%i0D54097am_6_A3u9)f_H><Gw!nqvgVOlv<2%BLgPXC_-k_9=sXN8t%m7$QnQ^a{qb'
        'ILvB4N~+fcTITxv=m<z2u7_dN3<l`DehSLr3_F2AywGK1h8@R{HMC`h1Vk|bUQDCqwDtpiJE}cf?D8=ILN?P8kRBmBs~K4Y3-Ey!'
        'B_O9^oZ<s5N<dC2Z;_E15)eblcUM60$yH!w2GjOJ#!6MKZ=M8XKv_n?a<U^JXu&nlk$~X!FuSN(sb!W5yMVlqfFLVXb{=^l0RdK6'
        'l?3FR8d1``C;?d_?-VaeK+Y;&s+t!iAZN&5#fuV<MHK~A&C8ozUaFdxx4OJkH80CuUaFdzw=@5dmt|z;oy;<(Eb}BF886Go%)6Oo'
        'L|NuYKr}OGnI!>PCT<in?{%43*34Y*FvFHJ0l@*c)g+trRRsm}@MAxC>YG?CN+_F?CwFz-DDm(D%e9^Z3@G|yRq&}XSv{v}St+n)'
        '?DV|^<(%!c992jj(8q9N$-M@hTa@8b3{PF+o->P=zUVqd{^a``_in7*ym9}*>fH~`^;;XO_g2vN-QP)W2fp)>K0ax3DXlF$KnYr&'
        'gC{8UD6kwn3*vCu?q8k(Ym0H1>&H-0TOJg{v8zs4i~xE@y-Xkp4xNy3rv@K|$;qtPgb&yVo($iBeMeU14fT;}d7UE`KN)I7mW@`Z'
        'c*`G98}29ht0{iG;vQ|s`CM)vMhcn{eJVA+c4O1LdFSE%2e&rN`>Vgbg>-y?l|Q%#MLqD^v(oGY%C>wzi18FEwp?GA;i|BIqwicv'
        '_}iamK0y1A&`$DibR6X37J776Ol?1bTjJVw8(_PIKVRU_=kU`KA3hhi*Z#dAR>hsFSQB@}J+Ur+B{q^m=tHeuBB#=1dim;`uXoQM'
        '`;R`vub+#h&65MUT;CQ$vnBPW?z3Qtq1teL$KaMN^lqM$-4l{^k6RL{>N%yrlESzV;`zueKaN~3)lr4RfhtedDwP|452F-fG7iGt'
        'SdV*sw4@<}z(;grLjZImX#XhdKQPqK<hwQx)yat!h90=}j`37*xaxH$;x>n%!(*Thj~zdtd!!E&!Oa-cT&J^=07E4J9xr=5=9Q{j'
        '<23_nt!j@<oHyPz4mbrpe+k#7Pb`UteSLtk3+7c@hzYAIrV9H1RK7|B?8uXrYd`jIb1!G4^`E6S)Gyoz4T)li*?lX%txl_J`={>q'
        'FRbu>TF>74uz>Yp$nvVpE5KJ;0l(73w|BwN+ph@yx}S38Zl@5Bhh8=RLw6nr>&LHl?l)_N7sFyijN|EPRZNKske;n9DSu+-ZvO@Q'
        'yuhCnemd#7{WnyI5(ptw)^WO)D<o5<L;t0SOu;P&;N_a#06qKeN2>K+_InvL`YZAOQ0u=y1b?Mu&#G?l32Dkcnx*1PQ)|FoW1qV?'
        'xb{DmW@u2G82|t'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
