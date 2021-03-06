'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_draw_buffers'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_draw_buffers',False)
_p.unpack_constants( """GL_MAX_DRAW_BUFFERS_ATI 0x8824
GL_DRAW_BUFFER0_ATI 0x8825
GL_DRAW_BUFFER1_ATI 0x8826
GL_DRAW_BUFFER2_ATI 0x8827
GL_DRAW_BUFFER3_ATI 0x8828
GL_DRAW_BUFFER4_ATI 0x8829
GL_DRAW_BUFFER5_ATI 0x882A
GL_DRAW_BUFFER6_ATI 0x882B
GL_DRAW_BUFFER7_ATI 0x882C
GL_DRAW_BUFFER8_ATI 0x882D
GL_DRAW_BUFFER9_ATI 0x882E
GL_DRAW_BUFFER10_ATI 0x882F
GL_DRAW_BUFFER11_ATI 0x8830
GL_DRAW_BUFFER12_ATI 0x8831
GL_DRAW_BUFFER13_ATI 0x8832
GL_DRAW_BUFFER14_ATI 0x8833
GL_DRAW_BUFFER15_ATI 0x8834""", globals())
glget.addGLGetConstant( GL_MAX_DRAW_BUFFERS_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER0_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER1_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER2_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER3_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER4_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER5_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER6_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER7_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER8_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER9_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER10_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER11_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER12_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER13_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER14_ATI, (1,) )
glget.addGLGetConstant( GL_DRAW_BUFFER15_ATI, (1,) )
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDrawBuffersATI( n,bufs ):pass


def glInitDrawBuffersATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
