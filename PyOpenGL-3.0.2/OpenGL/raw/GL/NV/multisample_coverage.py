'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_NV_multisample_coverage'
_p.unpack_constants( """GL_COVERAGE_SAMPLES_NV 0x80A9
GL_COLOR_SAMPLES_NV 0x8E20""", globals())


def glInitMultisampleCoverageNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
