# Use Peter Bengtsson's slimmer library when available
# from http://www.issuetrackerproduct.com/Download#slimmer

# You can plug in other XHTML-whitespace removal libraries here as well.

# Change the following value to True to enable xhtml whitespace compression
SLIMMER = None

try:
    from slimmer import xhtml_slimmer
except ImportError:
    SLIMMER = False


def xhtml_compress(string):
    if SLIMMER:
        return xhtml_slimmer(string)
    return string
