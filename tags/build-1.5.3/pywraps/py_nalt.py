#<pycode(py_nalt)>
SWI_SPARSE      = 0x1
"""sparse switch ( value table present ) otherwise lowcase present"""
SWI_V32         = 0x2
"""32-bit values in table"""
SWI_J32         = 0x4
"""32-bit jump offsets"""
SWI_VSPLIT      = 0x8
"""value table is split (only for 32-bit values)"""
SWI_DEFAULT     = 0x10
"""default case is present"""
SWI_END_IN_TBL  = 0x20
"""switchend in table (default entry)"""
SWI_JMP_INV     = 0x40
"""jumptable is inversed (last entry is for first entry in values table)"""
SWI_SHIFT_MASK  = 0x180
"""use formula (element*shift + elbase) to find jump targets"""

SWI_ELBASE      = 0x200
"""elbase is present (if not and shift!=0, endof(jumpea) is used)"""
SWI_JSIZE       = 0x400
"""jump offset expansion bit"""

SWI_VSIZE       = 0x800
"""value table element size expansion bit"""

SWI_SEPARATE    = 0x1000
"""do not create an array of individual dwords"""

SWI_SIGNED      = 0x2000
"""jump table entries are signed"""

SWI_CUSTOM      = 0x4000
"""custom jump table - ph.create_switch_xrefs will be called to create code xrefs for the table. it must return 2. custom jump table must be created by the module"""

SWI_EXTENDED    = 0x8000
"""this is switch_info_ex_t"""

SWI2_INDIRECT = 0x0001
"""value table elements are used as indexes into the jump table"""
SWI2_SUBTRACT = 0x0002
"""table values are subtracted from the elbase instead of being addded"""

