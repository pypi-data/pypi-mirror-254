from __future__ import print_function, absolute_import, division
import _supy_driver
import f90wrap.runtime
import logging
import numpy

class Suews_Driver(f90wrap.runtime.FortranModule):
    """
    Module suews_driver
    
    
    Defined at suews_ctrl_driver.fpp lines 10-9858
    
    """
    @f90wrap.runtime.register_class("supy_driver.config")
    class config(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=config)
        
        
        Defined at suews_ctrl_driver.fpp lines 53-57
        
        """
        def __init__(self, handle=None):
            """
            self = Config()
            
            
            Defined at suews_ctrl_driver.fpp lines 53-57
            
            
            Returns
            -------
            this : Config
            	Object to be constructed
            
            
            Automatically generated constructor for config
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_config_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Config
            
            
            Defined at suews_ctrl_driver.fpp lines 53-57
            
            Parameters
            ----------
            this : Config
            	Object to be destructed
            
            
            Automatically generated destructor for config
            """
            if self._alloc:
                _supy_driver.f90wrap_config_finalise(this=self._handle)
        
        @property
        def var1(self):
            """
            Element var1 ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 54
            
            """
            return _supy_driver.f90wrap_config__get__var1(self._handle)
        
        @var1.setter
        def var1(self, var1):
            _supy_driver.f90wrap_config__set__var1(self._handle, var1)
        
        @property
        def var2(self):
            """
            Element var2 ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 55
            
            """
            return _supy_driver.f90wrap_config__get__var2(self._handle)
        
        @var2.setter
        def var2(self, var2):
            _supy_driver.f90wrap_config__set__var2(self._handle, var2)
        
        def __str__(self):
            ret = ['<config>{\n']
            ret.append('    var1 : ')
            ret.append(repr(self.var1))
            ret.append(',\n    var2 : ')
            ret.append(repr(self.var2))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.array_m")
    class array_m(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=array_m)
        
        
        Defined at suews_ctrl_driver.fpp lines 59-63
        
        """
        def __init__(self, handle=None):
            """
            self = Array_M()
            
            
            Defined at suews_ctrl_driver.fpp lines 59-63
            
            
            Returns
            -------
            this : Array_M
            	Object to be constructed
            
            
            Automatically generated constructor for array_m
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_array_m_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Array_M
            
            
            Defined at suews_ctrl_driver.fpp lines 59-63
            
            Parameters
            ----------
            this : Array_M
            	Object to be destructed
            
            
            Automatically generated destructor for array_m
            """
            if self._alloc:
                _supy_driver.f90wrap_array_m_finalise(this=self._handle)
        
        @property
        def var1(self):
            """
            Element var1 ftype=integer pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 60
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_array_m__array__var1(self._handle)
            if array_handle in self._arrays:
                var1 = self._arrays[array_handle]
            else:
                var1 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_array_m__array__var1)
                self._arrays[array_handle] = var1
            return var1
        
        @var1.setter
        def var1(self, var1):
            self.var1[...] = var1
        
        @property
        def var2(self):
            """
            Element var2 ftype=integer pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 61
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_array_m__array__var2(self._handle)
            if array_handle in self._arrays:
                var2 = self._arrays[array_handle]
            else:
                var2 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_array_m__array__var2)
                self._arrays[array_handle] = var2
            return var2
        
        @var2.setter
        def var2(self, var2):
            self.var2[...] = var2
        
        def __str__(self):
            ret = ['<array_m>{\n']
            ret.append('    var1 : ')
            ret.append(repr(self.var1))
            ret.append(',\n    var2 : ')
            ret.append(repr(self.var2))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.output_block")
    class output_block(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=output_block)
        
        
        Defined at suews_ctrl_driver.fpp lines 65-78
        
        """
        def __init__(self, handle=None):
            """
            self = Output_Block()
            
            
            Defined at suews_ctrl_driver.fpp lines 65-78
            
            
            Returns
            -------
            this : Output_Block
            	Object to be constructed
            
            
            Automatically generated constructor for output_block
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_output_block_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Output_Block
            
            
            Defined at suews_ctrl_driver.fpp lines 65-78
            
            Parameters
            ----------
            this : Output_Block
            	Object to be destructed
            
            
            Automatically generated destructor for output_block
            """
            if self._alloc:
                _supy_driver.f90wrap_output_block_finalise(this=self._handle)
        
        @property
        def dataoutblocksuews(self):
            """
            Element dataoutblocksuews ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 66
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblocksuews(self._handle)
            if array_handle in self._arrays:
                dataoutblocksuews = self._arrays[array_handle]
            else:
                dataoutblocksuews = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblocksuews)
                self._arrays[array_handle] = dataoutblocksuews
            return dataoutblocksuews
        
        @dataoutblocksuews.setter
        def dataoutblocksuews(self, dataoutblocksuews):
            self.dataoutblocksuews[...] = dataoutblocksuews
        
        @property
        def dataoutblocksnow(self):
            """
            Element dataoutblocksnow ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 67
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblocksnow(self._handle)
            if array_handle in self._arrays:
                dataoutblocksnow = self._arrays[array_handle]
            else:
                dataoutblocksnow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblocksnow)
                self._arrays[array_handle] = dataoutblocksnow
            return dataoutblocksnow
        
        @dataoutblocksnow.setter
        def dataoutblocksnow(self, dataoutblocksnow):
            self.dataoutblocksnow[...] = dataoutblocksnow
        
        @property
        def dataoutblockestm(self):
            """
            Element dataoutblockestm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 68
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockestm(self._handle)
            if array_handle in self._arrays:
                dataoutblockestm = self._arrays[array_handle]
            else:
                dataoutblockestm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockestm)
                self._arrays[array_handle] = dataoutblockestm
            return dataoutblockestm
        
        @dataoutblockestm.setter
        def dataoutblockestm(self, dataoutblockestm):
            self.dataoutblockestm[...] = dataoutblockestm
        
        @property
        def dataoutblockestmext(self):
            """
            Element dataoutblockestmext ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 69
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockestmext(self._handle)
            if array_handle in self._arrays:
                dataoutblockestmext = self._arrays[array_handle]
            else:
                dataoutblockestmext = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockestmext)
                self._arrays[array_handle] = dataoutblockestmext
            return dataoutblockestmext
        
        @dataoutblockestmext.setter
        def dataoutblockestmext(self, dataoutblockestmext):
            self.dataoutblockestmext[...] = dataoutblockestmext
        
        @property
        def dataoutblockrsl(self):
            """
            Element dataoutblockrsl ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 70
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockrsl(self._handle)
            if array_handle in self._arrays:
                dataoutblockrsl = self._arrays[array_handle]
            else:
                dataoutblockrsl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockrsl)
                self._arrays[array_handle] = dataoutblockrsl
            return dataoutblockrsl
        
        @dataoutblockrsl.setter
        def dataoutblockrsl(self, dataoutblockrsl):
            self.dataoutblockrsl[...] = dataoutblockrsl
        
        @property
        def dataoutblockbeers(self):
            """
            Element dataoutblockbeers ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 71
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockbeers(self._handle)
            if array_handle in self._arrays:
                dataoutblockbeers = self._arrays[array_handle]
            else:
                dataoutblockbeers = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockbeers)
                self._arrays[array_handle] = dataoutblockbeers
            return dataoutblockbeers
        
        @dataoutblockbeers.setter
        def dataoutblockbeers(self, dataoutblockbeers):
            self.dataoutblockbeers[...] = dataoutblockbeers
        
        @property
        def dataoutblockdebug(self):
            """
            Element dataoutblockdebug ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 72
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockdebug(self._handle)
            if array_handle in self._arrays:
                dataoutblockdebug = self._arrays[array_handle]
            else:
                dataoutblockdebug = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockdebug)
                self._arrays[array_handle] = dataoutblockdebug
            return dataoutblockdebug
        
        @dataoutblockdebug.setter
        def dataoutblockdebug(self, dataoutblockdebug):
            self.dataoutblockdebug[...] = dataoutblockdebug
        
        @property
        def dataoutblockspartacus(self):
            """
            Element dataoutblockspartacus ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 73
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockspartacus(self._handle)
            if array_handle in self._arrays:
                dataoutblockspartacus = self._arrays[array_handle]
            else:
                dataoutblockspartacus = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockspartacus)
                self._arrays[array_handle] = dataoutblockspartacus
            return dataoutblockspartacus
        
        @dataoutblockspartacus.setter
        def dataoutblockspartacus(self, dataoutblockspartacus):
            self.dataoutblockspartacus[...] = dataoutblockspartacus
        
        @property
        def dataoutblockdailystate(self):
            """
            Element dataoutblockdailystate ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 74
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockdailystate(self._handle)
            if array_handle in self._arrays:
                dataoutblockdailystate = self._arrays[array_handle]
            else:
                dataoutblockdailystate = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockdailystate)
                self._arrays[array_handle] = dataoutblockdailystate
            return dataoutblockdailystate
        
        @dataoutblockdailystate.setter
        def dataoutblockdailystate(self, dataoutblockdailystate):
            self.dataoutblockdailystate[...] = dataoutblockdailystate
        
        def __str__(self):
            ret = ['<output_block>{\n']
            ret.append('    dataoutblocksuews : ')
            ret.append(repr(self.dataoutblocksuews))
            ret.append(',\n    dataoutblocksnow : ')
            ret.append(repr(self.dataoutblocksnow))
            ret.append(',\n    dataoutblockestm : ')
            ret.append(repr(self.dataoutblockestm))
            ret.append(',\n    dataoutblockestmext : ')
            ret.append(repr(self.dataoutblockestmext))
            ret.append(',\n    dataoutblockrsl : ')
            ret.append(repr(self.dataoutblockrsl))
            ret.append(',\n    dataoutblockbeers : ')
            ret.append(repr(self.dataoutblockbeers))
            ret.append(',\n    dataoutblockdebug : ')
            ret.append(repr(self.dataoutblockdebug))
            ret.append(',\n    dataoutblockspartacus : ')
            ret.append(repr(self.dataoutblockspartacus))
            ret.append(',\n    dataoutblockdailystate : ')
            ret.append(repr(self.dataoutblockdailystate))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.output_line")
    class output_line(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=output_line)
        
        
        Defined at suews_ctrl_driver.fpp lines 80-90
        
        """
        def __init__(self, handle=None):
            """
            self = Output_Line()
            
            
            Defined at suews_ctrl_driver.fpp lines 80-90
            
            
            Returns
            -------
            this : Output_Line
            	Object to be constructed
            
            
            Automatically generated constructor for output_line
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_output_line_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Output_Line
            
            
            Defined at suews_ctrl_driver.fpp lines 80-90
            
            Parameters
            ----------
            this : Output_Line
            	Object to be destructed
            
            
            Automatically generated destructor for output_line
            """
            if self._alloc:
                _supy_driver.f90wrap_output_line_finalise(this=self._handle)
        
        @property
        def datetimeline(self):
            """
            Element datetimeline ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 81
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__datetimeline(self._handle)
            if array_handle in self._arrays:
                datetimeline = self._arrays[array_handle]
            else:
                datetimeline = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__datetimeline)
                self._arrays[array_handle] = datetimeline
            return datetimeline
        
        @datetimeline.setter
        def datetimeline(self, datetimeline):
            self.datetimeline[...] = datetimeline
        
        @property
        def dataoutlinesuews(self):
            """
            Element dataoutlinesuews ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 82
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinesuews(self._handle)
            if array_handle in self._arrays:
                dataoutlinesuews = self._arrays[array_handle]
            else:
                dataoutlinesuews = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinesuews)
                self._arrays[array_handle] = dataoutlinesuews
            return dataoutlinesuews
        
        @dataoutlinesuews.setter
        def dataoutlinesuews(self, dataoutlinesuews):
            self.dataoutlinesuews[...] = dataoutlinesuews
        
        @property
        def dataoutlinesnow(self):
            """
            Element dataoutlinesnow ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 83
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinesnow(self._handle)
            if array_handle in self._arrays:
                dataoutlinesnow = self._arrays[array_handle]
            else:
                dataoutlinesnow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinesnow)
                self._arrays[array_handle] = dataoutlinesnow
            return dataoutlinesnow
        
        @dataoutlinesnow.setter
        def dataoutlinesnow(self, dataoutlinesnow):
            self.dataoutlinesnow[...] = dataoutlinesnow
        
        @property
        def dataoutlineestm(self):
            """
            Element dataoutlineestm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 84
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlineestm(self._handle)
            if array_handle in self._arrays:
                dataoutlineestm = self._arrays[array_handle]
            else:
                dataoutlineestm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlineestm)
                self._arrays[array_handle] = dataoutlineestm
            return dataoutlineestm
        
        @dataoutlineestm.setter
        def dataoutlineestm(self, dataoutlineestm):
            self.dataoutlineestm[...] = dataoutlineestm
        
        @property
        def dataoutlineestmext(self):
            """
            Element dataoutlineestmext ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 85
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlineestmext(self._handle)
            if array_handle in self._arrays:
                dataoutlineestmext = self._arrays[array_handle]
            else:
                dataoutlineestmext = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlineestmext)
                self._arrays[array_handle] = dataoutlineestmext
            return dataoutlineestmext
        
        @dataoutlineestmext.setter
        def dataoutlineestmext(self, dataoutlineestmext):
            self.dataoutlineestmext[...] = dataoutlineestmext
        
        @property
        def dataoutlinersl(self):
            """
            Element dataoutlinersl ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 86
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinersl(self._handle)
            if array_handle in self._arrays:
                dataoutlinersl = self._arrays[array_handle]
            else:
                dataoutlinersl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinersl)
                self._arrays[array_handle] = dataoutlinersl
            return dataoutlinersl
        
        @dataoutlinersl.setter
        def dataoutlinersl(self, dataoutlinersl):
            self.dataoutlinersl[...] = dataoutlinersl
        
        @property
        def dataoutlinebeers(self):
            """
            Element dataoutlinebeers ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 87
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinebeers(self._handle)
            if array_handle in self._arrays:
                dataoutlinebeers = self._arrays[array_handle]
            else:
                dataoutlinebeers = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinebeers)
                self._arrays[array_handle] = dataoutlinebeers
            return dataoutlinebeers
        
        @dataoutlinebeers.setter
        def dataoutlinebeers(self, dataoutlinebeers):
            self.dataoutlinebeers[...] = dataoutlinebeers
        
        @property
        def dataoutlinedebug(self):
            """
            Element dataoutlinedebug ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 88
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinedebug(self._handle)
            if array_handle in self._arrays:
                dataoutlinedebug = self._arrays[array_handle]
            else:
                dataoutlinedebug = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinedebug)
                self._arrays[array_handle] = dataoutlinedebug
            return dataoutlinedebug
        
        @dataoutlinedebug.setter
        def dataoutlinedebug(self, dataoutlinedebug):
            self.dataoutlinedebug[...] = dataoutlinedebug
        
        @property
        def dataoutlinespartacus(self):
            """
            Element dataoutlinespartacus ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 89
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinespartacus(self._handle)
            if array_handle in self._arrays:
                dataoutlinespartacus = self._arrays[array_handle]
            else:
                dataoutlinespartacus = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinespartacus)
                self._arrays[array_handle] = dataoutlinespartacus
            return dataoutlinespartacus
        
        @dataoutlinespartacus.setter
        def dataoutlinespartacus(self, dataoutlinespartacus):
            self.dataoutlinespartacus[...] = dataoutlinespartacus
        
        @property
        def dataoutlinedailystate(self):
            """
            Element dataoutlinedailystate ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 90
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinedailystate(self._handle)
            if array_handle in self._arrays:
                dataoutlinedailystate = self._arrays[array_handle]
            else:
                dataoutlinedailystate = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinedailystate)
                self._arrays[array_handle] = dataoutlinedailystate
            return dataoutlinedailystate
        
        @dataoutlinedailystate.setter
        def dataoutlinedailystate(self, dataoutlinedailystate):
            self.dataoutlinedailystate[...] = dataoutlinedailystate
        
        def __str__(self):
            ret = ['<output_line>{\n']
            ret.append('    datetimeline : ')
            ret.append(repr(self.datetimeline))
            ret.append(',\n    dataoutlinesuews : ')
            ret.append(repr(self.dataoutlinesuews))
            ret.append(',\n    dataoutlinesnow : ')
            ret.append(repr(self.dataoutlinesnow))
            ret.append(',\n    dataoutlineestm : ')
            ret.append(repr(self.dataoutlineestm))
            ret.append(',\n    dataoutlineestmext : ')
            ret.append(repr(self.dataoutlineestmext))
            ret.append(',\n    dataoutlinersl : ')
            ret.append(repr(self.dataoutlinersl))
            ret.append(',\n    dataoutlinebeers : ')
            ret.append(repr(self.dataoutlinebeers))
            ret.append(',\n    dataoutlinedebug : ')
            ret.append(repr(self.dataoutlinedebug))
            ret.append(',\n    dataoutlinespartacus : ')
            ret.append(repr(self.dataoutlinespartacus))
            ret.append(',\n    dataoutlinedailystate : ')
            ret.append(repr(self.dataoutlinedailystate))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.METHOD_PRM")
    class METHOD_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=method_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 93-107
        
        """
        def __init__(self, handle=None):
            """
            self = Method_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 93-107
            
            
            Returns
            -------
            this : Method_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for method_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_method_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Method_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 93-107
            
            Parameters
            ----------
            this : Method_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for method_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_method_prm_finalise(this=self._handle)
        
        @property
        def diagmethod(self):
            """
            Element diagmethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 94
            
            """
            return _supy_driver.f90wrap_method_prm__get__diagmethod(self._handle)
        
        @diagmethod.setter
        def diagmethod(self, diagmethod):
            _supy_driver.f90wrap_method_prm__set__diagmethod(self._handle, diagmethod)
        
        @property
        def emissionsmethod(self):
            """
            Element emissionsmethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 95
            
            """
            return _supy_driver.f90wrap_method_prm__get__emissionsmethod(self._handle)
        
        @emissionsmethod.setter
        def emissionsmethod(self, emissionsmethod):
            _supy_driver.f90wrap_method_prm__set__emissionsmethod(self._handle, \
                emissionsmethod)
        
        @property
        def roughlenheatmethod(self):
            """
            Element roughlenheatmethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 96
            
            """
            return _supy_driver.f90wrap_method_prm__get__roughlenheatmethod(self._handle)
        
        @roughlenheatmethod.setter
        def roughlenheatmethod(self, roughlenheatmethod):
            _supy_driver.f90wrap_method_prm__set__roughlenheatmethod(self._handle, \
                roughlenheatmethod)
        
        @property
        def roughlenmommethod(self):
            """
            Element roughlenmommethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 97
            
            """
            return _supy_driver.f90wrap_method_prm__get__roughlenmommethod(self._handle)
        
        @roughlenmommethod.setter
        def roughlenmommethod(self, roughlenmommethod):
            _supy_driver.f90wrap_method_prm__set__roughlenmommethod(self._handle, \
                roughlenmommethod)
        
        @property
        def faimethod(self):
            """
            Element faimethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 98
            
            """
            return _supy_driver.f90wrap_method_prm__get__faimethod(self._handle)
        
        @faimethod.setter
        def faimethod(self, faimethod):
            _supy_driver.f90wrap_method_prm__set__faimethod(self._handle, faimethod)
        
        @property
        def smdmethod(self):
            """
            Element smdmethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 99
            
            """
            return _supy_driver.f90wrap_method_prm__get__smdmethod(self._handle)
        
        @smdmethod.setter
        def smdmethod(self, smdmethod):
            _supy_driver.f90wrap_method_prm__set__smdmethod(self._handle, smdmethod)
        
        @property
        def waterusemethod(self):
            """
            Element waterusemethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 100
            
            """
            return _supy_driver.f90wrap_method_prm__get__waterusemethod(self._handle)
        
        @waterusemethod.setter
        def waterusemethod(self, waterusemethod):
            _supy_driver.f90wrap_method_prm__set__waterusemethod(self._handle, \
                waterusemethod)
        
        @property
        def netradiationmethod(self):
            """
            Element netradiationmethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 101
            
            """
            return _supy_driver.f90wrap_method_prm__get__netradiationmethod(self._handle)
        
        @netradiationmethod.setter
        def netradiationmethod(self, netradiationmethod):
            _supy_driver.f90wrap_method_prm__set__netradiationmethod(self._handle, \
                netradiationmethod)
        
        @property
        def stabilitymethod(self):
            """
            Element stabilitymethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 102
            
            """
            return _supy_driver.f90wrap_method_prm__get__stabilitymethod(self._handle)
        
        @stabilitymethod.setter
        def stabilitymethod(self, stabilitymethod):
            _supy_driver.f90wrap_method_prm__set__stabilitymethod(self._handle, \
                stabilitymethod)
        
        @property
        def storageheatmethod(self):
            """
            Element storageheatmethod ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 103
            
            """
            return _supy_driver.f90wrap_method_prm__get__storageheatmethod(self._handle)
        
        @storageheatmethod.setter
        def storageheatmethod(self, storageheatmethod):
            _supy_driver.f90wrap_method_prm__set__storageheatmethod(self._handle, \
                storageheatmethod)
        
        @property
        def diagnose(self):
            """
            Element diagnose ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 104
            
            """
            return _supy_driver.f90wrap_method_prm__get__diagnose(self._handle)
        
        @diagnose.setter
        def diagnose(self, diagnose):
            _supy_driver.f90wrap_method_prm__set__diagnose(self._handle, diagnose)
        
        @property
        def snowuse(self):
            """
            Element snowuse ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 105
            
            """
            return _supy_driver.f90wrap_method_prm__get__snowuse(self._handle)
        
        @snowuse.setter
        def snowuse(self, snowuse):
            _supy_driver.f90wrap_method_prm__set__snowuse(self._handle, snowuse)
        
        @property
        def use_sw_direct_albedo(self):
            """
            Element use_sw_direct_albedo ftype=logical pytype=bool
            
            
            Defined at suews_ctrl_driver.fpp line 106
            
            """
            return _supy_driver.f90wrap_method_prm__get__use_sw_direct_albedo(self._handle)
        
        @use_sw_direct_albedo.setter
        def use_sw_direct_albedo(self, use_sw_direct_albedo):
            _supy_driver.f90wrap_method_prm__set__use_sw_direct_albedo(self._handle, \
                use_sw_direct_albedo)
        
        @property
        def ohmincqf(self):
            """
            Element ohmincqf ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 107
            
            """
            return _supy_driver.f90wrap_method_prm__get__ohmincqf(self._handle)
        
        @ohmincqf.setter
        def ohmincqf(self, ohmincqf):
            _supy_driver.f90wrap_method_prm__set__ohmincqf(self._handle, ohmincqf)
        
        def __str__(self):
            ret = ['<method_prm>{\n']
            ret.append('    diagmethod : ')
            ret.append(repr(self.diagmethod))
            ret.append(',\n    emissionsmethod : ')
            ret.append(repr(self.emissionsmethod))
            ret.append(',\n    roughlenheatmethod : ')
            ret.append(repr(self.roughlenheatmethod))
            ret.append(',\n    roughlenmommethod : ')
            ret.append(repr(self.roughlenmommethod))
            ret.append(',\n    faimethod : ')
            ret.append(repr(self.faimethod))
            ret.append(',\n    smdmethod : ')
            ret.append(repr(self.smdmethod))
            ret.append(',\n    waterusemethod : ')
            ret.append(repr(self.waterusemethod))
            ret.append(',\n    netradiationmethod : ')
            ret.append(repr(self.netradiationmethod))
            ret.append(',\n    stabilitymethod : ')
            ret.append(repr(self.stabilitymethod))
            ret.append(',\n    storageheatmethod : ')
            ret.append(repr(self.storageheatmethod))
            ret.append(',\n    diagnose : ')
            ret.append(repr(self.diagnose))
            ret.append(',\n    snowuse : ')
            ret.append(repr(self.snowuse))
            ret.append(',\n    use_sw_direct_albedo : ')
            ret.append(repr(self.use_sw_direct_albedo))
            ret.append(',\n    ohmincqf : ')
            ret.append(repr(self.ohmincqf))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SURF_STORE_PRM")
    class SURF_STORE_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=surf_store_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 109-115
        
        """
        def __init__(self, handle=None):
            """
            self = Surf_Store_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 109-115
            
            
            Returns
            -------
            this : Surf_Store_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for surf_store_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_surf_store_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Surf_Store_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 109-115
            
            Parameters
            ----------
            this : Surf_Store_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for surf_store_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_surf_store_prm_finalise(this=self._handle)
        
        @property
        def store_min(self):
            """
            Element store_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 110
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__store_min(self._handle)
        
        @store_min.setter
        def store_min(self, store_min):
            _supy_driver.f90wrap_surf_store_prm__set__store_min(self._handle, store_min)
        
        @property
        def store_max(self):
            """
            Element store_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 111
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__store_max(self._handle)
        
        @store_max.setter
        def store_max(self, store_max):
            _supy_driver.f90wrap_surf_store_prm__set__store_max(self._handle, store_max)
        
        @property
        def store_cap(self):
            """
            Element store_cap ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 112
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__store_cap(self._handle)
        
        @store_cap.setter
        def store_cap(self, store_cap):
            _supy_driver.f90wrap_surf_store_prm__set__store_cap(self._handle, store_cap)
        
        @property
        def drain_eq(self):
            """
            Element drain_eq ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 113
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__drain_eq(self._handle)
        
        @drain_eq.setter
        def drain_eq(self, drain_eq):
            _supy_driver.f90wrap_surf_store_prm__set__drain_eq(self._handle, drain_eq)
        
        @property
        def drain_coef_1(self):
            """
            Element drain_coef_1 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 114
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__drain_coef_1(self._handle)
        
        @drain_coef_1.setter
        def drain_coef_1(self, drain_coef_1):
            _supy_driver.f90wrap_surf_store_prm__set__drain_coef_1(self._handle, \
                drain_coef_1)
        
        @property
        def drain_coef_2(self):
            """
            Element drain_coef_2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 115
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__drain_coef_2(self._handle)
        
        @drain_coef_2.setter
        def drain_coef_2(self, drain_coef_2):
            _supy_driver.f90wrap_surf_store_prm__set__drain_coef_2(self._handle, \
                drain_coef_2)
        
        def __str__(self):
            ret = ['<surf_store_prm>{\n']
            ret.append('    store_min : ')
            ret.append(repr(self.store_min))
            ret.append(',\n    store_max : ')
            ret.append(repr(self.store_max))
            ret.append(',\n    store_cap : ')
            ret.append(repr(self.store_cap))
            ret.append(',\n    drain_eq : ')
            ret.append(repr(self.drain_eq))
            ret.append(',\n    drain_coef_1 : ')
            ret.append(repr(self.drain_coef_1))
            ret.append(',\n    drain_coef_2 : ')
            ret.append(repr(self.drain_coef_2))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.WATER_DIST_PRM")
    class WATER_DIST_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=water_dist_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 117-125
        
        """
        def __init__(self, handle=None):
            """
            self = Water_Dist_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 117-125
            
            
            Returns
            -------
            this : Water_Dist_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for water_dist_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_water_dist_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 117-125
            
            Parameters
            ----------
            this : Water_Dist_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for water_dist_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_water_dist_prm_finalise(this=self._handle)
        
        @property
        def to_paved(self):
            """
            Element to_paved ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 118
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_paved(self._handle)
        
        @to_paved.setter
        def to_paved(self, to_paved):
            _supy_driver.f90wrap_water_dist_prm__set__to_paved(self._handle, to_paved)
        
        @property
        def to_bldg(self):
            """
            Element to_bldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 119
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_bldg(self._handle)
        
        @to_bldg.setter
        def to_bldg(self, to_bldg):
            _supy_driver.f90wrap_water_dist_prm__set__to_bldg(self._handle, to_bldg)
        
        @property
        def to_evetr(self):
            """
            Element to_evetr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 120
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_evetr(self._handle)
        
        @to_evetr.setter
        def to_evetr(self, to_evetr):
            _supy_driver.f90wrap_water_dist_prm__set__to_evetr(self._handle, to_evetr)
        
        @property
        def to_dectr(self):
            """
            Element to_dectr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 121
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_dectr(self._handle)
        
        @to_dectr.setter
        def to_dectr(self, to_dectr):
            _supy_driver.f90wrap_water_dist_prm__set__to_dectr(self._handle, to_dectr)
        
        @property
        def to_grass(self):
            """
            Element to_grass ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 122
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_grass(self._handle)
        
        @to_grass.setter
        def to_grass(self, to_grass):
            _supy_driver.f90wrap_water_dist_prm__set__to_grass(self._handle, to_grass)
        
        @property
        def to_bsoil(self):
            """
            Element to_bsoil ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 123
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_bsoil(self._handle)
        
        @to_bsoil.setter
        def to_bsoil(self, to_bsoil):
            _supy_driver.f90wrap_water_dist_prm__set__to_bsoil(self._handle, to_bsoil)
        
        @property
        def to_water(self):
            """
            Element to_water ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 124
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_water(self._handle)
        
        @to_water.setter
        def to_water(self, to_water):
            _supy_driver.f90wrap_water_dist_prm__set__to_water(self._handle, to_water)
        
        @property
        def to_soilstore(self):
            """
            Element to_soilstore ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 125
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_soilstore(self._handle)
        
        @to_soilstore.setter
        def to_soilstore(self, to_soilstore):
            _supy_driver.f90wrap_water_dist_prm__set__to_soilstore(self._handle, \
                to_soilstore)
        
        def __str__(self):
            ret = ['<water_dist_prm>{\n']
            ret.append('    to_paved : ')
            ret.append(repr(self.to_paved))
            ret.append(',\n    to_bldg : ')
            ret.append(repr(self.to_bldg))
            ret.append(',\n    to_evetr : ')
            ret.append(repr(self.to_evetr))
            ret.append(',\n    to_dectr : ')
            ret.append(repr(self.to_dectr))
            ret.append(',\n    to_grass : ')
            ret.append(repr(self.to_grass))
            ret.append(',\n    to_bsoil : ')
            ret.append(repr(self.to_bsoil))
            ret.append(',\n    to_water : ')
            ret.append(repr(self.to_water))
            ret.append(',\n    to_soilstore : ')
            ret.append(repr(self.to_soilstore))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.bioCO2_PRM")
    class bioCO2_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=bioco2_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 127-135
        
        """
        def __init__(self, handle=None):
            """
            self = Bioco2_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 127-135
            
            
            Returns
            -------
            this : Bioco2_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for bioco2_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_bioco2_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Bioco2_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 127-135
            
            Parameters
            ----------
            this : Bioco2_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for bioco2_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_bioco2_prm_finalise(this=self._handle)
        
        @property
        def beta_bioco2(self):
            """
            Element beta_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 128
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__beta_bioco2(self._handle)
        
        @beta_bioco2.setter
        def beta_bioco2(self, beta_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__beta_bioco2(self._handle, beta_bioco2)
        
        @property
        def beta_enh_bioco2(self):
            """
            Element beta_enh_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 129
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__beta_enh_bioco2(self._handle)
        
        @beta_enh_bioco2.setter
        def beta_enh_bioco2(self, beta_enh_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__beta_enh_bioco2(self._handle, \
                beta_enh_bioco2)
        
        @property
        def alpha_bioco2(self):
            """
            Element alpha_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 130
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__alpha_bioco2(self._handle)
        
        @alpha_bioco2.setter
        def alpha_bioco2(self, alpha_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__alpha_bioco2(self._handle, alpha_bioco2)
        
        @property
        def alpha_enh_bioco2(self):
            """
            Element alpha_enh_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 131
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__alpha_enh_bioco2(self._handle)
        
        @alpha_enh_bioco2.setter
        def alpha_enh_bioco2(self, alpha_enh_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__alpha_enh_bioco2(self._handle, \
                alpha_enh_bioco2)
        
        @property
        def resp_a(self):
            """
            Element resp_a ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 132
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__resp_a(self._handle)
        
        @resp_a.setter
        def resp_a(self, resp_a):
            _supy_driver.f90wrap_bioco2_prm__set__resp_a(self._handle, resp_a)
        
        @property
        def resp_b(self):
            """
            Element resp_b ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 133
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__resp_b(self._handle)
        
        @resp_b.setter
        def resp_b(self, resp_b):
            _supy_driver.f90wrap_bioco2_prm__set__resp_b(self._handle, resp_b)
        
        @property
        def theta_bioco2(self):
            """
            Element theta_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 134
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__theta_bioco2(self._handle)
        
        @theta_bioco2.setter
        def theta_bioco2(self, theta_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__theta_bioco2(self._handle, theta_bioco2)
        
        @property
        def min_res_bioco2(self):
            """
            Element min_res_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 135
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__min_res_bioco2(self._handle)
        
        @min_res_bioco2.setter
        def min_res_bioco2(self, min_res_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__min_res_bioco2(self._handle, \
                min_res_bioco2)
        
        def __str__(self):
            ret = ['<bioco2_prm>{\n']
            ret.append('    beta_bioco2 : ')
            ret.append(repr(self.beta_bioco2))
            ret.append(',\n    beta_enh_bioco2 : ')
            ret.append(repr(self.beta_enh_bioco2))
            ret.append(',\n    alpha_bioco2 : ')
            ret.append(repr(self.alpha_bioco2))
            ret.append(',\n    alpha_enh_bioco2 : ')
            ret.append(repr(self.alpha_enh_bioco2))
            ret.append(',\n    resp_a : ')
            ret.append(repr(self.resp_a))
            ret.append(',\n    resp_b : ')
            ret.append(repr(self.resp_b))
            ret.append(',\n    theta_bioco2 : ')
            ret.append(repr(self.theta_bioco2))
            ret.append(',\n    min_res_bioco2 : ')
            ret.append(repr(self.min_res_bioco2))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.CONDUCTANCE_PRM")
    class CONDUCTANCE_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=conductance_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 137-149
        
        """
        def __init__(self, handle=None):
            """
            self = Conductance_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 137-149
            
            
            Returns
            -------
            this : Conductance_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for conductance_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_conductance_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Conductance_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 137-149
            
            Parameters
            ----------
            this : Conductance_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for conductance_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_conductance_prm_finalise(this=self._handle)
        
        @property
        def g_max(self):
            """
            Element g_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 138
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_max(self._handle)
        
        @g_max.setter
        def g_max(self, g_max):
            _supy_driver.f90wrap_conductance_prm__set__g_max(self._handle, g_max)
        
        @property
        def g_k(self):
            """
            Element g_k ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 139
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_k(self._handle)
        
        @g_k.setter
        def g_k(self, g_k):
            _supy_driver.f90wrap_conductance_prm__set__g_k(self._handle, g_k)
        
        @property
        def g_q_base(self):
            """
            Element g_q_base ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 140
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_q_base(self._handle)
        
        @g_q_base.setter
        def g_q_base(self, g_q_base):
            _supy_driver.f90wrap_conductance_prm__set__g_q_base(self._handle, g_q_base)
        
        @property
        def g_q_shape(self):
            """
            Element g_q_shape ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 141
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_q_shape(self._handle)
        
        @g_q_shape.setter
        def g_q_shape(self, g_q_shape):
            _supy_driver.f90wrap_conductance_prm__set__g_q_shape(self._handle, g_q_shape)
        
        @property
        def g_t(self):
            """
            Element g_t ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 142
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_t(self._handle)
        
        @g_t.setter
        def g_t(self, g_t):
            _supy_driver.f90wrap_conductance_prm__set__g_t(self._handle, g_t)
        
        @property
        def g_sm(self):
            """
            Element g_sm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 143
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_sm(self._handle)
        
        @g_sm.setter
        def g_sm(self, g_sm):
            _supy_driver.f90wrap_conductance_prm__set__g_sm(self._handle, g_sm)
        
        @property
        def kmax(self):
            """
            Element kmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 144
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__kmax(self._handle)
        
        @kmax.setter
        def kmax(self, kmax):
            _supy_driver.f90wrap_conductance_prm__set__kmax(self._handle, kmax)
        
        @property
        def gsmodel(self):
            """
            Element gsmodel ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 145
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__gsmodel(self._handle)
        
        @gsmodel.setter
        def gsmodel(self, gsmodel):
            _supy_driver.f90wrap_conductance_prm__set__gsmodel(self._handle, gsmodel)
        
        @property
        def s1(self):
            """
            Element s1 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 146
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__s1(self._handle)
        
        @s1.setter
        def s1(self, s1):
            _supy_driver.f90wrap_conductance_prm__set__s1(self._handle, s1)
        
        @property
        def s2(self):
            """
            Element s2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 147
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__s2(self._handle)
        
        @s2.setter
        def s2(self, s2):
            _supy_driver.f90wrap_conductance_prm__set__s2(self._handle, s2)
        
        @property
        def th(self):
            """
            Element th ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 148
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__th(self._handle)
        
        @th.setter
        def th(self, th):
            _supy_driver.f90wrap_conductance_prm__set__th(self._handle, th)
        
        @property
        def tl(self):
            """
            Element tl ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 149
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__tl(self._handle)
        
        @tl.setter
        def tl(self, tl):
            _supy_driver.f90wrap_conductance_prm__set__tl(self._handle, tl)
        
        def __str__(self):
            ret = ['<conductance_prm>{\n']
            ret.append('    g_max : ')
            ret.append(repr(self.g_max))
            ret.append(',\n    g_k : ')
            ret.append(repr(self.g_k))
            ret.append(',\n    g_q_base : ')
            ret.append(repr(self.g_q_base))
            ret.append(',\n    g_q_shape : ')
            ret.append(repr(self.g_q_shape))
            ret.append(',\n    g_t : ')
            ret.append(repr(self.g_t))
            ret.append(',\n    g_sm : ')
            ret.append(repr(self.g_sm))
            ret.append(',\n    kmax : ')
            ret.append(repr(self.kmax))
            ret.append(',\n    gsmodel : ')
            ret.append(repr(self.gsmodel))
            ret.append(',\n    s1 : ')
            ret.append(repr(self.s1))
            ret.append(',\n    s2 : ')
            ret.append(repr(self.s2))
            ret.append(',\n    th : ')
            ret.append(repr(self.th))
            ret.append(',\n    tl : ')
            ret.append(repr(self.tl))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LAI_PRM")
    class LAI_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lai_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 151-159
        
        """
        def __init__(self, handle=None):
            """
            self = Lai_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 151-159
            
            
            Returns
            -------
            this : Lai_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lai_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lai_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lai_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 151-159
            
            Parameters
            ----------
            this : Lai_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lai_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lai_prm_finalise(this=self._handle)
        
        @property
        def baset(self):
            """
            Element baset ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 152
            
            """
            return _supy_driver.f90wrap_lai_prm__get__baset(self._handle)
        
        @baset.setter
        def baset(self, baset):
            _supy_driver.f90wrap_lai_prm__set__baset(self._handle, baset)
        
        @property
        def gddfull(self):
            """
            Element gddfull ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 153
            
            """
            return _supy_driver.f90wrap_lai_prm__get__gddfull(self._handle)
        
        @gddfull.setter
        def gddfull(self, gddfull):
            _supy_driver.f90wrap_lai_prm__set__gddfull(self._handle, gddfull)
        
        @property
        def basete(self):
            """
            Element basete ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 154
            
            """
            return _supy_driver.f90wrap_lai_prm__get__basete(self._handle)
        
        @basete.setter
        def basete(self, basete):
            _supy_driver.f90wrap_lai_prm__set__basete(self._handle, basete)
        
        @property
        def sddfull(self):
            """
            Element sddfull ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 155
            
            """
            return _supy_driver.f90wrap_lai_prm__get__sddfull(self._handle)
        
        @sddfull.setter
        def sddfull(self, sddfull):
            _supy_driver.f90wrap_lai_prm__set__sddfull(self._handle, sddfull)
        
        @property
        def laimin(self):
            """
            Element laimin ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 156
            
            """
            return _supy_driver.f90wrap_lai_prm__get__laimin(self._handle)
        
        @laimin.setter
        def laimin(self, laimin):
            _supy_driver.f90wrap_lai_prm__set__laimin(self._handle, laimin)
        
        @property
        def laimax(self):
            """
            Element laimax ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 157
            
            """
            return _supy_driver.f90wrap_lai_prm__get__laimax(self._handle)
        
        @laimax.setter
        def laimax(self, laimax):
            _supy_driver.f90wrap_lai_prm__set__laimax(self._handle, laimax)
        
        @property
        def laipower(self):
            """
            Element laipower ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 158
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_lai_prm__array__laipower(self._handle)
            if array_handle in self._arrays:
                laipower = self._arrays[array_handle]
            else:
                laipower = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_lai_prm__array__laipower)
                self._arrays[array_handle] = laipower
            return laipower
        
        @laipower.setter
        def laipower(self, laipower):
            self.laipower[...] = laipower
        
        @property
        def laitype(self):
            """
            Element laitype ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 159
            
            """
            return _supy_driver.f90wrap_lai_prm__get__laitype(self._handle)
        
        @laitype.setter
        def laitype(self, laitype):
            _supy_driver.f90wrap_lai_prm__set__laitype(self._handle, laitype)
        
        def __str__(self):
            ret = ['<lai_prm>{\n']
            ret.append('    baset : ')
            ret.append(repr(self.baset))
            ret.append(',\n    gddfull : ')
            ret.append(repr(self.gddfull))
            ret.append(',\n    basete : ')
            ret.append(repr(self.basete))
            ret.append(',\n    sddfull : ')
            ret.append(repr(self.sddfull))
            ret.append(',\n    laimin : ')
            ret.append(repr(self.laimin))
            ret.append(',\n    laimax : ')
            ret.append(repr(self.laimax))
            ret.append(',\n    laipower : ')
            ret.append(repr(self.laipower))
            ret.append(',\n    laitype : ')
            ret.append(repr(self.laitype))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.OHM_COEF_LC")
    class OHM_COEF_LC(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_coef_lc)
        
        
        Defined at suews_ctrl_driver.fpp lines 161-165
        
        """
        def __init__(self, handle=None):
            """
            self = Ohm_Coef_Lc()
            
            
            Defined at suews_ctrl_driver.fpp lines 161-165
            
            
            Returns
            -------
            this : Ohm_Coef_Lc
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_coef_lc
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_ohm_coef_lc_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_Coef_Lc
            
            
            Defined at suews_ctrl_driver.fpp lines 161-165
            
            Parameters
            ----------
            this : Ohm_Coef_Lc
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_coef_lc
            """
            if self._alloc:
                _supy_driver.f90wrap_ohm_coef_lc_finalise(this=self._handle)
        
        @property
        def summer_dry(self):
            """
            Element summer_dry ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 162
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__summer_dry(self._handle)
        
        @summer_dry.setter
        def summer_dry(self, summer_dry):
            _supy_driver.f90wrap_ohm_coef_lc__set__summer_dry(self._handle, summer_dry)
        
        @property
        def summer_wet(self):
            """
            Element summer_wet ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 163
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__summer_wet(self._handle)
        
        @summer_wet.setter
        def summer_wet(self, summer_wet):
            _supy_driver.f90wrap_ohm_coef_lc__set__summer_wet(self._handle, summer_wet)
        
        @property
        def winter_dry(self):
            """
            Element winter_dry ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 164
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__winter_dry(self._handle)
        
        @winter_dry.setter
        def winter_dry(self, winter_dry):
            _supy_driver.f90wrap_ohm_coef_lc__set__winter_dry(self._handle, winter_dry)
        
        @property
        def winter_wet(self):
            """
            Element winter_wet ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 165
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__winter_wet(self._handle)
        
        @winter_wet.setter
        def winter_wet(self, winter_wet):
            _supy_driver.f90wrap_ohm_coef_lc__set__winter_wet(self._handle, winter_wet)
        
        def __str__(self):
            ret = ['<ohm_coef_lc>{\n']
            ret.append('    summer_dry : ')
            ret.append(repr(self.summer_dry))
            ret.append(',\n    summer_wet : ')
            ret.append(repr(self.summer_wet))
            ret.append(',\n    winter_dry : ')
            ret.append(repr(self.winter_dry))
            ret.append(',\n    winter_wet : ')
            ret.append(repr(self.winter_wet))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.OHM_PRM")
    class OHM_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 167-173
        
        """
        def __init__(self, handle=None):
            """
            self = Ohm_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 167-173
            
            
            Returns
            -------
            this : Ohm_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_ohm_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 167-173
            
            Parameters
            ----------
            this : Ohm_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_ohm_prm_finalise(this=self._handle)
        
        @property
        def chanohm(self):
            """
            Element chanohm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 168
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__chanohm(self._handle)
        
        @chanohm.setter
        def chanohm(self, chanohm):
            _supy_driver.f90wrap_ohm_prm__set__chanohm(self._handle, chanohm)
        
        @property
        def cpanohm(self):
            """
            Element cpanohm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 169
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__cpanohm(self._handle)
        
        @cpanohm.setter
        def cpanohm(self, cpanohm):
            _supy_driver.f90wrap_ohm_prm__set__cpanohm(self._handle, cpanohm)
        
        @property
        def kkanohm(self):
            """
            Element kkanohm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 170
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__kkanohm(self._handle)
        
        @kkanohm.setter
        def kkanohm(self, kkanohm):
            _supy_driver.f90wrap_ohm_prm__set__kkanohm(self._handle, kkanohm)
        
        @property
        def ohm_threshsw(self):
            """
            Element ohm_threshsw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 171
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__ohm_threshsw(self._handle)
        
        @ohm_threshsw.setter
        def ohm_threshsw(self, ohm_threshsw):
            _supy_driver.f90wrap_ohm_prm__set__ohm_threshsw(self._handle, ohm_threshsw)
        
        @property
        def ohm_threshwd(self):
            """
            Element ohm_threshwd ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 172
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__ohm_threshwd(self._handle)
        
        @ohm_threshwd.setter
        def ohm_threshwd(self, ohm_threshwd):
            _supy_driver.f90wrap_ohm_prm__set__ohm_threshwd(self._handle, ohm_threshwd)
        
        def init_array_ohm_coef_lc(self):
            self.ohm_coef_lc = f90wrap.runtime.FortranDerivedTypeArray(self,
                                            _supy_driver.f90wrap_ohm_prm__array_getitem__ohm_coef_lc,
                                            _supy_driver.f90wrap_ohm_prm__array_setitem__ohm_coef_lc,
                                            _supy_driver.f90wrap_ohm_prm__array_len__ohm_coef_lc,
                                            """
            Element ohm_coef_lc ftype=type(ohm_coef_lc) pytype=Ohm_Coef_Lc
            
            
            Defined at suews_ctrl_driver.fpp line 173
            
            """, Suews_Driver.OHM_COEF_LC)
            return self.ohm_coef_lc
        
        def __str__(self):
            ret = ['<ohm_prm>{\n']
            ret.append('    chanohm : ')
            ret.append(repr(self.chanohm))
            ret.append(',\n    cpanohm : ')
            ret.append(repr(self.cpanohm))
            ret.append(',\n    kkanohm : ')
            ret.append(repr(self.kkanohm))
            ret.append(',\n    ohm_threshsw : ')
            ret.append(repr(self.ohm_threshsw))
            ret.append(',\n    ohm_threshwd : ')
            ret.append(repr(self.ohm_threshwd))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = [init_array_ohm_coef_lc]
        
    
    @f90wrap.runtime.register_class("supy_driver.SOIL_PRM")
    class SOIL_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=soil_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 175-178
        
        """
        def __init__(self, handle=None):
            """
            self = Soil_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 175-178
            
            
            Returns
            -------
            this : Soil_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for soil_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_soil_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 175-178
            
            Parameters
            ----------
            this : Soil_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for soil_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_soil_prm_finalise(this=self._handle)
        
        @property
        def soildepth(self):
            """
            Element soildepth ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 176
            
            """
            return _supy_driver.f90wrap_soil_prm__get__soildepth(self._handle)
        
        @soildepth.setter
        def soildepth(self, soildepth):
            _supy_driver.f90wrap_soil_prm__set__soildepth(self._handle, soildepth)
        
        @property
        def soilstorecap(self):
            """
            Element soilstorecap ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 177
            
            """
            return _supy_driver.f90wrap_soil_prm__get__soilstorecap(self._handle)
        
        @soilstorecap.setter
        def soilstorecap(self, soilstorecap):
            _supy_driver.f90wrap_soil_prm__set__soilstorecap(self._handle, soilstorecap)
        
        @property
        def sathydraulicconduct(self):
            """
            Element sathydraulicconduct ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 178
            
            """
            return _supy_driver.f90wrap_soil_prm__get__sathydraulicconduct(self._handle)
        
        @sathydraulicconduct.setter
        def sathydraulicconduct(self, sathydraulicconduct):
            _supy_driver.f90wrap_soil_prm__set__sathydraulicconduct(self._handle, \
                sathydraulicconduct)
        
        def __str__(self):
            ret = ['<soil_prm>{\n']
            ret.append('    soildepth : ')
            ret.append(repr(self.soildepth))
            ret.append(',\n    soilstorecap : ')
            ret.append(repr(self.soilstorecap))
            ret.append(',\n    sathydraulicconduct : ')
            ret.append(repr(self.sathydraulicconduct))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.anthroHEAT_PRM")
    class anthroHEAT_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=anthroheat_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 180-205
        
        """
        def __init__(self, handle=None):
            """
            self = Anthroheat_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 180-205
            
            
            Returns
            -------
            this : Anthroheat_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for anthroheat_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_anthroheat_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Anthroheat_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 180-205
            
            Parameters
            ----------
            this : Anthroheat_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for anthroheat_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_anthroheat_prm_finalise(this=self._handle)
        
        @property
        def qf0_beu_working(self):
            """
            Element qf0_beu_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 181
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf0_beu_working(self._handle)
        
        @qf0_beu_working.setter
        def qf0_beu_working(self, qf0_beu_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf0_beu_working(self._handle, \
                qf0_beu_working)
        
        @property
        def qf0_beu_holiday(self):
            """
            Element qf0_beu_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 182
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf0_beu_holiday(self._handle)
        
        @qf0_beu_holiday.setter
        def qf0_beu_holiday(self, qf0_beu_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf0_beu_holiday(self._handle, \
                qf0_beu_holiday)
        
        @property
        def qf_a_working(self):
            """
            Element qf_a_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 183
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_a_working(self._handle)
        
        @qf_a_working.setter
        def qf_a_working(self, qf_a_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_a_working(self._handle, \
                qf_a_working)
        
        @property
        def qf_a_holiday(self):
            """
            Element qf_a_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 184
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_a_holiday(self._handle)
        
        @qf_a_holiday.setter
        def qf_a_holiday(self, qf_a_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_a_holiday(self._handle, \
                qf_a_holiday)
        
        @property
        def qf_b_working(self):
            """
            Element qf_b_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 185
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_b_working(self._handle)
        
        @qf_b_working.setter
        def qf_b_working(self, qf_b_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_b_working(self._handle, \
                qf_b_working)
        
        @property
        def qf_b_holiday(self):
            """
            Element qf_b_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 186
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_b_holiday(self._handle)
        
        @qf_b_holiday.setter
        def qf_b_holiday(self, qf_b_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_b_holiday(self._handle, \
                qf_b_holiday)
        
        @property
        def qf_c_working(self):
            """
            Element qf_c_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 187
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_c_working(self._handle)
        
        @qf_c_working.setter
        def qf_c_working(self, qf_c_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_c_working(self._handle, \
                qf_c_working)
        
        @property
        def qf_c_holiday(self):
            """
            Element qf_c_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 188
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_c_holiday(self._handle)
        
        @qf_c_holiday.setter
        def qf_c_holiday(self, qf_c_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_c_holiday(self._handle, \
                qf_c_holiday)
        
        @property
        def baset_cooling_working(self):
            """
            Element baset_cooling_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 189
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_cooling_working(self._handle)
        
        @baset_cooling_working.setter
        def baset_cooling_working(self, baset_cooling_working):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_cooling_working(self._handle, \
                baset_cooling_working)
        
        @property
        def baset_cooling_holiday(self):
            """
            Element baset_cooling_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 190
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_cooling_holiday(self._handle)
        
        @baset_cooling_holiday.setter
        def baset_cooling_holiday(self, baset_cooling_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_cooling_holiday(self._handle, \
                baset_cooling_holiday)
        
        @property
        def baset_heating_working(self):
            """
            Element baset_heating_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 191
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_heating_working(self._handle)
        
        @baset_heating_working.setter
        def baset_heating_working(self, baset_heating_working):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_heating_working(self._handle, \
                baset_heating_working)
        
        @property
        def baset_heating_holiday(self):
            """
            Element baset_heating_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 192
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_heating_holiday(self._handle)
        
        @baset_heating_holiday.setter
        def baset_heating_holiday(self, baset_heating_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_heating_holiday(self._handle, \
                baset_heating_holiday)
        
        @property
        def ah_min_working(self):
            """
            Element ah_min_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 193
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__ah_min_working(self._handle)
        
        @ah_min_working.setter
        def ah_min_working(self, ah_min_working):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_min_working(self._handle, \
                ah_min_working)
        
        @property
        def ah_min_holiday(self):
            """
            Element ah_min_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 194
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__ah_min_holiday(self._handle)
        
        @ah_min_holiday.setter
        def ah_min_holiday(self, ah_min_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_min_holiday(self._handle, \
                ah_min_holiday)
        
        @property
        def ah_slope_cooling_working(self):
            """
            Element ah_slope_cooling_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 195
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_cooling_working(self._handle)
        
        @ah_slope_cooling_working.setter
        def ah_slope_cooling_working(self, ah_slope_cooling_working):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_cooling_working(self._handle, \
                ah_slope_cooling_working)
        
        @property
        def ah_slope_cooling_holiday(self):
            """
            Element ah_slope_cooling_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 196
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_cooling_holiday(self._handle)
        
        @ah_slope_cooling_holiday.setter
        def ah_slope_cooling_holiday(self, ah_slope_cooling_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_cooling_holiday(self._handle, \
                ah_slope_cooling_holiday)
        
        @property
        def ah_slope_heating_working(self):
            """
            Element ah_slope_heating_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 197
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_heating_working(self._handle)
        
        @ah_slope_heating_working.setter
        def ah_slope_heating_working(self, ah_slope_heating_working):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_heating_working(self._handle, \
                ah_slope_heating_working)
        
        @property
        def ah_slope_heating_holiday(self):
            """
            Element ah_slope_heating_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 198
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_heating_holiday(self._handle)
        
        @ah_slope_heating_holiday.setter
        def ah_slope_heating_holiday(self, ah_slope_heating_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_heating_holiday(self._handle, \
                ah_slope_heating_holiday)
        
        @property
        def ahprof_24hr_working(self):
            """
            Element ahprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 199
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                ahprof_24hr_working = self._arrays[array_handle]
            else:
                ahprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_working)
                self._arrays[array_handle] = ahprof_24hr_working
            return ahprof_24hr_working
        
        @ahprof_24hr_working.setter
        def ahprof_24hr_working(self, ahprof_24hr_working):
            self.ahprof_24hr_working[...] = ahprof_24hr_working
        
        @property
        def ahprof_24hr_holiday(self):
            """
            Element ahprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 200
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                ahprof_24hr_holiday = self._arrays[array_handle]
            else:
                ahprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_holiday)
                self._arrays[array_handle] = ahprof_24hr_holiday
            return ahprof_24hr_holiday
        
        @ahprof_24hr_holiday.setter
        def ahprof_24hr_holiday(self, ahprof_24hr_holiday):
            self.ahprof_24hr_holiday[...] = ahprof_24hr_holiday
        
        @property
        def popdensdaytime_working(self):
            """
            Element popdensdaytime_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 201
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__popdensdaytime_working(self._handle)
        
        @popdensdaytime_working.setter
        def popdensdaytime_working(self, popdensdaytime_working):
            _supy_driver.f90wrap_anthroheat_prm__set__popdensdaytime_working(self._handle, \
                popdensdaytime_working)
        
        @property
        def popdensdaytime_holiday(self):
            """
            Element popdensdaytime_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 202
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__popdensdaytime_holiday(self._handle)
        
        @popdensdaytime_holiday.setter
        def popdensdaytime_holiday(self, popdensdaytime_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__popdensdaytime_holiday(self._handle, \
                popdensdaytime_holiday)
        
        @property
        def popdensnighttime(self):
            """
            Element popdensnighttime ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 203
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__popdensnighttime(self._handle)
        
        @popdensnighttime.setter
        def popdensnighttime(self, popdensnighttime):
            _supy_driver.f90wrap_anthroheat_prm__set__popdensnighttime(self._handle, \
                popdensnighttime)
        
        @property
        def popprof_24hr_working(self):
            """
            Element popprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 204
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                popprof_24hr_working = self._arrays[array_handle]
            else:
                popprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_working)
                self._arrays[array_handle] = popprof_24hr_working
            return popprof_24hr_working
        
        @popprof_24hr_working.setter
        def popprof_24hr_working(self, popprof_24hr_working):
            self.popprof_24hr_working[...] = popprof_24hr_working
        
        @property
        def popprof_24hr_holiday(self):
            """
            Element popprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 205
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                popprof_24hr_holiday = self._arrays[array_handle]
            else:
                popprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_holiday)
                self._arrays[array_handle] = popprof_24hr_holiday
            return popprof_24hr_holiday
        
        @popprof_24hr_holiday.setter
        def popprof_24hr_holiday(self, popprof_24hr_holiday):
            self.popprof_24hr_holiday[...] = popprof_24hr_holiday
        
        def __str__(self):
            ret = ['<anthroheat_prm>{\n']
            ret.append('    qf0_beu_working : ')
            ret.append(repr(self.qf0_beu_working))
            ret.append(',\n    qf0_beu_holiday : ')
            ret.append(repr(self.qf0_beu_holiday))
            ret.append(',\n    qf_a_working : ')
            ret.append(repr(self.qf_a_working))
            ret.append(',\n    qf_a_holiday : ')
            ret.append(repr(self.qf_a_holiday))
            ret.append(',\n    qf_b_working : ')
            ret.append(repr(self.qf_b_working))
            ret.append(',\n    qf_b_holiday : ')
            ret.append(repr(self.qf_b_holiday))
            ret.append(',\n    qf_c_working : ')
            ret.append(repr(self.qf_c_working))
            ret.append(',\n    qf_c_holiday : ')
            ret.append(repr(self.qf_c_holiday))
            ret.append(',\n    baset_cooling_working : ')
            ret.append(repr(self.baset_cooling_working))
            ret.append(',\n    baset_cooling_holiday : ')
            ret.append(repr(self.baset_cooling_holiday))
            ret.append(',\n    baset_heating_working : ')
            ret.append(repr(self.baset_heating_working))
            ret.append(',\n    baset_heating_holiday : ')
            ret.append(repr(self.baset_heating_holiday))
            ret.append(',\n    ah_min_working : ')
            ret.append(repr(self.ah_min_working))
            ret.append(',\n    ah_min_holiday : ')
            ret.append(repr(self.ah_min_holiday))
            ret.append(',\n    ah_slope_cooling_working : ')
            ret.append(repr(self.ah_slope_cooling_working))
            ret.append(',\n    ah_slope_cooling_holiday : ')
            ret.append(repr(self.ah_slope_cooling_holiday))
            ret.append(',\n    ah_slope_heating_working : ')
            ret.append(repr(self.ah_slope_heating_working))
            ret.append(',\n    ah_slope_heating_holiday : ')
            ret.append(repr(self.ah_slope_heating_holiday))
            ret.append(',\n    ahprof_24hr_working : ')
            ret.append(repr(self.ahprof_24hr_working))
            ret.append(',\n    ahprof_24hr_holiday : ')
            ret.append(repr(self.ahprof_24hr_holiday))
            ret.append(',\n    popdensdaytime_working : ')
            ret.append(repr(self.popdensdaytime_working))
            ret.append(',\n    popdensdaytime_holiday : ')
            ret.append(repr(self.popdensdaytime_holiday))
            ret.append(',\n    popdensnighttime : ')
            ret.append(repr(self.popdensnighttime))
            ret.append(',\n    popprof_24hr_working : ')
            ret.append(repr(self.popprof_24hr_working))
            ret.append(',\n    popprof_24hr_holiday : ')
            ret.append(repr(self.popprof_24hr_holiday))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.IRRIG_daywater")
    class IRRIG_daywater(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=irrig_daywater)
        
        
        Defined at suews_ctrl_driver.fpp lines 207-221
        
        """
        def __init__(self, handle=None):
            """
            self = Irrig_Daywater()
            
            
            Defined at suews_ctrl_driver.fpp lines 207-221
            
            
            Returns
            -------
            this : Irrig_Daywater
            	Object to be constructed
            
            
            Automatically generated constructor for irrig_daywater
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_irrig_daywater_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Irrig_Daywater
            
            
            Defined at suews_ctrl_driver.fpp lines 207-221
            
            Parameters
            ----------
            this : Irrig_Daywater
            	Object to be destructed
            
            
            Automatically generated destructor for irrig_daywater
            """
            if self._alloc:
                _supy_driver.f90wrap_irrig_daywater_finalise(this=self._handle)
        
        @property
        def monday_flag(self):
            """
            Element monday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 208
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__monday_flag(self._handle)
        
        @monday_flag.setter
        def monday_flag(self, monday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__monday_flag(self._handle, monday_flag)
        
        @property
        def monday_percent(self):
            """
            Element monday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 209
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__monday_percent(self._handle)
        
        @monday_percent.setter
        def monday_percent(self, monday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__monday_percent(self._handle, \
                monday_percent)
        
        @property
        def tuesday_flag(self):
            """
            Element tuesday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 210
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__tuesday_flag(self._handle)
        
        @tuesday_flag.setter
        def tuesday_flag(self, tuesday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__tuesday_flag(self._handle, \
                tuesday_flag)
        
        @property
        def tuesday_percent(self):
            """
            Element tuesday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 211
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__tuesday_percent(self._handle)
        
        @tuesday_percent.setter
        def tuesday_percent(self, tuesday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__tuesday_percent(self._handle, \
                tuesday_percent)
        
        @property
        def wednesday_flag(self):
            """
            Element wednesday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 212
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__wednesday_flag(self._handle)
        
        @wednesday_flag.setter
        def wednesday_flag(self, wednesday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__wednesday_flag(self._handle, \
                wednesday_flag)
        
        @property
        def wednesday_percent(self):
            """
            Element wednesday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 213
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__wednesday_percent(self._handle)
        
        @wednesday_percent.setter
        def wednesday_percent(self, wednesday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__wednesday_percent(self._handle, \
                wednesday_percent)
        
        @property
        def thursday_flag(self):
            """
            Element thursday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 214
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__thursday_flag(self._handle)
        
        @thursday_flag.setter
        def thursday_flag(self, thursday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__thursday_flag(self._handle, \
                thursday_flag)
        
        @property
        def thursday_percent(self):
            """
            Element thursday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 215
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__thursday_percent(self._handle)
        
        @thursday_percent.setter
        def thursday_percent(self, thursday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__thursday_percent(self._handle, \
                thursday_percent)
        
        @property
        def friday_flag(self):
            """
            Element friday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 216
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__friday_flag(self._handle)
        
        @friday_flag.setter
        def friday_flag(self, friday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__friday_flag(self._handle, friday_flag)
        
        @property
        def friday_percent(self):
            """
            Element friday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 217
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__friday_percent(self._handle)
        
        @friday_percent.setter
        def friday_percent(self, friday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__friday_percent(self._handle, \
                friday_percent)
        
        @property
        def saturday_flag(self):
            """
            Element saturday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 218
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__saturday_flag(self._handle)
        
        @saturday_flag.setter
        def saturday_flag(self, saturday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__saturday_flag(self._handle, \
                saturday_flag)
        
        @property
        def saturday_percent(self):
            """
            Element saturday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 219
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__saturday_percent(self._handle)
        
        @saturday_percent.setter
        def saturday_percent(self, saturday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__saturday_percent(self._handle, \
                saturday_percent)
        
        @property
        def sunday_flag(self):
            """
            Element sunday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 220
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__sunday_flag(self._handle)
        
        @sunday_flag.setter
        def sunday_flag(self, sunday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__sunday_flag(self._handle, sunday_flag)
        
        @property
        def sunday_percent(self):
            """
            Element sunday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 221
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__sunday_percent(self._handle)
        
        @sunday_percent.setter
        def sunday_percent(self, sunday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__sunday_percent(self._handle, \
                sunday_percent)
        
        def __str__(self):
            ret = ['<irrig_daywater>{\n']
            ret.append('    monday_flag : ')
            ret.append(repr(self.monday_flag))
            ret.append(',\n    monday_percent : ')
            ret.append(repr(self.monday_percent))
            ret.append(',\n    tuesday_flag : ')
            ret.append(repr(self.tuesday_flag))
            ret.append(',\n    tuesday_percent : ')
            ret.append(repr(self.tuesday_percent))
            ret.append(',\n    wednesday_flag : ')
            ret.append(repr(self.wednesday_flag))
            ret.append(',\n    wednesday_percent : ')
            ret.append(repr(self.wednesday_percent))
            ret.append(',\n    thursday_flag : ')
            ret.append(repr(self.thursday_flag))
            ret.append(',\n    thursday_percent : ')
            ret.append(repr(self.thursday_percent))
            ret.append(',\n    friday_flag : ')
            ret.append(repr(self.friday_flag))
            ret.append(',\n    friday_percent : ')
            ret.append(repr(self.friday_percent))
            ret.append(',\n    saturday_flag : ')
            ret.append(repr(self.saturday_flag))
            ret.append(',\n    saturday_percent : ')
            ret.append(repr(self.saturday_percent))
            ret.append(',\n    sunday_flag : ')
            ret.append(repr(self.sunday_flag))
            ret.append(',\n    sunday_percent : ')
            ret.append(repr(self.sunday_percent))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.IRRIGATION_PRM")
    class IRRIGATION_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=irrigation_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 223-235
        
        """
        def __init__(self, handle=None):
            """
            self = Irrigation_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 223-235
            
            
            Returns
            -------
            this : Irrigation_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for irrigation_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_irrigation_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Irrigation_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 223-235
            
            Parameters
            ----------
            this : Irrigation_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for irrigation_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_irrigation_prm_finalise(this=self._handle)
        
        @property
        def h_maintain(self):
            """
            Element h_maintain ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 224
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__h_maintain(self._handle)
        
        @h_maintain.setter
        def h_maintain(self, h_maintain):
            _supy_driver.f90wrap_irrigation_prm__set__h_maintain(self._handle, h_maintain)
        
        @property
        def faut(self):
            """
            Element faut ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 225
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__faut(self._handle)
        
        @faut.setter
        def faut(self, faut):
            _supy_driver.f90wrap_irrigation_prm__set__faut(self._handle, faut)
        
        @property
        def ie_a(self):
            """
            Element ie_a ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 226
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__ie_a(self._handle)
            if array_handle in self._arrays:
                ie_a = self._arrays[array_handle]
            else:
                ie_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__ie_a)
                self._arrays[array_handle] = ie_a
            return ie_a
        
        @ie_a.setter
        def ie_a(self, ie_a):
            self.ie_a[...] = ie_a
        
        @property
        def ie_m(self):
            """
            Element ie_m ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 227
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__ie_m(self._handle)
            if array_handle in self._arrays:
                ie_m = self._arrays[array_handle]
            else:
                ie_m = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__ie_m)
                self._arrays[array_handle] = ie_m
            return ie_m
        
        @ie_m.setter
        def ie_m(self, ie_m):
            self.ie_m[...] = ie_m
        
        @property
        def ie_start(self):
            """
            Element ie_start ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 228
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__ie_start(self._handle)
        
        @ie_start.setter
        def ie_start(self, ie_start):
            _supy_driver.f90wrap_irrigation_prm__set__ie_start(self._handle, ie_start)
        
        @property
        def ie_end(self):
            """
            Element ie_end ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 229
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__ie_end(self._handle)
        
        @ie_end.setter
        def ie_end(self, ie_end):
            _supy_driver.f90wrap_irrigation_prm__set__ie_end(self._handle, ie_end)
        
        @property
        def internalwateruse_h(self):
            """
            Element internalwateruse_h ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 230
            
            """
            return \
                _supy_driver.f90wrap_irrigation_prm__get__internalwateruse_h(self._handle)
        
        @internalwateruse_h.setter
        def internalwateruse_h(self, internalwateruse_h):
            _supy_driver.f90wrap_irrigation_prm__set__internalwateruse_h(self._handle, \
                internalwateruse_h)
        
        @property
        def irr_daywater(self):
            """
            Element irr_daywater ftype=type(irrig_daywater) pytype=Irrig_Daywater
            
            
            Defined at suews_ctrl_driver.fpp line 231
            
            """
            irr_daywater_handle = \
                _supy_driver.f90wrap_irrigation_prm__get__irr_daywater(self._handle)
            if tuple(irr_daywater_handle) in self._objs:
                irr_daywater = self._objs[tuple(irr_daywater_handle)]
            else:
                irr_daywater = suews_driver.IRRIG_daywater.from_handle(irr_daywater_handle)
                self._objs[tuple(irr_daywater_handle)] = irr_daywater
            return irr_daywater
        
        @irr_daywater.setter
        def irr_daywater(self, irr_daywater):
            irr_daywater = irr_daywater._handle
            _supy_driver.f90wrap_irrigation_prm__set__irr_daywater(self._handle, \
                irr_daywater)
        
        @property
        def wuprofa_24hr_working(self):
            """
            Element wuprofa_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 232
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_working(self._handle)
            if array_handle in self._arrays:
                wuprofa_24hr_working = self._arrays[array_handle]
            else:
                wuprofa_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_working)
                self._arrays[array_handle] = wuprofa_24hr_working
            return wuprofa_24hr_working
        
        @wuprofa_24hr_working.setter
        def wuprofa_24hr_working(self, wuprofa_24hr_working):
            self.wuprofa_24hr_working[...] = wuprofa_24hr_working
        
        @property
        def wuprofa_24hr_holiday(self):
            """
            Element wuprofa_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 233
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                wuprofa_24hr_holiday = self._arrays[array_handle]
            else:
                wuprofa_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_holiday)
                self._arrays[array_handle] = wuprofa_24hr_holiday
            return wuprofa_24hr_holiday
        
        @wuprofa_24hr_holiday.setter
        def wuprofa_24hr_holiday(self, wuprofa_24hr_holiday):
            self.wuprofa_24hr_holiday[...] = wuprofa_24hr_holiday
        
        @property
        def wuprofm_24hr_working(self):
            """
            Element wuprofm_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 234
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_working(self._handle)
            if array_handle in self._arrays:
                wuprofm_24hr_working = self._arrays[array_handle]
            else:
                wuprofm_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_working)
                self._arrays[array_handle] = wuprofm_24hr_working
            return wuprofm_24hr_working
        
        @wuprofm_24hr_working.setter
        def wuprofm_24hr_working(self, wuprofm_24hr_working):
            self.wuprofm_24hr_working[...] = wuprofm_24hr_working
        
        @property
        def wuprofm_24hr_holiday(self):
            """
            Element wuprofm_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 235
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                wuprofm_24hr_holiday = self._arrays[array_handle]
            else:
                wuprofm_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_holiday)
                self._arrays[array_handle] = wuprofm_24hr_holiday
            return wuprofm_24hr_holiday
        
        @wuprofm_24hr_holiday.setter
        def wuprofm_24hr_holiday(self, wuprofm_24hr_holiday):
            self.wuprofm_24hr_holiday[...] = wuprofm_24hr_holiday
        
        def __str__(self):
            ret = ['<irrigation_prm>{\n']
            ret.append('    h_maintain : ')
            ret.append(repr(self.h_maintain))
            ret.append(',\n    faut : ')
            ret.append(repr(self.faut))
            ret.append(',\n    ie_a : ')
            ret.append(repr(self.ie_a))
            ret.append(',\n    ie_m : ')
            ret.append(repr(self.ie_m))
            ret.append(',\n    ie_start : ')
            ret.append(repr(self.ie_start))
            ret.append(',\n    ie_end : ')
            ret.append(repr(self.ie_end))
            ret.append(',\n    internalwateruse_h : ')
            ret.append(repr(self.internalwateruse_h))
            ret.append(',\n    irr_daywater : ')
            ret.append(repr(self.irr_daywater))
            ret.append(',\n    wuprofa_24hr_working : ')
            ret.append(repr(self.wuprofa_24hr_working))
            ret.append(',\n    wuprofa_24hr_holiday : ')
            ret.append(repr(self.wuprofa_24hr_holiday))
            ret.append(',\n    wuprofm_24hr_working : ')
            ret.append(repr(self.wuprofm_24hr_working))
            ret.append(',\n    wuprofm_24hr_holiday : ')
            ret.append(repr(self.wuprofm_24hr_holiday))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.anthroEMIS_PRM")
    class anthroEMIS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=anthroemis_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 237-256
        
        """
        def __init__(self, handle=None):
            """
            self = Anthroemis_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 237-256
            
            
            Returns
            -------
            this : Anthroemis_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for anthroemis_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_anthroemis_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Anthroemis_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 237-256
            
            Parameters
            ----------
            this : Anthroemis_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for anthroemis_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_anthroemis_prm_finalise(this=self._handle)
        
        @property
        def startdls(self):
            """
            Element startdls ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 238
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__startdls(self._handle)
        
        @startdls.setter
        def startdls(self, startdls):
            _supy_driver.f90wrap_anthroemis_prm__set__startdls(self._handle, startdls)
        
        @property
        def enddls(self):
            """
            Element enddls ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 239
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__enddls(self._handle)
        
        @enddls.setter
        def enddls(self, enddls):
            _supy_driver.f90wrap_anthroemis_prm__set__enddls(self._handle, enddls)
        
        @property
        def anthroheat(self):
            """
            Element anthroheat ftype=type(anthroheat_prm) pytype=Anthroheat_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 240
            
            """
            anthroheat_handle = \
                _supy_driver.f90wrap_anthroemis_prm__get__anthroheat(self._handle)
            if tuple(anthroheat_handle) in self._objs:
                anthroheat = self._objs[tuple(anthroheat_handle)]
            else:
                anthroheat = suews_driver.anthroHEAT_PRM.from_handle(anthroheat_handle)
                self._objs[tuple(anthroheat_handle)] = anthroheat
            return anthroheat
        
        @anthroheat.setter
        def anthroheat(self, anthroheat):
            anthroheat = anthroheat._handle
            _supy_driver.f90wrap_anthroemis_prm__set__anthroheat(self._handle, anthroheat)
        
        @property
        def ef_umolco2perj(self):
            """
            Element ef_umolco2perj ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 241
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__ef_umolco2perj(self._handle)
        
        @ef_umolco2perj.setter
        def ef_umolco2perj(self, ef_umolco2perj):
            _supy_driver.f90wrap_anthroemis_prm__set__ef_umolco2perj(self._handle, \
                ef_umolco2perj)
        
        @property
        def enef_v_jkm(self):
            """
            Element enef_v_jkm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 242
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__enef_v_jkm(self._handle)
        
        @enef_v_jkm.setter
        def enef_v_jkm(self, enef_v_jkm):
            _supy_driver.f90wrap_anthroemis_prm__set__enef_v_jkm(self._handle, enef_v_jkm)
        
        @property
        def frfossilfuel_heat(self):
            """
            Element frfossilfuel_heat ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 243
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__frfossilfuel_heat(self._handle)
        
        @frfossilfuel_heat.setter
        def frfossilfuel_heat(self, frfossilfuel_heat):
            _supy_driver.f90wrap_anthroemis_prm__set__frfossilfuel_heat(self._handle, \
                frfossilfuel_heat)
        
        @property
        def frfossilfuel_nonheat(self):
            """
            Element frfossilfuel_nonheat ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 244
            
            """
            return \
                _supy_driver.f90wrap_anthroemis_prm__get__frfossilfuel_nonheat(self._handle)
        
        @frfossilfuel_nonheat.setter
        def frfossilfuel_nonheat(self, frfossilfuel_nonheat):
            _supy_driver.f90wrap_anthroemis_prm__set__frfossilfuel_nonheat(self._handle, \
                frfossilfuel_nonheat)
        
        @property
        def fcef_v_kgkm(self):
            """
            Element fcef_v_kgkm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 245
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__fcef_v_kgkm(self._handle)
            if array_handle in self._arrays:
                fcef_v_kgkm = self._arrays[array_handle]
            else:
                fcef_v_kgkm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__fcef_v_kgkm)
                self._arrays[array_handle] = fcef_v_kgkm
            return fcef_v_kgkm
        
        @fcef_v_kgkm.setter
        def fcef_v_kgkm(self, fcef_v_kgkm):
            self.fcef_v_kgkm[...] = fcef_v_kgkm
        
        @property
        def humactivity_24hr_working(self):
            """
            Element humactivity_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 246
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_working(self._handle)
            if array_handle in self._arrays:
                humactivity_24hr_working = self._arrays[array_handle]
            else:
                humactivity_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_working)
                self._arrays[array_handle] = humactivity_24hr_working
            return humactivity_24hr_working
        
        @humactivity_24hr_working.setter
        def humactivity_24hr_working(self, humactivity_24hr_working):
            self.humactivity_24hr_working[...] = humactivity_24hr_working
        
        @property
        def humactivity_24hr_holiday(self):
            """
            Element humactivity_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 247
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                humactivity_24hr_holiday = self._arrays[array_handle]
            else:
                humactivity_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_holiday)
                self._arrays[array_handle] = humactivity_24hr_holiday
            return humactivity_24hr_holiday
        
        @humactivity_24hr_holiday.setter
        def humactivity_24hr_holiday(self, humactivity_24hr_holiday):
            self.humactivity_24hr_holiday[...] = humactivity_24hr_holiday
        
        @property
        def maxfcmetab(self):
            """
            Element maxfcmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 248
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__maxfcmetab(self._handle)
        
        @maxfcmetab.setter
        def maxfcmetab(self, maxfcmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__maxfcmetab(self._handle, maxfcmetab)
        
        @property
        def maxqfmetab(self):
            """
            Element maxqfmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 249
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__maxqfmetab(self._handle)
        
        @maxqfmetab.setter
        def maxqfmetab(self, maxqfmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__maxqfmetab(self._handle, maxqfmetab)
        
        @property
        def minfcmetab(self):
            """
            Element minfcmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 250
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__minfcmetab(self._handle)
        
        @minfcmetab.setter
        def minfcmetab(self, minfcmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__minfcmetab(self._handle, minfcmetab)
        
        @property
        def minqfmetab(self):
            """
            Element minqfmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 251
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__minqfmetab(self._handle)
        
        @minqfmetab.setter
        def minqfmetab(self, minqfmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__minqfmetab(self._handle, minqfmetab)
        
        @property
        def trafficrate_working(self):
            """
            Element trafficrate_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 252
            
            """
            return \
                _supy_driver.f90wrap_anthroemis_prm__get__trafficrate_working(self._handle)
        
        @trafficrate_working.setter
        def trafficrate_working(self, trafficrate_working):
            _supy_driver.f90wrap_anthroemis_prm__set__trafficrate_working(self._handle, \
                trafficrate_working)
        
        @property
        def trafficrate_holiday(self):
            """
            Element trafficrate_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 253
            
            """
            return \
                _supy_driver.f90wrap_anthroemis_prm__get__trafficrate_holiday(self._handle)
        
        @trafficrate_holiday.setter
        def trafficrate_holiday(self, trafficrate_holiday):
            _supy_driver.f90wrap_anthroemis_prm__set__trafficrate_holiday(self._handle, \
                trafficrate_holiday)
        
        @property
        def trafficunits(self):
            """
            Element trafficunits ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 254
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__trafficunits(self._handle)
        
        @trafficunits.setter
        def trafficunits(self, trafficunits):
            _supy_driver.f90wrap_anthroemis_prm__set__trafficunits(self._handle, \
                trafficunits)
        
        @property
        def traffprof_24hr_working(self):
            """
            Element traffprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 255
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                traffprof_24hr_working = self._arrays[array_handle]
            else:
                traffprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_working)
                self._arrays[array_handle] = traffprof_24hr_working
            return traffprof_24hr_working
        
        @traffprof_24hr_working.setter
        def traffprof_24hr_working(self, traffprof_24hr_working):
            self.traffprof_24hr_working[...] = traffprof_24hr_working
        
        @property
        def traffprof_24hr_holiday(self):
            """
            Element traffprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 256
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                traffprof_24hr_holiday = self._arrays[array_handle]
            else:
                traffprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_holiday)
                self._arrays[array_handle] = traffprof_24hr_holiday
            return traffprof_24hr_holiday
        
        @traffprof_24hr_holiday.setter
        def traffprof_24hr_holiday(self, traffprof_24hr_holiday):
            self.traffprof_24hr_holiday[...] = traffprof_24hr_holiday
        
        def __str__(self):
            ret = ['<anthroemis_prm>{\n']
            ret.append('    startdls : ')
            ret.append(repr(self.startdls))
            ret.append(',\n    enddls : ')
            ret.append(repr(self.enddls))
            ret.append(',\n    anthroheat : ')
            ret.append(repr(self.anthroheat))
            ret.append(',\n    ef_umolco2perj : ')
            ret.append(repr(self.ef_umolco2perj))
            ret.append(',\n    enef_v_jkm : ')
            ret.append(repr(self.enef_v_jkm))
            ret.append(',\n    frfossilfuel_heat : ')
            ret.append(repr(self.frfossilfuel_heat))
            ret.append(',\n    frfossilfuel_nonheat : ')
            ret.append(repr(self.frfossilfuel_nonheat))
            ret.append(',\n    fcef_v_kgkm : ')
            ret.append(repr(self.fcef_v_kgkm))
            ret.append(',\n    humactivity_24hr_working : ')
            ret.append(repr(self.humactivity_24hr_working))
            ret.append(',\n    humactivity_24hr_holiday : ')
            ret.append(repr(self.humactivity_24hr_holiday))
            ret.append(',\n    maxfcmetab : ')
            ret.append(repr(self.maxfcmetab))
            ret.append(',\n    maxqfmetab : ')
            ret.append(repr(self.maxqfmetab))
            ret.append(',\n    minfcmetab : ')
            ret.append(repr(self.minfcmetab))
            ret.append(',\n    minqfmetab : ')
            ret.append(repr(self.minqfmetab))
            ret.append(',\n    trafficrate_working : ')
            ret.append(repr(self.trafficrate_working))
            ret.append(',\n    trafficrate_holiday : ')
            ret.append(repr(self.trafficrate_holiday))
            ret.append(',\n    trafficunits : ')
            ret.append(repr(self.trafficunits))
            ret.append(',\n    traffprof_24hr_working : ')
            ret.append(repr(self.traffprof_24hr_working))
            ret.append(',\n    traffprof_24hr_holiday : ')
            ret.append(repr(self.traffprof_24hr_holiday))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SNOW_PRM")
    class SNOW_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=snow_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 258-277
        
        """
        def __init__(self, handle=None):
            """
            self = Snow_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 258-277
            
            
            Returns
            -------
            this : Snow_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for snow_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_snow_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Snow_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 258-277
            
            Parameters
            ----------
            this : Snow_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for snow_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_snow_prm_finalise(this=self._handle)
        
        @property
        def crwmax(self):
            """
            Element crwmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 259
            
            """
            return _supy_driver.f90wrap_snow_prm__get__crwmax(self._handle)
        
        @crwmax.setter
        def crwmax(self, crwmax):
            _supy_driver.f90wrap_snow_prm__set__crwmax(self._handle, crwmax)
        
        @property
        def crwmin(self):
            """
            Element crwmin ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 260
            
            """
            return _supy_driver.f90wrap_snow_prm__get__crwmin(self._handle)
        
        @crwmin.setter
        def crwmin(self, crwmin):
            _supy_driver.f90wrap_snow_prm__set__crwmin(self._handle, crwmin)
        
        @property
        def narp_emis_snow(self):
            """
            Element narp_emis_snow ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 261
            
            """
            return _supy_driver.f90wrap_snow_prm__get__narp_emis_snow(self._handle)
        
        @narp_emis_snow.setter
        def narp_emis_snow(self, narp_emis_snow):
            _supy_driver.f90wrap_snow_prm__set__narp_emis_snow(self._handle, narp_emis_snow)
        
        @property
        def preciplimit(self):
            """
            Element preciplimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 262
            
            """
            return _supy_driver.f90wrap_snow_prm__get__preciplimit(self._handle)
        
        @preciplimit.setter
        def preciplimit(self, preciplimit):
            _supy_driver.f90wrap_snow_prm__set__preciplimit(self._handle, preciplimit)
        
        @property
        def preciplimitalb(self):
            """
            Element preciplimitalb ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 263
            
            """
            return _supy_driver.f90wrap_snow_prm__get__preciplimitalb(self._handle)
        
        @preciplimitalb.setter
        def preciplimitalb(self, preciplimitalb):
            _supy_driver.f90wrap_snow_prm__set__preciplimitalb(self._handle, preciplimitalb)
        
        @property
        def snowalbmax(self):
            """
            Element snowalbmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 264
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowalbmax(self._handle)
        
        @snowalbmax.setter
        def snowalbmax(self, snowalbmax):
            _supy_driver.f90wrap_snow_prm__set__snowalbmax(self._handle, snowalbmax)
        
        @property
        def snowalbmin(self):
            """
            Element snowalbmin ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 265
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowalbmin(self._handle)
        
        @snowalbmin.setter
        def snowalbmin(self, snowalbmin):
            _supy_driver.f90wrap_snow_prm__set__snowalbmin(self._handle, snowalbmin)
        
        @property
        def snowdensmax(self):
            """
            Element snowdensmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 266
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowdensmax(self._handle)
        
        @snowdensmax.setter
        def snowdensmax(self, snowdensmax):
            _supy_driver.f90wrap_snow_prm__set__snowdensmax(self._handle, snowdensmax)
        
        @property
        def snowdensmin(self):
            """
            Element snowdensmin ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 267
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowdensmin(self._handle)
        
        @snowdensmin.setter
        def snowdensmin(self, snowdensmin):
            _supy_driver.f90wrap_snow_prm__set__snowdensmin(self._handle, snowdensmin)
        
        @property
        def snowlimbldg(self):
            """
            Element snowlimbldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 268
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowlimbldg(self._handle)
        
        @snowlimbldg.setter
        def snowlimbldg(self, snowlimbldg):
            _supy_driver.f90wrap_snow_prm__set__snowlimbldg(self._handle, snowlimbldg)
        
        @property
        def snowlimpaved(self):
            """
            Element snowlimpaved ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 269
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowlimpaved(self._handle)
        
        @snowlimpaved.setter
        def snowlimpaved(self, snowlimpaved):
            _supy_driver.f90wrap_snow_prm__set__snowlimpaved(self._handle, snowlimpaved)
        
        @property
        def snowpacklimit(self):
            """
            Element snowpacklimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 270
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_prm__array__snowpacklimit(self._handle)
            if array_handle in self._arrays:
                snowpacklimit = self._arrays[array_handle]
            else:
                snowpacklimit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_prm__array__snowpacklimit)
                self._arrays[array_handle] = snowpacklimit
            return snowpacklimit
        
        @snowpacklimit.setter
        def snowpacklimit(self, snowpacklimit):
            self.snowpacklimit[...] = snowpacklimit
        
        @property
        def snowprof_24hr_working(self):
            """
            Element snowprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 271
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                snowprof_24hr_working = self._arrays[array_handle]
            else:
                snowprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_working)
                self._arrays[array_handle] = snowprof_24hr_working
            return snowprof_24hr_working
        
        @snowprof_24hr_working.setter
        def snowprof_24hr_working(self, snowprof_24hr_working):
            self.snowprof_24hr_working[...] = snowprof_24hr_working
        
        @property
        def snowprof_24hr_holiday(self):
            """
            Element snowprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 272
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                snowprof_24hr_holiday = self._arrays[array_handle]
            else:
                snowprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_holiday)
                self._arrays[array_handle] = snowprof_24hr_holiday
            return snowprof_24hr_holiday
        
        @snowprof_24hr_holiday.setter
        def snowprof_24hr_holiday(self, snowprof_24hr_holiday):
            self.snowprof_24hr_holiday[...] = snowprof_24hr_holiday
        
        @property
        def tau_a(self):
            """
            Element tau_a ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 273
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tau_a(self._handle)
        
        @tau_a.setter
        def tau_a(self, tau_a):
            _supy_driver.f90wrap_snow_prm__set__tau_a(self._handle, tau_a)
        
        @property
        def tau_f(self):
            """
            Element tau_f ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 274
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tau_f(self._handle)
        
        @tau_f.setter
        def tau_f(self, tau_f):
            _supy_driver.f90wrap_snow_prm__set__tau_f(self._handle, tau_f)
        
        @property
        def tau_r(self):
            """
            Element tau_r ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 275
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tau_r(self._handle)
        
        @tau_r.setter
        def tau_r(self, tau_r):
            _supy_driver.f90wrap_snow_prm__set__tau_r(self._handle, tau_r)
        
        @property
        def tempmeltfact(self):
            """
            Element tempmeltfact ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 276
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tempmeltfact(self._handle)
        
        @tempmeltfact.setter
        def tempmeltfact(self, tempmeltfact):
            _supy_driver.f90wrap_snow_prm__set__tempmeltfact(self._handle, tempmeltfact)
        
        @property
        def radmeltfact(self):
            """
            Element radmeltfact ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 277
            
            """
            return _supy_driver.f90wrap_snow_prm__get__radmeltfact(self._handle)
        
        @radmeltfact.setter
        def radmeltfact(self, radmeltfact):
            _supy_driver.f90wrap_snow_prm__set__radmeltfact(self._handle, radmeltfact)
        
        def __str__(self):
            ret = ['<snow_prm>{\n']
            ret.append('    crwmax : ')
            ret.append(repr(self.crwmax))
            ret.append(',\n    crwmin : ')
            ret.append(repr(self.crwmin))
            ret.append(',\n    narp_emis_snow : ')
            ret.append(repr(self.narp_emis_snow))
            ret.append(',\n    preciplimit : ')
            ret.append(repr(self.preciplimit))
            ret.append(',\n    preciplimitalb : ')
            ret.append(repr(self.preciplimitalb))
            ret.append(',\n    snowalbmax : ')
            ret.append(repr(self.snowalbmax))
            ret.append(',\n    snowalbmin : ')
            ret.append(repr(self.snowalbmin))
            ret.append(',\n    snowdensmax : ')
            ret.append(repr(self.snowdensmax))
            ret.append(',\n    snowdensmin : ')
            ret.append(repr(self.snowdensmin))
            ret.append(',\n    snowlimbldg : ')
            ret.append(repr(self.snowlimbldg))
            ret.append(',\n    snowlimpaved : ')
            ret.append(repr(self.snowlimpaved))
            ret.append(',\n    snowpacklimit : ')
            ret.append(repr(self.snowpacklimit))
            ret.append(',\n    snowprof_24hr_working : ')
            ret.append(repr(self.snowprof_24hr_working))
            ret.append(',\n    snowprof_24hr_holiday : ')
            ret.append(repr(self.snowprof_24hr_holiday))
            ret.append(',\n    tau_a : ')
            ret.append(repr(self.tau_a))
            ret.append(',\n    tau_f : ')
            ret.append(repr(self.tau_f))
            ret.append(',\n    tau_r : ')
            ret.append(repr(self.tau_r))
            ret.append(',\n    tempmeltfact : ')
            ret.append(repr(self.tempmeltfact))
            ret.append(',\n    radmeltfact : ')
            ret.append(repr(self.radmeltfact))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SPARTACUS_PRM")
    class SPARTACUS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=spartacus_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 279-294
        
        """
        def __init__(self, handle=None):
            """
            self = Spartacus_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 279-294
            
            
            Returns
            -------
            this : Spartacus_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for spartacus_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_spartacus_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Spartacus_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 279-294
            
            Parameters
            ----------
            this : Spartacus_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for spartacus_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_spartacus_prm_finalise(this=self._handle)
        
        @property
        def air_ext_lw(self):
            """
            Element air_ext_lw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 280
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ext_lw(self._handle)
        
        @air_ext_lw.setter
        def air_ext_lw(self, air_ext_lw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ext_lw(self._handle, air_ext_lw)
        
        @property
        def air_ext_sw(self):
            """
            Element air_ext_sw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 281
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ext_sw(self._handle)
        
        @air_ext_sw.setter
        def air_ext_sw(self, air_ext_sw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ext_sw(self._handle, air_ext_sw)
        
        @property
        def air_ssa_lw(self):
            """
            Element air_ssa_lw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 282
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ssa_lw(self._handle)
        
        @air_ssa_lw.setter
        def air_ssa_lw(self, air_ssa_lw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ssa_lw(self._handle, air_ssa_lw)
        
        @property
        def air_ssa_sw(self):
            """
            Element air_ssa_sw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 283
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ssa_sw(self._handle)
        
        @air_ssa_sw.setter
        def air_ssa_sw(self, air_ssa_sw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ssa_sw(self._handle, air_ssa_sw)
        
        @property
        def height(self):
            """
            Element height ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 284
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_prm__array__height(self._handle)
            if array_handle in self._arrays:
                height = self._arrays[array_handle]
            else:
                height = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_prm__array__height)
                self._arrays[array_handle] = height
            return height
        
        @height.setter
        def height(self, height):
            self.height[...] = height
        
        @property
        def ground_albedo_dir_mult_fact(self):
            """
            Element ground_albedo_dir_mult_fact ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 285
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__ground_albedo_dir_mult_fact(self._handle)
        
        @ground_albedo_dir_mult_fact.setter
        def ground_albedo_dir_mult_fact(self, ground_albedo_dir_mult_fact):
            _supy_driver.f90wrap_spartacus_prm__set__ground_albedo_dir_mult_fact(self._handle, \
                ground_albedo_dir_mult_fact)
        
        @property
        def n_stream_lw_urban(self):
            """
            Element n_stream_lw_urban ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 286
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__n_stream_lw_urban(self._handle)
        
        @n_stream_lw_urban.setter
        def n_stream_lw_urban(self, n_stream_lw_urban):
            _supy_driver.f90wrap_spartacus_prm__set__n_stream_lw_urban(self._handle, \
                n_stream_lw_urban)
        
        @property
        def n_stream_sw_urban(self):
            """
            Element n_stream_sw_urban ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 287
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__n_stream_sw_urban(self._handle)
        
        @n_stream_sw_urban.setter
        def n_stream_sw_urban(self, n_stream_sw_urban):
            _supy_driver.f90wrap_spartacus_prm__set__n_stream_sw_urban(self._handle, \
                n_stream_sw_urban)
        
        @property
        def n_vegetation_region_urban(self):
            """
            Element n_vegetation_region_urban ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 288
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__n_vegetation_region_urban(self._handle)
        
        @n_vegetation_region_urban.setter
        def n_vegetation_region_urban(self, n_vegetation_region_urban):
            _supy_driver.f90wrap_spartacus_prm__set__n_vegetation_region_urban(self._handle, \
                n_vegetation_region_urban)
        
        @property
        def sw_dn_direct_frac(self):
            """
            Element sw_dn_direct_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 289
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__sw_dn_direct_frac(self._handle)
        
        @sw_dn_direct_frac.setter
        def sw_dn_direct_frac(self, sw_dn_direct_frac):
            _supy_driver.f90wrap_spartacus_prm__set__sw_dn_direct_frac(self._handle, \
                sw_dn_direct_frac)
        
        @property
        def use_sw_direct_albedo(self):
            """
            Element use_sw_direct_albedo ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 290
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__use_sw_direct_albedo(self._handle)
        
        @use_sw_direct_albedo.setter
        def use_sw_direct_albedo(self, use_sw_direct_albedo):
            _supy_driver.f90wrap_spartacus_prm__set__use_sw_direct_albedo(self._handle, \
                use_sw_direct_albedo)
        
        @property
        def veg_contact_fraction_const(self):
            """
            Element veg_contact_fraction_const ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 291
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__veg_contact_fraction_const(self._handle)
        
        @veg_contact_fraction_const.setter
        def veg_contact_fraction_const(self, veg_contact_fraction_const):
            _supy_driver.f90wrap_spartacus_prm__set__veg_contact_fraction_const(self._handle, \
                veg_contact_fraction_const)
        
        @property
        def veg_fsd_const(self):
            """
            Element veg_fsd_const ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 292
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__veg_fsd_const(self._handle)
        
        @veg_fsd_const.setter
        def veg_fsd_const(self, veg_fsd_const):
            _supy_driver.f90wrap_spartacus_prm__set__veg_fsd_const(self._handle, \
                veg_fsd_const)
        
        @property
        def veg_ssa_lw(self):
            """
            Element veg_ssa_lw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 293
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__veg_ssa_lw(self._handle)
        
        @veg_ssa_lw.setter
        def veg_ssa_lw(self, veg_ssa_lw):
            _supy_driver.f90wrap_spartacus_prm__set__veg_ssa_lw(self._handle, veg_ssa_lw)
        
        @property
        def veg_ssa_sw(self):
            """
            Element veg_ssa_sw ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 294
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__veg_ssa_sw(self._handle)
        
        @veg_ssa_sw.setter
        def veg_ssa_sw(self, veg_ssa_sw):
            _supy_driver.f90wrap_spartacus_prm__set__veg_ssa_sw(self._handle, veg_ssa_sw)
        
        def __str__(self):
            ret = ['<spartacus_prm>{\n']
            ret.append('    air_ext_lw : ')
            ret.append(repr(self.air_ext_lw))
            ret.append(',\n    air_ext_sw : ')
            ret.append(repr(self.air_ext_sw))
            ret.append(',\n    air_ssa_lw : ')
            ret.append(repr(self.air_ssa_lw))
            ret.append(',\n    air_ssa_sw : ')
            ret.append(repr(self.air_ssa_sw))
            ret.append(',\n    height : ')
            ret.append(repr(self.height))
            ret.append(',\n    ground_albedo_dir_mult_fact : ')
            ret.append(repr(self.ground_albedo_dir_mult_fact))
            ret.append(',\n    n_stream_lw_urban : ')
            ret.append(repr(self.n_stream_lw_urban))
            ret.append(',\n    n_stream_sw_urban : ')
            ret.append(repr(self.n_stream_sw_urban))
            ret.append(',\n    n_vegetation_region_urban : ')
            ret.append(repr(self.n_vegetation_region_urban))
            ret.append(',\n    sw_dn_direct_frac : ')
            ret.append(repr(self.sw_dn_direct_frac))
            ret.append(',\n    use_sw_direct_albedo : ')
            ret.append(repr(self.use_sw_direct_albedo))
            ret.append(',\n    veg_contact_fraction_const : ')
            ret.append(repr(self.veg_contact_fraction_const))
            ret.append(',\n    veg_fsd_const : ')
            ret.append(repr(self.veg_fsd_const))
            ret.append(',\n    veg_ssa_lw : ')
            ret.append(repr(self.veg_ssa_lw))
            ret.append(',\n    veg_ssa_sw : ')
            ret.append(repr(self.veg_ssa_sw))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SPARTACUS_LAYER_PRM")
    class SPARTACUS_LAYER_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=spartacus_layer_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 296-306
        
        """
        def __init__(self, handle=None):
            """
            self = Spartacus_Layer_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 296-306
            
            
            Returns
            -------
            this : Spartacus_Layer_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for spartacus_layer_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_spartacus_layer_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Spartacus_Layer_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 296-306
            
            Parameters
            ----------
            this : Spartacus_Layer_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for spartacus_layer_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_spartacus_layer_prm_finalise(this=self._handle)
        
        @property
        def building_frac(self):
            """
            Element building_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 297
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__building_frac(self._handle)
            if array_handle in self._arrays:
                building_frac = self._arrays[array_handle]
            else:
                building_frac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__building_frac)
                self._arrays[array_handle] = building_frac
            return building_frac
        
        @building_frac.setter
        def building_frac(self, building_frac):
            self.building_frac[...] = building_frac
        
        @property
        def building_scale(self):
            """
            Element building_scale ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 298
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__building_scale(self._handle)
            if array_handle in self._arrays:
                building_scale = self._arrays[array_handle]
            else:
                building_scale = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__building_scale)
                self._arrays[array_handle] = building_scale
            return building_scale
        
        @building_scale.setter
        def building_scale(self, building_scale):
            self.building_scale[...] = building_scale
        
        @property
        def veg_frac(self):
            """
            Element veg_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 299
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__veg_frac(self._handle)
            if array_handle in self._arrays:
                veg_frac = self._arrays[array_handle]
            else:
                veg_frac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__veg_frac)
                self._arrays[array_handle] = veg_frac
            return veg_frac
        
        @veg_frac.setter
        def veg_frac(self, veg_frac):
            self.veg_frac[...] = veg_frac
        
        @property
        def veg_scale(self):
            """
            Element veg_scale ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 300
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__veg_scale(self._handle)
            if array_handle in self._arrays:
                veg_scale = self._arrays[array_handle]
            else:
                veg_scale = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__veg_scale)
                self._arrays[array_handle] = veg_scale
            return veg_scale
        
        @veg_scale.setter
        def veg_scale(self, veg_scale):
            self.veg_scale[...] = veg_scale
        
        @property
        def alb_roof(self):
            """
            Element alb_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 301
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__alb_roof(self._handle)
            if array_handle in self._arrays:
                alb_roof = self._arrays[array_handle]
            else:
                alb_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__alb_roof)
                self._arrays[array_handle] = alb_roof
            return alb_roof
        
        @alb_roof.setter
        def alb_roof(self, alb_roof):
            self.alb_roof[...] = alb_roof
        
        @property
        def emis_roof(self):
            """
            Element emis_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 302
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__emis_roof(self._handle)
            if array_handle in self._arrays:
                emis_roof = self._arrays[array_handle]
            else:
                emis_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__emis_roof)
                self._arrays[array_handle] = emis_roof
            return emis_roof
        
        @emis_roof.setter
        def emis_roof(self, emis_roof):
            self.emis_roof[...] = emis_roof
        
        @property
        def alb_wall(self):
            """
            Element alb_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 303
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__alb_wall(self._handle)
            if array_handle in self._arrays:
                alb_wall = self._arrays[array_handle]
            else:
                alb_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__alb_wall)
                self._arrays[array_handle] = alb_wall
            return alb_wall
        
        @alb_wall.setter
        def alb_wall(self, alb_wall):
            self.alb_wall[...] = alb_wall
        
        @property
        def emis_wall(self):
            """
            Element emis_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 304
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__emis_wall(self._handle)
            if array_handle in self._arrays:
                emis_wall = self._arrays[array_handle]
            else:
                emis_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__emis_wall)
                self._arrays[array_handle] = emis_wall
            return emis_wall
        
        @emis_wall.setter
        def emis_wall(self, emis_wall):
            self.emis_wall[...] = emis_wall
        
        @property
        def roof_albedo_dir_mult_fact(self):
            """
            Element roof_albedo_dir_mult_fact ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 305
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__roof_albedo_dir_mult_fact(self._handle)
            if array_handle in self._arrays:
                roof_albedo_dir_mult_fact = self._arrays[array_handle]
            else:
                roof_albedo_dir_mult_fact = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__roof_albedo_dir_mult_fact)
                self._arrays[array_handle] = roof_albedo_dir_mult_fact
            return roof_albedo_dir_mult_fact
        
        @roof_albedo_dir_mult_fact.setter
        def roof_albedo_dir_mult_fact(self, roof_albedo_dir_mult_fact):
            self.roof_albedo_dir_mult_fact[...] = roof_albedo_dir_mult_fact
        
        @property
        def wall_specular_frac(self):
            """
            Element wall_specular_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 306
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__wall_specular_frac(self._handle)
            if array_handle in self._arrays:
                wall_specular_frac = self._arrays[array_handle]
            else:
                wall_specular_frac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__wall_specular_frac)
                self._arrays[array_handle] = wall_specular_frac
            return wall_specular_frac
        
        @wall_specular_frac.setter
        def wall_specular_frac(self, wall_specular_frac):
            self.wall_specular_frac[...] = wall_specular_frac
        
        def __str__(self):
            ret = ['<spartacus_layer_prm>{\n']
            ret.append('    building_frac : ')
            ret.append(repr(self.building_frac))
            ret.append(',\n    building_scale : ')
            ret.append(repr(self.building_scale))
            ret.append(',\n    veg_frac : ')
            ret.append(repr(self.veg_frac))
            ret.append(',\n    veg_scale : ')
            ret.append(repr(self.veg_scale))
            ret.append(',\n    alb_roof : ')
            ret.append(repr(self.alb_roof))
            ret.append(',\n    emis_roof : ')
            ret.append(repr(self.emis_roof))
            ret.append(',\n    alb_wall : ')
            ret.append(repr(self.alb_wall))
            ret.append(',\n    emis_wall : ')
            ret.append(repr(self.emis_wall))
            ret.append(',\n    roof_albedo_dir_mult_fact : ')
            ret.append(repr(self.roof_albedo_dir_mult_fact))
            ret.append(',\n    wall_specular_frac : ')
            ret.append(repr(self.wall_specular_frac))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SITE_PRM")
    class SITE_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=site_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 309-323
        
        """
        def __init__(self, handle=None):
            """
            self = Site_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 309-323
            
            
            Returns
            -------
            this : Site_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for site_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_site_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Site_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 309-323
            
            Parameters
            ----------
            this : Site_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for site_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_site_prm_finalise(this=self._handle)
        
        @property
        def lat(self):
            """
            Element lat ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 310
            
            """
            return _supy_driver.f90wrap_site_prm__get__lat(self._handle)
        
        @lat.setter
        def lat(self, lat):
            _supy_driver.f90wrap_site_prm__set__lat(self._handle, lat)
        
        @property
        def lon(self):
            """
            Element lon ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 311
            
            """
            return _supy_driver.f90wrap_site_prm__get__lon(self._handle)
        
        @lon.setter
        def lon(self, lon):
            _supy_driver.f90wrap_site_prm__set__lon(self._handle, lon)
        
        @property
        def alt(self):
            """
            Element alt ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 312
            
            """
            return _supy_driver.f90wrap_site_prm__get__alt(self._handle)
        
        @alt.setter
        def alt(self, alt):
            _supy_driver.f90wrap_site_prm__set__alt(self._handle, alt)
        
        @property
        def gridiv(self):
            """
            Element gridiv ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 313
            
            """
            return _supy_driver.f90wrap_site_prm__get__gridiv(self._handle)
        
        @gridiv.setter
        def gridiv(self, gridiv):
            _supy_driver.f90wrap_site_prm__set__gridiv(self._handle, gridiv)
        
        @property
        def timezone(self):
            """
            Element timezone ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 314
            
            """
            return _supy_driver.f90wrap_site_prm__get__timezone(self._handle)
        
        @timezone.setter
        def timezone(self, timezone):
            _supy_driver.f90wrap_site_prm__set__timezone(self._handle, timezone)
        
        @property
        def surfacearea(self):
            """
            Element surfacearea ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 315
            
            """
            return _supy_driver.f90wrap_site_prm__get__surfacearea(self._handle)
        
        @surfacearea.setter
        def surfacearea(self, surfacearea):
            _supy_driver.f90wrap_site_prm__set__surfacearea(self._handle, surfacearea)
        
        @property
        def z(self):
            """
            Element z ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 316
            
            """
            return _supy_driver.f90wrap_site_prm__get__z(self._handle)
        
        @z.setter
        def z(self, z):
            _supy_driver.f90wrap_site_prm__set__z(self._handle, z)
        
        @property
        def z0m_in(self):
            """
            Element z0m_in ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 317
            
            """
            return _supy_driver.f90wrap_site_prm__get__z0m_in(self._handle)
        
        @z0m_in.setter
        def z0m_in(self, z0m_in):
            _supy_driver.f90wrap_site_prm__set__z0m_in(self._handle, z0m_in)
        
        @property
        def zdm_in(self):
            """
            Element zdm_in ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 318
            
            """
            return _supy_driver.f90wrap_site_prm__get__zdm_in(self._handle)
        
        @zdm_in.setter
        def zdm_in(self, zdm_in):
            _supy_driver.f90wrap_site_prm__set__zdm_in(self._handle, zdm_in)
        
        @property
        def pipecapacity(self):
            """
            Element pipecapacity ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 319
            
            """
            return _supy_driver.f90wrap_site_prm__get__pipecapacity(self._handle)
        
        @pipecapacity.setter
        def pipecapacity(self, pipecapacity):
            _supy_driver.f90wrap_site_prm__set__pipecapacity(self._handle, pipecapacity)
        
        @property
        def runofftowater(self):
            """
            Element runofftowater ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 320
            
            """
            return _supy_driver.f90wrap_site_prm__get__runofftowater(self._handle)
        
        @runofftowater.setter
        def runofftowater(self, runofftowater):
            _supy_driver.f90wrap_site_prm__set__runofftowater(self._handle, runofftowater)
        
        @property
        def narp_trans_site(self):
            """
            Element narp_trans_site ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 321
            
            """
            return _supy_driver.f90wrap_site_prm__get__narp_trans_site(self._handle)
        
        @narp_trans_site.setter
        def narp_trans_site(self, narp_trans_site):
            _supy_driver.f90wrap_site_prm__set__narp_trans_site(self._handle, \
                narp_trans_site)
        
        @property
        def co2pointsource(self):
            """
            Element co2pointsource ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 322
            
            """
            return _supy_driver.f90wrap_site_prm__get__co2pointsource(self._handle)
        
        @co2pointsource.setter
        def co2pointsource(self, co2pointsource):
            _supy_driver.f90wrap_site_prm__set__co2pointsource(self._handle, co2pointsource)
        
        @property
        def flowchange(self):
            """
            Element flowchange ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 323
            
            """
            return _supy_driver.f90wrap_site_prm__get__flowchange(self._handle)
        
        @flowchange.setter
        def flowchange(self, flowchange):
            _supy_driver.f90wrap_site_prm__set__flowchange(self._handle, flowchange)
        
        def __str__(self):
            ret = ['<site_prm>{\n']
            ret.append('    lat : ')
            ret.append(repr(self.lat))
            ret.append(',\n    lon : ')
            ret.append(repr(self.lon))
            ret.append(',\n    alt : ')
            ret.append(repr(self.alt))
            ret.append(',\n    gridiv : ')
            ret.append(repr(self.gridiv))
            ret.append(',\n    timezone : ')
            ret.append(repr(self.timezone))
            ret.append(',\n    surfacearea : ')
            ret.append(repr(self.surfacearea))
            ret.append(',\n    z : ')
            ret.append(repr(self.z))
            ret.append(',\n    z0m_in : ')
            ret.append(repr(self.z0m_in))
            ret.append(',\n    zdm_in : ')
            ret.append(repr(self.zdm_in))
            ret.append(',\n    pipecapacity : ')
            ret.append(repr(self.pipecapacity))
            ret.append(',\n    runofftowater : ')
            ret.append(repr(self.runofftowater))
            ret.append(',\n    narp_trans_site : ')
            ret.append(repr(self.narp_trans_site))
            ret.append(',\n    co2pointsource : ')
            ret.append(repr(self.co2pointsource))
            ret.append(',\n    flowchange : ')
            ret.append(repr(self.flowchange))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LUMPS_PRM")
    class LUMPS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lumps_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 325-329
        
        """
        def __init__(self, handle=None):
            """
            self = Lumps_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 325-329
            
            
            Returns
            -------
            this : Lumps_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lumps_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lumps_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lumps_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 325-329
            
            Parameters
            ----------
            this : Lumps_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lumps_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lumps_prm_finalise(this=self._handle)
        
        @property
        def raincover(self):
            """
            Element raincover ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 326
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__raincover(self._handle)
        
        @raincover.setter
        def raincover(self, raincover):
            _supy_driver.f90wrap_lumps_prm__set__raincover(self._handle, raincover)
        
        @property
        def rainmaxres(self):
            """
            Element rainmaxres ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 327
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__rainmaxres(self._handle)
        
        @rainmaxres.setter
        def rainmaxres(self, rainmaxres):
            _supy_driver.f90wrap_lumps_prm__set__rainmaxres(self._handle, rainmaxres)
        
        @property
        def drainrt(self):
            """
            Element drainrt ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 328
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__drainrt(self._handle)
        
        @drainrt.setter
        def drainrt(self, drainrt):
            _supy_driver.f90wrap_lumps_prm__set__drainrt(self._handle, drainrt)
        
        @property
        def veg_type(self):
            """
            Element veg_type ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 329
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__veg_type(self._handle)
        
        @veg_type.setter
        def veg_type(self, veg_type):
            _supy_driver.f90wrap_lumps_prm__set__veg_type(self._handle, veg_type)
        
        def __str__(self):
            ret = ['<lumps_prm>{\n']
            ret.append('    raincover : ')
            ret.append(repr(self.raincover))
            ret.append(',\n    rainmaxres : ')
            ret.append(repr(self.rainmaxres))
            ret.append(',\n    drainrt : ')
            ret.append(repr(self.drainrt))
            ret.append(',\n    veg_type : ')
            ret.append(repr(self.veg_type))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.EHC_PRM")
    class EHC_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ehc_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 331-349
        
        """
        def __init__(self, handle=None):
            """
            self = Ehc_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 331-349
            
            
            Returns
            -------
            this : Ehc_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for ehc_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_ehc_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ehc_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 331-349
            
            Parameters
            ----------
            this : Ehc_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for ehc_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_ehc_prm_finalise(this=self._handle)
        
        @property
        def soil_storecap_roof(self):
            """
            Element soil_storecap_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 332
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__soil_storecap_roof(self._handle)
            if array_handle in self._arrays:
                soil_storecap_roof = self._arrays[array_handle]
            else:
                soil_storecap_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__soil_storecap_roof)
                self._arrays[array_handle] = soil_storecap_roof
            return soil_storecap_roof
        
        @soil_storecap_roof.setter
        def soil_storecap_roof(self, soil_storecap_roof):
            self.soil_storecap_roof[...] = soil_storecap_roof
        
        @property
        def soil_storecap_wall(self):
            """
            Element soil_storecap_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 333
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__soil_storecap_wall(self._handle)
            if array_handle in self._arrays:
                soil_storecap_wall = self._arrays[array_handle]
            else:
                soil_storecap_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__soil_storecap_wall)
                self._arrays[array_handle] = soil_storecap_wall
            return soil_storecap_wall
        
        @soil_storecap_wall.setter
        def soil_storecap_wall(self, soil_storecap_wall):
            self.soil_storecap_wall[...] = soil_storecap_wall
        
        @property
        def state_limit_roof(self):
            """
            Element state_limit_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 334
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__state_limit_roof(self._handle)
            if array_handle in self._arrays:
                state_limit_roof = self._arrays[array_handle]
            else:
                state_limit_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__state_limit_roof)
                self._arrays[array_handle] = state_limit_roof
            return state_limit_roof
        
        @state_limit_roof.setter
        def state_limit_roof(self, state_limit_roof):
            self.state_limit_roof[...] = state_limit_roof
        
        @property
        def state_limit_wall(self):
            """
            Element state_limit_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 335
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__state_limit_wall(self._handle)
            if array_handle in self._arrays:
                state_limit_wall = self._arrays[array_handle]
            else:
                state_limit_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__state_limit_wall)
                self._arrays[array_handle] = state_limit_wall
            return state_limit_wall
        
        @state_limit_wall.setter
        def state_limit_wall(self, state_limit_wall):
            self.state_limit_wall[...] = state_limit_wall
        
        @property
        def wet_thresh_roof(self):
            """
            Element wet_thresh_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 336
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__wet_thresh_roof(self._handle)
            if array_handle in self._arrays:
                wet_thresh_roof = self._arrays[array_handle]
            else:
                wet_thresh_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__wet_thresh_roof)
                self._arrays[array_handle] = wet_thresh_roof
            return wet_thresh_roof
        
        @wet_thresh_roof.setter
        def wet_thresh_roof(self, wet_thresh_roof):
            self.wet_thresh_roof[...] = wet_thresh_roof
        
        @property
        def wet_thresh_wall(self):
            """
            Element wet_thresh_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 337
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__wet_thresh_wall(self._handle)
            if array_handle in self._arrays:
                wet_thresh_wall = self._arrays[array_handle]
            else:
                wet_thresh_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__wet_thresh_wall)
                self._arrays[array_handle] = wet_thresh_wall
            return wet_thresh_wall
        
        @wet_thresh_wall.setter
        def wet_thresh_wall(self, wet_thresh_wall):
            self.wet_thresh_wall[...] = wet_thresh_wall
        
        @property
        def tin_roof(self):
            """
            Element tin_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 338
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__tin_roof(self._handle)
            if array_handle in self._arrays:
                tin_roof = self._arrays[array_handle]
            else:
                tin_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__tin_roof)
                self._arrays[array_handle] = tin_roof
            return tin_roof
        
        @tin_roof.setter
        def tin_roof(self, tin_roof):
            self.tin_roof[...] = tin_roof
        
        @property
        def tin_wall(self):
            """
            Element tin_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 339
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__tin_wall(self._handle)
            if array_handle in self._arrays:
                tin_wall = self._arrays[array_handle]
            else:
                tin_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__tin_wall)
                self._arrays[array_handle] = tin_wall
            return tin_wall
        
        @tin_wall.setter
        def tin_wall(self, tin_wall):
            self.tin_wall[...] = tin_wall
        
        @property
        def tin_surf(self):
            """
            Element tin_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 340
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__tin_surf(self._handle)
            if array_handle in self._arrays:
                tin_surf = self._arrays[array_handle]
            else:
                tin_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__tin_surf)
                self._arrays[array_handle] = tin_surf
            return tin_surf
        
        @tin_surf.setter
        def tin_surf(self, tin_surf):
            self.tin_surf[...] = tin_surf
        
        @property
        def k_roof(self):
            """
            Element k_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 341
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__k_roof(self._handle)
            if array_handle in self._arrays:
                k_roof = self._arrays[array_handle]
            else:
                k_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__k_roof)
                self._arrays[array_handle] = k_roof
            return k_roof
        
        @k_roof.setter
        def k_roof(self, k_roof):
            self.k_roof[...] = k_roof
        
        @property
        def k_wall(self):
            """
            Element k_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 342
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__k_wall(self._handle)
            if array_handle in self._arrays:
                k_wall = self._arrays[array_handle]
            else:
                k_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__k_wall)
                self._arrays[array_handle] = k_wall
            return k_wall
        
        @k_wall.setter
        def k_wall(self, k_wall):
            self.k_wall[...] = k_wall
        
        @property
        def k_surf(self):
            """
            Element k_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 343
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__k_surf(self._handle)
            if array_handle in self._arrays:
                k_surf = self._arrays[array_handle]
            else:
                k_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__k_surf)
                self._arrays[array_handle] = k_surf
            return k_surf
        
        @k_surf.setter
        def k_surf(self, k_surf):
            self.k_surf[...] = k_surf
        
        @property
        def cp_roof(self):
            """
            Element cp_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 344
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__cp_roof(self._handle)
            if array_handle in self._arrays:
                cp_roof = self._arrays[array_handle]
            else:
                cp_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__cp_roof)
                self._arrays[array_handle] = cp_roof
            return cp_roof
        
        @cp_roof.setter
        def cp_roof(self, cp_roof):
            self.cp_roof[...] = cp_roof
        
        @property
        def cp_wall(self):
            """
            Element cp_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 345
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__cp_wall(self._handle)
            if array_handle in self._arrays:
                cp_wall = self._arrays[array_handle]
            else:
                cp_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__cp_wall)
                self._arrays[array_handle] = cp_wall
            return cp_wall
        
        @cp_wall.setter
        def cp_wall(self, cp_wall):
            self.cp_wall[...] = cp_wall
        
        @property
        def cp_surf(self):
            """
            Element cp_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 346
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__cp_surf(self._handle)
            if array_handle in self._arrays:
                cp_surf = self._arrays[array_handle]
            else:
                cp_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__cp_surf)
                self._arrays[array_handle] = cp_surf
            return cp_surf
        
        @cp_surf.setter
        def cp_surf(self, cp_surf):
            self.cp_surf[...] = cp_surf
        
        @property
        def dz_roof(self):
            """
            Element dz_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 347
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__dz_roof(self._handle)
            if array_handle in self._arrays:
                dz_roof = self._arrays[array_handle]
            else:
                dz_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__dz_roof)
                self._arrays[array_handle] = dz_roof
            return dz_roof
        
        @dz_roof.setter
        def dz_roof(self, dz_roof):
            self.dz_roof[...] = dz_roof
        
        @property
        def dz_wall(self):
            """
            Element dz_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 348
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__dz_wall(self._handle)
            if array_handle in self._arrays:
                dz_wall = self._arrays[array_handle]
            else:
                dz_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__dz_wall)
                self._arrays[array_handle] = dz_wall
            return dz_wall
        
        @dz_wall.setter
        def dz_wall(self, dz_wall):
            self.dz_wall[...] = dz_wall
        
        @property
        def dz_surf(self):
            """
            Element dz_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 349
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__dz_surf(self._handle)
            if array_handle in self._arrays:
                dz_surf = self._arrays[array_handle]
            else:
                dz_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__dz_surf)
                self._arrays[array_handle] = dz_surf
            return dz_surf
        
        @dz_surf.setter
        def dz_surf(self, dz_surf):
            self.dz_surf[...] = dz_surf
        
        def __str__(self):
            ret = ['<ehc_prm>{\n']
            ret.append('    soil_storecap_roof : ')
            ret.append(repr(self.soil_storecap_roof))
            ret.append(',\n    soil_storecap_wall : ')
            ret.append(repr(self.soil_storecap_wall))
            ret.append(',\n    state_limit_roof : ')
            ret.append(repr(self.state_limit_roof))
            ret.append(',\n    state_limit_wall : ')
            ret.append(repr(self.state_limit_wall))
            ret.append(',\n    wet_thresh_roof : ')
            ret.append(repr(self.wet_thresh_roof))
            ret.append(',\n    wet_thresh_wall : ')
            ret.append(repr(self.wet_thresh_wall))
            ret.append(',\n    tin_roof : ')
            ret.append(repr(self.tin_roof))
            ret.append(',\n    tin_wall : ')
            ret.append(repr(self.tin_wall))
            ret.append(',\n    tin_surf : ')
            ret.append(repr(self.tin_surf))
            ret.append(',\n    k_roof : ')
            ret.append(repr(self.k_roof))
            ret.append(',\n    k_wall : ')
            ret.append(repr(self.k_wall))
            ret.append(',\n    k_surf : ')
            ret.append(repr(self.k_surf))
            ret.append(',\n    cp_roof : ')
            ret.append(repr(self.cp_roof))
            ret.append(',\n    cp_wall : ')
            ret.append(repr(self.cp_wall))
            ret.append(',\n    cp_surf : ')
            ret.append(repr(self.cp_surf))
            ret.append(',\n    dz_roof : ')
            ret.append(repr(self.dz_roof))
            ret.append(',\n    dz_wall : ')
            ret.append(repr(self.dz_wall))
            ret.append(',\n    dz_surf : ')
            ret.append(repr(self.dz_surf))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_PAVED_PRM")
    class LC_PAVED_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_paved_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 351-360
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Paved_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 351-360
            
            
            Returns
            -------
            this : Lc_Paved_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_paved_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_paved_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Paved_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 351-360
            
            Parameters
            ----------
            this : Lc_Paved_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_paved_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_paved_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 352
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_paved_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 353
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_paved_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 354
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_paved_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_paved_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 355
            
            """
            soil_handle = _supy_driver.f90wrap_lc_paved_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_paved_prm__set__soil(self._handle, soil)
        
        @property
        def state(self):
            """
            Element state ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 356
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__state(self._handle)
        
        @state.setter
        def state(self, state):
            _supy_driver.f90wrap_lc_paved_prm__set__state(self._handle, state)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 357
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_paved_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracpaved(self):
            """
            Element irrfracpaved ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 358
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__irrfracpaved(self._handle)
        
        @irrfracpaved.setter
        def irrfracpaved(self, irrfracpaved):
            _supy_driver.f90wrap_lc_paved_prm__set__irrfracpaved(self._handle, irrfracpaved)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 359
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_paved_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 360
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_paved_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_driver.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_paved_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_paved_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    state : ')
            ret.append(repr(self.state))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracpaved : ')
            ret.append(repr(self.irrfracpaved))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_BLDG_PRM")
    class LC_BLDG_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_bldg_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 362-373
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Bldg_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 362-373
            
            
            Returns
            -------
            this : Lc_Bldg_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_bldg_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_bldg_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Bldg_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 362-373
            
            Parameters
            ----------
            this : Lc_Bldg_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_bldg_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_bldg_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 363
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_bldg_prm__set__sfr(self._handle, sfr)
        
        @property
        def faibldg(self):
            """
            Element faibldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 364
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__faibldg(self._handle)
        
        @faibldg.setter
        def faibldg(self, faibldg):
            _supy_driver.f90wrap_lc_bldg_prm__set__faibldg(self._handle, faibldg)
        
        @property
        def bldgh(self):
            """
            Element bldgh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 365
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__bldgh(self._handle)
        
        @bldgh.setter
        def bldgh(self, bldgh):
            _supy_driver.f90wrap_lc_bldg_prm__set__bldgh(self._handle, bldgh)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 366
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_bldg_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 367
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_bldg_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_bldg_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 368
            
            """
            soil_handle = _supy_driver.f90wrap_lc_bldg_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_bldg_prm__set__soil(self._handle, soil)
        
        @property
        def state(self):
            """
            Element state ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 369
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__state(self._handle)
        
        @state.setter
        def state(self, state):
            _supy_driver.f90wrap_lc_bldg_prm__set__state(self._handle, state)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 370
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_bldg_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracbldgs(self):
            """
            Element irrfracbldgs ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 371
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__irrfracbldgs(self._handle)
        
        @irrfracbldgs.setter
        def irrfracbldgs(self, irrfracbldgs):
            _supy_driver.f90wrap_lc_bldg_prm__set__irrfracbldgs(self._handle, irrfracbldgs)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 372
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_bldg_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 373
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_bldg_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_driver.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_bldg_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_bldg_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    faibldg : ')
            ret.append(repr(self.faibldg))
            ret.append(',\n    bldgh : ')
            ret.append(repr(self.bldgh))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    state : ')
            ret.append(repr(self.state))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracbldgs : ')
            ret.append(repr(self.irrfracbldgs))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_DECTR_PRM")
    class LC_DECTR_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_dectr_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 375-395
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Dectr_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 375-395
            
            
            Returns
            -------
            this : Lc_Dectr_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_dectr_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_dectr_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Dectr_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 375-395
            
            Parameters
            ----------
            this : Lc_Dectr_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_dectr_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_dectr_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 376
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_dectr_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 377
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_dectr_prm__set__emis(self._handle, emis)
        
        @property
        def faidectree(self):
            """
            Element faidectree ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 378
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__faidectree(self._handle)
        
        @faidectree.setter
        def faidectree(self, faidectree):
            _supy_driver.f90wrap_lc_dectr_prm__set__faidectree(self._handle, faidectree)
        
        @property
        def dectreeh(self):
            """
            Element dectreeh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 379
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__dectreeh(self._handle)
        
        @dectreeh.setter
        def dectreeh(self, dectreeh):
            _supy_driver.f90wrap_lc_dectr_prm__set__dectreeh(self._handle, dectreeh)
        
        @property
        def pormin_dec(self):
            """
            Element pormin_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 380
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__pormin_dec(self._handle)
        
        @pormin_dec.setter
        def pormin_dec(self, pormin_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__pormin_dec(self._handle, pormin_dec)
        
        @property
        def pormax_dec(self):
            """
            Element pormax_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 381
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__pormax_dec(self._handle)
        
        @pormax_dec.setter
        def pormax_dec(self, pormax_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__pormax_dec(self._handle, pormax_dec)
        
        @property
        def alb_min(self):
            """
            Element alb_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 382
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__alb_min(self._handle)
        
        @alb_min.setter
        def alb_min(self, alb_min):
            _supy_driver.f90wrap_lc_dectr_prm__set__alb_min(self._handle, alb_min)
        
        @property
        def alb_max(self):
            """
            Element alb_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 383
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__alb_max(self._handle)
        
        @alb_max.setter
        def alb_max(self, alb_max):
            _supy_driver.f90wrap_lc_dectr_prm__set__alb_max(self._handle, alb_max)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 384
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_dectr_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 385
            
            """
            soil_handle = _supy_driver.f90wrap_lc_dectr_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 386
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_dectr_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def capmax_dec(self):
            """
            Element capmax_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 387
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__capmax_dec(self._handle)
        
        @capmax_dec.setter
        def capmax_dec(self, capmax_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__capmax_dec(self._handle, capmax_dec)
        
        @property
        def capmin_dec(self):
            """
            Element capmin_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 388
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__capmin_dec(self._handle)
        
        @capmin_dec.setter
        def capmin_dec(self, capmin_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__capmin_dec(self._handle, capmin_dec)
        
        @property
        def irrfracdectr(self):
            """
            Element irrfracdectr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 389
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__irrfracdectr(self._handle)
        
        @irrfracdectr.setter
        def irrfracdectr(self, irrfracdectr):
            _supy_driver.f90wrap_lc_dectr_prm__set__irrfracdectr(self._handle, irrfracdectr)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 390
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_dectr_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def bioco2(self):
            """
            Element bioco2 ftype=type(bioco2_prm) pytype=Bioco2_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 391
            
            """
            bioco2_handle = _supy_driver.f90wrap_lc_dectr_prm__get__bioco2(self._handle)
            if tuple(bioco2_handle) in self._objs:
                bioco2 = self._objs[tuple(bioco2_handle)]
            else:
                bioco2 = suews_driver.bioCO2_PRM.from_handle(bioco2_handle)
                self._objs[tuple(bioco2_handle)] = bioco2
            return bioco2
        
        @bioco2.setter
        def bioco2(self, bioco2):
            bioco2 = bioco2._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__bioco2(self._handle, bioco2)
        
        @property
        def maxconductance(self):
            """
            Element maxconductance ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 392
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__maxconductance(self._handle)
        
        @maxconductance.setter
        def maxconductance(self, maxconductance):
            _supy_driver.f90wrap_lc_dectr_prm__set__maxconductance(self._handle, \
                maxconductance)
        
        @property
        def lai(self):
            """
            Element lai ftype=type(lai_prm) pytype=Lai_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 394
            
            """
            lai_handle = _supy_driver.f90wrap_lc_dectr_prm__get__lai(self._handle)
            if tuple(lai_handle) in self._objs:
                lai = self._objs[tuple(lai_handle)]
            else:
                lai = suews_driver.LAI_PRM.from_handle(lai_handle)
                self._objs[tuple(lai_handle)] = lai
            return lai
        
        @lai.setter
        def lai(self, lai):
            lai = lai._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__lai(self._handle, lai)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 395
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_dectr_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_driver.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_dectr_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    faidectree : ')
            ret.append(repr(self.faidectree))
            ret.append(',\n    dectreeh : ')
            ret.append(repr(self.dectreeh))
            ret.append(',\n    pormin_dec : ')
            ret.append(repr(self.pormin_dec))
            ret.append(',\n    pormax_dec : ')
            ret.append(repr(self.pormax_dec))
            ret.append(',\n    alb_min : ')
            ret.append(repr(self.alb_min))
            ret.append(',\n    alb_max : ')
            ret.append(repr(self.alb_max))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    capmax_dec : ')
            ret.append(repr(self.capmax_dec))
            ret.append(',\n    capmin_dec : ')
            ret.append(repr(self.capmin_dec))
            ret.append(',\n    irrfracdectr : ')
            ret.append(repr(self.irrfracdectr))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    bioco2 : ')
            ret.append(repr(self.bioco2))
            ret.append(',\n    maxconductance : ')
            ret.append(repr(self.maxconductance))
            ret.append(',\n    lai : ')
            ret.append(repr(self.lai))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_EVETR_PRM")
    class LC_EVETR_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_evetr_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 397-413
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Evetr_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 397-413
            
            
            Returns
            -------
            this : Lc_Evetr_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_evetr_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_evetr_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Evetr_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 397-413
            
            Parameters
            ----------
            this : Lc_Evetr_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_evetr_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_evetr_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 398
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_evetr_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 399
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_evetr_prm__set__emis(self._handle, emis)
        
        @property
        def faievetree(self):
            """
            Element faievetree ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 400
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__faievetree(self._handle)
        
        @faievetree.setter
        def faievetree(self, faievetree):
            _supy_driver.f90wrap_lc_evetr_prm__set__faievetree(self._handle, faievetree)
        
        @property
        def evetreeh(self):
            """
            Element evetreeh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 401
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__evetreeh(self._handle)
        
        @evetreeh.setter
        def evetreeh(self, evetreeh):
            _supy_driver.f90wrap_lc_evetr_prm__set__evetreeh(self._handle, evetreeh)
        
        @property
        def alb_min(self):
            """
            Element alb_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 402
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__alb_min(self._handle)
        
        @alb_min.setter
        def alb_min(self, alb_min):
            _supy_driver.f90wrap_lc_evetr_prm__set__alb_min(self._handle, alb_min)
        
        @property
        def alb_max(self):
            """
            Element alb_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 403
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__alb_max(self._handle)
        
        @alb_max.setter
        def alb_max(self, alb_max):
            _supy_driver.f90wrap_lc_evetr_prm__set__alb_max(self._handle, alb_max)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 404
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_evetr_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 405
            
            """
            soil_handle = _supy_driver.f90wrap_lc_evetr_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 406
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_evetr_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracevetr(self):
            """
            Element irrfracevetr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 407
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__irrfracevetr(self._handle)
        
        @irrfracevetr.setter
        def irrfracevetr(self, irrfracevetr):
            _supy_driver.f90wrap_lc_evetr_prm__set__irrfracevetr(self._handle, irrfracevetr)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 408
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_evetr_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def bioco2(self):
            """
            Element bioco2 ftype=type(bioco2_prm) pytype=Bioco2_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 409
            
            """
            bioco2_handle = _supy_driver.f90wrap_lc_evetr_prm__get__bioco2(self._handle)
            if tuple(bioco2_handle) in self._objs:
                bioco2 = self._objs[tuple(bioco2_handle)]
            else:
                bioco2 = suews_driver.bioCO2_PRM.from_handle(bioco2_handle)
                self._objs[tuple(bioco2_handle)] = bioco2
            return bioco2
        
        @bioco2.setter
        def bioco2(self, bioco2):
            bioco2 = bioco2._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__bioco2(self._handle, bioco2)
        
        @property
        def maxconductance(self):
            """
            Element maxconductance ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 411
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__maxconductance(self._handle)
        
        @maxconductance.setter
        def maxconductance(self, maxconductance):
            _supy_driver.f90wrap_lc_evetr_prm__set__maxconductance(self._handle, \
                maxconductance)
        
        @property
        def lai(self):
            """
            Element lai ftype=type(lai_prm) pytype=Lai_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 412
            
            """
            lai_handle = _supy_driver.f90wrap_lc_evetr_prm__get__lai(self._handle)
            if tuple(lai_handle) in self._objs:
                lai = self._objs[tuple(lai_handle)]
            else:
                lai = suews_driver.LAI_PRM.from_handle(lai_handle)
                self._objs[tuple(lai_handle)] = lai
            return lai
        
        @lai.setter
        def lai(self, lai):
            lai = lai._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__lai(self._handle, lai)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 413
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_evetr_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_driver.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_evetr_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    faievetree : ')
            ret.append(repr(self.faievetree))
            ret.append(',\n    evetreeh : ')
            ret.append(repr(self.evetreeh))
            ret.append(',\n    alb_min : ')
            ret.append(repr(self.alb_min))
            ret.append(',\n    alb_max : ')
            ret.append(repr(self.alb_max))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracevetr : ')
            ret.append(repr(self.irrfracevetr))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    bioco2 : ')
            ret.append(repr(self.bioco2))
            ret.append(',\n    maxconductance : ')
            ret.append(repr(self.maxconductance))
            ret.append(',\n    lai : ')
            ret.append(repr(self.lai))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_GRASS_PRM")
    class LC_GRASS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_grass_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 415-429
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Grass_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 415-429
            
            
            Returns
            -------
            this : Lc_Grass_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_grass_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_grass_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Grass_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 415-429
            
            Parameters
            ----------
            this : Lc_Grass_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_grass_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_grass_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 416
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_grass_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 417
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_grass_prm__set__emis(self._handle, emis)
        
        @property
        def alb_min(self):
            """
            Element alb_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 418
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__alb_min(self._handle)
        
        @alb_min.setter
        def alb_min(self, alb_min):
            _supy_driver.f90wrap_lc_grass_prm__set__alb_min(self._handle, alb_min)
        
        @property
        def alb_max(self):
            """
            Element alb_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 419
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__alb_max(self._handle)
        
        @alb_max.setter
        def alb_max(self, alb_max):
            _supy_driver.f90wrap_lc_grass_prm__set__alb_max(self._handle, alb_max)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 420
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_grass_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_grass_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 421
            
            """
            soil_handle = _supy_driver.f90wrap_lc_grass_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_grass_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 422
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_grass_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracgrass(self):
            """
            Element irrfracgrass ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 423
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__irrfracgrass(self._handle)
        
        @irrfracgrass.setter
        def irrfracgrass(self, irrfracgrass):
            _supy_driver.f90wrap_lc_grass_prm__set__irrfracgrass(self._handle, irrfracgrass)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 424
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_grass_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def bioco2(self):
            """
            Element bioco2 ftype=type(bioco2_prm) pytype=Bioco2_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 425
            
            """
            bioco2_handle = _supy_driver.f90wrap_lc_grass_prm__get__bioco2(self._handle)
            if tuple(bioco2_handle) in self._objs:
                bioco2 = self._objs[tuple(bioco2_handle)]
            else:
                bioco2 = suews_driver.bioCO2_PRM.from_handle(bioco2_handle)
                self._objs[tuple(bioco2_handle)] = bioco2
            return bioco2
        
        @bioco2.setter
        def bioco2(self, bioco2):
            bioco2 = bioco2._handle
            _supy_driver.f90wrap_lc_grass_prm__set__bioco2(self._handle, bioco2)
        
        @property
        def maxconductance(self):
            """
            Element maxconductance ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 427
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__maxconductance(self._handle)
        
        @maxconductance.setter
        def maxconductance(self, maxconductance):
            _supy_driver.f90wrap_lc_grass_prm__set__maxconductance(self._handle, \
                maxconductance)
        
        @property
        def lai(self):
            """
            Element lai ftype=type(lai_prm) pytype=Lai_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 428
            
            """
            lai_handle = _supy_driver.f90wrap_lc_grass_prm__get__lai(self._handle)
            if tuple(lai_handle) in self._objs:
                lai = self._objs[tuple(lai_handle)]
            else:
                lai = suews_driver.LAI_PRM.from_handle(lai_handle)
                self._objs[tuple(lai_handle)] = lai
            return lai
        
        @lai.setter
        def lai(self, lai):
            lai = lai._handle
            _supy_driver.f90wrap_lc_grass_prm__set__lai(self._handle, lai)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 429
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_grass_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_driver.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_grass_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_grass_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    alb_min : ')
            ret.append(repr(self.alb_min))
            ret.append(',\n    alb_max : ')
            ret.append(repr(self.alb_max))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracgrass : ')
            ret.append(repr(self.irrfracgrass))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    bioco2 : ')
            ret.append(repr(self.bioco2))
            ret.append(',\n    maxconductance : ')
            ret.append(repr(self.maxconductance))
            ret.append(',\n    lai : ')
            ret.append(repr(self.lai))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_BSOIL_PRM")
    class LC_BSOIL_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_bsoil_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 431-439
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Bsoil_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 431-439
            
            
            Returns
            -------
            this : Lc_Bsoil_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_bsoil_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_bsoil_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Bsoil_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 431-439
            
            Parameters
            ----------
            this : Lc_Bsoil_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_bsoil_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_bsoil_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 432
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_bsoil_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 433
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_bsoil_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 434
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_bsoil_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_bsoil_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 435
            
            """
            soil_handle = _supy_driver.f90wrap_lc_bsoil_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_bsoil_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 436
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_bsoil_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracbsoil(self):
            """
            Element irrfracbsoil ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 437
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__irrfracbsoil(self._handle)
        
        @irrfracbsoil.setter
        def irrfracbsoil(self, irrfracbsoil):
            _supy_driver.f90wrap_lc_bsoil_prm__set__irrfracbsoil(self._handle, irrfracbsoil)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 438
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_bsoil_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 439
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_bsoil_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_driver.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_bsoil_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_bsoil_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracbsoil : ')
            ret.append(repr(self.irrfracbsoil))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_WATER_PRM")
    class LC_WATER_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_water_prm)
        
        
        Defined at suews_ctrl_driver.fpp lines 441-449
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Water_Prm()
            
            
            Defined at suews_ctrl_driver.fpp lines 441-449
            
            
            Returns
            -------
            this : Lc_Water_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_water_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_lc_water_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Water_Prm
            
            
            Defined at suews_ctrl_driver.fpp lines 441-449
            
            Parameters
            ----------
            this : Lc_Water_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_water_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_lc_water_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 442
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_water_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 443
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_water_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 444
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_water_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_driver.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_water_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at suews_ctrl_driver.fpp line 445
            
            """
            soil_handle = _supy_driver.f90wrap_lc_water_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_driver.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_water_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 446
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_water_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracwater(self):
            """
            Element irrfracwater ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 447
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__irrfracwater(self._handle)
        
        @irrfracwater.setter
        def irrfracwater(self, irrfracwater):
            _supy_driver.f90wrap_lc_water_prm__set__irrfracwater(self._handle, irrfracwater)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 448
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_water_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def flowchange(self):
            """
            Element flowchange ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 449
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__flowchange(self._handle)
        
        @flowchange.setter
        def flowchange(self, flowchange):
            _supy_driver.f90wrap_lc_water_prm__set__flowchange(self._handle, flowchange)
        
        def __str__(self):
            ret = ['<lc_water_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracwater : ')
            ret.append(repr(self.irrfracwater))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    flowchange : ')
            ret.append(repr(self.flowchange))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.anthroHEAT_STATE")
    class anthroHEAT_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=anthroheat_state)
        
        
        Defined at suews_ctrl_driver.fpp lines 452-453
        
        """
        def __init__(self, handle=None):
            """
            self = Anthroheat_State()
            
            
            Defined at suews_ctrl_driver.fpp lines 452-453
            
            
            Returns
            -------
            this : Anthroheat_State
            	Object to be constructed
            
            
            Automatically generated constructor for anthroheat_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_anthroheat_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Anthroheat_State
            
            
            Defined at suews_ctrl_driver.fpp lines 452-453
            
            Parameters
            ----------
            this : Anthroheat_State
            	Object to be destructed
            
            
            Automatically generated destructor for anthroheat_state
            """
            if self._alloc:
                _supy_driver.f90wrap_anthroheat_state_finalise(this=self._handle)
        
        @property
        def hdd_id(self):
            """
            Element hdd_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 453
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_state__array__hdd_id(self._handle)
            if array_handle in self._arrays:
                hdd_id = self._arrays[array_handle]
            else:
                hdd_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_state__array__hdd_id)
                self._arrays[array_handle] = hdd_id
            return hdd_id
        
        @hdd_id.setter
        def hdd_id(self, hdd_id):
            self.hdd_id[...] = hdd_id
        
        def __str__(self):
            ret = ['<anthroheat_state>{\n']
            ret.append('    hdd_id : ')
            ret.append(repr(self.hdd_id))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.HYDRO_STATE")
    class HYDRO_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=hydro_state)
        
        
        Defined at suews_ctrl_driver.fpp lines 455-463
        
        """
        def __init__(self, handle=None):
            """
            self = Hydro_State()
            
            
            Defined at suews_ctrl_driver.fpp lines 455-463
            
            
            Returns
            -------
            this : Hydro_State
            	Object to be constructed
            
            
            Automatically generated constructor for hydro_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_hydro_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Hydro_State
            
            
            Defined at suews_ctrl_driver.fpp lines 455-463
            
            Parameters
            ----------
            this : Hydro_State
            	Object to be destructed
            
            
            Automatically generated destructor for hydro_state
            """
            if self._alloc:
                _supy_driver.f90wrap_hydro_state_finalise(this=self._handle)
        
        @property
        def soilstore_surf(self):
            """
            Element soilstore_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 457
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__soilstore_surf(self._handle)
            if array_handle in self._arrays:
                soilstore_surf = self._arrays[array_handle]
            else:
                soilstore_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__soilstore_surf)
                self._arrays[array_handle] = soilstore_surf
            return soilstore_surf
        
        @soilstore_surf.setter
        def soilstore_surf(self, soilstore_surf):
            self.soilstore_surf[...] = soilstore_surf
        
        @property
        def state_surf(self):
            """
            Element state_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 458
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__state_surf(self._handle)
            if array_handle in self._arrays:
                state_surf = self._arrays[array_handle]
            else:
                state_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__state_surf)
                self._arrays[array_handle] = state_surf
            return state_surf
        
        @state_surf.setter
        def state_surf(self, state_surf):
            self.state_surf[...] = state_surf
        
        @property
        def wuday_id(self):
            """
            Element wuday_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 459
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__wuday_id(self._handle)
            if array_handle in self._arrays:
                wuday_id = self._arrays[array_handle]
            else:
                wuday_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__wuday_id)
                self._arrays[array_handle] = wuday_id
            return wuday_id
        
        @wuday_id.setter
        def wuday_id(self, wuday_id):
            self.wuday_id[...] = wuday_id
        
        @property
        def soilstore_roof(self):
            """
            Element soilstore_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 460
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__soilstore_roof(self._handle)
            if array_handle in self._arrays:
                soilstore_roof = self._arrays[array_handle]
            else:
                soilstore_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__soilstore_roof)
                self._arrays[array_handle] = soilstore_roof
            return soilstore_roof
        
        @soilstore_roof.setter
        def soilstore_roof(self, soilstore_roof):
            self.soilstore_roof[...] = soilstore_roof
        
        @property
        def state_roof(self):
            """
            Element state_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 461
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__state_roof(self._handle)
            if array_handle in self._arrays:
                state_roof = self._arrays[array_handle]
            else:
                state_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__state_roof)
                self._arrays[array_handle] = state_roof
            return state_roof
        
        @state_roof.setter
        def state_roof(self, state_roof):
            self.state_roof[...] = state_roof
        
        @property
        def soilstore_wall(self):
            """
            Element soilstore_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 462
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__soilstore_wall(self._handle)
            if array_handle in self._arrays:
                soilstore_wall = self._arrays[array_handle]
            else:
                soilstore_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__soilstore_wall)
                self._arrays[array_handle] = soilstore_wall
            return soilstore_wall
        
        @soilstore_wall.setter
        def soilstore_wall(self, soilstore_wall):
            self.soilstore_wall[...] = soilstore_wall
        
        @property
        def state_wall(self):
            """
            Element state_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 463
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__state_wall(self._handle)
            if array_handle in self._arrays:
                state_wall = self._arrays[array_handle]
            else:
                state_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__state_wall)
                self._arrays[array_handle] = state_wall
            return state_wall
        
        @state_wall.setter
        def state_wall(self, state_wall):
            self.state_wall[...] = state_wall
        
        def __str__(self):
            ret = ['<hydro_state>{\n']
            ret.append('    soilstore_surf : ')
            ret.append(repr(self.soilstore_surf))
            ret.append(',\n    state_surf : ')
            ret.append(repr(self.state_surf))
            ret.append(',\n    wuday_id : ')
            ret.append(repr(self.wuday_id))
            ret.append(',\n    soilstore_roof : ')
            ret.append(repr(self.soilstore_roof))
            ret.append(',\n    state_roof : ')
            ret.append(repr(self.state_roof))
            ret.append(',\n    soilstore_wall : ')
            ret.append(repr(self.soilstore_wall))
            ret.append(',\n    state_wall : ')
            ret.append(repr(self.state_wall))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.HEAT_STATE")
    class HEAT_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=heat_state)
        
        
        Defined at suews_ctrl_driver.fpp lines 465-471
        
        """
        def __init__(self, handle=None):
            """
            self = Heat_State()
            
            
            Defined at suews_ctrl_driver.fpp lines 465-471
            
            
            Returns
            -------
            this : Heat_State
            	Object to be constructed
            
            
            Automatically generated constructor for heat_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_heat_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Heat_State
            
            
            Defined at suews_ctrl_driver.fpp lines 465-471
            
            Parameters
            ----------
            this : Heat_State
            	Object to be destructed
            
            
            Automatically generated destructor for heat_state
            """
            if self._alloc:
                _supy_driver.f90wrap_heat_state_finalise(this=self._handle)
        
        @property
        def temp_roof(self):
            """
            Element temp_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 466
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__temp_roof(self._handle)
            if array_handle in self._arrays:
                temp_roof = self._arrays[array_handle]
            else:
                temp_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__temp_roof)
                self._arrays[array_handle] = temp_roof
            return temp_roof
        
        @temp_roof.setter
        def temp_roof(self, temp_roof):
            self.temp_roof[...] = temp_roof
        
        @property
        def temp_wall(self):
            """
            Element temp_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 467
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__temp_wall(self._handle)
            if array_handle in self._arrays:
                temp_wall = self._arrays[array_handle]
            else:
                temp_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__temp_wall)
                self._arrays[array_handle] = temp_wall
            return temp_wall
        
        @temp_wall.setter
        def temp_wall(self, temp_wall):
            self.temp_wall[...] = temp_wall
        
        @property
        def temp_surf(self):
            """
            Element temp_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 468
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__temp_surf(self._handle)
            if array_handle in self._arrays:
                temp_surf = self._arrays[array_handle]
            else:
                temp_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__temp_surf)
                self._arrays[array_handle] = temp_surf
            return temp_surf
        
        @temp_surf.setter
        def temp_surf(self, temp_surf):
            self.temp_surf[...] = temp_surf
        
        @property
        def tsfc_roof(self):
            """
            Element tsfc_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 469
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_roof(self._handle)
            if array_handle in self._arrays:
                tsfc_roof = self._arrays[array_handle]
            else:
                tsfc_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_roof)
                self._arrays[array_handle] = tsfc_roof
            return tsfc_roof
        
        @tsfc_roof.setter
        def tsfc_roof(self, tsfc_roof):
            self.tsfc_roof[...] = tsfc_roof
        
        @property
        def tsfc_wall(self):
            """
            Element tsfc_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 470
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_wall(self._handle)
            if array_handle in self._arrays:
                tsfc_wall = self._arrays[array_handle]
            else:
                tsfc_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_wall)
                self._arrays[array_handle] = tsfc_wall
            return tsfc_wall
        
        @tsfc_wall.setter
        def tsfc_wall(self, tsfc_wall):
            self.tsfc_wall[...] = tsfc_wall
        
        @property
        def tsfc_surf(self):
            """
            Element tsfc_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 471
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_surf(self._handle)
            if array_handle in self._arrays:
                tsfc_surf = self._arrays[array_handle]
            else:
                tsfc_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_surf)
                self._arrays[array_handle] = tsfc_surf
            return tsfc_surf
        
        @tsfc_surf.setter
        def tsfc_surf(self, tsfc_surf):
            self.tsfc_surf[...] = tsfc_surf
        
        def __str__(self):
            ret = ['<heat_state>{\n']
            ret.append('    temp_roof : ')
            ret.append(repr(self.temp_roof))
            ret.append(',\n    temp_wall : ')
            ret.append(repr(self.temp_wall))
            ret.append(',\n    temp_surf : ')
            ret.append(repr(self.temp_surf))
            ret.append(',\n    tsfc_roof : ')
            ret.append(repr(self.tsfc_roof))
            ret.append(',\n    tsfc_wall : ')
            ret.append(repr(self.tsfc_wall))
            ret.append(',\n    tsfc_surf : ')
            ret.append(repr(self.tsfc_surf))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.OHM_STATE")
    class OHM_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_state)
        
        
        Defined at suews_ctrl_driver.fpp lines 473-477
        
        """
        def __init__(self, handle=None):
            """
            self = Ohm_State()
            
            
            Defined at suews_ctrl_driver.fpp lines 473-477
            
            
            Returns
            -------
            this : Ohm_State
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_ohm_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_State
            
            
            Defined at suews_ctrl_driver.fpp lines 473-477
            
            Parameters
            ----------
            this : Ohm_State
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_state
            """
            if self._alloc:
                _supy_driver.f90wrap_ohm_state_finalise(this=self._handle)
        
        @property
        def qn_av(self):
            """
            Element qn_av ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 474
            
            """
            return _supy_driver.f90wrap_ohm_state__get__qn_av(self._handle)
        
        @qn_av.setter
        def qn_av(self, qn_av):
            _supy_driver.f90wrap_ohm_state__set__qn_av(self._handle, qn_av)
        
        @property
        def dqndt(self):
            """
            Element dqndt ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 475
            
            """
            return _supy_driver.f90wrap_ohm_state__get__dqndt(self._handle)
        
        @dqndt.setter
        def dqndt(self, dqndt):
            _supy_driver.f90wrap_ohm_state__set__dqndt(self._handle, dqndt)
        
        @property
        def qn_s_av(self):
            """
            Element qn_s_av ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 476
            
            """
            return _supy_driver.f90wrap_ohm_state__get__qn_s_av(self._handle)
        
        @qn_s_av.setter
        def qn_s_av(self, qn_s_av):
            _supy_driver.f90wrap_ohm_state__set__qn_s_av(self._handle, qn_s_av)
        
        @property
        def dqnsdt(self):
            """
            Element dqnsdt ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 477
            
            """
            return _supy_driver.f90wrap_ohm_state__get__dqnsdt(self._handle)
        
        @dqnsdt.setter
        def dqnsdt(self, dqnsdt):
            _supy_driver.f90wrap_ohm_state__set__dqnsdt(self._handle, dqnsdt)
        
        def __str__(self):
            ret = ['<ohm_state>{\n']
            ret.append('    qn_av : ')
            ret.append(repr(self.qn_av))
            ret.append(',\n    dqndt : ')
            ret.append(repr(self.dqndt))
            ret.append(',\n    qn_s_av : ')
            ret.append(repr(self.qn_s_av))
            ret.append(',\n    dqnsdt : ')
            ret.append(repr(self.dqnsdt))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.PHENOLOGY_STATE")
    class PHENOLOGY_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=phenology_state)
        
        
        Defined at suews_ctrl_driver.fpp lines 479-492
        
        """
        def __init__(self, handle=None):
            """
            self = Phenology_State()
            
            
            Defined at suews_ctrl_driver.fpp lines 479-492
            
            
            Returns
            -------
            this : Phenology_State
            	Object to be constructed
            
            
            Automatically generated constructor for phenology_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_phenology_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Phenology_State
            
            
            Defined at suews_ctrl_driver.fpp lines 479-492
            
            Parameters
            ----------
            this : Phenology_State
            	Object to be destructed
            
            
            Automatically generated destructor for phenology_state
            """
            if self._alloc:
                _supy_driver.f90wrap_phenology_state_finalise(this=self._handle)
        
        @property
        def alb(self):
            """
            Element alb ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 480
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__alb(self._handle)
            if array_handle in self._arrays:
                alb = self._arrays[array_handle]
            else:
                alb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__alb)
                self._arrays[array_handle] = alb
            return alb
        
        @alb.setter
        def alb(self, alb):
            self.alb[...] = alb
        
        @property
        def lai_id(self):
            """
            Element lai_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 481
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__lai_id(self._handle)
            if array_handle in self._arrays:
                lai_id = self._arrays[array_handle]
            else:
                lai_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__lai_id)
                self._arrays[array_handle] = lai_id
            return lai_id
        
        @lai_id.setter
        def lai_id(self, lai_id):
            self.lai_id[...] = lai_id
        
        @property
        def gdd_id(self):
            """
            Element gdd_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 482
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__gdd_id(self._handle)
            if array_handle in self._arrays:
                gdd_id = self._arrays[array_handle]
            else:
                gdd_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__gdd_id)
                self._arrays[array_handle] = gdd_id
            return gdd_id
        
        @gdd_id.setter
        def gdd_id(self, gdd_id):
            self.gdd_id[...] = gdd_id
        
        @property
        def sdd_id(self):
            """
            Element sdd_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 483
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__sdd_id(self._handle)
            if array_handle in self._arrays:
                sdd_id = self._arrays[array_handle]
            else:
                sdd_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__sdd_id)
                self._arrays[array_handle] = sdd_id
            return sdd_id
        
        @sdd_id.setter
        def sdd_id(self, sdd_id):
            self.sdd_id[...] = sdd_id
        
        @property
        def porosity_id(self):
            """
            Element porosity_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 484
            
            """
            return _supy_driver.f90wrap_phenology_state__get__porosity_id(self._handle)
        
        @porosity_id.setter
        def porosity_id(self, porosity_id):
            _supy_driver.f90wrap_phenology_state__set__porosity_id(self._handle, \
                porosity_id)
        
        @property
        def decidcap_id(self):
            """
            Element decidcap_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 485
            
            """
            return _supy_driver.f90wrap_phenology_state__get__decidcap_id(self._handle)
        
        @decidcap_id.setter
        def decidcap_id(self, decidcap_id):
            _supy_driver.f90wrap_phenology_state__set__decidcap_id(self._handle, \
                decidcap_id)
        
        @property
        def albdectr_id(self):
            """
            Element albdectr_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 486
            
            """
            return _supy_driver.f90wrap_phenology_state__get__albdectr_id(self._handle)
        
        @albdectr_id.setter
        def albdectr_id(self, albdectr_id):
            _supy_driver.f90wrap_phenology_state__set__albdectr_id(self._handle, \
                albdectr_id)
        
        @property
        def albevetr_id(self):
            """
            Element albevetr_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 487
            
            """
            return _supy_driver.f90wrap_phenology_state__get__albevetr_id(self._handle)
        
        @albevetr_id.setter
        def albevetr_id(self, albevetr_id):
            _supy_driver.f90wrap_phenology_state__set__albevetr_id(self._handle, \
                albevetr_id)
        
        @property
        def albgrass_id(self):
            """
            Element albgrass_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 488
            
            """
            return _supy_driver.f90wrap_phenology_state__get__albgrass_id(self._handle)
        
        @albgrass_id.setter
        def albgrass_id(self, albgrass_id):
            _supy_driver.f90wrap_phenology_state__set__albgrass_id(self._handle, \
                albgrass_id)
        
        @property
        def tmin_id(self):
            """
            Element tmin_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 489
            
            """
            return _supy_driver.f90wrap_phenology_state__get__tmin_id(self._handle)
        
        @tmin_id.setter
        def tmin_id(self, tmin_id):
            _supy_driver.f90wrap_phenology_state__set__tmin_id(self._handle, tmin_id)
        
        @property
        def tmax_id(self):
            """
            Element tmax_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 490
            
            """
            return _supy_driver.f90wrap_phenology_state__get__tmax_id(self._handle)
        
        @tmax_id.setter
        def tmax_id(self, tmax_id):
            _supy_driver.f90wrap_phenology_state__set__tmax_id(self._handle, tmax_id)
        
        @property
        def lenday_id(self):
            """
            Element lenday_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 491
            
            """
            return _supy_driver.f90wrap_phenology_state__get__lenday_id(self._handle)
        
        @lenday_id.setter
        def lenday_id(self, lenday_id):
            _supy_driver.f90wrap_phenology_state__set__lenday_id(self._handle, lenday_id)
        
        @property
        def storedrainprm(self):
            """
            Element storedrainprm ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 492
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__storedrainprm(self._handle)
            if array_handle in self._arrays:
                storedrainprm = self._arrays[array_handle]
            else:
                storedrainprm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__storedrainprm)
                self._arrays[array_handle] = storedrainprm
            return storedrainprm
        
        @storedrainprm.setter
        def storedrainprm(self, storedrainprm):
            self.storedrainprm[...] = storedrainprm
        
        def __str__(self):
            ret = ['<phenology_state>{\n']
            ret.append('    alb : ')
            ret.append(repr(self.alb))
            ret.append(',\n    lai_id : ')
            ret.append(repr(self.lai_id))
            ret.append(',\n    gdd_id : ')
            ret.append(repr(self.gdd_id))
            ret.append(',\n    sdd_id : ')
            ret.append(repr(self.sdd_id))
            ret.append(',\n    porosity_id : ')
            ret.append(repr(self.porosity_id))
            ret.append(',\n    decidcap_id : ')
            ret.append(repr(self.decidcap_id))
            ret.append(',\n    albdectr_id : ')
            ret.append(repr(self.albdectr_id))
            ret.append(',\n    albevetr_id : ')
            ret.append(repr(self.albevetr_id))
            ret.append(',\n    albgrass_id : ')
            ret.append(repr(self.albgrass_id))
            ret.append(',\n    tmin_id : ')
            ret.append(repr(self.tmin_id))
            ret.append(',\n    tmax_id : ')
            ret.append(repr(self.tmax_id))
            ret.append(',\n    lenday_id : ')
            ret.append(repr(self.lenday_id))
            ret.append(',\n    storedrainprm : ')
            ret.append(repr(self.storedrainprm))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SNOW_STATE")
    class SNOW_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=snow_state)
        
        
        Defined at suews_ctrl_driver.fpp lines 494-501
        
        """
        def __init__(self, handle=None):
            """
            self = Snow_State()
            
            
            Defined at suews_ctrl_driver.fpp lines 494-501
            
            
            Returns
            -------
            this : Snow_State
            	Object to be constructed
            
            
            Automatically generated constructor for snow_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_snow_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Snow_State
            
            
            Defined at suews_ctrl_driver.fpp lines 494-501
            
            Parameters
            ----------
            this : Snow_State
            	Object to be destructed
            
            
            Automatically generated destructor for snow_state
            """
            if self._alloc:
                _supy_driver.f90wrap_snow_state_finalise(this=self._handle)
        
        @property
        def snowfallcum(self):
            """
            Element snowfallcum ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 495
            
            """
            return _supy_driver.f90wrap_snow_state__get__snowfallcum(self._handle)
        
        @snowfallcum.setter
        def snowfallcum(self, snowfallcum):
            _supy_driver.f90wrap_snow_state__set__snowfallcum(self._handle, snowfallcum)
        
        @property
        def snowalb(self):
            """
            Element snowalb ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 496
            
            """
            return _supy_driver.f90wrap_snow_state__get__snowalb(self._handle)
        
        @snowalb.setter
        def snowalb(self, snowalb):
            _supy_driver.f90wrap_snow_state__set__snowalb(self._handle, snowalb)
        
        @property
        def icefrac(self):
            """
            Element icefrac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 497
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__icefrac(self._handle)
            if array_handle in self._arrays:
                icefrac = self._arrays[array_handle]
            else:
                icefrac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__icefrac)
                self._arrays[array_handle] = icefrac
            return icefrac
        
        @icefrac.setter
        def icefrac(self, icefrac):
            self.icefrac[...] = icefrac
        
        @property
        def snowdens(self):
            """
            Element snowdens ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 498
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowdens(self._handle)
            if array_handle in self._arrays:
                snowdens = self._arrays[array_handle]
            else:
                snowdens = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowdens)
                self._arrays[array_handle] = snowdens
            return snowdens
        
        @snowdens.setter
        def snowdens(self, snowdens):
            self.snowdens[...] = snowdens
        
        @property
        def snowfrac(self):
            """
            Element snowfrac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 499
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowfrac(self._handle)
            if array_handle in self._arrays:
                snowfrac = self._arrays[array_handle]
            else:
                snowfrac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowfrac)
                self._arrays[array_handle] = snowfrac
            return snowfrac
        
        @snowfrac.setter
        def snowfrac(self, snowfrac):
            self.snowfrac[...] = snowfrac
        
        @property
        def snowpack(self):
            """
            Element snowpack ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 500
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowpack(self._handle)
            if array_handle in self._arrays:
                snowpack = self._arrays[array_handle]
            else:
                snowpack = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowpack)
                self._arrays[array_handle] = snowpack
            return snowpack
        
        @snowpack.setter
        def snowpack(self, snowpack):
            self.snowpack[...] = snowpack
        
        @property
        def snowwater(self):
            """
            Element snowwater ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 501
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowwater(self._handle)
            if array_handle in self._arrays:
                snowwater = self._arrays[array_handle]
            else:
                snowwater = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowwater)
                self._arrays[array_handle] = snowwater
            return snowwater
        
        @snowwater.setter
        def snowwater(self, snowwater):
            self.snowwater[...] = snowwater
        
        def __str__(self):
            ret = ['<snow_state>{\n']
            ret.append('    snowfallcum : ')
            ret.append(repr(self.snowfallcum))
            ret.append(',\n    snowalb : ')
            ret.append(repr(self.snowalb))
            ret.append(',\n    icefrac : ')
            ret.append(repr(self.icefrac))
            ret.append(',\n    snowdens : ')
            ret.append(repr(self.snowdens))
            ret.append(',\n    snowfrac : ')
            ret.append(repr(self.snowfrac))
            ret.append(',\n    snowpack : ')
            ret.append(repr(self.snowpack))
            ret.append(',\n    snowwater : ')
            ret.append(repr(self.snowwater))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_FORCING")
    class SUEWS_FORCING(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_forcing)
        
        
        Defined at suews_ctrl_driver.fpp lines 504-520
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Forcing()
            
            
            Defined at suews_ctrl_driver.fpp lines 504-520
            
            
            Returns
            -------
            this : Suews_Forcing
            	Object to be constructed
            
            
            Automatically generated constructor for suews_forcing
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_forcing_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Forcing
            
            
            Defined at suews_ctrl_driver.fpp lines 504-520
            
            Parameters
            ----------
            this : Suews_Forcing
            	Object to be destructed
            
            
            Automatically generated destructor for suews_forcing
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_forcing_finalise(this=self._handle)
        
        @property
        def kdown(self):
            """
            Element kdown ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 505
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__kdown(self._handle)
        
        @kdown.setter
        def kdown(self, kdown):
            _supy_driver.f90wrap_suews_forcing__set__kdown(self._handle, kdown)
        
        @property
        def ldown(self):
            """
            Element ldown ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 506
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__ldown(self._handle)
        
        @ldown.setter
        def ldown(self, ldown):
            _supy_driver.f90wrap_suews_forcing__set__ldown(self._handle, ldown)
        
        @property
        def rh(self):
            """
            Element rh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 507
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__rh(self._handle)
        
        @rh.setter
        def rh(self, rh):
            _supy_driver.f90wrap_suews_forcing__set__rh(self._handle, rh)
        
        @property
        def pres(self):
            """
            Element pres ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 508
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__pres(self._handle)
        
        @pres.setter
        def pres(self, pres):
            _supy_driver.f90wrap_suews_forcing__set__pres(self._handle, pres)
        
        @property
        def tair(self):
            """
            Element tair ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 509
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__tair(self._handle)
        
        @tair.setter
        def tair(self, tair):
            _supy_driver.f90wrap_suews_forcing__set__tair(self._handle, tair)
        
        @property
        def u(self):
            """
            Element u ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 510
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__u(self._handle)
        
        @u.setter
        def u(self, u):
            _supy_driver.f90wrap_suews_forcing__set__u(self._handle, u)
        
        @property
        def rain(self):
            """
            Element rain ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 511
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__rain(self._handle)
        
        @rain.setter
        def rain(self, rain):
            _supy_driver.f90wrap_suews_forcing__set__rain(self._handle, rain)
        
        @property
        def wuh(self):
            """
            Element wuh ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 512
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__wuh(self._handle)
        
        @wuh.setter
        def wuh(self, wuh):
            _supy_driver.f90wrap_suews_forcing__set__wuh(self._handle, wuh)
        
        @property
        def fcld(self):
            """
            Element fcld ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 513
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__fcld(self._handle)
        
        @fcld.setter
        def fcld(self, fcld):
            _supy_driver.f90wrap_suews_forcing__set__fcld(self._handle, fcld)
        
        @property
        def lai_obs(self):
            """
            Element lai_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 514
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__lai_obs(self._handle)
        
        @lai_obs.setter
        def lai_obs(self, lai_obs):
            _supy_driver.f90wrap_suews_forcing__set__lai_obs(self._handle, lai_obs)
        
        @property
        def snowfrac(self):
            """
            Element snowfrac ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 515
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__snowfrac(self._handle)
        
        @snowfrac.setter
        def snowfrac(self, snowfrac):
            _supy_driver.f90wrap_suews_forcing__set__snowfrac(self._handle, snowfrac)
        
        @property
        def xsmd(self):
            """
            Element xsmd ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 516
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__xsmd(self._handle)
        
        @xsmd.setter
        def xsmd(self, xsmd):
            _supy_driver.f90wrap_suews_forcing__set__xsmd(self._handle, xsmd)
        
        @property
        def qf_obs(self):
            """
            Element qf_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 517
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__qf_obs(self._handle)
        
        @qf_obs.setter
        def qf_obs(self, qf_obs):
            _supy_driver.f90wrap_suews_forcing__set__qf_obs(self._handle, qf_obs)
        
        @property
        def qn1_obs(self):
            """
            Element qn1_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 518
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__qn1_obs(self._handle)
        
        @qn1_obs.setter
        def qn1_obs(self, qn1_obs):
            _supy_driver.f90wrap_suews_forcing__set__qn1_obs(self._handle, qn1_obs)
        
        @property
        def qs_obs(self):
            """
            Element qs_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 519
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__qs_obs(self._handle)
        
        @qs_obs.setter
        def qs_obs(self, qs_obs):
            _supy_driver.f90wrap_suews_forcing__set__qs_obs(self._handle, qs_obs)
        
        @property
        def temp_c(self):
            """
            Element temp_c ftype=real(kind(1d0) pytype=float
            
            
            Defined at suews_ctrl_driver.fpp line 520
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__temp_c(self._handle)
        
        @temp_c.setter
        def temp_c(self, temp_c):
            _supy_driver.f90wrap_suews_forcing__set__temp_c(self._handle, temp_c)
        
        def __str__(self):
            ret = ['<suews_forcing>{\n']
            ret.append('    kdown : ')
            ret.append(repr(self.kdown))
            ret.append(',\n    ldown : ')
            ret.append(repr(self.ldown))
            ret.append(',\n    rh : ')
            ret.append(repr(self.rh))
            ret.append(',\n    pres : ')
            ret.append(repr(self.pres))
            ret.append(',\n    tair : ')
            ret.append(repr(self.tair))
            ret.append(',\n    u : ')
            ret.append(repr(self.u))
            ret.append(',\n    rain : ')
            ret.append(repr(self.rain))
            ret.append(',\n    wuh : ')
            ret.append(repr(self.wuh))
            ret.append(',\n    fcld : ')
            ret.append(repr(self.fcld))
            ret.append(',\n    lai_obs : ')
            ret.append(repr(self.lai_obs))
            ret.append(',\n    snowfrac : ')
            ret.append(repr(self.snowfrac))
            ret.append(',\n    xsmd : ')
            ret.append(repr(self.xsmd))
            ret.append(',\n    qf_obs : ')
            ret.append(repr(self.qf_obs))
            ret.append(',\n    qn1_obs : ')
            ret.append(repr(self.qn1_obs))
            ret.append(',\n    qs_obs : ')
            ret.append(repr(self.qs_obs))
            ret.append(',\n    temp_c : ')
            ret.append(repr(self.temp_c))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_TIMER")
    class SUEWS_TIMER(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_timer)
        
        
        Defined at suews_ctrl_driver.fpp lines 522-530
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Timer()
            
            
            Defined at suews_ctrl_driver.fpp lines 522-530
            
            
            Returns
            -------
            this : Suews_Timer
            	Object to be constructed
            
            
            Automatically generated constructor for suews_timer
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_timer_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Timer
            
            
            Defined at suews_ctrl_driver.fpp lines 522-530
            
            Parameters
            ----------
            this : Suews_Timer
            	Object to be destructed
            
            
            Automatically generated destructor for suews_timer
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_timer_finalise(this=self._handle)
        
        @property
        def id(self):
            """
            Element id ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 523
            
            """
            return _supy_driver.f90wrap_suews_timer__get__id(self._handle)
        
        @id.setter
        def id(self, id):
            _supy_driver.f90wrap_suews_timer__set__id(self._handle, id)
        
        @property
        def imin(self):
            """
            Element imin ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 524
            
            """
            return _supy_driver.f90wrap_suews_timer__get__imin(self._handle)
        
        @imin.setter
        def imin(self, imin):
            _supy_driver.f90wrap_suews_timer__set__imin(self._handle, imin)
        
        @property
        def isec(self):
            """
            Element isec ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 525
            
            """
            return _supy_driver.f90wrap_suews_timer__get__isec(self._handle)
        
        @isec.setter
        def isec(self, isec):
            _supy_driver.f90wrap_suews_timer__set__isec(self._handle, isec)
        
        @property
        def it(self):
            """
            Element it ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 526
            
            """
            return _supy_driver.f90wrap_suews_timer__get__it(self._handle)
        
        @it.setter
        def it(self, it):
            _supy_driver.f90wrap_suews_timer__set__it(self._handle, it)
        
        @property
        def iy(self):
            """
            Element iy ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 527
            
            """
            return _supy_driver.f90wrap_suews_timer__get__iy(self._handle)
        
        @iy.setter
        def iy(self, iy):
            _supy_driver.f90wrap_suews_timer__set__iy(self._handle, iy)
        
        @property
        def tstep(self):
            """
            Element tstep ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 528
            
            """
            return _supy_driver.f90wrap_suews_timer__get__tstep(self._handle)
        
        @tstep.setter
        def tstep(self, tstep):
            _supy_driver.f90wrap_suews_timer__set__tstep(self._handle, tstep)
        
        @property
        def tstep_prev(self):
            """
            Element tstep_prev ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 529
            
            """
            return _supy_driver.f90wrap_suews_timer__get__tstep_prev(self._handle)
        
        @tstep_prev.setter
        def tstep_prev(self, tstep_prev):
            _supy_driver.f90wrap_suews_timer__set__tstep_prev(self._handle, tstep_prev)
        
        @property
        def dt_since_start(self):
            """
            Element dt_since_start ftype=integer  pytype=int
            
            
            Defined at suews_ctrl_driver.fpp line 530
            
            """
            return _supy_driver.f90wrap_suews_timer__get__dt_since_start(self._handle)
        
        @dt_since_start.setter
        def dt_since_start(self, dt_since_start):
            _supy_driver.f90wrap_suews_timer__set__dt_since_start(self._handle, \
                dt_since_start)
        
        def __str__(self):
            ret = ['<suews_timer>{\n']
            ret.append('    id : ')
            ret.append(repr(self.id))
            ret.append(',\n    imin : ')
            ret.append(repr(self.imin))
            ret.append(',\n    isec : ')
            ret.append(repr(self.isec))
            ret.append(',\n    it : ')
            ret.append(repr(self.it))
            ret.append(',\n    iy : ')
            ret.append(repr(self.iy))
            ret.append(',\n    tstep : ')
            ret.append(repr(self.tstep))
            ret.append(',\n    tstep_prev : ')
            ret.append(repr(self.tstep_prev))
            ret.append(',\n    dt_since_start : ')
            ret.append(repr(self.dt_since_start))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.Ohm_Coef_Lc_X3_Array")
    class Ohm_Coef_Lc_X3_Array(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_coef_lc_x3_array)
        
        
        Defined at suews_ctrl_driver.fpp lines 161-165
        
        super-type
        Automatically generated to handle derived type arrays as a new derived type
        """
        def __init__(self, handle=None):
            """
            self = Ohm_Coef_Lc_X3_Array()
            
            
            Defined at suews_ctrl_driver.fpp lines 161-165
            
            
            Returns
            -------
            this : Ohm_Coef_Lc_X3_Array
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_coef_lc_x3_array
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_ohm_coef_lc_x3_array_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_Coef_Lc_X3_Array
            
            
            Defined at suews_ctrl_driver.fpp lines 161-165
            
            Parameters
            ----------
            this : Ohm_Coef_Lc_X3_Array
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_coef_lc_x3_array
            """
            if self._alloc:
                _supy_driver.f90wrap_ohm_coef_lc_x3_array_finalise(this=self._handle)
        
        def init_array_items(self):
            self.items = f90wrap.runtime.FortranDerivedTypeArray(self,
                                            _supy_driver.f90wrap_ohm_coef_lc_x3_array__array_getitem__items,
                                            _supy_driver.f90wrap_ohm_coef_lc_x3_array__array_setitem__items,
                                            _supy_driver.f90wrap_ohm_coef_lc_x3_array__array_len__items,
                                            """
            Element items ftype=type(ohm_coef_lc) pytype=Ohm_Coef_Lc
            
            
            Defined at  line 0
            
            """, Suews_Driver.OHM_COEF_LC)
            return self.items
        
        _dt_array_initialisers = [init_array_items]
        
    
    @staticmethod
    def output_line_init(self):
        """
        output_line_init(self)
        
        
        Defined at suews_ctrl_driver.fpp lines 533-545
        
        Parameters
        ----------
        this_line : Output_Line
        
        """
        _supy_driver.f90wrap_output_line_init(this_line=self._handle)
    
    @staticmethod
    def output_block_init(self, len_bn):
        """
        output_block_init(self, len_bn)
        
        
        Defined at suews_ctrl_driver.fpp lines 547-569
        
        Parameters
        ----------
        this_block : Output_Block
        len_bn : int
        
        """
        _supy_driver.f90wrap_output_block_init(this_block=self._handle, len_bn=len_bn)
    
    @staticmethod
    def output_block_finalize(self):
        """
        output_block_finalize(self)
        
        
        Defined at suews_ctrl_driver.fpp lines 571-582
        
        Parameters
        ----------
        this_line : Output_Block
        
        """
        _supy_driver.f90wrap_output_block_finalize(this_line=self._handle)
    
    @staticmethod
    def var2add_two(self):
        """
        res_type = var2add_two(self)
        
        
        Defined at suews_ctrl_driver.fpp lines 584-588
        
        Parameters
        ----------
        arg_type : Config
        
        Returns
        -------
        res_type : Config
        
        """
        res_type = _supy_driver.f90wrap_var2add_two(arg_type=self._handle)
        res_type = \
            f90wrap.runtime.lookup_class("supy_driver.config").from_handle(res_type, \
            alloc=True)
        return res_type
    
    @staticmethod
    def arr2add_two(self):
        """
        res_type = arr2add_two(self)
        
        
        Defined at suews_ctrl_driver.fpp lines 590-594
        
        Parameters
        ----------
        arg_type : Array_M
        
        Returns
        -------
        res_type : Array_M
        
        """
        res_type = _supy_driver.f90wrap_arr2add_two(arg_type=self._handle)
        res_type = \
            f90wrap.runtime.lookup_class("supy_driver.array_m").from_handle(res_type, \
            alloc=True)
        return res_type
    
    @staticmethod
    def suews_cal_main(ah_min, ahprof_24hr, ah_slope_cooling, ah_slope_heating, alb, \
        albmax_dectr, albmax_evetr, albmax_grass, albmin_dectr, albmin_evetr, \
        albmin_grass, alpha_bioco2, alpha_enh_bioco2, alt, kdown, avrh, avu1, baset, \
        basete, beta_bioco2, beta_enh_bioco2, bldgh, capmax_dec, capmin_dec, \
        chanohm, co2pointsource, cpanohm, crwmax, crwmin, daywat, daywatper, \
        dectreeh, diagmethod, diagnose, drainrt, dt_since_start, dqndt, qn_av, \
        dqnsdt, qn_s_av, ef_umolco2perj, emis, emissionsmethod, enef_v_jkm, enddls, \
        evetreeh, faibldg, faidectree, faievetree, faimethod, faut, fcef_v_kgkm, \
        fcld_obs, flowchange, frfossilfuel_heat, frfossilfuel_nonheat, g_max, g_k, \
        g_q_base, g_q_shape, g_t, g_sm, gdd_id, gddfull, gridiv, gsmodel, \
        h_maintain, hdd_id, humactivity_24hr, icefrac, id, ie_a, ie_end, ie_m, \
        ie_start, imin, internalwateruse_h, irrfracpaved, irrfracbldgs, \
        irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, irrfracwater, isec, \
        it, iy, kkanohm, kmax, lai_id, laimax, laimin, lai_obs, laipower, laitype, \
        lat, lenday_id, ldown_obs, lng, maxconductance, maxfcmetab, maxqfmetab, \
        snowwater, minfcmetab, minqfmetab, min_res_bioco2, narp_emis_snow, \
        narp_trans_site, netradiationmethod, nlayer, n_vegetation_region_urban, \
        n_stream_sw_urban, n_stream_lw_urban, sw_dn_direct_frac, air_ext_sw, \
        air_ssa_sw, veg_ssa_sw, air_ext_lw, air_ssa_lw, veg_ssa_lw, veg_fsd_const, \
        veg_contact_fraction_const, ground_albedo_dir_mult_fact, \
        use_sw_direct_albedo, height, building_frac, veg_frac, building_scale, \
        veg_scale, alb_roof, emis_roof, alb_wall, emis_wall, \
        roof_albedo_dir_mult_fact, wall_specular_frac, ohm_coef, ohmincqf, \
        ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, popdensnighttime, \
        popprof_24hr, pormax_dec, pormin_dec, precip, preciplimit, preciplimitalb, \
        press_hpa, qf0_beu, qf_a, qf_b, qf_c, qn1_obs, qs_obs, qf_obs, radmeltfact, \
        raincover, rainmaxres, resp_a, resp_b, roughlenheatmethod, \
        roughlenmommethod, runofftowater, s1, s2, sathydraulicconduct, sddfull, \
        sdd_id, smdmethod, snowalb, snowalbmax, snowalbmin, snowpacklimit, snowdens, \
        snowdensmax, snowdensmin, snowfallcum, snowfrac, snowlimbldg, snowlimpaved, \
        snowfrac_obs, snowpack, snowprof_24hr, snowuse, soildepth, stabilitymethod, \
        startdls, soilstore_surf, soilstorecap_surf, state_surf, statelimit_surf, \
        wetthresh_surf, soilstore_roof, soilstorecap_roof, state_roof, \
        statelimit_roof, wetthresh_roof, soilstore_wall, soilstorecap_wall, \
        state_wall, statelimit_wall, wetthresh_wall, storageheatmethod, \
        storedrainprm, surfacearea, tair_av, tau_a, tau_f, tau_r, tmax_id, tmin_id, \
        baset_cooling, baset_heating, temp_c, tempmeltfact, th, theta_bioco2, \
        timezone, tl, trafficrate, trafficunits, sfr_surf, tsfc_roof, tsfc_wall, \
        tsfc_surf, temp_roof, temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, \
        k_roof, k_wall, k_surf, cp_roof, cp_wall, cp_surf, dz_roof, dz_wall, \
        dz_surf, traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, \
        waterdist, waterusemethod, wu_m3, wuday_id, decidcap_id, albdectr_id, \
        albevetr_id, albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, xsmd, z, \
        z0m_in, zdm_in):
        """
        output_line_suews = suews_cal_main(ah_min, ahprof_24hr, ah_slope_cooling, \
            ah_slope_heating, alb, albmax_dectr, albmax_evetr, albmax_grass, \
            albmin_dectr, albmin_evetr, albmin_grass, alpha_bioco2, alpha_enh_bioco2, \
            alt, kdown, avrh, avu1, baset, basete, beta_bioco2, beta_enh_bioco2, bldgh, \
            capmax_dec, capmin_dec, chanohm, co2pointsource, cpanohm, crwmax, crwmin, \
            daywat, daywatper, dectreeh, diagmethod, diagnose, drainrt, dt_since_start, \
            dqndt, qn_av, dqnsdt, qn_s_av, ef_umolco2perj, emis, emissionsmethod, \
            enef_v_jkm, enddls, evetreeh, faibldg, faidectree, faievetree, faimethod, \
            faut, fcef_v_kgkm, fcld_obs, flowchange, frfossilfuel_heat, \
            frfossilfuel_nonheat, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, gdd_id, \
            gddfull, gridiv, gsmodel, h_maintain, hdd_id, humactivity_24hr, icefrac, id, \
            ie_a, ie_end, ie_m, ie_start, imin, internalwateruse_h, irrfracpaved, \
            irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, \
            irrfracwater, isec, it, iy, kkanohm, kmax, lai_id, laimax, laimin, lai_obs, \
            laipower, laitype, lat, lenday_id, ldown_obs, lng, maxconductance, \
            maxfcmetab, maxqfmetab, snowwater, minfcmetab, minqfmetab, min_res_bioco2, \
            narp_emis_snow, narp_trans_site, netradiationmethod, nlayer, \
            n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
            emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, ohm_coef, \
            ohmincqf, ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, \
            popdensnighttime, popprof_24hr, pormax_dec, pormin_dec, precip, preciplimit, \
            preciplimitalb, press_hpa, qf0_beu, qf_a, qf_b, qf_c, qn1_obs, qs_obs, \
            qf_obs, radmeltfact, raincover, rainmaxres, resp_a, resp_b, \
            roughlenheatmethod, roughlenmommethod, runofftowater, s1, s2, \
            sathydraulicconduct, sddfull, sdd_id, smdmethod, snowalb, snowalbmax, \
            snowalbmin, snowpacklimit, snowdens, snowdensmax, snowdensmin, snowfallcum, \
            snowfrac, snowlimbldg, snowlimpaved, snowfrac_obs, snowpack, snowprof_24hr, \
            snowuse, soildepth, stabilitymethod, startdls, soilstore_surf, \
            soilstorecap_surf, state_surf, statelimit_surf, wetthresh_surf, \
            soilstore_roof, soilstorecap_roof, state_roof, statelimit_roof, \
            wetthresh_roof, soilstore_wall, soilstorecap_wall, state_wall, \
            statelimit_wall, wetthresh_wall, storageheatmethod, storedrainprm, \
            surfacearea, tair_av, tau_a, tau_f, tau_r, tmax_id, tmin_id, baset_cooling, \
            baset_heating, temp_c, tempmeltfact, th, theta_bioco2, timezone, tl, \
            trafficrate, trafficunits, sfr_surf, tsfc_roof, tsfc_wall, tsfc_surf, \
            temp_roof, temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, k_roof, \
            k_wall, k_surf, cp_roof, cp_wall, cp_surf, dz_roof, dz_wall, dz_surf, \
            traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, waterdist, \
            waterusemethod, wu_m3, wuday_id, decidcap_id, albdectr_id, albevetr_id, \
            albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, xsmd, z, z0m_in, \
            zdm_in)
        
        
        Defined at suews_ctrl_driver.fpp lines 661-2069
        
        Parameters
        ----------
        ah_min : float array
        ahprof_24hr : float array
        ah_slope_cooling : float array
        ah_slope_heating : float array
        alb : float array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        alpha_bioco2 : float array
        alpha_enh_bioco2 : float array
        alt : float
        kdown : float
        avrh : float
        avu1 : float
        baset : float array
        basete : float array
        beta_bioco2 : float array
        beta_enh_bioco2 : float array
        bldgh : float
        capmax_dec : float
        capmin_dec : float
        chanohm : float array
        co2pointsource : float
        cpanohm : float array
        crwmax : float
        crwmin : float
        daywat : float array
        daywatper : float array
        dectreeh : float
        diagmethod : int
        diagnose : int
        drainrt : float
        dt_since_start : int
        dqndt : float
        qn_av : float
        dqnsdt : float
        qn_s_av : float
        ef_umolco2perj : float
        emis : float array
        emissionsmethod : int
        enef_v_jkm : float
        enddls : int
        evetreeh : float
        faibldg : float
        faidectree : float
        faievetree : float
        faimethod : int
        faut : float
        fcef_v_kgkm : float array
        fcld_obs : float
        flowchange : float
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        gdd_id : float array
        gddfull : float array
        gridiv : int
        gsmodel : int
        h_maintain : float
        hdd_id : float array
        humactivity_24hr : float array
        icefrac : float array
        id : int
        ie_a : float array
        ie_end : int
        ie_m : float array
        ie_start : int
        imin : int
        internalwateruse_h : float
        irrfracpaved : float
        irrfracbldgs : float
        irrfracevetr : float
        irrfracdectr : float
        irrfracgrass : float
        irrfracbsoil : float
        irrfracwater : float
        isec : int
        it : int
        iy : int
        kkanohm : float array
        kmax : float
        lai_id : float array
        laimax : float array
        laimin : float array
        lai_obs : float
        laipower : float array
        laitype : int array
        lat : float
        lenday_id : float
        ldown_obs : float
        lng : float
        maxconductance : float array
        maxfcmetab : float
        maxqfmetab : float
        snowwater : float array
        minfcmetab : float
        minqfmetab : float
        min_res_bioco2 : float array
        narp_emis_snow : float
        narp_trans_site : float
        netradiationmethod : int
        nlayer : int
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        ohm_coef : float array
        ohmincqf : int
        ohm_threshsw : float array
        ohm_threshwd : float array
        pipecapacity : float
        popdensdaytime : float array
        popdensnighttime : float
        popprof_24hr : float array
        pormax_dec : float
        pormin_dec : float
        precip : float
        preciplimit : float
        preciplimitalb : float
        press_hpa : float
        qf0_beu : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        qn1_obs : float
        qs_obs : float
        qf_obs : float
        radmeltfact : float
        raincover : float
        rainmaxres : float
        resp_a : float array
        resp_b : float array
        roughlenheatmethod : int
        roughlenmommethod : int
        runofftowater : float
        s1 : float
        s2 : float
        sathydraulicconduct : float array
        sddfull : float array
        sdd_id : float array
        smdmethod : int
        snowalb : float
        snowalbmax : float
        snowalbmin : float
        snowpacklimit : float array
        snowdens : float array
        snowdensmax : float
        snowdensmin : float
        snowfallcum : float
        snowfrac : float array
        snowlimbldg : float
        snowlimpaved : float
        snowfrac_obs : float
        snowpack : float array
        snowprof_24hr : float array
        snowuse : int
        soildepth : float array
        stabilitymethod : int
        startdls : int
        soilstore_surf : float array
        soilstorecap_surf : float array
        state_surf : float array
        statelimit_surf : float array
        wetthresh_surf : float array
        soilstore_roof : float array
        soilstorecap_roof : float array
        state_roof : float array
        statelimit_roof : float array
        wetthresh_roof : float array
        soilstore_wall : float array
        soilstorecap_wall : float array
        state_wall : float array
        statelimit_wall : float array
        wetthresh_wall : float array
        storageheatmethod : int
        storedrainprm : float array
        surfacearea : float
        tair_av : float
        tau_a : float
        tau_f : float
        tau_r : float
        tmax_id : float
        tmin_id : float
        baset_cooling : float array
        baset_heating : float array
        temp_c : float
        tempmeltfact : float
        th : float
        theta_bioco2 : float array
        timezone : float
        tl : float
        trafficrate : float array
        trafficunits : float
        sfr_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        tsfc_surf : float array
        temp_roof : float array
        temp_wall : float array
        temp_surf : float array
        tin_roof : float array
        tin_wall : float array
        tin_surf : float array
        k_roof : float array
        k_wall : float array
        k_surf : float array
        cp_roof : float array
        cp_wall : float array
        cp_surf : float array
        dz_roof : float array
        dz_wall : float array
        dz_surf : float array
        traffprof_24hr : float array
        ts5mindata_ir : float array
        tstep : int
        tstep_prev : int
        veg_type : int
        waterdist : float array
        waterusemethod : int
        wu_m3 : float
        wuday_id : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        wuprofa_24hr : float array
        wuprofm_24hr : float array
        xsmd : float
        z : float
        z0m_in : float
        zdm_in : float
        
        Returns
        -------
        output_line_suews : Output_Line
        
        ==============main calculation start=======================
        ==============surface roughness calculation=======================
        """
        output_line_suews = _supy_driver.f90wrap_suews_cal_main(ah_min=ah_min, \
            ahprof_24hr=ahprof_24hr, ah_slope_cooling=ah_slope_cooling, \
            ah_slope_heating=ah_slope_heating, alb=alb, albmax_dectr=albmax_dectr, \
            albmax_evetr=albmax_evetr, albmax_grass=albmax_grass, \
            albmin_dectr=albmin_dectr, albmin_evetr=albmin_evetr, \
            albmin_grass=albmin_grass, alpha_bioco2=alpha_bioco2, \
            alpha_enh_bioco2=alpha_enh_bioco2, alt=alt, kdown=kdown, avrh=avrh, \
            avu1=avu1, baset=baset, basete=basete, beta_bioco2=beta_bioco2, \
            beta_enh_bioco2=beta_enh_bioco2, bldgh=bldgh, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, chanohm=chanohm, co2pointsource=co2pointsource, \
            cpanohm=cpanohm, crwmax=crwmax, crwmin=crwmin, daywat=daywat, \
            daywatper=daywatper, dectreeh=dectreeh, diagmethod=diagmethod, \
            diagnose=diagnose, drainrt=drainrt, dt_since_start=dt_since_start, \
            dqndt=dqndt, qn_av=qn_av, dqnsdt=dqnsdt, qn_s_av=qn_s_av, \
            ef_umolco2perj=ef_umolco2perj, emis=emis, emissionsmethod=emissionsmethod, \
            enef_v_jkm=enef_v_jkm, enddls=enddls, evetreeh=evetreeh, faibldg=faibldg, \
            faidectree=faidectree, faievetree=faievetree, faimethod=faimethod, \
            faut=faut, fcef_v_kgkm=fcef_v_kgkm, fcld_obs=fcld_obs, \
            flowchange=flowchange, frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, gdd_id=gdd_id, \
            gddfull=gddfull, gridiv=gridiv, gsmodel=gsmodel, h_maintain=h_maintain, \
            hdd_id=hdd_id, humactivity_24hr=humactivity_24hr, icefrac=icefrac, id=id, \
            ie_a=ie_a, ie_end=ie_end, ie_m=ie_m, ie_start=ie_start, imin=imin, \
            internalwateruse_h=internalwateruse_h, irrfracpaved=irrfracpaved, \
            irrfracbldgs=irrfracbldgs, irrfracevetr=irrfracevetr, \
            irrfracdectr=irrfracdectr, irrfracgrass=irrfracgrass, \
            irrfracbsoil=irrfracbsoil, irrfracwater=irrfracwater, isec=isec, it=it, \
            iy=iy, kkanohm=kkanohm, kmax=kmax, lai_id=lai_id, laimax=laimax, \
            laimin=laimin, lai_obs=lai_obs, laipower=laipower, laitype=laitype, lat=lat, \
            lenday_id=lenday_id, ldown_obs=ldown_obs, lng=lng, \
            maxconductance=maxconductance, maxfcmetab=maxfcmetab, maxqfmetab=maxqfmetab, \
            snowwater=snowwater, minfcmetab=minfcmetab, minqfmetab=minqfmetab, \
            min_res_bioco2=min_res_bioco2, narp_emis_snow=narp_emis_snow, \
            narp_trans_site=narp_trans_site, netradiationmethod=netradiationmethod, \
            nlayer=nlayer, n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, \
            building_scale=building_scale, veg_scale=veg_scale, alb_roof=alb_roof, \
            emis_roof=emis_roof, alb_wall=alb_wall, emis_wall=emis_wall, \
            roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, ohm_coef=ohm_coef, ohmincqf=ohmincqf, \
            ohm_threshsw=ohm_threshsw, ohm_threshwd=ohm_threshwd, \
            pipecapacity=pipecapacity, popdensdaytime=popdensdaytime, \
            popdensnighttime=popdensnighttime, popprof_24hr=popprof_24hr, \
            pormax_dec=pormax_dec, pormin_dec=pormin_dec, precip=precip, \
            preciplimit=preciplimit, preciplimitalb=preciplimitalb, press_hpa=press_hpa, \
            qf0_beu=qf0_beu, qf_a=qf_a, qf_b=qf_b, qf_c=qf_c, qn1_obs=qn1_obs, \
            qs_obs=qs_obs, qf_obs=qf_obs, radmeltfact=radmeltfact, raincover=raincover, \
            rainmaxres=rainmaxres, resp_a=resp_a, resp_b=resp_b, \
            roughlenheatmethod=roughlenheatmethod, roughlenmommethod=roughlenmommethod, \
            runofftowater=runofftowater, s1=s1, s2=s2, \
            sathydraulicconduct=sathydraulicconduct, sddfull=sddfull, sdd_id=sdd_id, \
            smdmethod=smdmethod, snowalb=snowalb, snowalbmax=snowalbmax, \
            snowalbmin=snowalbmin, snowpacklimit=snowpacklimit, snowdens=snowdens, \
            snowdensmax=snowdensmax, snowdensmin=snowdensmin, snowfallcum=snowfallcum, \
            snowfrac=snowfrac, snowlimbldg=snowlimbldg, snowlimpaved=snowlimpaved, \
            snowfrac_obs=snowfrac_obs, snowpack=snowpack, snowprof_24hr=snowprof_24hr, \
            snowuse=snowuse, soildepth=soildepth, stabilitymethod=stabilitymethod, \
            startdls=startdls, soilstore_surf=soilstore_surf, \
            soilstorecap_surf=soilstorecap_surf, state_surf=state_surf, \
            statelimit_surf=statelimit_surf, wetthresh_surf=wetthresh_surf, \
            soilstore_roof=soilstore_roof, soilstorecap_roof=soilstorecap_roof, \
            state_roof=state_roof, statelimit_roof=statelimit_roof, \
            wetthresh_roof=wetthresh_roof, soilstore_wall=soilstore_wall, \
            soilstorecap_wall=soilstorecap_wall, state_wall=state_wall, \
            statelimit_wall=statelimit_wall, wetthresh_wall=wetthresh_wall, \
            storageheatmethod=storageheatmethod, storedrainprm=storedrainprm, \
            surfacearea=surfacearea, tair_av=tair_av, tau_a=tau_a, tau_f=tau_f, \
            tau_r=tau_r, tmax_id=tmax_id, tmin_id=tmin_id, baset_cooling=baset_cooling, \
            baset_heating=baset_heating, temp_c=temp_c, tempmeltfact=tempmeltfact, \
            th=th, theta_bioco2=theta_bioco2, timezone=timezone, tl=tl, \
            trafficrate=trafficrate, trafficunits=trafficunits, sfr_surf=sfr_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, tsfc_surf=tsfc_surf, \
            temp_roof=temp_roof, temp_wall=temp_wall, temp_surf=temp_surf, \
            tin_roof=tin_roof, tin_wall=tin_wall, tin_surf=tin_surf, k_roof=k_roof, \
            k_wall=k_wall, k_surf=k_surf, cp_roof=cp_roof, cp_wall=cp_wall, \
            cp_surf=cp_surf, dz_roof=dz_roof, dz_wall=dz_wall, dz_surf=dz_surf, \
            traffprof_24hr=traffprof_24hr, ts5mindata_ir=ts5mindata_ir, tstep=tstep, \
            tstep_prev=tstep_prev, veg_type=veg_type, waterdist=waterdist, \
            waterusemethod=waterusemethod, wu_m3=wu_m3, wuday_id=wuday_id, \
            decidcap_id=decidcap_id, albdectr_id=albdectr_id, albevetr_id=albevetr_id, \
            albgrass_id=albgrass_id, porosity_id=porosity_id, wuprofa_24hr=wuprofa_24hr, \
            wuprofm_24hr=wuprofm_24hr, xsmd=xsmd, z=z, z0m_in=z0m_in, zdm_in=zdm_in)
        output_line_suews = \
            f90wrap.runtime.lookup_class("supy_driver.output_line").from_handle(output_line_suews, \
            alloc=True)
        return output_line_suews
    
    @staticmethod
    def suews_cal_main_dts(ah_min, ahprof_24hr, ah_slope_cooling, ah_slope_heating, \
        alb, albmax_dectr, albmax_evetr, albmax_grass, albmin_dectr, albmin_evetr, \
        albmin_grass, alpha_bioco2, alpha_enh_bioco2, alt, kdown, avrh, avu1, baset, \
        basete, beta_bioco2, beta_enh_bioco2, bldgh, capmax_dec, capmin_dec, \
        chanohm, co2pointsource, cpanohm, crwmax, crwmin, daywat, daywatper, \
        dectreeh, diagmethod, diagnose, drainrt, dt_since_start, dqndt, qn_av, \
        dqnsdt, qn_s_av, ef_umolco2perj, emis, emissionsmethod, enef_v_jkm, enddls, \
        evetreeh, faibldg, faidectree, faievetree, faimethod, faut, fcef_v_kgkm, \
        fcld_obs, flowchange, frfossilfuel_heat, frfossilfuel_nonheat, g_max, g_k, \
        g_q_base, g_q_shape, g_t, g_sm, gdd_id, gddfull, gridiv, gsmodel, \
        h_maintain, hdd_id, humactivity_24hr, icefrac, id, ie_a, ie_end, ie_m, \
        ie_start, imin, internalwateruse_h, irrfracpaved, irrfracbldgs, \
        irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, irrfracwater, isec, \
        it, iy, kkanohm, kmax, lai_id, laimax, laimin, lai_obs, laipower, laitype, \
        lat, lenday_id, ldown_obs, lng, maxconductance, maxfcmetab, maxqfmetab, \
        snowwater, minfcmetab, minqfmetab, min_res_bioco2, narp_emis_snow, \
        narp_trans_site, netradiationmethod, nlayer, n_vegetation_region_urban, \
        n_stream_sw_urban, n_stream_lw_urban, sw_dn_direct_frac, air_ext_sw, \
        air_ssa_sw, veg_ssa_sw, air_ext_lw, air_ssa_lw, veg_ssa_lw, veg_fsd_const, \
        veg_contact_fraction_const, ground_albedo_dir_mult_fact, \
        use_sw_direct_albedo, height, building_frac, veg_frac, building_scale, \
        veg_scale, alb_roof, emis_roof, alb_wall, emis_wall, \
        roof_albedo_dir_mult_fact, wall_specular_frac, ohm_coef, ohmincqf, \
        ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, popdensnighttime, \
        popprof_24hr, pormax_dec, pormin_dec, precip, preciplimit, preciplimitalb, \
        press_hpa, qf0_beu, qf_a, qf_b, qf_c, qn1_obs, qs_obs, qf_obs, radmeltfact, \
        raincover, rainmaxres, resp_a, resp_b, roughlenheatmethod, \
        roughlenmommethod, runofftowater, s1, s2, sathydraulicconduct, sddfull, \
        sdd_id, smdmethod, snowalb, snowalbmax, snowalbmin, snowpacklimit, snowdens, \
        snowdensmax, snowdensmin, snowfallcum, snowfrac, snowlimbldg, snowlimpaved, \
        snowfrac_obs, snowpack, snowprof_24hr, snowuse, soildepth, stabilitymethod, \
        startdls, soilstore_surf, soilstorecap_surf, state_surf, statelimit_surf, \
        wetthresh_surf, soilstore_roof, soilstorecap_roof, state_roof, \
        statelimit_roof, wetthresh_roof, soilstore_wall, soilstorecap_wall, \
        state_wall, statelimit_wall, wetthresh_wall, storageheatmethod, \
        storedrainprm, surfacearea, tair_av, tau_a, tau_f, tau_r, tmax_id, tmin_id, \
        baset_cooling, baset_heating, temp_c, tempmeltfact, th, theta_bioco2, \
        timezone, tl, trafficrate, trafficunits, sfr_surf, tsfc_roof, tsfc_wall, \
        tsfc_surf, temp_roof, temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, \
        k_roof, k_wall, k_surf, cp_roof, cp_wall, cp_surf, dz_roof, dz_wall, \
        dz_surf, traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, \
        waterdist, waterusemethod, wu_m3, wuday_id, decidcap_id, albdectr_id, \
        albevetr_id, albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, xsmd, z, \
        z0m_in, zdm_in):
        """
        output_line_suews = suews_cal_main_dts(ah_min, ahprof_24hr, ah_slope_cooling, \
            ah_slope_heating, alb, albmax_dectr, albmax_evetr, albmax_grass, \
            albmin_dectr, albmin_evetr, albmin_grass, alpha_bioco2, alpha_enh_bioco2, \
            alt, kdown, avrh, avu1, baset, basete, beta_bioco2, beta_enh_bioco2, bldgh, \
            capmax_dec, capmin_dec, chanohm, co2pointsource, cpanohm, crwmax, crwmin, \
            daywat, daywatper, dectreeh, diagmethod, diagnose, drainrt, dt_since_start, \
            dqndt, qn_av, dqnsdt, qn_s_av, ef_umolco2perj, emis, emissionsmethod, \
            enef_v_jkm, enddls, evetreeh, faibldg, faidectree, faievetree, faimethod, \
            faut, fcef_v_kgkm, fcld_obs, flowchange, frfossilfuel_heat, \
            frfossilfuel_nonheat, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, gdd_id, \
            gddfull, gridiv, gsmodel, h_maintain, hdd_id, humactivity_24hr, icefrac, id, \
            ie_a, ie_end, ie_m, ie_start, imin, internalwateruse_h, irrfracpaved, \
            irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, \
            irrfracwater, isec, it, iy, kkanohm, kmax, lai_id, laimax, laimin, lai_obs, \
            laipower, laitype, lat, lenday_id, ldown_obs, lng, maxconductance, \
            maxfcmetab, maxqfmetab, snowwater, minfcmetab, minqfmetab, min_res_bioco2, \
            narp_emis_snow, narp_trans_site, netradiationmethod, nlayer, \
            n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
            emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, ohm_coef, \
            ohmincqf, ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, \
            popdensnighttime, popprof_24hr, pormax_dec, pormin_dec, precip, preciplimit, \
            preciplimitalb, press_hpa, qf0_beu, qf_a, qf_b, qf_c, qn1_obs, qs_obs, \
            qf_obs, radmeltfact, raincover, rainmaxres, resp_a, resp_b, \
            roughlenheatmethod, roughlenmommethod, runofftowater, s1, s2, \
            sathydraulicconduct, sddfull, sdd_id, smdmethod, snowalb, snowalbmax, \
            snowalbmin, snowpacklimit, snowdens, snowdensmax, snowdensmin, snowfallcum, \
            snowfrac, snowlimbldg, snowlimpaved, snowfrac_obs, snowpack, snowprof_24hr, \
            snowuse, soildepth, stabilitymethod, startdls, soilstore_surf, \
            soilstorecap_surf, state_surf, statelimit_surf, wetthresh_surf, \
            soilstore_roof, soilstorecap_roof, state_roof, statelimit_roof, \
            wetthresh_roof, soilstore_wall, soilstorecap_wall, state_wall, \
            statelimit_wall, wetthresh_wall, storageheatmethod, storedrainprm, \
            surfacearea, tair_av, tau_a, tau_f, tau_r, tmax_id, tmin_id, baset_cooling, \
            baset_heating, temp_c, tempmeltfact, th, theta_bioco2, timezone, tl, \
            trafficrate, trafficunits, sfr_surf, tsfc_roof, tsfc_wall, tsfc_surf, \
            temp_roof, temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, k_roof, \
            k_wall, k_surf, cp_roof, cp_wall, cp_surf, dz_roof, dz_wall, dz_surf, \
            traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, waterdist, \
            waterusemethod, wu_m3, wuday_id, decidcap_id, albdectr_id, albevetr_id, \
            albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, xsmd, z, z0m_in, \
            zdm_in)
        
        
        Defined at suews_ctrl_driver.fpp lines 2071-4569
        
        Parameters
        ----------
        ah_min : float array
        ahprof_24hr : float array
        ah_slope_cooling : float array
        ah_slope_heating : float array
        alb : float array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        alpha_bioco2 : float array
        alpha_enh_bioco2 : float array
        alt : float
        kdown : float
        avrh : float
        avu1 : float
        baset : float array
        basete : float array
        beta_bioco2 : float array
        beta_enh_bioco2 : float array
        bldgh : float
        capmax_dec : float
        capmin_dec : float
        chanohm : float array
        co2pointsource : float
        cpanohm : float array
        crwmax : float
        crwmin : float
        daywat : float array
        daywatper : float array
        dectreeh : float
        diagmethod : int
        diagnose : int
        drainrt : float
        dt_since_start : int
        dqndt : float
        qn_av : float
        dqnsdt : float
        qn_s_av : float
        ef_umolco2perj : float
        emis : float array
        emissionsmethod : int
        enef_v_jkm : float
        enddls : int
        evetreeh : float
        faibldg : float
        faidectree : float
        faievetree : float
        faimethod : int
        faut : float
        fcef_v_kgkm : float array
        fcld_obs : float
        flowchange : float
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        gdd_id : float array
        gddfull : float array
        gridiv : int
        gsmodel : int
        h_maintain : float
        hdd_id : float array
        humactivity_24hr : float array
        icefrac : float array
        id : int
        ie_a : float array
        ie_end : int
        ie_m : float array
        ie_start : int
        imin : int
        internalwateruse_h : float
        irrfracpaved : float
        irrfracbldgs : float
        irrfracevetr : float
        irrfracdectr : float
        irrfracgrass : float
        irrfracbsoil : float
        irrfracwater : float
        isec : int
        it : int
        iy : int
        kkanohm : float array
        kmax : float
        lai_id : float array
        laimax : float array
        laimin : float array
        lai_obs : float
        laipower : float array
        laitype : int array
        lat : float
        lenday_id : float
        ldown_obs : float
        lng : float
        maxconductance : float array
        maxfcmetab : float
        maxqfmetab : float
        snowwater : float array
        minfcmetab : float
        minqfmetab : float
        min_res_bioco2 : float array
        narp_emis_snow : float
        narp_trans_site : float
        netradiationmethod : int
        nlayer : int
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        ohm_coef : float array
        ohmincqf : int
        ohm_threshsw : float array
        ohm_threshwd : float array
        pipecapacity : float
        popdensdaytime : float array
        popdensnighttime : float
        popprof_24hr : float array
        pormax_dec : float
        pormin_dec : float
        precip : float
        preciplimit : float
        preciplimitalb : float
        press_hpa : float
        qf0_beu : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        qn1_obs : float
        qs_obs : float
        qf_obs : float
        radmeltfact : float
        raincover : float
        rainmaxres : float
        resp_a : float array
        resp_b : float array
        roughlenheatmethod : int
        roughlenmommethod : int
        runofftowater : float
        s1 : float
        s2 : float
        sathydraulicconduct : float array
        sddfull : float array
        sdd_id : float array
        smdmethod : int
        snowalb : float
        snowalbmax : float
        snowalbmin : float
        snowpacklimit : float array
        snowdens : float array
        snowdensmax : float
        snowdensmin : float
        snowfallcum : float
        snowfrac : float array
        snowlimbldg : float
        snowlimpaved : float
        snowfrac_obs : float
        snowpack : float array
        snowprof_24hr : float array
        snowuse : int
        soildepth : float array
        stabilitymethod : int
        startdls : int
        soilstore_surf : float array
        soilstorecap_surf : float array
        state_surf : float array
        statelimit_surf : float array
        wetthresh_surf : float array
        soilstore_roof : float array
        soilstorecap_roof : float array
        state_roof : float array
        statelimit_roof : float array
        wetthresh_roof : float array
        soilstore_wall : float array
        soilstorecap_wall : float array
        state_wall : float array
        statelimit_wall : float array
        wetthresh_wall : float array
        storageheatmethod : int
        storedrainprm : float array
        surfacearea : float
        tair_av : float
        tau_a : float
        tau_f : float
        tau_r : float
        tmax_id : float
        tmin_id : float
        baset_cooling : float array
        baset_heating : float array
        temp_c : float
        tempmeltfact : float
        th : float
        theta_bioco2 : float array
        timezone : float
        tl : float
        trafficrate : float array
        trafficunits : float
        sfr_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        tsfc_surf : float array
        temp_roof : float array
        temp_wall : float array
        temp_surf : float array
        tin_roof : float array
        tin_wall : float array
        tin_surf : float array
        k_roof : float array
        k_wall : float array
        k_surf : float array
        cp_roof : float array
        cp_wall : float array
        cp_surf : float array
        dz_roof : float array
        dz_wall : float array
        dz_surf : float array
        traffprof_24hr : float array
        ts5mindata_ir : float array
        tstep : int
        tstep_prev : int
        veg_type : int
        waterdist : float array
        waterusemethod : int
        wu_m3 : float
        wuday_id : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        wuprofa_24hr : float array
        wuprofm_24hr : float array
        xsmd : float
        z : float
        z0m_in : float
        zdm_in : float
        
        Returns
        -------
        output_line_suews : Output_Line
        
        ==============main calculation start=======================
        ==============surface roughness calculation=======================
        """
        output_line_suews = _supy_driver.f90wrap_suews_cal_main_dts(ah_min=ah_min, \
            ahprof_24hr=ahprof_24hr, ah_slope_cooling=ah_slope_cooling, \
            ah_slope_heating=ah_slope_heating, alb=alb, albmax_dectr=albmax_dectr, \
            albmax_evetr=albmax_evetr, albmax_grass=albmax_grass, \
            albmin_dectr=albmin_dectr, albmin_evetr=albmin_evetr, \
            albmin_grass=albmin_grass, alpha_bioco2=alpha_bioco2, \
            alpha_enh_bioco2=alpha_enh_bioco2, alt=alt, kdown=kdown, avrh=avrh, \
            avu1=avu1, baset=baset, basete=basete, beta_bioco2=beta_bioco2, \
            beta_enh_bioco2=beta_enh_bioco2, bldgh=bldgh, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, chanohm=chanohm, co2pointsource=co2pointsource, \
            cpanohm=cpanohm, crwmax=crwmax, crwmin=crwmin, daywat=daywat, \
            daywatper=daywatper, dectreeh=dectreeh, diagmethod=diagmethod, \
            diagnose=diagnose, drainrt=drainrt, dt_since_start=dt_since_start, \
            dqndt=dqndt, qn_av=qn_av, dqnsdt=dqnsdt, qn_s_av=qn_s_av, \
            ef_umolco2perj=ef_umolco2perj, emis=emis, emissionsmethod=emissionsmethod, \
            enef_v_jkm=enef_v_jkm, enddls=enddls, evetreeh=evetreeh, faibldg=faibldg, \
            faidectree=faidectree, faievetree=faievetree, faimethod=faimethod, \
            faut=faut, fcef_v_kgkm=fcef_v_kgkm, fcld_obs=fcld_obs, \
            flowchange=flowchange, frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, gdd_id=gdd_id, \
            gddfull=gddfull, gridiv=gridiv, gsmodel=gsmodel, h_maintain=h_maintain, \
            hdd_id=hdd_id, humactivity_24hr=humactivity_24hr, icefrac=icefrac, id=id, \
            ie_a=ie_a, ie_end=ie_end, ie_m=ie_m, ie_start=ie_start, imin=imin, \
            internalwateruse_h=internalwateruse_h, irrfracpaved=irrfracpaved, \
            irrfracbldgs=irrfracbldgs, irrfracevetr=irrfracevetr, \
            irrfracdectr=irrfracdectr, irrfracgrass=irrfracgrass, \
            irrfracbsoil=irrfracbsoil, irrfracwater=irrfracwater, isec=isec, it=it, \
            iy=iy, kkanohm=kkanohm, kmax=kmax, lai_id=lai_id, laimax=laimax, \
            laimin=laimin, lai_obs=lai_obs, laipower=laipower, laitype=laitype, lat=lat, \
            lenday_id=lenday_id, ldown_obs=ldown_obs, lng=lng, \
            maxconductance=maxconductance, maxfcmetab=maxfcmetab, maxqfmetab=maxqfmetab, \
            snowwater=snowwater, minfcmetab=minfcmetab, minqfmetab=minqfmetab, \
            min_res_bioco2=min_res_bioco2, narp_emis_snow=narp_emis_snow, \
            narp_trans_site=narp_trans_site, netradiationmethod=netradiationmethod, \
            nlayer=nlayer, n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, \
            building_scale=building_scale, veg_scale=veg_scale, alb_roof=alb_roof, \
            emis_roof=emis_roof, alb_wall=alb_wall, emis_wall=emis_wall, \
            roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, ohm_coef=ohm_coef, ohmincqf=ohmincqf, \
            ohm_threshsw=ohm_threshsw, ohm_threshwd=ohm_threshwd, \
            pipecapacity=pipecapacity, popdensdaytime=popdensdaytime, \
            popdensnighttime=popdensnighttime, popprof_24hr=popprof_24hr, \
            pormax_dec=pormax_dec, pormin_dec=pormin_dec, precip=precip, \
            preciplimit=preciplimit, preciplimitalb=preciplimitalb, press_hpa=press_hpa, \
            qf0_beu=qf0_beu, qf_a=qf_a, qf_b=qf_b, qf_c=qf_c, qn1_obs=qn1_obs, \
            qs_obs=qs_obs, qf_obs=qf_obs, radmeltfact=radmeltfact, raincover=raincover, \
            rainmaxres=rainmaxres, resp_a=resp_a, resp_b=resp_b, \
            roughlenheatmethod=roughlenheatmethod, roughlenmommethod=roughlenmommethod, \
            runofftowater=runofftowater, s1=s1, s2=s2, \
            sathydraulicconduct=sathydraulicconduct, sddfull=sddfull, sdd_id=sdd_id, \
            smdmethod=smdmethod, snowalb=snowalb, snowalbmax=snowalbmax, \
            snowalbmin=snowalbmin, snowpacklimit=snowpacklimit, snowdens=snowdens, \
            snowdensmax=snowdensmax, snowdensmin=snowdensmin, snowfallcum=snowfallcum, \
            snowfrac=snowfrac, snowlimbldg=snowlimbldg, snowlimpaved=snowlimpaved, \
            snowfrac_obs=snowfrac_obs, snowpack=snowpack, snowprof_24hr=snowprof_24hr, \
            snowuse=snowuse, soildepth=soildepth, stabilitymethod=stabilitymethod, \
            startdls=startdls, soilstore_surf=soilstore_surf, \
            soilstorecap_surf=soilstorecap_surf, state_surf=state_surf, \
            statelimit_surf=statelimit_surf, wetthresh_surf=wetthresh_surf, \
            soilstore_roof=soilstore_roof, soilstorecap_roof=soilstorecap_roof, \
            state_roof=state_roof, statelimit_roof=statelimit_roof, \
            wetthresh_roof=wetthresh_roof, soilstore_wall=soilstore_wall, \
            soilstorecap_wall=soilstorecap_wall, state_wall=state_wall, \
            statelimit_wall=statelimit_wall, wetthresh_wall=wetthresh_wall, \
            storageheatmethod=storageheatmethod, storedrainprm=storedrainprm, \
            surfacearea=surfacearea, tair_av=tair_av, tau_a=tau_a, tau_f=tau_f, \
            tau_r=tau_r, tmax_id=tmax_id, tmin_id=tmin_id, baset_cooling=baset_cooling, \
            baset_heating=baset_heating, temp_c=temp_c, tempmeltfact=tempmeltfact, \
            th=th, theta_bioco2=theta_bioco2, timezone=timezone, tl=tl, \
            trafficrate=trafficrate, trafficunits=trafficunits, sfr_surf=sfr_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, tsfc_surf=tsfc_surf, \
            temp_roof=temp_roof, temp_wall=temp_wall, temp_surf=temp_surf, \
            tin_roof=tin_roof, tin_wall=tin_wall, tin_surf=tin_surf, k_roof=k_roof, \
            k_wall=k_wall, k_surf=k_surf, cp_roof=cp_roof, cp_wall=cp_wall, \
            cp_surf=cp_surf, dz_roof=dz_roof, dz_wall=dz_wall, dz_surf=dz_surf, \
            traffprof_24hr=traffprof_24hr, ts5mindata_ir=ts5mindata_ir, tstep=tstep, \
            tstep_prev=tstep_prev, veg_type=veg_type, waterdist=waterdist, \
            waterusemethod=waterusemethod, wu_m3=wu_m3, wuday_id=wuday_id, \
            decidcap_id=decidcap_id, albdectr_id=albdectr_id, albevetr_id=albevetr_id, \
            albgrass_id=albgrass_id, porosity_id=porosity_id, wuprofa_24hr=wuprofa_24hr, \
            wuprofm_24hr=wuprofm_24hr, xsmd=xsmd, z=z, z0m_in=z0m_in, zdm_in=zdm_in)
        output_line_suews = \
            f90wrap.runtime.lookup_class("supy_driver.output_line").from_handle(output_line_suews, \
            alloc=True)
        return output_line_suews
    
    @staticmethod
    def suews_cal_anthropogenicemission(ah_min, ahprof_24hr, ah_slope_cooling, \
        ah_slope_heating, co2pointsource, dayofweek_id, dls, ef_umolco2perj, \
        emissionsmethod, enef_v_jkm, fcef_v_kgkm, frfossilfuel_heat, \
        frfossilfuel_nonheat, hdd_id, humactivity_24hr, imin, it, maxfcmetab, \
        maxqfmetab, minfcmetab, minqfmetab, popdensdaytime, popdensnighttime, \
        popprof_24hr, qf0_beu, qf_a, qf_b, qf_c, qf_obs, surfacearea, baset_cooling, \
        baset_heating, temp_c, trafficrate, trafficunits, traffprof_24hr):
        """
        qf, qf_sahp, fc_anthro, fc_build, fc_metab, fc_point, fc_traff = \
            suews_cal_anthropogenicemission(ah_min, ahprof_24hr, ah_slope_cooling, \
            ah_slope_heating, co2pointsource, dayofweek_id, dls, ef_umolco2perj, \
            emissionsmethod, enef_v_jkm, fcef_v_kgkm, frfossilfuel_heat, \
            frfossilfuel_nonheat, hdd_id, humactivity_24hr, imin, it, maxfcmetab, \
            maxqfmetab, minfcmetab, minqfmetab, popdensdaytime, popdensnighttime, \
            popprof_24hr, qf0_beu, qf_a, qf_b, qf_c, qf_obs, surfacearea, baset_cooling, \
            baset_heating, temp_c, trafficrate, trafficunits, traffprof_24hr)
        
        
        Defined at suews_ctrl_driver.fpp lines 4581-4682
        
        Parameters
        ----------
        ah_min : float array
        ahprof_24hr : float array
        ah_slope_cooling : float array
        ah_slope_heating : float array
        co2pointsource : float
        dayofweek_id : int array
        dls : int
        ef_umolco2perj : float
        emissionsmethod : int
        enef_v_jkm : float
        fcef_v_kgkm : float array
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        hdd_id : float array
        humactivity_24hr : float array
        imin : int
        it : int
        maxfcmetab : float
        maxqfmetab : float
        minfcmetab : float
        minqfmetab : float
        popdensdaytime : float array
        popdensnighttime : float
        popprof_24hr : float array
        qf0_beu : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        qf_obs : float
        surfacearea : float
        baset_cooling : float array
        baset_heating : float array
        temp_c : float
        trafficrate : float array
        trafficunits : float
        traffprof_24hr : float array
        
        Returns
        -------
        qf : float
        qf_sahp : float
        fc_anthro : float
        fc_build : float
        fc_metab : float
        fc_point : float
        fc_traff : float
        
        """
        qf, qf_sahp, fc_anthro, fc_build, fc_metab, fc_point, fc_traff = \
            _supy_driver.f90wrap_suews_cal_anthropogenicemission(ah_min=ah_min, \
            ahprof_24hr=ahprof_24hr, ah_slope_cooling=ah_slope_cooling, \
            ah_slope_heating=ah_slope_heating, co2pointsource=co2pointsource, \
            dayofweek_id=dayofweek_id, dls=dls, ef_umolco2perj=ef_umolco2perj, \
            emissionsmethod=emissionsmethod, enef_v_jkm=enef_v_jkm, \
            fcef_v_kgkm=fcef_v_kgkm, frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, hdd_id=hdd_id, \
            humactivity_24hr=humactivity_24hr, imin=imin, it=it, maxfcmetab=maxfcmetab, \
            maxqfmetab=maxqfmetab, minfcmetab=minfcmetab, minqfmetab=minqfmetab, \
            popdensdaytime=popdensdaytime, popdensnighttime=popdensnighttime, \
            popprof_24hr=popprof_24hr, qf0_beu=qf0_beu, qf_a=qf_a, qf_b=qf_b, qf_c=qf_c, \
            qf_obs=qf_obs, surfacearea=surfacearea, baset_cooling=baset_cooling, \
            baset_heating=baset_heating, temp_c=temp_c, trafficrate=trafficrate, \
            trafficunits=trafficunits, traffprof_24hr=traffprof_24hr)
        return qf, qf_sahp, fc_anthro, fc_build, fc_metab, fc_point, fc_traff
    
    @staticmethod
    def suews_cal_anthropogenicemission_dts(ah_min_working, ah_min_holiday, \
        ahprof_24hr_working, ahprof_24hr_holiday, ah_slope_cooling_working, \
        ah_slope_cooling_holiday, ah_slope_heating_working, \
        ah_slope_heating_holiday, co2pointsource, dayofweek_id, dls, ef_umolco2perj, \
        emissionsmethod, enef_v_jkm, fcef_v_kgkm, frfossilfuel_heat, \
        frfossilfuel_nonheat, hdd_id, humactivity_24hr_working, \
        humactivity_24hr_holiday, imin, it, maxfcmetab, maxqfmetab, minfcmetab, \
        minqfmetab, popdensdaytime_working, popdensdaytime_holiday, \
        popdensnighttime, popprof_24hr_working, popprof_24hr_holiday, \
        qf0_beu_working, qf0_beu_holiday, qf_a_working, qf_a_holiday, qf_b_working, \
        qf_b_holiday, qf_c_working, qf_c_holiday, qf_obs, surfacearea, \
        baset_cooling_working, baset_cooling_holiday, baset_heating_working, \
        baset_heating_holiday, temp_c, trafficrate_working, trafficrate_holiday, \
        trafficunits, traffprof_24hr_working, traffprof_24hr_holiday):
        """
        qf, qf_sahp, fc_anthro, fc_build, fc_metab, fc_point, fc_traff = \
            suews_cal_anthropogenicemission_dts(ah_min_working, ah_min_holiday, \
            ahprof_24hr_working, ahprof_24hr_holiday, ah_slope_cooling_working, \
            ah_slope_cooling_holiday, ah_slope_heating_working, \
            ah_slope_heating_holiday, co2pointsource, dayofweek_id, dls, ef_umolco2perj, \
            emissionsmethod, enef_v_jkm, fcef_v_kgkm, frfossilfuel_heat, \
            frfossilfuel_nonheat, hdd_id, humactivity_24hr_working, \
            humactivity_24hr_holiday, imin, it, maxfcmetab, maxqfmetab, minfcmetab, \
            minqfmetab, popdensdaytime_working, popdensdaytime_holiday, \
            popdensnighttime, popprof_24hr_working, popprof_24hr_holiday, \
            qf0_beu_working, qf0_beu_holiday, qf_a_working, qf_a_holiday, qf_b_working, \
            qf_b_holiday, qf_c_working, qf_c_holiday, qf_obs, surfacearea, \
            baset_cooling_working, baset_cooling_holiday, baset_heating_working, \
            baset_heating_holiday, temp_c, trafficrate_working, trafficrate_holiday, \
            trafficunits, traffprof_24hr_working, traffprof_24hr_holiday)
        
        
        Defined at suews_ctrl_driver.fpp lines 4684-4824
        
        Parameters
        ----------
        ah_min_working : float
        ah_min_holiday : float
        ahprof_24hr_working : float array
        ahprof_24hr_holiday : float array
        ah_slope_cooling_working : float
        ah_slope_cooling_holiday : float
        ah_slope_heating_working : float
        ah_slope_heating_holiday : float
        co2pointsource : float
        dayofweek_id : int array
        dls : int
        ef_umolco2perj : float
        emissionsmethod : int
        enef_v_jkm : float
        fcef_v_kgkm : float array
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        hdd_id : float array
        humactivity_24hr_working : float array
        humactivity_24hr_holiday : float array
        imin : int
        it : int
        maxfcmetab : float
        maxqfmetab : float
        minfcmetab : float
        minqfmetab : float
        popdensdaytime_working : float
        popdensdaytime_holiday : float
        popdensnighttime : float
        popprof_24hr_working : float array
        popprof_24hr_holiday : float array
        qf0_beu_working : float
        qf0_beu_holiday : float
        qf_a_working : float
        qf_a_holiday : float
        qf_b_working : float
        qf_b_holiday : float
        qf_c_working : float
        qf_c_holiday : float
        qf_obs : float
        surfacearea : float
        baset_cooling_working : float
        baset_cooling_holiday : float
        baset_heating_working : float
        baset_heating_holiday : float
        temp_c : float
        trafficrate_working : float
        trafficrate_holiday : float
        trafficunits : float
        traffprof_24hr_working : float array
        traffprof_24hr_holiday : float array
        
        Returns
        -------
        qf : float
        qf_sahp : float
        fc_anthro : float
        fc_build : float
        fc_metab : float
        fc_point : float
        fc_traff : float
        
        """
        qf, qf_sahp, fc_anthro, fc_build, fc_metab, fc_point, fc_traff = \
            _supy_driver.f90wrap_suews_cal_anthropogenicemission_dts(ah_min_working=ah_min_working, \
            ah_min_holiday=ah_min_holiday, ahprof_24hr_working=ahprof_24hr_working, \
            ahprof_24hr_holiday=ahprof_24hr_holiday, \
            ah_slope_cooling_working=ah_slope_cooling_working, \
            ah_slope_cooling_holiday=ah_slope_cooling_holiday, \
            ah_slope_heating_working=ah_slope_heating_working, \
            ah_slope_heating_holiday=ah_slope_heating_holiday, \
            co2pointsource=co2pointsource, dayofweek_id=dayofweek_id, dls=dls, \
            ef_umolco2perj=ef_umolco2perj, emissionsmethod=emissionsmethod, \
            enef_v_jkm=enef_v_jkm, fcef_v_kgkm=fcef_v_kgkm, \
            frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, hdd_id=hdd_id, \
            humactivity_24hr_working=humactivity_24hr_working, \
            humactivity_24hr_holiday=humactivity_24hr_holiday, imin=imin, it=it, \
            maxfcmetab=maxfcmetab, maxqfmetab=maxqfmetab, minfcmetab=minfcmetab, \
            minqfmetab=minqfmetab, popdensdaytime_working=popdensdaytime_working, \
            popdensdaytime_holiday=popdensdaytime_holiday, \
            popdensnighttime=popdensnighttime, \
            popprof_24hr_working=popprof_24hr_working, \
            popprof_24hr_holiday=popprof_24hr_holiday, qf0_beu_working=qf0_beu_working, \
            qf0_beu_holiday=qf0_beu_holiday, qf_a_working=qf_a_working, \
            qf_a_holiday=qf_a_holiday, qf_b_working=qf_b_working, \
            qf_b_holiday=qf_b_holiday, qf_c_working=qf_c_working, \
            qf_c_holiday=qf_c_holiday, qf_obs=qf_obs, surfacearea=surfacearea, \
            baset_cooling_working=baset_cooling_working, \
            baset_cooling_holiday=baset_cooling_holiday, \
            baset_heating_working=baset_heating_working, \
            baset_heating_holiday=baset_heating_holiday, temp_c=temp_c, \
            trafficrate_working=trafficrate_working, \
            trafficrate_holiday=trafficrate_holiday, trafficunits=trafficunits, \
            traffprof_24hr_working=traffprof_24hr_working, \
            traffprof_24hr_holiday=traffprof_24hr_holiday)
        return qf, qf_sahp, fc_anthro, fc_build, fc_metab, fc_point, fc_traff
    
    @staticmethod
    def suews_cal_biogenco2(alpha_bioco2, alpha_enh_bioco2, avkdn, avrh, \
        beta_bioco2, beta_enh_bioco2, dectime, diagnose, emissionsmethod, fc_anthro, \
        g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, gfunc, gsmodel, id, it, kmax, \
        lai_id, laimin, laimax, maxconductance, min_res_bioco2, press_hpa, resp_a, \
        resp_b, s1, s2, sfr_surf, smdmethod, snowfrac, t2_c, temp_c, theta_bioco2, \
        th, tl, vsmd, xsmd):
        """
        fc, fc_biogen, fc_photo, fc_respi = suews_cal_biogenco2(alpha_bioco2, \
            alpha_enh_bioco2, avkdn, avrh, beta_bioco2, beta_enh_bioco2, dectime, \
            diagnose, emissionsmethod, fc_anthro, g_max, g_k, g_q_base, g_q_shape, g_t, \
            g_sm, gfunc, gsmodel, id, it, kmax, lai_id, laimin, laimax, maxconductance, \
            min_res_bioco2, press_hpa, resp_a, resp_b, s1, s2, sfr_surf, smdmethod, \
            snowfrac, t2_c, temp_c, theta_bioco2, th, tl, vsmd, xsmd)
        
        
        Defined at suews_ctrl_driver.fpp lines 4834-4960
        
        Parameters
        ----------
        alpha_bioco2 : float array
        alpha_enh_bioco2 : float array
        avkdn : float
        avrh : float
        beta_bioco2 : float array
        beta_enh_bioco2 : float array
        dectime : float
        diagnose : int
        emissionsmethod : int
        fc_anthro : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        gfunc : float
        gsmodel : int
        id : int
        it : int
        kmax : float
        lai_id : float array
        laimin : float array
        laimax : float array
        maxconductance : float array
        min_res_bioco2 : float array
        press_hpa : float
        resp_a : float array
        resp_b : float array
        s1 : float
        s2 : float
        sfr_surf : float array
        smdmethod : int
        snowfrac : float array
        t2_c : float
        temp_c : float
        theta_bioco2 : float array
        th : float
        tl : float
        vsmd : float
        xsmd : float
        
        Returns
        -------
        fc : float
        fc_biogen : float
        fc_photo : float
        fc_respi : float
        
        """
        fc, fc_biogen, fc_photo, fc_respi = \
            _supy_driver.f90wrap_suews_cal_biogenco2(alpha_bioco2=alpha_bioco2, \
            alpha_enh_bioco2=alpha_enh_bioco2, avkdn=avkdn, avrh=avrh, \
            beta_bioco2=beta_bioco2, beta_enh_bioco2=beta_enh_bioco2, dectime=dectime, \
            diagnose=diagnose, emissionsmethod=emissionsmethod, fc_anthro=fc_anthro, \
            g_max=g_max, g_k=g_k, g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, \
            g_sm=g_sm, gfunc=gfunc, gsmodel=gsmodel, id=id, it=it, kmax=kmax, \
            lai_id=lai_id, laimin=laimin, laimax=laimax, maxconductance=maxconductance, \
            min_res_bioco2=min_res_bioco2, press_hpa=press_hpa, resp_a=resp_a, \
            resp_b=resp_b, s1=s1, s2=s2, sfr_surf=sfr_surf, smdmethod=smdmethod, \
            snowfrac=snowfrac, t2_c=t2_c, temp_c=temp_c, theta_bioco2=theta_bioco2, \
            th=th, tl=tl, vsmd=vsmd, xsmd=xsmd)
        return fc, fc_biogen, fc_photo, fc_respi
    
    @staticmethod
    def suews_cal_biogenco2_dts(alpha_bioco2_evetr, alpha_bioco2_dectr, \
        alpha_bioco2_grass, alpha_enh_bioco2_evetr, alpha_enh_bioco2_dectr, \
        alpha_enh_bioco2_grass, avkdn, avrh, beta_bioco2_evetr, beta_bioco2_dectr, \
        beta_bioco2_grass, beta_enh_bioco2_evetr, beta_enh_bioco2_dectr, \
        beta_enh_bioco2_grass, dectime, diagnose, emissionsmethod, fc_anthro, g_max, \
        g_k, g_q_base, g_q_shape, g_t, g_sm, gfunc, gsmodel, id, it, kmax, lai_id, \
        laimin_evetr, laimin_dectr, laimin_grass, laimax_evetr, laimax_dectr, \
        laimax_grass, maxconductance_evetr, maxconductance_dectr, \
        maxconductance_grass, min_res_bioco2_evetr, min_res_bioco2_dectr, \
        min_res_bioco2_grass, press_hpa, resp_a_evetr, resp_a_dectr, resp_a_grass, \
        resp_b_evetr, resp_b_dectr, resp_b_grass, s1, s2, sfr_paved, sfr_bldg, \
        sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, smdmethod, snowfrac, \
        t2_c, temp_c, theta_bioco2_evetr, theta_bioco2_dectr, theta_bioco2_grass, \
        th, tl, vsmd, xsmd):
        """
        fc, fc_biogen, fc_photo, fc_respi = suews_cal_biogenco2_dts(alpha_bioco2_evetr, \
            alpha_bioco2_dectr, alpha_bioco2_grass, alpha_enh_bioco2_evetr, \
            alpha_enh_bioco2_dectr, alpha_enh_bioco2_grass, avkdn, avrh, \
            beta_bioco2_evetr, beta_bioco2_dectr, beta_bioco2_grass, \
            beta_enh_bioco2_evetr, beta_enh_bioco2_dectr, beta_enh_bioco2_grass, \
            dectime, diagnose, emissionsmethod, fc_anthro, g_max, g_k, g_q_base, \
            g_q_shape, g_t, g_sm, gfunc, gsmodel, id, it, kmax, lai_id, laimin_evetr, \
            laimin_dectr, laimin_grass, laimax_evetr, laimax_dectr, laimax_grass, \
            maxconductance_evetr, maxconductance_dectr, maxconductance_grass, \
            min_res_bioco2_evetr, min_res_bioco2_dectr, min_res_bioco2_grass, press_hpa, \
            resp_a_evetr, resp_a_dectr, resp_a_grass, resp_b_evetr, resp_b_dectr, \
            resp_b_grass, s1, s2, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, \
            sfr_bsoil, sfr_water, smdmethod, snowfrac, t2_c, temp_c, theta_bioco2_evetr, \
            theta_bioco2_dectr, theta_bioco2_grass, th, tl, vsmd, xsmd)
        
        
        Defined at suews_ctrl_driver.fpp lines 4962-5120
        
        Parameters
        ----------
        alpha_bioco2_evetr : float
        alpha_bioco2_dectr : float
        alpha_bioco2_grass : float
        alpha_enh_bioco2_evetr : float
        alpha_enh_bioco2_dectr : float
        alpha_enh_bioco2_grass : float
        avkdn : float
        avrh : float
        beta_bioco2_evetr : float
        beta_bioco2_dectr : float
        beta_bioco2_grass : float
        beta_enh_bioco2_evetr : float
        beta_enh_bioco2_dectr : float
        beta_enh_bioco2_grass : float
        dectime : float
        diagnose : int
        emissionsmethod : int
        fc_anthro : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        gfunc : float
        gsmodel : int
        id : int
        it : int
        kmax : float
        lai_id : float array
        laimin_evetr : float
        laimin_dectr : float
        laimin_grass : float
        laimax_evetr : float
        laimax_dectr : float
        laimax_grass : float
        maxconductance_evetr : float
        maxconductance_dectr : float
        maxconductance_grass : float
        min_res_bioco2_evetr : float
        min_res_bioco2_dectr : float
        min_res_bioco2_grass : float
        press_hpa : float
        resp_a_evetr : float
        resp_a_dectr : float
        resp_a_grass : float
        resp_b_evetr : float
        resp_b_dectr : float
        resp_b_grass : float
        s1 : float
        s2 : float
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        smdmethod : int
        snowfrac : float array
        t2_c : float
        temp_c : float
        theta_bioco2_evetr : float
        theta_bioco2_dectr : float
        theta_bioco2_grass : float
        th : float
        tl : float
        vsmd : float
        xsmd : float
        
        Returns
        -------
        fc : float
        fc_biogen : float
        fc_photo : float
        fc_respi : float
        
        """
        fc, fc_biogen, fc_photo, fc_respi = \
            _supy_driver.f90wrap_suews_cal_biogenco2_dts(alpha_bioco2_evetr=alpha_bioco2_evetr, \
            alpha_bioco2_dectr=alpha_bioco2_dectr, \
            alpha_bioco2_grass=alpha_bioco2_grass, \
            alpha_enh_bioco2_evetr=alpha_enh_bioco2_evetr, \
            alpha_enh_bioco2_dectr=alpha_enh_bioco2_dectr, \
            alpha_enh_bioco2_grass=alpha_enh_bioco2_grass, avkdn=avkdn, avrh=avrh, \
            beta_bioco2_evetr=beta_bioco2_evetr, beta_bioco2_dectr=beta_bioco2_dectr, \
            beta_bioco2_grass=beta_bioco2_grass, \
            beta_enh_bioco2_evetr=beta_enh_bioco2_evetr, \
            beta_enh_bioco2_dectr=beta_enh_bioco2_dectr, \
            beta_enh_bioco2_grass=beta_enh_bioco2_grass, dectime=dectime, \
            diagnose=diagnose, emissionsmethod=emissionsmethod, fc_anthro=fc_anthro, \
            g_max=g_max, g_k=g_k, g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, \
            g_sm=g_sm, gfunc=gfunc, gsmodel=gsmodel, id=id, it=it, kmax=kmax, \
            lai_id=lai_id, laimin_evetr=laimin_evetr, laimin_dectr=laimin_dectr, \
            laimin_grass=laimin_grass, laimax_evetr=laimax_evetr, \
            laimax_dectr=laimax_dectr, laimax_grass=laimax_grass, \
            maxconductance_evetr=maxconductance_evetr, \
            maxconductance_dectr=maxconductance_dectr, \
            maxconductance_grass=maxconductance_grass, \
            min_res_bioco2_evetr=min_res_bioco2_evetr, \
            min_res_bioco2_dectr=min_res_bioco2_dectr, \
            min_res_bioco2_grass=min_res_bioco2_grass, press_hpa=press_hpa, \
            resp_a_evetr=resp_a_evetr, resp_a_dectr=resp_a_dectr, \
            resp_a_grass=resp_a_grass, resp_b_evetr=resp_b_evetr, \
            resp_b_dectr=resp_b_dectr, resp_b_grass=resp_b_grass, s1=s1, s2=s2, \
            sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, \
            sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, \
            sfr_water=sfr_water, smdmethod=smdmethod, snowfrac=snowfrac, t2_c=t2_c, \
            temp_c=temp_c, theta_bioco2_evetr=theta_bioco2_evetr, \
            theta_bioco2_dectr=theta_bioco2_dectr, \
            theta_bioco2_grass=theta_bioco2_grass, th=th, tl=tl, vsmd=vsmd, xsmd=xsmd)
        return fc, fc_biogen, fc_photo, fc_respi
    
    @staticmethod
    def suews_cal_qn(storageheatmethod, netradiationmethod, snowuse, tstep, nlayer, \
        snowpack_prev, tau_a, tau_f, snowalbmax, snowalbmin, diagnose, ldown_obs, \
        fcld_obs, dectime, zenith_deg, tsurf_0, kdown, tair_c, avrh, ea_hpa, \
        qn1_obs, snowalb_prev, snowfrac_prev, diagqn, narp_trans_site, \
        narp_emis_snow, icefrac, sfr_surf, sfr_roof, sfr_wall, tsfc_surf, tsfc_roof, \
        tsfc_wall, emis, alb_prev, albdectr_id, albevetr_id, albgrass_id, lai_id, \
        n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
        sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
        air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
        ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
        veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
        emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, alb_next, qn_surf, \
        qn_roof, qn_wall, qn_ind_snow, kup_ind_snow, tsurf_ind_snow, tsurf_ind, \
        dataoutlinespartacus):
        """
        ldown, fcld, qn, qn_snowfree, qn_snow, kclear, kup, lup, tsurf, albedo_snow, \
            snowalb_next = suews_cal_qn(storageheatmethod, netradiationmethod, snowuse, \
            tstep, nlayer, snowpack_prev, tau_a, tau_f, snowalbmax, snowalbmin, \
            diagnose, ldown_obs, fcld_obs, dectime, zenith_deg, tsurf_0, kdown, tair_c, \
            avrh, ea_hpa, qn1_obs, snowalb_prev, snowfrac_prev, diagqn, narp_trans_site, \
            narp_emis_snow, icefrac, sfr_surf, sfr_roof, sfr_wall, tsfc_surf, tsfc_roof, \
            tsfc_wall, emis, alb_prev, albdectr_id, albevetr_id, albgrass_id, lai_id, \
            n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
            emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, alb_next, qn_surf, \
            qn_roof, qn_wall, qn_ind_snow, kup_ind_snow, tsurf_ind_snow, tsurf_ind, \
            dataoutlinespartacus)
        
        
        Defined at suews_ctrl_driver.fpp lines 5149-5368
        
        Parameters
        ----------
        storageheatmethod : int
        netradiationmethod : int
        snowuse : int
        tstep : int
        nlayer : int
        snowpack_prev : float array
        tau_a : float
        tau_f : float
        snowalbmax : float
        snowalbmin : float
        diagnose : int
        ldown_obs : float
        fcld_obs : float
        dectime : float
        zenith_deg : float
        tsurf_0 : float
        kdown : float
        tair_c : float
        avrh : float
        ea_hpa : float
        qn1_obs : float
        snowalb_prev : float
        snowfrac_prev : float array
        diagqn : int
        narp_trans_site : float
        narp_emis_snow : float
        icefrac : float array
        sfr_surf : float array
        sfr_roof : float array
        sfr_wall : float array
        tsfc_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        emis : float array
        alb_prev : float array
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        lai_id : float array
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        alb_next : float array
        qn_surf : float array
        qn_roof : float array
        qn_wall : float array
        qn_ind_snow : float array
        kup_ind_snow : float array
        tsurf_ind_snow : float array
        tsurf_ind : float array
        dataoutlinespartacus : float array
        
        Returns
        -------
        ldown : float
        fcld : float
        qn : float
        qn_snowfree : float
        qn_snow : float
        kclear : float
        kup : float
        lup : float
        tsurf : float
        albedo_snow : float
        snowalb_next : float
        
        """
        ldown, fcld, qn, qn_snowfree, qn_snow, kclear, kup, lup, tsurf, albedo_snow, \
            snowalb_next = \
            _supy_driver.f90wrap_suews_cal_qn(storageheatmethod=storageheatmethod, \
            netradiationmethod=netradiationmethod, snowuse=snowuse, tstep=tstep, \
            nlayer=nlayer, snowpack_prev=snowpack_prev, tau_a=tau_a, tau_f=tau_f, \
            snowalbmax=snowalbmax, snowalbmin=snowalbmin, diagnose=diagnose, \
            ldown_obs=ldown_obs, fcld_obs=fcld_obs, dectime=dectime, \
            zenith_deg=zenith_deg, tsurf_0=tsurf_0, kdown=kdown, tair_c=tair_c, \
            avrh=avrh, ea_hpa=ea_hpa, qn1_obs=qn1_obs, snowalb_prev=snowalb_prev, \
            snowfrac_prev=snowfrac_prev, diagqn=diagqn, narp_trans_site=narp_trans_site, \
            narp_emis_snow=narp_emis_snow, icefrac=icefrac, sfr_surf=sfr_surf, \
            sfr_roof=sfr_roof, sfr_wall=sfr_wall, tsfc_surf=tsfc_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, emis=emis, alb_prev=alb_prev, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            lai_id=lai_id, n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, \
            building_scale=building_scale, veg_scale=veg_scale, alb_roof=alb_roof, \
            emis_roof=emis_roof, alb_wall=alb_wall, emis_wall=emis_wall, \
            roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, alb_next=alb_next, qn_surf=qn_surf, \
            qn_roof=qn_roof, qn_wall=qn_wall, qn_ind_snow=qn_ind_snow, \
            kup_ind_snow=kup_ind_snow, tsurf_ind_snow=tsurf_ind_snow, \
            tsurf_ind=tsurf_ind, dataoutlinespartacus=dataoutlinespartacus)
        return ldown, fcld, qn, qn_snowfree, qn_snow, kclear, kup, lup, tsurf, \
            albedo_snow, snowalb_next
    
    @staticmethod
    def suews_cal_qn_dts(storageheatmethod, netradiationmethod, snowuse, tstep, \
        nlayer, snowpack_prev, tau_a, tau_f, snowalbmax, snowalbmin, diagnose, \
        ldown_obs, fcld_obs, dectime, zenith_deg, tsurf_0, kdown, tair_c, avrh, \
        ea_hpa, qn1_obs, snowalb_prev, snowfrac_prev, diagqn, narp_trans_site, \
        narp_emis_snow, icefrac, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, \
        sfr_grass, sfr_bsoil, sfr_water, sfr_roof, sfr_wall, tsfc_surf, tsfc_roof, \
        tsfc_wall, emis_paved, emis_bldg, emis_evetr, emis_dectr, emis_grass, \
        emis_bsoil, emis_water, alb_prev, albdectr_id, albevetr_id, albgrass_id, \
        lai_id, n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
        sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
        air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
        ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
        veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
        emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, alb_next, qn_surf, \
        qn_roof, qn_wall, qn_ind_snow, kup_ind_snow, tsurf_ind_snow, tsurf_ind, \
        dataoutlinespartacus):
        """
        ldown, fcld, qn, qn_snowfree, qn_snow, kclear, kup, lup, tsurf, albedo_snow, \
            snowalb_next = suews_cal_qn_dts(storageheatmethod, netradiationmethod, \
            snowuse, tstep, nlayer, snowpack_prev, tau_a, tau_f, snowalbmax, snowalbmin, \
            diagnose, ldown_obs, fcld_obs, dectime, zenith_deg, tsurf_0, kdown, tair_c, \
            avrh, ea_hpa, qn1_obs, snowalb_prev, snowfrac_prev, diagqn, narp_trans_site, \
            narp_emis_snow, icefrac, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, \
            sfr_grass, sfr_bsoil, sfr_water, sfr_roof, sfr_wall, tsfc_surf, tsfc_roof, \
            tsfc_wall, emis_paved, emis_bldg, emis_evetr, emis_dectr, emis_grass, \
            emis_bsoil, emis_water, alb_prev, albdectr_id, albevetr_id, albgrass_id, \
            lai_id, n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
            emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, alb_next, qn_surf, \
            qn_roof, qn_wall, qn_ind_snow, kup_ind_snow, tsurf_ind_snow, tsurf_ind, \
            dataoutlinespartacus)
        
        
        Defined at suews_ctrl_driver.fpp lines 5370-5578
        
        Parameters
        ----------
        storageheatmethod : int
        netradiationmethod : int
        snowuse : int
        tstep : int
        nlayer : int
        snowpack_prev : float array
        tau_a : float
        tau_f : float
        snowalbmax : float
        snowalbmin : float
        diagnose : int
        ldown_obs : float
        fcld_obs : float
        dectime : float
        zenith_deg : float
        tsurf_0 : float
        kdown : float
        tair_c : float
        avrh : float
        ea_hpa : float
        qn1_obs : float
        snowalb_prev : float
        snowfrac_prev : float array
        diagqn : int
        narp_trans_site : float
        narp_emis_snow : float
        icefrac : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        sfr_roof : float array
        sfr_wall : float array
        tsfc_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        emis_paved : float
        emis_bldg : float
        emis_evetr : float
        emis_dectr : float
        emis_grass : float
        emis_bsoil : float
        emis_water : float
        alb_prev : float array
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        lai_id : float array
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        alb_next : float array
        qn_surf : float array
        qn_roof : float array
        qn_wall : float array
        qn_ind_snow : float array
        kup_ind_snow : float array
        tsurf_ind_snow : float array
        tsurf_ind : float array
        dataoutlinespartacus : float array
        
        Returns
        -------
        ldown : float
        fcld : float
        qn : float
        qn_snowfree : float
        qn_snow : float
        kclear : float
        kup : float
        lup : float
        tsurf : float
        albedo_snow : float
        snowalb_next : float
        
        """
        ldown, fcld, qn, qn_snowfree, qn_snow, kclear, kup, lup, tsurf, albedo_snow, \
            snowalb_next = \
            _supy_driver.f90wrap_suews_cal_qn_dts(storageheatmethod=storageheatmethod, \
            netradiationmethod=netradiationmethod, snowuse=snowuse, tstep=tstep, \
            nlayer=nlayer, snowpack_prev=snowpack_prev, tau_a=tau_a, tau_f=tau_f, \
            snowalbmax=snowalbmax, snowalbmin=snowalbmin, diagnose=diagnose, \
            ldown_obs=ldown_obs, fcld_obs=fcld_obs, dectime=dectime, \
            zenith_deg=zenith_deg, tsurf_0=tsurf_0, kdown=kdown, tair_c=tair_c, \
            avrh=avrh, ea_hpa=ea_hpa, qn1_obs=qn1_obs, snowalb_prev=snowalb_prev, \
            snowfrac_prev=snowfrac_prev, diagqn=diagqn, narp_trans_site=narp_trans_site, \
            narp_emis_snow=narp_emis_snow, icefrac=icefrac, sfr_paved=sfr_paved, \
            sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, \
            sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, \
            sfr_roof=sfr_roof, sfr_wall=sfr_wall, tsfc_surf=tsfc_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, emis_paved=emis_paved, \
            emis_bldg=emis_bldg, emis_evetr=emis_evetr, emis_dectr=emis_dectr, \
            emis_grass=emis_grass, emis_bsoil=emis_bsoil, emis_water=emis_water, \
            alb_prev=alb_prev, albdectr_id=albdectr_id, albevetr_id=albevetr_id, \
            albgrass_id=albgrass_id, lai_id=lai_id, \
            n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, \
            building_scale=building_scale, veg_scale=veg_scale, alb_roof=alb_roof, \
            emis_roof=emis_roof, alb_wall=alb_wall, emis_wall=emis_wall, \
            roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, alb_next=alb_next, qn_surf=qn_surf, \
            qn_roof=qn_roof, qn_wall=qn_wall, qn_ind_snow=qn_ind_snow, \
            kup_ind_snow=kup_ind_snow, tsurf_ind_snow=tsurf_ind_snow, \
            tsurf_ind=tsurf_ind, dataoutlinespartacus=dataoutlinespartacus)
        return ldown, fcld, qn, qn_snowfree, qn_snow, kclear, kup, lup, tsurf, \
            albedo_snow, snowalb_next
    
    @staticmethod
    def suews_cal_qs(storageheatmethod, qs_obs, ohmincqf, gridiv, id, tstep, \
        dt_since_start, diagnose, nlayer, qg_surf, qg_roof, qg_wall, tsfc_roof, \
        tin_roof, temp_in_roof, k_roof, cp_roof, dz_roof, sfr_roof, tsfc_wall, \
        tin_wall, temp_in_wall, k_wall, cp_wall, dz_wall, sfr_wall, tsfc_surf, \
        tin_surf, temp_in_surf, k_surf, cp_surf, dz_surf, sfr_surf, ohm_coef, \
        ohm_threshsw, ohm_threshwd, soilstore_id, soilstorecap, state_id, snowuse, \
        snowfrac, diagqs, hdd_id, metforcingdata_grid, ts5mindata_ir, qf, qn, avkdn, \
        avu1, temp_c, zenith_deg, avrh, press_hpa, ldown, bldgh, alb, emis, cpanohm, \
        kkanohm, chanohm, emissionsmethod, tair_av, qn_av_prev, dqndt_prev, \
        qn_s_av_prev, dqnsdt_prev, storedrainprm, dataoutlineestm, deltaqi, \
        temp_out_roof, qs_roof, temp_out_wall, qs_wall, temp_out_surf, qs_surf):
        """
        qn_s, qs, qn_av_next, dqndt_next, qn_s_av_next, dqnsdt_next, a1, a2, a3 = \
            suews_cal_qs(storageheatmethod, qs_obs, ohmincqf, gridiv, id, tstep, \
            dt_since_start, diagnose, nlayer, qg_surf, qg_roof, qg_wall, tsfc_roof, \
            tin_roof, temp_in_roof, k_roof, cp_roof, dz_roof, sfr_roof, tsfc_wall, \
            tin_wall, temp_in_wall, k_wall, cp_wall, dz_wall, sfr_wall, tsfc_surf, \
            tin_surf, temp_in_surf, k_surf, cp_surf, dz_surf, sfr_surf, ohm_coef, \
            ohm_threshsw, ohm_threshwd, soilstore_id, soilstorecap, state_id, snowuse, \
            snowfrac, diagqs, hdd_id, metforcingdata_grid, ts5mindata_ir, qf, qn, avkdn, \
            avu1, temp_c, zenith_deg, avrh, press_hpa, ldown, bldgh, alb, emis, cpanohm, \
            kkanohm, chanohm, emissionsmethod, tair_av, qn_av_prev, dqndt_prev, \
            qn_s_av_prev, dqnsdt_prev, storedrainprm, dataoutlineestm, deltaqi, \
            temp_out_roof, qs_roof, temp_out_wall, qs_wall, temp_out_surf, qs_surf)
        
        
        Defined at suews_ctrl_driver.fpp lines 5602-5834
        
        Parameters
        ----------
        storageheatmethod : int
        qs_obs : float
        ohmincqf : int
        gridiv : int
        id : int
        tstep : int
        dt_since_start : int
        diagnose : int
        nlayer : int
        qg_surf : float array
        qg_roof : float array
        qg_wall : float array
        tsfc_roof : float array
        tin_roof : float array
        temp_in_roof : float array
        k_roof : float array
        cp_roof : float array
        dz_roof : float array
        sfr_roof : float array
        tsfc_wall : float array
        tin_wall : float array
        temp_in_wall : float array
        k_wall : float array
        cp_wall : float array
        dz_wall : float array
        sfr_wall : float array
        tsfc_surf : float array
        tin_surf : float array
        temp_in_surf : float array
        k_surf : float array
        cp_surf : float array
        dz_surf : float array
        sfr_surf : float array
        ohm_coef : float array
        ohm_threshsw : float array
        ohm_threshwd : float array
        soilstore_id : float array
        soilstorecap : float array
        state_id : float array
        snowuse : int
        snowfrac : float array
        diagqs : int
        hdd_id : float array
        metforcingdata_grid : float array
        ts5mindata_ir : float array
        qf : float
        qn : float
        avkdn : float
        avu1 : float
        temp_c : float
        zenith_deg : float
        avrh : float
        press_hpa : float
        ldown : float
        bldgh : float
        alb : float array
        emis : float array
        cpanohm : float array
        kkanohm : float array
        chanohm : float array
        emissionsmethod : int
        tair_av : float
        qn_av_prev : float
        dqndt_prev : float
        qn_s_av_prev : float
        dqnsdt_prev : float
        storedrainprm : float array
        dataoutlineestm : float array
        deltaqi : float array
        temp_out_roof : float array
        qs_roof : float array
        temp_out_wall : float array
        qs_wall : float array
        temp_out_surf : float array
        qs_surf : float array
        
        Returns
        -------
        qn_s : float
        qs : float
        qn_av_next : float
        dqndt_next : float
        qn_s_av_next : float
        dqnsdt_next : float
        a1 : float
        a2 : float
        a3 : float
        
        """
        qn_s, qs, qn_av_next, dqndt_next, qn_s_av_next, dqnsdt_next, a1, a2, a3 = \
            _supy_driver.f90wrap_suews_cal_qs(storageheatmethod=storageheatmethod, \
            qs_obs=qs_obs, ohmincqf=ohmincqf, gridiv=gridiv, id=id, tstep=tstep, \
            dt_since_start=dt_since_start, diagnose=diagnose, nlayer=nlayer, \
            qg_surf=qg_surf, qg_roof=qg_roof, qg_wall=qg_wall, tsfc_roof=tsfc_roof, \
            tin_roof=tin_roof, temp_in_roof=temp_in_roof, k_roof=k_roof, \
            cp_roof=cp_roof, dz_roof=dz_roof, sfr_roof=sfr_roof, tsfc_wall=tsfc_wall, \
            tin_wall=tin_wall, temp_in_wall=temp_in_wall, k_wall=k_wall, \
            cp_wall=cp_wall, dz_wall=dz_wall, sfr_wall=sfr_wall, tsfc_surf=tsfc_surf, \
            tin_surf=tin_surf, temp_in_surf=temp_in_surf, k_surf=k_surf, \
            cp_surf=cp_surf, dz_surf=dz_surf, sfr_surf=sfr_surf, ohm_coef=ohm_coef, \
            ohm_threshsw=ohm_threshsw, ohm_threshwd=ohm_threshwd, \
            soilstore_id=soilstore_id, soilstorecap=soilstorecap, state_id=state_id, \
            snowuse=snowuse, snowfrac=snowfrac, diagqs=diagqs, hdd_id=hdd_id, \
            metforcingdata_grid=metforcingdata_grid, ts5mindata_ir=ts5mindata_ir, qf=qf, \
            qn=qn, avkdn=avkdn, avu1=avu1, temp_c=temp_c, zenith_deg=zenith_deg, \
            avrh=avrh, press_hpa=press_hpa, ldown=ldown, bldgh=bldgh, alb=alb, \
            emis=emis, cpanohm=cpanohm, kkanohm=kkanohm, chanohm=chanohm, \
            emissionsmethod=emissionsmethod, tair_av=tair_av, qn_av_prev=qn_av_prev, \
            dqndt_prev=dqndt_prev, qn_s_av_prev=qn_s_av_prev, dqnsdt_prev=dqnsdt_prev, \
            storedrainprm=storedrainprm, dataoutlineestm=dataoutlineestm, \
            deltaqi=deltaqi, temp_out_roof=temp_out_roof, qs_roof=qs_roof, \
            temp_out_wall=temp_out_wall, qs_wall=qs_wall, temp_out_surf=temp_out_surf, \
            qs_surf=qs_surf)
        return qn_s, qs, qn_av_next, dqndt_next, qn_s_av_next, dqnsdt_next, a1, a2, a3
    
    @staticmethod
    def suews_cal_qs_dts(storageheatmethod, qs_obs, ohmincqf, gridiv, id, tstep, \
        dt_since_start, diagnose, nlayer, qg_surf, qg_roof, qg_wall, tsfc_roof, \
        tin_roof, temp_in_roof, k_roof, cp_roof, dz_roof, sfr_roof, tsfc_wall, \
        tin_wall, temp_in_wall, k_wall, cp_wall, dz_wall, sfr_wall, tsfc_surf, \
        tin_surf, temp_in_surf, k_surf, cp_surf, dz_surf, sfr_paved, sfr_bldg, \
        sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, ohm_coef_paved, \
        ohm_coef_bldg, ohm_coef_evetr, ohm_coef_dectr, ohm_coef_grass, \
        ohm_coef_bsoil, ohm_coef_water, ohm_threshsw_paved, ohm_threshsw_bldg, \
        ohm_threshsw_evetr, ohm_threshsw_dectr, ohm_threshsw_grass, \
        ohm_threshsw_bsoil, ohm_threshsw_water, ohm_threshwd_paved, \
        ohm_threshwd_bldg, ohm_threshwd_evetr, ohm_threshwd_dectr, \
        ohm_threshwd_grass, ohm_threshwd_bsoil, ohm_threshwd_water, soilstore_id, \
        soilstorecap_paved, soilstorecap_bldg, soilstorecap_evetr, \
        soilstorecap_dectr, soilstorecap_grass, soilstorecap_bsoil, \
        soilstorecap_water, state_id, snowuse, snowfrac, diagqs, hdd_id, \
        metforcingdata_grid, ts5mindata_ir, qf, qn, avkdn, avu1, temp_c, zenith_deg, \
        avrh, press_hpa, ldown, bldgh, alb, emis_paved, emis_bldg, emis_evetr, \
        emis_dectr, emis_grass, emis_bsoil, emis_water, cpanohm_paved, cpanohm_bldg, \
        cpanohm_evetr, cpanohm_dectr, cpanohm_grass, cpanohm_bsoil, cpanohm_water, \
        kkanohm_paved, kkanohm_bldg, kkanohm_evetr, kkanohm_dectr, kkanohm_grass, \
        kkanohm_bsoil, kkanohm_water, chanohm_paved, chanohm_bldg, chanohm_evetr, \
        chanohm_dectr, chanohm_grass, chanohm_bsoil, chanohm_water, emissionsmethod, \
        tair_av, qn_av_prev, dqndt_prev, qn_s_av_prev, dqnsdt_prev, storedrainprm, \
        dataoutlineestm, deltaqi, temp_out_roof, qs_roof, temp_out_wall, qs_wall, \
        temp_out_surf, qs_surf):
        """
        qn_s, qs, qn_av_next, dqndt_next, qn_s_av_next, dqnsdt_next, a1, a2, a3 = \
            suews_cal_qs_dts(storageheatmethod, qs_obs, ohmincqf, gridiv, id, tstep, \
            dt_since_start, diagnose, nlayer, qg_surf, qg_roof, qg_wall, tsfc_roof, \
            tin_roof, temp_in_roof, k_roof, cp_roof, dz_roof, sfr_roof, tsfc_wall, \
            tin_wall, temp_in_wall, k_wall, cp_wall, dz_wall, sfr_wall, tsfc_surf, \
            tin_surf, temp_in_surf, k_surf, cp_surf, dz_surf, sfr_paved, sfr_bldg, \
            sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, ohm_coef_paved, \
            ohm_coef_bldg, ohm_coef_evetr, ohm_coef_dectr, ohm_coef_grass, \
            ohm_coef_bsoil, ohm_coef_water, ohm_threshsw_paved, ohm_threshsw_bldg, \
            ohm_threshsw_evetr, ohm_threshsw_dectr, ohm_threshsw_grass, \
            ohm_threshsw_bsoil, ohm_threshsw_water, ohm_threshwd_paved, \
            ohm_threshwd_bldg, ohm_threshwd_evetr, ohm_threshwd_dectr, \
            ohm_threshwd_grass, ohm_threshwd_bsoil, ohm_threshwd_water, soilstore_id, \
            soilstorecap_paved, soilstorecap_bldg, soilstorecap_evetr, \
            soilstorecap_dectr, soilstorecap_grass, soilstorecap_bsoil, \
            soilstorecap_water, state_id, snowuse, snowfrac, diagqs, hdd_id, \
            metforcingdata_grid, ts5mindata_ir, qf, qn, avkdn, avu1, temp_c, zenith_deg, \
            avrh, press_hpa, ldown, bldgh, alb, emis_paved, emis_bldg, emis_evetr, \
            emis_dectr, emis_grass, emis_bsoil, emis_water, cpanohm_paved, cpanohm_bldg, \
            cpanohm_evetr, cpanohm_dectr, cpanohm_grass, cpanohm_bsoil, cpanohm_water, \
            kkanohm_paved, kkanohm_bldg, kkanohm_evetr, kkanohm_dectr, kkanohm_grass, \
            kkanohm_bsoil, kkanohm_water, chanohm_paved, chanohm_bldg, chanohm_evetr, \
            chanohm_dectr, chanohm_grass, chanohm_bsoil, chanohm_water, emissionsmethod, \
            tair_av, qn_av_prev, dqndt_prev, qn_s_av_prev, dqnsdt_prev, storedrainprm, \
            dataoutlineestm, deltaqi, temp_out_roof, qs_roof, temp_out_wall, qs_wall, \
            temp_out_surf, qs_surf)
        
        
        Defined at suews_ctrl_driver.fpp lines 5836-6242
        
        Parameters
        ----------
        storageheatmethod : int
        qs_obs : float
        ohmincqf : int
        gridiv : int
        id : int
        tstep : int
        dt_since_start : int
        diagnose : int
        nlayer : int
        qg_surf : float array
        qg_roof : float array
        qg_wall : float array
        tsfc_roof : float array
        tin_roof : float array
        temp_in_roof : float array
        k_roof : float array
        cp_roof : float array
        dz_roof : float array
        sfr_roof : float array
        tsfc_wall : float array
        tin_wall : float array
        temp_in_wall : float array
        k_wall : float array
        cp_wall : float array
        dz_wall : float array
        sfr_wall : float array
        tsfc_surf : float array
        tin_surf : float array
        temp_in_surf : float array
        k_surf : float array
        cp_surf : float array
        dz_surf : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        ohm_coef_paved : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_coef_bldg : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_coef_evetr : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_coef_dectr : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_coef_grass : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_coef_bsoil : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_coef_water : Ohm_Coef_Lc_X3_Array
        	super-type
        
        ohm_threshsw_paved : float
        ohm_threshsw_bldg : float
        ohm_threshsw_evetr : float
        ohm_threshsw_dectr : float
        ohm_threshsw_grass : float
        ohm_threshsw_bsoil : float
        ohm_threshsw_water : float
        ohm_threshwd_paved : float
        ohm_threshwd_bldg : float
        ohm_threshwd_evetr : float
        ohm_threshwd_dectr : float
        ohm_threshwd_grass : float
        ohm_threshwd_bsoil : float
        ohm_threshwd_water : float
        soilstore_id : float array
        soilstorecap_paved : float
        soilstorecap_bldg : float
        soilstorecap_evetr : float
        soilstorecap_dectr : float
        soilstorecap_grass : float
        soilstorecap_bsoil : float
        soilstorecap_water : float
        state_id : float array
        snowuse : int
        snowfrac : float array
        diagqs : int
        hdd_id : float array
        metforcingdata_grid : float array
        ts5mindata_ir : float array
        qf : float
        qn : float
        avkdn : float
        avu1 : float
        temp_c : float
        zenith_deg : float
        avrh : float
        press_hpa : float
        ldown : float
        bldgh : float
        alb : float array
        emis_paved : float
        emis_bldg : float
        emis_evetr : float
        emis_dectr : float
        emis_grass : float
        emis_bsoil : float
        emis_water : float
        cpanohm_paved : float
        cpanohm_bldg : float
        cpanohm_evetr : float
        cpanohm_dectr : float
        cpanohm_grass : float
        cpanohm_bsoil : float
        cpanohm_water : float
        kkanohm_paved : float
        kkanohm_bldg : float
        kkanohm_evetr : float
        kkanohm_dectr : float
        kkanohm_grass : float
        kkanohm_bsoil : float
        kkanohm_water : float
        chanohm_paved : float
        chanohm_bldg : float
        chanohm_evetr : float
        chanohm_dectr : float
        chanohm_grass : float
        chanohm_bsoil : float
        chanohm_water : float
        emissionsmethod : int
        tair_av : float
        qn_av_prev : float
        dqndt_prev : float
        qn_s_av_prev : float
        dqnsdt_prev : float
        storedrainprm : float array
        dataoutlineestm : float array
        deltaqi : float array
        temp_out_roof : float array
        qs_roof : float array
        temp_out_wall : float array
        qs_wall : float array
        temp_out_surf : float array
        qs_surf : float array
        
        Returns
        -------
        qn_s : float
        qs : float
        qn_av_next : float
        dqndt_next : float
        qn_s_av_next : float
        dqnsdt_next : float
        a1 : float
        a2 : float
        a3 : float
        
        """
        qn_s, qs, qn_av_next, dqndt_next, qn_s_av_next, dqnsdt_next, a1, a2, a3 = \
            _supy_driver.f90wrap_suews_cal_qs_dts(storageheatmethod=storageheatmethod, \
            qs_obs=qs_obs, ohmincqf=ohmincqf, gridiv=gridiv, id=id, tstep=tstep, \
            dt_since_start=dt_since_start, diagnose=diagnose, nlayer=nlayer, \
            qg_surf=qg_surf, qg_roof=qg_roof, qg_wall=qg_wall, tsfc_roof=tsfc_roof, \
            tin_roof=tin_roof, temp_in_roof=temp_in_roof, k_roof=k_roof, \
            cp_roof=cp_roof, dz_roof=dz_roof, sfr_roof=sfr_roof, tsfc_wall=tsfc_wall, \
            tin_wall=tin_wall, temp_in_wall=temp_in_wall, k_wall=k_wall, \
            cp_wall=cp_wall, dz_wall=dz_wall, sfr_wall=sfr_wall, tsfc_surf=tsfc_surf, \
            tin_surf=tin_surf, temp_in_surf=temp_in_surf, k_surf=k_surf, \
            cp_surf=cp_surf, dz_surf=dz_surf, sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, \
            sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, \
            sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, \
            ohm_coef_paved=ohm_coef_paved._handle, ohm_coef_bldg=ohm_coef_bldg._handle, \
            ohm_coef_evetr=ohm_coef_evetr._handle, \
            ohm_coef_dectr=ohm_coef_dectr._handle, \
            ohm_coef_grass=ohm_coef_grass._handle, \
            ohm_coef_bsoil=ohm_coef_bsoil._handle, \
            ohm_coef_water=ohm_coef_water._handle, \
            ohm_threshsw_paved=ohm_threshsw_paved, ohm_threshsw_bldg=ohm_threshsw_bldg, \
            ohm_threshsw_evetr=ohm_threshsw_evetr, \
            ohm_threshsw_dectr=ohm_threshsw_dectr, \
            ohm_threshsw_grass=ohm_threshsw_grass, \
            ohm_threshsw_bsoil=ohm_threshsw_bsoil, \
            ohm_threshsw_water=ohm_threshsw_water, \
            ohm_threshwd_paved=ohm_threshwd_paved, ohm_threshwd_bldg=ohm_threshwd_bldg, \
            ohm_threshwd_evetr=ohm_threshwd_evetr, \
            ohm_threshwd_dectr=ohm_threshwd_dectr, \
            ohm_threshwd_grass=ohm_threshwd_grass, \
            ohm_threshwd_bsoil=ohm_threshwd_bsoil, \
            ohm_threshwd_water=ohm_threshwd_water, soilstore_id=soilstore_id, \
            soilstorecap_paved=soilstorecap_paved, soilstorecap_bldg=soilstorecap_bldg, \
            soilstorecap_evetr=soilstorecap_evetr, \
            soilstorecap_dectr=soilstorecap_dectr, \
            soilstorecap_grass=soilstorecap_grass, \
            soilstorecap_bsoil=soilstorecap_bsoil, \
            soilstorecap_water=soilstorecap_water, state_id=state_id, snowuse=snowuse, \
            snowfrac=snowfrac, diagqs=diagqs, hdd_id=hdd_id, \
            metforcingdata_grid=metforcingdata_grid, ts5mindata_ir=ts5mindata_ir, qf=qf, \
            qn=qn, avkdn=avkdn, avu1=avu1, temp_c=temp_c, zenith_deg=zenith_deg, \
            avrh=avrh, press_hpa=press_hpa, ldown=ldown, bldgh=bldgh, alb=alb, \
            emis_paved=emis_paved, emis_bldg=emis_bldg, emis_evetr=emis_evetr, \
            emis_dectr=emis_dectr, emis_grass=emis_grass, emis_bsoil=emis_bsoil, \
            emis_water=emis_water, cpanohm_paved=cpanohm_paved, \
            cpanohm_bldg=cpanohm_bldg, cpanohm_evetr=cpanohm_evetr, \
            cpanohm_dectr=cpanohm_dectr, cpanohm_grass=cpanohm_grass, \
            cpanohm_bsoil=cpanohm_bsoil, cpanohm_water=cpanohm_water, \
            kkanohm_paved=kkanohm_paved, kkanohm_bldg=kkanohm_bldg, \
            kkanohm_evetr=kkanohm_evetr, kkanohm_dectr=kkanohm_dectr, \
            kkanohm_grass=kkanohm_grass, kkanohm_bsoil=kkanohm_bsoil, \
            kkanohm_water=kkanohm_water, chanohm_paved=chanohm_paved, \
            chanohm_bldg=chanohm_bldg, chanohm_evetr=chanohm_evetr, \
            chanohm_dectr=chanohm_dectr, chanohm_grass=chanohm_grass, \
            chanohm_bsoil=chanohm_bsoil, chanohm_water=chanohm_water, \
            emissionsmethod=emissionsmethod, tair_av=tair_av, qn_av_prev=qn_av_prev, \
            dqndt_prev=dqndt_prev, qn_s_av_prev=qn_s_av_prev, dqnsdt_prev=dqnsdt_prev, \
            storedrainprm=storedrainprm, dataoutlineestm=dataoutlineestm, \
            deltaqi=deltaqi, temp_out_roof=temp_out_roof, qs_roof=qs_roof, \
            temp_out_wall=temp_out_wall, qs_wall=qs_wall, temp_out_surf=temp_out_surf, \
            qs_surf=qs_surf)
        return qn_s, qs, qn_av_next, dqndt_next, qn_s_av_next, dqnsdt_next, a1, a2, a3
    
    @staticmethod
    def suews_cal_water(diagnose, snowuse, nonwaterfraction, addpipes, \
        addimpervious, addveg, addwaterbody, state_id, sfr_surf, storedrainprm, \
        waterdist, nsh_real, drain, frac_water2runoff, addwater):
        """
        drain_per_tstep, additionalwater, runoffpipes, runoff_per_interval = \
            suews_cal_water(diagnose, snowuse, nonwaterfraction, addpipes, \
            addimpervious, addveg, addwaterbody, state_id, sfr_surf, storedrainprm, \
            waterdist, nsh_real, drain, frac_water2runoff, addwater)
        
        
        Defined at suews_ctrl_driver.fpp lines 6253-6350
        
        Parameters
        ----------
        diagnose : int
        snowuse : int
        nonwaterfraction : float
        addpipes : float
        addimpervious : float
        addveg : float
        addwaterbody : float
        state_id : float array
        sfr_surf : float array
        storedrainprm : float array
        waterdist : float array
        nsh_real : float
        drain : float array
        frac_water2runoff : float array
        addwater : float array
        
        Returns
        -------
        drain_per_tstep : float
        additionalwater : float
        runoffpipes : float
        runoff_per_interval : float
        
        ============= Grid-to-grid runoff =============
         Calculate additional water coming from other grids
         i.e. the variables addImpervious, addVeg, addWaterBody, addPipes
        call RunoffFromGrid(GridFromFrac)
        Need to code between-grid water transfer
         Sum water coming from other grids(these are expressed as depths over the whole \
             surface)
        """
        drain_per_tstep, additionalwater, runoffpipes, runoff_per_interval = \
            _supy_driver.f90wrap_suews_cal_water(diagnose=diagnose, snowuse=snowuse, \
            nonwaterfraction=nonwaterfraction, addpipes=addpipes, \
            addimpervious=addimpervious, addveg=addveg, addwaterbody=addwaterbody, \
            state_id=state_id, sfr_surf=sfr_surf, storedrainprm=storedrainprm, \
            waterdist=waterdist, nsh_real=nsh_real, drain=drain, \
            frac_water2runoff=frac_water2runoff, addwater=addwater)
        return drain_per_tstep, additionalwater, runoffpipes, runoff_per_interval
    
    @staticmethod
    def suews_cal_water_dts(diagnose, snowuse, nonwaterfraction, addpipes, \
        addimpervious, addveg, addwaterbody, state_id, sfr_paved, sfr_bldg, \
        sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, storedrainprm, \
        waterdist_paved_topaved, waterdist_paved_tobldg, waterdist_paved_toevetr, \
        waterdist_paved_todectr, waterdist_paved_tograss, waterdist_paved_tobsoil, \
        waterdist_paved_towater, waterdist_paved_tosoilstore, \
        waterdist_bldg_topaved, waterdist_bldg_tobldg, waterdist_bldg_toevetr, \
        waterdist_bldg_todectr, waterdist_bldg_tograss, waterdist_bldg_tobsoil, \
        waterdist_bldg_towater, waterdist_bldg_tosoilstore, waterdist_evetr_topaved, \
        waterdist_evetr_tobldg, waterdist_evetr_toevetr, waterdist_evetr_todectr, \
        waterdist_evetr_tograss, waterdist_evetr_tobsoil, waterdist_evetr_towater, \
        waterdist_evetr_tosoilstore, waterdist_dectr_topaved, \
        waterdist_dectr_tobldg, waterdist_dectr_toevetr, waterdist_dectr_todectr, \
        waterdist_dectr_tograss, waterdist_dectr_tobsoil, waterdist_dectr_towater, \
        waterdist_dectr_tosoilstore, waterdist_grass_topaved, \
        waterdist_grass_tobldg, waterdist_grass_toevetr, waterdist_grass_todectr, \
        waterdist_grass_tograss, waterdist_grass_tobsoil, waterdist_grass_towater, \
        waterdist_grass_tosoilstore, waterdist_bsoil_topaved, \
        waterdist_bsoil_tobldg, waterdist_bsoil_toevetr, waterdist_bsoil_todectr, \
        waterdist_bsoil_tograss, waterdist_bsoil_tobsoil, waterdist_bsoil_towater, \
        waterdist_bsoil_tosoilstore, nsh_real, drain, frac_water2runoff, addwater):
        """
        drain_per_tstep, additionalwater, runoffpipes, runoff_per_interval = \
            suews_cal_water_dts(diagnose, snowuse, nonwaterfraction, addpipes, \
            addimpervious, addveg, addwaterbody, state_id, sfr_paved, sfr_bldg, \
            sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, storedrainprm, \
            waterdist_paved_topaved, waterdist_paved_tobldg, waterdist_paved_toevetr, \
            waterdist_paved_todectr, waterdist_paved_tograss, waterdist_paved_tobsoil, \
            waterdist_paved_towater, waterdist_paved_tosoilstore, \
            waterdist_bldg_topaved, waterdist_bldg_tobldg, waterdist_bldg_toevetr, \
            waterdist_bldg_todectr, waterdist_bldg_tograss, waterdist_bldg_tobsoil, \
            waterdist_bldg_towater, waterdist_bldg_tosoilstore, waterdist_evetr_topaved, \
            waterdist_evetr_tobldg, waterdist_evetr_toevetr, waterdist_evetr_todectr, \
            waterdist_evetr_tograss, waterdist_evetr_tobsoil, waterdist_evetr_towater, \
            waterdist_evetr_tosoilstore, waterdist_dectr_topaved, \
            waterdist_dectr_tobldg, waterdist_dectr_toevetr, waterdist_dectr_todectr, \
            waterdist_dectr_tograss, waterdist_dectr_tobsoil, waterdist_dectr_towater, \
            waterdist_dectr_tosoilstore, waterdist_grass_topaved, \
            waterdist_grass_tobldg, waterdist_grass_toevetr, waterdist_grass_todectr, \
            waterdist_grass_tograss, waterdist_grass_tobsoil, waterdist_grass_towater, \
            waterdist_grass_tosoilstore, waterdist_bsoil_topaved, \
            waterdist_bsoil_tobldg, waterdist_bsoil_toevetr, waterdist_bsoil_todectr, \
            waterdist_bsoil_tograss, waterdist_bsoil_tobsoil, waterdist_bsoil_towater, \
            waterdist_bsoil_tosoilstore, nsh_real, drain, frac_water2runoff, addwater)
        
        
        Defined at suews_ctrl_driver.fpp lines 6352-6526
        
        Parameters
        ----------
        diagnose : int
        snowuse : int
        nonwaterfraction : float
        addpipes : float
        addimpervious : float
        addveg : float
        addwaterbody : float
        state_id : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        storedrainprm : float array
        waterdist_paved_topaved : float
        waterdist_paved_tobldg : float
        waterdist_paved_toevetr : float
        waterdist_paved_todectr : float
        waterdist_paved_tograss : float
        waterdist_paved_tobsoil : float
        waterdist_paved_towater : float
        waterdist_paved_tosoilstore : float
        waterdist_bldg_topaved : float
        waterdist_bldg_tobldg : float
        waterdist_bldg_toevetr : float
        waterdist_bldg_todectr : float
        waterdist_bldg_tograss : float
        waterdist_bldg_tobsoil : float
        waterdist_bldg_towater : float
        waterdist_bldg_tosoilstore : float
        waterdist_evetr_topaved : float
        waterdist_evetr_tobldg : float
        waterdist_evetr_toevetr : float
        waterdist_evetr_todectr : float
        waterdist_evetr_tograss : float
        waterdist_evetr_tobsoil : float
        waterdist_evetr_towater : float
        waterdist_evetr_tosoilstore : float
        waterdist_dectr_topaved : float
        waterdist_dectr_tobldg : float
        waterdist_dectr_toevetr : float
        waterdist_dectr_todectr : float
        waterdist_dectr_tograss : float
        waterdist_dectr_tobsoil : float
        waterdist_dectr_towater : float
        waterdist_dectr_tosoilstore : float
        waterdist_grass_topaved : float
        waterdist_grass_tobldg : float
        waterdist_grass_toevetr : float
        waterdist_grass_todectr : float
        waterdist_grass_tograss : float
        waterdist_grass_tobsoil : float
        waterdist_grass_towater : float
        waterdist_grass_tosoilstore : float
        waterdist_bsoil_topaved : float
        waterdist_bsoil_tobldg : float
        waterdist_bsoil_toevetr : float
        waterdist_bsoil_todectr : float
        waterdist_bsoil_tograss : float
        waterdist_bsoil_tobsoil : float
        waterdist_bsoil_towater : float
        waterdist_bsoil_tosoilstore : float
        nsh_real : float
        drain : float array
        frac_water2runoff : float array
        addwater : float array
        
        Returns
        -------
        drain_per_tstep : float
        additionalwater : float
        runoffpipes : float
        runoff_per_interval : float
        
        ============= Grid-to-grid runoff =============
         Calculate additional water coming from other grids
         i.e. the variables addImpervious, addVeg, addWaterBody, addPipes
        call RunoffFromGrid(GridFromFrac)
        Need to code between-grid water transfer
         Sum water coming from other grids(these are expressed as depths over the whole \
             surface)
         Initialise runoff in pipes
        """
        drain_per_tstep, additionalwater, runoffpipes, runoff_per_interval = \
            _supy_driver.f90wrap_suews_cal_water_dts(diagnose=diagnose, snowuse=snowuse, \
            nonwaterfraction=nonwaterfraction, addpipes=addpipes, \
            addimpervious=addimpervious, addveg=addveg, addwaterbody=addwaterbody, \
            state_id=state_id, sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, \
            sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, \
            sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, storedrainprm=storedrainprm, \
            waterdist_paved_topaved=waterdist_paved_topaved, \
            waterdist_paved_tobldg=waterdist_paved_tobldg, \
            waterdist_paved_toevetr=waterdist_paved_toevetr, \
            waterdist_paved_todectr=waterdist_paved_todectr, \
            waterdist_paved_tograss=waterdist_paved_tograss, \
            waterdist_paved_tobsoil=waterdist_paved_tobsoil, \
            waterdist_paved_towater=waterdist_paved_towater, \
            waterdist_paved_tosoilstore=waterdist_paved_tosoilstore, \
            waterdist_bldg_topaved=waterdist_bldg_topaved, \
            waterdist_bldg_tobldg=waterdist_bldg_tobldg, \
            waterdist_bldg_toevetr=waterdist_bldg_toevetr, \
            waterdist_bldg_todectr=waterdist_bldg_todectr, \
            waterdist_bldg_tograss=waterdist_bldg_tograss, \
            waterdist_bldg_tobsoil=waterdist_bldg_tobsoil, \
            waterdist_bldg_towater=waterdist_bldg_towater, \
            waterdist_bldg_tosoilstore=waterdist_bldg_tosoilstore, \
            waterdist_evetr_topaved=waterdist_evetr_topaved, \
            waterdist_evetr_tobldg=waterdist_evetr_tobldg, \
            waterdist_evetr_toevetr=waterdist_evetr_toevetr, \
            waterdist_evetr_todectr=waterdist_evetr_todectr, \
            waterdist_evetr_tograss=waterdist_evetr_tograss, \
            waterdist_evetr_tobsoil=waterdist_evetr_tobsoil, \
            waterdist_evetr_towater=waterdist_evetr_towater, \
            waterdist_evetr_tosoilstore=waterdist_evetr_tosoilstore, \
            waterdist_dectr_topaved=waterdist_dectr_topaved, \
            waterdist_dectr_tobldg=waterdist_dectr_tobldg, \
            waterdist_dectr_toevetr=waterdist_dectr_toevetr, \
            waterdist_dectr_todectr=waterdist_dectr_todectr, \
            waterdist_dectr_tograss=waterdist_dectr_tograss, \
            waterdist_dectr_tobsoil=waterdist_dectr_tobsoil, \
            waterdist_dectr_towater=waterdist_dectr_towater, \
            waterdist_dectr_tosoilstore=waterdist_dectr_tosoilstore, \
            waterdist_grass_topaved=waterdist_grass_topaved, \
            waterdist_grass_tobldg=waterdist_grass_tobldg, \
            waterdist_grass_toevetr=waterdist_grass_toevetr, \
            waterdist_grass_todectr=waterdist_grass_todectr, \
            waterdist_grass_tograss=waterdist_grass_tograss, \
            waterdist_grass_tobsoil=waterdist_grass_tobsoil, \
            waterdist_grass_towater=waterdist_grass_towater, \
            waterdist_grass_tosoilstore=waterdist_grass_tosoilstore, \
            waterdist_bsoil_topaved=waterdist_bsoil_topaved, \
            waterdist_bsoil_tobldg=waterdist_bsoil_tobldg, \
            waterdist_bsoil_toevetr=waterdist_bsoil_toevetr, \
            waterdist_bsoil_todectr=waterdist_bsoil_todectr, \
            waterdist_bsoil_tograss=waterdist_bsoil_tograss, \
            waterdist_bsoil_tobsoil=waterdist_bsoil_tobsoil, \
            waterdist_bsoil_towater=waterdist_bsoil_towater, \
            waterdist_bsoil_tosoilstore=waterdist_bsoil_tosoilstore, nsh_real=nsh_real, \
            drain=drain, frac_water2runoff=frac_water2runoff, addwater=addwater)
        return drain_per_tstep, additionalwater, runoffpipes, runoff_per_interval
    
    @staticmethod
    def suews_init_qh(avdens, avcp, h_mod, qn1, dectime):
        """
        h_init = suews_init_qh(avdens, avcp, h_mod, qn1, dectime)
        
        
        Defined at suews_ctrl_driver.fpp lines 6532-6553
        
        Parameters
        ----------
        avdens : float
        avcp : float
        h_mod : float
        qn1 : float
        dectime : float
        
        Returns
        -------
        h_init : float
        
        """
        h_init = _supy_driver.f90wrap_suews_init_qh(avdens=avdens, avcp=avcp, \
            h_mod=h_mod, qn1=qn1, dectime=dectime)
        return h_init
    
    @staticmethod
    def suews_cal_snow(diagnose, nlayer, tstep, imin, it, evapmethod, dayofweek_id, \
        crwmin, crwmax, dectime, avdens, avcp, lv_j_kg, lvs_j_kg, avrh, press_hpa, \
        temp_c, rasnow, psyc_hpa, sice_hpa, tau_r, radmeltfact, tempmeltfact, \
        snowalbmax, preciplimit, preciplimitalb, qn_ind_snow, kup_ind_snow, deltaqi, \
        tsurf_ind_snow, snowalb_in, pervfraction, vegfraction, addimpervious, \
        qn_snowfree, qf, qs, vpd_hpa, s_hpa, rs, ra, rb, snowdensmax, snowdensmin, \
        precip, pipecapacity, runofftowater, addveg, snowlimpaved, snowlimbldg, \
        flowchange, drain, wetthresh_surf, soilstorecap, tsurf_ind, sfr_surf, \
        addwater, addwaterrunoff, storedrainprm, snowpacklimit, snowprof_24hr, \
        snowpack_in, snowfrac_in, snowwater_in, icefrac_in, snowdens_in, \
        snowfallcum_in, state_id_in, soilstore_id_in, qn_surf, qs_surf, snowremoval, \
        snowpack_out, snowfrac_out, snowwater_out, icefrac_out, snowdens_out, \
        state_id_out, soilstore_id_out, qe_surf, qe_roof, qe_wall, rss_surf, \
        dataoutlinesnow):
        """
        snowfallcum_out, state_per_tstep, nwstate_per_tstep, qe, snowalb_out, swe, \
            chsnow_per_tstep, ev_per_tstep, runoff_per_tstep, surf_chang_per_tstep, \
            runoffpipes, mwstore, runoffwaterbody, runoffagveg, runoffagimpervious = \
            suews_cal_snow(diagnose, nlayer, tstep, imin, it, evapmethod, dayofweek_id, \
            crwmin, crwmax, dectime, avdens, avcp, lv_j_kg, lvs_j_kg, avrh, press_hpa, \
            temp_c, rasnow, psyc_hpa, sice_hpa, tau_r, radmeltfact, tempmeltfact, \
            snowalbmax, preciplimit, preciplimitalb, qn_ind_snow, kup_ind_snow, deltaqi, \
            tsurf_ind_snow, snowalb_in, pervfraction, vegfraction, addimpervious, \
            qn_snowfree, qf, qs, vpd_hpa, s_hpa, rs, ra, rb, snowdensmax, snowdensmin, \
            precip, pipecapacity, runofftowater, addveg, snowlimpaved, snowlimbldg, \
            flowchange, drain, wetthresh_surf, soilstorecap, tsurf_ind, sfr_surf, \
            addwater, addwaterrunoff, storedrainprm, snowpacklimit, snowprof_24hr, \
            snowpack_in, snowfrac_in, snowwater_in, icefrac_in, snowdens_in, \
            snowfallcum_in, state_id_in, soilstore_id_in, qn_surf, qs_surf, snowremoval, \
            snowpack_out, snowfrac_out, snowwater_out, icefrac_out, snowdens_out, \
            state_id_out, soilstore_id_out, qe_surf, qe_roof, qe_wall, rss_surf, \
            dataoutlinesnow)
        
        
        Defined at suews_ctrl_driver.fpp lines 6582-6915
        
        Parameters
        ----------
        diagnose : int
        nlayer : int
        tstep : int
        imin : int
        it : int
        evapmethod : int
        dayofweek_id : int array
        crwmin : float
        crwmax : float
        dectime : float
        avdens : float
        avcp : float
        lv_j_kg : float
        lvs_j_kg : float
        avrh : float
        press_hpa : float
        temp_c : float
        rasnow : float
        psyc_hpa : float
        sice_hpa : float
        tau_r : float
        radmeltfact : float
        tempmeltfact : float
        snowalbmax : float
        preciplimit : float
        preciplimitalb : float
        qn_ind_snow : float array
        kup_ind_snow : float array
        deltaqi : float array
        tsurf_ind_snow : float array
        snowalb_in : float
        pervfraction : float
        vegfraction : float
        addimpervious : float
        qn_snowfree : float
        qf : float
        qs : float
        vpd_hpa : float
        s_hpa : float
        rs : float
        ra : float
        rb : float
        snowdensmax : float
        snowdensmin : float
        precip : float
        pipecapacity : float
        runofftowater : float
        addveg : float
        snowlimpaved : float
        snowlimbldg : float
        flowchange : float
        drain : float array
        wetthresh_surf : float array
        soilstorecap : float array
        tsurf_ind : float array
        sfr_surf : float array
        addwater : float array
        addwaterrunoff : float array
        storedrainprm : float array
        snowpacklimit : float array
        snowprof_24hr : float array
        snowpack_in : float array
        snowfrac_in : float array
        snowwater_in : float array
        icefrac_in : float array
        snowdens_in : float array
        snowfallcum_in : float
        state_id_in : float array
        soilstore_id_in : float array
        qn_surf : float array
        qs_surf : float array
        snowremoval : float array
        snowpack_out : float array
        snowfrac_out : float array
        snowwater_out : float array
        icefrac_out : float array
        snowdens_out : float array
        state_id_out : float array
        soilstore_id_out : float array
        qe_surf : float array
        qe_roof : float array
        qe_wall : float array
        rss_surf : float array
        dataoutlinesnow : float array
        
        Returns
        -------
        snowfallcum_out : float
        state_per_tstep : float
        nwstate_per_tstep : float
        qe : float
        snowalb_out : float
        swe : float
        chsnow_per_tstep : float
        ev_per_tstep : float
        runoff_per_tstep : float
        surf_chang_per_tstep : float
        runoffpipes : float
        mwstore : float
        runoffwaterbody : float
        runoffagveg : float
        runoffagimpervious : float
        
        """
        snowfallcum_out, state_per_tstep, nwstate_per_tstep, qe, snowalb_out, swe, \
            chsnow_per_tstep, ev_per_tstep, runoff_per_tstep, surf_chang_per_tstep, \
            runoffpipes, mwstore, runoffwaterbody, runoffagveg, runoffagimpervious = \
            _supy_driver.f90wrap_suews_cal_snow(diagnose=diagnose, nlayer=nlayer, \
            tstep=tstep, imin=imin, it=it, evapmethod=evapmethod, \
            dayofweek_id=dayofweek_id, crwmin=crwmin, crwmax=crwmax, dectime=dectime, \
            avdens=avdens, avcp=avcp, lv_j_kg=lv_j_kg, lvs_j_kg=lvs_j_kg, avrh=avrh, \
            press_hpa=press_hpa, temp_c=temp_c, rasnow=rasnow, psyc_hpa=psyc_hpa, \
            sice_hpa=sice_hpa, tau_r=tau_r, radmeltfact=radmeltfact, \
            tempmeltfact=tempmeltfact, snowalbmax=snowalbmax, preciplimit=preciplimit, \
            preciplimitalb=preciplimitalb, qn_ind_snow=qn_ind_snow, \
            kup_ind_snow=kup_ind_snow, deltaqi=deltaqi, tsurf_ind_snow=tsurf_ind_snow, \
            snowalb_in=snowalb_in, pervfraction=pervfraction, vegfraction=vegfraction, \
            addimpervious=addimpervious, qn_snowfree=qn_snowfree, qf=qf, qs=qs, \
            vpd_hpa=vpd_hpa, s_hpa=s_hpa, rs=rs, ra=ra, rb=rb, snowdensmax=snowdensmax, \
            snowdensmin=snowdensmin, precip=precip, pipecapacity=pipecapacity, \
            runofftowater=runofftowater, addveg=addveg, snowlimpaved=snowlimpaved, \
            snowlimbldg=snowlimbldg, flowchange=flowchange, drain=drain, \
            wetthresh_surf=wetthresh_surf, soilstorecap=soilstorecap, \
            tsurf_ind=tsurf_ind, sfr_surf=sfr_surf, addwater=addwater, \
            addwaterrunoff=addwaterrunoff, storedrainprm=storedrainprm, \
            snowpacklimit=snowpacklimit, snowprof_24hr=snowprof_24hr, \
            snowpack_in=snowpack_in, snowfrac_in=snowfrac_in, snowwater_in=snowwater_in, \
            icefrac_in=icefrac_in, snowdens_in=snowdens_in, \
            snowfallcum_in=snowfallcum_in, state_id_in=state_id_in, \
            soilstore_id_in=soilstore_id_in, qn_surf=qn_surf, qs_surf=qs_surf, \
            snowremoval=snowremoval, snowpack_out=snowpack_out, \
            snowfrac_out=snowfrac_out, snowwater_out=snowwater_out, \
            icefrac_out=icefrac_out, snowdens_out=snowdens_out, \
            state_id_out=state_id_out, soilstore_id_out=soilstore_id_out, \
            qe_surf=qe_surf, qe_roof=qe_roof, qe_wall=qe_wall, rss_surf=rss_surf, \
            dataoutlinesnow=dataoutlinesnow)
        return snowfallcum_out, state_per_tstep, nwstate_per_tstep, qe, snowalb_out, \
            swe, chsnow_per_tstep, ev_per_tstep, runoff_per_tstep, surf_chang_per_tstep, \
            runoffpipes, mwstore, runoffwaterbody, runoffagveg, runoffagimpervious
    
    @staticmethod
    def suews_cal_snow_dts(diagnose, nlayer, tstep, imin, it, evapmethod, \
        dayofweek_id, crwmin, crwmax, dectime, avdens, avcp, lv_j_kg, lvs_j_kg, \
        avrh, press_hpa, temp_c, rasnow, psyc_hpa, sice_hpa, tau_r, radmeltfact, \
        tempmeltfact, snowalbmax, preciplimit, preciplimitalb, qn_ind_snow, \
        kup_ind_snow, deltaqi, tsurf_ind_snow, snowalb_in, pervfraction, \
        vegfraction, addimpervious, qn_snowfree, qf, qs, vpd_hpa, s_hpa, rs, ra, rb, \
        snowdensmax, snowdensmin, precip, pipecapacity, runofftowater, addveg, \
        snowlimpaved, snowlimbldg, flowchange, drain, wetthresh_paved, \
        wetthresh_bldg, wetthresh_evetr, wetthresh_dectr, wetthresh_grass, \
        wetthresh_bsoil, wetthresh_water, soilstorecap_paved, soilstorecap_bldg, \
        soilstorecap_evetr, soilstorecap_dectr, soilstorecap_grass, \
        soilstorecap_bsoil, soilstorecap_water, tsurf_ind, sfr_paved, sfr_bldg, \
        sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, addwater, \
        addwaterrunoff, storedrainprm, snowpacklimit, snowprof_24hr_working, \
        snowprof_24hr_holiday, snowpack_in, snowfrac_in, snowwater_in, icefrac_in, \
        snowdens_in, snowfallcum_in, state_id_in, soilstore_id_in, qn_surf, qs_surf, \
        snowremoval, snowpack_out, snowfrac_out, snowwater_out, icefrac_out, \
        snowdens_out, state_id_out, soilstore_id_out, qe_surf, qe_roof, qe_wall, \
        rss_surf, dataoutlinesnow):
        """
        snowfallcum_out, state_per_tstep, nwstate_per_tstep, qe, snowalb_out, swe, \
            chsnow_per_tstep, ev_per_tstep, runoff_per_tstep, surf_chang_per_tstep, \
            runoffpipes, mwstore, runoffwaterbody, runoffagveg, runoffagimpervious = \
            suews_cal_snow_dts(diagnose, nlayer, tstep, imin, it, evapmethod, \
            dayofweek_id, crwmin, crwmax, dectime, avdens, avcp, lv_j_kg, lvs_j_kg, \
            avrh, press_hpa, temp_c, rasnow, psyc_hpa, sice_hpa, tau_r, radmeltfact, \
            tempmeltfact, snowalbmax, preciplimit, preciplimitalb, qn_ind_snow, \
            kup_ind_snow, deltaqi, tsurf_ind_snow, snowalb_in, pervfraction, \
            vegfraction, addimpervious, qn_snowfree, qf, qs, vpd_hpa, s_hpa, rs, ra, rb, \
            snowdensmax, snowdensmin, precip, pipecapacity, runofftowater, addveg, \
            snowlimpaved, snowlimbldg, flowchange, drain, wetthresh_paved, \
            wetthresh_bldg, wetthresh_evetr, wetthresh_dectr, wetthresh_grass, \
            wetthresh_bsoil, wetthresh_water, soilstorecap_paved, soilstorecap_bldg, \
            soilstorecap_evetr, soilstorecap_dectr, soilstorecap_grass, \
            soilstorecap_bsoil, soilstorecap_water, tsurf_ind, sfr_paved, sfr_bldg, \
            sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, addwater, \
            addwaterrunoff, storedrainprm, snowpacklimit, snowprof_24hr_working, \
            snowprof_24hr_holiday, snowpack_in, snowfrac_in, snowwater_in, icefrac_in, \
            snowdens_in, snowfallcum_in, state_id_in, soilstore_id_in, qn_surf, qs_surf, \
            snowremoval, snowpack_out, snowfrac_out, snowwater_out, icefrac_out, \
            snowdens_out, state_id_out, soilstore_id_out, qe_surf, qe_roof, qe_wall, \
            rss_surf, dataoutlinesnow)
        
        
        Defined at suews_ctrl_driver.fpp lines 6917-7248
        
        Parameters
        ----------
        diagnose : int
        nlayer : int
        tstep : int
        imin : int
        it : int
        evapmethod : int
        dayofweek_id : int array
        crwmin : float
        crwmax : float
        dectime : float
        avdens : float
        avcp : float
        lv_j_kg : float
        lvs_j_kg : float
        avrh : float
        press_hpa : float
        temp_c : float
        rasnow : float
        psyc_hpa : float
        sice_hpa : float
        tau_r : float
        radmeltfact : float
        tempmeltfact : float
        snowalbmax : float
        preciplimit : float
        preciplimitalb : float
        qn_ind_snow : float array
        kup_ind_snow : float array
        deltaqi : float array
        tsurf_ind_snow : float array
        snowalb_in : float
        pervfraction : float
        vegfraction : float
        addimpervious : float
        qn_snowfree : float
        qf : float
        qs : float
        vpd_hpa : float
        s_hpa : float
        rs : float
        ra : float
        rb : float
        snowdensmax : float
        snowdensmin : float
        precip : float
        pipecapacity : float
        runofftowater : float
        addveg : float
        snowlimpaved : float
        snowlimbldg : float
        flowchange : float
        drain : float array
        wetthresh_paved : float
        wetthresh_bldg : float
        wetthresh_evetr : float
        wetthresh_dectr : float
        wetthresh_grass : float
        wetthresh_bsoil : float
        wetthresh_water : float
        soilstorecap_paved : float
        soilstorecap_bldg : float
        soilstorecap_evetr : float
        soilstorecap_dectr : float
        soilstorecap_grass : float
        soilstorecap_bsoil : float
        soilstorecap_water : float
        tsurf_ind : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        addwater : float array
        addwaterrunoff : float array
        storedrainprm : float array
        snowpacklimit : float array
        snowprof_24hr_working : float array
        snowprof_24hr_holiday : float array
        snowpack_in : float array
        snowfrac_in : float array
        snowwater_in : float array
        icefrac_in : float array
        snowdens_in : float array
        snowfallcum_in : float
        state_id_in : float array
        soilstore_id_in : float array
        qn_surf : float array
        qs_surf : float array
        snowremoval : float array
        snowpack_out : float array
        snowfrac_out : float array
        snowwater_out : float array
        icefrac_out : float array
        snowdens_out : float array
        state_id_out : float array
        soilstore_id_out : float array
        qe_surf : float array
        qe_roof : float array
        qe_wall : float array
        rss_surf : float array
        dataoutlinesnow : float array
        
        Returns
        -------
        snowfallcum_out : float
        state_per_tstep : float
        nwstate_per_tstep : float
        qe : float
        snowalb_out : float
        swe : float
        chsnow_per_tstep : float
        ev_per_tstep : float
        runoff_per_tstep : float
        surf_chang_per_tstep : float
        runoffpipes : float
        mwstore : float
        runoffwaterbody : float
        runoffagveg : float
        runoffagimpervious : float
        
        """
        snowfallcum_out, state_per_tstep, nwstate_per_tstep, qe, snowalb_out, swe, \
            chsnow_per_tstep, ev_per_tstep, runoff_per_tstep, surf_chang_per_tstep, \
            runoffpipes, mwstore, runoffwaterbody, runoffagveg, runoffagimpervious = \
            _supy_driver.f90wrap_suews_cal_snow_dts(diagnose=diagnose, nlayer=nlayer, \
            tstep=tstep, imin=imin, it=it, evapmethod=evapmethod, \
            dayofweek_id=dayofweek_id, crwmin=crwmin, crwmax=crwmax, dectime=dectime, \
            avdens=avdens, avcp=avcp, lv_j_kg=lv_j_kg, lvs_j_kg=lvs_j_kg, avrh=avrh, \
            press_hpa=press_hpa, temp_c=temp_c, rasnow=rasnow, psyc_hpa=psyc_hpa, \
            sice_hpa=sice_hpa, tau_r=tau_r, radmeltfact=radmeltfact, \
            tempmeltfact=tempmeltfact, snowalbmax=snowalbmax, preciplimit=preciplimit, \
            preciplimitalb=preciplimitalb, qn_ind_snow=qn_ind_snow, \
            kup_ind_snow=kup_ind_snow, deltaqi=deltaqi, tsurf_ind_snow=tsurf_ind_snow, \
            snowalb_in=snowalb_in, pervfraction=pervfraction, vegfraction=vegfraction, \
            addimpervious=addimpervious, qn_snowfree=qn_snowfree, qf=qf, qs=qs, \
            vpd_hpa=vpd_hpa, s_hpa=s_hpa, rs=rs, ra=ra, rb=rb, snowdensmax=snowdensmax, \
            snowdensmin=snowdensmin, precip=precip, pipecapacity=pipecapacity, \
            runofftowater=runofftowater, addveg=addveg, snowlimpaved=snowlimpaved, \
            snowlimbldg=snowlimbldg, flowchange=flowchange, drain=drain, \
            wetthresh_paved=wetthresh_paved, wetthresh_bldg=wetthresh_bldg, \
            wetthresh_evetr=wetthresh_evetr, wetthresh_dectr=wetthresh_dectr, \
            wetthresh_grass=wetthresh_grass, wetthresh_bsoil=wetthresh_bsoil, \
            wetthresh_water=wetthresh_water, soilstorecap_paved=soilstorecap_paved, \
            soilstorecap_bldg=soilstorecap_bldg, soilstorecap_evetr=soilstorecap_evetr, \
            soilstorecap_dectr=soilstorecap_dectr, \
            soilstorecap_grass=soilstorecap_grass, \
            soilstorecap_bsoil=soilstorecap_bsoil, \
            soilstorecap_water=soilstorecap_water, tsurf_ind=tsurf_ind, \
            sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, \
            sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, \
            sfr_water=sfr_water, addwater=addwater, addwaterrunoff=addwaterrunoff, \
            storedrainprm=storedrainprm, snowpacklimit=snowpacklimit, \
            snowprof_24hr_working=snowprof_24hr_working, \
            snowprof_24hr_holiday=snowprof_24hr_holiday, snowpack_in=snowpack_in, \
            snowfrac_in=snowfrac_in, snowwater_in=snowwater_in, icefrac_in=icefrac_in, \
            snowdens_in=snowdens_in, snowfallcum_in=snowfallcum_in, \
            state_id_in=state_id_in, soilstore_id_in=soilstore_id_in, qn_surf=qn_surf, \
            qs_surf=qs_surf, snowremoval=snowremoval, snowpack_out=snowpack_out, \
            snowfrac_out=snowfrac_out, snowwater_out=snowwater_out, \
            icefrac_out=icefrac_out, snowdens_out=snowdens_out, \
            state_id_out=state_id_out, soilstore_id_out=soilstore_id_out, \
            qe_surf=qe_surf, qe_roof=qe_roof, qe_wall=qe_wall, rss_surf=rss_surf, \
            dataoutlinesnow=dataoutlinesnow)
        return snowfallcum_out, state_per_tstep, nwstate_per_tstep, qe, snowalb_out, \
            swe, chsnow_per_tstep, ev_per_tstep, runoff_per_tstep, surf_chang_per_tstep, \
            runoffpipes, mwstore, runoffwaterbody, runoffagveg, runoffagimpervious
    
    @staticmethod
    def suews_cal_qe(diagnose, storageheatmethod, nlayer, tstep, evapmethod, avdens, \
        avcp, lv_j_kg, psyc_hpa, pervfraction, addimpervious, qf, vpd_hpa, s_hpa, \
        rs, ra_h, rb, precip, pipecapacity, runofftowater, nonwaterfraction, \
        wu_surf, addveg, addwaterbody, addwater_surf, flowchange, drain_surf, \
        frac_water2runoff_surf, storedrainprm, sfr_surf, statelimit_surf, \
        soilstorecap_surf, wetthresh_surf, state_surf_in, soilstore_surf_in, \
        qn_surf, qs_surf, sfr_roof, statelimit_roof, soilstorecap_roof, \
        wetthresh_roof, state_roof_in, soilstore_roof_in, qn_roof, qs_roof, \
        sfr_wall, statelimit_wall, soilstorecap_wall, wetthresh_wall, state_wall_in, \
        soilstore_wall_in, qn_wall, qs_wall, state_surf_out, soilstore_surf_out, \
        ev_surf, state_roof_out, soilstore_roof_out, ev_roof, state_wall_out, \
        soilstore_wall_out, ev_wall, ev0_surf, qe0_surf, qe_surf, qe_roof, qe_wall, \
        rss_surf):
        """
        state_grid, nwstate_grid, qe, ev_grid, runoff_grid, surf_chang_grid, \
            runoffpipes_grid, runoffwaterbody_grid, runoffagveg_grid, \
            runoffagimpervious_grid = suews_cal_qe(diagnose, storageheatmethod, nlayer, \
            tstep, evapmethod, avdens, avcp, lv_j_kg, psyc_hpa, pervfraction, \
            addimpervious, qf, vpd_hpa, s_hpa, rs, ra_h, rb, precip, pipecapacity, \
            runofftowater, nonwaterfraction, wu_surf, addveg, addwaterbody, \
            addwater_surf, flowchange, drain_surf, frac_water2runoff_surf, \
            storedrainprm, sfr_surf, statelimit_surf, soilstorecap_surf, wetthresh_surf, \
            state_surf_in, soilstore_surf_in, qn_surf, qs_surf, sfr_roof, \
            statelimit_roof, soilstorecap_roof, wetthresh_roof, state_roof_in, \
            soilstore_roof_in, qn_roof, qs_roof, sfr_wall, statelimit_wall, \
            soilstorecap_wall, wetthresh_wall, state_wall_in, soilstore_wall_in, \
            qn_wall, qs_wall, state_surf_out, soilstore_surf_out, ev_surf, \
            state_roof_out, soilstore_roof_out, ev_roof, state_wall_out, \
            soilstore_wall_out, ev_wall, ev0_surf, qe0_surf, qe_surf, qe_roof, qe_wall, \
            rss_surf)
        
        
        Defined at suews_ctrl_driver.fpp lines 7280-7576
        
        Parameters
        ----------
        diagnose : int
        storageheatmethod : int
        nlayer : int
        tstep : int
        evapmethod : int
        avdens : float
        avcp : float
        lv_j_kg : float
        psyc_hpa : float
        pervfraction : float
        addimpervious : float
        qf : float
        vpd_hpa : float
        s_hpa : float
        rs : float
        ra_h : float
        rb : float
        precip : float
        pipecapacity : float
        runofftowater : float
        nonwaterfraction : float
        wu_surf : float array
        addveg : float
        addwaterbody : float
        addwater_surf : float array
        flowchange : float
        drain_surf : float array
        frac_water2runoff_surf : float array
        storedrainprm : float array
        sfr_surf : float array
        statelimit_surf : float array
        soilstorecap_surf : float array
        wetthresh_surf : float array
        state_surf_in : float array
        soilstore_surf_in : float array
        qn_surf : float array
        qs_surf : float array
        sfr_roof : float array
        statelimit_roof : float array
        soilstorecap_roof : float array
        wetthresh_roof : float array
        state_roof_in : float array
        soilstore_roof_in : float array
        qn_roof : float array
        qs_roof : float array
        sfr_wall : float array
        statelimit_wall : float array
        soilstorecap_wall : float array
        wetthresh_wall : float array
        state_wall_in : float array
        soilstore_wall_in : float array
        qn_wall : float array
        qs_wall : float array
        state_surf_out : float array
        soilstore_surf_out : float array
        ev_surf : float array
        state_roof_out : float array
        soilstore_roof_out : float array
        ev_roof : float array
        state_wall_out : float array
        soilstore_wall_out : float array
        ev_wall : float array
        ev0_surf : float array
        qe0_surf : float array
        qe_surf : float array
        qe_roof : float array
        qe_wall : float array
        rss_surf : float array
        
        Returns
        -------
        state_grid : float
        nwstate_grid : float
        qe : float
        ev_grid : float
        runoff_grid : float
        surf_chang_grid : float
        runoffpipes_grid : float
        runoffwaterbody_grid : float
        runoffagveg_grid : float
        runoffagimpervious_grid : float
        
        """
        state_grid, nwstate_grid, qe, ev_grid, runoff_grid, surf_chang_grid, \
            runoffpipes_grid, runoffwaterbody_grid, runoffagveg_grid, \
            runoffagimpervious_grid = \
            _supy_driver.f90wrap_suews_cal_qe(diagnose=diagnose, \
            storageheatmethod=storageheatmethod, nlayer=nlayer, tstep=tstep, \
            evapmethod=evapmethod, avdens=avdens, avcp=avcp, lv_j_kg=lv_j_kg, \
            psyc_hpa=psyc_hpa, pervfraction=pervfraction, addimpervious=addimpervious, \
            qf=qf, vpd_hpa=vpd_hpa, s_hpa=s_hpa, rs=rs, ra_h=ra_h, rb=rb, precip=precip, \
            pipecapacity=pipecapacity, runofftowater=runofftowater, \
            nonwaterfraction=nonwaterfraction, wu_surf=wu_surf, addveg=addveg, \
            addwaterbody=addwaterbody, addwater_surf=addwater_surf, \
            flowchange=flowchange, drain_surf=drain_surf, \
            frac_water2runoff_surf=frac_water2runoff_surf, storedrainprm=storedrainprm, \
            sfr_surf=sfr_surf, statelimit_surf=statelimit_surf, \
            soilstorecap_surf=soilstorecap_surf, wetthresh_surf=wetthresh_surf, \
            state_surf_in=state_surf_in, soilstore_surf_in=soilstore_surf_in, \
            qn_surf=qn_surf, qs_surf=qs_surf, sfr_roof=sfr_roof, \
            statelimit_roof=statelimit_roof, soilstorecap_roof=soilstorecap_roof, \
            wetthresh_roof=wetthresh_roof, state_roof_in=state_roof_in, \
            soilstore_roof_in=soilstore_roof_in, qn_roof=qn_roof, qs_roof=qs_roof, \
            sfr_wall=sfr_wall, statelimit_wall=statelimit_wall, \
            soilstorecap_wall=soilstorecap_wall, wetthresh_wall=wetthresh_wall, \
            state_wall_in=state_wall_in, soilstore_wall_in=soilstore_wall_in, \
            qn_wall=qn_wall, qs_wall=qs_wall, state_surf_out=state_surf_out, \
            soilstore_surf_out=soilstore_surf_out, ev_surf=ev_surf, \
            state_roof_out=state_roof_out, soilstore_roof_out=soilstore_roof_out, \
            ev_roof=ev_roof, state_wall_out=state_wall_out, \
            soilstore_wall_out=soilstore_wall_out, ev_wall=ev_wall, ev0_surf=ev0_surf, \
            qe0_surf=qe0_surf, qe_surf=qe_surf, qe_roof=qe_roof, qe_wall=qe_wall, \
            rss_surf=rss_surf)
        return state_grid, nwstate_grid, qe, ev_grid, runoff_grid, surf_chang_grid, \
            runoffpipes_grid, runoffwaterbody_grid, runoffagveg_grid, \
            runoffagimpervious_grid
    
    @staticmethod
    def suews_cal_qe_dts(diagnose, storageheatmethod, nlayer, tstep, evapmethod, \
        avdens, avcp, lv_j_kg, psyc_hpa, pervfraction, addimpervious, qf, vpd_hpa, \
        s_hpa, rs, ra_h, rb, precip, pipecapacity, runofftowater, nonwaterfraction, \
        wu_surf, addveg, addwaterbody, addwater_surf, flowchange, drain_surf, \
        frac_water2runoff_surf, storedrainprm, sfr_paved, sfr_bldg, sfr_evetr, \
        sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, statelimit_paved, \
        statelimit_bldg, statelimit_evetr, statelimit_dectr, statelimit_grass, \
        statelimit_bsoil, statelimit_water, soilstorecap_paved, soilstorecap_bldg, \
        soilstorecap_evetr, soilstorecap_dectr, soilstorecap_grass, \
        soilstorecap_bsoil, soilstorecap_water, wetthresh_paved, wetthresh_bldg, \
        wetthresh_evetr, wetthresh_dectr, wetthresh_grass, wetthresh_bsoil, \
        wetthresh_water, state_surf_in, soilstore_surf_in, qn_surf, qs_surf, \
        sfr_roof, statelimit_roof, soilstorecap_roof, wetthresh_roof, state_roof_in, \
        soilstore_roof_in, qn_roof, qs_roof, sfr_wall, statelimit_wall, \
        soilstorecap_wall, wetthresh_wall, state_wall_in, soilstore_wall_in, \
        qn_wall, qs_wall, state_surf_out, soilstore_surf_out, ev_surf, \
        state_roof_out, soilstore_roof_out, ev_roof, state_wall_out, \
        soilstore_wall_out, ev_wall, ev0_surf, qe0_surf, qe_surf, qe_roof, qe_wall, \
        rss_surf):
        """
        state_grid, nwstate_grid, qe, ev_grid, runoff_grid, surf_chang_grid, \
            runoffpipes_grid, runoffwaterbody_grid, runoffagveg_grid, \
            runoffagimpervious_grid = suews_cal_qe_dts(diagnose, storageheatmethod, \
            nlayer, tstep, evapmethod, avdens, avcp, lv_j_kg, psyc_hpa, pervfraction, \
            addimpervious, qf, vpd_hpa, s_hpa, rs, ra_h, rb, precip, pipecapacity, \
            runofftowater, nonwaterfraction, wu_surf, addveg, addwaterbody, \
            addwater_surf, flowchange, drain_surf, frac_water2runoff_surf, \
            storedrainprm, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, \
            sfr_bsoil, sfr_water, statelimit_paved, statelimit_bldg, statelimit_evetr, \
            statelimit_dectr, statelimit_grass, statelimit_bsoil, statelimit_water, \
            soilstorecap_paved, soilstorecap_bldg, soilstorecap_evetr, \
            soilstorecap_dectr, soilstorecap_grass, soilstorecap_bsoil, \
            soilstorecap_water, wetthresh_paved, wetthresh_bldg, wetthresh_evetr, \
            wetthresh_dectr, wetthresh_grass, wetthresh_bsoil, wetthresh_water, \
            state_surf_in, soilstore_surf_in, qn_surf, qs_surf, sfr_roof, \
            statelimit_roof, soilstorecap_roof, wetthresh_roof, state_roof_in, \
            soilstore_roof_in, qn_roof, qs_roof, sfr_wall, statelimit_wall, \
            soilstorecap_wall, wetthresh_wall, state_wall_in, soilstore_wall_in, \
            qn_wall, qs_wall, state_surf_out, soilstore_surf_out, ev_surf, \
            state_roof_out, soilstore_roof_out, ev_roof, state_wall_out, \
            soilstore_wall_out, ev_wall, ev0_surf, qe0_surf, qe_surf, qe_roof, qe_wall, \
            rss_surf)
        
        
        Defined at suews_ctrl_driver.fpp lines 7578-7876
        
        Parameters
        ----------
        diagnose : int
        storageheatmethod : int
        nlayer : int
        tstep : int
        evapmethod : int
        avdens : float
        avcp : float
        lv_j_kg : float
        psyc_hpa : float
        pervfraction : float
        addimpervious : float
        qf : float
        vpd_hpa : float
        s_hpa : float
        rs : float
        ra_h : float
        rb : float
        precip : float
        pipecapacity : float
        runofftowater : float
        nonwaterfraction : float
        wu_surf : float array
        addveg : float
        addwaterbody : float
        addwater_surf : float array
        flowchange : float
        drain_surf : float array
        frac_water2runoff_surf : float array
        storedrainprm : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        statelimit_paved : float
        statelimit_bldg : float
        statelimit_evetr : float
        statelimit_dectr : float
        statelimit_grass : float
        statelimit_bsoil : float
        statelimit_water : float
        soilstorecap_paved : float
        soilstorecap_bldg : float
        soilstorecap_evetr : float
        soilstorecap_dectr : float
        soilstorecap_grass : float
        soilstorecap_bsoil : float
        soilstorecap_water : float
        wetthresh_paved : float
        wetthresh_bldg : float
        wetthresh_evetr : float
        wetthresh_dectr : float
        wetthresh_grass : float
        wetthresh_bsoil : float
        wetthresh_water : float
        state_surf_in : float array
        soilstore_surf_in : float array
        qn_surf : float array
        qs_surf : float array
        sfr_roof : float array
        statelimit_roof : float array
        soilstorecap_roof : float array
        wetthresh_roof : float array
        state_roof_in : float array
        soilstore_roof_in : float array
        qn_roof : float array
        qs_roof : float array
        sfr_wall : float array
        statelimit_wall : float array
        soilstorecap_wall : float array
        wetthresh_wall : float array
        state_wall_in : float array
        soilstore_wall_in : float array
        qn_wall : float array
        qs_wall : float array
        state_surf_out : float array
        soilstore_surf_out : float array
        ev_surf : float array
        state_roof_out : float array
        soilstore_roof_out : float array
        ev_roof : float array
        state_wall_out : float array
        soilstore_wall_out : float array
        ev_wall : float array
        ev0_surf : float array
        qe0_surf : float array
        qe_surf : float array
        qe_roof : float array
        qe_wall : float array
        rss_surf : float array
        
        Returns
        -------
        state_grid : float
        nwstate_grid : float
        qe : float
        ev_grid : float
        runoff_grid : float
        surf_chang_grid : float
        runoffpipes_grid : float
        runoffwaterbody_grid : float
        runoffagveg_grid : float
        runoffagimpervious_grid : float
        
        """
        state_grid, nwstate_grid, qe, ev_grid, runoff_grid, surf_chang_grid, \
            runoffpipes_grid, runoffwaterbody_grid, runoffagveg_grid, \
            runoffagimpervious_grid = \
            _supy_driver.f90wrap_suews_cal_qe_dts(diagnose=diagnose, \
            storageheatmethod=storageheatmethod, nlayer=nlayer, tstep=tstep, \
            evapmethod=evapmethod, avdens=avdens, avcp=avcp, lv_j_kg=lv_j_kg, \
            psyc_hpa=psyc_hpa, pervfraction=pervfraction, addimpervious=addimpervious, \
            qf=qf, vpd_hpa=vpd_hpa, s_hpa=s_hpa, rs=rs, ra_h=ra_h, rb=rb, precip=precip, \
            pipecapacity=pipecapacity, runofftowater=runofftowater, \
            nonwaterfraction=nonwaterfraction, wu_surf=wu_surf, addveg=addveg, \
            addwaterbody=addwaterbody, addwater_surf=addwater_surf, \
            flowchange=flowchange, drain_surf=drain_surf, \
            frac_water2runoff_surf=frac_water2runoff_surf, storedrainprm=storedrainprm, \
            sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, \
            sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, \
            sfr_water=sfr_water, statelimit_paved=statelimit_paved, \
            statelimit_bldg=statelimit_bldg, statelimit_evetr=statelimit_evetr, \
            statelimit_dectr=statelimit_dectr, statelimit_grass=statelimit_grass, \
            statelimit_bsoil=statelimit_bsoil, statelimit_water=statelimit_water, \
            soilstorecap_paved=soilstorecap_paved, soilstorecap_bldg=soilstorecap_bldg, \
            soilstorecap_evetr=soilstorecap_evetr, \
            soilstorecap_dectr=soilstorecap_dectr, \
            soilstorecap_grass=soilstorecap_grass, \
            soilstorecap_bsoil=soilstorecap_bsoil, \
            soilstorecap_water=soilstorecap_water, wetthresh_paved=wetthresh_paved, \
            wetthresh_bldg=wetthresh_bldg, wetthresh_evetr=wetthresh_evetr, \
            wetthresh_dectr=wetthresh_dectr, wetthresh_grass=wetthresh_grass, \
            wetthresh_bsoil=wetthresh_bsoil, wetthresh_water=wetthresh_water, \
            state_surf_in=state_surf_in, soilstore_surf_in=soilstore_surf_in, \
            qn_surf=qn_surf, qs_surf=qs_surf, sfr_roof=sfr_roof, \
            statelimit_roof=statelimit_roof, soilstorecap_roof=soilstorecap_roof, \
            wetthresh_roof=wetthresh_roof, state_roof_in=state_roof_in, \
            soilstore_roof_in=soilstore_roof_in, qn_roof=qn_roof, qs_roof=qs_roof, \
            sfr_wall=sfr_wall, statelimit_wall=statelimit_wall, \
            soilstorecap_wall=soilstorecap_wall, wetthresh_wall=wetthresh_wall, \
            state_wall_in=state_wall_in, soilstore_wall_in=soilstore_wall_in, \
            qn_wall=qn_wall, qs_wall=qs_wall, state_surf_out=state_surf_out, \
            soilstore_surf_out=soilstore_surf_out, ev_surf=ev_surf, \
            state_roof_out=state_roof_out, soilstore_roof_out=soilstore_roof_out, \
            ev_roof=ev_roof, state_wall_out=state_wall_out, \
            soilstore_wall_out=soilstore_wall_out, ev_wall=ev_wall, ev0_surf=ev0_surf, \
            qe0_surf=qe0_surf, qe_surf=qe_surf, qe_roof=qe_roof, qe_wall=qe_wall, \
            rss_surf=rss_surf)
        return state_grid, nwstate_grid, qe, ev_grid, runoff_grid, surf_chang_grid, \
            runoffpipes_grid, runoffwaterbody_grid, runoffagveg_grid, \
            runoffagimpervious_grid
    
    @staticmethod
    def suews_cal_qh(qhmethod, nlayer, storageheatmethod, qn, qf, qmrain, qe, qs, \
        qmfreez, qm, avdens, avcp, sfr_surf, sfr_roof, sfr_wall, tsfc_surf, \
        tsfc_roof, tsfc_wall, temp_c, ra, qh_resist_surf, qh_resist_roof, \
        qh_resist_wall):
        """
        qh, qh_residual, qh_resist = suews_cal_qh(qhmethod, nlayer, storageheatmethod, \
            qn, qf, qmrain, qe, qs, qmfreez, qm, avdens, avcp, sfr_surf, sfr_roof, \
            sfr_wall, tsfc_surf, tsfc_roof, tsfc_wall, temp_c, ra, qh_resist_surf, \
            qh_resist_roof, qh_resist_wall)
        
        
        Defined at suews_ctrl_driver.fpp lines 7888-7963
        
        Parameters
        ----------
        qhmethod : int
        nlayer : int
        storageheatmethod : int
        qn : float
        qf : float
        qmrain : float
        qe : float
        qs : float
        qmfreez : float
        qm : float
        avdens : float
        avcp : float
        sfr_surf : float array
        sfr_roof : float array
        sfr_wall : float array
        tsfc_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        temp_c : float
        ra : float
        qh_resist_surf : float array
        qh_resist_roof : float array
        qh_resist_wall : float array
        
        Returns
        -------
        qh : float
        qh_residual : float
        qh_resist : float
        
        """
        qh, qh_residual, qh_resist = \
            _supy_driver.f90wrap_suews_cal_qh(qhmethod=qhmethod, nlayer=nlayer, \
            storageheatmethod=storageheatmethod, qn=qn, qf=qf, qmrain=qmrain, qe=qe, \
            qs=qs, qmfreez=qmfreez, qm=qm, avdens=avdens, avcp=avcp, sfr_surf=sfr_surf, \
            sfr_roof=sfr_roof, sfr_wall=sfr_wall, tsfc_surf=tsfc_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, temp_c=temp_c, ra=ra, \
            qh_resist_surf=qh_resist_surf, qh_resist_roof=qh_resist_roof, \
            qh_resist_wall=qh_resist_wall)
        return qh, qh_residual, qh_resist
    
    @staticmethod
    def suews_cal_qh_dts(qhmethod, nlayer, storageheatmethod, qn, qf, qmrain, qe, \
        qs, qmfreez, qm, avdens, avcp, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, \
        sfr_grass, sfr_bsoil, sfr_water, sfr_roof, sfr_wall, tsfc_surf, tsfc_roof, \
        tsfc_wall, temp_c, ra, qh_resist_surf, qh_resist_roof, qh_resist_wall):
        """
        qh, qh_residual, qh_resist = suews_cal_qh_dts(qhmethod, nlayer, \
            storageheatmethod, qn, qf, qmrain, qe, qs, qmfreez, qm, avdens, avcp, \
            sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
            sfr_roof, sfr_wall, tsfc_surf, tsfc_roof, tsfc_wall, temp_c, ra, \
            qh_resist_surf, qh_resist_roof, qh_resist_wall)
        
        
        Defined at suews_ctrl_driver.fpp lines 7965-8039
        
        Parameters
        ----------
        qhmethod : int
        nlayer : int
        storageheatmethod : int
        qn : float
        qf : float
        qmrain : float
        qe : float
        qs : float
        qmfreez : float
        qm : float
        avdens : float
        avcp : float
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        sfr_roof : float array
        sfr_wall : float array
        tsfc_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        temp_c : float
        ra : float
        qh_resist_surf : float array
        qh_resist_roof : float array
        qh_resist_wall : float array
        
        Returns
        -------
        qh : float
        qh_residual : float
        qh_resist : float
        
        """
        qh, qh_residual, qh_resist = \
            _supy_driver.f90wrap_suews_cal_qh_dts(qhmethod=qhmethod, nlayer=nlayer, \
            storageheatmethod=storageheatmethod, qn=qn, qf=qf, qmrain=qmrain, qe=qe, \
            qs=qs, qmfreez=qmfreez, qm=qm, avdens=avdens, avcp=avcp, \
            sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, \
            sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, \
            sfr_water=sfr_water, sfr_roof=sfr_roof, sfr_wall=sfr_wall, \
            tsfc_surf=tsfc_surf, tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, \
            temp_c=temp_c, ra=ra, qh_resist_surf=qh_resist_surf, \
            qh_resist_roof=qh_resist_roof, qh_resist_wall=qh_resist_wall)
        return qh, qh_residual, qh_resist
    
    @staticmethod
    def suews_cal_resistance(stabilitymethod, diagnose, aerodynamicresistancemethod, \
        roughlenheatmethod, snowuse, id, it, gsmodel, smdmethod, avdens, avcp, \
        qh_init, zzd, z0m, zdm, avu1, temp_c, vegfraction, avkdn, kmax, g_max, g_k, \
        g_q_base, g_q_shape, g_t, g_sm, s1, s2, th, tl, dq, xsmd, vsmd, \
        maxconductance, laimax, lai_id, snowfrac, sfr_surf):
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, ustar, tstar, l_mod, zl, gsc, rs, ra, rasnow, \
            rb, z0v, z0vsnow = suews_cal_resistance(stabilitymethod, diagnose, \
            aerodynamicresistancemethod, roughlenheatmethod, snowuse, id, it, gsmodel, \
            smdmethod, avdens, avcp, qh_init, zzd, z0m, zdm, avu1, temp_c, vegfraction, \
            avkdn, kmax, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, s1, s2, th, tl, dq, \
            xsmd, vsmd, maxconductance, laimax, lai_id, snowfrac, sfr_surf)
        
        
        Defined at suews_ctrl_driver.fpp lines 8056-8194
        
        Parameters
        ----------
        stabilitymethod : int
        diagnose : int
        aerodynamicresistancemethod : int
        roughlenheatmethod : int
        snowuse : int
        id : int
        it : int
        gsmodel : int
        smdmethod : int
        avdens : float
        avcp : float
        qh_init : float
        zzd : float
        z0m : float
        zdm : float
        avu1 : float
        temp_c : float
        vegfraction : float
        avkdn : float
        kmax : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        s1 : float
        s2 : float
        th : float
        tl : float
        dq : float
        xsmd : float
        vsmd : float
        maxconductance : float array
        laimax : float array
        lai_id : float array
        snowfrac : float array
        sfr_surf : float array
        
        Returns
        -------
        g_kdown : float
        g_dq : float
        g_ta : float
        g_smd : float
        g_lai : float
        ustar : float
        tstar : float
        l_mod : float
        zl : float
        gsc : float
        rs : float
        ra : float
        rasnow : float
        rb : float
        z0v : float
        z0vsnow : float
        
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, ustar, tstar, l_mod, zl, gsc, rs, ra, rasnow, \
            rb, z0v, z0vsnow = \
            _supy_driver.f90wrap_suews_cal_resistance(stabilitymethod=stabilitymethod, \
            diagnose=diagnose, aerodynamicresistancemethod=aerodynamicresistancemethod, \
            roughlenheatmethod=roughlenheatmethod, snowuse=snowuse, id=id, it=it, \
            gsmodel=gsmodel, smdmethod=smdmethod, avdens=avdens, avcp=avcp, \
            qh_init=qh_init, zzd=zzd, z0m=z0m, zdm=zdm, avu1=avu1, temp_c=temp_c, \
            vegfraction=vegfraction, avkdn=avkdn, kmax=kmax, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, s1=s1, s2=s2, \
            th=th, tl=tl, dq=dq, xsmd=xsmd, vsmd=vsmd, maxconductance=maxconductance, \
            laimax=laimax, lai_id=lai_id, snowfrac=snowfrac, sfr_surf=sfr_surf)
        return g_kdown, g_dq, g_ta, g_smd, g_lai, ustar, tstar, l_mod, zl, gsc, rs, ra, \
            rasnow, rb, z0v, z0vsnow
    
    @staticmethod
    def suews_cal_resistance_dts(stabilitymethod, diagnose, \
        aerodynamicresistancemethod, roughlenheatmethod, snowuse, id, it, gsmodel, \
        smdmethod, avdens, avcp, qh_init, zzd, z0m, zdm, avu1, temp_c, vegfraction, \
        avkdn, kmax, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, s1, s2, th, tl, dq, \
        xsmd, vsmd, maxconductance_evetr, maxconductance_dectr, \
        maxconductance_grass, laimax_evetr, laimax_dectr, laimax_grass, lai_id, \
        snowfrac, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, \
        sfr_water):
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, ustar, tstar, l_mod, zl, gsc, rs, ra, rasnow, \
            rb, z0v, z0vsnow = suews_cal_resistance_dts(stabilitymethod, diagnose, \
            aerodynamicresistancemethod, roughlenheatmethod, snowuse, id, it, gsmodel, \
            smdmethod, avdens, avcp, qh_init, zzd, z0m, zdm, avu1, temp_c, vegfraction, \
            avkdn, kmax, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, s1, s2, th, tl, dq, \
            xsmd, vsmd, maxconductance_evetr, maxconductance_dectr, \
            maxconductance_grass, laimax_evetr, laimax_dectr, laimax_grass, lai_id, \
            snowfrac, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, \
            sfr_water)
        
        
        Defined at suews_ctrl_driver.fpp lines 8196-8337
        
        Parameters
        ----------
        stabilitymethod : int
        diagnose : int
        aerodynamicresistancemethod : int
        roughlenheatmethod : int
        snowuse : int
        id : int
        it : int
        gsmodel : int
        smdmethod : int
        avdens : float
        avcp : float
        qh_init : float
        zzd : float
        z0m : float
        zdm : float
        avu1 : float
        temp_c : float
        vegfraction : float
        avkdn : float
        kmax : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        s1 : float
        s2 : float
        th : float
        tl : float
        dq : float
        xsmd : float
        vsmd : float
        maxconductance_evetr : float
        maxconductance_dectr : float
        maxconductance_grass : float
        laimax_evetr : float
        laimax_dectr : float
        laimax_grass : float
        lai_id : float array
        snowfrac : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        
        Returns
        -------
        g_kdown : float
        g_dq : float
        g_ta : float
        g_smd : float
        g_lai : float
        ustar : float
        tstar : float
        l_mod : float
        zl : float
        gsc : float
        rs : float
        ra : float
        rasnow : float
        rb : float
        z0v : float
        z0vsnow : float
        
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, ustar, tstar, l_mod, zl, gsc, rs, ra, rasnow, \
            rb, z0v, z0vsnow = \
            _supy_driver.f90wrap_suews_cal_resistance_dts(stabilitymethod=stabilitymethod, \
            diagnose=diagnose, aerodynamicresistancemethod=aerodynamicresistancemethod, \
            roughlenheatmethod=roughlenheatmethod, snowuse=snowuse, id=id, it=it, \
            gsmodel=gsmodel, smdmethod=smdmethod, avdens=avdens, avcp=avcp, \
            qh_init=qh_init, zzd=zzd, z0m=z0m, zdm=zdm, avu1=avu1, temp_c=temp_c, \
            vegfraction=vegfraction, avkdn=avkdn, kmax=kmax, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, s1=s1, s2=s2, \
            th=th, tl=tl, dq=dq, xsmd=xsmd, vsmd=vsmd, \
            maxconductance_evetr=maxconductance_evetr, \
            maxconductance_dectr=maxconductance_dectr, \
            maxconductance_grass=maxconductance_grass, laimax_evetr=laimax_evetr, \
            laimax_dectr=laimax_dectr, laimax_grass=laimax_grass, lai_id=lai_id, \
            snowfrac=snowfrac, sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, \
            sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, \
            sfr_bsoil=sfr_bsoil, sfr_water=sfr_water)
        return g_kdown, g_dq, g_ta, g_smd, g_lai, ustar, tstar, l_mod, zl, gsc, rs, ra, \
            rasnow, rb, z0v, z0vsnow
    
    @staticmethod
    def suews_update_outputline(additionalwater, alb, avkdn, avu10_ms, azimuth, \
        chsnow_per_interval, dectime, drain_per_tstep, e_mod, ev_per_tstep, ext_wu, \
        fc, fc_build, fcld, fc_metab, fc_photo, fc_respi, fc_point, fc_traff, \
        flowchange, h_mod, id, imin, int_wu, it, iy, kup, lai_id, ldown, l_mod, lup, \
        mwh, mwstore, nsh_real, nwstate_per_tstep, precip, q2_gkg, qeout, qf, qh, \
        qh_resist, qm, qmfreez, qmrain, qn, qn_snow, qn_snowfree, qs, ra, \
        resistsurf, rh2, runoffagimpervious, runoffagveg, runoff_per_tstep, \
        runoffpipes, runoffsoil_per_tstep, runoffwaterbody, sfr_surf, smd, \
        smd_nsurf, snowalb, snowremoval, state_id, state_per_tstep, \
        surf_chang_per_tstep, swe, t2_c, tskin_c, tot_chang_per_tstep, tsurf, ustar, \
        wu_nsurf, z0m, zdm, zenith_deg, datetimeline, dataoutlinesuews):
        """
        suews_update_outputline(additionalwater, alb, avkdn, avu10_ms, azimuth, \
            chsnow_per_interval, dectime, drain_per_tstep, e_mod, ev_per_tstep, ext_wu, \
            fc, fc_build, fcld, fc_metab, fc_photo, fc_respi, fc_point, fc_traff, \
            flowchange, h_mod, id, imin, int_wu, it, iy, kup, lai_id, ldown, l_mod, lup, \
            mwh, mwstore, nsh_real, nwstate_per_tstep, precip, q2_gkg, qeout, qf, qh, \
            qh_resist, qm, qmfreez, qmrain, qn, qn_snow, qn_snowfree, qs, ra, \
            resistsurf, rh2, runoffagimpervious, runoffagveg, runoff_per_tstep, \
            runoffpipes, runoffsoil_per_tstep, runoffwaterbody, sfr_surf, smd, \
            smd_nsurf, snowalb, snowremoval, state_id, state_per_tstep, \
            surf_chang_per_tstep, swe, t2_c, tskin_c, tot_chang_per_tstep, tsurf, ustar, \
            wu_nsurf, z0m, zdm, zenith_deg, datetimeline, dataoutlinesuews)
        
        
        Defined at suews_ctrl_driver.fpp lines 8359-8507
        
        Parameters
        ----------
        additionalwater : float
        alb : float array
        avkdn : float
        avu10_ms : float
        azimuth : float
        chsnow_per_interval : float
        dectime : float
        drain_per_tstep : float
        e_mod : float
        ev_per_tstep : float
        ext_wu : float
        fc : float
        fc_build : float
        fcld : float
        fc_metab : float
        fc_photo : float
        fc_respi : float
        fc_point : float
        fc_traff : float
        flowchange : float
        h_mod : float
        id : int
        imin : int
        int_wu : float
        it : int
        iy : int
        kup : float
        lai_id : float array
        ldown : float
        l_mod : float
        lup : float
        mwh : float
        mwstore : float
        nsh_real : float
        nwstate_per_tstep : float
        precip : float
        q2_gkg : float
        qeout : float
        qf : float
        qh : float
        qh_resist : float
        qm : float
        qmfreez : float
        qmrain : float
        qn : float
        qn_snow : float
        qn_snowfree : float
        qs : float
        ra : float
        resistsurf : float
        rh2 : float
        runoffagimpervious : float
        runoffagveg : float
        runoff_per_tstep : float
        runoffpipes : float
        runoffsoil_per_tstep : float
        runoffwaterbody : float
        sfr_surf : float array
        smd : float
        smd_nsurf : float array
        snowalb : float
        snowremoval : float array
        state_id : float array
        state_per_tstep : float
        surf_chang_per_tstep : float
        swe : float
        t2_c : float
        tskin_c : float
        tot_chang_per_tstep : float
        tsurf : float
        ustar : float
        wu_nsurf : float array
        z0m : float
        zdm : float
        zenith_deg : float
        datetimeline : float array
        dataoutlinesuews : float array
        
        =====================================================================
        ====================== Prepare data for output ======================
         values outside of reasonable range are set as NAN-like numbers. TS 10 Jun 2018
         Remove non-existing surface type from surface and soil outputs
         Added back in with NANs by HCW 24 Aug 2016
        """
        _supy_driver.f90wrap_suews_update_outputline(additionalwater=additionalwater, \
            alb=alb, avkdn=avkdn, avu10_ms=avu10_ms, azimuth=azimuth, \
            chsnow_per_interval=chsnow_per_interval, dectime=dectime, \
            drain_per_tstep=drain_per_tstep, e_mod=e_mod, ev_per_tstep=ev_per_tstep, \
            ext_wu=ext_wu, fc=fc, fc_build=fc_build, fcld=fcld, fc_metab=fc_metab, \
            fc_photo=fc_photo, fc_respi=fc_respi, fc_point=fc_point, fc_traff=fc_traff, \
            flowchange=flowchange, h_mod=h_mod, id=id, imin=imin, int_wu=int_wu, it=it, \
            iy=iy, kup=kup, lai_id=lai_id, ldown=ldown, l_mod=l_mod, lup=lup, mwh=mwh, \
            mwstore=mwstore, nsh_real=nsh_real, nwstate_per_tstep=nwstate_per_tstep, \
            precip=precip, q2_gkg=q2_gkg, qeout=qeout, qf=qf, qh=qh, \
            qh_resist=qh_resist, qm=qm, qmfreez=qmfreez, qmrain=qmrain, qn=qn, \
            qn_snow=qn_snow, qn_snowfree=qn_snowfree, qs=qs, ra=ra, \
            resistsurf=resistsurf, rh2=rh2, runoffagimpervious=runoffagimpervious, \
            runoffagveg=runoffagveg, runoff_per_tstep=runoff_per_tstep, \
            runoffpipes=runoffpipes, runoffsoil_per_tstep=runoffsoil_per_tstep, \
            runoffwaterbody=runoffwaterbody, sfr_surf=sfr_surf, smd=smd, \
            smd_nsurf=smd_nsurf, snowalb=snowalb, snowremoval=snowremoval, \
            state_id=state_id, state_per_tstep=state_per_tstep, \
            surf_chang_per_tstep=surf_chang_per_tstep, swe=swe, t2_c=t2_c, \
            tskin_c=tskin_c, tot_chang_per_tstep=tot_chang_per_tstep, tsurf=tsurf, \
            ustar=ustar, wu_nsurf=wu_nsurf, z0m=z0m, zdm=zdm, zenith_deg=zenith_deg, \
            datetimeline=datetimeline, dataoutlinesuews=dataoutlinesuews)
    
    @staticmethod
    def estmext_update_outputline(iy, id, it, imin, dectime, nlayer, tsfc_out_surf, \
        qs_surf, tsfc_out_roof, qn_roof, qs_roof, qe_roof, qh_roof, state_roof, \
        soilstore_roof, tsfc_out_wall, qn_wall, qs_wall, qe_wall, qh_wall, \
        state_wall, soilstore_wall, datetimeline, dataoutlineestmext):
        """
        estmext_update_outputline(iy, id, it, imin, dectime, nlayer, tsfc_out_surf, \
            qs_surf, tsfc_out_roof, qn_roof, qs_roof, qe_roof, qh_roof, state_roof, \
            soilstore_roof, tsfc_out_wall, qn_wall, qs_wall, qe_wall, qh_wall, \
            state_wall, soilstore_wall, datetimeline, dataoutlineestmext)
        
        
        Defined at suews_ctrl_driver.fpp lines 8528-8595
        
        Parameters
        ----------
        iy : int
        id : int
        it : int
        imin : int
        dectime : float
        nlayer : int
        tsfc_out_surf : float array
        qs_surf : float array
        tsfc_out_roof : float array
        qn_roof : float array
        qs_roof : float array
        qe_roof : float array
        qh_roof : float array
        state_roof : float array
        soilstore_roof : float array
        tsfc_out_wall : float array
        qn_wall : float array
        qs_wall : float array
        qe_wall : float array
        qh_wall : float array
        state_wall : float array
        soilstore_wall : float array
        datetimeline : float array
        dataoutlineestmext : float array
        
        ====================update output line end==============================
        """
        _supy_driver.f90wrap_estmext_update_outputline(iy=iy, id=id, it=it, imin=imin, \
            dectime=dectime, nlayer=nlayer, tsfc_out_surf=tsfc_out_surf, \
            qs_surf=qs_surf, tsfc_out_roof=tsfc_out_roof, qn_roof=qn_roof, \
            qs_roof=qs_roof, qe_roof=qe_roof, qh_roof=qh_roof, state_roof=state_roof, \
            soilstore_roof=soilstore_roof, tsfc_out_wall=tsfc_out_wall, qn_wall=qn_wall, \
            qs_wall=qs_wall, qe_wall=qe_wall, qh_wall=qh_wall, state_wall=state_wall, \
            soilstore_wall=soilstore_wall, datetimeline=datetimeline, \
            dataoutlineestmext=dataoutlineestmext)
    
    @staticmethod
    def fill_result_x(res_valid, n_fill):
        """
        res_filled = fill_result_x(res_valid, n_fill)
        
        
        Defined at suews_ctrl_driver.fpp lines 8598-8604
        
        Parameters
        ----------
        res_valid : float array
        n_fill : int
        
        Returns
        -------
        res_filled : float array
        
        """
        res_filled = _supy_driver.f90wrap_fill_result_x(res_valid=res_valid, \
            n_fill=n_fill)
        return res_filled
    
    @staticmethod
    def suews_update_output(snowuse, storageheatmethod, readlinesmetdata, \
        numberofgrids, ir, gridiv, dataoutlinesuews, dataoutlinesnow, \
        dataoutlineestm, dataoutlinersl, dataoutlinebeers, dataoutlinedebug, \
        dataoutlinespartacus, dataoutlineestmext, dataoutsuews, dataoutsnow, \
        dataoutestm, dataoutrsl, dataoutbeers, dataoutdebug, dataoutspartacus, \
        dataoutestmext):
        """
        suews_update_output(snowuse, storageheatmethod, readlinesmetdata, numberofgrids, \
            ir, gridiv, dataoutlinesuews, dataoutlinesnow, dataoutlineestm, \
            dataoutlinersl, dataoutlinebeers, dataoutlinedebug, dataoutlinespartacus, \
            dataoutlineestmext, dataoutsuews, dataoutsnow, dataoutestm, dataoutrsl, \
            dataoutbeers, dataoutdebug, dataoutspartacus, dataoutestmext)
        
        
        Defined at suews_ctrl_driver.fpp lines 8614-8659
        
        Parameters
        ----------
        snowuse : int
        storageheatmethod : int
        readlinesmetdata : int
        numberofgrids : int
        ir : int
        gridiv : int
        dataoutlinesuews : float array
        dataoutlinesnow : float array
        dataoutlineestm : float array
        dataoutlinersl : float array
        dataoutlinebeers : float array
        dataoutlinedebug : float array
        dataoutlinespartacus : float array
        dataoutlineestmext : float array
        dataoutsuews : float array
        dataoutsnow : float array
        dataoutestm : float array
        dataoutrsl : float array
        dataoutbeers : float array
        dataoutdebug : float array
        dataoutspartacus : float array
        dataoutestmext : float array
        
        ====================== update output arrays ==============================
        Define the overall output matrix to be printed out step by step
        """
        _supy_driver.f90wrap_suews_update_output(snowuse=snowuse, \
            storageheatmethod=storageheatmethod, readlinesmetdata=readlinesmetdata, \
            numberofgrids=numberofgrids, ir=ir, gridiv=gridiv, \
            dataoutlinesuews=dataoutlinesuews, dataoutlinesnow=dataoutlinesnow, \
            dataoutlineestm=dataoutlineestm, dataoutlinersl=dataoutlinersl, \
            dataoutlinebeers=dataoutlinebeers, dataoutlinedebug=dataoutlinedebug, \
            dataoutlinespartacus=dataoutlinespartacus, \
            dataoutlineestmext=dataoutlineestmext, dataoutsuews=dataoutsuews, \
            dataoutsnow=dataoutsnow, dataoutestm=dataoutestm, dataoutrsl=dataoutrsl, \
            dataoutbeers=dataoutbeers, dataoutdebug=dataoutdebug, \
            dataoutspartacus=dataoutspartacus, dataoutestmext=dataoutestmext)
    
    @staticmethod
    def suews_cal_surf(storageheatmethod, netradiationmethod, nlayer, sfr_surf, \
        building_frac, building_scale, height, sfr_roof, sfr_wall):
        """
        vegfraction, impervfraction, pervfraction, nonwaterfraction = \
            suews_cal_surf(storageheatmethod, netradiationmethod, nlayer, sfr_surf, \
            building_frac, building_scale, height, sfr_roof, sfr_wall)
        
        
        Defined at suews_ctrl_driver.fpp lines 8729-8778
        
        Parameters
        ----------
        storageheatmethod : int
        netradiationmethod : int
        nlayer : int
        sfr_surf : float array
        building_frac : float array
        building_scale : float array
        height : float array
        sfr_roof : float array
        sfr_wall : float array
        
        Returns
        -------
        vegfraction : float
        impervfraction : float
        pervfraction : float
        nonwaterfraction : float
        
        """
        vegfraction, impervfraction, pervfraction, nonwaterfraction = \
            _supy_driver.f90wrap_suews_cal_surf(storageheatmethod=storageheatmethod, \
            netradiationmethod=netradiationmethod, nlayer=nlayer, sfr_surf=sfr_surf, \
            building_frac=building_frac, building_scale=building_scale, height=height, \
            sfr_roof=sfr_roof, sfr_wall=sfr_wall)
        return vegfraction, impervfraction, pervfraction, nonwaterfraction
    
    @staticmethod
    def suews_cal_surf_dts(storageheatmethod, netradiationmethod, nlayer, sfr_paved, \
        sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
        building_frac, building_scale, height, sfr_roof, sfr_wall):
        """
        vegfraction, impervfraction, pervfraction, nonwaterfraction = \
            suews_cal_surf_dts(storageheatmethod, netradiationmethod, nlayer, sfr_paved, \
            sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
            building_frac, building_scale, height, sfr_roof, sfr_wall)
        
        
        Defined at suews_ctrl_driver.fpp lines 8780-8831
        
        Parameters
        ----------
        storageheatmethod : int
        netradiationmethod : int
        nlayer : int
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        building_frac : float array
        building_scale : float array
        height : float array
        sfr_roof : float array
        sfr_wall : float array
        
        Returns
        -------
        vegfraction : float
        impervfraction : float
        pervfraction : float
        nonwaterfraction : float
        
        """
        vegfraction, impervfraction, pervfraction, nonwaterfraction = \
            _supy_driver.f90wrap_suews_cal_surf_dts(storageheatmethod=storageheatmethod, \
            netradiationmethod=netradiationmethod, nlayer=nlayer, sfr_paved=sfr_paved, \
            sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, \
            sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, \
            building_frac=building_frac, building_scale=building_scale, height=height, \
            sfr_roof=sfr_roof, sfr_wall=sfr_wall)
        return vegfraction, impervfraction, pervfraction, nonwaterfraction
    
    @staticmethod
    def set_nan(x):
        """
        xx = set_nan(x)
        
        
        Defined at suews_ctrl_driver.fpp lines 8950-8963
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        xx : float
        
        """
        xx = _supy_driver.f90wrap_set_nan(x=x)
        return xx
    
    @staticmethod
    def square(x):
        """
        xx = square(x)
        
        
        Defined at suews_ctrl_driver.fpp lines 8967-8974
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        xx : float
        
        """
        xx = _supy_driver.f90wrap_square(x=x)
        return xx
    
    @staticmethod
    def square_real(x):
        """
        xx = square_real(x)
        
        
        Defined at suews_ctrl_driver.fpp lines 8976-8983
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        xx : float
        
        """
        xx = _supy_driver.f90wrap_square_real(x=x)
        return xx
    
    @staticmethod
    def output_name_n(i):
        """
        name, group, aggreg, outlevel = output_name_n(i)
        
        
        Defined at suews_ctrl_driver.fpp lines 8985-9005
        
        Parameters
        ----------
        i : int
        
        Returns
        -------
        name : str
        group : str
        aggreg : str
        outlevel : int
        
        """
        name, group, aggreg, outlevel = _supy_driver.f90wrap_output_name_n(i=i)
        return name, group, aggreg, outlevel
    
    @staticmethod
    def output_size():
        """
        nvar = output_size()
        
        
        Defined at suews_ctrl_driver.fpp lines 9007-9076
        
        
        Returns
        -------
        nvar : int
        
        """
        nvar = _supy_driver.f90wrap_output_size()
        return nvar
    
    @staticmethod
    def suews_cal_multitsteps(metforcingblock, len_sim, ah_min, ahprof_24hr, \
        ah_slope_cooling, ah_slope_heating, alb, albmax_dectr, albmax_evetr, \
        albmax_grass, albmin_dectr, albmin_evetr, albmin_grass, alpha_bioco2, \
        alpha_enh_bioco2, alt, baset, basete, beta_bioco2, beta_enh_bioco2, bldgh, \
        capmax_dec, capmin_dec, chanohm, co2pointsource, cpanohm, crwmax, crwmin, \
        daywat, daywatper, dectreeh, diagmethod, diagnose, drainrt, dt_since_start, \
        dqndt, qn_av, dqnsdt, qn_s_av, ef_umolco2perj, emis, emissionsmethod, \
        enef_v_jkm, enddls, evetreeh, faibldg, faidectree, faievetree, faimethod, \
        faut, fcef_v_kgkm, flowchange, frfossilfuel_heat, frfossilfuel_nonheat, \
        g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, gdd_id, gddfull, gridiv, \
        gsmodel, h_maintain, hdd_id, humactivity_24hr, icefrac, ie_a, ie_end, ie_m, \
        ie_start, internalwateruse_h, irrfracpaved, irrfracbldgs, irrfracevetr, \
        irrfracdectr, irrfracgrass, irrfracbsoil, irrfracwater, kkanohm, kmax, \
        lai_id, laimax, laimin, laipower, laitype, lat, lng, maxconductance, \
        maxfcmetab, maxqfmetab, snowwater, minfcmetab, minqfmetab, min_res_bioco2, \
        narp_emis_snow, narp_trans_site, netradiationmethod, ohm_coef, ohmincqf, \
        ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, popdensnighttime, \
        popprof_24hr, pormax_dec, pormin_dec, preciplimit, preciplimitalb, qf0_beu, \
        qf_a, qf_b, qf_c, nlayer, n_vegetation_region_urban, n_stream_sw_urban, \
        n_stream_lw_urban, sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, \
        air_ext_lw, air_ssa_lw, veg_ssa_lw, veg_fsd_const, \
        veg_contact_fraction_const, ground_albedo_dir_mult_fact, \
        use_sw_direct_albedo, height, building_frac, veg_frac, building_scale, \
        veg_scale, alb_roof, emis_roof, alb_wall, emis_wall, \
        roof_albedo_dir_mult_fact, wall_specular_frac, radmeltfact, raincover, \
        rainmaxres, resp_a, resp_b, roughlenheatmethod, roughlenmommethod, \
        runofftowater, s1, s2, sathydraulicconduct, sddfull, sdd_id, smdmethod, \
        snowalb, snowalbmax, snowalbmin, snowpacklimit, snowdens, snowdensmax, \
        snowdensmin, snowfallcum, snowfrac, snowlimbldg, snowlimpaved, snowpack, \
        snowprof_24hr, snowuse, soildepth, stabilitymethod, startdls, \
        soilstore_surf, soilstorecap_surf, state_surf, statelimit_surf, \
        wetthresh_surf, soilstore_roof, soilstorecap_roof, state_roof, \
        statelimit_roof, wetthresh_roof, soilstore_wall, soilstorecap_wall, \
        state_wall, statelimit_wall, wetthresh_wall, storageheatmethod, \
        storedrainprm, surfacearea, tair_av, tau_a, tau_f, tau_r, baset_cooling, \
        baset_heating, tempmeltfact, th, theta_bioco2, timezone, tl, trafficrate, \
        trafficunits, sfr_surf, tsfc_roof, tsfc_wall, tsfc_surf, temp_roof, \
        temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, k_wall, k_roof, k_surf, \
        cp_wall, cp_roof, cp_surf, dz_wall, dz_roof, dz_surf, tmin_id, tmax_id, \
        lenday_id, traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, \
        waterdist, waterusemethod, wuday_id, decidcap_id, albdectr_id, albevetr_id, \
        albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, z, z0m_in, zdm_in):
        """
        output_block_suews = suews_cal_multitsteps(metforcingblock, len_sim, ah_min, \
            ahprof_24hr, ah_slope_cooling, ah_slope_heating, alb, albmax_dectr, \
            albmax_evetr, albmax_grass, albmin_dectr, albmin_evetr, albmin_grass, \
            alpha_bioco2, alpha_enh_bioco2, alt, baset, basete, beta_bioco2, \
            beta_enh_bioco2, bldgh, capmax_dec, capmin_dec, chanohm, co2pointsource, \
            cpanohm, crwmax, crwmin, daywat, daywatper, dectreeh, diagmethod, diagnose, \
            drainrt, dt_since_start, dqndt, qn_av, dqnsdt, qn_s_av, ef_umolco2perj, \
            emis, emissionsmethod, enef_v_jkm, enddls, evetreeh, faibldg, faidectree, \
            faievetree, faimethod, faut, fcef_v_kgkm, flowchange, frfossilfuel_heat, \
            frfossilfuel_nonheat, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, gdd_id, \
            gddfull, gridiv, gsmodel, h_maintain, hdd_id, humactivity_24hr, icefrac, \
            ie_a, ie_end, ie_m, ie_start, internalwateruse_h, irrfracpaved, \
            irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, \
            irrfracwater, kkanohm, kmax, lai_id, laimax, laimin, laipower, laitype, lat, \
            lng, maxconductance, maxfcmetab, maxqfmetab, snowwater, minfcmetab, \
            minqfmetab, min_res_bioco2, narp_emis_snow, narp_trans_site, \
            netradiationmethod, ohm_coef, ohmincqf, ohm_threshsw, ohm_threshwd, \
            pipecapacity, popdensdaytime, popdensnighttime, popprof_24hr, pormax_dec, \
            pormin_dec, preciplimit, preciplimitalb, qf0_beu, qf_a, qf_b, qf_c, nlayer, \
            n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
            emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, radmeltfact, \
            raincover, rainmaxres, resp_a, resp_b, roughlenheatmethod, \
            roughlenmommethod, runofftowater, s1, s2, sathydraulicconduct, sddfull, \
            sdd_id, smdmethod, snowalb, snowalbmax, snowalbmin, snowpacklimit, snowdens, \
            snowdensmax, snowdensmin, snowfallcum, snowfrac, snowlimbldg, snowlimpaved, \
            snowpack, snowprof_24hr, snowuse, soildepth, stabilitymethod, startdls, \
            soilstore_surf, soilstorecap_surf, state_surf, statelimit_surf, \
            wetthresh_surf, soilstore_roof, soilstorecap_roof, state_roof, \
            statelimit_roof, wetthresh_roof, soilstore_wall, soilstorecap_wall, \
            state_wall, statelimit_wall, wetthresh_wall, storageheatmethod, \
            storedrainprm, surfacearea, tair_av, tau_a, tau_f, tau_r, baset_cooling, \
            baset_heating, tempmeltfact, th, theta_bioco2, timezone, tl, trafficrate, \
            trafficunits, sfr_surf, tsfc_roof, tsfc_wall, tsfc_surf, temp_roof, \
            temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, k_wall, k_roof, k_surf, \
            cp_wall, cp_roof, cp_surf, dz_wall, dz_roof, dz_surf, tmin_id, tmax_id, \
            lenday_id, traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, \
            waterdist, waterusemethod, wuday_id, decidcap_id, albdectr_id, albevetr_id, \
            albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, z, z0m_in, zdm_in)
        
        
        Defined at suews_ctrl_driver.fpp lines 9078-9806
        
        Parameters
        ----------
        metforcingblock : float array
        len_sim : int
        ah_min : float array
        ahprof_24hr : float array
        ah_slope_cooling : float array
        ah_slope_heating : float array
        alb : float array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        alpha_bioco2 : float array
        alpha_enh_bioco2 : float array
        alt : float
        baset : float array
        basete : float array
        beta_bioco2 : float array
        beta_enh_bioco2 : float array
        bldgh : float
        capmax_dec : float
        capmin_dec : float
        chanohm : float array
        co2pointsource : float
        cpanohm : float array
        crwmax : float
        crwmin : float
        daywat : float array
        daywatper : float array
        dectreeh : float
        diagmethod : int
        diagnose : int
        drainrt : float
        dt_since_start : int
        dqndt : float
        qn_av : float
        dqnsdt : float
        qn_s_av : float
        ef_umolco2perj : float
        emis : float array
        emissionsmethod : int
        enef_v_jkm : float
        enddls : int
        evetreeh : float
        faibldg : float
        faidectree : float
        faievetree : float
        faimethod : int
        faut : float
        fcef_v_kgkm : float array
        flowchange : float
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        gdd_id : float array
        gddfull : float array
        gridiv : int
        gsmodel : int
        h_maintain : float
        hdd_id : float array
        humactivity_24hr : float array
        icefrac : float array
        ie_a : float array
        ie_end : int
        ie_m : float array
        ie_start : int
        internalwateruse_h : float
        irrfracpaved : float
        irrfracbldgs : float
        irrfracevetr : float
        irrfracdectr : float
        irrfracgrass : float
        irrfracbsoil : float
        irrfracwater : float
        kkanohm : float array
        kmax : float
        lai_id : float array
        laimax : float array
        laimin : float array
        laipower : float array
        laitype : int array
        lat : float
        lng : float
        maxconductance : float array
        maxfcmetab : float
        maxqfmetab : float
        snowwater : float array
        minfcmetab : float
        minqfmetab : float
        min_res_bioco2 : float array
        narp_emis_snow : float
        narp_trans_site : float
        netradiationmethod : int
        ohm_coef : float array
        ohmincqf : int
        ohm_threshsw : float array
        ohm_threshwd : float array
        pipecapacity : float
        popdensdaytime : float array
        popdensnighttime : float
        popprof_24hr : float array
        pormax_dec : float
        pormin_dec : float
        preciplimit : float
        preciplimitalb : float
        qf0_beu : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        nlayer : int
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        radmeltfact : float
        raincover : float
        rainmaxres : float
        resp_a : float array
        resp_b : float array
        roughlenheatmethod : int
        roughlenmommethod : int
        runofftowater : float
        s1 : float
        s2 : float
        sathydraulicconduct : float array
        sddfull : float array
        sdd_id : float array
        smdmethod : int
        snowalb : float
        snowalbmax : float
        snowalbmin : float
        snowpacklimit : float array
        snowdens : float array
        snowdensmax : float
        snowdensmin : float
        snowfallcum : float
        snowfrac : float array
        snowlimbldg : float
        snowlimpaved : float
        snowpack : float array
        snowprof_24hr : float array
        snowuse : int
        soildepth : float array
        stabilitymethod : int
        startdls : int
        soilstore_surf : float array
        soilstorecap_surf : float array
        state_surf : float array
        statelimit_surf : float array
        wetthresh_surf : float array
        soilstore_roof : float array
        soilstorecap_roof : float array
        state_roof : float array
        statelimit_roof : float array
        wetthresh_roof : float array
        soilstore_wall : float array
        soilstorecap_wall : float array
        state_wall : float array
        statelimit_wall : float array
        wetthresh_wall : float array
        storageheatmethod : int
        storedrainprm : float array
        surfacearea : float
        tair_av : float
        tau_a : float
        tau_f : float
        tau_r : float
        baset_cooling : float array
        baset_heating : float array
        tempmeltfact : float
        th : float
        theta_bioco2 : float array
        timezone : float
        tl : float
        trafficrate : float array
        trafficunits : float
        sfr_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        tsfc_surf : float array
        temp_roof : float array
        temp_wall : float array
        temp_surf : float array
        tin_roof : float array
        tin_wall : float array
        tin_surf : float array
        k_wall : float array
        k_roof : float array
        k_surf : float array
        cp_wall : float array
        cp_roof : float array
        cp_surf : float array
        dz_wall : float array
        dz_roof : float array
        dz_surf : float array
        tmin_id : float
        tmax_id : float
        lenday_id : float
        traffprof_24hr : float array
        ts5mindata_ir : float array
        tstep : int
        tstep_prev : int
        veg_type : int
        waterdist : float array
        waterusemethod : int
        wuday_id : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        wuprofa_24hr : float array
        wuprofm_24hr : float array
        z : float
        z0m_in : float
        zdm_in : float
        
        Returns
        -------
        output_block_suews : Output_Block
        
        ================================================
         below is for debugging
         WRITE(year_txt, '(I4)') INT(iy)
         WRITE(id_text, '(I3)') INT(id)
         WRITE(it_text, '(I4)') INT(it)
         WRITE(imin_text, '(I4)') INT(imin)
         FileStateInit = './'//TRIM(ADJUSTL(year_txt))//'_'&
         //TRIM(ADJUSTL(id_text))//'_'&
         //TRIM(ADJUSTL(it_text))//'_'&
         //TRIM(ADJUSTL(imin_text))//'_'&
         //'state_init.nml'
         OPEN(12, file=FileStateInit, position='rewind')
         write(12, *) '&state_init'
         write(12, *) 'aerodynamicresistancemethod=', aerodynamicresistancemethod
         write(12, *) 'ah_min=', ah_min
         write(12, *) 'ahprof_24hr=', ahprof_24hr
         write(12, *) 'ah_slope_cooling=', ah_slope_cooling
         write(12, *) 'ah_slope_heating=', ah_slope_heating
         write(12, *) 'alb=', alb
         write(12, *) 'albmax_dectr=', albmax_dectr
         write(12, *) 'albmax_evetr=', albmax_evetr
         write(12, *) 'albmax_grass=', albmax_grass
         write(12, *) 'albmin_dectr=', albmin_dectr
         write(12, *) 'albmin_evetr=', albmin_evetr
         write(12, *) 'albmin_grass=', albmin_grass
         write(12, *) 'alpha_bioco2=', alpha_bioco2
         write(12, *) 'alpha_enh_bioco2=', alpha_enh_bioco2
         write(12, *) 'alt=', alt
         write(12, *) 'avkdn=', avkdn
         write(12, *) 'avrh=', avrh
         write(12, *) 'avu1=', avu1
         write(12, *) 'baset=', baset
         write(12, *) 'basete=', basete
         write(12, *) 'BaseT_HC=', BaseT_HC
         write(12, *) 'beta_bioco2=', beta_bioco2
         write(12, *) 'beta_enh_bioco2=', beta_enh_bioco2
         write(12, *) 'bldgh=', bldgh
         write(12, *) 'capmax_dec=', capmax_dec
         write(12, *) 'capmin_dec=', capmin_dec
         write(12, *) 'chanohm=', chanohm
         write(12, *) 'co2pointsource=', co2pointsource
         write(12, *) 'cpanohm=', cpanohm
         write(12, *) 'crwmax=', crwmax
         write(12, *) 'crwmin=', crwmin
         write(12, *) 'daywat=', daywat
         write(12, *) 'daywatper=', daywatper
         write(12, *) 'dectreeh=', dectreeh
         write(12, *) 'diagnose=', diagnose
         write(12, *) 'diagqn=', diagqn
         write(12, *) 'diagqs=', diagqs
         write(12, *) 'drainrt=', drainrt
         write(12, *) 'dt_since_start=', dt_since_start
         write(12, *) 'dqndt=', dqndt
         write(12, *) 'qn_av=', qn_av
         write(12, *) 'dqnsdt=', dqnsdt
         write(12, *) 'qn1_s_av=', qn1_s_av
         write(12, *) 'ef_umolco2perj=', ef_umolco2perj
         write(12, *) 'emis=', emis
         write(12, *) 'emissionsmethod=', emissionsmethod
         write(12, *) 'enef_v_jkm=', enef_v_jkm
         write(12, *) 'enddls=', enddls
         write(12, *) 'evetreeh=', evetreeh
         write(12, *) 'faibldg=', faibldg
         write(12, *) 'faidectree=', faidectree
         write(12, *) 'faievetree=', faievetree
         write(12, *) 'faut=', faut
         write(12, *) 'fcef_v_kgkm=', fcef_v_kgkm
         write(12, *) 'fcld_obs=', fcld_obs
         write(12, *) 'flowchange=', flowchange
         write(12, *) 'frfossilfuel_heat=', frfossilfuel_heat
         write(12, *) 'frfossilfuel_nonheat=', frfossilfuel_nonheat
         write(12, *) 'g1=', g1
         write(12, *) 'g2=', g2
         write(12, *) 'g3=', g3
         write(12, *) 'g4=', g4
         write(12, *) 'g5=', g5
         write(12, *) 'g6=', g6
         write(12, *) 'gdd_id=', gdd_id
         write(12, *) 'gddfull=', gddfull
         write(12, *) 'gridiv=', gridiv
         write(12, *) 'gsmodel=', gsmodel
         write(12, *) 'hdd_id=', hdd_id
         write(12, *) 'humactivity_24hr=', humactivity_24hr
         write(12, *) 'icefrac=', icefrac
         write(12, *) 'id=', id
         write(12, *) 'ie_a=', ie_a
         write(12, *) 'ie_end=', ie_end
         write(12, *) 'ie_m=', ie_m
         write(12, *) 'ie_start=', ie_start
         write(12, *) 'imin=', imin
         write(12, *) 'internalwateruse_h=', internalwateruse_h
         write(12, *) 'IrrFracEveTr=', IrrFracEveTr
         write(12, *) 'IrrFracDecTr=', IrrFracDecTr
         write(12, *) 'irrfracgrass=', irrfracgrass
         write(12, *) 'isec=', isec
         write(12, *) 'it=', it
         write(12, *) 'evapmethod=', evapmethod
         write(12, *) 'iy=', iy
         write(12, *) 'kkanohm=', kkanohm
         write(12, *) 'kmax=', kmax
         write(12, *) 'lai_id=', lai_id
         write(12, *) 'laicalcyes=', laicalcyes
         write(12, *) 'laimax=', laimax
         write(12, *) 'laimin=', laimin
         write(12, *) 'lai_obs=', lai_obs
         write(12, *) 'laipower=', laipower
         write(12, *) 'laitype=', laitype
         write(12, *) 'lat=', lat
         write(12, *) 'lenday_id=', lenday_id
         write(12, *) 'ldown_obs=', ldown_obs
         write(12, *) 'lng=', lng
         write(12, *) 'maxconductance=', maxconductance
         write(12, *) 'maxfcmetab=', maxfcmetab
         write(12, *) 'maxqfmetab=', maxqfmetab
         write(12, *) 'snowwater=', snowwater
         write(12, *) 'metforcingdata_grid=', metforcingdata_grid
         write(12, *) 'minfcmetab=', minfcmetab
         write(12, *) 'minqfmetab=', minqfmetab
         write(12, *) 'min_res_bioco2=', min_res_bioco2
         write(12, *) 'narp_emis_snow=', narp_emis_snow
         write(12, *) 'narp_trans_site=', narp_trans_site
         write(12, *) 'netradiationmethod=', netradiationmethod
         write(12, *) 'ohm_coef=', ohm_coef
         write(12, *) 'ohmincqf=', ohmincqf
         write(12, *) 'ohm_threshsw=', ohm_threshsw
         write(12, *) 'ohm_threshwd=', ohm_threshwd
         write(12, *) 'pipecapacity=', pipecapacity
         write(12, *) 'popdensdaytime=', popdensdaytime
         write(12, *) 'popdensnighttime=', popdensnighttime
         write(12, *) 'popprof_24hr=', popprof_24hr
         write(12, *) 'pormax_dec=', pormax_dec
         write(12, *) 'pormin_dec=', pormin_dec
         write(12, *) 'precip=', precip
         write(12, *) 'preciplimit=', preciplimit
         write(12, *) 'preciplimitalb=', preciplimitalb
         write(12, *) 'press_hpa=', press_hpa
         write(12, *) 'qf0_beu=', qf0_beu
         write(12, *) 'qf_a=', qf_a
         write(12, *) 'qf_b=', qf_b
         write(12, *) 'qf_c=', qf_c
         write(12, *) 'qn1_obs=', qn1_obs
         write(12, *) 'qh_obs=', qh_obs
         write(12, *) 'qs_obs=', qs_obs
         write(12, *) 'qf_obs=', qf_obs
         write(12, *) 'radmeltfact=', radmeltfact
         write(12, *) 'raincover=', raincover
         write(12, *) 'rainmaxres=', rainmaxres
         write(12, *) 'resp_a=', resp_a
         write(12, *) 'resp_b=', resp_b
         write(12, *) 'roughlenheatmethod=', roughlenheatmethod
         write(12, *) 'roughlenmommethod=', roughlenmommethod
         write(12, *) 'runofftowater=', runofftowater
         write(12, *) 's1=', s1
         write(12, *) 's2=', s2
         write(12, *) 'sathydraulicconduct=', sathydraulicconduct
         write(12, *) 'sddfull=', sddfull
         write(12, *) 'sdd_id=', sdd_id
         write(12, *) 'sfr_surf=', sfr_surf
         write(12, *) 'smdmethod=', smdmethod
         write(12, *) 'snowalb=', snowalb
         write(12, *) 'snowalbmax=', snowalbmax
         write(12, *) 'snowalbmin=', snowalbmin
         write(12, *) 'snowpacklimit=', snowpacklimit
         write(12, *) 'snowdens=', snowdens
         write(12, *) 'snowdensmax=', snowdensmax
         write(12, *) 'snowdensmin=', snowdensmin
         write(12, *) 'snowfallcum=', snowfallcum
         write(12, *) 'snowfrac=', snowfrac
         write(12, *) 'snowlimbldg=', snowlimbldg
         write(12, *) 'snowlimpaved=', snowlimpaved
         write(12, *) 'snowfrac_obs=', snowfrac_obs
         write(12, *) 'snowpack=', snowpack
         write(12, *) 'snowprof_24hr=', snowprof_24hr
         write(12, *) 'SnowUse=', SnowUse
         write(12, *) 'soildepth=', soildepth
         write(12, *) 'soilstore_id=', soilstore_id
         write(12, *) 'soilstorecap=', soilstorecap
         write(12, *) 'stabilitymethod=', stabilitymethod
         write(12, *) 'startdls=', startdls
         write(12, *) 'state_id=', state_id
         write(12, *) 'statelimit=', statelimit
         write(12, *) 'storageheatmethod=', storageheatmethod
         write(12, *) 'storedrainprm=', storedrainprm
         write(12, *) 'surfacearea=', surfacearea
         write(12, *) 'tair_av=', tair_av
         write(12, *) 'tau_a=', tau_a
         write(12, *) 'tau_f=', tau_f
         write(12, *) 'tau_r=', tau_r
         write(12, *) 'tmax_id=', tmax_id
         write(12, *) 'tmin_id=', tmin_id
         write(12, *) 'BaseT_Cooling=', BaseT_Cooling
         write(12, *) 'BaseT_Heating=', BaseT_Heating
         write(12, *) 'temp_c=', temp_c
         write(12, *) 'tempmeltfact=', tempmeltfact
         write(12, *) 'th=', th
         write(12, *) 'theta_bioco2=', theta_bioco2
         write(12, *) 'timezone=', timezone
         write(12, *) 'tl=', tl
         write(12, *) 'trafficrate=', trafficrate
         write(12, *) 'trafficunits=', trafficunits
         write(12, *) 'traffprof_24hr=', traffprof_24hr
         write(12, *) 'ts5mindata_ir=', ts5mindata_ir
         write(12, *) 'tstep=', tstep
         write(12, *) 'tstep_prev=', tstep_prev
         write(12, *) 'veg_type=', veg_type
         write(12, *) 'waterdist=', waterdist
         write(12, *) 'waterusemethod=', waterusemethod
         write(12, *) 'wetthresh=', wetthresh
         write(12, *) 'wu_m3=', wu_m3
         write(12, *) 'wuday_id=', wuday_id
         write(12, *) 'decidcap_id=', decidcap_id
         write(12, *) 'albdectr_id=', albdectr_id
         write(12, *) 'albevetr_id=', albevetr_id
         write(12, *) 'albgrass_id=', albgrass_id
         write(12, *) 'porosity_id=', porosity_id
         write(12, *) 'wuprofa_24hr=', wuprofa_24hr
         write(12, *) 'wuprofm_24hr=', wuprofm_24hr
         write(12, *) 'xsmd=', xsmd
         write(12, *) 'z=', z
         write(12, *) 'z0m_in=', z0m_in
         write(12, *) 'zdm_in=', zdm_in
         write(12, *) '/'
         WRITE(12, *) ''
         CLOSE(12)
        ================================================
         CALL SUEWS_cal_Main( &
        """
        output_block_suews = \
            _supy_driver.f90wrap_suews_cal_multitsteps(metforcingblock=metforcingblock, \
            len_sim=len_sim, ah_min=ah_min, ahprof_24hr=ahprof_24hr, \
            ah_slope_cooling=ah_slope_cooling, ah_slope_heating=ah_slope_heating, \
            alb=alb, albmax_dectr=albmax_dectr, albmax_evetr=albmax_evetr, \
            albmax_grass=albmax_grass, albmin_dectr=albmin_dectr, \
            albmin_evetr=albmin_evetr, albmin_grass=albmin_grass, \
            alpha_bioco2=alpha_bioco2, alpha_enh_bioco2=alpha_enh_bioco2, alt=alt, \
            baset=baset, basete=basete, beta_bioco2=beta_bioco2, \
            beta_enh_bioco2=beta_enh_bioco2, bldgh=bldgh, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, chanohm=chanohm, co2pointsource=co2pointsource, \
            cpanohm=cpanohm, crwmax=crwmax, crwmin=crwmin, daywat=daywat, \
            daywatper=daywatper, dectreeh=dectreeh, diagmethod=diagmethod, \
            diagnose=diagnose, drainrt=drainrt, dt_since_start=dt_since_start, \
            dqndt=dqndt, qn_av=qn_av, dqnsdt=dqnsdt, qn_s_av=qn_s_av, \
            ef_umolco2perj=ef_umolco2perj, emis=emis, emissionsmethod=emissionsmethod, \
            enef_v_jkm=enef_v_jkm, enddls=enddls, evetreeh=evetreeh, faibldg=faibldg, \
            faidectree=faidectree, faievetree=faievetree, faimethod=faimethod, \
            faut=faut, fcef_v_kgkm=fcef_v_kgkm, flowchange=flowchange, \
            frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, gdd_id=gdd_id, \
            gddfull=gddfull, gridiv=gridiv, gsmodel=gsmodel, h_maintain=h_maintain, \
            hdd_id=hdd_id, humactivity_24hr=humactivity_24hr, icefrac=icefrac, \
            ie_a=ie_a, ie_end=ie_end, ie_m=ie_m, ie_start=ie_start, \
            internalwateruse_h=internalwateruse_h, irrfracpaved=irrfracpaved, \
            irrfracbldgs=irrfracbldgs, irrfracevetr=irrfracevetr, \
            irrfracdectr=irrfracdectr, irrfracgrass=irrfracgrass, \
            irrfracbsoil=irrfracbsoil, irrfracwater=irrfracwater, kkanohm=kkanohm, \
            kmax=kmax, lai_id=lai_id, laimax=laimax, laimin=laimin, laipower=laipower, \
            laitype=laitype, lat=lat, lng=lng, maxconductance=maxconductance, \
            maxfcmetab=maxfcmetab, maxqfmetab=maxqfmetab, snowwater=snowwater, \
            minfcmetab=minfcmetab, minqfmetab=minqfmetab, min_res_bioco2=min_res_bioco2, \
            narp_emis_snow=narp_emis_snow, narp_trans_site=narp_trans_site, \
            netradiationmethod=netradiationmethod, ohm_coef=ohm_coef, ohmincqf=ohmincqf, \
            ohm_threshsw=ohm_threshsw, ohm_threshwd=ohm_threshwd, \
            pipecapacity=pipecapacity, popdensdaytime=popdensdaytime, \
            popdensnighttime=popdensnighttime, popprof_24hr=popprof_24hr, \
            pormax_dec=pormax_dec, pormin_dec=pormin_dec, preciplimit=preciplimit, \
            preciplimitalb=preciplimitalb, qf0_beu=qf0_beu, qf_a=qf_a, qf_b=qf_b, \
            qf_c=qf_c, nlayer=nlayer, \
            n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, \
            building_scale=building_scale, veg_scale=veg_scale, alb_roof=alb_roof, \
            emis_roof=emis_roof, alb_wall=alb_wall, emis_wall=emis_wall, \
            roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, radmeltfact=radmeltfact, \
            raincover=raincover, rainmaxres=rainmaxres, resp_a=resp_a, resp_b=resp_b, \
            roughlenheatmethod=roughlenheatmethod, roughlenmommethod=roughlenmommethod, \
            runofftowater=runofftowater, s1=s1, s2=s2, \
            sathydraulicconduct=sathydraulicconduct, sddfull=sddfull, sdd_id=sdd_id, \
            smdmethod=smdmethod, snowalb=snowalb, snowalbmax=snowalbmax, \
            snowalbmin=snowalbmin, snowpacklimit=snowpacklimit, snowdens=snowdens, \
            snowdensmax=snowdensmax, snowdensmin=snowdensmin, snowfallcum=snowfallcum, \
            snowfrac=snowfrac, snowlimbldg=snowlimbldg, snowlimpaved=snowlimpaved, \
            snowpack=snowpack, snowprof_24hr=snowprof_24hr, snowuse=snowuse, \
            soildepth=soildepth, stabilitymethod=stabilitymethod, startdls=startdls, \
            soilstore_surf=soilstore_surf, soilstorecap_surf=soilstorecap_surf, \
            state_surf=state_surf, statelimit_surf=statelimit_surf, \
            wetthresh_surf=wetthresh_surf, soilstore_roof=soilstore_roof, \
            soilstorecap_roof=soilstorecap_roof, state_roof=state_roof, \
            statelimit_roof=statelimit_roof, wetthresh_roof=wetthresh_roof, \
            soilstore_wall=soilstore_wall, soilstorecap_wall=soilstorecap_wall, \
            state_wall=state_wall, statelimit_wall=statelimit_wall, \
            wetthresh_wall=wetthresh_wall, storageheatmethod=storageheatmethod, \
            storedrainprm=storedrainprm, surfacearea=surfacearea, tair_av=tair_av, \
            tau_a=tau_a, tau_f=tau_f, tau_r=tau_r, baset_cooling=baset_cooling, \
            baset_heating=baset_heating, tempmeltfact=tempmeltfact, th=th, \
            theta_bioco2=theta_bioco2, timezone=timezone, tl=tl, \
            trafficrate=trafficrate, trafficunits=trafficunits, sfr_surf=sfr_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, tsfc_surf=tsfc_surf, \
            temp_roof=temp_roof, temp_wall=temp_wall, temp_surf=temp_surf, \
            tin_roof=tin_roof, tin_wall=tin_wall, tin_surf=tin_surf, k_wall=k_wall, \
            k_roof=k_roof, k_surf=k_surf, cp_wall=cp_wall, cp_roof=cp_roof, \
            cp_surf=cp_surf, dz_wall=dz_wall, dz_roof=dz_roof, dz_surf=dz_surf, \
            tmin_id=tmin_id, tmax_id=tmax_id, lenday_id=lenday_id, \
            traffprof_24hr=traffprof_24hr, ts5mindata_ir=ts5mindata_ir, tstep=tstep, \
            tstep_prev=tstep_prev, veg_type=veg_type, waterdist=waterdist, \
            waterusemethod=waterusemethod, wuday_id=wuday_id, decidcap_id=decidcap_id, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            porosity_id=porosity_id, wuprofa_24hr=wuprofa_24hr, \
            wuprofm_24hr=wuprofm_24hr, z=z, z0m_in=z0m_in, zdm_in=zdm_in)
        output_block_suews = \
            f90wrap.runtime.lookup_class("supy_driver.output_block").from_handle(output_block_suews, \
            alloc=True)
        return output_block_suews
    
    @staticmethod
    def suews_cal_sunposition(year, idectime, utc, locationlatitude, \
        locationlongitude, locationaltitude):
        """
        sunazimuth, sunzenith = suews_cal_sunposition(year, idectime, utc, \
            locationlatitude, locationlongitude, locationaltitude)
        
        
        Defined at suews_ctrl_driver.fpp lines 9811-9818
        
        Parameters
        ----------
        year : float
        idectime : float
        utc : float
        locationlatitude : float
        locationlongitude : float
        locationaltitude : float
        
        Returns
        -------
        sunazimuth : float
        sunzenith : float
        
        """
        sunazimuth, sunzenith = _supy_driver.f90wrap_suews_cal_sunposition(year=year, \
            idectime=idectime, utc=utc, locationlatitude=locationlatitude, \
            locationlongitude=locationlongitude, locationaltitude=locationaltitude)
        return sunazimuth, sunzenith
    
    @staticmethod
    def cal_tair_av(tair_av_prev, dt_since_start, tstep, temp_c):
        """
        tair_av_next = cal_tair_av(tair_av_prev, dt_since_start, tstep, temp_c)
        
        
        Defined at suews_ctrl_driver.fpp lines 9825-9846
        
        Parameters
        ----------
        tair_av_prev : float
        dt_since_start : int
        tstep : int
        temp_c : float
        
        Returns
        -------
        tair_av_next : float
        
        """
        tair_av_next = _supy_driver.f90wrap_cal_tair_av(tair_av_prev=tair_av_prev, \
            dt_since_start=dt_since_start, tstep=tstep, temp_c=temp_c)
        return tair_av_next
    
    @staticmethod
    def cal_tsfc(qh, avdens, avcp, ra, temp_c):
        """
        tsfc_c = cal_tsfc(qh, avdens, avcp, ra, temp_c)
        
        
        Defined at suews_ctrl_driver.fpp lines 9848-9858
        
        Parameters
        ----------
        qh : float
        avdens : float
        avcp : float
        ra : float
        temp_c : float
        
        Returns
        -------
        tsfc_c : float
        
        """
        tsfc_c = _supy_driver.f90wrap_cal_tsfc(qh=qh, avdens=avdens, avcp=avcp, ra=ra, \
            temp_c=temp_c)
        return tsfc_c
    
    _dt_array_initialisers = []
    

suews_driver = Suews_Driver()

class Narp_Module(f90wrap.runtime.FortranModule):
    """
    Module narp_module
    
    
    Defined at suews_phys_narp.fpp lines 5-1269
    
    """
    @staticmethod
    def radmethod(netradiationmethod, snowuse):
        """
        netradiationmethod_use, albedochoice, ldown_option = \
            radmethod(netradiationmethod, snowuse)
        
        
        Defined at suews_phys_narp.fpp lines 47-109
        
        Parameters
        ----------
        netradiationmethod : int
        snowuse : int
        
        Returns
        -------
        netradiationmethod_use : int
        albedochoice : int
        ldown_option : int
        
        """
        netradiationmethod_use, albedochoice, ldown_option = \
            _supy_driver.f90wrap_radmethod(netradiationmethod=netradiationmethod, \
            snowuse=snowuse)
        return netradiationmethod_use, albedochoice, ldown_option
    
    @staticmethod
    def narp(storageheatmethod, nsurf, sfr_surf, tsfc_surf, snowfrac, alb, emis, \
        icefrac, narp_trans_site, narp_emis_snow, dtime, zenith_deg, tsurf_0, kdown, \
        temp_c, rh, press_hpa, qn1_obs, ldown_obs, snowalb, albedochoice, \
        ldown_option, netradiationmethod_use, diagqn, qn_surf, qn1_ind_snow, \
        kup_ind_snow, tsurf_ind_snow, tsurf_surf):
        """
        qstarall, qstar_sf, qstar_s, kclear, kupall, ldown, lupall, fcld, tsurfall, \
            albedo_snowfree, albedo_snow = narp(storageheatmethod, nsurf, sfr_surf, \
            tsfc_surf, snowfrac, alb, emis, icefrac, narp_trans_site, narp_emis_snow, \
            dtime, zenith_deg, tsurf_0, kdown, temp_c, rh, press_hpa, qn1_obs, \
            ldown_obs, snowalb, albedochoice, ldown_option, netradiationmethod_use, \
            diagqn, qn_surf, qn1_ind_snow, kup_ind_snow, tsurf_ind_snow, tsurf_surf)
        
        
        Defined at suews_phys_narp.fpp lines 123-459
        
        Parameters
        ----------
        storageheatmethod : int
        nsurf : int
        sfr_surf : float array
        tsfc_surf : float array
        snowfrac : float array
        alb : float array
        emis : float array
        icefrac : float array
        narp_trans_site : float
        narp_emis_snow : float
        dtime : float
        zenith_deg : float
        tsurf_0 : float
        kdown : float
        temp_c : float
        rh : float
        press_hpa : float
        qn1_obs : float
        ldown_obs : float
        snowalb : float
        albedochoice : int
        ldown_option : int
        netradiationmethod_use : int
        diagqn : int
        qn_surf : float array
        qn1_ind_snow : float array
        kup_ind_snow : float array
        tsurf_ind_snow : float array
        tsurf_surf : float array
        
        Returns
        -------
        qstarall : float
        qstar_sf : float
        qstar_s : float
        kclear : float
        kupall : float
        ldown : float
        lupall : float
        fcld : float
        tsurfall : float
        albedo_snowfree : float
        albedo_snow : float
        
        -------------------------------------------------------------------------------
         USE allocateArray
         use gis_data
         use data_in
         Included 20140701, FL
         use moist
         Included 20140701, FL
         use time
         Included 20140701, FL
        """
        qstarall, qstar_sf, qstar_s, kclear, kupall, ldown, lupall, fcld, tsurfall, \
            albedo_snowfree, albedo_snow = \
            _supy_driver.f90wrap_narp(storageheatmethod=storageheatmethod, nsurf=nsurf, \
            sfr_surf=sfr_surf, tsfc_surf=tsfc_surf, snowfrac=snowfrac, alb=alb, \
            emis=emis, icefrac=icefrac, narp_trans_site=narp_trans_site, \
            narp_emis_snow=narp_emis_snow, dtime=dtime, zenith_deg=zenith_deg, \
            tsurf_0=tsurf_0, kdown=kdown, temp_c=temp_c, rh=rh, press_hpa=press_hpa, \
            qn1_obs=qn1_obs, ldown_obs=ldown_obs, snowalb=snowalb, \
            albedochoice=albedochoice, ldown_option=ldown_option, \
            netradiationmethod_use=netradiationmethod_use, diagqn=diagqn, \
            qn_surf=qn_surf, qn1_ind_snow=qn1_ind_snow, kup_ind_snow=kup_ind_snow, \
            tsurf_ind_snow=tsurf_ind_snow, tsurf_surf=tsurf_surf)
        return qstarall, qstar_sf, qstar_s, kclear, kupall, ldown, lupall, fcld, \
            tsurfall, albedo_snowfree, albedo_snow
    
    @staticmethod
    def narp_cal_sunposition(year, idectime, utc, locationlatitude, \
        locationlongitude, locationaltitude):
        """
        sunazimuth, sunzenith = narp_cal_sunposition(year, idectime, utc, \
            locationlatitude, locationlongitude, locationaltitude)
        
        
        Defined at suews_phys_narp.fpp lines 464-547
        
        Parameters
        ----------
        year : float
        idectime : float
        utc : float
        locationlatitude : float
        locationlongitude : float
        locationaltitude : float
        
        Returns
        -------
        sunazimuth : float
        sunzenith : float
        
        """
        sunazimuth, sunzenith = _supy_driver.f90wrap_narp_cal_sunposition(year=year, \
            idectime=idectime, utc=utc, locationlatitude=locationlatitude, \
            locationlongitude=locationlongitude, locationaltitude=locationaltitude)
        return sunazimuth, sunzenith
    
    @staticmethod
    def julian_calculation(year, month, day, hour, min_bn, sec, utc, juliancentury, \
        julianday, julianephemeris_century, julianephemeris_day, \
        julianephemeris_millenium):
        """
        julian_calculation(year, month, day, hour, min_bn, sec, utc, juliancentury, \
            julianday, julianephemeris_century, julianephemeris_day, \
            julianephemeris_millenium)
        
        
        Defined at suews_phys_narp.fpp lines 551-608
        
        Parameters
        ----------
        year : float
        month : int
        day : int
        hour : int
        min_bn : int
        sec : float
        utc : float
        juliancentury : float
        julianday : float
        julianephemeris_century : float
        julianephemeris_day : float
        julianephemeris_millenium : float
        
        """
        _supy_driver.f90wrap_julian_calculation(year=year, month=month, day=day, \
            hour=hour, min_bn=min_bn, sec=sec, utc=utc, juliancentury=juliancentury, \
            julianday=julianday, julianephemeris_century=julianephemeris_century, \
            julianephemeris_day=julianephemeris_day, \
            julianephemeris_millenium=julianephemeris_millenium)
    
    @staticmethod
    def earth_heliocentric_position_calculation(julianephemeris_millenium, \
        earth_heliocentric_positionlatitude, earth_heliocentric_positionlongitude, \
        earth_heliocentric_positionradius):
        """
        earth_heliocentric_position_calculation(julianephemeris_millenium, \
            earth_heliocentric_positionlatitude, earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionradius)
        
        
        Defined at suews_phys_narp.fpp lines 610-776
        
        Parameters
        ----------
        julianephemeris_millenium : float
        earth_heliocentric_positionlatitude : float
        earth_heliocentric_positionlongitude : float
        earth_heliocentric_positionradius : float
        
        """
        _supy_driver.f90wrap_earth_heliocentric_position_calculation(julianephemeris_millenium=julianephemeris_millenium, \
            earth_heliocentric_positionlatitude=earth_heliocentric_positionlatitude, \
            earth_heliocentric_positionlongitude=earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionradius=earth_heliocentric_positionradius)
    
    @staticmethod
    def sun_geocentric_position_calculation(earth_heliocentric_positionlongitude, \
        earth_heliocentric_positionlatitude, sun_geocentric_positionlatitude, \
        sun_geocentric_positionlongitude):
        """
        sun_geocentric_position_calculation(earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionlatitude, sun_geocentric_positionlatitude, \
            sun_geocentric_positionlongitude)
        
        
        Defined at suews_phys_narp.fpp lines 778-790
        
        Parameters
        ----------
        earth_heliocentric_positionlongitude : float
        earth_heliocentric_positionlatitude : float
        sun_geocentric_positionlatitude : float
        sun_geocentric_positionlongitude : float
        
        """
        _supy_driver.f90wrap_sun_geocentric_position_calculation(earth_heliocentric_positionlongitude=earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionlatitude=earth_heliocentric_positionlatitude, \
            sun_geocentric_positionlatitude=sun_geocentric_positionlatitude, \
            sun_geocentric_positionlongitude=sun_geocentric_positionlongitude)
    
    @staticmethod
    def nutation_calculation(julianephemeris_century, nutationlongitude, \
        nutationobliquity):
        """
        nutation_calculation(julianephemeris_century, nutationlongitude, \
            nutationobliquity)
        
        
        Defined at suews_phys_narp.fpp lines 792-896
        
        Parameters
        ----------
        julianephemeris_century : float
        nutationlongitude : float
        nutationobliquity : float
        
        """
        _supy_driver.f90wrap_nutation_calculation(julianephemeris_century=julianephemeris_century, \
            nutationlongitude=nutationlongitude, nutationobliquity=nutationobliquity)
    
    @staticmethod
    def corr_obliquity_calculation(julianephemeris_millenium, nutationobliquity):
        """
        corr_obliquity = corr_obliquity_calculation(julianephemeris_millenium, \
            nutationobliquity)
        
        
        Defined at suews_phys_narp.fpp lines 898-913
        
        Parameters
        ----------
        julianephemeris_millenium : float
        nutationobliquity : float
        
        Returns
        -------
        corr_obliquity : float
        
        """
        corr_obliquity = \
            _supy_driver.f90wrap_corr_obliquity_calculation(julianephemeris_millenium=julianephemeris_millenium, \
            nutationobliquity=nutationobliquity)
        return corr_obliquity
    
    @staticmethod
    def abberation_correction_calculation(earth_heliocentric_positionradius):
        """
        aberration_correction = \
            abberation_correction_calculation(earth_heliocentric_positionradius)
        
        
        Defined at suews_phys_narp.fpp lines 915-922
        
        Parameters
        ----------
        earth_heliocentric_positionradius : float
        
        Returns
        -------
        aberration_correction : float
        
        """
        aberration_correction = \
            _supy_driver.f90wrap_abberation_correction_calculation(earth_heliocentric_positionradius=earth_heliocentric_positionradius)
        return aberration_correction
    
    @staticmethod
    def apparent_sun_longitude_calculation(sun_geocentric_positionlongitude, \
        nutationlongitude, aberration_correction):
        """
        apparent_sun_longitude = \
            apparent_sun_longitude_calculation(sun_geocentric_positionlongitude, \
            nutationlongitude, aberration_correction)
        
        
        Defined at suews_phys_narp.fpp lines 924-932
        
        Parameters
        ----------
        sun_geocentric_positionlongitude : float
        nutationlongitude : float
        aberration_correction : float
        
        Returns
        -------
        apparent_sun_longitude : float
        
        """
        apparent_sun_longitude = \
            _supy_driver.f90wrap_apparent_sun_longitude_calculation(sun_geocentric_positionlongitude=sun_geocentric_positionlongitude, \
            nutationlongitude=nutationlongitude, \
            aberration_correction=aberration_correction)
        return apparent_sun_longitude
    
    @staticmethod
    def apparent_stime_at_greenwich_calculation(julianday, juliancentury, \
        nutationlongitude, corr_obliquity):
        """
        apparent_stime_at_greenwich = apparent_stime_at_greenwich_calculation(julianday, \
            juliancentury, nutationlongitude, corr_obliquity)
        
        
        Defined at suews_phys_narp.fpp lines 934-953
        
        Parameters
        ----------
        julianday : float
        juliancentury : float
        nutationlongitude : float
        corr_obliquity : float
        
        Returns
        -------
        apparent_stime_at_greenwich : float
        
        """
        apparent_stime_at_greenwich = \
            _supy_driver.f90wrap_apparent_stime_at_greenwich_calculation(julianday=julianday, \
            juliancentury=juliancentury, nutationlongitude=nutationlongitude, \
            corr_obliquity=corr_obliquity)
        return apparent_stime_at_greenwich
    
    @staticmethod
    def sun_rigth_ascension_calculation(apparent_sun_longitude, corr_obliquity, \
        sun_geocentric_positionlatitude):
        """
        sun_rigth_ascension = sun_rigth_ascension_calculation(apparent_sun_longitude, \
            corr_obliquity, sun_geocentric_positionlatitude)
        
        
        Defined at suews_phys_narp.fpp lines 955-971
        
        Parameters
        ----------
        apparent_sun_longitude : float
        corr_obliquity : float
        sun_geocentric_positionlatitude : float
        
        Returns
        -------
        sun_rigth_ascension : float
        
        """
        sun_rigth_ascension = \
            _supy_driver.f90wrap_sun_rigth_ascension_calculation(apparent_sun_longitude=apparent_sun_longitude, \
            corr_obliquity=corr_obliquity, \
            sun_geocentric_positionlatitude=sun_geocentric_positionlatitude)
        return sun_rigth_ascension
    
    @staticmethod
    def sun_geocentric_declination_calculation(apparent_sun_longitude, \
        corr_obliquity, sun_geocentric_positionlatitude):
        """
        sun_geocentric_declination = \
            sun_geocentric_declination_calculation(apparent_sun_longitude, \
            corr_obliquity, sun_geocentric_positionlatitude)
        
        
        Defined at suews_phys_narp.fpp lines 973-984
        
        Parameters
        ----------
        apparent_sun_longitude : float
        corr_obliquity : float
        sun_geocentric_positionlatitude : float
        
        Returns
        -------
        sun_geocentric_declination : float
        
        """
        sun_geocentric_declination = \
            _supy_driver.f90wrap_sun_geocentric_declination_calculation(apparent_sun_longitude=apparent_sun_longitude, \
            corr_obliquity=corr_obliquity, \
            sun_geocentric_positionlatitude=sun_geocentric_positionlatitude)
        return sun_geocentric_declination
    
    @staticmethod
    def observer_local_hour_calculation(apparent_stime_at_greenwich, \
        locationlongitude, sun_rigth_ascension):
        """
        observer_local_hour = \
            observer_local_hour_calculation(apparent_stime_at_greenwich, \
            locationlongitude, sun_rigth_ascension)
        
        
        Defined at suews_phys_narp.fpp lines 986-997
        
        Parameters
        ----------
        apparent_stime_at_greenwich : float
        locationlongitude : float
        sun_rigth_ascension : float
        
        Returns
        -------
        observer_local_hour : float
        
        """
        observer_local_hour = \
            _supy_driver.f90wrap_observer_local_hour_calculation(apparent_stime_at_greenwich=apparent_stime_at_greenwich, \
            locationlongitude=locationlongitude, \
            sun_rigth_ascension=sun_rigth_ascension)
        return observer_local_hour
    
    @staticmethod
    def topocentric_sun_position_calculate(topocentric_sun_positionrigth_ascension, \
        topocentric_sun_positionrigth_ascension_parallax, \
        topocentric_sun_positiondeclination, locationaltitude, locationlatitude, \
        observer_local_hour, sun_rigth_ascension, sun_geocentric_declination, \
        earth_heliocentric_positionradius):
        """
        topocentric_sun_position_calculate(topocentric_sun_positionrigth_ascension, \
            topocentric_sun_positionrigth_ascension_parallax, \
            topocentric_sun_positiondeclination, locationaltitude, locationlatitude, \
            observer_local_hour, sun_rigth_ascension, sun_geocentric_declination, \
            earth_heliocentric_positionradius)
        
        
        Defined at suews_phys_narp.fpp lines 999-1044
        
        Parameters
        ----------
        topocentric_sun_positionrigth_ascension : float
        topocentric_sun_positionrigth_ascension_parallax : float
        topocentric_sun_positiondeclination : float
        locationaltitude : float
        locationlatitude : float
        observer_local_hour : float
        sun_rigth_ascension : float
        sun_geocentric_declination : float
        earth_heliocentric_positionradius : float
        
        """
        _supy_driver.f90wrap_topocentric_sun_position_calculate(topocentric_sun_positionrigth_ascension=topocentric_sun_positionrigth_ascension, \
            topocentric_sun_positionrigth_ascension_parallax=topocentric_sun_positionrigth_ascension_parallax, \
            topocentric_sun_positiondeclination=topocentric_sun_positiondeclination, \
            locationaltitude=locationaltitude, locationlatitude=locationlatitude, \
            observer_local_hour=observer_local_hour, \
            sun_rigth_ascension=sun_rigth_ascension, \
            sun_geocentric_declination=sun_geocentric_declination, \
            earth_heliocentric_positionradius=earth_heliocentric_positionradius)
    
    @staticmethod
    def topocentric_local_hour_calculate(observer_local_hour, \
        topocentric_sun_positionrigth_ascension_parallax):
        """
        topocentric_local_hour = topocentric_local_hour_calculate(observer_local_hour, \
            topocentric_sun_positionrigth_ascension_parallax)
        
        
        Defined at suews_phys_narp.fpp lines 1046-1053
        
        Parameters
        ----------
        observer_local_hour : float
        topocentric_sun_positionrigth_ascension_parallax : float
        
        Returns
        -------
        topocentric_local_hour : float
        
        """
        topocentric_local_hour = \
            _supy_driver.f90wrap_topocentric_local_hour_calculate(observer_local_hour=observer_local_hour, \
            topocentric_sun_positionrigth_ascension_parallax=topocentric_sun_positionrigth_ascension_parallax)
        return topocentric_local_hour
    
    @staticmethod
    def sun_topocentric_zenith_angle_calculate(locationlatitude, \
        topocentric_sun_positiondeclination, topocentric_local_hour, sunazimuth, \
        sunzenith):
        """
        sun_topocentric_zenith_angle_calculate(locationlatitude, \
            topocentric_sun_positiondeclination, topocentric_local_hour, sunazimuth, \
            sunzenith)
        
        
        Defined at suews_phys_narp.fpp lines 1055-1094
        
        Parameters
        ----------
        locationlatitude : float
        topocentric_sun_positiondeclination : float
        topocentric_local_hour : float
        sunazimuth : float
        sunzenith : float
        
        """
        _supy_driver.f90wrap_sun_topocentric_zenith_angle_calculate(locationlatitude=locationlatitude, \
            topocentric_sun_positiondeclination=topocentric_sun_positiondeclination, \
            topocentric_local_hour=topocentric_local_hour, sunazimuth=sunazimuth, \
            sunzenith=sunzenith)
    
    @staticmethod
    def set_to_range(var):
        """
        vari = set_to_range(var)
        
        
        Defined at suews_phys_narp.fpp lines 1096-1108
        
        Parameters
        ----------
        var : float
        
        Returns
        -------
        vari : float
        
        """
        vari = _supy_driver.f90wrap_set_to_range(var=var)
        return vari
    
    @staticmethod
    def dewpoint_narp(temp_c, rh):
        """
        td = dewpoint_narp(temp_c, rh)
        
        
        Defined at suews_phys_narp.fpp lines 1111-1121
        
        Parameters
        ----------
        temp_c : float
        rh : float
        
        Returns
        -------
        td : float
        
        """
        td = _supy_driver.f90wrap_dewpoint_narp(temp_c=temp_c, rh=rh)
        return td
    
    @staticmethod
    def prata_emis(temp_k, ea_hpa):
        """
        emis_a = prata_emis(temp_k, ea_hpa)
        
        
        Defined at suews_phys_narp.fpp lines 1124-1129
        
        Parameters
        ----------
        temp_k : float
        ea_hpa : float
        
        Returns
        -------
        emis_a : float
        
        """
        emis_a = _supy_driver.f90wrap_prata_emis(temp_k=temp_k, ea_hpa=ea_hpa)
        return emis_a
    
    @staticmethod
    def emis_cloud(emis_a, fcld):
        """
        em_adj = emis_cloud(emis_a, fcld)
        
        
        Defined at suews_phys_narp.fpp lines 1132-1137
        
        Parameters
        ----------
        emis_a : float
        fcld : float
        
        Returns
        -------
        em_adj : float
        
        """
        em_adj = _supy_driver.f90wrap_emis_cloud(emis_a=emis_a, fcld=fcld)
        return em_adj
    
    @staticmethod
    def emis_cloud_sq(emis_a, fcld):
        """
        em_adj = emis_cloud_sq(emis_a, fcld)
        
        
        Defined at suews_phys_narp.fpp lines 1140-1143
        
        Parameters
        ----------
        emis_a : float
        fcld : float
        
        Returns
        -------
        em_adj : float
        
        """
        em_adj = _supy_driver.f90wrap_emis_cloud_sq(emis_a=emis_a, fcld=fcld)
        return em_adj
    
    @staticmethod
    def cloud_fraction(kdown, kclear):
        """
        fcld = cloud_fraction(kdown, kclear)
        
        
        Defined at suews_phys_narp.fpp lines 1146-1150
        
        Parameters
        ----------
        kdown : float
        kclear : float
        
        Returns
        -------
        fcld : float
        
        """
        fcld = _supy_driver.f90wrap_cloud_fraction(kdown=kdown, kclear=kclear)
        return fcld
    
    @staticmethod
    def wc_fraction(rh, temp):
        """
        fwc = wc_fraction(rh, temp)
        
        
        Defined at suews_phys_narp.fpp lines 1153-1168
        
        Parameters
        ----------
        rh : float
        temp : float
        
        Returns
        -------
        fwc : float
        
        """
        fwc = _supy_driver.f90wrap_wc_fraction(rh=rh, temp=temp)
        return fwc
    
    @staticmethod
    def isurface(doy, zenith):
        """
        isurf = isurface(doy, zenith)
        
        
        Defined at suews_phys_narp.fpp lines 1191-1207
        
        Parameters
        ----------
        doy : int
        zenith : float
        
        Returns
        -------
        isurf : float
        
        """
        isurf = _supy_driver.f90wrap_isurface(doy=doy, zenith=zenith)
        return isurf
    
    @staticmethod
    def solar_esdist(doy):
        """
        rse = solar_esdist(doy)
        
        
        Defined at suews_phys_narp.fpp lines 1210-1219
        
        Parameters
        ----------
        doy : int
        
        Returns
        -------
        rse : float
        
        """
        rse = _supy_driver.f90wrap_solar_esdist(doy=doy)
        return rse
    
    @staticmethod
    def smithlambda(lat):
        """
        g = smithlambda(lat)
        
        
        Defined at suews_phys_narp.fpp lines 1222-1241
        
        Parameters
        ----------
        lat : int
        
        Returns
        -------
        g : float array
        
        """
        g = _supy_driver.f90wrap_smithlambda(lat=lat)
        return g
    
    @staticmethod
    def transmissivity(press_hpa, temp_c_dew, g, zenith):
        """
        trans = transmissivity(press_hpa, temp_c_dew, g, zenith)
        
        
        Defined at suews_phys_narp.fpp lines 1244-1268
        
        Parameters
        ----------
        press_hpa : float
        temp_c_dew : float
        g : float
        zenith : float
        
        Returns
        -------
        trans : float
        
        """
        trans = _supy_driver.f90wrap_transmissivity(press_hpa=press_hpa, \
            temp_c_dew=temp_c_dew, g=g, zenith=zenith)
        return trans
    
    _dt_array_initialisers = []
    

narp_module = Narp_Module()

class Atmmoiststab_Module(f90wrap.runtime.FortranModule):
    """
    Module atmmoiststab_module
    
    
    Defined at suews_phys_atmmoiststab.fpp lines 5-861
    
    """
    @staticmethod
    def cal_atmmoist(temp_c, press_hpa, avrh, dectime):
        """
        lv_j_kg, lvs_j_kg, es_hpa, ea_hpa, vpd_hpa, vpd_pa, dq, dens_dry, avcp, air_dens \
            = cal_atmmoist(temp_c, press_hpa, avrh, dectime)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 21-82
        
        Parameters
        ----------
        temp_c : float
        press_hpa : float
        avrh : float
        dectime : float
        
        Returns
        -------
        lv_j_kg : float
        lvs_j_kg : float
        es_hpa : float
        ea_hpa : float
        vpd_hpa : float
        vpd_pa : float
        dq : float
        dens_dry : float
        avcp : float
        air_dens : float
        
        """
        lv_j_kg, lvs_j_kg, es_hpa, ea_hpa, vpd_hpa, vpd_pa, dq, dens_dry, avcp, air_dens \
            = _supy_driver.f90wrap_cal_atmmoist(temp_c=temp_c, press_hpa=press_hpa, \
            avrh=avrh, dectime=dectime)
        return lv_j_kg, lvs_j_kg, es_hpa, ea_hpa, vpd_hpa, vpd_pa, dq, dens_dry, avcp, \
            air_dens
    
    @staticmethod
    def cal_stab(stabilitymethod, zzd, z0m, zdm, avu1, temp_c, qh_init, avdens, \
        avcp):
        """
        l_mod, tstar, ustar, zl = cal_stab(stabilitymethod, zzd, z0m, zdm, avu1, temp_c, \
            qh_init, avdens, avcp)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 109-224
        
        Parameters
        ----------
        stabilitymethod : int
        zzd : float
        z0m : float
        zdm : float
        avu1 : float
        temp_c : float
        qh_init : float
        avdens : float
        avcp : float
        
        Returns
        -------
        l_mod : float
        tstar : float
        ustar : float
        zl : float
        
        """
        l_mod, tstar, ustar, zl = \
            _supy_driver.f90wrap_cal_stab(stabilitymethod=stabilitymethod, zzd=zzd, \
            z0m=z0m, zdm=zdm, avu1=avu1, temp_c=temp_c, qh_init=qh_init, avdens=avdens, \
            avcp=avcp)
        return l_mod, tstar, ustar, zl
    
    @staticmethod
    def stab_psi_mom(stabilitymethod, zl):
        """
        psim = stab_psi_mom(stabilitymethod, zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 230-241
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_stab_psi_mom(stabilitymethod=stabilitymethod, zl=zl)
        return psim
    
    @staticmethod
    def stab_psi_heat(stabilitymethod, zl):
        """
        psih = stab_psi_heat(stabilitymethod, zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 244-255
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_stab_psi_heat(stabilitymethod=stabilitymethod, \
            zl=zl)
        return psih
    
    @staticmethod
    def stab_phi_mom(stabilitymethod, zl):
        """
        phim = stab_phi_mom(stabilitymethod, zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 258-269
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_stab_phi_mom(stabilitymethod=stabilitymethod, zl=zl)
        return phim
    
    @staticmethod
    def stab_phi_heat(stabilitymethod, zl):
        """
        phih = stab_phi_heat(stabilitymethod, zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 272-283
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_stab_phi_heat(stabilitymethod=stabilitymethod, \
            zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_j12(zl):
        """
        psim = psi_mom_j12(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 288-302
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_psi_mom_j12(zl=zl)
        return psim
    
    @staticmethod
    def phi_mom_j12(zl):
        """
        phim = phi_mom_j12(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 304-316
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_phi_mom_j12(zl=zl)
        return phim
    
    @staticmethod
    def psi_heat_j12(zl):
        """
        psih = psi_heat_j12(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 318-330
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_psi_heat_j12(zl=zl)
        return psih
    
    @staticmethod
    def phi_heat_j12(zl):
        """
        phih = phi_heat_j12(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 332-340
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_phi_heat_j12(zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_g00(zl):
        """
        psim = psi_mom_g00(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 348-365
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_psi_mom_g00(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_g00(zl):
        """
        psih = psi_heat_g00(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 367-384
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_psi_heat_g00(zl=zl)
        return psih
    
    @staticmethod
    def phi_mom_g00(zl):
        """
        phim = phi_mom_g00(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 392-413
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_phi_mom_g00(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_g00(zl):
        """
        phih = phi_heat_g00(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 415-433
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_phi_heat_g00(zl=zl)
        return phih
    
    @staticmethod
    def psi_conv(zl, ax):
        """
        psic = psi_conv(zl, ax)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 435-440
        
        Parameters
        ----------
        zl : float
        ax : float
        
        Returns
        -------
        psic : float
        
        """
        psic = _supy_driver.f90wrap_psi_conv(zl=zl, ax=ax)
        return psic
    
    @staticmethod
    def phi_conv(zl, ax):
        """
        phic = phi_conv(zl, ax)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 442-450
        
        Parameters
        ----------
        zl : float
        ax : float
        
        Returns
        -------
        phic : float
        
        """
        phic = _supy_driver.f90wrap_phi_conv(zl=zl, ax=ax)
        return phic
    
    @staticmethod
    def dpsi_dzl_g00(zl, psik, phik, psic, phic):
        """
        dpsi = dpsi_dzl_g00(zl, psik, phik, psic, phic)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 452-467
        
        Parameters
        ----------
        zl : float
        psik : float
        phik : float
        psic : float
        phic : float
        
        Returns
        -------
        dpsi : float
        
        """
        dpsi = _supy_driver.f90wrap_dpsi_dzl_g00(zl=zl, psik=psik, phik=phik, psic=psic, \
            phic=phic)
        return dpsi
    
    @staticmethod
    def psi_cb05(zl, k1, k2):
        """
        psi = psi_cb05(zl, k1, k2)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 474-477
        
        Parameters
        ----------
        zl : float
        k1 : float
        k2 : float
        
        Returns
        -------
        psi : float
        
        """
        psi = _supy_driver.f90wrap_psi_cb05(zl=zl, k1=k1, k2=k2)
        return psi
    
    @staticmethod
    def psi_mom_cb05(zl):
        """
        psim = psi_mom_cb05(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 479-488
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_psi_mom_cb05(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_cb05(zl):
        """
        psih = psi_heat_cb05(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 490-499
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_psi_heat_cb05(zl=zl)
        return psih
    
    @staticmethod
    def phi_cb05(zl, k1, k2):
        """
        phi = phi_cb05(zl, k1, k2)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 501-508
        
        Parameters
        ----------
        zl : float
        k1 : float
        k2 : float
        
        Returns
        -------
        phi : float
        
        """
        phi = _supy_driver.f90wrap_phi_cb05(zl=zl, k1=k1, k2=k2)
        return phi
    
    @staticmethod
    def phi_mom_cb05(zl):
        """
        phim = phi_mom_cb05(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 510-519
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_phi_mom_cb05(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_cb05(zl):
        """
        phih = phi_heat_cb05(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 521-531
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_phi_heat_cb05(zl=zl)
        return phih
    
    @staticmethod
    def phi_mom_k75(zl):
        """
        phim = phi_mom_k75(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 537-546
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_phi_mom_k75(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_k75(zl):
        """
        phih = phi_heat_k75(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 548-557
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_phi_heat_k75(zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_k75(zl):
        """
        psim = psi_mom_k75(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 559-568
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_psi_mom_k75(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_k75(zl):
        """
        psih = psi_heat_k75(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 570-579
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_psi_heat_k75(zl=zl)
        return psih
    
    @staticmethod
    def phi_mom_b71(zl):
        """
        phim = phi_mom_b71(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 585-595
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_phi_mom_b71(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_b71(zl):
        """
        phih = phi_heat_b71(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 597-607
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_phi_heat_b71(zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_b71(zl):
        """
        psim = psi_mom_b71(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 609-621
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_psi_mom_b71(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_b71(zl):
        """
        psih = psi_heat_b71(zl)
        
        
        Defined at suews_phys_atmmoiststab.fpp lines 623-637
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_psi_heat_b71(zl=zl)
        return psih
    
    @property
    def neut_limit(self):
        """
        Element neut_limit ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_phys_atmmoiststab.fpp line 7
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__neut_limit()
    
    @property
    def k(self):
        """
        Element k ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_phys_atmmoiststab.fpp line 8
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__k()
    
    @property
    def grav(self):
        """
        Element grav ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_phys_atmmoiststab.fpp line 9
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__grav()
    
    @property
    def j12(self):
        """
        Element j12 ftype=integer pytype=int
        
        
        Defined at suews_phys_atmmoiststab.fpp line 11
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__j12()
    
    @property
    def k75(self):
        """
        Element k75 ftype=integer pytype=int
        
        
        Defined at suews_phys_atmmoiststab.fpp line 12
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__k75()
    
    @property
    def b71(self):
        """
        Element b71 ftype=integer pytype=int
        
        
        Defined at suews_phys_atmmoiststab.fpp line 13
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__b71()
    
    def __str__(self):
        ret = ['<atmmoiststab_module>{\n']
        ret.append('    neut_limit : ')
        ret.append(repr(self.neut_limit))
        ret.append(',\n    k : ')
        ret.append(repr(self.k))
        ret.append(',\n    grav : ')
        ret.append(repr(self.grav))
        ret.append(',\n    j12 : ')
        ret.append(repr(self.j12))
        ret.append(',\n    k75 : ')
        ret.append(repr(self.k75))
        ret.append(',\n    b71 : ')
        ret.append(repr(self.b71))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

atmmoiststab_module = Atmmoiststab_Module()

class Waterdist_Module(f90wrap.runtime.FortranModule):
    """
    Module waterdist_module
    
    
    Defined at suews_phys_waterdist.fpp lines 5-1760
    
    """
    @staticmethod
    def drainage(is_, state_is, storcap, draineq, draincoef1, draincoef2, nsh_real):
        """
        drain_is = drainage(is_, state_is, storcap, draineq, draincoef1, draincoef2, \
            nsh_real)
        
        
        Defined at suews_phys_waterdist.fpp lines 30-78
        
        Parameters
        ----------
        is_ : int
        state_is : float
        storcap : float
        draineq : float
        draincoef1 : float
        draincoef2 : float
        nsh_real : float
        
        Returns
        -------
        drain_is : float
        
        ------------------------------------------------------------------------------
        """
        drain_is = _supy_driver.f90wrap_drainage(is_=is_, state_is=state_is, \
            storcap=storcap, draineq=draineq, draincoef1=draincoef1, \
            draincoef2=draincoef2, nsh_real=nsh_real)
        return drain_is
    
    @staticmethod
    def cal_water_storage(is_, sfr_surf, pipecapacity, runofftowater, pin, wu_surf, \
        drain_surf, addwater, addimpervious, nsh_real, state_in, frac_water2runoff, \
        pervfraction, addveg, soilstorecap, addwaterbody, flowchange, statelimit, \
        runoffagimpervious, runoffagveg, runoffpipes, ev, soilstore_id, \
        surpluswaterbody, surplusevap, runoffwaterbody, runoff, state_out):
        """
        cal_water_storage(is_, sfr_surf, pipecapacity, runofftowater, pin, wu_surf, \
            drain_surf, addwater, addimpervious, nsh_real, state_in, frac_water2runoff, \
            pervfraction, addveg, soilstorecap, addwaterbody, flowchange, statelimit, \
            runoffagimpervious, runoffagveg, runoffpipes, ev, soilstore_id, \
            surpluswaterbody, surplusevap, runoffwaterbody, runoff, state_out)
        
        
        Defined at suews_phys_waterdist.fpp lines 89-338
        
        Parameters
        ----------
        is_ : int
        sfr_surf : float array
        pipecapacity : float
        runofftowater : float
        pin : float
        wu_surf : float array
        drain_surf : float array
        addwater : float array
        addimpervious : float
        nsh_real : float
        state_in : float array
        frac_water2runoff : float array
        pervfraction : float
        addveg : float
        soilstorecap : float array
        addwaterbody : float
        flowchange : float
        statelimit : float array
        runoffagimpervious : float
        runoffagveg : float
        runoffpipes : float
        ev : float
        soilstore_id : float array
        surpluswaterbody : float
        surplusevap : float array
        runoffwaterbody : float
        runoff : float array
        state_out : float array
        
        ------------------------------------------------------------------------------
        Calculation of storage change
         TS 30 Nov 2019
           - Allow irrigation on all surfaces(previously only on vegetated surfaces)
         LJ 27 Jan 2016
           - Removed tabs and cleaned the code
         HCW 08 Dec 2015
           -Added if-loop check for no Paved surfaces
         LJ 6 May 2015
           - Calculations of the piperunoff exceedings moved to separate subroutine \
               updateFlood.
           - Now also called from snow subroutine
           - Evaporation is modified using EvapPart
           - when no water on impervious surfaces, evap occurs above pervious surfaces \
               instead
         Rewritten by HCW 12 Feb 2015
           - Old variable 'p' for water input to the surface renamed to 'p_mm'
           - All water now added to p_mm first, before threshold checks or other \
               calculations
           - Water from other grids now added to p_mm(instead of state_id for impervious \
               surfaces)
           - Removed division of runoff by nsh, as whole model now runs at the same \
               timestep
           - Adjusted transfer of ev between surfaces to conserve mass(not depth)
           - Volumes used for water transport between grids to account for SurfaceArea \
               changing between grids
           - Added threshold check for state_id(WaterSurf) - was going negative
         Last modified HCW 09 Feb 2015
           - Removed StorCap input because it is provided by module allocateArray
           - Tidied and commented code
         Modified by LJ in November 2012:
           - P>10 was not taken into account for impervious surfaces - Was fixed.
           - Above impervious surfaces possibility of the state_id to exceed max capacity \
               was limited
             although this should be possible - was fixed
         Modified by LJ 10/2010
         Rewritten mostly by LJ in 2010
         To do:
           - Finish area normalisation for RG2G & finish coding GridConnections
           - What is the 10 mm hr-1 threshold for?
          - Decide upon and correct storage capacities here & in evap subroutine
          - FlowChange units should be mm hr-1 - need to update everywhere
           - Add SurfaceFlood(is)?
           - What happens if sfr_surf(is) = 0 or 1?
           - Consider how irrigated trees actually works...
        ------------------------------------------------------------------------------
        """
        _supy_driver.f90wrap_cal_water_storage(is_=is_, sfr_surf=sfr_surf, \
            pipecapacity=pipecapacity, runofftowater=runofftowater, pin=pin, \
            wu_surf=wu_surf, drain_surf=drain_surf, addwater=addwater, \
            addimpervious=addimpervious, nsh_real=nsh_real, state_in=state_in, \
            frac_water2runoff=frac_water2runoff, pervfraction=pervfraction, \
            addveg=addveg, soilstorecap=soilstorecap, addwaterbody=addwaterbody, \
            flowchange=flowchange, statelimit=statelimit, \
            runoffagimpervious=runoffagimpervious, runoffagveg=runoffagveg, \
            runoffpipes=runoffpipes, ev=ev, soilstore_id=soilstore_id, \
            surpluswaterbody=surpluswaterbody, surplusevap=surplusevap, \
            runoffwaterbody=runoffwaterbody, runoff=runoff, state_out=state_out)
    
    @staticmethod
    def cal_water_storage_surf(pin, nsh_real, pipecapacity, runofftowater, \
        addimpervious, addveg, addwaterbody, flowchange, soilstorecap_surf, \
        statelimit_surf, pervfraction, sfr_surf, drain_surf, addwater_surf, \
        frac_water2runoff_surf, wu_surf, ev_surf_in, state_surf_in, \
        soilstore_surf_in, ev_surf_out, state_surf_out, soilstore_surf_out, \
        runoff_surf):
        """
        runoffagimpervious_grid, runoffagveg_grid, runoffpipes_grid, \
            runoffwaterbody_grid = cal_water_storage_surf(pin, nsh_real, pipecapacity, \
            runofftowater, addimpervious, addveg, addwaterbody, flowchange, \
            soilstorecap_surf, statelimit_surf, pervfraction, sfr_surf, drain_surf, \
            addwater_surf, frac_water2runoff_surf, wu_surf, ev_surf_in, state_surf_in, \
            soilstore_surf_in, ev_surf_out, state_surf_out, soilstore_surf_out, \
            runoff_surf)
        
        
        Defined at suews_phys_waterdist.fpp lines 353-445
        
        Parameters
        ----------
        pin : float
        nsh_real : float
        pipecapacity : float
        runofftowater : float
        addimpervious : float
        addveg : float
        addwaterbody : float
        flowchange : float
        soilstorecap_surf : float array
        statelimit_surf : float array
        pervfraction : float
        sfr_surf : float array
        drain_surf : float array
        addwater_surf : float array
        frac_water2runoff_surf : float array
        wu_surf : float array
        ev_surf_in : float array
        state_surf_in : float array
        soilstore_surf_in : float array
        ev_surf_out : float array
        state_surf_out : float array
        soilstore_surf_out : float array
        runoff_surf : float array
        
        Returns
        -------
        runoffagimpervious_grid : float
        runoffagveg_grid : float
        runoffpipes_grid : float
        runoffwaterbody_grid : float
        
        """
        runoffagimpervious_grid, runoffagveg_grid, runoffpipes_grid, \
            runoffwaterbody_grid = _supy_driver.f90wrap_cal_water_storage_surf(pin=pin, \
            nsh_real=nsh_real, pipecapacity=pipecapacity, runofftowater=runofftowater, \
            addimpervious=addimpervious, addveg=addveg, addwaterbody=addwaterbody, \
            flowchange=flowchange, soilstorecap_surf=soilstorecap_surf, \
            statelimit_surf=statelimit_surf, pervfraction=pervfraction, \
            sfr_surf=sfr_surf, drain_surf=drain_surf, addwater_surf=addwater_surf, \
            frac_water2runoff_surf=frac_water2runoff_surf, wu_surf=wu_surf, \
            ev_surf_in=ev_surf_in, state_surf_in=state_surf_in, \
            soilstore_surf_in=soilstore_surf_in, ev_surf_out=ev_surf_out, \
            state_surf_out=state_surf_out, soilstore_surf_out=soilstore_surf_out, \
            runoff_surf=runoff_surf)
        return runoffagimpervious_grid, runoffagveg_grid, runoffpipes_grid, \
            runoffwaterbody_grid
    
    @staticmethod
    def cal_water_storage_building(pin, nsh_real, nlayer, sfr_roof, statelimit_roof, \
        soilstorecap_roof, wetthresh_roof, ev_roof_in, state_roof_in, \
        soilstore_roof_in, sfr_wall, statelimit_wall, soilstorecap_wall, \
        wetthresh_wall, ev_wall_in, state_wall_in, soilstore_wall_in, ev_roof_out, \
        state_roof_out, soilstore_roof_out, runoff_roof, ev_wall_out, \
        state_wall_out, soilstore_wall_out, runoff_wall):
        """
        state_building, soilstore_building, runoff_building, soilstorecap_building = \
            cal_water_storage_building(pin, nsh_real, nlayer, sfr_roof, statelimit_roof, \
            soilstorecap_roof, wetthresh_roof, ev_roof_in, state_roof_in, \
            soilstore_roof_in, sfr_wall, statelimit_wall, soilstorecap_wall, \
            wetthresh_wall, ev_wall_in, state_wall_in, soilstore_wall_in, ev_roof_out, \
            state_roof_out, soilstore_roof_out, runoff_roof, ev_wall_out, \
            state_wall_out, soilstore_wall_out, runoff_wall)
        
        
        Defined at suews_phys_waterdist.fpp lines 447-608
        
        Parameters
        ----------
        pin : float
        nsh_real : float
        nlayer : int
        sfr_roof : float array
        statelimit_roof : float array
        soilstorecap_roof : float array
        wetthresh_roof : float array
        ev_roof_in : float array
        state_roof_in : float array
        soilstore_roof_in : float array
        sfr_wall : float array
        statelimit_wall : float array
        soilstorecap_wall : float array
        wetthresh_wall : float array
        ev_wall_in : float array
        state_wall_in : float array
        soilstore_wall_in : float array
        ev_roof_out : float array
        state_roof_out : float array
        soilstore_roof_out : float array
        runoff_roof : float array
        ev_wall_out : float array
        state_wall_out : float array
        soilstore_wall_out : float array
        runoff_wall : float array
        
        Returns
        -------
        state_building : float
        soilstore_building : float
        runoff_building : float
        soilstorecap_building : float
        
        """
        state_building, soilstore_building, runoff_building, soilstorecap_building = \
            _supy_driver.f90wrap_cal_water_storage_building(pin=pin, nsh_real=nsh_real, \
            nlayer=nlayer, sfr_roof=sfr_roof, statelimit_roof=statelimit_roof, \
            soilstorecap_roof=soilstorecap_roof, wetthresh_roof=wetthresh_roof, \
            ev_roof_in=ev_roof_in, state_roof_in=state_roof_in, \
            soilstore_roof_in=soilstore_roof_in, sfr_wall=sfr_wall, \
            statelimit_wall=statelimit_wall, soilstorecap_wall=soilstorecap_wall, \
            wetthresh_wall=wetthresh_wall, ev_wall_in=ev_wall_in, \
            state_wall_in=state_wall_in, soilstore_wall_in=soilstore_wall_in, \
            ev_roof_out=ev_roof_out, state_roof_out=state_roof_out, \
            soilstore_roof_out=soilstore_roof_out, runoff_roof=runoff_roof, \
            ev_wall_out=ev_wall_out, state_wall_out=state_wall_out, \
            soilstore_wall_out=soilstore_wall_out, runoff_wall=runoff_wall)
        return state_building, soilstore_building, runoff_building, \
            soilstorecap_building
    
    @staticmethod
    def updateflood(is_, runoff, sfr_surf, pipecapacity, runofftowater, \
        runoffagimpervious, surpluswaterbody, runoffagveg, runoffpipes):
        """
        updateflood(is_, runoff, sfr_surf, pipecapacity, runofftowater, \
            runoffagimpervious, surpluswaterbody, runoffagveg, runoffpipes)
        
        
        Defined at suews_phys_waterdist.fpp lines 614-647
        
        Parameters
        ----------
        is_ : int
        runoff : float array
        sfr_surf : float array
        pipecapacity : float
        runofftowater : float
        runoffagimpervious : float
        surpluswaterbody : float
        runoffagveg : float
        runoffpipes : float
        
        ------Paved and building surface
        """
        _supy_driver.f90wrap_updateflood(is_=is_, runoff=runoff, sfr_surf=sfr_surf, \
            pipecapacity=pipecapacity, runofftowater=runofftowater, \
            runoffagimpervious=runoffagimpervious, surpluswaterbody=surpluswaterbody, \
            runoffagveg=runoffagveg, runoffpipes=runoffpipes)
    
    @staticmethod
    def redistributewater(snowuse, waterdist, sfr_surf, drain, addwaterrunoff, \
        addwater):
        """
        redistributewater(snowuse, waterdist, sfr_surf, drain, addwaterrunoff, addwater)
        
        
        Defined at suews_phys_waterdist.fpp lines 653-688
        
        Parameters
        ----------
        snowuse : int
        waterdist : float array
        sfr_surf : float array
        drain : float array
        addwaterrunoff : float array
        addwater : float array
        
        -------------------------------------------------------------------
        """
        _supy_driver.f90wrap_redistributewater(snowuse=snowuse, waterdist=waterdist, \
            sfr_surf=sfr_surf, drain=drain, addwaterrunoff=addwaterrunoff, \
            addwater=addwater)
    
    @staticmethod
    def suews_update_soilmoist(nonwaterfraction, soilstorecap, sfr_surf, \
        soilstore_id):
        """
        soilmoistcap, soilstate, vsmd, smd = suews_update_soilmoist(nonwaterfraction, \
            soilstorecap, sfr_surf, soilstore_id)
        
        
        Defined at suews_phys_waterdist.fpp lines 696-739
        
        Parameters
        ----------
        nonwaterfraction : float
        soilstorecap : float array
        sfr_surf : float array
        soilstore_id : float array
        
        Returns
        -------
        soilmoistcap : float
        soilstate : float
        vsmd : float
        smd : float
        
        """
        soilmoistcap, soilstate, vsmd, smd = \
            _supy_driver.f90wrap_suews_update_soilmoist(nonwaterfraction=nonwaterfraction, \
            soilstorecap=soilstorecap, sfr_surf=sfr_surf, soilstore_id=soilstore_id)
        return soilmoistcap, soilstate, vsmd, smd
    
    @staticmethod
    def suews_update_soilmoist_dts(nonwaterfraction, sfr_paved, sfr_bldg, sfr_evetr, \
        sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, soilstorecap_paved, \
        soilstorecap_bldg, soilstorecap_evetr, soilstorecap_dectr, \
        soilstorecap_grass, soilstorecap_bsoil, soilstorecap_water, soilstore_id):
        """
        soilmoistcap, soilstate, vsmd, smd = \
            suews_update_soilmoist_dts(nonwaterfraction, sfr_paved, sfr_bldg, sfr_evetr, \
            sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, soilstorecap_paved, \
            soilstorecap_bldg, soilstorecap_evetr, soilstorecap_dectr, \
            soilstorecap_grass, soilstorecap_bsoil, soilstorecap_water, soilstore_id)
        
        
        Defined at suews_phys_waterdist.fpp lines 741-801
        
        Parameters
        ----------
        nonwaterfraction : float
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        soilstorecap_paved : float
        soilstorecap_bldg : float
        soilstorecap_evetr : float
        soilstorecap_dectr : float
        soilstorecap_grass : float
        soilstorecap_bsoil : float
        soilstorecap_water : float
        soilstore_id : float array
        
        Returns
        -------
        soilmoistcap : float
        soilstate : float
        vsmd : float
        smd : float
        
        """
        soilmoistcap, soilstate, vsmd, smd = \
            _supy_driver.f90wrap_suews_update_soilmoist_dts(nonwaterfraction=nonwaterfraction, \
            sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, \
            sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, \
            sfr_water=sfr_water, soilstorecap_paved=soilstorecap_paved, \
            soilstorecap_bldg=soilstorecap_bldg, soilstorecap_evetr=soilstorecap_evetr, \
            soilstorecap_dectr=soilstorecap_dectr, \
            soilstorecap_grass=soilstorecap_grass, \
            soilstorecap_bsoil=soilstorecap_bsoil, \
            soilstorecap_water=soilstorecap_water, soilstore_id=soilstore_id)
        return soilmoistcap, soilstate, vsmd, smd
    
    @staticmethod
    def cal_smd_veg(soilstorecap, soilstore_id, sfr_surf):
        """
        vsmd = cal_smd_veg(soilstorecap, soilstore_id, sfr_surf)
        
        
        Defined at suews_phys_waterdist.fpp lines 805-820
        
        Parameters
        ----------
        soilstorecap : float array
        soilstore_id : float array
        sfr_surf : float array
        
        Returns
        -------
        vsmd : float
        
        """
        vsmd = _supy_driver.f90wrap_cal_smd_veg(soilstorecap=soilstorecap, \
            soilstore_id=soilstore_id, sfr_surf=sfr_surf)
        return vsmd
    
    @staticmethod
    def suews_cal_soilstate(smdmethod, xsmd, nonwaterfraction, soilmoistcap, \
        soilstorecap, surf_chang_per_tstep, soilstore_id, soilstoreold, sfr_surf, \
        smd_nsurf):
        """
        smd, tot_chang_per_tstep, soilstate = suews_cal_soilstate(smdmethod, xsmd, \
            nonwaterfraction, soilmoistcap, soilstorecap, surf_chang_per_tstep, \
            soilstore_id, soilstoreold, sfr_surf, smd_nsurf)
        
        
        Defined at suews_phys_waterdist.fpp lines 827-885
        
        Parameters
        ----------
        smdmethod : int
        xsmd : float
        nonwaterfraction : float
        soilmoistcap : float
        soilstorecap : float array
        surf_chang_per_tstep : float
        soilstore_id : float array
        soilstoreold : float array
        sfr_surf : float array
        smd_nsurf : float array
        
        Returns
        -------
        smd : float
        tot_chang_per_tstep : float
        soilstate : float
        
        """
        smd, tot_chang_per_tstep, soilstate = \
            _supy_driver.f90wrap_suews_cal_soilstate(smdmethod=smdmethod, xsmd=xsmd, \
            nonwaterfraction=nonwaterfraction, soilmoistcap=soilmoistcap, \
            soilstorecap=soilstorecap, surf_chang_per_tstep=surf_chang_per_tstep, \
            soilstore_id=soilstore_id, soilstoreold=soilstoreold, sfr_surf=sfr_surf, \
            smd_nsurf=smd_nsurf)
        return smd, tot_chang_per_tstep, soilstate
    
    @staticmethod
    def suews_cal_soilstate_dts(smdmethod, xsmd, nonwaterfraction, soilmoistcap, \
        soilstorecap_paved, soilstorecap_bldg, soilstorecap_evetr, \
        soilstorecap_dectr, soilstorecap_grass, soilstorecap_bsoil, \
        soilstorecap_water, surf_chang_per_tstep, soilstore_id, soilstoreold, \
        sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
        smd_nsurf):
        """
        smd, tot_chang_per_tstep, soilstate = suews_cal_soilstate_dts(smdmethod, xsmd, \
            nonwaterfraction, soilmoistcap, soilstorecap_paved, soilstorecap_bldg, \
            soilstorecap_evetr, soilstorecap_dectr, soilstorecap_grass, \
            soilstorecap_bsoil, soilstorecap_water, surf_chang_per_tstep, soilstore_id, \
            soilstoreold, sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, \
            sfr_bsoil, sfr_water, smd_nsurf)
        
        
        Defined at suews_phys_waterdist.fpp lines 887-960
        
        Parameters
        ----------
        smdmethod : int
        xsmd : float
        nonwaterfraction : float
        soilmoistcap : float
        soilstorecap_paved : float
        soilstorecap_bldg : float
        soilstorecap_evetr : float
        soilstorecap_dectr : float
        soilstorecap_grass : float
        soilstorecap_bsoil : float
        soilstorecap_water : float
        surf_chang_per_tstep : float
        soilstore_id : float array
        soilstoreold : float array
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        smd_nsurf : float array
        
        Returns
        -------
        smd : float
        tot_chang_per_tstep : float
        soilstate : float
        
        """
        smd, tot_chang_per_tstep, soilstate = \
            _supy_driver.f90wrap_suews_cal_soilstate_dts(smdmethod=smdmethod, xsmd=xsmd, \
            nonwaterfraction=nonwaterfraction, soilmoistcap=soilmoistcap, \
            soilstorecap_paved=soilstorecap_paved, soilstorecap_bldg=soilstorecap_bldg, \
            soilstorecap_evetr=soilstorecap_evetr, \
            soilstorecap_dectr=soilstorecap_dectr, \
            soilstorecap_grass=soilstorecap_grass, \
            soilstorecap_bsoil=soilstorecap_bsoil, \
            soilstorecap_water=soilstorecap_water, \
            surf_chang_per_tstep=surf_chang_per_tstep, soilstore_id=soilstore_id, \
            soilstoreold=soilstoreold, sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, \
            sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, \
            sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, smd_nsurf=smd_nsurf)
        return smd, tot_chang_per_tstep, soilstate
    
    @staticmethod
    def suews_cal_horizontalsoilwater(sfr_surf, soilstorecap, soildepth, \
        sathydraulicconduct, surfacearea, nonwaterfraction, tstep_real, \
        soilstore_id, runoffsoil):
        """
        runoffsoil_per_tstep = suews_cal_horizontalsoilwater(sfr_surf, soilstorecap, \
            soildepth, sathydraulicconduct, surfacearea, nonwaterfraction, tstep_real, \
            soilstore_id, runoffsoil)
        
        
        Defined at suews_phys_waterdist.fpp lines 974-1168
        
        Parameters
        ----------
        sfr_surf : float array
        soilstorecap : float array
        soildepth : float array
        sathydraulicconduct : float array
        surfacearea : float
        nonwaterfraction : float
        tstep_real : float
        soilstore_id : float array
        runoffsoil : float array
        
        Returns
        -------
        runoffsoil_per_tstep : float
        
        ------------------------------------------------------
         use SUES_data
         use gis_data
         use time
         use allocateArray
        """
        runoffsoil_per_tstep = \
            _supy_driver.f90wrap_suews_cal_horizontalsoilwater(sfr_surf=sfr_surf, \
            soilstorecap=soilstorecap, soildepth=soildepth, \
            sathydraulicconduct=sathydraulicconduct, surfacearea=surfacearea, \
            nonwaterfraction=nonwaterfraction, tstep_real=tstep_real, \
            soilstore_id=soilstore_id, runoffsoil=runoffsoil)
        return runoffsoil_per_tstep
    
    @staticmethod
    def suews_cal_horizontalsoilwater_dts(sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, \
        sfr_grass, sfr_bsoil, sfr_water, soilstorecap_paved, soilstorecap_bldg, \
        soilstorecap_evetr, soilstorecap_dectr, soilstorecap_grass, \
        soilstorecap_bsoil, soilstorecap_water, soildepth_paved, soildepth_bldg, \
        soildepth_evetr, soildepth_dectr, soildepth_grass, soildepth_bsoil, \
        soildepth_water, sathydraulicconduct_paved, sathydraulicconduct_bldg, \
        sathydraulicconduct_evetr, sathydraulicconduct_dectr, \
        sathydraulicconduct_grass, sathydraulicconduct_bsoil, \
        sathydraulicconduct_water, surfacearea, nonwaterfraction, tstep_real, \
        soilstore_id, runoffsoil):
        """
        runoffsoil_per_tstep = suews_cal_horizontalsoilwater_dts(sfr_paved, sfr_bldg, \
            sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, soilstorecap_paved, \
            soilstorecap_bldg, soilstorecap_evetr, soilstorecap_dectr, \
            soilstorecap_grass, soilstorecap_bsoil, soilstorecap_water, soildepth_paved, \
            soildepth_bldg, soildepth_evetr, soildepth_dectr, soildepth_grass, \
            soildepth_bsoil, soildepth_water, sathydraulicconduct_paved, \
            sathydraulicconduct_bldg, sathydraulicconduct_evetr, \
            sathydraulicconduct_dectr, sathydraulicconduct_grass, \
            sathydraulicconduct_bsoil, sathydraulicconduct_water, surfacearea, \
            nonwaterfraction, tstep_real, soilstore_id, runoffsoil)
        
        
        Defined at suews_phys_waterdist.fpp lines 1170-1400
        
        Parameters
        ----------
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        soilstorecap_paved : float
        soilstorecap_bldg : float
        soilstorecap_evetr : float
        soilstorecap_dectr : float
        soilstorecap_grass : float
        soilstorecap_bsoil : float
        soilstorecap_water : float
        soildepth_paved : float
        soildepth_bldg : float
        soildepth_evetr : float
        soildepth_dectr : float
        soildepth_grass : float
        soildepth_bsoil : float
        soildepth_water : float
        sathydraulicconduct_paved : float
        sathydraulicconduct_bldg : float
        sathydraulicconduct_evetr : float
        sathydraulicconduct_dectr : float
        sathydraulicconduct_grass : float
        sathydraulicconduct_bsoil : float
        sathydraulicconduct_water : float
        surfacearea : float
        nonwaterfraction : float
        tstep_real : float
        soilstore_id : float array
        runoffsoil : float array
        
        Returns
        -------
        runoffsoil_per_tstep : float
        
        ------------------------------------------------------
         use SUES_data
         use gis_data
         use time
         use allocateArray
        """
        runoffsoil_per_tstep = \
            _supy_driver.f90wrap_suews_cal_horizontalsoilwater_dts(sfr_paved=sfr_paved, \
            sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, \
            sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, \
            soilstorecap_paved=soilstorecap_paved, soilstorecap_bldg=soilstorecap_bldg, \
            soilstorecap_evetr=soilstorecap_evetr, \
            soilstorecap_dectr=soilstorecap_dectr, \
            soilstorecap_grass=soilstorecap_grass, \
            soilstorecap_bsoil=soilstorecap_bsoil, \
            soilstorecap_water=soilstorecap_water, soildepth_paved=soildepth_paved, \
            soildepth_bldg=soildepth_bldg, soildepth_evetr=soildepth_evetr, \
            soildepth_dectr=soildepth_dectr, soildepth_grass=soildepth_grass, \
            soildepth_bsoil=soildepth_bsoil, soildepth_water=soildepth_water, \
            sathydraulicconduct_paved=sathydraulicconduct_paved, \
            sathydraulicconduct_bldg=sathydraulicconduct_bldg, \
            sathydraulicconduct_evetr=sathydraulicconduct_evetr, \
            sathydraulicconduct_dectr=sathydraulicconduct_dectr, \
            sathydraulicconduct_grass=sathydraulicconduct_grass, \
            sathydraulicconduct_bsoil=sathydraulicconduct_bsoil, \
            sathydraulicconduct_water=sathydraulicconduct_water, \
            surfacearea=surfacearea, nonwaterfraction=nonwaterfraction, \
            tstep_real=tstep_real, soilstore_id=soilstore_id, runoffsoil=runoffsoil)
        return runoffsoil_per_tstep
    
    @staticmethod
    def suews_cal_wateruse(nsh_real, wu_m3, surfacearea, sfr_surf, irrfracpaved, \
        irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, \
        irrfracwater, dayofweek_id, wuprofa_24hr, wuprofm_24hr, internalwateruse_h, \
        hdd_id, wuday_id, waterusemethod, nsh, it, imin, dls, wu_surf):
        """
        wu_int, wu_ext = suews_cal_wateruse(nsh_real, wu_m3, surfacearea, sfr_surf, \
            irrfracpaved, irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, \
            irrfracbsoil, irrfracwater, dayofweek_id, wuprofa_24hr, wuprofm_24hr, \
            internalwateruse_h, hdd_id, wuday_id, waterusemethod, nsh, it, imin, dls, \
            wu_surf)
        
        
        Defined at suews_phys_waterdist.fpp lines 1413-1583
        
        Parameters
        ----------
        nsh_real : float
        wu_m3 : float
        surfacearea : float
        sfr_surf : float array
        irrfracpaved : float
        irrfracbldgs : float
        irrfracevetr : float
        irrfracdectr : float
        irrfracgrass : float
        irrfracbsoil : float
        irrfracwater : float
        dayofweek_id : int array
        wuprofa_24hr : float array
        wuprofm_24hr : float array
        internalwateruse_h : float
        hdd_id : float array
        wuday_id : float array
        waterusemethod : int
        nsh : int
        it : int
        imin : int
        dls : int
        wu_surf : float array
        
        Returns
        -------
        wu_int : float
        wu_ext : float
        
        """
        wu_int, wu_ext = _supy_driver.f90wrap_suews_cal_wateruse(nsh_real=nsh_real, \
            wu_m3=wu_m3, surfacearea=surfacearea, sfr_surf=sfr_surf, \
            irrfracpaved=irrfracpaved, irrfracbldgs=irrfracbldgs, \
            irrfracevetr=irrfracevetr, irrfracdectr=irrfracdectr, \
            irrfracgrass=irrfracgrass, irrfracbsoil=irrfracbsoil, \
            irrfracwater=irrfracwater, dayofweek_id=dayofweek_id, \
            wuprofa_24hr=wuprofa_24hr, wuprofm_24hr=wuprofm_24hr, \
            internalwateruse_h=internalwateruse_h, hdd_id=hdd_id, wuday_id=wuday_id, \
            waterusemethod=waterusemethod, nsh=nsh, it=it, imin=imin, dls=dls, \
            wu_surf=wu_surf)
        return wu_int, wu_ext
    
    @staticmethod
    def suews_cal_wateruse_dts(nsh_real, wu_m3, surfacearea, sfr_paved, sfr_bldg, \
        sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, irrfracpaved, \
        irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, irrfracbsoil, \
        irrfracwater, dayofweek_id, wuprofa_24hr_working, wuprofa_24hr_holiday, \
        wuprofm_24hr_working, wuprofm_24hr_holiday, internalwateruse_h, hdd_id, \
        wuday_id, waterusemethod, nsh, it, imin, dls, wu_surf):
        """
        wu_int, wu_ext = suews_cal_wateruse_dts(nsh_real, wu_m3, surfacearea, sfr_paved, \
            sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
            irrfracpaved, irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, \
            irrfracbsoil, irrfracwater, dayofweek_id, wuprofa_24hr_working, \
            wuprofa_24hr_holiday, wuprofm_24hr_working, wuprofm_24hr_holiday, \
            internalwateruse_h, hdd_id, wuday_id, waterusemethod, nsh, it, imin, dls, \
            wu_surf)
        
        
        Defined at suews_phys_waterdist.fpp lines 1585-1759
        
        Parameters
        ----------
        nsh_real : float
        wu_m3 : float
        surfacearea : float
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        irrfracpaved : float
        irrfracbldgs : float
        irrfracevetr : float
        irrfracdectr : float
        irrfracgrass : float
        irrfracbsoil : float
        irrfracwater : float
        dayofweek_id : int array
        wuprofa_24hr_working : float array
        wuprofa_24hr_holiday : float array
        wuprofm_24hr_working : float array
        wuprofm_24hr_holiday : float array
        internalwateruse_h : float
        hdd_id : float array
        wuday_id : float array
        waterusemethod : int
        nsh : int
        it : int
        imin : int
        dls : int
        wu_surf : float array
        
        Returns
        -------
        wu_int : float
        wu_ext : float
        
        """
        wu_int, wu_ext = _supy_driver.f90wrap_suews_cal_wateruse_dts(nsh_real=nsh_real, \
            wu_m3=wu_m3, surfacearea=surfacearea, sfr_paved=sfr_paved, \
            sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, \
            sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, \
            irrfracpaved=irrfracpaved, irrfracbldgs=irrfracbldgs, \
            irrfracevetr=irrfracevetr, irrfracdectr=irrfracdectr, \
            irrfracgrass=irrfracgrass, irrfracbsoil=irrfracbsoil, \
            irrfracwater=irrfracwater, dayofweek_id=dayofweek_id, \
            wuprofa_24hr_working=wuprofa_24hr_working, \
            wuprofa_24hr_holiday=wuprofa_24hr_holiday, \
            wuprofm_24hr_working=wuprofm_24hr_working, \
            wuprofm_24hr_holiday=wuprofm_24hr_holiday, \
            internalwateruse_h=internalwateruse_h, hdd_id=hdd_id, wuday_id=wuday_id, \
            waterusemethod=waterusemethod, nsh=nsh, it=it, imin=imin, dls=dls, \
            wu_surf=wu_surf)
        return wu_int, wu_ext
    
    _dt_array_initialisers = []
    

waterdist_module = Waterdist_Module()

class Resist_Module(f90wrap.runtime.FortranModule):
    """
    Module resist_module
    
    
    Defined at suews_phys_resist.fpp lines 5-669
    
    """
    @staticmethod
    def aerodynamicresistance(zzd, z0m, avu1, l_mod, ustar, vegfraction, \
        aerodynamicresistancemethod, stabilitymethod, roughlenheatmethod):
        """
        ra_h, z0v = aerodynamicresistance(zzd, z0m, avu1, l_mod, ustar, vegfraction, \
            aerodynamicresistancemethod, stabilitymethod, roughlenheatmethod)
        
        
        Defined at suews_phys_resist.fpp lines 18-101
        
        Parameters
        ----------
        zzd : float
        z0m : float
        avu1 : float
        l_mod : float
        ustar : float
        vegfraction : float
        aerodynamicresistancemethod : int
        stabilitymethod : int
        roughlenheatmethod : int
        
        Returns
        -------
        ra_h : float
        z0v : float
        
        """
        ra_h, z0v = _supy_driver.f90wrap_aerodynamicresistance(zzd=zzd, z0m=z0m, \
            avu1=avu1, l_mod=l_mod, ustar=ustar, vegfraction=vegfraction, \
            aerodynamicresistancemethod=aerodynamicresistancemethod, \
            stabilitymethod=stabilitymethod, roughlenheatmethod=roughlenheatmethod)
        return ra_h, z0v
    
    @staticmethod
    def surfaceresistance(id, it, smdmethod, snowfrac, sfr_surf, avkdn, temp_c, dq, \
        xsmd, vsmd, maxconductance, laimax, lai_id, gsmodel, kmax, g_max, g_k, \
        g_q_base, g_q_shape, g_t, g_sm, th, tl, s1, s2):
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, gfunc, gsc, rs = surfaceresistance(id, it, \
            smdmethod, snowfrac, sfr_surf, avkdn, temp_c, dq, xsmd, vsmd, \
            maxconductance, laimax, lai_id, gsmodel, kmax, g_max, g_k, g_q_base, \
            g_q_shape, g_t, g_sm, th, tl, s1, s2)
        
        
        Defined at suews_phys_resist.fpp lines 103-340
        
        Parameters
        ----------
        id : int
        it : int
        smdmethod : int
        snowfrac : float array
        sfr_surf : float array
        avkdn : float
        temp_c : float
        dq : float
        xsmd : float
        vsmd : float
        maxconductance : float array
        laimax : float array
        lai_id : float array
        gsmodel : int
        kmax : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        th : float
        tl : float
        s1 : float
        s2 : float
        
        Returns
        -------
        g_kdown : float
        g_dq : float
        g_ta : float
        g_smd : float
        g_lai : float
        gfunc : float
        gsc : float
        rs : float
        
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, gfunc, gsc, rs = \
            _supy_driver.f90wrap_surfaceresistance(id=id, it=it, smdmethod=smdmethod, \
            snowfrac=snowfrac, sfr_surf=sfr_surf, avkdn=avkdn, temp_c=temp_c, dq=dq, \
            xsmd=xsmd, vsmd=vsmd, maxconductance=maxconductance, laimax=laimax, \
            lai_id=lai_id, gsmodel=gsmodel, kmax=kmax, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, th=th, tl=tl, \
            s1=s1, s2=s2)
        return g_kdown, g_dq, g_ta, g_smd, g_lai, gfunc, gsc, rs
    
    @staticmethod
    def boundarylayerresistance(zzd, z0m, avu1, ustar):
        """
        rb = boundarylayerresistance(zzd, z0m, avu1, ustar)
        
        
        Defined at suews_phys_resist.fpp lines 342-362
        
        Parameters
        ----------
        zzd : float
        z0m : float
        avu1 : float
        ustar : float
        
        Returns
        -------
        rb : float
        
        """
        rb = _supy_driver.f90wrap_boundarylayerresistance(zzd=zzd, z0m=z0m, avu1=avu1, \
            ustar=ustar)
        return rb
    
    @staticmethod
    def suews_cal_roughnessparameters(roughlenmommethod, faimethod, sfr_surf, \
        surfacearea, bldgh, evetreeh, dectreeh, porosity_dectr, faibldg, faievetree, \
        faidectree, z0m_in, zdm_in, z):
        """
        fai, pai, zh, z0m, zdm, zzd = suews_cal_roughnessparameters(roughlenmommethod, \
            faimethod, sfr_surf, surfacearea, bldgh, evetreeh, dectreeh, porosity_dectr, \
            faibldg, faievetree, faidectree, z0m_in, zdm_in, z)
        
        
        Defined at suews_phys_resist.fpp lines 364-497
        
        Parameters
        ----------
        roughlenmommethod : int
        faimethod : int
        sfr_surf : float array
        surfacearea : float
        bldgh : float
        evetreeh : float
        dectreeh : float
        porosity_dectr : float
        faibldg : float
        faievetree : float
        faidectree : float
        z0m_in : float
        zdm_in : float
        z : float
        
        Returns
        -------
        fai : float
        pai : float
        zh : float
        z0m : float
        zdm : float
        zzd : float
        
        --------------------------------------------------------------------------------
        """
        fai, pai, zh, z0m, zdm, zzd = \
            _supy_driver.f90wrap_suews_cal_roughnessparameters(roughlenmommethod=roughlenmommethod, \
            faimethod=faimethod, sfr_surf=sfr_surf, surfacearea=surfacearea, \
            bldgh=bldgh, evetreeh=evetreeh, dectreeh=dectreeh, \
            porosity_dectr=porosity_dectr, faibldg=faibldg, faievetree=faievetree, \
            faidectree=faidectree, z0m_in=z0m_in, zdm_in=zdm_in, z=z)
        return fai, pai, zh, z0m, zdm, zzd
    
    @staticmethod
    def suews_cal_roughnessparameters_dts(roughlenmommethod, faimethod, sfr_paved, \
        sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
        surfacearea, bldgh, evetreeh, dectreeh, porosity_dectr, faibldg, faievetree, \
        faidectree, z0m_in, zdm_in, z):
        """
        faibldg_use, faievetree_use, faidectree_use, fai, pai, zh, z0m, zdm, zzd = \
            suews_cal_roughnessparameters_dts(roughlenmommethod, faimethod, sfr_paved, \
            sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
            surfacearea, bldgh, evetreeh, dectreeh, porosity_dectr, faibldg, faievetree, \
            faidectree, z0m_in, zdm_in, z)
        
        
        Defined at suews_phys_resist.fpp lines 499-630
        
        Parameters
        ----------
        roughlenmommethod : int
        faimethod : int
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        surfacearea : float
        bldgh : float
        evetreeh : float
        dectreeh : float
        porosity_dectr : float
        faibldg : float
        faievetree : float
        faidectree : float
        z0m_in : float
        zdm_in : float
        z : float
        
        Returns
        -------
        faibldg_use : float
        faievetree_use : float
        faidectree_use : float
        fai : float
        pai : float
        zh : float
        z0m : float
        zdm : float
        zzd : float
        
        --------------------------------------------------------------------------------
        """
        faibldg_use, faievetree_use, faidectree_use, fai, pai, zh, z0m, zdm, zzd = \
            _supy_driver.f90wrap_suews_cal_roughnessparameters_dts(roughlenmommethod=roughlenmommethod, \
            faimethod=faimethod, sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, \
            sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, \
            sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, surfacearea=surfacearea, \
            bldgh=bldgh, evetreeh=evetreeh, dectreeh=dectreeh, \
            porosity_dectr=porosity_dectr, faibldg=faibldg, faievetree=faievetree, \
            faidectree=faidectree, z0m_in=z0m_in, zdm_in=zdm_in, z=z)
        return faibldg_use, faievetree_use, faidectree_use, fai, pai, zh, z0m, zdm, zzd
    
    @staticmethod
    def cal_z0v(roughlenheatmethod, z0m, vegfraction, ustar):
        """
        z0v = cal_z0v(roughlenheatmethod, z0m, vegfraction, ustar)
        
        
        Defined at suews_phys_resist.fpp lines 632-663
        
        Parameters
        ----------
        roughlenheatmethod : int
        z0m : float
        vegfraction : float
        ustar : float
        
        Returns
        -------
        z0v : float
        
        """
        z0v = _supy_driver.f90wrap_cal_z0v(roughlenheatmethod=roughlenheatmethod, \
            z0m=z0m, vegfraction=vegfraction, ustar=ustar)
        return z0v
    
    @staticmethod
    def sigmoid(x):
        """
        res = sigmoid(x)
        
        
        Defined at suews_phys_resist.fpp lines 665-669
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        res : float
        
        """
        res = _supy_driver.f90wrap_sigmoid(x=x)
        return res
    
    _dt_array_initialisers = []
    

resist_module = Resist_Module()

class Evap_Module(f90wrap.runtime.FortranModule):
    """
    Module evap_module
    
    
    Defined at suews_phys_evap.fpp lines 5-146
    
    """
    @staticmethod
    def cal_evap(evapmethod, state_is, wetthresh_is, capstore_is, vpd_hpa, avdens, \
        avcp, qn_e, s_hpa, psyc_hpa, rs, ra, rb, tlv):
        """
        rss, ev, qe = cal_evap(evapmethod, state_is, wetthresh_is, capstore_is, vpd_hpa, \
            avdens, avcp, qn_e, s_hpa, psyc_hpa, rs, ra, rb, tlv)
        
        
        Defined at suews_phys_evap.fpp lines 11-106
        
        Parameters
        ----------
        evapmethod : int
        state_is : float
        wetthresh_is : float
        capstore_is : float
        vpd_hpa : float
        avdens : float
        avcp : float
        qn_e : float
        s_hpa : float
        psyc_hpa : float
        rs : float
        ra : float
        rb : float
        tlv : float
        
        Returns
        -------
        rss : float
        ev : float
        qe : float
        
        ------------------------------------------------------------------------------
        -Calculates evaporation for each surface from modified Penman-Monteith eqn
        -State determines whether each surface type is dry or wet(wet/transition)
        -Wet surfaces below storage capacity are in transition
         and QE depends on the state and storage capacity(i.e. varies with surface);
         for wet or dry surfaces QE does not vary between surface types
        -See Sect 2.4 of Jarvi et al. (2011) Ja11
        Last modified:
          HCW 06 Jul 2016
           Moved rss declaration to LUMPS_Module_Constants so it can be written out
          HCW 11 Jun 2015
           Added WetThresh to distinguish wet/partially wet surfaces from the storage \
               capacities used in SUEWS_drain
          HCW 30 Jan 2015
           Removed StorCap input because it is provided by module allocateArray
           Tidied and commented code
          LJ 10/2010
        ------------------------------------------------------------------------------
        """
        rss, ev, qe = _supy_driver.f90wrap_cal_evap(evapmethod=evapmethod, \
            state_is=state_is, wetthresh_is=wetthresh_is, capstore_is=capstore_is, \
            vpd_hpa=vpd_hpa, avdens=avdens, avcp=avcp, qn_e=qn_e, s_hpa=s_hpa, \
            psyc_hpa=psyc_hpa, rs=rs, ra=ra, rb=rb, tlv=tlv)
        return rss, ev, qe
    
    @staticmethod
    def cal_evap_multi(evapmethod, sfr_multi, state_multi, wetthresh_multi, \
        capstore_multi, vpd_hpa, avdens, avcp, qn_e_multi, s_hpa, psyc_hpa, rs, ra, \
        rb, tlv, rss_multi, ev_multi, qe_multi):
        """
        cal_evap_multi(evapmethod, sfr_multi, state_multi, wetthresh_multi, \
            capstore_multi, vpd_hpa, avdens, avcp, qn_e_multi, s_hpa, psyc_hpa, rs, ra, \
            rb, tlv, rss_multi, ev_multi, qe_multi)
        
        
        Defined at suews_phys_evap.fpp lines 108-146
        
        Parameters
        ----------
        evapmethod : int
        sfr_multi : float array
        state_multi : float array
        wetthresh_multi : float array
        capstore_multi : float array
        vpd_hpa : float
        avdens : float
        avcp : float
        qn_e_multi : float array
        s_hpa : float
        psyc_hpa : float
        rs : float
        ra : float
        rb : float
        tlv : float
        rss_multi : float array
        ev_multi : float array
        qe_multi : float array
        
        """
        _supy_driver.f90wrap_cal_evap_multi(evapmethod=evapmethod, sfr_multi=sfr_multi, \
            state_multi=state_multi, wetthresh_multi=wetthresh_multi, \
            capstore_multi=capstore_multi, vpd_hpa=vpd_hpa, avdens=avdens, avcp=avcp, \
            qn_e_multi=qn_e_multi, s_hpa=s_hpa, psyc_hpa=psyc_hpa, rs=rs, ra=ra, rb=rb, \
            tlv=tlv, rss_multi=rss_multi, ev_multi=ev_multi, qe_multi=qe_multi)
    
    _dt_array_initialisers = []
    

evap_module = Evap_Module()

class Dailystate_Module(f90wrap.runtime.FortranModule):
    """
    Module dailystate_module
    
    
    Defined at suews_phys_dailystate.fpp lines 5-1307
    
    """
    @staticmethod
    def suews_cal_dailystate(iy, id, it, imin, isec, tstep, tstep_prev, \
        dt_since_start, dayofweek_id, tmin_id_prev, tmax_id_prev, lenday_id_prev, \
        basetmethod, waterusemethod, ie_start, ie_end, laicalcyes, laitype, \
        nsh_real, avkdn, temp_c, precip, baset_hc, baset_heating, baset_cooling, \
        lat, faut, lai_obs, albmax_dectr, albmax_evetr, albmax_grass, albmin_dectr, \
        albmin_evetr, albmin_grass, capmax_dec, capmin_dec, pormax_dec, pormin_dec, \
        ie_a, ie_m, daywatper, daywat, baset, basete, gddfull, sddfull, laimin, \
        laimax, laipower, decidcap_id_prev, storedrainprm_prev, lai_id_prev, \
        gdd_id_prev, sdd_id_prev, albdectr_id_prev, albevetr_id_prev, \
        albgrass_id_prev, porosity_id_prev, hdd_id_prev, state_id, soilstore_id, \
        soilstorecap, h_maintain, hdd_id_next, porosity_id_next, storedrainprm_next, \
        lai_id_next, gdd_id_next, sdd_id_next, wuday_id):
        """
        tmin_id_next, tmax_id_next, lenday_id_next, albdectr_id_next, albevetr_id_next, \
            albgrass_id_next, decidcap_id_next = suews_cal_dailystate(iy, id, it, imin, \
            isec, tstep, tstep_prev, dt_since_start, dayofweek_id, tmin_id_prev, \
            tmax_id_prev, lenday_id_prev, basetmethod, waterusemethod, ie_start, ie_end, \
            laicalcyes, laitype, nsh_real, avkdn, temp_c, precip, baset_hc, \
            baset_heating, baset_cooling, lat, faut, lai_obs, albmax_dectr, \
            albmax_evetr, albmax_grass, albmin_dectr, albmin_evetr, albmin_grass, \
            capmax_dec, capmin_dec, pormax_dec, pormin_dec, ie_a, ie_m, daywatper, \
            daywat, baset, basete, gddfull, sddfull, laimin, laimax, laipower, \
            decidcap_id_prev, storedrainprm_prev, lai_id_prev, gdd_id_prev, sdd_id_prev, \
            albdectr_id_prev, albevetr_id_prev, albgrass_id_prev, porosity_id_prev, \
            hdd_id_prev, state_id, soilstore_id, soilstorecap, h_maintain, hdd_id_next, \
            porosity_id_next, storedrainprm_next, lai_id_next, gdd_id_next, sdd_id_next, \
            wuday_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 79-350
        
        Parameters
        ----------
        iy : int
        id : int
        it : int
        imin : int
        isec : int
        tstep : int
        tstep_prev : int
        dt_since_start : int
        dayofweek_id : int array
        tmin_id_prev : float
        tmax_id_prev : float
        lenday_id_prev : float
        basetmethod : int
        waterusemethod : int
        ie_start : int
        ie_end : int
        laicalcyes : int
        laitype : int array
        nsh_real : float
        avkdn : float
        temp_c : float
        precip : float
        baset_hc : float
        baset_heating : float array
        baset_cooling : float array
        lat : float
        faut : float
        lai_obs : float
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        capmax_dec : float
        capmin_dec : float
        pormax_dec : float
        pormin_dec : float
        ie_a : float array
        ie_m : float array
        daywatper : float array
        	of houses following daily water
        
        daywat : float array
        baset : float array
        basete : float array
        gddfull : float array
        sddfull : float array
        laimin : float array
        laimax : float array
        laipower : float array
        decidcap_id_prev : float
        storedrainprm_prev : float array
        lai_id_prev : float array
        gdd_id_prev : float array
        sdd_id_prev : float array
        albdectr_id_prev : float
        albevetr_id_prev : float
        albgrass_id_prev : float
        porosity_id_prev : float
        hdd_id_prev : float array
        state_id : float array
        soilstore_id : float array
        soilstorecap : float array
        h_maintain : float
        hdd_id_next : float array
        porosity_id_next : float
        storedrainprm_next : float array
        lai_id_next : float array
        gdd_id_next : float array
        sdd_id_next : float array
        wuday_id : float array
        
        Returns
        -------
        tmin_id_next : float
        tmax_id_next : float
        lenday_id_next : float
        albdectr_id_next : float
        albevetr_id_next : float
        albgrass_id_next : float
        decidcap_id_next : float
        
        """
        tmin_id_next, tmax_id_next, lenday_id_next, albdectr_id_next, albevetr_id_next, \
            albgrass_id_next, decidcap_id_next = \
            _supy_driver.f90wrap_suews_cal_dailystate(iy=iy, id=id, it=it, imin=imin, \
            isec=isec, tstep=tstep, tstep_prev=tstep_prev, \
            dt_since_start=dt_since_start, dayofweek_id=dayofweek_id, \
            tmin_id_prev=tmin_id_prev, tmax_id_prev=tmax_id_prev, \
            lenday_id_prev=lenday_id_prev, basetmethod=basetmethod, \
            waterusemethod=waterusemethod, ie_start=ie_start, ie_end=ie_end, \
            laicalcyes=laicalcyes, laitype=laitype, nsh_real=nsh_real, avkdn=avkdn, \
            temp_c=temp_c, precip=precip, baset_hc=baset_hc, \
            baset_heating=baset_heating, baset_cooling=baset_cooling, lat=lat, \
            faut=faut, lai_obs=lai_obs, albmax_dectr=albmax_dectr, \
            albmax_evetr=albmax_evetr, albmax_grass=albmax_grass, \
            albmin_dectr=albmin_dectr, albmin_evetr=albmin_evetr, \
            albmin_grass=albmin_grass, capmax_dec=capmax_dec, capmin_dec=capmin_dec, \
            pormax_dec=pormax_dec, pormin_dec=pormin_dec, ie_a=ie_a, ie_m=ie_m, \
            daywatper=daywatper, daywat=daywat, baset=baset, basete=basete, \
            gddfull=gddfull, sddfull=sddfull, laimin=laimin, laimax=laimax, \
            laipower=laipower, decidcap_id_prev=decidcap_id_prev, \
            storedrainprm_prev=storedrainprm_prev, lai_id_prev=lai_id_prev, \
            gdd_id_prev=gdd_id_prev, sdd_id_prev=sdd_id_prev, \
            albdectr_id_prev=albdectr_id_prev, albevetr_id_prev=albevetr_id_prev, \
            albgrass_id_prev=albgrass_id_prev, porosity_id_prev=porosity_id_prev, \
            hdd_id_prev=hdd_id_prev, state_id=state_id, soilstore_id=soilstore_id, \
            soilstorecap=soilstorecap, h_maintain=h_maintain, hdd_id_next=hdd_id_next, \
            porosity_id_next=porosity_id_next, storedrainprm_next=storedrainprm_next, \
            lai_id_next=lai_id_next, gdd_id_next=gdd_id_next, sdd_id_next=sdd_id_next, \
            wuday_id=wuday_id)
        return tmin_id_next, tmax_id_next, lenday_id_next, albdectr_id_next, \
            albevetr_id_next, albgrass_id_next, decidcap_id_next
    
    @staticmethod
    def suews_cal_dailystate_dts(iy, id, it, imin, isec, tstep, tstep_prev, \
        dt_since_start, dayofweek_id, tmin_id_prev, tmax_id_prev, lenday_id_prev, \
        basetmethod, waterusemethod, ie_start, ie_end, laicalcyes, evetrlaitype, \
        dectrlaitype, grasslaitype, nsh_real, avkdn, temp_c, precip, baset_hc, \
        baset_heating_working, baset_heating_holiday, baset_cooling_working, \
        baset_cooling_holiday, lat, faut, lai_obs, albmax_evetr, albmax_dectr, \
        albmax_grass, albmin_evetr, albmin_dectr, albmin_grass, capmax_dec, \
        capmin_dec, pormax_dec, pormin_dec, ie_a, ie_m, daywatper_mon, \
        daywatper_tues, daywatper_wed, daywatper_thur, daywatper_fri, daywatper_sat, \
        daywatper_sun, daywat_mon, daywat_tues, daywat_wed, daywat_thur, daywat_fri, \
        daywat_sat, daywat_sun, evetrbaset, dectrbaset, grassbaset, evetrbasete, \
        dectrbasete, grassbasete, evetrgddfull, dectrgddfull, grassgddfull, \
        evetrsddfull, dectrsddfull, grasssddfull, evetrlaimin, dectrlaimin, \
        grasslaimin, evetrlaimax, dectrlaimax, grasslaimax, evetrlaipower, \
        dectrlaipower, grasslaipower, decidcap_id_prev, storedrainprm_prev, \
        lai_id_prev, gdd_id_prev, sdd_id_prev, albdectr_id_prev, albevetr_id_prev, \
        albgrass_id_prev, porosity_id_prev, hdd_id_prev, state_id, soilstore_id, \
        soilstorecap, h_maintain, hdd_id_next, porosity_id_next, storedrainprm_next, \
        lai_id_next, gdd_id_next, sdd_id_next, wuday_id):
        """
        tmin_id_next, tmax_id_next, lenday_id_next, albdectr_id_next, albevetr_id_next, \
            albgrass_id_next, decidcap_id_next = suews_cal_dailystate_dts(iy, id, it, \
            imin, isec, tstep, tstep_prev, dt_since_start, dayofweek_id, tmin_id_prev, \
            tmax_id_prev, lenday_id_prev, basetmethod, waterusemethod, ie_start, ie_end, \
            laicalcyes, evetrlaitype, dectrlaitype, grasslaitype, nsh_real, avkdn, \
            temp_c, precip, baset_hc, baset_heating_working, baset_heating_holiday, \
            baset_cooling_working, baset_cooling_holiday, lat, faut, lai_obs, \
            albmax_evetr, albmax_dectr, albmax_grass, albmin_evetr, albmin_dectr, \
            albmin_grass, capmax_dec, capmin_dec, pormax_dec, pormin_dec, ie_a, ie_m, \
            daywatper_mon, daywatper_tues, daywatper_wed, daywatper_thur, daywatper_fri, \
            daywatper_sat, daywatper_sun, daywat_mon, daywat_tues, daywat_wed, \
            daywat_thur, daywat_fri, daywat_sat, daywat_sun, evetrbaset, dectrbaset, \
            grassbaset, evetrbasete, dectrbasete, grassbasete, evetrgddfull, \
            dectrgddfull, grassgddfull, evetrsddfull, dectrsddfull, grasssddfull, \
            evetrlaimin, dectrlaimin, grasslaimin, evetrlaimax, dectrlaimax, \
            grasslaimax, evetrlaipower, dectrlaipower, grasslaipower, decidcap_id_prev, \
            storedrainprm_prev, lai_id_prev, gdd_id_prev, sdd_id_prev, albdectr_id_prev, \
            albevetr_id_prev, albgrass_id_prev, porosity_id_prev, hdd_id_prev, state_id, \
            soilstore_id, soilstorecap, h_maintain, hdd_id_next, porosity_id_next, \
            storedrainprm_next, lai_id_next, gdd_id_next, sdd_id_next, wuday_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 352-694
        
        Parameters
        ----------
        iy : int
        id : int
        it : int
        imin : int
        isec : int
        tstep : int
        tstep_prev : int
        dt_since_start : int
        dayofweek_id : int array
        tmin_id_prev : float
        tmax_id_prev : float
        lenday_id_prev : float
        basetmethod : int
        waterusemethod : int
        ie_start : int
        ie_end : int
        laicalcyes : int
        evetrlaitype : int
        dectrlaitype : int
        grasslaitype : int
        nsh_real : float
        avkdn : float
        temp_c : float
        precip : float
        baset_hc : float
        baset_heating_working : float
        baset_heating_holiday : float
        baset_cooling_working : float
        baset_cooling_holiday : float
        lat : float
        faut : float
        lai_obs : float
        albmax_evetr : float
        albmax_dectr : float
        albmax_grass : float
        albmin_evetr : float
        albmin_dectr : float
        albmin_grass : float
        capmax_dec : float
        capmin_dec : float
        pormax_dec : float
        pormin_dec : float
        ie_a : float array
        ie_m : float array
        daywatper_mon : float
        daywatper_tues : float
        daywatper_wed : float
        daywatper_thur : float
        daywatper_fri : float
        daywatper_sat : float
        daywatper_sun : float
        daywat_mon : float
        daywat_tues : float
        daywat_wed : float
        daywat_thur : float
        daywat_fri : float
        daywat_sat : float
        daywat_sun : float
        evetrbaset : float
        dectrbaset : float
        grassbaset : float
        evetrbasete : float
        dectrbasete : float
        grassbasete : float
        evetrgddfull : float
        dectrgddfull : float
        grassgddfull : float
        evetrsddfull : float
        dectrsddfull : float
        grasssddfull : float
        evetrlaimin : float
        dectrlaimin : float
        grasslaimin : float
        evetrlaimax : float
        dectrlaimax : float
        grasslaimax : float
        evetrlaipower : float array
        dectrlaipower : float array
        grasslaipower : float array
        decidcap_id_prev : float
        storedrainprm_prev : float array
        lai_id_prev : float array
        gdd_id_prev : float array
        sdd_id_prev : float array
        albdectr_id_prev : float
        albevetr_id_prev : float
        albgrass_id_prev : float
        porosity_id_prev : float
        hdd_id_prev : float array
        state_id : float array
        soilstore_id : float array
        soilstorecap : float array
        h_maintain : float
        hdd_id_next : float array
        porosity_id_next : float
        storedrainprm_next : float array
        lai_id_next : float array
        gdd_id_next : float array
        sdd_id_next : float array
        wuday_id : float array
        
        Returns
        -------
        tmin_id_next : float
        tmax_id_next : float
        lenday_id_next : float
        albdectr_id_next : float
        albevetr_id_next : float
        albgrass_id_next : float
        decidcap_id_next : float
        
        """
        tmin_id_next, tmax_id_next, lenday_id_next, albdectr_id_next, albevetr_id_next, \
            albgrass_id_next, decidcap_id_next = \
            _supy_driver.f90wrap_suews_cal_dailystate_dts(iy=iy, id=id, it=it, \
            imin=imin, isec=isec, tstep=tstep, tstep_prev=tstep_prev, \
            dt_since_start=dt_since_start, dayofweek_id=dayofweek_id, \
            tmin_id_prev=tmin_id_prev, tmax_id_prev=tmax_id_prev, \
            lenday_id_prev=lenday_id_prev, basetmethod=basetmethod, \
            waterusemethod=waterusemethod, ie_start=ie_start, ie_end=ie_end, \
            laicalcyes=laicalcyes, evetrlaitype=evetrlaitype, dectrlaitype=dectrlaitype, \
            grasslaitype=grasslaitype, nsh_real=nsh_real, avkdn=avkdn, temp_c=temp_c, \
            precip=precip, baset_hc=baset_hc, \
            baset_heating_working=baset_heating_working, \
            baset_heating_holiday=baset_heating_holiday, \
            baset_cooling_working=baset_cooling_working, \
            baset_cooling_holiday=baset_cooling_holiday, lat=lat, faut=faut, \
            lai_obs=lai_obs, albmax_evetr=albmax_evetr, albmax_dectr=albmax_dectr, \
            albmax_grass=albmax_grass, albmin_evetr=albmin_evetr, \
            albmin_dectr=albmin_dectr, albmin_grass=albmin_grass, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, pormax_dec=pormax_dec, pormin_dec=pormin_dec, \
            ie_a=ie_a, ie_m=ie_m, daywatper_mon=daywatper_mon, \
            daywatper_tues=daywatper_tues, daywatper_wed=daywatper_wed, \
            daywatper_thur=daywatper_thur, daywatper_fri=daywatper_fri, \
            daywatper_sat=daywatper_sat, daywatper_sun=daywatper_sun, \
            daywat_mon=daywat_mon, daywat_tues=daywat_tues, daywat_wed=daywat_wed, \
            daywat_thur=daywat_thur, daywat_fri=daywat_fri, daywat_sat=daywat_sat, \
            daywat_sun=daywat_sun, evetrbaset=evetrbaset, dectrbaset=dectrbaset, \
            grassbaset=grassbaset, evetrbasete=evetrbasete, dectrbasete=dectrbasete, \
            grassbasete=grassbasete, evetrgddfull=evetrgddfull, \
            dectrgddfull=dectrgddfull, grassgddfull=grassgddfull, \
            evetrsddfull=evetrsddfull, dectrsddfull=dectrsddfull, \
            grasssddfull=grasssddfull, evetrlaimin=evetrlaimin, dectrlaimin=dectrlaimin, \
            grasslaimin=grasslaimin, evetrlaimax=evetrlaimax, dectrlaimax=dectrlaimax, \
            grasslaimax=grasslaimax, evetrlaipower=evetrlaipower, \
            dectrlaipower=dectrlaipower, grasslaipower=grasslaipower, \
            decidcap_id_prev=decidcap_id_prev, storedrainprm_prev=storedrainprm_prev, \
            lai_id_prev=lai_id_prev, gdd_id_prev=gdd_id_prev, sdd_id_prev=sdd_id_prev, \
            albdectr_id_prev=albdectr_id_prev, albevetr_id_prev=albevetr_id_prev, \
            albgrass_id_prev=albgrass_id_prev, porosity_id_prev=porosity_id_prev, \
            hdd_id_prev=hdd_id_prev, state_id=state_id, soilstore_id=soilstore_id, \
            soilstorecap=soilstorecap, h_maintain=h_maintain, hdd_id_next=hdd_id_next, \
            porosity_id_next=porosity_id_next, storedrainprm_next=storedrainprm_next, \
            lai_id_next=lai_id_next, gdd_id_next=gdd_id_next, sdd_id_next=sdd_id_next, \
            wuday_id=wuday_id)
        return tmin_id_next, tmax_id_next, lenday_id_next, albdectr_id_next, \
            albevetr_id_next, albgrass_id_next, decidcap_id_next
    
    @staticmethod
    def update_dailystate_end(id, it, imin, tstep, dt_since_start, tmin_id, tmax_id, \
        lenday_id, laitype, ie_end, ie_start, laicalcyes, waterusemethod, \
        dayofweek_id, albmax_dectr, albmax_evetr, albmax_grass, albmin_dectr, \
        albmin_evetr, albmin_grass, baset, basete, capmax_dec, capmin_dec, daywat, \
        daywatper, faut, gddfull, ie_a, ie_m, laimax, laimin, laipower, lat, \
        pormax_dec, pormin_dec, sddfull, lai_obs, state_id, soilstore_id, \
        soilstorecap, h_maintain, gdd_id, sdd_id, hdd_id, lai_id, decidcap_id, \
        albdectr_id, albevetr_id, albgrass_id, porosity_id, storedrainprm, \
        wuday_id):
        """
        update_dailystate_end(id, it, imin, tstep, dt_since_start, tmin_id, tmax_id, \
            lenday_id, laitype, ie_end, ie_start, laicalcyes, waterusemethod, \
            dayofweek_id, albmax_dectr, albmax_evetr, albmax_grass, albmin_dectr, \
            albmin_evetr, albmin_grass, baset, basete, capmax_dec, capmin_dec, daywat, \
            daywatper, faut, gddfull, ie_a, ie_m, laimax, laimin, laipower, lat, \
            pormax_dec, pormin_dec, sddfull, lai_obs, state_id, soilstore_id, \
            soilstorecap, h_maintain, gdd_id, sdd_id, hdd_id, lai_id, decidcap_id, \
            albdectr_id, albevetr_id, albgrass_id, porosity_id, storedrainprm, wuday_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 696-809
        
        Parameters
        ----------
        id : int
        it : int
        imin : int
        tstep : int
        dt_since_start : int
        tmin_id : float
        tmax_id : float
        lenday_id : float
        laitype : int array
        ie_end : int
        ie_start : int
        laicalcyes : int
        waterusemethod : int
        dayofweek_id : int array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        baset : float array
        basete : float array
        capmax_dec : float
        capmin_dec : float
        daywat : float array
        daywatper : float array
        faut : float
        gddfull : float array
        ie_a : float array
        ie_m : float array
        laimax : float array
        laimin : float array
        laipower : float array
        lat : float
        pormax_dec : float
        pormin_dec : float
        sddfull : float array
        lai_obs : float
        state_id : float array
        soilstore_id : float array
        soilstorecap : float array
        h_maintain : float
        gdd_id : float array
        sdd_id : float array
        hdd_id : float array
        lai_id : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        storedrainprm : float array
        wuday_id : float array
        
        ------------------------------------------------------------------------------
         Calculation of LAI from growing degree days
         This was revised and checked on 16 Feb 2014 by LJ
        ------------------------------------------------------------------------------
         save initial LAI_id
        """
        _supy_driver.f90wrap_update_dailystate_end(id=id, it=it, imin=imin, tstep=tstep, \
            dt_since_start=dt_since_start, tmin_id=tmin_id, tmax_id=tmax_id, \
            lenday_id=lenday_id, laitype=laitype, ie_end=ie_end, ie_start=ie_start, \
            laicalcyes=laicalcyes, waterusemethod=waterusemethod, \
            dayofweek_id=dayofweek_id, albmax_dectr=albmax_dectr, \
            albmax_evetr=albmax_evetr, albmax_grass=albmax_grass, \
            albmin_dectr=albmin_dectr, albmin_evetr=albmin_evetr, \
            albmin_grass=albmin_grass, baset=baset, basete=basete, \
            capmax_dec=capmax_dec, capmin_dec=capmin_dec, daywat=daywat, \
            daywatper=daywatper, faut=faut, gddfull=gddfull, ie_a=ie_a, ie_m=ie_m, \
            laimax=laimax, laimin=laimin, laipower=laipower, lat=lat, \
            pormax_dec=pormax_dec, pormin_dec=pormin_dec, sddfull=sddfull, \
            lai_obs=lai_obs, state_id=state_id, soilstore_id=soilstore_id, \
            soilstorecap=soilstorecap, h_maintain=h_maintain, gdd_id=gdd_id, \
            sdd_id=sdd_id, hdd_id=hdd_id, lai_id=lai_id, decidcap_id=decidcap_id, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            porosity_id=porosity_id, storedrainprm=storedrainprm, wuday_id=wuday_id)
    
    @staticmethod
    def update_dailystate_day(basetmethod, dayofweek_id, avkdn, temp_c, precip, \
        baset_hc, baset_heating, baset_cooling, nsh_real, tmin_id, tmax_id, \
        lenday_id, hdd_id):
        """
        update_dailystate_day(basetmethod, dayofweek_id, avkdn, temp_c, precip, \
            baset_hc, baset_heating, baset_cooling, nsh_real, tmin_id, tmax_id, \
            lenday_id, hdd_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 811-879
        
        Parameters
        ----------
        basetmethod : int
        dayofweek_id : int array
        avkdn : float
        temp_c : float
        precip : float
        baset_hc : float
        baset_heating : float array
        baset_cooling : float array
        nsh_real : float
        tmin_id : float
        tmax_id : float
        lenday_id : float
        hdd_id : float array
        
        """
        _supy_driver.f90wrap_update_dailystate_day(basetmethod=basetmethod, \
            dayofweek_id=dayofweek_id, avkdn=avkdn, temp_c=temp_c, precip=precip, \
            baset_hc=baset_hc, baset_heating=baset_heating, baset_cooling=baset_cooling, \
            nsh_real=nsh_real, tmin_id=tmin_id, tmax_id=tmax_id, lenday_id=lenday_id, \
            hdd_id=hdd_id)
    
    @staticmethod
    def update_veg(laimax, laimin, albmax_dectr, albmax_evetr, albmax_grass, \
        albmin_dectr, albmin_evetr, albmin_grass, capmax_dec, capmin_dec, \
        pormax_dec, pormin_dec, lai_id, lai_id_prev, decidcap_id, albdectr_id, \
        albevetr_id, albgrass_id, porosity_id, storedrainprm):
        """
        update_veg(laimax, laimin, albmax_dectr, albmax_evetr, albmax_grass, \
            albmin_dectr, albmin_evetr, albmin_grass, capmax_dec, capmin_dec, \
            pormax_dec, pormin_dec, lai_id, lai_id_prev, decidcap_id, albdectr_id, \
            albevetr_id, albgrass_id, porosity_id, storedrainprm)
        
        
        Defined at suews_phys_dailystate.fpp lines 881-964
        
        Parameters
        ----------
        laimax : float array
        laimin : float array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        capmax_dec : float
        capmin_dec : float
        pormax_dec : float
        pormin_dec : float
        lai_id : float array
        lai_id_prev : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        storedrainprm : float array
        
        """
        _supy_driver.f90wrap_update_veg(laimax=laimax, laimin=laimin, \
            albmax_dectr=albmax_dectr, albmax_evetr=albmax_evetr, \
            albmax_grass=albmax_grass, albmin_dectr=albmin_dectr, \
            albmin_evetr=albmin_evetr, albmin_grass=albmin_grass, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, pormax_dec=pormax_dec, pormin_dec=pormin_dec, \
            lai_id=lai_id, lai_id_prev=lai_id_prev, decidcap_id=decidcap_id, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            porosity_id=porosity_id, storedrainprm=storedrainprm)
    
    @staticmethod
    def update_gddlai(id, laicalcyes, lat, lai_obs, tmin_id_prev, tmax_id_prev, \
        lenday_id_prev, baset, basete, gddfull, sddfull, laimin, laimax, laipower, \
        laitype, lai_id_prev, gdd_id, sdd_id, lai_id_next):
        """
        update_gddlai(id, laicalcyes, lat, lai_obs, tmin_id_prev, tmax_id_prev, \
            lenday_id_prev, baset, basete, gddfull, sddfull, laimin, laimax, laipower, \
            laitype, lai_id_prev, gdd_id, sdd_id, lai_id_next)
        
        
        Defined at suews_phys_dailystate.fpp lines 966-1102
        
        Parameters
        ----------
        id : int
        laicalcyes : int
        lat : float
        lai_obs : float
        tmin_id_prev : float
        tmax_id_prev : float
        lenday_id_prev : float
        baset : float array
        basete : float array
        gddfull : float array
        sddfull : float array
        laimin : float array
        laimax : float array
        laipower : float array
        laitype : int array
        lai_id_prev : float array
        gdd_id : float array
        sdd_id : float array
        lai_id_next : float array
        
        ------------------------------------------------------------------------------
         Calculation of LAI from growing degree days
         This was revised and checked on 16 Feb 2014 by LJ
        ------------------------------------------------------------------------------
        """
        _supy_driver.f90wrap_update_gddlai(id=id, laicalcyes=laicalcyes, lat=lat, \
            lai_obs=lai_obs, tmin_id_prev=tmin_id_prev, tmax_id_prev=tmax_id_prev, \
            lenday_id_prev=lenday_id_prev, baset=baset, basete=basete, gddfull=gddfull, \
            sddfull=sddfull, laimin=laimin, laimax=laimax, laipower=laipower, \
            laitype=laitype, lai_id_prev=lai_id_prev, gdd_id=gdd_id, sdd_id=sdd_id, \
            lai_id_next=lai_id_next)
    
    @staticmethod
    def update_wateruse(id, waterusemethod, dayofweek_id, lat, frirriauto, hdd_id, \
        state_id, soilstore_id, soilstorecap, h_maintain, ie_a, ie_m, ie_start, \
        ie_end, daywatper, daywat, wuday_id):
        """
        update_wateruse(id, waterusemethod, dayofweek_id, lat, frirriauto, hdd_id, \
            state_id, soilstore_id, soilstorecap, h_maintain, ie_a, ie_m, ie_start, \
            ie_end, daywatper, daywat, wuday_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 1104-1180
        
        Parameters
        ----------
        id : int
        waterusemethod : int
        dayofweek_id : int array
        lat : float
        frirriauto : float
        hdd_id : float array
        state_id : float array
        soilstore_id : float array
        soilstorecap : float array
        h_maintain : float
        ie_a : float array
        ie_m : float array
        ie_start : int
        ie_end : int
        daywatper : float array
        	of houses following daily water
        
        daywat : float array
        wuday_id : float array
        
        """
        _supy_driver.f90wrap_update_wateruse(id=id, waterusemethod=waterusemethod, \
            dayofweek_id=dayofweek_id, lat=lat, frirriauto=frirriauto, hdd_id=hdd_id, \
            state_id=state_id, soilstore_id=soilstore_id, soilstorecap=soilstorecap, \
            h_maintain=h_maintain, ie_a=ie_a, ie_m=ie_m, ie_start=ie_start, \
            ie_end=ie_end, daywatper=daywatper, daywat=daywat, wuday_id=wuday_id)
    
    @staticmethod
    def update_hdd(dt_since_start, it, imin, tstep, hdd_id):
        """
        update_hdd(dt_since_start, it, imin, tstep, hdd_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 1182-1208
        
        Parameters
        ----------
        dt_since_start : int
        it : int
        imin : int
        tstep : int
        hdd_id : float array
        
        """
        _supy_driver.f90wrap_update_hdd(dt_since_start=dt_since_start, it=it, imin=imin, \
            tstep=tstep, hdd_id=hdd_id)
    
    @staticmethod
    def update_dailystate_start(it, imin, hdd_id):
        """
        update_dailystate_start(it, imin, hdd_id)
        
        
        Defined at suews_phys_dailystate.fpp lines 1210-1229
        
        Parameters
        ----------
        it : int
        imin : int
        hdd_id : float array
        
        """
        _supy_driver.f90wrap_update_dailystate_start(it=it, imin=imin, hdd_id=hdd_id)
    
    @staticmethod
    def suews_update_dailystate(id, datetimeline, gridiv, numberofgrids, \
        dailystateline, dataoutdailystate):
        """
        suews_update_dailystate(id, datetimeline, gridiv, numberofgrids, dailystateline, \
            dataoutdailystate)
        
        
        Defined at suews_phys_dailystate.fpp lines 1231-1245
        
        Parameters
        ----------
        id : int
        datetimeline : float array
        gridiv : int
        numberofgrids : int
        dailystateline : float array
        dataoutdailystate : float array
        
        """
        _supy_driver.f90wrap_suews_update_dailystate(id=id, datetimeline=datetimeline, \
            gridiv=gridiv, numberofgrids=numberofgrids, dailystateline=dailystateline, \
            dataoutdailystate=dataoutdailystate)
    
    @staticmethod
    def update_dailystateline(it, imin, nsh_real, gdd_id, hdd_id, lai_id, sdd_id, \
        tmin_id, tmax_id, lenday_id, decidcap_id, albdectr_id, albevetr_id, \
        albgrass_id, porosity_id, wuday_id, vegphenlumps, snowalb, snowdens, a1, a2, \
        a3, dailystateline):
        """
        update_dailystateline(it, imin, nsh_real, gdd_id, hdd_id, lai_id, sdd_id, \
            tmin_id, tmax_id, lenday_id, decidcap_id, albdectr_id, albevetr_id, \
            albgrass_id, porosity_id, wuday_id, vegphenlumps, snowalb, snowdens, a1, a2, \
            a3, dailystateline)
        
        
        Defined at suews_phys_dailystate.fpp lines 1262-1307
        
        Parameters
        ----------
        it : int
        imin : int
        nsh_real : float
        gdd_id : float array
        hdd_id : float array
        lai_id : float array
        sdd_id : float array
        tmin_id : float
        tmax_id : float
        lenday_id : float
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        wuday_id : float array
        vegphenlumps : float
        snowalb : float
        snowdens : float array
        a1 : float
        a2 : float
        a3 : float
        dailystateline : float array
        
        """
        _supy_driver.f90wrap_update_dailystateline(it=it, imin=imin, nsh_real=nsh_real, \
            gdd_id=gdd_id, hdd_id=hdd_id, lai_id=lai_id, sdd_id=sdd_id, tmin_id=tmin_id, \
            tmax_id=tmax_id, lenday_id=lenday_id, decidcap_id=decidcap_id, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            porosity_id=porosity_id, wuday_id=wuday_id, vegphenlumps=vegphenlumps, \
            snowalb=snowalb, snowdens=snowdens, a1=a1, a2=a2, a3=a3, \
            dailystateline=dailystateline)
    
    _dt_array_initialisers = []
    

dailystate_module = Dailystate_Module()

class Anemsn_Module(f90wrap.runtime.FortranModule):
    """
    Module anemsn_module
    
    
    Defined at suews_phys_anemsn.fpp lines 5-282
    
    """
    @staticmethod
    def anthropogenicemissions(co2pointsource, emissionsmethod, it, imin, dls, \
        dayofweek_id, ef_umolco2perj, fcef_v_kgkm, enef_v_jkm, trafficunits, \
        frfossilfuel_heat, frfossilfuel_nonheat, minfcmetab, maxfcmetab, minqfmetab, \
        maxqfmetab, popdensdaytime, popdensnighttime, temp_c, hdd_id, qf_a, qf_b, \
        qf_c, ah_min, ah_slope_heating, ah_slope_cooling, baset_heating, \
        baset_cooling, trafficrate, qf0_beu, ahprof_24hr, humactivity_24hr, \
        traffprof_24hr, popprof_24hr, surfacearea):
        """
        qf_sahp, fc_anthro, fc_metab, fc_traff, fc_build, fc_point = \
            anthropogenicemissions(co2pointsource, emissionsmethod, it, imin, dls, \
            dayofweek_id, ef_umolco2perj, fcef_v_kgkm, enef_v_jkm, trafficunits, \
            frfossilfuel_heat, frfossilfuel_nonheat, minfcmetab, maxfcmetab, minqfmetab, \
            maxqfmetab, popdensdaytime, popdensnighttime, temp_c, hdd_id, qf_a, qf_b, \
            qf_c, ah_min, ah_slope_heating, ah_slope_cooling, baset_heating, \
            baset_cooling, trafficrate, qf0_beu, ahprof_24hr, humactivity_24hr, \
            traffprof_24hr, popprof_24hr, surfacearea)
        
        
        Defined at suews_phys_anemsn.fpp lines 43-281
        
        Parameters
        ----------
        co2pointsource : float
        emissionsmethod : int
        it : int
        imin : int
        dls : int
        dayofweek_id : int array
        ef_umolco2perj : float
        fcef_v_kgkm : float array
        enef_v_jkm : float
        trafficunits : float
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        minfcmetab : float
        maxfcmetab : float
        minqfmetab : float
        maxqfmetab : float
        popdensdaytime : float array
        popdensnighttime : float
        temp_c : float
        hdd_id : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        ah_min : float array
        ah_slope_heating : float array
        ah_slope_cooling : float array
        baset_heating : float array
        baset_cooling : float array
        trafficrate : float array
        qf0_beu : float array
        ahprof_24hr : float array
        humactivity_24hr : float array
        traffprof_24hr : float array
        popprof_24hr : float array
        surfacearea : float
        
        Returns
        -------
        qf_sahp : float
        fc_anthro : float
        fc_metab : float
        fc_traff : float
        fc_build : float
        fc_point : float
        
        -----------------------------------------------------------------------
         Account for Daylight saving
        """
        qf_sahp, fc_anthro, fc_metab, fc_traff, fc_build, fc_point = \
            _supy_driver.f90wrap_anthropogenicemissions(co2pointsource=co2pointsource, \
            emissionsmethod=emissionsmethod, it=it, imin=imin, dls=dls, \
            dayofweek_id=dayofweek_id, ef_umolco2perj=ef_umolco2perj, \
            fcef_v_kgkm=fcef_v_kgkm, enef_v_jkm=enef_v_jkm, trafficunits=trafficunits, \
            frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, minfcmetab=minfcmetab, \
            maxfcmetab=maxfcmetab, minqfmetab=minqfmetab, maxqfmetab=maxqfmetab, \
            popdensdaytime=popdensdaytime, popdensnighttime=popdensnighttime, \
            temp_c=temp_c, hdd_id=hdd_id, qf_a=qf_a, qf_b=qf_b, qf_c=qf_c, \
            ah_min=ah_min, ah_slope_heating=ah_slope_heating, \
            ah_slope_cooling=ah_slope_cooling, baset_heating=baset_heating, \
            baset_cooling=baset_cooling, trafficrate=trafficrate, qf0_beu=qf0_beu, \
            ahprof_24hr=ahprof_24hr, humactivity_24hr=humactivity_24hr, \
            traffprof_24hr=traffprof_24hr, popprof_24hr=popprof_24hr, \
            surfacearea=surfacearea)
        return qf_sahp, fc_anthro, fc_metab, fc_traff, fc_build, fc_point
    
    _dt_array_initialisers = []
    

anemsn_module = Anemsn_Module()

class Rsl_Module(f90wrap.runtime.FortranModule):
    """
    Module rsl_module
    
    
    Defined at suews_phys_rslprof.fpp lines 5-1311
    
    """
    @staticmethod
    def rslprofile(diagmethod, zh, z0m, zdm, z0v, l_mod, sfr_surf, fai, pai, \
        stabilitymethod, ra_h, avcp, lv_j_kg, avdens, avu1, temp_c, avrh, press_hpa, \
        zmeas, qh, qe, dataoutlinersl):
        """
        t2_c, q2_gkg, u10_ms, rh2 = rslprofile(diagmethod, zh, z0m, zdm, z0v, l_mod, \
            sfr_surf, fai, pai, stabilitymethod, ra_h, avcp, lv_j_kg, avdens, avu1, \
            temp_c, avrh, press_hpa, zmeas, qh, qe, dataoutlinersl)
        
        
        Defined at suews_phys_rslprof.fpp lines 22-339
        
        Parameters
        ----------
        diagmethod : int
        zh : float
        z0m : float
        zdm : float
        z0v : float
        l_mod : float
        sfr_surf : float array
        fai : float
        pai : float
        stabilitymethod : int
        ra_h : float
        avcp : float
        lv_j_kg : float
        avdens : float
        avu1 : float
        temp_c : float
        avrh : float
        press_hpa : float
        zmeas : float
        qh : float
        qe : float
        dataoutlinersl : float array
        
        Returns
        -------
        t2_c : float
        q2_gkg : float
        u10_ms : float
        rh2 : float
        
        -----------------------------------------------------
         calculates windprofiles using MOST with a RSL-correction
         based on Harman & Finnigan 2007
         last modified by:
         NT 16 Mar 2019: initial version
         TS 16 Oct 2019: improved consistency in parameters/varaibles within SUEWS
         TODO how to improve the speed of this code
        -----------------------------------------------------
        """
        t2_c, q2_gkg, u10_ms, rh2 = \
            _supy_driver.f90wrap_rslprofile(diagmethod=diagmethod, zh=zh, z0m=z0m, \
            zdm=zdm, z0v=z0v, l_mod=l_mod, sfr_surf=sfr_surf, fai=fai, pai=pai, \
            stabilitymethod=stabilitymethod, ra_h=ra_h, avcp=avcp, lv_j_kg=lv_j_kg, \
            avdens=avdens, avu1=avu1, temp_c=temp_c, avrh=avrh, press_hpa=press_hpa, \
            zmeas=zmeas, qh=qh, qe=qe, dataoutlinersl=dataoutlinersl)
        return t2_c, q2_gkg, u10_ms, rh2
    
    @staticmethod
    def rslprofile_dts(diagmethod, zh, z0m, zdm, z0v, l_mod, sfr_paved, sfr_bldg, \
        sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, fai, pai, \
        stabilitymethod, ra_h, avcp, lv_j_kg, avdens, avu1, temp_c, avrh, press_hpa, \
        zmeas, qh, qe, dataoutlinersl):
        """
        t2_c, q2_gkg, u10_ms, rh2 = rslprofile_dts(diagmethod, zh, z0m, zdm, z0v, l_mod, \
            sfr_paved, sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
            fai, pai, stabilitymethod, ra_h, avcp, lv_j_kg, avdens, avu1, temp_c, avrh, \
            press_hpa, zmeas, qh, qe, dataoutlinersl)
        
        
        Defined at suews_phys_rslprof.fpp lines 341-655
        
        Parameters
        ----------
        diagmethod : int
        zh : float
        z0m : float
        zdm : float
        z0v : float
        l_mod : float
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        fai : float
        pai : float
        stabilitymethod : int
        ra_h : float
        avcp : float
        lv_j_kg : float
        avdens : float
        avu1 : float
        temp_c : float
        avrh : float
        press_hpa : float
        zmeas : float
        qh : float
        qe : float
        dataoutlinersl : float array
        
        Returns
        -------
        t2_c : float
        q2_gkg : float
        u10_ms : float
        rh2 : float
        
        -----------------------------------------------------
         calculates windprofiles using MOST with a RSL-correction
         based on Harman & Finnigan 2007
         last modified by:
         NT 16 Mar 2019: initial version
         TS 16 Oct 2019: improved consistency in parameters/varaibles within SUEWS
         TODO how to improve the speed of this code
        -----------------------------------------------------
        """
        t2_c, q2_gkg, u10_ms, rh2 = \
            _supy_driver.f90wrap_rslprofile_dts(diagmethod=diagmethod, zh=zh, z0m=z0m, \
            zdm=zdm, z0v=z0v, l_mod=l_mod, sfr_paved=sfr_paved, sfr_bldg=sfr_bldg, \
            sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, sfr_grass=sfr_grass, \
            sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, fai=fai, pai=pai, \
            stabilitymethod=stabilitymethod, ra_h=ra_h, avcp=avcp, lv_j_kg=lv_j_kg, \
            avdens=avdens, avu1=avu1, temp_c=temp_c, avrh=avrh, press_hpa=press_hpa, \
            zmeas=zmeas, qh=qh, qe=qe, dataoutlinersl=dataoutlinersl)
        return t2_c, q2_gkg, u10_ms, rh2
    
    @staticmethod
    def interp_z(z_x, z, v):
        """
        v_x = interp_z(z_x, z, v)
        
        
        Defined at suews_phys_rslprof.fpp lines 657-686
        
        Parameters
        ----------
        z_x : float
        z : float array
        v : float array
        
        Returns
        -------
        v_x : float
        
        """
        v_x = _supy_driver.f90wrap_interp_z(z_x=z_x, z=z, v=v)
        return v_x
    
    @staticmethod
    def cal_elm_rsl(beta, lc):
        """
        elm = cal_elm_rsl(beta, lc)
        
        
        Defined at suews_phys_rslprof.fpp lines 688-698
        
        Parameters
        ----------
        beta : float
        lc : float
        
        Returns
        -------
        elm : float
        
        """
        elm = _supy_driver.f90wrap_cal_elm_rsl(beta=beta, lc=lc)
        return elm
    
    @staticmethod
    def cal_psim_hat(stabilitymethod, psihatm_top, psihatm_mid, z_top, z_mid, z_btm, \
        cm, c2, zh_rsl, zd_rsl, l_mod, beta, elm, lc):
        """
        psihatm_btm = cal_psim_hat(stabilitymethod, psihatm_top, psihatm_mid, z_top, \
            z_mid, z_btm, cm, c2, zh_rsl, zd_rsl, l_mod, beta, elm, lc)
        
        
        Defined at suews_phys_rslprof.fpp lines 700-765
        
        Parameters
        ----------
        stabilitymethod : int
        psihatm_top : float
        psihatm_mid : float
        z_top : float
        z_mid : float
        z_btm : float
        cm : float
        c2 : float
        zh_rsl : float
        zd_rsl : float
        l_mod : float
        beta : float
        elm : float
        lc : float
        
        Returns
        -------
        psihatm_btm : float
        
        """
        psihatm_btm = _supy_driver.f90wrap_cal_psim_hat(stabilitymethod=stabilitymethod, \
            psihatm_top=psihatm_top, psihatm_mid=psihatm_mid, z_top=z_top, z_mid=z_mid, \
            z_btm=z_btm, cm=cm, c2=c2, zh_rsl=zh_rsl, zd_rsl=zd_rsl, l_mod=l_mod, \
            beta=beta, elm=elm, lc=lc)
        return psihatm_btm
    
    @staticmethod
    def cal_psih_hat(stabilitymethod, psihath_top, psihath_mid, z_top, z_mid, z_btm, \
        ch, c2h, zh_rsl, zd_rsl, l_mod, beta, elm, lc):
        """
        psihath_btm = cal_psih_hat(stabilitymethod, psihath_top, psihath_mid, z_top, \
            z_mid, z_btm, ch, c2h, zh_rsl, zd_rsl, l_mod, beta, elm, lc)
        
        
        Defined at suews_phys_rslprof.fpp lines 767-828
        
        Parameters
        ----------
        stabilitymethod : int
        psihath_top : float
        psihath_mid : float
        z_top : float
        z_mid : float
        z_btm : float
        ch : float
        c2h : float
        zh_rsl : float
        zd_rsl : float
        l_mod : float
        beta : float
        elm : float
        lc : float
        
        Returns
        -------
        psihath_btm : float
        
        """
        psihath_btm = _supy_driver.f90wrap_cal_psih_hat(stabilitymethod=stabilitymethod, \
            psihath_top=psihath_top, psihath_mid=psihath_mid, z_top=z_top, z_mid=z_mid, \
            z_btm=z_btm, ch=ch, c2h=c2h, zh_rsl=zh_rsl, zd_rsl=zd_rsl, l_mod=l_mod, \
            beta=beta, elm=elm, lc=lc)
        return psihath_btm
    
    @staticmethod
    def cal_phim_hat(stabilitymethod, z, zh_rsl, l_mod, beta, lc):
        """
        phim_hat = cal_phim_hat(stabilitymethod, z, zh_rsl, l_mod, beta, lc)
        
        
        Defined at suews_phys_rslprof.fpp lines 830-846
        
        Parameters
        ----------
        stabilitymethod : int
        z : float
        zh_rsl : float
        l_mod : float
        beta : float
        lc : float
        
        Returns
        -------
        phim_hat : float
        
        """
        phim_hat = _supy_driver.f90wrap_cal_phim_hat(stabilitymethod=stabilitymethod, \
            z=z, zh_rsl=zh_rsl, l_mod=l_mod, beta=beta, lc=lc)
        return phim_hat
    
    @staticmethod
    def cal_cm(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod):
        """
        c2, cm = cal_cm(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod)
        
        
        Defined at suews_phys_rslprof.fpp lines 848-889
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zd_rsl : float
        lc : float
        beta : float
        l_mod : float
        
        Returns
        -------
        c2 : float
        cm : float
        
        """
        c2, cm = _supy_driver.f90wrap_cal_cm(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zd_rsl=zd_rsl, lc=lc, beta=beta, l_mod=l_mod)
        return c2, cm
    
    @staticmethod
    def cal_ch(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod, scc, f):
        """
        c2h, ch = cal_ch(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod, scc, f)
        
        
        Defined at suews_phys_rslprof.fpp lines 891-931
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zd_rsl : float
        lc : float
        beta : float
        l_mod : float
        scc : float
        f : float
        
        Returns
        -------
        c2h : float
        ch : float
        
        """
        c2h, ch = _supy_driver.f90wrap_cal_ch(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zd_rsl=zd_rsl, lc=lc, beta=beta, l_mod=l_mod, scc=scc, f=f)
        return c2h, ch
    
    @staticmethod
    def cal_zd_rsl(zh_rsl, beta, lc):
        """
        zd_rsl = cal_zd_rsl(zh_rsl, beta, lc)
        
        
        Defined at suews_phys_rslprof.fpp lines 1057-1065
        
        Parameters
        ----------
        zh_rsl : float
        beta : float
        lc : float
        
        Returns
        -------
        zd_rsl : float
        
        """
        zd_rsl = _supy_driver.f90wrap_cal_zd_rsl(zh_rsl=zh_rsl, beta=beta, lc=lc)
        return zd_rsl
    
    @staticmethod
    def cal_z0_rsl(stabilitymethod, zh_rsl, zd_rsl, beta, l_mod_rsl, psihatm_zh):
        """
        z0_rsl = cal_z0_rsl(stabilitymethod, zh_rsl, zd_rsl, beta, l_mod_rsl, \
            psihatm_zh)
        
        
        Defined at suews_phys_rslprof.fpp lines 1067-1104
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zd_rsl : float
        beta : float
        l_mod_rsl : float
        psihatm_zh : float
        
        Returns
        -------
        z0_rsl : float
        
        """
        z0_rsl = _supy_driver.f90wrap_cal_z0_rsl(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zd_rsl=zd_rsl, beta=beta, l_mod_rsl=l_mod_rsl, \
            psihatm_zh=psihatm_zh)
        return z0_rsl
    
    @staticmethod
    def rsl_cal_prms(stabilitymethod, nz_above, z_array, zh, l_mod, sfr_surf, fai, \
        pai, psihatm_array, psihath_array):
        """
        zh_rsl, l_mod_rsl, lc, beta, zd_rsl, z0_rsl, elm, scc, fx = \
            rsl_cal_prms(stabilitymethod, nz_above, z_array, zh, l_mod, sfr_surf, fai, \
            pai, psihatm_array, psihath_array)
        
        
        Defined at suews_phys_rslprof.fpp lines 1106-1242
        
        Parameters
        ----------
        stabilitymethod : int
        nz_above : int
        z_array : float array
        zh : float
        l_mod : float
        sfr_surf : float array
        fai : float
        pai : float
        psihatm_array : float array
        psihath_array : float array
        
        Returns
        -------
        zh_rsl : float
        l_mod_rsl : float
        lc : float
        beta : float
        zd_rsl : float
        z0_rsl : float
        elm : float
        scc : float
        fx : float
        
        """
        zh_rsl, l_mod_rsl, lc, beta, zd_rsl, z0_rsl, elm, scc, fx = \
            _supy_driver.f90wrap_rsl_cal_prms(stabilitymethod=stabilitymethod, \
            nz_above=nz_above, z_array=z_array, zh=zh, l_mod=l_mod, sfr_surf=sfr_surf, \
            fai=fai, pai=pai, psihatm_array=psihatm_array, psihath_array=psihath_array)
        return zh_rsl, l_mod_rsl, lc, beta, zd_rsl, z0_rsl, elm, scc, fx
    
    @staticmethod
    def cal_beta_rsl(stabilitymethod, pai, sfr_tr, lc_over_l):
        """
        beta = cal_beta_rsl(stabilitymethod, pai, sfr_tr, lc_over_l)
        
        
        Defined at suews_phys_rslprof.fpp lines 1244-1281
        
        Parameters
        ----------
        stabilitymethod : int
        pai : float
        sfr_tr : float
        lc_over_l : float
        
        Returns
        -------
        beta : float
        
        """
        beta = _supy_driver.f90wrap_cal_beta_rsl(stabilitymethod=stabilitymethod, \
            pai=pai, sfr_tr=sfr_tr, lc_over_l=lc_over_l)
        return beta
    
    @staticmethod
    def cal_beta_lc(stabilitymethod, beta0, lc_over_l):
        """
        beta_x = cal_beta_lc(stabilitymethod, beta0, lc_over_l)
        
        
        Defined at suews_phys_rslprof.fpp lines 1283-1310
        
        Parameters
        ----------
        stabilitymethod : int
        beta0 : float
        lc_over_l : float
        
        Returns
        -------
        beta_x : float
        
        """
        beta_x = _supy_driver.f90wrap_cal_beta_lc(stabilitymethod=stabilitymethod, \
            beta0=beta0, lc_over_l=lc_over_l)
        return beta_x
    
    @property
    def nz(self):
        """
        Element nz ftype=integer pytype=int
        
        
        Defined at suews_phys_rslprof.fpp line 12
        
        """
        return _supy_driver.f90wrap_rsl_module__get__nz()
    
    def __str__(self):
        ret = ['<rsl_module>{\n']
        ret.append('    nz : ')
        ret.append(repr(self.nz))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

rsl_module = Rsl_Module()

class Meteo(f90wrap.runtime.FortranModule):
    """
    Module meteo
    
    
    Defined at suews_util_meteo.fpp lines 6-446
    
    """
    @staticmethod
    def sat_vap_press(tk, p):
        """
        es = sat_vap_press(tk, p)
        
        
        Defined at suews_util_meteo.fpp lines 25-38
        
        Parameters
        ----------
        tk : float
        p : float
        
        Returns
        -------
        es : float
        
        """
        es = _supy_driver.f90wrap_sat_vap_press(tk=tk, p=p)
        return es
    
    @staticmethod
    def sos_dryair(tk):
        """
        sos_dryair = sos_dryair(tk)
        
        
        Defined at suews_util_meteo.fpp lines 40-43
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        sos_dryair : float
        
        """
        sos_dryair = _supy_driver.f90wrap_sos_dryair(tk=tk)
        return sos_dryair
    
    @staticmethod
    def potential_temp(tk, p):
        """
        potential_temp = potential_temp(tk, p)
        
        
        Defined at suews_util_meteo.fpp lines 46-50
        
        Parameters
        ----------
        tk : float
        p : float
        
        Returns
        -------
        potential_temp : float
        
        """
        potential_temp = _supy_driver.f90wrap_potential_temp(tk=tk, p=p)
        return potential_temp
    
    @staticmethod
    def latentheat_v(tk):
        """
        latentheat_v = latentheat_v(tk)
        
        
        Defined at suews_util_meteo.fpp lines 52-56
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        latentheat_v : float
        
        """
        latentheat_v = _supy_driver.f90wrap_latentheat_v(tk=tk)
        return latentheat_v
    
    @staticmethod
    def latentheat_m(tk):
        """
        latentheat_m = latentheat_m(tk)
        
        
        Defined at suews_util_meteo.fpp lines 58-63
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        latentheat_m : float
        
        """
        latentheat_m = _supy_driver.f90wrap_latentheat_m(tk=tk)
        return latentheat_m
    
    @staticmethod
    def spec_heat_dryair(tk):
        """
        spec_heat_dryair = spec_heat_dryair(tk)
        
        
        Defined at suews_util_meteo.fpp lines 65-69
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        spec_heat_dryair : float
        
        """
        spec_heat_dryair = _supy_driver.f90wrap_spec_heat_dryair(tk=tk)
        return spec_heat_dryair
    
    @staticmethod
    def spec_heat_vapor(tk, rh):
        """
        spec_heat_vapor = spec_heat_vapor(tk, rh)
        
        
        Defined at suews_util_meteo.fpp lines 71-75
        
        Parameters
        ----------
        tk : float
        rh : float
        
        Returns
        -------
        spec_heat_vapor : float
        
        """
        spec_heat_vapor = _supy_driver.f90wrap_spec_heat_vapor(tk=tk, rh=rh)
        return spec_heat_vapor
    
    @staticmethod
    def heatcapacity_air(tk, rh, p):
        """
        heatcapacity_air = heatcapacity_air(tk, rh, p)
        
        
        Defined at suews_util_meteo.fpp lines 77-85
        
        Parameters
        ----------
        tk : float
        rh : float
        p : float
        
        Returns
        -------
        heatcapacity_air : float
        
        """
        heatcapacity_air = _supy_driver.f90wrap_heatcapacity_air(tk=tk, rh=rh, p=p)
        return heatcapacity_air
    
    @staticmethod
    def density_moist(tvk, p):
        """
        density_moist = density_moist(tvk, p)
        
        
        Defined at suews_util_meteo.fpp lines 87-92
        
        Parameters
        ----------
        tvk : float
        p : float
        
        Returns
        -------
        density_moist : float
        
        """
        density_moist = _supy_driver.f90wrap_density_moist(tvk=tvk, p=p)
        return density_moist
    
    @staticmethod
    def density_vapor(tk, rh, p):
        """
        density_vapor = density_vapor(tk, rh, p)
        
        
        Defined at suews_util_meteo.fpp lines 94-98
        
        Parameters
        ----------
        tk : float
        rh : float
        p : float
        
        Returns
        -------
        density_vapor : float
        
        """
        density_vapor = _supy_driver.f90wrap_density_vapor(tk=tk, rh=rh, p=p)
        return density_vapor
    
    @staticmethod
    def density_dryair(tk, p):
        """
        density_dryair = density_dryair(tk, p)
        
        
        Defined at suews_util_meteo.fpp lines 100-102
        
        Parameters
        ----------
        tk : float
        p : float
        
        Returns
        -------
        density_dryair : float
        
        """
        density_dryair = _supy_driver.f90wrap_density_dryair(tk=tk, p=p)
        return density_dryair
    
    @staticmethod
    def density_gas(tk, pp, molmass):
        """
        density_gas = density_gas(tk, pp, molmass)
        
        
        Defined at suews_util_meteo.fpp lines 104-107
        
        Parameters
        ----------
        tk : float
        pp : float
        molmass : float
        
        Returns
        -------
        density_gas : float
        
        """
        density_gas = _supy_driver.f90wrap_density_gas(tk=tk, pp=pp, molmass=molmass)
        return density_gas
    
    @staticmethod
    def partial_pressure(tk, n):
        """
        partial_pressure = partial_pressure(tk, n)
        
        
        Defined at suews_util_meteo.fpp lines 109-112
        
        Parameters
        ----------
        tk : float
        n : float
        
        Returns
        -------
        partial_pressure : float
        
        """
        partial_pressure = _supy_driver.f90wrap_partial_pressure(tk=tk, n=n)
        return partial_pressure
    
    @staticmethod
    def scale_height(tk):
        """
        scale_height = scale_height(tk)
        
        
        Defined at suews_util_meteo.fpp lines 114-117
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        scale_height : float
        
        """
        scale_height = _supy_driver.f90wrap_scale_height(tk=tk)
        return scale_height
    
    @staticmethod
    def vaisala_brunt_f(tk):
        """
        vaisala_brunt_f = vaisala_brunt_f(tk)
        
        
        Defined at suews_util_meteo.fpp lines 119-122
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        vaisala_brunt_f : float
        
        """
        vaisala_brunt_f = _supy_driver.f90wrap_vaisala_brunt_f(tk=tk)
        return vaisala_brunt_f
    
    @staticmethod
    def sat_vap_press_x(temp_c, press_hpa, from_, dectime):
        """
        es_hpa = sat_vap_press_x(temp_c, press_hpa, from_, dectime)
        
        
        Defined at suews_util_meteo.fpp lines 132-165
        
        Parameters
        ----------
        temp_c : float
        press_hpa : float
        from_ : int
        dectime : float
        
        Returns
        -------
        es_hpa : float
        
        """
        es_hpa = _supy_driver.f90wrap_sat_vap_press_x(temp_c=temp_c, \
            press_hpa=press_hpa, from_=from_, dectime=dectime)
        return es_hpa
    
    @staticmethod
    def sat_vap_pressice(temp_c, press_hpa, from_, dectime):
        """
        es_hpa = sat_vap_pressice(temp_c, press_hpa, from_, dectime)
        
        
        Defined at suews_util_meteo.fpp lines 167-192
        
        Parameters
        ----------
        temp_c : float
        press_hpa : float
        from_ : int
        dectime : float
        
        Returns
        -------
        es_hpa : float
        
        """
        es_hpa = _supy_driver.f90wrap_sat_vap_pressice(temp_c=temp_c, \
            press_hpa=press_hpa, from_=from_, dectime=dectime)
        return es_hpa
    
    @staticmethod
    def spec_hum_def(vpd_hpa, press_hpa):
        """
        dq = spec_hum_def(vpd_hpa, press_hpa)
        
        
        Defined at suews_util_meteo.fpp lines 197-202
        
        Parameters
        ----------
        vpd_hpa : float
        press_hpa : float
        
        Returns
        -------
        dq : float
        
        """
        dq = _supy_driver.f90wrap_spec_hum_def(vpd_hpa=vpd_hpa, press_hpa=press_hpa)
        return dq
    
    @staticmethod
    def spec_heat_beer(temp_c, rh, rho_v, rho_d):
        """
        cp = spec_heat_beer(temp_c, rh, rho_v, rho_d)
        
        
        Defined at suews_util_meteo.fpp lines 205-223
        
        Parameters
        ----------
        temp_c : float
        rh : float
        rho_v : float
        rho_d : float
        
        Returns
        -------
        cp : float
        
        -------------------------------------------------------------------------------
         USE defaultnotUsed
        """
        cp = _supy_driver.f90wrap_spec_heat_beer(temp_c=temp_c, rh=rh, rho_v=rho_v, \
            rho_d=rho_d)
        return cp
    
    @staticmethod
    def lat_vap(temp_c, ea_hpa, press_hpa, cp, dectime):
        """
        lv_j_kg = lat_vap(temp_c, ea_hpa, press_hpa, cp, dectime)
        
        
        Defined at suews_util_meteo.fpp lines 229-280
        
        Parameters
        ----------
        temp_c : float
        ea_hpa : float
        press_hpa : float
        cp : float
        dectime : float
        
        Returns
        -------
        lv_j_kg : float
        
        """
        lv_j_kg = _supy_driver.f90wrap_lat_vap(temp_c=temp_c, ea_hpa=ea_hpa, \
            press_hpa=press_hpa, cp=cp, dectime=dectime)
        return lv_j_kg
    
    @staticmethod
    def lat_vapsublim(temp_c, ea_hpa, press_hpa, cp):
        """
        lvs_j_kg = lat_vapsublim(temp_c, ea_hpa, press_hpa, cp)
        
        
        Defined at suews_util_meteo.fpp lines 282-321
        
        Parameters
        ----------
        temp_c : float
        ea_hpa : float
        press_hpa : float
        cp : float
        
        Returns
        -------
        lvs_j_kg : float
        
        """
        lvs_j_kg = _supy_driver.f90wrap_lat_vapsublim(temp_c=temp_c, ea_hpa=ea_hpa, \
            press_hpa=press_hpa, cp=cp)
        return lvs_j_kg
    
    @staticmethod
    def psyc_const(cp, press_hpa, lv_j_kg):
        """
        psyc_hpa = psyc_const(cp, press_hpa, lv_j_kg)
        
        
        Defined at suews_util_meteo.fpp lines 327-343
        
        Parameters
        ----------
        cp : float
        press_hpa : float
        lv_j_kg : float
        
        Returns
        -------
        psyc_hpa : float
        
        """
        psyc_hpa = _supy_driver.f90wrap_psyc_const(cp=cp, press_hpa=press_hpa, \
            lv_j_kg=lv_j_kg)
        return psyc_hpa
    
    @staticmethod
    def dewpoint(ea_hpa):
        """
        temp_c_dew = dewpoint(ea_hpa)
        
        
        Defined at suews_util_meteo.fpp lines 346-353
        
        Parameters
        ----------
        ea_hpa : float
        
        Returns
        -------
        temp_c_dew : float
        
        """
        temp_c_dew = _supy_driver.f90wrap_dewpoint(ea_hpa=ea_hpa)
        return temp_c_dew
    
    @staticmethod
    def slope_svp(temp_c):
        """
        s_hpa = slope_svp(temp_c)
        
        
        Defined at suews_util_meteo.fpp lines 356-376
        
        Parameters
        ----------
        temp_c : float
        
        Returns
        -------
        s_hpa : float
        
        """
        s_hpa = _supy_driver.f90wrap_slope_svp(temp_c=temp_c)
        return s_hpa
    
    @staticmethod
    def slopeice_svp(temp_c):
        """
        s_hpa = slopeice_svp(temp_c)
        
        
        Defined at suews_util_meteo.fpp lines 379-394
        
        Parameters
        ----------
        temp_c : float
        
        Returns
        -------
        s_hpa : float
        
        """
        s_hpa = _supy_driver.f90wrap_slopeice_svp(temp_c=temp_c)
        return s_hpa
    
    @staticmethod
    def qsatf(t, pmb):
        """
        qsat = qsatf(t, pmb)
        
        
        Defined at suews_util_meteo.fpp lines 397-413
        
        Parameters
        ----------
        t : float
        pmb : float
        
        Returns
        -------
        qsat : float
        
        """
        qsat = _supy_driver.f90wrap_qsatf(t=t, pmb=pmb)
        return qsat
    
    @staticmethod
    def rh2qa(rh_dec, pres_hpa, ta_degc):
        """
        qa_gkg = rh2qa(rh_dec, pres_hpa, ta_degc)
        
        
        Defined at suews_util_meteo.fpp lines 415-427
        
        Parameters
        ----------
        rh_dec : float
        pres_hpa : float
        ta_degc : float
        
        Returns
        -------
        qa_gkg : float
        
        """
        qa_gkg = _supy_driver.f90wrap_rh2qa(rh_dec=rh_dec, pres_hpa=pres_hpa, \
            ta_degc=ta_degc)
        return qa_gkg
    
    @staticmethod
    def qa2rh(qa_gkg, pres_hpa, ta_degc):
        """
        rh = qa2rh(qa_gkg, pres_hpa, ta_degc)
        
        
        Defined at suews_util_meteo.fpp lines 429-446
        
        Parameters
        ----------
        qa_gkg : float
        pres_hpa : float
        ta_degc : float
        
        Returns
        -------
        rh : float
        
        """
        rh = _supy_driver.f90wrap_qa2rh(qa_gkg=qa_gkg, pres_hpa=pres_hpa, \
            ta_degc=ta_degc)
        return rh
    
    @property
    def rad2deg(self):
        """
        Element rad2deg ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 10
        
        """
        return _supy_driver.f90wrap_meteo__get__rad2deg()
    
    @property
    def deg2rad(self):
        """
        Element deg2rad ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 11
        
        """
        return _supy_driver.f90wrap_meteo__get__deg2rad()
    
    @property
    def molmass_air(self):
        """
        Element molmass_air ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 12
        
        """
        return _supy_driver.f90wrap_meteo__get__molmass_air()
    
    @property
    def molmass_co2(self):
        """
        Element molmass_co2 ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 13
        
        """
        return _supy_driver.f90wrap_meteo__get__molmass_co2()
    
    @property
    def molmass_h2o(self):
        """
        Element molmass_h2o ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 14
        
        """
        return _supy_driver.f90wrap_meteo__get__molmass_h2o()
    
    @property
    def mu_h2o(self):
        """
        Element mu_h2o ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 15
        
        """
        return _supy_driver.f90wrap_meteo__get__mu_h2o()
    
    @property
    def mu_co2(self):
        """
        Element mu_co2 ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 16
        
        """
        return _supy_driver.f90wrap_meteo__get__mu_co2()
    
    @property
    def r_dry_mol(self):
        """
        Element r_dry_mol ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 17
        
        """
        return _supy_driver.f90wrap_meteo__get__r_dry_mol()
    
    @property
    def r_dry_mass(self):
        """
        Element r_dry_mass ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 18
        
        """
        return _supy_driver.f90wrap_meteo__get__r_dry_mass()
    
    @property
    def epsil(self):
        """
        Element epsil ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 20
        
        """
        return _supy_driver.f90wrap_meteo__get__epsil()
    
    @property
    def kb(self):
        """
        Element kb ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 21
        
        """
        return _supy_driver.f90wrap_meteo__get__kb()
    
    @property
    def avogadro(self):
        """
        Element avogadro ftype=real(kind(1d0) pytype=float
        
        
        Defined at suews_util_meteo.fpp line 22
        
        """
        return _supy_driver.f90wrap_meteo__get__avogadro()
    
    def __str__(self):
        ret = ['<meteo>{\n']
        ret.append('    rad2deg : ')
        ret.append(repr(self.rad2deg))
        ret.append(',\n    deg2rad : ')
        ret.append(repr(self.deg2rad))
        ret.append(',\n    molmass_air : ')
        ret.append(repr(self.molmass_air))
        ret.append(',\n    molmass_co2 : ')
        ret.append(repr(self.molmass_co2))
        ret.append(',\n    molmass_h2o : ')
        ret.append(repr(self.molmass_h2o))
        ret.append(',\n    mu_h2o : ')
        ret.append(repr(self.mu_h2o))
        ret.append(',\n    mu_co2 : ')
        ret.append(repr(self.mu_co2))
        ret.append(',\n    r_dry_mol : ')
        ret.append(repr(self.r_dry_mol))
        ret.append(',\n    r_dry_mass : ')
        ret.append(repr(self.r_dry_mass))
        ret.append(',\n    epsil : ')
        ret.append(repr(self.epsil))
        ret.append(',\n    kb : ')
        ret.append(repr(self.kb))
        ret.append(',\n    avogadro : ')
        ret.append(repr(self.avogadro))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

meteo = Meteo()

class Spartacus_Module(f90wrap.runtime.FortranModule):
    """
    Module spartacus_module
    
    
    Defined at suews_phys_spartacus.fpp lines 5-622
    
    """
    @staticmethod
    def spartacus_initialise():
        """
        spartacus_initialise()
        
        
        Defined at suews_phys_spartacus.fpp lines 45-80
        
        
        """
        _supy_driver.f90wrap_spartacus_initialise()
    
    @staticmethod
    def spartacus(diagqn, sfr_surf, zenith_deg, nlayer, tsfc_surf, tsfc_roof, \
        tsfc_wall, kdown, ldown, tair_c, alb_surf, emis_surf, lai_id, \
        n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
        sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
        air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
        ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
        veg_frac, sfr_roof, sfr_wall, building_scale, veg_scale, alb_roof, \
        emis_roof, alb_wall, emis_wall, roof_albedo_dir_mult_fact, \
        wall_specular_frac, qn_roof, qn_wall, qn_surf, dataoutlinespartacus):
        """
        qn, kup, lup = spartacus(diagqn, sfr_surf, zenith_deg, nlayer, tsfc_surf, \
            tsfc_roof, tsfc_wall, kdown, ldown, tair_c, alb_surf, emis_surf, lai_id, \
            n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, sfr_roof, sfr_wall, building_scale, veg_scale, alb_roof, \
            emis_roof, alb_wall, emis_wall, roof_albedo_dir_mult_fact, \
            wall_specular_frac, qn_roof, qn_wall, qn_surf, dataoutlinespartacus)
        
        
        Defined at suews_phys_spartacus.fpp lines 82-622
        
        Parameters
        ----------
        diagqn : int
        sfr_surf : float array
        zenith_deg : float
        nlayer : int
        tsfc_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        kdown : float
        ldown : float
        tair_c : float
        alb_surf : float array
        emis_surf : float array
        lai_id : float array
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        sfr_roof : float array
        sfr_wall : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        qn_roof : float array
        qn_wall : float array
        qn_surf : float array
        dataoutlinespartacus : float array
        
        Returns
        -------
        qn : float
        kup : float
        lup : float
        
        """
        qn, kup, lup = _supy_driver.f90wrap_spartacus(diagqn=diagqn, sfr_surf=sfr_surf, \
            zenith_deg=zenith_deg, nlayer=nlayer, tsfc_surf=tsfc_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, kdown=kdown, ldown=ldown, \
            tair_c=tair_c, alb_surf=alb_surf, emis_surf=emis_surf, lai_id=lai_id, \
            n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, sfr_roof=sfr_roof, \
            sfr_wall=sfr_wall, building_scale=building_scale, veg_scale=veg_scale, \
            alb_roof=alb_roof, emis_roof=emis_roof, alb_wall=alb_wall, \
            emis_wall=emis_wall, roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, qn_roof=qn_roof, qn_wall=qn_wall, \
            qn_surf=qn_surf, dataoutlinespartacus=dataoutlinespartacus)
        return qn, kup, lup
    
    _dt_array_initialisers = []
    

spartacus_module = Spartacus_Module()