# --------------------------------------------------------------------------
class switch_info_ex_t(py_clinked_object_t):
    def __init__(self, lnk = None):
        py_clinked_object_t.__init__(self, lnk)

    def _create_clink(self):
        return _idaapi.switch_info_ex_t_create()

    def _del_clink(self, lnk):
        return _idaapi.switch_info_ex_t_destroy(lnk)

    def assign(self, other):
        return _idaapi.switch_info_ex_t_assign(self, other)

    def is_indirect(self):
        return (self.flags & SWI_EXTENDED) != 0 and (self.flags2 & SWI2_INDIRECT) != 0

    def is_subtract(self):
        return (self.flags & SWI_EXTENDED) != 0 and (self.flags2 & SWI2_SUBTRACT) != 0

    def get_jtable_size(self):
        return self.jcases if self.is_indirect() else self.ncases

    def get_lowcase(self):
        return self.ind_lowcase if self.is_indirect() else self.lowcase

    def set_expr(self, r, dt):
        self.regnum = r
        self.regdtyp = dt

    def get_shift(self):
        return (self.flags & SWI_SHIFT_MASK) >> 7

    def set_shift(self, shift):
        self.flags &= ~SWI_SHIFT_MASK
        self.flags |= ((shift & 3) << 7)

    def get_jtable_element_size(self):
        code = self.flags & (SWI_J32|SWI_JSIZE)
        if   code == 0:         return 2
        elif code == SWI_J32:   return 4
        elif code == SWI_JSIZE: return 1
        else:                   return 8

    def set_jtable_element_size(self, size):
        self.flags &= ~(SWI_J32|SWI_JSIZE)
        if size == 4:   self.flags |= SWI_J32
        elif size == 1: self.flags |= SWI_JSIZE
        elif size == 8: self.flags |= SWI_J32|SWI_JSIZE
        elif size != 2: return False
        return True

    def get_vtable_element_size(self):
        code = self.flags & (SWI_V32|SWI_VSIZE)
        if   code == 0:         return 2
        elif code == SWI_V32:   return 4
        elif code == SWI_VSIZE: return 1
        return 8

    def set_vtable_element_size(self, size):
        self.flags &= ~SWI_V32|SWI_VSIZE
        if size == 4:   self.flags |= SWI_V32
        elif size == 1: self.flags |= SWI_VSIZE
        elif size == 8: self.flags |= SWI_V32|SWI_VSIZE
        elif size != 2: return False
        return True

    #
    # Autogenerated
    #
    def __get_regdtyp__(self):
        return _idaapi.switch_info_ex_t_get_regdtyp(self)
    def __set_regdtyp__(self, v):
        _idaapi.switch_info_ex_t_set_regdtyp(self, v)
    def __get_flags2__(self):
        return _idaapi.switch_info_ex_t_get_flags2(self)
    def __set_flags2__(self, v):
        _idaapi.switch_info_ex_t_set_flags2(self, v)
    def __get_jcases__(self):
        return _idaapi.switch_info_ex_t_get_jcases(self)
    def __set_jcases__(self, v):
        _idaapi.switch_info_ex_t_set_jcases(self, v)
    def __get_regnum__(self):
        return _idaapi.switch_info_ex_t_get_regnum(self)
    def __set_regnum__(self, v):
        _idaapi.switch_info_ex_t_set_regnum(self, v)
    def __get_flags__(self):
        return _idaapi.switch_info_ex_t_get_flags(self)
    def __set_flags__(self, v):
        _idaapi.switch_info_ex_t_set_flags(self, v)
    def __get_ncases__(self):
        return _idaapi.switch_info_ex_t_get_ncases(self)
    def __set_ncases__(self, v):
        _idaapi.switch_info_ex_t_set_ncases(self, v)
    def __get_defjump__(self):
        return _idaapi.switch_info_ex_t_get_defjump(self)
    def __set_defjump__(self, v):
        _idaapi.switch_info_ex_t_set_defjump(self, v)
    def __get_jumps__(self):
        return _idaapi.switch_info_ex_t_get_jumps(self)
    def __set_jumps__(self, v):
        _idaapi.switch_info_ex_t_set_jumps(self, v)
    def __get_elbase__(self):
        return _idaapi.switch_info_ex_t_get_elbase(self)
    def __set_elbase__(self, v):
        _idaapi.switch_info_ex_t_set_elbase(self, v)
    def __get_startea__(self):
        return _idaapi.switch_info_ex_t_get_startea(self)
    def __set_startea__(self, v):
        _idaapi.switch_info_ex_t_set_startea(self, v)
    def __get_custom__(self):
        return _idaapi.switch_info_ex_t_get_custom(self)
    def __set_custom__(self, v):
        _idaapi.switch_info_ex_t_set_custom(self, v)
    def __get_ind_lowcase__(self):
        return _idaapi.switch_info_ex_t_get_ind_lowcase(self)
    def __set_ind_lowcase__(self, v):
        _idaapi.switch_info_ex_t_set_ind_lowcase(self, v)
    def __get_values_lowcase__(self):
        return _idaapi.switch_info_ex_t_get_values_lowcase(self)
    def __set_values_lowcase__(self, v):
        _idaapi.switch_info_ex_t_set_values_lowcase(self, v)
    regdtyp = property(__get_regdtyp__, __set_regdtyp__)
    """size of the switch expression register as dtyp"""
    flags2 = property(__get_flags2__, __set_flags2__)
    jcases = property(__get_jcases__, __set_jcases__)
    """number of entries in the jump table (SWI2_INDIRECT)"""
    regnum = property(__get_regnum__, __set_regnum__)
    """the switch expression as a register number"""
    flags = property(__get_flags__, __set_flags__)
    """the switch expression as a register number"""
    ncases = property(__get_ncases__, __set_ncases__)
    """number of cases (excluding default)"""
    defjump = property(__get_defjump__, __set_defjump__)
    """default jump address"""
    jumps = property(__get_jumps__, __set_jumps__)
    """jump table address"""
    elbase = property(__get_elbase__, __set_elbase__)
    """element base"""
    startea = property(__get_startea__, __set_startea__)
    """start of switch idiom"""
    custom = property(__get_custom__, __set_custom__)
    """information for custom tables (filled and used by modules)"""
    ind_lowcase = property(__get_ind_lowcase__, __set_ind_lowcase__)
    values = property(__get_values_lowcase__, __set_values_lowcase__)
    lowcase = property(__get_values_lowcase__, __set_values_lowcase__)

#</pycode(py_nalt)>