# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-I../../include', '-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/', '-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes
import sys

from . import library_loader


class AsDictMixin:
    @classmethod
    def as_dict(cls, self):
        result = {}
        if not isinstance(self, AsDictMixin):
            # not a structure, assume it's already a python object
            return self
        if not hasattr(cls, "_fields_"):
            return result
        # sys.version_info >= (3, 5)
        # for (field, *_) in cls._fields_:  # noqa
        for field_tuple in cls._fields_:  # noqa
            field = field_tuple[0]
            if field.startswith("PADDING_"):
                continue
            value = getattr(self, field)
            type_ = type(value)
            if hasattr(value, "_length_") and hasattr(value, "_type_"):
                # array
                if not hasattr(type_, "as_dict"):
                    value = [v for v in value]
                else:
                    type_ = type_._type_
                    value = [type_.as_dict(v) for v in value]
            elif hasattr(value, "contents") and hasattr(value, "_type_"):
                # pointer
                try:
                    if not hasattr(type_, "as_dict"):
                        value = value.contents
                    else:
                        type_ = type_._type_
                        value = type_.as_dict(value.contents)
                except ValueError:
                    # nullptr
                    value = None
            elif isinstance(value, AsDictMixin):
                # other structure
                value = type_.as_dict(value)
            result[field] = value
        return result


class Structure(ctypes.Structure, AsDictMixin):

    def __init__(self, *args, **kwds):
        # We don't want to use positional arguments fill PADDING_* fields

        args = dict(zip(self.__class__._field_names_(), args))
        args.update(kwds)
        super(Structure, self).__init__(**args)

    @classmethod
    def _field_names_(cls):
        if hasattr(cls, "_fields_"):
            return (f[0] for f in cls._fields_ if not f[0].startswith("PADDING"))
        else:
            return ()

    @classmethod
    def get_type(cls, field):
        for f in cls._fields_:
            if f[0] == field:
                return f[1]
        return None

    @classmethod
    def bind(cls, bound_fields):
        fields = {}
        for name, type_ in cls._fields_:
            if hasattr(type_, "restype"):
                if name in bound_fields:
                    if bound_fields[name] is None:
                        fields[name] = type_()
                    else:
                        # use a closure to capture the callback from the loop scope
                        fields[name] = type_(
                            (lambda callback: lambda *args: callback(*args))(
                                bound_fields[name]
                            )
                        )
                    del bound_fields[name]
                else:
                    # default callback implementation (does nothing)
                    try:
                        default_ = type_(0).restype().value
                    except TypeError:
                        default_ = None
                    fields[name] = type_(
                        (lambda default_: lambda *args: default_)(default_)
                    )
            else:
                # not a callback function, use default initialization
                if name in bound_fields:
                    fields[name] = bound_fields[name]
                    del bound_fields[name]
                else:
                    fields[name] = type_()
        if len(bound_fields) != 0:
            raise ValueError(
                "Cannot bind the following unknown callback(s) {}.{}".format(
                    cls.__name__, bound_fields.keys()
                )
            )
        return cls(**fields)


class Union(ctypes.Union, AsDictMixin):
    pass


def string_cast(char_pointer, encoding="utf-8", errors="strict"):
    value = ctypes.cast(char_pointer, ctypes.c_char_p).value
    if value is not None and encoding is not None:
        value = value.decode(encoding, errors=errors)
    return value


def char_pointer_cast(string, encoding="utf-8"):
    if encoding is not None:
        try:
            string = string.encode(encoding)
        except AttributeError:
            # In Python3, bytes has no encode attribute
            pass
    string = ctypes.c_char_p(string)
    return ctypes.cast(string, ctypes.POINTER(ctypes.c_char))


c_int128 = ctypes.c_ubyte * 16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte * 16


class FunctionFactoryStub:
    def __getattr__(self, _):
        return ctypes.CFUNCTYPE(lambda y: y)


# libraries['xnvme'] explanation
# As you did not list (-l libraryname.so) a library that exports this function
# This is a non-working stub instead.
# You can either re-run clan2py with -l /path/to/library.so
# Or manually fix this by comment the ctypes.CDLL loading
_libraries = {}
_libraries["xnvme"] = library_loader.load()
is_loaded = _libraries["xnvme"] is not None
_libraries["xnvme"] = (
    _libraries["xnvme"] if _libraries["xnvme"] else FunctionFactoryStub()
)
#  ctypes.CDLL('xnvme')


class xnvme_opts_css(Structure):
    pass


xnvme_opts_css._pack_ = 1  # source:False
xnvme_opts_css._fields_ = [
    ("value", ctypes.c_uint32),
    ("given", ctypes.c_uint32),
]


class xnvme_opts(Structure):
    pass


xnvme_opts._pack_ = 1  # source:False
xnvme_opts._fields_ = [
    ("be", ctypes.POINTER(ctypes.c_char)),
    ("dev", ctypes.POINTER(ctypes.c_char)),
    ("mem", ctypes.POINTER(ctypes.c_char)),
    ("sync", ctypes.POINTER(ctypes.c_char)),
    ("async", ctypes.POINTER(ctypes.c_char)),
    ("admin", ctypes.POINTER(ctypes.c_char)),
    ("nsid", ctypes.c_uint32),
    ("rdonly", ctypes.c_ubyte),
    ("wronly", ctypes.c_ubyte),
    ("rdwr", ctypes.c_ubyte),
    ("create", ctypes.c_ubyte),
    ("truncate", ctypes.c_ubyte),
    ("direct", ctypes.c_ubyte),
    ("PADDING_0", ctypes.c_ubyte * 2),
    ("create_mode", ctypes.c_uint32),
    ("poll_io", ctypes.c_ubyte),
    ("poll_sq", ctypes.c_ubyte),
    ("register_files", ctypes.c_ubyte),
    ("register_buffers", ctypes.c_ubyte),
    ("css", xnvme_opts_css),
    ("use_cmb_sqs", ctypes.c_uint32),
    ("shm_id", ctypes.c_uint32),
    ("main_core", ctypes.c_uint32),
    ("core_mask", ctypes.POINTER(ctypes.c_char)),
    ("adrfam", ctypes.POINTER(ctypes.c_char)),
    ("subnqn", ctypes.POINTER(ctypes.c_char)),
    ("hostnqn", ctypes.POINTER(ctypes.c_char)),
    ("admin_timeout", ctypes.c_uint32),
    ("command_timeout", ctypes.c_uint32),
    ("spdk_fabrics", ctypes.c_uint32),
    ("PADDING_1", ctypes.c_ubyte * 4),
]

xnvme_opts_set_defaults = _libraries["xnvme"].xnvme_opts_set_defaults
xnvme_opts_set_defaults.restype = None
xnvme_opts_set_defaults.argtypes = [ctypes.POINTER(xnvme_opts)]
xnvme_opts_default = _libraries["xnvme"].xnvme_opts_default
xnvme_opts_default.restype = xnvme_opts
xnvme_opts_default.argtypes = []

# values for enumeration 'xnvme_enumerate_action'
xnvme_enumerate_action__enumvalues = {
    0: "XNVME_ENUMERATE_DEV_KEEP_OPEN",
    1: "XNVME_ENUMERATE_DEV_CLOSE",
}
XNVME_ENUMERATE_DEV_KEEP_OPEN = 0
XNVME_ENUMERATE_DEV_CLOSE = 1
xnvme_enumerate_action = ctypes.c_uint32  # enum


class xnvme_dev(Structure):
    pass


xnvme_enumerate_cb = ctypes.CFUNCTYPE(
    ctypes.c_int32, ctypes.POINTER(xnvme_dev), ctypes.POINTER(None)
)
xnvme_enumerate = _libraries["xnvme"].xnvme_enumerate
xnvme_enumerate.restype = ctypes.c_int32
xnvme_enumerate.argtypes = [
    ctypes.POINTER(ctypes.c_char),
    ctypes.POINTER(xnvme_opts),
    xnvme_enumerate_cb,
    ctypes.POINTER(None),
]
xnvme_dev_derive_geo = _libraries["xnvme"].xnvme_dev_derive_geo
xnvme_dev_derive_geo.restype = ctypes.c_int32
xnvme_dev_derive_geo.argtypes = [ctypes.POINTER(xnvme_dev)]


class xnvme_geo(Structure):
    pass


xnvme_dev_get_geo = _libraries["xnvme"].xnvme_dev_get_geo
xnvme_dev_get_geo.restype = ctypes.POINTER(xnvme_geo)
xnvme_dev_get_geo.argtypes = [ctypes.POINTER(xnvme_dev)]


class xnvme_spec_idfy_ctrlr(Structure):
    pass


xnvme_dev_get_ctrlr = _libraries["xnvme"].xnvme_dev_get_ctrlr
xnvme_dev_get_ctrlr.restype = ctypes.POINTER(xnvme_spec_idfy_ctrlr)
xnvme_dev_get_ctrlr.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_dev_get_ctrlr_css = _libraries["xnvme"].xnvme_dev_get_ctrlr_css
xnvme_dev_get_ctrlr_css.restype = ctypes.POINTER(xnvme_spec_idfy_ctrlr)
xnvme_dev_get_ctrlr_css.argtypes = [ctypes.POINTER(xnvme_dev)]


class xnvme_spec_idfy_ns(Structure):
    pass


xnvme_dev_get_ns = _libraries["xnvme"].xnvme_dev_get_ns
xnvme_dev_get_ns.restype = ctypes.POINTER(xnvme_spec_idfy_ns)
xnvme_dev_get_ns.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_dev_get_ns_css = _libraries["xnvme"].xnvme_dev_get_ns_css
xnvme_dev_get_ns_css.restype = ctypes.POINTER(xnvme_spec_idfy_ns)
xnvme_dev_get_ns_css.argtypes = [ctypes.POINTER(xnvme_dev)]
uint32_t = ctypes.c_uint32
xnvme_dev_get_nsid = _libraries["xnvme"].xnvme_dev_get_nsid
xnvme_dev_get_nsid.restype = uint32_t
xnvme_dev_get_nsid.argtypes = [ctypes.POINTER(xnvme_dev)]
uint8_t = ctypes.c_uint8
xnvme_dev_get_csi = _libraries["xnvme"].xnvme_dev_get_csi
xnvme_dev_get_csi.restype = uint8_t
xnvme_dev_get_csi.argtypes = [ctypes.POINTER(xnvme_dev)]


class xnvme_ident(Structure):
    pass


xnvme_dev_get_ident = _libraries["xnvme"].xnvme_dev_get_ident
xnvme_dev_get_ident.restype = ctypes.POINTER(xnvme_ident)
xnvme_dev_get_ident.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_dev_get_opts = _libraries["xnvme"].xnvme_dev_get_opts
xnvme_dev_get_opts.restype = ctypes.POINTER(xnvme_opts)
xnvme_dev_get_opts.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_dev_get_be_state = _libraries["xnvme"].xnvme_dev_get_be_state
xnvme_dev_get_be_state.restype = ctypes.POINTER(None)
xnvme_dev_get_be_state.argtypes = [ctypes.POINTER(xnvme_dev)]
uint64_t = ctypes.c_uint64
xnvme_dev_get_ssw = _libraries["xnvme"].xnvme_dev_get_ssw
xnvme_dev_get_ssw.restype = uint64_t
xnvme_dev_get_ssw.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_dev_open = _libraries["xnvme"].xnvme_dev_open
xnvme_dev_open.restype = ctypes.POINTER(xnvme_dev)
xnvme_dev_open.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(xnvme_opts)]
xnvme_dev_close = _libraries["xnvme"].xnvme_dev_close
xnvme_dev_close.restype = None
xnvme_dev_close.argtypes = [ctypes.POINTER(xnvme_dev)]


class xnvme_be_attr(Structure):
    pass


xnvme_be_attr._pack_ = 1  # source:False
xnvme_be_attr._fields_ = [
    ("name", ctypes.POINTER(ctypes.c_char)),
    ("enabled", ctypes.c_ubyte),
    ("_rsvd", ctypes.c_ubyte * 15),
]


class xnvme_be_attr_list(Structure):
    pass


xnvme_be_attr_list._pack_ = 1  # source:False
xnvme_be_attr_list._fields_ = [
    ("capacity", ctypes.c_uint32),
    ("count", ctypes.c_int32),
    ("item", xnvme_be_attr * 0),
]

xnvme_be_attr_list_bundled = _libraries["xnvme"].xnvme_be_attr_list_bundled
xnvme_be_attr_list_bundled.restype = ctypes.c_int32
xnvme_be_attr_list_bundled.argtypes = [
    ctypes.POINTER(ctypes.POINTER(xnvme_be_attr_list))
]
size_t = ctypes.c_uint64
xnvme_buf_alloc = _libraries["xnvme"].xnvme_buf_alloc
xnvme_buf_alloc.restype = ctypes.POINTER(None)
xnvme_buf_alloc.argtypes = [ctypes.POINTER(xnvme_dev), size_t]
xnvme_buf_realloc = _libraries["xnvme"].xnvme_buf_realloc
xnvme_buf_realloc.restype = ctypes.POINTER(None)
xnvme_buf_realloc.argtypes = [ctypes.POINTER(xnvme_dev), ctypes.POINTER(None), size_t]
xnvme_buf_free = _libraries["xnvme"].xnvme_buf_free
xnvme_buf_free.restype = None
xnvme_buf_free.argtypes = [ctypes.POINTER(xnvme_dev), ctypes.POINTER(None)]
xnvme_buf_phys_alloc = _libraries["xnvme"].xnvme_buf_phys_alloc
xnvme_buf_phys_alloc.restype = ctypes.POINTER(None)
xnvme_buf_phys_alloc.argtypes = [
    ctypes.POINTER(xnvme_dev),
    size_t,
    ctypes.POINTER(ctypes.c_uint64),
]
xnvme_buf_phys_free = _libraries["xnvme"].xnvme_buf_phys_free
xnvme_buf_phys_free.restype = None
xnvme_buf_phys_free.argtypes = [ctypes.POINTER(xnvme_dev), ctypes.POINTER(None)]
xnvme_buf_phys_realloc = _libraries["xnvme"].xnvme_buf_phys_realloc
xnvme_buf_phys_realloc.restype = ctypes.POINTER(None)
xnvme_buf_phys_realloc.argtypes = [
    ctypes.POINTER(xnvme_dev),
    ctypes.POINTER(None),
    size_t,
    ctypes.POINTER(ctypes.c_uint64),
]
xnvme_buf_vtophys = _libraries["xnvme"].xnvme_buf_vtophys
xnvme_buf_vtophys.restype = ctypes.c_int32
xnvme_buf_vtophys.argtypes = [
    ctypes.POINTER(xnvme_dev),
    ctypes.POINTER(None),
    ctypes.POINTER(ctypes.c_uint64),
]
xnvme_buf_virt_alloc = _libraries["xnvme"].xnvme_buf_virt_alloc
xnvme_buf_virt_alloc.restype = ctypes.POINTER(None)
xnvme_buf_virt_alloc.argtypes = [size_t, size_t]
xnvme_buf_virt_free = _libraries["xnvme"].xnvme_buf_virt_free
xnvme_buf_virt_free.restype = None
xnvme_buf_virt_free.argtypes = [ctypes.POINTER(None)]
xnvme_buf_fill = _libraries["xnvme"].xnvme_buf_fill
xnvme_buf_fill.restype = ctypes.c_int32
xnvme_buf_fill.argtypes = [ctypes.POINTER(None), size_t, ctypes.POINTER(ctypes.c_char)]
xnvme_buf_clear = _libraries["xnvme"].xnvme_buf_clear
xnvme_buf_clear.restype = ctypes.POINTER(None)
xnvme_buf_clear.argtypes = [ctypes.POINTER(None), size_t]
xnvme_buf_diff = _libraries["xnvme"].xnvme_buf_diff
xnvme_buf_diff.restype = size_t
xnvme_buf_diff.argtypes = [ctypes.POINTER(None), ctypes.POINTER(None), size_t]
xnvme_buf_diff_pr = _libraries["xnvme"].xnvme_buf_diff_pr
xnvme_buf_diff_pr.restype = None
xnvme_buf_diff_pr.argtypes = [
    ctypes.POINTER(None),
    ctypes.POINTER(None),
    size_t,
    ctypes.c_int32,
]
xnvme_buf_to_file = _libraries["xnvme"].xnvme_buf_to_file
xnvme_buf_to_file.restype = ctypes.c_int32
xnvme_buf_to_file.argtypes = [
    ctypes.POINTER(None),
    size_t,
    ctypes.POINTER(ctypes.c_char),
]
xnvme_buf_from_file = _libraries["xnvme"].xnvme_buf_from_file
xnvme_buf_from_file.restype = ctypes.c_int32
xnvme_buf_from_file.argtypes = [
    ctypes.POINTER(None),
    size_t,
    ctypes.POINTER(ctypes.c_char),
]
xnvme_mem_map = _libraries["xnvme"].xnvme_mem_map
xnvme_mem_map.restype = ctypes.c_int32
xnvme_mem_map.argtypes = [ctypes.POINTER(xnvme_dev), ctypes.POINTER(None), size_t]
xnvme_mem_unmap = _libraries["xnvme"].xnvme_mem_unmap
xnvme_mem_unmap.restype = ctypes.c_int32
xnvme_mem_unmap.argtypes = [ctypes.POINTER(xnvme_dev), ctypes.POINTER(None)]

# values for enumeration 'xnvme_geo_type'
xnvme_geo_type__enumvalues = {
    0: "XNVME_GEO_UNKNOWN",
    1: "XNVME_GEO_CONVENTIONAL",
    2: "XNVME_GEO_ZONED",
    3: "XNVME_GEO_KV",
}
XNVME_GEO_UNKNOWN = 0
XNVME_GEO_CONVENTIONAL = 1
XNVME_GEO_ZONED = 2
XNVME_GEO_KV = 3
xnvme_geo_type = ctypes.c_uint32  # enum
xnvme_ident_from_uri = _libraries["xnvme"].xnvme_ident_from_uri
xnvme_ident_from_uri.restype = ctypes.c_int32
xnvme_ident_from_uri.argtypes = [
    ctypes.POINTER(ctypes.c_char),
    ctypes.POINTER(xnvme_ident),
]


class xnvme_queue(Structure):
    pass


# values for enumeration 'xnvme_queue_opts'
xnvme_queue_opts__enumvalues = {
    1: "XNVME_QUEUE_IOPOLL",
    2: "XNVME_QUEUE_SQPOLL",
}
XNVME_QUEUE_IOPOLL = 1
XNVME_QUEUE_SQPOLL = 2
xnvme_queue_opts = ctypes.c_uint32  # enum
uint16_t = ctypes.c_uint16
xnvme_queue_init = _libraries["xnvme"].xnvme_queue_init
xnvme_queue_init.restype = ctypes.c_int32
xnvme_queue_init.argtypes = [
    ctypes.POINTER(xnvme_dev),
    uint16_t,
    ctypes.c_int32,
    ctypes.POINTER(ctypes.POINTER(xnvme_queue)),
]
xnvme_queue_get_capacity = _libraries["xnvme"].xnvme_queue_get_capacity
xnvme_queue_get_capacity.restype = uint32_t
xnvme_queue_get_capacity.argtypes = [ctypes.POINTER(xnvme_queue)]
xnvme_queue_get_outstanding = _libraries["xnvme"].xnvme_queue_get_outstanding
xnvme_queue_get_outstanding.restype = uint32_t
xnvme_queue_get_outstanding.argtypes = [ctypes.POINTER(xnvme_queue)]
xnvme_queue_term = _libraries["xnvme"].xnvme_queue_term
xnvme_queue_term.restype = ctypes.c_int32
xnvme_queue_term.argtypes = [ctypes.POINTER(xnvme_queue)]
xnvme_queue_poke = _libraries["xnvme"].xnvme_queue_poke
xnvme_queue_poke.restype = ctypes.c_int32
xnvme_queue_poke.argtypes = [ctypes.POINTER(xnvme_queue), uint32_t]
xnvme_queue_drain = _libraries["xnvme"].xnvme_queue_drain
xnvme_queue_drain.restype = ctypes.c_int32
xnvme_queue_drain.argtypes = [ctypes.POINTER(xnvme_queue)]
xnvme_queue_wait = _libraries["xnvme"].xnvme_queue_wait
xnvme_queue_wait.restype = ctypes.c_int32
xnvme_queue_wait.argtypes = [ctypes.POINTER(xnvme_queue)]


class xnvme_cmd_ctx(Structure):
    pass


xnvme_queue_get_cmd_ctx = _libraries["xnvme"].xnvme_queue_get_cmd_ctx
xnvme_queue_get_cmd_ctx.restype = ctypes.POINTER(xnvme_cmd_ctx)
xnvme_queue_get_cmd_ctx.argtypes = [ctypes.POINTER(xnvme_queue)]
xnvme_queue_put_cmd_ctx = _libraries["xnvme"].xnvme_queue_put_cmd_ctx
xnvme_queue_put_cmd_ctx.restype = ctypes.c_int32
xnvme_queue_put_cmd_ctx.argtypes = [
    ctypes.POINTER(xnvme_queue),
    ctypes.POINTER(xnvme_cmd_ctx),
]
xnvme_queue_cb = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(xnvme_cmd_ctx), ctypes.POINTER(None)
)
xnvme_queue_set_cb = _libraries["xnvme"].xnvme_queue_set_cb
xnvme_queue_set_cb.restype = ctypes.c_int32
xnvme_queue_set_cb.argtypes = [
    ctypes.POINTER(xnvme_queue),
    xnvme_queue_cb,
    ctypes.POINTER(None),
]
xnvme_queue_get_completion_fd = _libraries["xnvme"].xnvme_queue_get_completion_fd
xnvme_queue_get_completion_fd.restype = ctypes.c_int32
xnvme_queue_get_completion_fd.argtypes = [ctypes.POINTER(xnvme_queue)]


class xnvme_spec_ctrlr_bar(Structure):
    pass


xnvme_spec_ctrlr_bar._pack_ = 1  # source:True
xnvme_spec_ctrlr_bar._fields_ = [
    ("cap", ctypes.c_uint64),
    ("vs", ctypes.c_uint32),
    ("intms", ctypes.c_uint32),
    ("intmc", ctypes.c_uint32),
    ("cc", ctypes.c_uint32),
    ("rsvd24", ctypes.c_uint32),
    ("csts", ctypes.c_uint32),
    ("nssr", ctypes.c_uint32),
    ("aqa", ctypes.c_uint32),
    ("asq", ctypes.c_uint64),
    ("acq", ctypes.c_uint64),
    ("cmbloc", ctypes.c_uint32),
    ("cmbsz", ctypes.c_uint32),
    ("bpinfo", ctypes.c_uint32),
    ("bprsel", ctypes.c_uint32),
    ("bpmbl", ctypes.c_uint64),
    ("cmbmsc", ctypes.c_uint64),
    ("cmbsts", ctypes.c_uint32),
    ("rsvd92", ctypes.c_ubyte * 3492),
    ("pmrcap", ctypes.c_uint32),
    ("pmrctl", ctypes.c_uint32),
    ("pmrsts", ctypes.c_uint32),
    ("pmrebs", ctypes.c_uint32),
    ("pmrswtp", ctypes.c_uint32),
    ("pmrmscl", ctypes.c_uint32),
    ("pmrmscu", ctypes.c_uint32),
    ("css", ctypes.c_ubyte * 484),
]


# values for enumeration 'xnvme_spec_status_code_type'
xnvme_spec_status_code_type__enumvalues = {
    0: "XNVME_STATUS_CODE_TYPE_GENERIC",
    1: "XNVME_STATUS_CODE_TYPE_CMDSPEC",
    2: "XNVME_STATUS_CODE_TYPE_MEDIA",
    3: "XNVME_STATUS_CODE_TYPE_PATH",
    7: "XNVME_STATUS_CODE_TYPE_VENDOR",
}
XNVME_STATUS_CODE_TYPE_GENERIC = 0
XNVME_STATUS_CODE_TYPE_CMDSPEC = 1
XNVME_STATUS_CODE_TYPE_MEDIA = 2
XNVME_STATUS_CODE_TYPE_PATH = 3
XNVME_STATUS_CODE_TYPE_VENDOR = 7
xnvme_spec_status_code_type = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_status_code'
xnvme_spec_status_code__enumvalues = {
    2: "XNVME_STATUS_CODE_INVALID_FIELD",
}
XNVME_STATUS_CODE_INVALID_FIELD = 2
xnvme_spec_status_code = ctypes.c_uint32  # enum


class xnvme_spec_status(Structure):
    pass


class xnvme_spec_status_0(Union):
    pass


class xnvme_spec_status_0_0(Structure):
    pass


xnvme_spec_status_0_0._pack_ = 1  # source:False
xnvme_spec_status_0_0._fields_ = [
    ("p", ctypes.c_uint16, 1),
    ("sc", ctypes.c_uint16, 8),
    ("sct", ctypes.c_uint16, 3),
    ("rsvd2", ctypes.c_uint16, 2),
    ("m", ctypes.c_uint16, 1),
    ("dnr", ctypes.c_uint16, 1),
]

xnvme_spec_status_0._pack_ = 1  # source:False
xnvme_spec_status_0._anonymous_ = ("_0",)
xnvme_spec_status_0._fields_ = [
    ("_0", xnvme_spec_status_0_0),
    ("val", ctypes.c_uint16),
]

xnvme_spec_status._pack_ = 1  # source:False
xnvme_spec_status._anonymous_ = ("_0",)
xnvme_spec_status._fields_ = [
    ("_0", xnvme_spec_status_0),
]


class xnvme_spec_cpl(Structure):
    pass


class xnvme_spec_cpl_0(Union):
    pass


class xnvme_spec_cpl_0_0(Structure):
    pass


xnvme_spec_cpl_0_0._pack_ = 1  # source:False
xnvme_spec_cpl_0_0._fields_ = [
    ("cdw0", ctypes.c_uint32),
    ("rsvd1", ctypes.c_uint32),
]

xnvme_spec_cpl_0._pack_ = 1  # source:False
xnvme_spec_cpl_0._anonymous_ = ("_0",)
xnvme_spec_cpl_0._fields_ = [
    ("_0", xnvme_spec_cpl_0_0),
    ("result", ctypes.c_uint64),
]

xnvme_spec_cpl._pack_ = 1  # source:False
xnvme_spec_cpl._anonymous_ = ("_0",)
xnvme_spec_cpl._fields_ = [
    ("_0", xnvme_spec_cpl_0),
    ("sqhd", ctypes.c_uint16),
    ("sqid", ctypes.c_uint16),
    ("cid", ctypes.c_uint16),
    ("status", xnvme_spec_status),
]


class xnvme_spec_log_health_entry(Structure):
    pass


xnvme_spec_log_health_entry._pack_ = 1  # source:True
xnvme_spec_log_health_entry._fields_ = [
    ("crit_warn", ctypes.c_ubyte),
    ("comp_temp", ctypes.c_uint16),
    ("avail_spare", ctypes.c_ubyte),
    ("avail_spare_thresh", ctypes.c_ubyte),
    ("pct_used", ctypes.c_ubyte),
    ("eg_crit_warn_sum", ctypes.c_ubyte),
    ("rsvd8", ctypes.c_ubyte * 25),
    ("data_units_read", ctypes.c_ubyte * 16),
    ("data_units_written", ctypes.c_ubyte * 16),
    ("host_read_cmds", ctypes.c_ubyte * 16),
    ("host_write_cmds", ctypes.c_ubyte * 16),
    ("ctrlr_busy_time", ctypes.c_ubyte * 16),
    ("pwr_cycles", ctypes.c_ubyte * 16),
    ("pwr_on_hours", ctypes.c_ubyte * 16),
    ("unsafe_shutdowns", ctypes.c_ubyte * 16),
    ("mdi_errs", ctypes.c_ubyte * 16),
    ("nr_err_logs", ctypes.c_ubyte * 16),
    ("warn_comp_temp_time", ctypes.c_uint32),
    ("crit_comp_temp_time", ctypes.c_uint32),
    ("temp_sens", ctypes.c_uint16 * 8),
    ("tmt1tc", ctypes.c_uint32),
    ("tmt2tc", ctypes.c_uint32),
    ("tttmt1", ctypes.c_uint32),
    ("tttmt2", ctypes.c_uint32),
    ("rsvd", ctypes.c_ubyte * 280),
]


class xnvme_spec_log_erri_entry(Structure):
    pass


xnvme_spec_log_erri_entry._pack_ = 1  # source:False
xnvme_spec_log_erri_entry._fields_ = [
    ("ecnt", ctypes.c_uint64),
    ("sqid", ctypes.c_uint16),
    ("cid", ctypes.c_uint16),
    ("status", xnvme_spec_status),
    ("eloc", ctypes.c_uint16),
    ("lba", ctypes.c_uint64),
    ("nsid", ctypes.c_uint32),
    ("ven_si", ctypes.c_ubyte),
    ("trtype", ctypes.c_ubyte),
    ("reserved30", ctypes.c_ubyte * 2),
    ("cmd_si", ctypes.c_uint64),
    ("trtype_si", ctypes.c_uint16),
    ("reserved42", ctypes.c_ubyte * 22),
]


class xnvme_spec_ruh_desc(Structure):
    pass


xnvme_spec_ruh_desc._pack_ = 1  # source:False
xnvme_spec_ruh_desc._fields_ = [
    ("ruht", ctypes.c_ubyte),
    ("rsvd", ctypes.c_ubyte * 3),
]


class xnvme_spec_fdp_conf_desc(Structure):
    pass


class xnvme_spec_fdp_conf_desc_fdpa(Union):
    pass


class xnvme_spec_fdp_conf_desc_0_0(Structure):
    pass


xnvme_spec_fdp_conf_desc_0_0._pack_ = 1  # source:False
xnvme_spec_fdp_conf_desc_0_0._fields_ = [
    ("rgif", ctypes.c_ubyte, 4),
    ("fdpvwc", ctypes.c_ubyte, 1),
    ("rsvd1", ctypes.c_ubyte, 2),
    ("fdpcv", ctypes.c_ubyte, 1),
]

xnvme_spec_fdp_conf_desc_fdpa._pack_ = 1  # source:False
xnvme_spec_fdp_conf_desc_fdpa._anonymous_ = ("_0",)
xnvme_spec_fdp_conf_desc_fdpa._fields_ = [
    ("_0", xnvme_spec_fdp_conf_desc_0_0),
    ("val", ctypes.c_ubyte),
]

xnvme_spec_fdp_conf_desc._pack_ = 1  # source:False
xnvme_spec_fdp_conf_desc._fields_ = [
    ("ds", ctypes.c_uint16),
    ("fdpa", xnvme_spec_fdp_conf_desc_fdpa),
    ("vss", ctypes.c_ubyte),
    ("nrg", ctypes.c_uint32),
    ("nruh", ctypes.c_uint16),
    ("maxpids", ctypes.c_uint16),
    ("nns", ctypes.c_uint32),
    ("runs", ctypes.c_uint64),
    ("erutl", ctypes.c_uint32),
    ("rsvd28", ctypes.c_ubyte * 36),
    ("ruh_desc", xnvme_spec_ruh_desc * 0),
]


class xnvme_spec_log_fdp_conf(Structure):
    pass


xnvme_spec_log_fdp_conf._pack_ = 1  # source:False
xnvme_spec_log_fdp_conf._fields_ = [
    ("ncfg", ctypes.c_uint16),
    ("version", ctypes.c_ubyte),
    ("rsvd1", ctypes.c_ubyte),
    ("size", ctypes.c_uint32),
    ("rsvd2", ctypes.c_ubyte * 8),
    ("conf_desc", xnvme_spec_fdp_conf_desc * 0),
]


class xnvme_spec_ruhu_desc(Structure):
    pass


xnvme_spec_ruhu_desc._pack_ = 1  # source:False
xnvme_spec_ruhu_desc._fields_ = [
    ("ruha", ctypes.c_ubyte),
    ("rsvd", ctypes.c_ubyte * 7),
]


class xnvme_spec_log_ruhu(Structure):
    pass


xnvme_spec_log_ruhu._pack_ = 1  # source:False
xnvme_spec_log_ruhu._fields_ = [
    ("nruh", ctypes.c_uint16),
    ("rsvd", ctypes.c_ubyte * 6),
    ("ruhu_desc", xnvme_spec_ruhu_desc * 0),
]


class xnvme_spec_log_fdp_stats(Structure):
    pass


xnvme_spec_log_fdp_stats._pack_ = 1  # source:False
xnvme_spec_log_fdp_stats._fields_ = [
    ("hbmw", ctypes.c_uint64 * 2),
    ("mbmw", ctypes.c_uint64 * 2),
    ("mbe", ctypes.c_uint64 * 2),
    ("rsvd48", ctypes.c_ubyte * 16),
]


class xnvme_spec_fdp_event_media_reallocated(Structure):
    pass


class xnvme_spec_fdp_event_media_reallocated_sef(Union):
    pass


class xnvme_spec_fdp_event_media_reallocated_0_0(Structure):
    pass


xnvme_spec_fdp_event_media_reallocated_0_0._pack_ = 1  # source:False
xnvme_spec_fdp_event_media_reallocated_0_0._fields_ = [
    ("lbav", ctypes.c_ubyte, 1),
    ("rsvd", ctypes.c_ubyte, 7),
]

xnvme_spec_fdp_event_media_reallocated_sef._pack_ = 1  # source:False
xnvme_spec_fdp_event_media_reallocated_sef._anonymous_ = ("_0",)
xnvme_spec_fdp_event_media_reallocated_sef._fields_ = [
    ("_0", xnvme_spec_fdp_event_media_reallocated_0_0),
    ("val", ctypes.c_ubyte),
]

xnvme_spec_fdp_event_media_reallocated._pack_ = 1  # source:True
xnvme_spec_fdp_event_media_reallocated._fields_ = [
    ("sef", xnvme_spec_fdp_event_media_reallocated_sef),
    ("rsvd1", ctypes.c_ubyte),
    ("nlbam", ctypes.c_uint16),
    ("lba", ctypes.c_uint64),
    ("rsvd2", ctypes.c_ubyte * 4),
]


class xnvme_spec_fdp_event(Structure):
    pass


class xnvme_spec_fdp_event_fdpef(Union):
    pass


class xnvme_spec_fdp_event_0_0(Structure):
    pass


xnvme_spec_fdp_event_0_0._pack_ = 1  # source:False
xnvme_spec_fdp_event_0_0._fields_ = [
    ("piv", ctypes.c_ubyte, 1),
    ("nsidv", ctypes.c_ubyte, 1),
    ("lv", ctypes.c_ubyte, 1),
    ("rsvd1", ctypes.c_ubyte, 5),
]

xnvme_spec_fdp_event_fdpef._pack_ = 1  # source:False
xnvme_spec_fdp_event_fdpef._anonymous_ = ("_0",)
xnvme_spec_fdp_event_fdpef._fields_ = [
    ("_0", xnvme_spec_fdp_event_0_0),
    ("val", ctypes.c_ubyte),
]

xnvme_spec_fdp_event._pack_ = 1  # source:True
xnvme_spec_fdp_event._fields_ = [
    ("type", ctypes.c_ubyte),
    ("fdpef", xnvme_spec_fdp_event_fdpef),
    ("pid", ctypes.c_uint16),
    ("timestamp", ctypes.c_uint64),
    ("nsid", ctypes.c_uint32),
    ("type_specific", ctypes.c_ubyte * 16),
    ("rgid", ctypes.c_uint16),
    ("ruhid", ctypes.c_uint16),
    ("rsvd1", ctypes.c_ubyte * 4),
    ("vs", ctypes.c_ubyte * 24),
]


class xnvme_spec_log_fdp_events(Structure):
    pass


xnvme_spec_log_fdp_events._pack_ = 1  # source:False
xnvme_spec_log_fdp_events._fields_ = [
    ("nevents", ctypes.c_uint32),
    ("rsvd", ctypes.c_ubyte * 60),
    ("event", xnvme_spec_fdp_event * 0),
]


class xnvme_spec_fdp_event_desc(Structure):
    pass


class xnvme_spec_fdp_event_desc_fdpeta(Union):
    pass


class xnvme_spec_fdp_event_desc_0_0(Structure):
    pass


xnvme_spec_fdp_event_desc_0_0._pack_ = 1  # source:False
xnvme_spec_fdp_event_desc_0_0._fields_ = [
    ("ee", ctypes.c_ubyte, 1),
    ("rsvd", ctypes.c_ubyte, 7),
]

xnvme_spec_fdp_event_desc_fdpeta._pack_ = 1  # source:False
xnvme_spec_fdp_event_desc_fdpeta._anonymous_ = ("_0",)
xnvme_spec_fdp_event_desc_fdpeta._fields_ = [
    ("_0", xnvme_spec_fdp_event_desc_0_0),
    ("val", ctypes.c_ubyte),
]

xnvme_spec_fdp_event_desc._pack_ = 1  # source:False
xnvme_spec_fdp_event_desc._fields_ = [
    ("type", ctypes.c_ubyte),
    ("fdpeta", xnvme_spec_fdp_event_desc_fdpeta),
]


# values for enumeration 'xnvme_spec_log_lpi'
xnvme_spec_log_lpi__enumvalues = {
    0: "XNVME_SPEC_LOG_RSVD",
    1: "XNVME_SPEC_LOG_ERRI",
    2: "XNVME_SPEC_LOG_HEALTH",
    3: "XNVME_SPEC_LOG_FW",
    4: "XNVME_SPEC_LOG_CHNS",
    5: "XNVME_SPEC_LOG_CSAE",
    6: "XNVME_SPEC_LOG_SELFTEST",
    7: "XNVME_SPEC_LOG_TELEHOST",
    8: "XNVME_SPEC_LOG_TELECTRLR",
    32: "XNVME_SPEC_LOG_FDPCONF",
    33: "XNVME_SPEC_LOG_FDPRUHU",
    34: "XNVME_SPEC_LOG_FDPSTATS",
    35: "XNVME_SPEC_LOG_FDPEVENTS",
}
XNVME_SPEC_LOG_RSVD = 0
XNVME_SPEC_LOG_ERRI = 1
XNVME_SPEC_LOG_HEALTH = 2
XNVME_SPEC_LOG_FW = 3
XNVME_SPEC_LOG_CHNS = 4
XNVME_SPEC_LOG_CSAE = 5
XNVME_SPEC_LOG_SELFTEST = 6
XNVME_SPEC_LOG_TELEHOST = 7
XNVME_SPEC_LOG_TELECTRLR = 8
XNVME_SPEC_LOG_FDPCONF = 32
XNVME_SPEC_LOG_FDPRUHU = 33
XNVME_SPEC_LOG_FDPSTATS = 34
XNVME_SPEC_LOG_FDPEVENTS = 35
xnvme_spec_log_lpi = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_io_mgmt_recv_mo'
xnvme_spec_io_mgmt_recv_mo__enumvalues = {
    1: "XNVME_SPEC_IO_MGMT_RECV_RUHS",
}
XNVME_SPEC_IO_MGMT_RECV_RUHS = 1
xnvme_spec_io_mgmt_recv_mo = ctypes.c_uint32  # enum


class xnvme_spec_ruhs_desc(Structure):
    pass


xnvme_spec_ruhs_desc._pack_ = 1  # source:False
xnvme_spec_ruhs_desc._fields_ = [
    ("pi", ctypes.c_uint16),
    ("ruhi", ctypes.c_uint16),
    ("earutr", ctypes.c_uint32),
    ("ruamw", ctypes.c_uint64),
    ("rsvd", ctypes.c_ubyte * 16),
]


class xnvme_spec_ruhs(Structure):
    pass


xnvme_spec_ruhs._pack_ = 1  # source:False
xnvme_spec_ruhs._fields_ = [
    ("rsvd", ctypes.c_ubyte * 14),
    ("nruhsd", ctypes.c_uint16),
    ("desc", xnvme_spec_ruhs_desc * 0),
]


# values for enumeration 'xnvme_spec_io_mgmt_send_mo'
xnvme_spec_io_mgmt_send_mo__enumvalues = {
    1: "XNVME_SPEC_IO_MGMT_SEND_RUHU",
}
XNVME_SPEC_IO_MGMT_SEND_RUHU = 1
xnvme_spec_io_mgmt_send_mo = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_idfy_cns'
xnvme_spec_idfy_cns__enumvalues = {
    0: "XNVME_SPEC_IDFY_NS",
    1: "XNVME_SPEC_IDFY_CTRLR",
    2: "XNVME_SPEC_IDFY_NSLIST",
    3: "XNVME_SPEC_IDFY_NSDSCR",
    4: "XNVME_SPEC_IDFY_SETL",
    5: "XNVME_SPEC_IDFY_NS_IOCS",
    6: "XNVME_SPEC_IDFY_CTRLR_IOCS",
    7: "XNVME_SPEC_IDFY_NSLIST_IOCS",
    16: "XNVME_SPEC_IDFY_NSLIST_ALLOC",
    17: "XNVME_SPEC_IDFY_NS_ALLOC",
    18: "XNVME_SPEC_IDFY_CTRLR_NS",
    19: "XNVME_SPEC_IDFY_CTRLR_SUB",
    20: "XNVME_SPEC_IDFY_CTRLR_PRI",
    21: "XNVME_SPEC_IDFY_CTRLR_SEC",
    22: "XNVME_SPEC_IDFY_NSGRAN",
    23: "XNVME_SPEC_IDFY_UUIDL",
    26: "XNVME_SPEC_IDFY_NSLIST_ALLOC_IOCS",
    27: "XNVME_SPEC_IDFY_NS_ALLOC_IOCS",
    28: "XNVME_SPEC_IDFY_IOCS",
}
XNVME_SPEC_IDFY_NS = 0
XNVME_SPEC_IDFY_CTRLR = 1
XNVME_SPEC_IDFY_NSLIST = 2
XNVME_SPEC_IDFY_NSDSCR = 3
XNVME_SPEC_IDFY_SETL = 4
XNVME_SPEC_IDFY_NS_IOCS = 5
XNVME_SPEC_IDFY_CTRLR_IOCS = 6
XNVME_SPEC_IDFY_NSLIST_IOCS = 7
XNVME_SPEC_IDFY_NSLIST_ALLOC = 16
XNVME_SPEC_IDFY_NS_ALLOC = 17
XNVME_SPEC_IDFY_CTRLR_NS = 18
XNVME_SPEC_IDFY_CTRLR_SUB = 19
XNVME_SPEC_IDFY_CTRLR_PRI = 20
XNVME_SPEC_IDFY_CTRLR_SEC = 21
XNVME_SPEC_IDFY_NSGRAN = 22
XNVME_SPEC_IDFY_UUIDL = 23
XNVME_SPEC_IDFY_NSLIST_ALLOC_IOCS = 26
XNVME_SPEC_IDFY_NS_ALLOC_IOCS = 27
XNVME_SPEC_IDFY_IOCS = 28
xnvme_spec_idfy_cns = ctypes.c_uint32  # enum


class xnvme_spec_lbaf(Structure):
    pass


xnvme_spec_lbaf._pack_ = 1  # source:False
xnvme_spec_lbaf._fields_ = [
    ("ms", ctypes.c_uint16),
    ("ds", ctypes.c_ubyte),
    ("rp", ctypes.c_ubyte, 2),
    ("rsvd", ctypes.c_ubyte, 6),
]


# values for enumeration 'xnvme_spec_csi'
xnvme_spec_csi__enumvalues = {
    0: "XNVME_SPEC_CSI_NVM",
    1: "XNVME_SPEC_CSI_KV",
    2: "XNVME_SPEC_CSI_ZONED",
}
XNVME_SPEC_CSI_NVM = 0
XNVME_SPEC_CSI_KV = 1
XNVME_SPEC_CSI_ZONED = 2
xnvme_spec_csi = ctypes.c_uint32  # enum


class xnvme_spec_idfy_ns_nsfeat(Structure):
    pass


xnvme_spec_idfy_ns_nsfeat._pack_ = 1  # source:False
xnvme_spec_idfy_ns_nsfeat._fields_ = [
    ("thin_prov", ctypes.c_ubyte, 1),
    ("ns_atomic_write_unit", ctypes.c_ubyte, 1),
    ("dealloc_or_unwritten_error", ctypes.c_ubyte, 1),
    ("guid_never_reused", ctypes.c_ubyte, 1),
    ("optimal_performance", ctypes.c_ubyte, 1),
    ("reserved1", ctypes.c_ubyte, 3),
]


class xnvme_spec_idfy_ns_flbas(Structure):
    pass


xnvme_spec_idfy_ns_flbas._pack_ = 1  # source:False
xnvme_spec_idfy_ns_flbas._fields_ = [
    ("format", ctypes.c_ubyte, 4),
    ("extended", ctypes.c_ubyte, 1),
    ("format_msb", ctypes.c_ubyte, 2),
    ("reserved2", ctypes.c_ubyte, 1),
]


class xnvme_spec_idfy_ns_mc(Structure):
    pass


xnvme_spec_idfy_ns_mc._pack_ = 1  # source:False
xnvme_spec_idfy_ns_mc._fields_ = [
    ("extended", ctypes.c_ubyte, 1),
    ("pointer", ctypes.c_ubyte, 1),
    ("reserved3", ctypes.c_ubyte, 6),
]


class xnvme_spec_idfy_ns_3_0(Structure):
    pass


xnvme_spec_idfy_ns_3_0._pack_ = 1  # source:False
xnvme_spec_idfy_ns_3_0._fields_ = [
    ("pit1", ctypes.c_ubyte, 1),
    ("pit2", ctypes.c_ubyte, 1),
    ("pit3", ctypes.c_ubyte, 1),
    ("md_start", ctypes.c_ubyte, 1),
    ("md_end", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 3),
]


class xnvme_spec_idfy_ns_dpc(Union):
    pass


xnvme_spec_idfy_ns_dpc._pack_ = 1  # source:False
xnvme_spec_idfy_ns_dpc._anonymous_ = ("_0",)
xnvme_spec_idfy_ns_dpc._fields_ = [
    ("_0", xnvme_spec_idfy_ns_3_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ns_4_0(Structure):
    pass


xnvme_spec_idfy_ns_4_0._pack_ = 1  # source:False
xnvme_spec_idfy_ns_4_0._fields_ = [
    ("pit", ctypes.c_ubyte, 3),
    ("md_start", ctypes.c_ubyte, 1),
    ("reserved4", ctypes.c_ubyte, 4),
]


class xnvme_spec_idfy_ns_dps(Union):
    pass


xnvme_spec_idfy_ns_dps._pack_ = 1  # source:False
xnvme_spec_idfy_ns_dps._anonymous_ = ("_0",)
xnvme_spec_idfy_ns_dps._fields_ = [
    ("_0", xnvme_spec_idfy_ns_4_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ns_nmic(Structure):
    pass


xnvme_spec_idfy_ns_nmic._pack_ = 1  # source:False
xnvme_spec_idfy_ns_nmic._fields_ = [
    ("can_share", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 7),
]


class xnvme_spec_idfy_ns_6_0(Structure):
    pass


xnvme_spec_idfy_ns_6_0._pack_ = 1  # source:False
xnvme_spec_idfy_ns_6_0._fields_ = [
    ("persist", ctypes.c_ubyte, 1),
    ("write_exclusive", ctypes.c_ubyte, 1),
    ("exclusive_access", ctypes.c_ubyte, 1),
    ("write_exclusive_reg_only", ctypes.c_ubyte, 1),
    ("exclusive_access_reg_only", ctypes.c_ubyte, 1),
    ("write_exclusive_all_reg", ctypes.c_ubyte, 1),
    ("exclusive_access_all_reg", ctypes.c_ubyte, 1),
    ("ignore_existing_key", ctypes.c_ubyte, 1),
]


class xnvme_spec_idfy_ns_nsrescap(Union):
    pass


xnvme_spec_idfy_ns_nsrescap._pack_ = 1  # source:False
xnvme_spec_idfy_ns_nsrescap._anonymous_ = ("_0",)
xnvme_spec_idfy_ns_nsrescap._fields_ = [
    ("_0", xnvme_spec_idfy_ns_6_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ns_7_0(Structure):
    pass


xnvme_spec_idfy_ns_7_0._pack_ = 1  # source:False
xnvme_spec_idfy_ns_7_0._fields_ = [
    ("percentage_remaining", ctypes.c_ubyte, 7),
    ("fpi_supported", ctypes.c_ubyte, 1),
]


class xnvme_spec_idfy_ns_fpi(Union):
    pass


xnvme_spec_idfy_ns_fpi._pack_ = 1  # source:False
xnvme_spec_idfy_ns_fpi._anonymous_ = ("_0",)
xnvme_spec_idfy_ns_fpi._fields_ = [
    ("_0", xnvme_spec_idfy_ns_7_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ns_8_bits(Structure):
    pass


xnvme_spec_idfy_ns_8_bits._pack_ = 1  # source:False
xnvme_spec_idfy_ns_8_bits._fields_ = [
    ("read_value", ctypes.c_ubyte, 3),
    ("write_zero_deallocate", ctypes.c_ubyte, 1),
    ("guard_value", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 3),
]


class xnvme_spec_idfy_ns_dlfeat(Union):
    pass


xnvme_spec_idfy_ns_dlfeat._pack_ = 1  # source:False
xnvme_spec_idfy_ns_dlfeat._fields_ = [
    ("bits", xnvme_spec_idfy_ns_8_bits),
    ("val", ctypes.c_ubyte),
]


class xnvme_pif(Structure):
    pass


class xnvme_pif_0(Union):
    pass


class xnvme_pif_0_g64(Structure):
    pass


xnvme_pif_0_g64._pack_ = 1  # source:False
xnvme_pif_0_g64._fields_ = [
    ("guard", ctypes.c_uint64),
    ("app_tag", ctypes.c_uint16),
    ("stor_ref_space_p1", ctypes.c_uint16),
    ("stor_ref_space_p2", ctypes.c_uint32),
]


class xnvme_pif_0_g16(Structure):
    pass


xnvme_pif_0_g16._pack_ = 1  # source:False
xnvme_pif_0_g16._fields_ = [
    ("guard", ctypes.c_uint16),
    ("app_tag", ctypes.c_uint16),
    ("stor_ref_space", ctypes.c_uint32),
]

xnvme_pif_0._pack_ = 1  # source:False
xnvme_pif_0._fields_ = [
    ("g16", xnvme_pif_0_g16),
    ("g64", xnvme_pif_0_g64),
]

xnvme_pif._pack_ = 1  # source:False
xnvme_pif._anonymous_ = ("_0",)
xnvme_pif._fields_ = [
    ("_0", xnvme_pif_0),
]


# values for enumeration 'xnvme_spec_nvm_ns_pif'
xnvme_spec_nvm_ns_pif__enumvalues = {
    0: "XNVME_SPEC_NVM_NS_16B_GUARD",
    1: "XNVME_SPEC_NVM_NS_32B_GUARD",
    2: "XNVME_SPEC_NVM_NS_64B_GUARD",
}
XNVME_SPEC_NVM_NS_16B_GUARD = 0
XNVME_SPEC_NVM_NS_32B_GUARD = 1
XNVME_SPEC_NVM_NS_64B_GUARD = 2
xnvme_spec_nvm_ns_pif = ctypes.c_uint32  # enum


class xnvme_spec_elbaf(Structure):
    pass


xnvme_spec_elbaf._pack_ = 1  # source:False
xnvme_spec_elbaf._fields_ = [
    ("sts", ctypes.c_uint32, 7),
    ("pif", ctypes.c_uint32, 2),
    ("rsvd", ctypes.c_uint32, 23),
]


class xnvme_spec_nvm_idfy_ns_iocs(Structure):
    pass


class xnvme_spec_nvm_idfy_ns_iocs_pic(Union):
    pass


class xnvme_spec_nvm_idfy_ns_iocs_0_0(Structure):
    pass


xnvme_spec_nvm_idfy_ns_iocs_0_0._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ns_iocs_0_0._fields_ = [
    ("gpistm", ctypes.c_ubyte, 1),
    ("gpists", ctypes.c_ubyte, 1),
    ("reserved1", ctypes.c_ubyte, 6),
]

xnvme_spec_nvm_idfy_ns_iocs_pic._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ns_iocs_pic._anonymous_ = ("_0",)
xnvme_spec_nvm_idfy_ns_iocs_pic._fields_ = [
    ("_0", xnvme_spec_nvm_idfy_ns_iocs_0_0),
    ("val", ctypes.c_ubyte),
]

xnvme_spec_nvm_idfy_ns_iocs._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ns_iocs._fields_ = [
    ("lbstm", ctypes.c_uint64),
    ("pic", xnvme_spec_nvm_idfy_ns_iocs_pic),
    ("reserved9", ctypes.c_ubyte * 3),
    ("elbaf", xnvme_spec_elbaf * 64),
    ("reserved268", ctypes.c_ubyte * 3828),
]


class xnvme_spec_power_state(Structure):
    pass


xnvme_spec_power_state._pack_ = 1  # source:False
xnvme_spec_power_state._fields_ = [
    ("mp", ctypes.c_uint16),
    ("reserved1", ctypes.c_ubyte),
    ("mps", ctypes.c_ubyte, 1),
    ("nops", ctypes.c_ubyte, 1),
    ("reserved2", ctypes.c_ubyte, 6),
    ("enlat", ctypes.c_uint32),
    ("exlat", ctypes.c_uint32),
    ("rrt", ctypes.c_ubyte, 5),
    ("reserved3", ctypes.c_ubyte, 3),
    ("rrl", ctypes.c_ubyte, 5),
    ("reserved4", ctypes.c_ubyte, 3),
    ("rwt", ctypes.c_ubyte, 5),
    ("reserved5", ctypes.c_ubyte, 3),
    ("rwl", ctypes.c_ubyte, 5),
    ("reserved6", ctypes.c_ubyte, 3),
    ("idlp", ctypes.c_uint16),
    ("reserved7", ctypes.c_ubyte, 6),
    ("ips", ctypes.c_ubyte, 2),
    ("reserved8", ctypes.c_ubyte, 8),
    ("actp", ctypes.c_uint16),
    ("apw", ctypes.c_ubyte, 3),
    ("reserved9", ctypes.c_ubyte, 3),
    ("aps", ctypes.c_ubyte, 2),
    ("reserved10", ctypes.c_ubyte * 9),
]


class xnvme_spec_vs_register(Union):
    pass


class xnvme_spec_vs_register_bits(Structure):
    pass


xnvme_spec_vs_register_bits._pack_ = 1  # source:False
xnvme_spec_vs_register_bits._fields_ = [
    ("ter", ctypes.c_uint32, 8),
    ("mnr", ctypes.c_uint32, 8),
    ("mjr", ctypes.c_uint32, 16),
]

xnvme_spec_vs_register._pack_ = 1  # source:False
xnvme_spec_vs_register._fields_ = [
    ("bits", xnvme_spec_vs_register_bits),
    ("val", ctypes.c_uint32),
]


class xnvme_spec_idfy_ctrlr_0_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_0_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_0_0._fields_ = [
    ("multi_port", ctypes.c_ubyte, 1),
    ("multi_host", ctypes.c_ubyte, 1),
    ("sr_iov", ctypes.c_ubyte, 1),
    ("ana_rprt", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 4),
]


class xnvme_spec_idfy_ctrlr_cmic(Union):
    pass


xnvme_spec_idfy_ctrlr_cmic._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_cmic._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_cmic._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_0_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_1_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_1_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_1_0._fields_ = [
    ("reserved1", ctypes.c_uint32, 8),
    ("ns_attribute_notices", ctypes.c_uint32, 1),
    ("fw_activation_notices", ctypes.c_uint32, 1),
    ("reserved2", ctypes.c_uint32, 1),
    ("ana_notices", ctypes.c_uint32, 1),
    ("pleal_notices", ctypes.c_uint32, 1),
    ("lba_sia_notices", ctypes.c_uint32, 1),
    ("egea_notices", ctypes.c_uint32, 1),
    ("normal_nvm_ss", ctypes.c_uint32, 1),
    ("reserved3", ctypes.c_uint32, 11),
    ("zone_changes", ctypes.c_uint32, 1),
    ("reserved4", ctypes.c_uint32, 3),
    ("discovery_log_notices", ctypes.c_uint32, 1),
]


class xnvme_spec_idfy_ctrlr_oaes(Union):
    pass


xnvme_spec_idfy_ctrlr_oaes._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_oaes._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_oaes._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_1_0),
    ("val", ctypes.c_uint32),
]


class xnvme_spec_idfy_ctrlr_2_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_2_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_2_0._fields_ = [
    ("host_id_exhid_supported", ctypes.c_uint32, 1),
    ("non_operational_power_state_permissive_mode", ctypes.c_uint32, 1),
    ("nvm_sets", ctypes.c_uint32, 1),
    ("read_recovery_levels", ctypes.c_uint32, 1),
    ("endurance_groups", ctypes.c_uint32, 1),
    ("predictable_latency_mode", ctypes.c_uint32, 1),
    ("tbkas", ctypes.c_uint32, 1),
    ("namespace_granularity", ctypes.c_uint32, 1),
    ("sq_associations", ctypes.c_uint32, 1),
    ("uuid_list", ctypes.c_uint32, 1),
    ("multi_domain_subsystem", ctypes.c_uint32, 1),
    ("fixed_capacity_management", ctypes.c_uint32, 1),
    ("variable_capacity_management", ctypes.c_uint32, 1),
    ("delete_endurance_group", ctypes.c_uint32, 1),
    ("delete_nvm_set", ctypes.c_uint32, 1),
    ("extended_lba_formats", ctypes.c_uint32, 1),
    ("reserved1", ctypes.c_uint32, 3),
    ("flexible_data_placement", ctypes.c_uint32, 1),
    ("reserved2", ctypes.c_uint32, 12),
]


class xnvme_spec_idfy_ctrlr_ctratt(Union):
    pass


xnvme_spec_idfy_ctrlr_ctratt._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_ctratt._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_ctratt._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_2_0),
    ("val", ctypes.c_uint32),
]


class xnvme_spec_idfy_ctrlr_3_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_3_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_3_0._fields_ = [
    ("nvmesd", ctypes.c_ubyte, 1),
    ("nvmee", ctypes.c_ubyte, 1),
    ("nvmsr_rsvd", ctypes.c_ubyte, 6),
]


class xnvme_spec_idfy_ctrlr_nvmsr(Union):
    pass


xnvme_spec_idfy_ctrlr_nvmsr._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_nvmsr._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_nvmsr._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_3_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_4_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_4_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_4_0._fields_ = [
    ("vwcr", ctypes.c_ubyte, 7),
    ("vwcrv", ctypes.c_ubyte, 1),
]


class xnvme_spec_idfy_ctrlr_vwci(Union):
    pass


xnvme_spec_idfy_ctrlr_vwci._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_vwci._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_vwci._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_4_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_5_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_5_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_5_0._fields_ = [
    ("smbusme", ctypes.c_ubyte, 1),
    ("pcieme", ctypes.c_ubyte, 1),
    ("mec_rsvd", ctypes.c_ubyte, 6),
]


class xnvme_spec_idfy_ctrlr_mec(Union):
    pass


xnvme_spec_idfy_ctrlr_mec._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_mec._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_mec._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_5_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_6_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_6_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_6_0._fields_ = [
    ("security", ctypes.c_uint16, 1),
    ("format", ctypes.c_uint16, 1),
    ("firmware", ctypes.c_uint16, 1),
    ("ns_manage", ctypes.c_uint16, 1),
    ("device_self_test", ctypes.c_uint16, 1),
    ("directives", ctypes.c_uint16, 1),
    ("nvme_mi", ctypes.c_uint16, 1),
    ("virtualization_management", ctypes.c_uint16, 1),
    ("doorbell_buffer_config", ctypes.c_uint16, 1),
    ("lba_status", ctypes.c_uint16, 1),
    ("cmd_feature_lockdown", ctypes.c_uint16, 1),
    ("oacs_rsvd", ctypes.c_uint16, 5),
]


class xnvme_spec_idfy_ctrlr_oacs(Union):
    pass


xnvme_spec_idfy_ctrlr_oacs._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_oacs._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_oacs._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_6_0),
    ("val", ctypes.c_uint16),
]


class xnvme_spec_idfy_ctrlr_7_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_7_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_7_0._fields_ = [
    ("slot1_ro", ctypes.c_ubyte, 1),
    ("num_slots", ctypes.c_ubyte, 3),
    ("activation_without_reset", ctypes.c_ubyte, 1),
    ("mul_update_detection", ctypes.c_ubyte, 1),
    ("frmw_rsvd", ctypes.c_ubyte, 2),
]


class xnvme_spec_idfy_ctrlr_frmw(Union):
    pass


xnvme_spec_idfy_ctrlr_frmw._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_frmw._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_frmw._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_7_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_8_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_8_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_8_0._fields_ = [
    ("ns_smart", ctypes.c_ubyte, 1),
    ("celp", ctypes.c_ubyte, 1),
    ("edlp", ctypes.c_ubyte, 1),
    ("telemetry", ctypes.c_ubyte, 1),
    ("pel", ctypes.c_ubyte, 1),
    ("mel", ctypes.c_ubyte, 1),
    ("tel_da4", ctypes.c_ubyte, 1),
    ("lpa_rsvd", ctypes.c_ubyte, 1),
]


class xnvme_spec_idfy_ctrlr_lpa(Union):
    pass


xnvme_spec_idfy_ctrlr_lpa._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_lpa._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_lpa._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_8_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_9_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_9_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_9_0._fields_ = [
    ("spec_format", ctypes.c_ubyte, 1),
    ("avscc_rsvd", ctypes.c_ubyte, 7),
]


class xnvme_spec_idfy_ctrlr_avscc(Union):
    pass


xnvme_spec_idfy_ctrlr_avscc._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_avscc._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_avscc._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_9_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_10_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_10_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_10_0._fields_ = [
    ("supported", ctypes.c_ubyte, 1),
    ("apsta_rsvd", ctypes.c_ubyte, 7),
]


class xnvme_spec_idfy_ctrlr_apsta(Union):
    pass


xnvme_spec_idfy_ctrlr_apsta._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_apsta._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_apsta._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_10_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_11_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_11_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_11_0._fields_ = [
    ("num_rpmb_units", ctypes.c_ubyte, 3),
    ("auth_method", ctypes.c_ubyte, 3),
    ("reserved1", ctypes.c_ubyte, 2),
    ("reserved2", ctypes.c_ubyte, 8),
    ("total_size", ctypes.c_ubyte),
    ("access_size", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_rpmbs(Union):
    pass


xnvme_spec_idfy_ctrlr_rpmbs._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_rpmbs._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_rpmbs._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_11_0),
    ("val", ctypes.c_uint32),
]


class xnvme_spec_idfy_ctrlr_12_bits(Structure):
    pass


xnvme_spec_idfy_ctrlr_12_bits._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_12_bits._fields_ = [
    ("one_only", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 7),
]


class xnvme_spec_idfy_ctrlr_dsto(Union):
    pass


xnvme_spec_idfy_ctrlr_dsto._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_dsto._fields_ = [
    ("bits", xnvme_spec_idfy_ctrlr_12_bits),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_13_bits(Structure):
    pass


xnvme_spec_idfy_ctrlr_13_bits._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_13_bits._fields_ = [
    ("supported", ctypes.c_uint16, 1),
    ("reserved", ctypes.c_uint16, 15),
]


class xnvme_spec_idfy_ctrlr_hctma(Union):
    pass


xnvme_spec_idfy_ctrlr_hctma._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_hctma._fields_ = [
    ("bits", xnvme_spec_idfy_ctrlr_13_bits),
    ("val", ctypes.c_uint16),
]


class xnvme_spec_idfy_ctrlr_14_bits(Structure):
    pass


xnvme_spec_idfy_ctrlr_14_bits._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_14_bits._fields_ = [
    ("crypto_erase", ctypes.c_uint32, 1),
    ("block_erase", ctypes.c_uint32, 1),
    ("overwrite", ctypes.c_uint32, 1),
    ("reserved", ctypes.c_uint32, 26),
    ("ndi", ctypes.c_uint32, 1),
    ("nodmmas", ctypes.c_uint32, 2),
]


class xnvme_spec_idfy_ctrlr_sanicap(Union):
    pass


xnvme_spec_idfy_ctrlr_sanicap._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_sanicap._fields_ = [
    ("bits", xnvme_spec_idfy_ctrlr_14_bits),
    ("val", ctypes.c_uint32),
]


class xnvme_spec_idfy_ctrlr_15_bits(Structure):
    pass


xnvme_spec_idfy_ctrlr_15_bits._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_15_bits._fields_ = [
    ("optimize", ctypes.c_ubyte, 1),
    ("non_optimize", ctypes.c_ubyte, 1),
    ("inaccessible", ctypes.c_ubyte, 1),
    ("persist_loss", ctypes.c_ubyte, 1),
    ("change", ctypes.c_ubyte, 1),
    ("reserved1", ctypes.c_ubyte, 1),
    ("ns_anagrpid", ctypes.c_ubyte, 1),
    ("mgt_anagrpid", ctypes.c_ubyte, 1),
]


class xnvme_spec_idfy_ctrlr_anacap(Union):
    pass


xnvme_spec_idfy_ctrlr_anacap._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_anacap._fields_ = [
    ("bits", xnvme_spec_idfy_ctrlr_15_bits),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_16_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_16_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_16_0._fields_ = [
    ("min", ctypes.c_ubyte, 4),
    ("max", ctypes.c_ubyte, 4),
]


class xnvme_spec_idfy_ctrlr_sqes(Union):
    pass


xnvme_spec_idfy_ctrlr_sqes._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_sqes._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_sqes._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_16_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_17_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_17_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_17_0._fields_ = [
    ("min", ctypes.c_ubyte, 4),
    ("max", ctypes.c_ubyte, 4),
]


class xnvme_spec_idfy_ctrlr_cqes(Union):
    pass


xnvme_spec_idfy_ctrlr_cqes._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_cqes._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_cqes._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_17_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_18_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_18_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_18_0._fields_ = [
    ("compare", ctypes.c_uint16, 1),
    ("write_unc", ctypes.c_uint16, 1),
    ("dsm", ctypes.c_uint16, 1),
    ("write_zeroes", ctypes.c_uint16, 1),
    ("set_features_save", ctypes.c_uint16, 1),
    ("reservations", ctypes.c_uint16, 1),
    ("timestamp", ctypes.c_uint16, 1),
    ("verify", ctypes.c_uint16, 1),
    ("copy", ctypes.c_uint16, 1),
    ("reserved", ctypes.c_uint16, 7),
]


class xnvme_spec_idfy_ctrlr_oncs(Union):
    pass


xnvme_spec_idfy_ctrlr_oncs._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_oncs._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_oncs._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_18_0),
    ("val", ctypes.c_uint16),
]


class xnvme_spec_idfy_ctrlr_19_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_19_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_19_0._fields_ = [
    ("format_all_ns", ctypes.c_ubyte, 1),
    ("erase_all_ns", ctypes.c_ubyte, 1),
    ("crypto_erase_supported", ctypes.c_ubyte, 1),
    ("nsid_ffffffff", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 4),
]


class xnvme_spec_idfy_ctrlr_fna(Union):
    pass


xnvme_spec_idfy_ctrlr_fna._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_fna._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_fna._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_19_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_20_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_20_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_20_0._fields_ = [
    ("present", ctypes.c_ubyte, 1),
    ("flush_broadcast", ctypes.c_ubyte, 2),
    ("reserved", ctypes.c_ubyte, 5),
]


class xnvme_spec_idfy_ctrlr_vwc(Union):
    pass


xnvme_spec_idfy_ctrlr_vwc._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_vwc._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_vwc._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_20_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_idfy_ctrlr_21_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_21_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_21_0._fields_ = [
    ("format0", ctypes.c_uint16, 1),
    ("format1", ctypes.c_uint16, 1),
    ("reserved", ctypes.c_uint16, 14),
]


class xnvme_spec_idfy_ctrlr_cdfs(Union):
    pass


xnvme_spec_idfy_ctrlr_cdfs._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_cdfs._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_cdfs._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_21_0),
    ("val", ctypes.c_uint16),
]


class xnvme_spec_idfy_ctrlr_22_0(Structure):
    pass


xnvme_spec_idfy_ctrlr_22_0._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_22_0._fields_ = [
    ("supported", ctypes.c_uint32, 2),
    ("keyed_sgl", ctypes.c_uint32, 1),
    ("reserved1", ctypes.c_uint32, 5),
    ("sgl_desc_threshold", ctypes.c_uint32, 8),
    ("bit_bucket_descriptor", ctypes.c_uint32, 1),
    ("metadata_pointer", ctypes.c_uint32, 1),
    ("oversized_sgl", ctypes.c_uint32, 1),
    ("metadata_address", ctypes.c_uint32, 1),
    ("sgl_offset", ctypes.c_uint32, 1),
    ("transport_sgl", ctypes.c_uint32, 1),
    ("reserved2", ctypes.c_uint32, 10),
]


class xnvme_spec_idfy_ctrlr_sgls(Union):
    pass


xnvme_spec_idfy_ctrlr_sgls._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_sgls._anonymous_ = ("_0",)
xnvme_spec_idfy_ctrlr_sgls._fields_ = [
    ("_0", xnvme_spec_idfy_ctrlr_22_0),
    ("val", ctypes.c_uint32),
]


class xnvme_spec_idfy_ctrlr_23_ctrattr(Structure):
    pass


xnvme_spec_idfy_ctrlr_23_ctrattr._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_23_ctrattr._fields_ = [
    ("ctrlr_model", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 7),
]


class xnvme_spec_idfy_ctrlr_23_ofcs(Structure):
    pass


xnvme_spec_idfy_ctrlr_23_ofcs._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_23_ofcs._fields_ = [
    ("disc_del", ctypes.c_uint16, 1),
    ("reserved", ctypes.c_uint16, 15),
]


class xnvme_spec_idfy_ctrlr_nvmf_specific(Structure):
    pass


xnvme_spec_idfy_ctrlr_nvmf_specific._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr_nvmf_specific._fields_ = [
    ("ioccsz", ctypes.c_uint32),
    ("iorcsz", ctypes.c_uint32),
    ("icdoff", ctypes.c_uint16),
    ("ctrattr", xnvme_spec_idfy_ctrlr_23_ctrattr),
    ("msdbd", ctypes.c_ubyte),
    ("ofcs", xnvme_spec_idfy_ctrlr_23_ofcs),
    ("reserved", ctypes.c_ubyte * 242),
]


class xnvme_spec_cs_vector(Structure):
    pass


class xnvme_spec_cs_vector_0(Union):
    pass


class xnvme_spec_cs_vector_0_0(Structure):
    pass


xnvme_spec_cs_vector_0_0._pack_ = 1  # source:False
xnvme_spec_cs_vector_0_0._fields_ = [
    ("nvm", ctypes.c_uint64, 1),
    ("kv", ctypes.c_uint64, 1),
    ("zns", ctypes.c_uint64, 1),
    ("rsvd", ctypes.c_uint64, 61),
]

xnvme_spec_cs_vector_0._pack_ = 1  # source:False
xnvme_spec_cs_vector_0._anonymous_ = ("_0",)
xnvme_spec_cs_vector_0._fields_ = [
    ("_0", xnvme_spec_cs_vector_0_0),
    ("val", ctypes.c_uint64),
]

xnvme_spec_cs_vector._pack_ = 1  # source:False
xnvme_spec_cs_vector._anonymous_ = ("_0",)
xnvme_spec_cs_vector._fields_ = [
    ("_0", xnvme_spec_cs_vector_0),
]


class xnvme_spec_idfy_cs(Structure):
    _pack_ = 1  # source:False
    _fields_ = [
        ("iocsc", xnvme_spec_cs_vector * 512),
    ]


class xnvme_spec_idfy(Structure):
    pass


class xnvme_spec_idfy_0(Union):
    pass


xnvme_spec_idfy_ctrlr._pack_ = 1  # source:False
xnvme_spec_idfy_ctrlr._fields_ = [
    ("vid", ctypes.c_uint16),
    ("ssvid", ctypes.c_uint16),
    ("sn", ctypes.c_byte * 20),
    ("mn", ctypes.c_byte * 40),
    ("fr", ctypes.c_ubyte * 8),
    ("rab", ctypes.c_ubyte),
    ("ieee", ctypes.c_ubyte * 3),
    ("cmic", xnvme_spec_idfy_ctrlr_cmic),
    ("mdts", ctypes.c_ubyte),
    ("cntlid", ctypes.c_uint16),
    ("ver", xnvme_spec_vs_register),
    ("rtd3r", ctypes.c_uint32),
    ("rtd3e", ctypes.c_uint32),
    ("oaes", xnvme_spec_idfy_ctrlr_oaes),
    ("ctratt", xnvme_spec_idfy_ctrlr_ctratt),
    ("rrls", ctypes.c_uint16),
    ("reserved_102", ctypes.c_ubyte * 9),
    ("cntrltype", ctypes.c_ubyte),
    ("fguid", ctypes.c_ubyte * 16),
    ("crdt1", ctypes.c_uint16),
    ("crdt2", ctypes.c_uint16),
    ("crdt3", ctypes.c_uint16),
    ("reserved_134", ctypes.c_ubyte * 119),
    ("nvmsr", xnvme_spec_idfy_ctrlr_nvmsr),
    ("vwci", xnvme_spec_idfy_ctrlr_vwci),
    ("mec", xnvme_spec_idfy_ctrlr_mec),
    ("oacs", xnvme_spec_idfy_ctrlr_oacs),
    ("acl", ctypes.c_ubyte),
    ("aerl", ctypes.c_ubyte),
    ("frmw", xnvme_spec_idfy_ctrlr_frmw),
    ("lpa", xnvme_spec_idfy_ctrlr_lpa),
    ("elpe", ctypes.c_ubyte),
    ("npss", ctypes.c_ubyte),
    ("avscc", xnvme_spec_idfy_ctrlr_avscc),
    ("apsta", xnvme_spec_idfy_ctrlr_apsta),
    ("wctemp", ctypes.c_uint16),
    ("cctemp", ctypes.c_uint16),
    ("mtfa", ctypes.c_uint16),
    ("hmpre", ctypes.c_uint32),
    ("hmmin", ctypes.c_uint32),
    ("tnvmcap", ctypes.c_uint64 * 2),
    ("unvmcap", ctypes.c_uint64 * 2),
    ("rpmbs", xnvme_spec_idfy_ctrlr_rpmbs),
    ("edstt", ctypes.c_uint16),
    ("dsto", xnvme_spec_idfy_ctrlr_dsto),
    ("fwug", ctypes.c_ubyte),
    ("kas", ctypes.c_uint16),
    ("hctma", xnvme_spec_idfy_ctrlr_hctma),
    ("mntmt", ctypes.c_uint16),
    ("mxtmt", ctypes.c_uint16),
    ("sanicap", xnvme_spec_idfy_ctrlr_sanicap),
    ("hmminds", ctypes.c_uint32),
    ("hmmaxd", ctypes.c_uint16),
    ("nsetidmax", ctypes.c_uint16),
    ("endgidmax", ctypes.c_uint16),
    ("anatt", ctypes.c_ubyte),
    ("anacap", xnvme_spec_idfy_ctrlr_anacap),
    ("anagrpmax", ctypes.c_uint32),
    ("nanagrpid", ctypes.c_uint32),
    ("pels", ctypes.c_uint32),
    ("domain_identifier", ctypes.c_uint16),
    ("reserved_358", ctypes.c_ubyte * 10),
    ("megcap", ctypes.c_uint64 * 2),
    ("reserved_384", ctypes.c_ubyte * 128),
    ("sqes", xnvme_spec_idfy_ctrlr_sqes),
    ("cqes", xnvme_spec_idfy_ctrlr_cqes),
    ("maxcmd", ctypes.c_uint16),
    ("nn", ctypes.c_uint32),
    ("oncs", xnvme_spec_idfy_ctrlr_oncs),
    ("fuses", ctypes.c_uint16),
    ("fna", xnvme_spec_idfy_ctrlr_fna),
    ("vwc", xnvme_spec_idfy_ctrlr_vwc),
    ("awun", ctypes.c_uint16),
    ("awupf", ctypes.c_uint16),
    ("nvscc", ctypes.c_ubyte),
    ("nwpc", ctypes.c_ubyte),
    ("acwu", ctypes.c_uint16),
    ("cdfs", xnvme_spec_idfy_ctrlr_cdfs),
    ("sgls", xnvme_spec_idfy_ctrlr_sgls),
    ("mnan", ctypes.c_uint32),
    ("maxdna", ctypes.c_uint64 * 2),
    ("maxcna", ctypes.c_uint32),
    ("reserved_564", ctypes.c_ubyte * 204),
    ("subnqn", ctypes.c_ubyte * 256),
    ("reserved_1024", ctypes.c_ubyte * 768),
    ("nvmf_specific", xnvme_spec_idfy_ctrlr_nvmf_specific),
    ("psd", xnvme_spec_power_state * 32),
    ("vs", ctypes.c_ubyte * 1024),
]

xnvme_spec_idfy_ns._pack_ = 1  # source:False
xnvme_spec_idfy_ns._fields_ = [
    ("nsze", ctypes.c_uint64),
    ("ncap", ctypes.c_uint64),
    ("nuse", ctypes.c_uint64),
    ("nsfeat", xnvme_spec_idfy_ns_nsfeat),
    ("nlbaf", ctypes.c_ubyte),
    ("flbas", xnvme_spec_idfy_ns_flbas),
    ("mc", xnvme_spec_idfy_ns_mc),
    ("dpc", xnvme_spec_idfy_ns_dpc),
    ("dps", xnvme_spec_idfy_ns_dps),
    ("nmic", xnvme_spec_idfy_ns_nmic),
    ("nsrescap", xnvme_spec_idfy_ns_nsrescap),
    ("fpi", xnvme_spec_idfy_ns_fpi),
    ("dlfeat", xnvme_spec_idfy_ns_dlfeat),
    ("nawun", ctypes.c_uint16),
    ("nawupf", ctypes.c_uint16),
    ("nacwu", ctypes.c_uint16),
    ("nabsn", ctypes.c_uint16),
    ("nabo", ctypes.c_uint16),
    ("nabspf", ctypes.c_uint16),
    ("noiob", ctypes.c_uint16),
    ("nvmcap", ctypes.c_uint64 * 2),
    ("npwg", ctypes.c_uint16),
    ("npwa", ctypes.c_uint16),
    ("npdg", ctypes.c_uint16),
    ("npda", ctypes.c_uint16),
    ("nows", ctypes.c_uint16),
    ("mssrl", ctypes.c_uint16),
    ("mcl", ctypes.c_uint32),
    ("msrc", ctypes.c_ubyte),
    ("reserved81", ctypes.c_ubyte * 11),
    ("anagrpid", ctypes.c_uint32),
    ("reserved96", ctypes.c_ubyte * 3),
    ("nsattr", ctypes.c_ubyte),
    ("nvmsetid", ctypes.c_uint16),
    ("endgid", ctypes.c_uint16),
    ("nguid", ctypes.c_ubyte * 16),
    ("eui64", ctypes.c_uint64),
    ("lbaf", xnvme_spec_lbaf * 64),
    ("vendor_specific", ctypes.c_ubyte * 3712),
]

xnvme_spec_idfy_0._pack_ = 1  # source:False
xnvme_spec_idfy_0._fields_ = [
    ("ctrlr", xnvme_spec_idfy_ctrlr),
    ("ns", xnvme_spec_idfy_ns),
    ("cs", xnvme_spec_idfy_cs),
]

xnvme_spec_idfy._pack_ = 1  # source:False
xnvme_spec_idfy._anonymous_ = ("_0",)
xnvme_spec_idfy._fields_ = [
    ("_0", xnvme_spec_idfy_0),
]


# values for enumeration 'xnvme_spec_adm_opc'
xnvme_spec_adm_opc__enumvalues = {
    2: "XNVME_SPEC_ADM_OPC_LOG",
    6: "XNVME_SPEC_ADM_OPC_IDFY",
    9: "XNVME_SPEC_ADM_OPC_SFEAT",
    10: "XNVME_SPEC_ADM_OPC_GFEAT",
    25: "XNVME_SPEC_ADM_OPC_DSEND",
    26: "XNVME_SPEC_ADM_OPC_DRECV",
}
XNVME_SPEC_ADM_OPC_LOG = 2
XNVME_SPEC_ADM_OPC_IDFY = 6
XNVME_SPEC_ADM_OPC_SFEAT = 9
XNVME_SPEC_ADM_OPC_GFEAT = 10
XNVME_SPEC_ADM_OPC_DSEND = 25
XNVME_SPEC_ADM_OPC_DRECV = 26
xnvme_spec_adm_opc = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_nvm_opc'
xnvme_spec_nvm_opc__enumvalues = {
    0: "XNVME_SPEC_NVM_OPC_FLUSH",
    1: "XNVME_SPEC_NVM_OPC_WRITE",
    2: "XNVME_SPEC_NVM_OPC_READ",
    4: "XNVME_SPEC_NVM_OPC_WRITE_UNCORRECTABLE",
    5: "XNVME_SPEC_NVM_OPC_COMPARE",
    8: "XNVME_SPEC_NVM_OPC_WRITE_ZEROES",
    9: "XNVME_SPEC_NVM_OPC_DATASET_MANAGEMENT",
    25: "XNVME_SPEC_NVM_OPC_SCOPY",
    18: "XNVME_SPEC_NVM_OPC_IO_MGMT_RECV",
    29: "XNVME_SPEC_NVM_OPC_IO_MGMT_SEND",
    128: "XNVME_SPEC_NVM_OPC_FMT",
    132: "XNVME_SPEC_NVM_OPC_SANITIZE",
}
XNVME_SPEC_NVM_OPC_FLUSH = 0
XNVME_SPEC_NVM_OPC_WRITE = 1
XNVME_SPEC_NVM_OPC_READ = 2
XNVME_SPEC_NVM_OPC_WRITE_UNCORRECTABLE = 4
XNVME_SPEC_NVM_OPC_COMPARE = 5
XNVME_SPEC_NVM_OPC_WRITE_ZEROES = 8
XNVME_SPEC_NVM_OPC_DATASET_MANAGEMENT = 9
XNVME_SPEC_NVM_OPC_SCOPY = 25
XNVME_SPEC_NVM_OPC_IO_MGMT_RECV = 18
XNVME_SPEC_NVM_OPC_IO_MGMT_SEND = 29
XNVME_SPEC_NVM_OPC_FMT = 128
XNVME_SPEC_NVM_OPC_SANITIZE = 132
xnvme_spec_nvm_opc = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_feat_id'
xnvme_spec_feat_id__enumvalues = {
    1: "XNVME_SPEC_FEAT_ARBITRATION",
    2: "XNVME_SPEC_FEAT_PWR_MGMT",
    3: "XNVME_SPEC_FEAT_LBA_RANGETYPE",
    4: "XNVME_SPEC_FEAT_TEMP_THRESHOLD",
    5: "XNVME_SPEC_FEAT_ERROR_RECOVERY",
    6: "XNVME_SPEC_FEAT_VWCACHE",
    7: "XNVME_SPEC_FEAT_NQUEUES",
    29: "XNVME_SPEC_FEAT_FDP_MODE",
    30: "XNVME_SPEC_FEAT_FDP_EVENTS",
}
XNVME_SPEC_FEAT_ARBITRATION = 1
XNVME_SPEC_FEAT_PWR_MGMT = 2
XNVME_SPEC_FEAT_LBA_RANGETYPE = 3
XNVME_SPEC_FEAT_TEMP_THRESHOLD = 4
XNVME_SPEC_FEAT_ERROR_RECOVERY = 5
XNVME_SPEC_FEAT_VWCACHE = 6
XNVME_SPEC_FEAT_NQUEUES = 7
XNVME_SPEC_FEAT_FDP_MODE = 29
XNVME_SPEC_FEAT_FDP_EVENTS = 30
xnvme_spec_feat_id = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_feat_sel'
xnvme_spec_feat_sel__enumvalues = {
    0: "XNVME_SPEC_FEAT_SEL_CURRENT",
    1: "XNVME_SPEC_FEAT_SEL_DEFAULT",
    2: "XNVME_SPEC_FEAT_SEL_SAVED",
    3: "XNVME_SPEC_FEAT_SEL_SUPPORTED",
}
XNVME_SPEC_FEAT_SEL_CURRENT = 0
XNVME_SPEC_FEAT_SEL_DEFAULT = 1
XNVME_SPEC_FEAT_SEL_SAVED = 2
XNVME_SPEC_FEAT_SEL_SUPPORTED = 3
xnvme_spec_feat_sel = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_dir_types'
xnvme_spec_dir_types__enumvalues = {
    0: "XNVME_SPEC_DIR_IDENTIFY",
    1: "XNVME_SPEC_DIR_STREAMS",
}
XNVME_SPEC_DIR_IDENTIFY = 0
XNVME_SPEC_DIR_STREAMS = 1
xnvme_spec_dir_types = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_dsend_idfy_doper'
xnvme_spec_dsend_idfy_doper__enumvalues = {
    1: "XNVME_SPEC_DSEND_IDFY_ENDIR",
}
XNVME_SPEC_DSEND_IDFY_ENDIR = 1
xnvme_spec_dsend_idfy_doper = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_dsend_streams_doper'
xnvme_spec_dsend_streams_doper__enumvalues = {
    1: "XNVME_SPEC_DSEND_STREAMS_RELID",
    2: "XNVME_SPEC_DSEND_STREAMS_RELRS",
}
XNVME_SPEC_DSEND_STREAMS_RELID = 1
XNVME_SPEC_DSEND_STREAMS_RELRS = 2
xnvme_spec_dsend_streams_doper = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_drecv_idfy_doper'
xnvme_spec_drecv_idfy_doper__enumvalues = {
    1: "XNVME_SPEC_DRECV_IDFY_RETPR",
}
XNVME_SPEC_DRECV_IDFY_RETPR = 1
xnvme_spec_drecv_idfy_doper = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_drecv_streams_doper'
xnvme_spec_drecv_streams_doper__enumvalues = {
    1: "XNVME_SPEC_DRECV_STREAMS_RETPR",
    2: "XNVME_SPEC_DRECV_STREAMS_GETST",
    3: "XNVME_SPEC_DRECV_STREAMS_ALLRS",
}
XNVME_SPEC_DRECV_STREAMS_RETPR = 1
XNVME_SPEC_DRECV_STREAMS_GETST = 2
XNVME_SPEC_DRECV_STREAMS_ALLRS = 3
xnvme_spec_drecv_streams_doper = ctypes.c_uint32  # enum


class xnvme_spec_idfy_dir_rp(Structure):
    pass


class xnvme_spec_idfy_dir_rp_directives_supported(Structure):
    pass


xnvme_spec_idfy_dir_rp_directives_supported._pack_ = 1  # source:False
xnvme_spec_idfy_dir_rp_directives_supported._fields_ = [
    ("identify", ctypes.c_ubyte, 1),
    ("streams", ctypes.c_ubyte, 1),
    ("data_placement", ctypes.c_ubyte, 1),
    ("rsvd1", ctypes.c_ubyte, 5),
    ("rsvd2", ctypes.c_ubyte * 31),
]


class xnvme_spec_idfy_dir_rp_directives_enabled(Structure):
    pass


xnvme_spec_idfy_dir_rp_directives_enabled._pack_ = 1  # source:False
xnvme_spec_idfy_dir_rp_directives_enabled._fields_ = [
    ("identify", ctypes.c_ubyte, 1),
    ("streams", ctypes.c_ubyte, 1),
    ("data_placement", ctypes.c_ubyte, 1),
    ("rsvd1", ctypes.c_ubyte, 5),
    ("rsvd2", ctypes.c_ubyte * 31),
]


class xnvme_spec_idfy_dir_rp_directives_persistence(Structure):
    pass


xnvme_spec_idfy_dir_rp_directives_persistence._pack_ = 1  # source:False
xnvme_spec_idfy_dir_rp_directives_persistence._fields_ = [
    ("identify", ctypes.c_ubyte, 1),
    ("streams", ctypes.c_ubyte, 1),
    ("data_placement", ctypes.c_ubyte, 1),
    ("rsvd1", ctypes.c_ubyte, 5),
    ("rsvd2", ctypes.c_ubyte * 31),
]

xnvme_spec_idfy_dir_rp._pack_ = 1  # source:False
xnvme_spec_idfy_dir_rp._fields_ = [
    ("directives_supported", xnvme_spec_idfy_dir_rp_directives_supported),
    ("directives_enabled", xnvme_spec_idfy_dir_rp_directives_enabled),
    ("directives_persistence", xnvme_spec_idfy_dir_rp_directives_persistence),
    ("rsvd4", ctypes.c_ubyte * 4000),
]


class xnvme_spec_streams_dir_rp(Structure):
    pass


class xnvme_spec_streams_dir_rp_nssc(Union):
    pass


class xnvme_spec_streams_dir_rp_0_bits(Structure):
    pass


xnvme_spec_streams_dir_rp_0_bits._pack_ = 1  # source:False
xnvme_spec_streams_dir_rp_0_bits._fields_ = [
    ("multi_host", ctypes.c_ubyte, 1),
    ("reserved", ctypes.c_ubyte, 7),
]

xnvme_spec_streams_dir_rp_nssc._pack_ = 1  # source:False
xnvme_spec_streams_dir_rp_nssc._fields_ = [
    ("bits", xnvme_spec_streams_dir_rp_0_bits),
    ("val", ctypes.c_ubyte),
]

xnvme_spec_streams_dir_rp._pack_ = 1  # source:False
xnvme_spec_streams_dir_rp._fields_ = [
    ("msl", ctypes.c_uint16),
    ("nssa", ctypes.c_uint16),
    ("nsso", ctypes.c_uint16),
    ("nssc", xnvme_spec_streams_dir_rp_nssc),
    ("reserved1", ctypes.c_ubyte * 9),
    ("sws", ctypes.c_uint32),
    ("sgs", ctypes.c_uint16),
    ("nsa", ctypes.c_uint16),
    ("nso", ctypes.c_uint16),
    ("reserved2", ctypes.c_ubyte * 6),
]


class xnvme_spec_streams_dir_gs(Structure):
    pass


xnvme_spec_streams_dir_gs._pack_ = 1  # source:False
xnvme_spec_streams_dir_gs._fields_ = [
    ("open_sc", ctypes.c_uint16),
    ("sid", ctypes.c_uint16 * 0),
]


class xnvme_spec_alloc_resource(Structure):
    pass


class xnvme_spec_alloc_resource_0(Union):
    pass


class xnvme_spec_alloc_resource_0_bits(Structure):
    pass


xnvme_spec_alloc_resource_0_bits._pack_ = 1  # source:False
xnvme_spec_alloc_resource_0_bits._fields_ = [
    ("nsa", ctypes.c_uint32, 16),
    ("rsvd", ctypes.c_uint32, 16),
]

xnvme_spec_alloc_resource_0._pack_ = 1  # source:False
xnvme_spec_alloc_resource_0._fields_ = [
    ("bits", xnvme_spec_alloc_resource_0_bits),
    ("val", ctypes.c_uint32),
]

xnvme_spec_alloc_resource._pack_ = 1  # source:False
xnvme_spec_alloc_resource._anonymous_ = ("_0",)
xnvme_spec_alloc_resource._fields_ = [
    ("_0", xnvme_spec_alloc_resource_0),
]


class xnvme_spec_feat(Structure):
    pass


class xnvme_spec_feat_0(Union):
    pass


class xnvme_spec_feat_0_fdp_mode(Structure):
    pass


xnvme_spec_feat_0_fdp_mode._pack_ = 1  # source:False
xnvme_spec_feat_0_fdp_mode._fields_ = [
    ("fdpe", ctypes.c_uint32, 1),
    ("rsvd1", ctypes.c_uint32, 7),
    ("fdpci", ctypes.c_uint32, 8),
    ("rsvd2", ctypes.c_uint32, 16),
]


class xnvme_spec_feat_0_nqueues(Structure):
    pass


xnvme_spec_feat_0_nqueues._pack_ = 1  # source:False
xnvme_spec_feat_0_nqueues._fields_ = [
    ("nsqa", ctypes.c_uint32, 16),
    ("ncqa", ctypes.c_uint32, 16),
]


class xnvme_spec_feat_0_temp_threshold(Structure):
    pass


xnvme_spec_feat_0_temp_threshold._pack_ = 1  # source:False
xnvme_spec_feat_0_temp_threshold._fields_ = [
    ("tmpth", ctypes.c_uint32, 16),
    ("tmpsel", ctypes.c_uint32, 4),
    ("thsel", ctypes.c_uint32, 3),
    ("rsvd", ctypes.c_uint32, 9),
]


class xnvme_spec_feat_0_error_recovery(Structure):
    pass


xnvme_spec_feat_0_error_recovery._pack_ = 1  # source:False
xnvme_spec_feat_0_error_recovery._fields_ = [
    ("tler", ctypes.c_uint32, 16),
    ("dulbe", ctypes.c_uint32, 1),
    ("rsvd", ctypes.c_uint32, 15),
]

xnvme_spec_feat_0._pack_ = 1  # source:False
xnvme_spec_feat_0._fields_ = [
    ("temp_threshold", xnvme_spec_feat_0_temp_threshold),
    ("error_recovery", xnvme_spec_feat_0_error_recovery),
    ("nqueues", xnvme_spec_feat_0_nqueues),
    ("fdp_mode", xnvme_spec_feat_0_fdp_mode),
    ("val", ctypes.c_uint32),
]

xnvme_spec_feat._pack_ = 1  # source:False
xnvme_spec_feat._anonymous_ = ("_0",)
xnvme_spec_feat._fields_ = [
    ("_0", xnvme_spec_feat_0),
]


class xnvme_spec_dsm_range(Structure):
    pass


xnvme_spec_dsm_range._pack_ = 1  # source:False
xnvme_spec_dsm_range._fields_ = [
    ("cattr", ctypes.c_uint32),
    ("llb", ctypes.c_uint32),
    ("slba", ctypes.c_uint64),
]


# values for enumeration 'xnvme_spec_flag'
xnvme_spec_flag__enumvalues = {
    32768: "XNVME_SPEC_FLAG_LIMITED_RETRY",
    16384: "XNVME_SPEC_FLAG_FORCE_UNIT_ACCESS",
    1024: "XNVME_SPEC_FLAG_PRINFO_PRCHK_REF",
    2048: "XNVME_SPEC_FLAG_PRINFO_PRCHK_APP",
    4096: "XNVME_SPEC_FLAG_PRINFO_PRCHK_GUARD",
    8192: "XNVME_SPEC_FLAG_PRINFO_PRACT",
}
XNVME_SPEC_FLAG_LIMITED_RETRY = 32768
XNVME_SPEC_FLAG_FORCE_UNIT_ACCESS = 16384
XNVME_SPEC_FLAG_PRINFO_PRCHK_REF = 1024
XNVME_SPEC_FLAG_PRINFO_PRCHK_APP = 2048
XNVME_SPEC_FLAG_PRINFO_PRCHK_GUARD = 4096
XNVME_SPEC_FLAG_PRINFO_PRACT = 8192
xnvme_spec_flag = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_nvme_sgl_descriptor_type'
xnvme_nvme_sgl_descriptor_type__enumvalues = {
    0: "XNVME_SPEC_SGL_DESCR_TYPE_DATA_BLOCK",
    1: "XNVME_SPEC_SGL_DESCR_TYPE_BIT_BUCKET",
    2: "XNVME_SPEC_SGL_DESCR_TYPE_SEGMENT",
    3: "XNVME_SPEC_SGL_DESCR_TYPE_LAST_SEGMENT",
    4: "XNVME_SPEC_SGL_DESCR_TYPE_KEYED_DATA_BLOCK",
    15: "XNVME_SPEC_SGL_DESCR_TYPE_VENDOR_SPECIFIC",
}
XNVME_SPEC_SGL_DESCR_TYPE_DATA_BLOCK = 0
XNVME_SPEC_SGL_DESCR_TYPE_BIT_BUCKET = 1
XNVME_SPEC_SGL_DESCR_TYPE_SEGMENT = 2
XNVME_SPEC_SGL_DESCR_TYPE_LAST_SEGMENT = 3
XNVME_SPEC_SGL_DESCR_TYPE_KEYED_DATA_BLOCK = 4
XNVME_SPEC_SGL_DESCR_TYPE_VENDOR_SPECIFIC = 15
xnvme_nvme_sgl_descriptor_type = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_sgl_descriptor_subtype'
xnvme_spec_sgl_descriptor_subtype__enumvalues = {
    0: "XNVME_SPEC_SGL_DESCR_SUBTYPE_ADDRESS",
    1: "XNVME_SPEC_SGL_DESCR_SUBTYPE_OFFSET",
}
XNVME_SPEC_SGL_DESCR_SUBTYPE_ADDRESS = 0
XNVME_SPEC_SGL_DESCR_SUBTYPE_OFFSET = 1
xnvme_spec_sgl_descriptor_subtype = ctypes.c_uint32  # enum


class xnvme_spec_sgl_descriptor(Structure):
    pass


class xnvme_spec_sgl_descriptor_0(Union):
    pass


class xnvme_spec_sgl_descriptor_0_unkeyed(Structure):
    pass


xnvme_spec_sgl_descriptor_0_unkeyed._pack_ = 1  # source:False
xnvme_spec_sgl_descriptor_0_unkeyed._fields_ = [
    ("len", ctypes.c_uint64, 32),
    ("rsvd", ctypes.c_uint64, 24),
    ("subtype", ctypes.c_uint64, 4),
    ("type", ctypes.c_uint64, 4),
]


class xnvme_spec_sgl_descriptor_0_generic(Structure):
    pass


xnvme_spec_sgl_descriptor_0_generic._pack_ = 1  # source:False
xnvme_spec_sgl_descriptor_0_generic._fields_ = [
    ("rsvd", ctypes.c_uint64, 56),
    ("subtype", ctypes.c_uint64, 4),
    ("type", ctypes.c_uint64, 4),
]

xnvme_spec_sgl_descriptor_0._pack_ = 1  # source:False
xnvme_spec_sgl_descriptor_0._fields_ = [
    ("generic", xnvme_spec_sgl_descriptor_0_generic),
    ("unkeyed", xnvme_spec_sgl_descriptor_0_unkeyed),
]

xnvme_spec_sgl_descriptor._pack_ = 1  # source:False
xnvme_spec_sgl_descriptor._anonymous_ = ("_0",)
xnvme_spec_sgl_descriptor._fields_ = [
    ("addr", ctypes.c_uint64),
    ("_0", xnvme_spec_sgl_descriptor_0),
]


# values for enumeration 'xnvme_spec_psdt'
xnvme_spec_psdt__enumvalues = {
    0: "XNVME_SPEC_PSDT_PRP",
    1: "XNVME_SPEC_PSDT_SGL_MPTR_CONTIGUOUS",
    2: "XNVME_SPEC_PSDT_SGL_MPTR_SGL",
}
XNVME_SPEC_PSDT_PRP = 0
XNVME_SPEC_PSDT_SGL_MPTR_CONTIGUOUS = 1
XNVME_SPEC_PSDT_SGL_MPTR_SGL = 2
xnvme_spec_psdt = ctypes.c_uint32  # enum


class xnvme_spec_cmd_common(Structure):
    pass


class xnvme_spec_cmd_common_dptr(Union):
    pass


class xnvme_spec_cmd_common_0_prp(Structure):
    pass


xnvme_spec_cmd_common_0_prp._pack_ = 1  # source:False
xnvme_spec_cmd_common_0_prp._fields_ = [
    ("prp1", ctypes.c_uint64),
    ("prp2", ctypes.c_uint64),
]


class xnvme_spec_cmd_common_0_lnx_ioctl(Structure):
    pass


xnvme_spec_cmd_common_0_lnx_ioctl._pack_ = 1  # source:False
xnvme_spec_cmd_common_0_lnx_ioctl._fields_ = [
    ("data", ctypes.c_uint64),
    ("metadata_len", ctypes.c_uint32),
    ("data_len", ctypes.c_uint32),
]

xnvme_spec_cmd_common_dptr._pack_ = 1  # source:False
xnvme_spec_cmd_common_dptr._fields_ = [
    ("prp", xnvme_spec_cmd_common_0_prp),
    ("sgl", xnvme_spec_sgl_descriptor),
    ("lnx_ioctl", xnvme_spec_cmd_common_0_lnx_ioctl),
]

xnvme_spec_cmd_common._pack_ = 1  # source:False
xnvme_spec_cmd_common._fields_ = [
    ("opcode", ctypes.c_uint16, 8),
    ("fuse", ctypes.c_uint16, 2),
    ("rsvd", ctypes.c_uint16, 4),
    ("psdt", ctypes.c_uint16, 2),
    ("cid", ctypes.c_uint16),
    ("nsid", ctypes.c_uint32),
    ("cdw02", ctypes.c_uint32),
    ("cdw03", ctypes.c_uint32),
    ("mptr", ctypes.c_uint64),
    ("dptr", xnvme_spec_cmd_common_dptr),
    ("ndt", ctypes.c_uint32),
    ("ndm", ctypes.c_uint32),
    ("cdw12", ctypes.c_uint32),
    ("cdw13", ctypes.c_uint32),
    ("cdw14", ctypes.c_uint32),
    ("cdw15", ctypes.c_uint32),
]


class xnvme_spec_cmd_sanitize(Structure):
    pass


xnvme_spec_cmd_sanitize._pack_ = 1  # source:False
xnvme_spec_cmd_sanitize._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("sanact", ctypes.c_uint32, 3),
    ("ause", ctypes.c_uint32, 1),
    ("owpass", ctypes.c_uint32, 4),
    ("oipbp", ctypes.c_uint32, 1),
    ("nodas", ctypes.c_uint32, 1),
    ("rsvd", ctypes.c_uint32, 22),
    ("ovrpat", ctypes.c_uint32),
    ("cdw12_15", ctypes.c_uint32 * 4),
]


class xnvme_spec_cmd_format(Structure):
    pass


xnvme_spec_cmd_format._pack_ = 1  # source:False
xnvme_spec_cmd_format._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("lbafl", ctypes.c_uint32, 4),
    ("mset", ctypes.c_uint32, 1),
    ("pi", ctypes.c_uint32, 3),
    ("pil", ctypes.c_uint32, 1),
    ("ses", ctypes.c_uint32, 3),
    ("lbafu", ctypes.c_uint32, 2),
    ("rsvd", ctypes.c_uint32, 18),
    ("cdw11_15", ctypes.c_uint32 * 5),
]


class xnvme_spec_cmd_gfeat(Structure):
    pass


class xnvme_spec_cmd_gfeat_cdw10(Union):
    pass


class xnvme_spec_cmd_gfeat_0_0(Structure):
    pass


xnvme_spec_cmd_gfeat_0_0._pack_ = 1  # source:False
xnvme_spec_cmd_gfeat_0_0._fields_ = [
    ("fid", ctypes.c_uint32, 8),
    ("sel", ctypes.c_uint32, 3),
    ("rsvd10", ctypes.c_uint32, 21),
]

xnvme_spec_cmd_gfeat_cdw10._pack_ = 1  # source:False
xnvme_spec_cmd_gfeat_cdw10._anonymous_ = ("_0",)
xnvme_spec_cmd_gfeat_cdw10._fields_ = [
    ("_0", xnvme_spec_cmd_gfeat_0_0),
    ("val", ctypes.c_uint32),
]

xnvme_spec_cmd_gfeat._pack_ = 1  # source:False
xnvme_spec_cmd_gfeat._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("cdw10", xnvme_spec_cmd_gfeat_cdw10),
    ("cdw11", ctypes.c_uint32),
    ("cdw12_15", ctypes.c_uint32 * 4),
]


class xnvme_spec_cmd_sfeat(Structure):
    pass


class xnvme_spec_cmd_sfeat_cdw10(Union):
    pass


class xnvme_spec_cmd_sfeat_0_0(Structure):
    pass


xnvme_spec_cmd_sfeat_0_0._pack_ = 1  # source:False
xnvme_spec_cmd_sfeat_0_0._fields_ = [
    ("fid", ctypes.c_uint32, 8),
    ("rsvd10", ctypes.c_uint32, 23),
    ("save", ctypes.c_uint32, 1),
]

xnvme_spec_cmd_sfeat_cdw10._pack_ = 1  # source:False
xnvme_spec_cmd_sfeat_cdw10._anonymous_ = ("_0",)
xnvme_spec_cmd_sfeat_cdw10._fields_ = [
    ("_0", xnvme_spec_cmd_sfeat_0_0),
    ("val", ctypes.c_uint32),
]

xnvme_spec_cmd_sfeat._pack_ = 1  # source:False
xnvme_spec_cmd_sfeat._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("cdw10", xnvme_spec_cmd_sfeat_cdw10),
    ("feat", xnvme_spec_feat),
    ("cdw12", ctypes.c_uint32),
    ("cdw13_15", ctypes.c_uint32 * 3),
]


class xnvme_spec_cmd_dsend(Structure):
    pass


class xnvme_spec_cmd_dsend_cdw12(Union):
    pass


class xnvme_spec_cmd_dsend_0_0(Structure):
    pass


xnvme_spec_cmd_dsend_0_0._pack_ = 1  # source:False
xnvme_spec_cmd_dsend_0_0._fields_ = [
    ("endir", ctypes.c_uint32, 1),
    ("rsvd1", ctypes.c_uint32, 7),
    ("tdtype", ctypes.c_uint32, 8),
    ("rsvd2", ctypes.c_uint32, 16),
]

xnvme_spec_cmd_dsend_cdw12._pack_ = 1  # source:False
xnvme_spec_cmd_dsend_cdw12._anonymous_ = ("_0",)
xnvme_spec_cmd_dsend_cdw12._fields_ = [
    ("_0", xnvme_spec_cmd_dsend_0_0),
    ("val", ctypes.c_uint32),
]

xnvme_spec_cmd_dsend._pack_ = 1  # source:False
xnvme_spec_cmd_dsend._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("numd", ctypes.c_uint32),
    ("doper", ctypes.c_uint32, 8),
    ("dtype", ctypes.c_uint32, 8),
    ("dspec", ctypes.c_uint32, 16),
    ("cdw12", xnvme_spec_cmd_dsend_cdw12),
    ("cdw13_15", ctypes.c_uint32 * 3),
]


class xnvme_spec_cmd_drecv(Structure):
    pass


class xnvme_spec_cmd_drecv_cdw12(Union):
    pass


class xnvme_spec_cmd_drecv_0_0(Structure):
    pass


xnvme_spec_cmd_drecv_0_0._pack_ = 1  # source:False
xnvme_spec_cmd_drecv_0_0._fields_ = [
    ("nsr", ctypes.c_uint32, 16),
    ("rsvd", ctypes.c_uint32, 16),
]

xnvme_spec_cmd_drecv_cdw12._pack_ = 1  # source:False
xnvme_spec_cmd_drecv_cdw12._anonymous_ = ("_0",)
xnvme_spec_cmd_drecv_cdw12._fields_ = [
    ("_0", xnvme_spec_cmd_drecv_0_0),
    ("val", ctypes.c_uint32),
]

xnvme_spec_cmd_drecv._pack_ = 1  # source:False
xnvme_spec_cmd_drecv._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("numd", ctypes.c_uint32),
    ("doper", ctypes.c_uint32, 8),
    ("dtype", ctypes.c_uint32, 8),
    ("dspec", ctypes.c_uint32, 16),
    ("cdw12", xnvme_spec_cmd_drecv_cdw12),
    ("cdw13_15", ctypes.c_uint32 * 3),
]


class xnvme_spec_cmd_idfy(Structure):
    pass


xnvme_spec_cmd_idfy._pack_ = 1  # source:False
xnvme_spec_cmd_idfy._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("cns", ctypes.c_uint64, 8),
    ("rsvd1", ctypes.c_uint64, 8),
    ("cntid", ctypes.c_uint64, 16),
    ("nvmsetid", ctypes.c_uint64, 16),
    ("rsvd2", ctypes.c_uint64, 8),
    ("csi", ctypes.c_uint64, 8),
    ("cdw12_13", ctypes.c_uint32 * 2),
    ("uuid", ctypes.c_uint32, 7),
    ("rsvd3", ctypes.c_uint32, 25),
    ("cdw15", ctypes.c_uint32),
]


class xnvme_spec_cmd_log(Structure):
    pass


xnvme_spec_cmd_log._pack_ = 1  # source:False
xnvme_spec_cmd_log._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("lid", ctypes.c_uint64, 8),
    ("lsp", ctypes.c_uint64, 7),
    ("rae", ctypes.c_uint64, 1),
    ("numdl", ctypes.c_uint64, 16),
    ("numdu", ctypes.c_uint64, 16),
    ("lsi", ctypes.c_uint64, 16),
    ("lpol", ctypes.c_uint32),
    ("lpou", ctypes.c_uint32),
    ("uuidx", ctypes.c_uint32, 7),
    ("rsvd1", ctypes.c_uint32, 16),
    ("ot", ctypes.c_uint32, 1),
    ("csi", ctypes.c_uint32, 8),
    ("cdw15", ctypes.c_uint32),
]


class xnvme_spec_cmd_nvm(Structure):
    pass


class xnvme_spec_cmd_nvm_cdw13(Union):
    pass


class xnvme_spec_cmd_nvm_0_0(Structure):
    pass


xnvme_spec_cmd_nvm_0_0._pack_ = 1  # source:False
xnvme_spec_cmd_nvm_0_0._fields_ = [
    ("af", ctypes.c_uint32, 4),
    ("al", ctypes.c_uint32, 2),
    ("sr", ctypes.c_uint32, 1),
    ("incom", ctypes.c_uint32, 1),
    ("rsvd3", ctypes.c_uint32, 8),
    ("dspec", ctypes.c_uint32, 16),
]

xnvme_spec_cmd_nvm_cdw13._pack_ = 1  # source:False
xnvme_spec_cmd_nvm_cdw13._anonymous_ = ("_0",)
xnvme_spec_cmd_nvm_cdw13._fields_ = [
    ("_0", xnvme_spec_cmd_nvm_0_0),
    ("val", ctypes.c_uint32),
]

xnvme_spec_cmd_nvm._pack_ = 1  # source:False
xnvme_spec_cmd_nvm._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("slba", ctypes.c_uint64),
    ("nlb", ctypes.c_uint32, 16),
    ("rsvd", ctypes.c_uint32, 4),
    ("dtype", ctypes.c_uint32, 4),
    ("rsvd2", ctypes.c_uint32, 2),
    ("prinfo", ctypes.c_uint32, 4),
    ("fua", ctypes.c_uint32, 1),
    ("lr", ctypes.c_uint32, 1),
    ("cdw13", xnvme_spec_cmd_nvm_cdw13),
    ("ilbrt", ctypes.c_uint64, 32),
    ("lbat", ctypes.c_uint64, 16),
    ("lbatm", ctypes.c_uint64, 16),
]


class xnvme_spec_cmd_dsm(Structure):
    pass


xnvme_spec_cmd_dsm._pack_ = 1  # source:False
xnvme_spec_cmd_dsm._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("nr", ctypes.c_uint64, 8),
    ("rsvd1", ctypes.c_uint64, 24),
    ("idr", ctypes.c_uint64, 1),
    ("idw", ctypes.c_uint64, 1),
    ("ad", ctypes.c_uint64, 1),
    ("rsvd2", ctypes.c_uint64, 29),
    ("cdw12_15", ctypes.c_uint32 * 4),
]


class xnvme_spec_nvm_write_zeroes(Structure):
    pass


xnvme_spec_nvm_write_zeroes._pack_ = 1  # source:False
xnvme_spec_nvm_write_zeroes._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("slba", ctypes.c_uint64),
    ("nlb", ctypes.c_uint32, 16),
    ("rsvd1", ctypes.c_uint32, 8),
    ("deac", ctypes.c_uint32, 1),
    ("prinfo", ctypes.c_uint32, 4),
    ("fua", ctypes.c_uint32, 1),
    ("lr", ctypes.c_uint32, 1),
    ("PADDING_0", ctypes.c_uint8, 1),
    ("cdw_13", ctypes.c_uint32),
    ("ilbrt", ctypes.c_uint64, 32),
    ("lbat", ctypes.c_uint64, 16),
    ("lbatm", ctypes.c_uint64, 16),
]


# values for enumeration 'xnvme_spec_nvm_cmd_cpl_sc'
xnvme_spec_nvm_cmd_cpl_sc__enumvalues = {
    130: "XNVME_SPEC_NVM_CMD_CPL_SC_WRITE_TO_RONLY",
}
XNVME_SPEC_NVM_CMD_CPL_SC_WRITE_TO_RONLY = 130
xnvme_spec_nvm_cmd_cpl_sc = ctypes.c_uint32  # enum


class xnvme_spec_nvm_scopy_fmt_zero(Structure):
    pass


xnvme_spec_nvm_scopy_fmt_zero._pack_ = 1  # source:False
xnvme_spec_nvm_scopy_fmt_zero._fields_ = [
    ("rsvd0", ctypes.c_ubyte * 8),
    ("slba", ctypes.c_uint64),
    ("nlb", ctypes.c_uint32, 16),
    ("rsvd20", ctypes.c_uint32, 16),
    ("eilbrt", ctypes.c_uint32),
    ("elbatm", ctypes.c_uint32),
    ("elbat", ctypes.c_uint32),
]


# values for enumeration 'xnvme_nvm_scopy_fmt'
xnvme_nvm_scopy_fmt__enumvalues = {
    1: "XNVME_NVM_SCOPY_FMT_ZERO",
    256: "XNVME_NVM_SCOPY_FMT_SRCLEN",
}
XNVME_NVM_SCOPY_FMT_ZERO = 1
XNVME_NVM_SCOPY_FMT_SRCLEN = 256
xnvme_nvm_scopy_fmt = ctypes.c_uint32  # enum


class xnvme_spec_nvm_scopy_source_range(Structure):
    _pack_ = 1  # source:False
    _fields_ = [
        ("entry", xnvme_spec_nvm_scopy_fmt_zero * 128),
    ]


class xnvme_spec_nvm_cmd_scopy(Structure):
    pass


xnvme_spec_nvm_cmd_scopy._pack_ = 1  # source:False
xnvme_spec_nvm_cmd_scopy._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("sdlba", ctypes.c_uint64),
    ("nr", ctypes.c_uint64, 8),
    ("df", ctypes.c_uint64, 4),
    ("prinfor", ctypes.c_uint64, 4),
    ("rsvd1", ctypes.c_uint64, 4),
    ("dtype", ctypes.c_uint64, 4),
    ("rsvd2", ctypes.c_uint64, 2),
    ("prinfow", ctypes.c_uint64, 4),
    ("fua", ctypes.c_uint64, 1),
    ("lr", ctypes.c_uint64, 1),
    ("rsvd3", ctypes.c_uint64, 16),
    ("dspec", ctypes.c_uint64, 16),
    ("ilbrt", ctypes.c_uint32),
    ("lbat", ctypes.c_uint32, 16),
    ("lbatm", ctypes.c_uint32, 16),
]


class xnvme_spec_nvm_cmd_scopy_fmt_srclen(Structure):
    pass


xnvme_spec_nvm_cmd_scopy_fmt_srclen._pack_ = 1  # source:False
xnvme_spec_nvm_cmd_scopy_fmt_srclen._fields_ = [
    ("start", ctypes.c_uint64),
    ("len", ctypes.c_uint64),
]


class xnvme_spec_nvm_cmd(Structure):
    pass


class xnvme_spec_nvm_cmd_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("scopy", xnvme_spec_nvm_cmd_scopy),
    ]


xnvme_spec_nvm_cmd._pack_ = 1  # source:False
xnvme_spec_nvm_cmd._anonymous_ = ("_0",)
xnvme_spec_nvm_cmd._fields_ = [
    ("_0", xnvme_spec_nvm_cmd_0),
]


class xnvme_spec_nvm_idfy_ctrlr(Structure):
    pass


class xnvme_spec_nvm_idfy_ctrlr_oncs(Union):
    pass


class xnvme_spec_nvm_idfy_ctrlr_0_0(Structure):
    pass


xnvme_spec_nvm_idfy_ctrlr_0_0._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ctrlr_0_0._fields_ = [
    ("compare", ctypes.c_uint16, 1),
    ("write_unc", ctypes.c_uint16, 1),
    ("dsm", ctypes.c_uint16, 1),
    ("write_zeroes", ctypes.c_uint16, 1),
    ("set_features_save", ctypes.c_uint16, 1),
    ("reservations", ctypes.c_uint16, 1),
    ("timestamp", ctypes.c_uint16, 1),
    ("verify", ctypes.c_uint16, 1),
    ("copy", ctypes.c_uint16, 1),
    ("reserved", ctypes.c_uint16, 7),
]

xnvme_spec_nvm_idfy_ctrlr_oncs._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ctrlr_oncs._anonymous_ = ("_0",)
xnvme_spec_nvm_idfy_ctrlr_oncs._fields_ = [
    ("_0", xnvme_spec_nvm_idfy_ctrlr_0_0),
    ("val", ctypes.c_uint16),
]


class xnvme_spec_nvm_idfy_ctrlr_ocfs(Union):
    pass


class xnvme_spec_nvm_idfy_ctrlr_1_0(Structure):
    pass


xnvme_spec_nvm_idfy_ctrlr_1_0._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ctrlr_1_0._fields_ = [
    ("copy_fmt0", ctypes.c_uint16, 1),
    ("rsvd", ctypes.c_uint16, 15),
]

xnvme_spec_nvm_idfy_ctrlr_ocfs._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ctrlr_ocfs._anonymous_ = ("_0",)
xnvme_spec_nvm_idfy_ctrlr_ocfs._fields_ = [
    ("_0", xnvme_spec_nvm_idfy_ctrlr_1_0),
    ("val", ctypes.c_uint16),
]

xnvme_spec_nvm_idfy_ctrlr._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ctrlr._fields_ = [
    ("byte0_519", ctypes.c_ubyte * 520),
    ("oncs", xnvme_spec_nvm_idfy_ctrlr_oncs),
    ("byte522_533", ctypes.c_ubyte * 12),
    ("ocfs", xnvme_spec_nvm_idfy_ctrlr_ocfs),
    ("byte536_4095", ctypes.c_ubyte * 3559),
    ("PADDING_0", ctypes.c_ubyte),
]


class xnvme_spec_nvm_idfy_ns(Structure):
    pass


xnvme_spec_nvm_idfy_ns._pack_ = 1  # source:False
xnvme_spec_nvm_idfy_ns._fields_ = [
    ("byte0_73", ctypes.c_ubyte * 74),
    ("mssrl", ctypes.c_uint16),
    ("mcl", ctypes.c_uint32),
    ("msrc", ctypes.c_ubyte),
    ("byte81_4095", ctypes.c_ubyte * 4014),
    ("PADDING_0", ctypes.c_ubyte),
]


class xnvme_spec_nvm_idfy(Structure):
    pass


class xnvme_spec_nvm_idfy_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("base", xnvme_spec_idfy),
        ("ctrlr", xnvme_spec_nvm_idfy_ctrlr),
        ("ns", xnvme_spec_nvm_idfy_ns),
    ]


xnvme_spec_nvm_idfy._pack_ = 1  # source:False
xnvme_spec_nvm_idfy._anonymous_ = ("_0",)
xnvme_spec_nvm_idfy._fields_ = [
    ("_0", xnvme_spec_nvm_idfy_0),
]


# values for enumeration 'xnvme_spec_znd_log_lid'
xnvme_spec_znd_log_lid__enumvalues = {
    191: "XNVME_SPEC_LOG_ZND_CHANGES",
}
XNVME_SPEC_LOG_ZND_CHANGES = 191
xnvme_spec_znd_log_lid = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_opc'
xnvme_spec_znd_opc__enumvalues = {
    121: "XNVME_SPEC_ZND_OPC_MGMT_SEND",
    122: "XNVME_SPEC_ZND_OPC_MGMT_RECV",
    125: "XNVME_SPEC_ZND_OPC_APPEND",
}
XNVME_SPEC_ZND_OPC_MGMT_SEND = 121
XNVME_SPEC_ZND_OPC_MGMT_RECV = 122
XNVME_SPEC_ZND_OPC_APPEND = 125
xnvme_spec_znd_opc = ctypes.c_uint32  # enum


class xnvme_spec_znd_cmd_mgmt_send(Structure):
    pass


xnvme_spec_znd_cmd_mgmt_send._pack_ = 1  # source:False
xnvme_spec_znd_cmd_mgmt_send._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("slba", ctypes.c_uint64),
    ("nrange", ctypes.c_uint32),
    ("zsa", ctypes.c_uint32, 8),
    ("select_all", ctypes.c_uint32, 1),
    ("zsaso", ctypes.c_uint32, 1),
    ("rsvd", ctypes.c_uint32, 22),
    ("cdw14_15", ctypes.c_uint32 * 2),
]


class xnvme_spec_znd_cmd_mgmt_recv(Structure):
    pass


xnvme_spec_znd_cmd_mgmt_recv._pack_ = 1  # source:False
xnvme_spec_znd_cmd_mgmt_recv._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("slba", ctypes.c_uint64),
    ("ndwords", ctypes.c_uint32),
    ("zra", ctypes.c_uint32, 8),
    ("zrasf", ctypes.c_uint32, 8),
    ("partial", ctypes.c_uint32, 1),
    ("rsvd", ctypes.c_uint32, 15),
    ("addrs_dst", ctypes.c_uint64),
]


class xnvme_spec_znd_cmd_append(Structure):
    pass


xnvme_spec_znd_cmd_append._pack_ = 1  # source:False
xnvme_spec_znd_cmd_append._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("zslba", ctypes.c_uint64),
    ("nlb", ctypes.c_uint32, 16),
    ("rsvd", ctypes.c_uint32, 4),
    ("dtype", ctypes.c_uint32, 4),
    ("prinfo", ctypes.c_uint32, 4),
    ("rsvd2", ctypes.c_uint32, 2),
    ("fua", ctypes.c_uint32, 1),
    ("lr", ctypes.c_uint32, 1),
    ("cdw13_15", ctypes.c_uint32 * 3),
]


class xnvme_spec_znd_cmd(Structure):
    pass


class xnvme_spec_znd_cmd_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("mgmt_send", xnvme_spec_znd_cmd_mgmt_send),
        ("mgmt_recv", xnvme_spec_znd_cmd_mgmt_recv),
        ("append", xnvme_spec_znd_cmd_append),
    ]


xnvme_spec_znd_cmd._pack_ = 1  # source:False
xnvme_spec_znd_cmd._anonymous_ = ("_0",)
xnvme_spec_znd_cmd._fields_ = [
    ("_0", xnvme_spec_znd_cmd_0),
]


class xnvme_spec_io_mgmt_recv_cmd(Structure):
    pass


xnvme_spec_io_mgmt_recv_cmd._pack_ = 1  # source:False
xnvme_spec_io_mgmt_recv_cmd._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("mo", ctypes.c_uint32, 8),
    ("rsvd", ctypes.c_uint32, 8),
    ("mos", ctypes.c_uint32, 16),
    ("numd", ctypes.c_uint32),
    ("cdw12_15", ctypes.c_uint32 * 4),
]


class xnvme_spec_io_mgmt_send_cmd(Structure):
    pass


xnvme_spec_io_mgmt_send_cmd._pack_ = 1  # source:False
xnvme_spec_io_mgmt_send_cmd._fields_ = [
    ("cdw00_09", ctypes.c_uint32 * 10),
    ("mo", ctypes.c_uint32, 8),
    ("rsvd", ctypes.c_uint32, 8),
    ("mos", ctypes.c_uint32, 16),
    ("cdw11_15", ctypes.c_uint32 * 5),
]


class xnvme_spec_io_mgmt_cmd(Structure):
    pass


class xnvme_spec_io_mgmt_cmd_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("mgmt_recv", xnvme_spec_io_mgmt_recv_cmd),
        ("mgmt_send", xnvme_spec_io_mgmt_send_cmd),
    ]


xnvme_spec_io_mgmt_cmd._pack_ = 1  # source:False
xnvme_spec_io_mgmt_cmd._anonymous_ = ("_0",)
xnvme_spec_io_mgmt_cmd._fields_ = [
    ("_0", xnvme_spec_io_mgmt_cmd_0),
]


# values for enumeration 'xnvme_spec_kv_opc'
xnvme_spec_kv_opc__enumvalues = {
    1: "XNVME_SPEC_KV_OPC_STORE",
    2: "XNVME_SPEC_KV_OPC_RETRIEVE",
    16: "XNVME_SPEC_KV_OPC_DELETE",
    20: "XNVME_SPEC_KV_OPC_EXIST",
    6: "XNVME_SPEC_KV_OPC_LIST",
}
XNVME_SPEC_KV_OPC_STORE = 1
XNVME_SPEC_KV_OPC_RETRIEVE = 2
XNVME_SPEC_KV_OPC_DELETE = 16
XNVME_SPEC_KV_OPC_EXIST = 20
XNVME_SPEC_KV_OPC_LIST = 6
xnvme_spec_kv_opc = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_kv_status_code'
xnvme_spec_kv_status_code__enumvalues = {
    129: "XNVME_SPEC_KV_SC_CAPACITY_EXCEEDED",
    130: "XNVME_SPEC_KV_SC_NS_NOT_READY",
    131: "XNVME_SPEC_KV_SC_RESERVATION_CONFLICT",
    132: "XNVME_SPEC_KV_SC_FORMAT_IN_PROGRESS",
    133: "XNVME_SPEC_KV_SC_INVALID_VAL_SIZE",
    134: "XNVME_SPEC_KV_SC_INVALID_KEY_SIZE",
    135: "XNVME_SPEC_KV_SC_KEY_NOT_EXISTS",
    136: "XNVME_SPEC_KV_SC_UNRECOVERED_ERR",
    137: "XNVME_SPEC_KV_SC_KEY_EXISTS",
}
XNVME_SPEC_KV_SC_CAPACITY_EXCEEDED = 129
XNVME_SPEC_KV_SC_NS_NOT_READY = 130
XNVME_SPEC_KV_SC_RESERVATION_CONFLICT = 131
XNVME_SPEC_KV_SC_FORMAT_IN_PROGRESS = 132
XNVME_SPEC_KV_SC_INVALID_VAL_SIZE = 133
XNVME_SPEC_KV_SC_INVALID_KEY_SIZE = 134
XNVME_SPEC_KV_SC_KEY_NOT_EXISTS = 135
XNVME_SPEC_KV_SC_UNRECOVERED_ERR = 136
XNVME_SPEC_KV_SC_KEY_EXISTS = 137
xnvme_spec_kv_status_code = ctypes.c_uint32  # enum


class xnvme_spec_kvs_cmd(Structure):
    pass


class xnvme_spec_kvs_cmd_cdw11(Structure):
    pass


xnvme_spec_kvs_cmd_cdw11._pack_ = 1  # source:False
xnvme_spec_kvs_cmd_cdw11._fields_ = [
    ("kl", ctypes.c_ubyte),
    ("ro", ctypes.c_ubyte),
    ("rsvd", ctypes.c_uint16),
]

xnvme_spec_kvs_cmd._pack_ = 1  # source:False
xnvme_spec_kvs_cmd._fields_ = [
    ("cdw0", ctypes.c_uint32),
    ("nsid", ctypes.c_uint32),
    ("key", ctypes.c_uint64),
    ("mptr", ctypes.c_uint64),
    ("cdw06", ctypes.c_uint32),
    ("cdw07", ctypes.c_uint32),
    ("cdw08", ctypes.c_uint32),
    ("cdw09", ctypes.c_uint32),
    ("cdw10", ctypes.c_uint32),
    ("cdw11", xnvme_spec_kvs_cmd_cdw11),
    ("cdw12", ctypes.c_uint32),
    ("cdw13", ctypes.c_uint32),
    ("key_hi", ctypes.c_uint64),
]


class xnvme_spec_cmd(Structure):
    pass


class xnvme_spec_cmd_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("common", xnvme_spec_cmd_common),
        ("sanitize", xnvme_spec_cmd_sanitize),
        ("format", xnvme_spec_cmd_format),
        ("log", xnvme_spec_cmd_log),
        ("gfeat", xnvme_spec_cmd_gfeat),
        ("sfeat", xnvme_spec_cmd_sfeat),
        ("idfy", xnvme_spec_cmd_idfy),
        ("dsend", xnvme_spec_cmd_dsend),
        ("drecv", xnvme_spec_cmd_drecv),
        ("nvm", xnvme_spec_cmd_nvm),
        ("dsm", xnvme_spec_cmd_dsm),
        ("scopy", xnvme_spec_nvm_cmd_scopy),
        ("write_zeroes", xnvme_spec_nvm_write_zeroes),
        ("znd", xnvme_spec_znd_cmd),
        ("mgmt", xnvme_spec_io_mgmt_cmd),
        ("kvs", xnvme_spec_kvs_cmd),
    ]


xnvme_spec_cmd._pack_ = 1  # source:False
xnvme_spec_cmd._anonymous_ = ("_0",)
xnvme_spec_cmd._fields_ = [
    ("_0", xnvme_spec_cmd_0),
]


# values for enumeration 'xnvme_spec_znd_status_code'
xnvme_spec_znd_status_code__enumvalues = {
    127: "XNVME_SPEC_ZND_SC_INVALID_FORMAT",
    182: "XNVME_SPEC_ZND_SC_INVALID_ZONE_OP",
    183: "XNVME_SPEC_ZND_SC_NOZRWA",
    184: "XNVME_SPEC_ZND_SC_BOUNDARY_ERROR",
    185: "XNVME_SPEC_ZND_SC_IS_FULL",
    186: "XNVME_SPEC_ZND_SC_IS_READONLY",
    187: "XNVME_SPEC_ZND_SC_IS_OFFLINE",
    188: "XNVME_SPEC_ZND_SC_INVALID_WRITE",
    189: "XNVME_SPEC_ZND_SC_TOO_MANY_ACTIVE",
    190: "XNVME_SPEC_ZND_SC_TOO_MANY_OPEN",
    191: "XNVME_SPEC_ZND_SC_INVALID_TRANS",
}
XNVME_SPEC_ZND_SC_INVALID_FORMAT = 127
XNVME_SPEC_ZND_SC_INVALID_ZONE_OP = 182
XNVME_SPEC_ZND_SC_NOZRWA = 183
XNVME_SPEC_ZND_SC_BOUNDARY_ERROR = 184
XNVME_SPEC_ZND_SC_IS_FULL = 185
XNVME_SPEC_ZND_SC_IS_READONLY = 186
XNVME_SPEC_ZND_SC_IS_OFFLINE = 187
XNVME_SPEC_ZND_SC_INVALID_WRITE = 188
XNVME_SPEC_ZND_SC_TOO_MANY_ACTIVE = 189
XNVME_SPEC_ZND_SC_TOO_MANY_OPEN = 190
XNVME_SPEC_ZND_SC_INVALID_TRANS = 191
xnvme_spec_znd_status_code = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_mgmt_send_action_so'
xnvme_spec_znd_mgmt_send_action_so__enumvalues = {
    1: "XNVME_SPEC_ZND_MGMT_OPEN_WITH_ZRWA",
}
XNVME_SPEC_ZND_MGMT_OPEN_WITH_ZRWA = 1
xnvme_spec_znd_mgmt_send_action_so = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_cmd_mgmt_send_action'
xnvme_spec_znd_cmd_mgmt_send_action__enumvalues = {
    1: "XNVME_SPEC_ZND_CMD_MGMT_SEND_CLOSE",
    2: "XNVME_SPEC_ZND_CMD_MGMT_SEND_FINISH",
    3: "XNVME_SPEC_ZND_CMD_MGMT_SEND_OPEN",
    4: "XNVME_SPEC_ZND_CMD_MGMT_SEND_RESET",
    5: "XNVME_SPEC_ZND_CMD_MGMT_SEND_OFFLINE",
    16: "XNVME_SPEC_ZND_CMD_MGMT_SEND_DESCRIPTOR",
    17: "XNVME_SPEC_ZND_CMD_MGMT_SEND_FLUSH",
}
XNVME_SPEC_ZND_CMD_MGMT_SEND_CLOSE = 1
XNVME_SPEC_ZND_CMD_MGMT_SEND_FINISH = 2
XNVME_SPEC_ZND_CMD_MGMT_SEND_OPEN = 3
XNVME_SPEC_ZND_CMD_MGMT_SEND_RESET = 4
XNVME_SPEC_ZND_CMD_MGMT_SEND_OFFLINE = 5
XNVME_SPEC_ZND_CMD_MGMT_SEND_DESCRIPTOR = 16
XNVME_SPEC_ZND_CMD_MGMT_SEND_FLUSH = 17
xnvme_spec_znd_cmd_mgmt_send_action = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_cmd_mgmt_recv_action_sf'
xnvme_spec_znd_cmd_mgmt_recv_action_sf__enumvalues = {
    0: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_ALL",
    1: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_EMPTY",
    2: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_IOPEN",
    3: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_EOPEN",
    4: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_CLOSED",
    5: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_FULL",
    6: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_RONLY",
    7: "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_OFFLINE",
}
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_ALL = 0
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_EMPTY = 1
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_IOPEN = 2
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_EOPEN = 3
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_CLOSED = 4
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_FULL = 5
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_RONLY = 6
XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_OFFLINE = 7
xnvme_spec_znd_cmd_mgmt_recv_action_sf = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_cmd_mgmt_recv_action'
xnvme_spec_znd_cmd_mgmt_recv_action__enumvalues = {
    0: "XNVME_SPEC_ZND_CMD_MGMT_RECV_ACTION_REPORT",
    1: "XNVME_SPEC_ZND_CMD_MGMT_RECV_ACTION_REPORT_EXTENDED",
}
XNVME_SPEC_ZND_CMD_MGMT_RECV_ACTION_REPORT = 0
XNVME_SPEC_ZND_CMD_MGMT_RECV_ACTION_REPORT_EXTENDED = 1
xnvme_spec_znd_cmd_mgmt_recv_action = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_type'
xnvme_spec_znd_type__enumvalues = {
    2: "XNVME_SPEC_ZND_TYPE_SEQWR",
}
XNVME_SPEC_ZND_TYPE_SEQWR = 2
xnvme_spec_znd_type = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_spec_znd_state'
xnvme_spec_znd_state__enumvalues = {
    1: "XNVME_SPEC_ZND_STATE_EMPTY",
    2: "XNVME_SPEC_ZND_STATE_IOPEN",
    3: "XNVME_SPEC_ZND_STATE_EOPEN",
    4: "XNVME_SPEC_ZND_STATE_CLOSED",
    13: "XNVME_SPEC_ZND_STATE_RONLY",
    14: "XNVME_SPEC_ZND_STATE_FULL",
    15: "XNVME_SPEC_ZND_STATE_OFFLINE",
}
XNVME_SPEC_ZND_STATE_EMPTY = 1
XNVME_SPEC_ZND_STATE_IOPEN = 2
XNVME_SPEC_ZND_STATE_EOPEN = 3
XNVME_SPEC_ZND_STATE_CLOSED = 4
XNVME_SPEC_ZND_STATE_RONLY = 13
XNVME_SPEC_ZND_STATE_FULL = 14
XNVME_SPEC_ZND_STATE_OFFLINE = 15
xnvme_spec_znd_state = ctypes.c_uint32  # enum


class xnvme_spec_znd_idfy_ctrlr(Structure):
    pass


xnvme_spec_znd_idfy_ctrlr._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ctrlr._fields_ = [
    ("zasl", ctypes.c_ubyte),
    ("rsvd8", ctypes.c_ubyte * 4095),
]


class xnvme_spec_znd_idfy_lbafe(Structure):
    pass


xnvme_spec_znd_idfy_lbafe._pack_ = 1  # source:False
xnvme_spec_znd_idfy_lbafe._fields_ = [
    ("zsze", ctypes.c_uint64),
    ("zdes", ctypes.c_ubyte),
    ("rsvd", ctypes.c_ubyte * 7),
]


class xnvme_spec_znd_idfy_ns(Structure):
    pass


class xnvme_spec_znd_idfy_ns_zrwacap(Union):
    pass


class xnvme_spec_znd_idfy_ns_2_bits(Structure):
    pass


xnvme_spec_znd_idfy_ns_2_bits._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns_2_bits._fields_ = [
    ("expflushsup", ctypes.c_ubyte, 1),
    ("rsvd0", ctypes.c_ubyte, 7),
]

xnvme_spec_znd_idfy_ns_zrwacap._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns_zrwacap._fields_ = [
    ("bits", xnvme_spec_znd_idfy_ns_2_bits),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_znd_idfy_ns_ozcs(Union):
    pass


class xnvme_spec_znd_idfy_ns_1_bits(Structure):
    pass


xnvme_spec_znd_idfy_ns_1_bits._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns_1_bits._fields_ = [
    ("razb", ctypes.c_uint16, 1),
    ("zrwasup", ctypes.c_uint16, 1),
    ("rsvd", ctypes.c_uint16, 14),
]

xnvme_spec_znd_idfy_ns_ozcs._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns_ozcs._fields_ = [
    ("bits", xnvme_spec_znd_idfy_ns_1_bits),
    ("val", ctypes.c_uint16),
]


class xnvme_spec_znd_idfy_ns_zoc(Union):
    pass


class xnvme_spec_znd_idfy_ns_0_bits(Structure):
    pass


xnvme_spec_znd_idfy_ns_0_bits._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns_0_bits._fields_ = [
    ("vzcap", ctypes.c_uint16, 1),
    ("zae", ctypes.c_uint16, 1),
    ("rsvd", ctypes.c_uint16, 14),
]

xnvme_spec_znd_idfy_ns_zoc._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns_zoc._fields_ = [
    ("bits", xnvme_spec_znd_idfy_ns_0_bits),
    ("val", ctypes.c_uint16),
]

xnvme_spec_znd_idfy_ns._pack_ = 1  # source:False
xnvme_spec_znd_idfy_ns._fields_ = [
    ("zoc", xnvme_spec_znd_idfy_ns_zoc),
    ("ozcs", xnvme_spec_znd_idfy_ns_ozcs),
    ("mar", ctypes.c_uint32),
    ("mor", ctypes.c_uint32),
    ("rrl", ctypes.c_uint32),
    ("frl", ctypes.c_uint32),
    ("rsvd12", ctypes.c_ubyte * 24),
    ("numzrwa", ctypes.c_uint32),
    ("zrwafg", ctypes.c_uint16),
    ("zrwas", ctypes.c_uint16),
    ("zrwacap", xnvme_spec_znd_idfy_ns_zrwacap),
    ("rsvd53", ctypes.c_ubyte * 2763),
    ("lbafe", xnvme_spec_znd_idfy_lbafe * 16),
    ("rsvd3072", ctypes.c_ubyte * 768),
    ("vs", ctypes.c_ubyte * 256),
]


class xnvme_spec_znd_idfy(Structure):
    pass


class xnvme_spec_znd_idfy_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("base", xnvme_spec_idfy),
        ("zctrlr", xnvme_spec_znd_idfy_ctrlr),
        ("zns", xnvme_spec_znd_idfy_ns),
    ]


xnvme_spec_znd_idfy._pack_ = 1  # source:False
xnvme_spec_znd_idfy._anonymous_ = ("_0",)
xnvme_spec_znd_idfy._fields_ = [
    ("_0", xnvme_spec_znd_idfy_0),
]


class xnvme_spec_znd_log_changes(Structure):
    pass


xnvme_spec_znd_log_changes._pack_ = 1  # source:False
xnvme_spec_znd_log_changes._fields_ = [
    ("nidents", ctypes.c_uint16),
    ("rsvd2", ctypes.c_ubyte * 6),
    ("idents", ctypes.c_uint64 * 511),
]


class xnvme_spec_znd_descr(Structure):
    pass


xnvme_spec_znd_descr._pack_ = 1  # source:False
xnvme_spec_znd_descr._fields_ = [
    ("zt", ctypes.c_ubyte, 4),
    ("rsvd0", ctypes.c_ubyte, 4),
    ("rsvd1", ctypes.c_ubyte, 4),
    ("zs", ctypes.c_ubyte, 4),
    ("za", ctypes.c_ubyte, 8),
    ("rsvd7", ctypes.c_ubyte * 5),
    ("zcap", ctypes.c_uint64),
    ("zslba", ctypes.c_uint64),
    ("wp", ctypes.c_uint64),
    ("rsvd63", ctypes.c_ubyte * 32),
]


class xnvme_spec_znd_descr_0_0(Structure):
    pass


xnvme_spec_znd_descr_0_0._pack_ = 1  # source:False
xnvme_spec_znd_descr_0_0._fields_ = [
    ("zfc", ctypes.c_ubyte, 1),
    ("zfr", ctypes.c_ubyte, 1),
    ("rzr", ctypes.c_ubyte, 1),
    ("zrwav", ctypes.c_ubyte, 1),
    ("rsvd3", ctypes.c_ubyte, 3),
    ("zdev", ctypes.c_ubyte, 1),
]


class xnvme_spec_znd_descr_za(Union):
    pass


xnvme_spec_znd_descr_za._pack_ = 1  # source:False
xnvme_spec_znd_descr_za._anonymous_ = ("_0",)
xnvme_spec_znd_descr_za._fields_ = [
    ("_0", xnvme_spec_znd_descr_0_0),
    ("val", ctypes.c_ubyte),
]


class xnvme_spec_znd_report_hdr(Structure):
    pass


xnvme_spec_znd_report_hdr._pack_ = 1  # source:False
xnvme_spec_znd_report_hdr._fields_ = [
    ("nzones", ctypes.c_uint64),
    ("rsvd", ctypes.c_ubyte * 56),
]


class xnvme_spec_kvs_idfy_ns_format(Structure):
    pass


xnvme_spec_kvs_idfy_ns_format._pack_ = 1  # source:False
xnvme_spec_kvs_idfy_ns_format._fields_ = [
    ("kml", ctypes.c_uint16),
    ("rsvd2", ctypes.c_ubyte),
    ("fopt", ctypes.c_ubyte),
    ("vml", ctypes.c_uint32),
    ("mnk", ctypes.c_uint32),
    ("rsvd12", ctypes.c_ubyte * 4),
]


class xnvme_spec_kvs_idfy_ns(Structure):
    pass


xnvme_spec_kvs_idfy_ns._pack_ = 1  # source:False
xnvme_spec_kvs_idfy_ns._fields_ = [
    ("nsze", ctypes.c_uint64),
    ("rsvd8", ctypes.c_ubyte * 8),
    ("nuse", ctypes.c_uint64),
    ("nsfeat", ctypes.c_ubyte),
    ("nkvf", ctypes.c_ubyte),
    ("nmic", ctypes.c_ubyte),
    ("rescap", ctypes.c_ubyte),
    ("fpi", ctypes.c_ubyte),
    ("rsvd29", ctypes.c_ubyte * 3),
    ("novg", ctypes.c_uint32),
    ("anagrpid", ctypes.c_uint32),
    ("rsvd40", ctypes.c_ubyte * 3),
    ("nsattr", ctypes.c_ubyte),
    ("nvmsetid", ctypes.c_uint16),
    ("endgid", ctypes.c_uint16),
    ("nguid", ctypes.c_uint64 * 2),
    ("eui64", ctypes.c_uint64),
    ("kvf", xnvme_spec_kvs_idfy_ns_format * 16),
    ("rsvd328", ctypes.c_ubyte * 3512),
    ("vs", ctypes.c_ubyte * 256),
]


class xnvme_spec_kvs_idfy(Structure):
    pass


class xnvme_spec_kvs_idfy_0(Union):
    _pack_ = 1  # source:False
    _fields_ = [
        ("base", xnvme_spec_idfy),
        ("ns", xnvme_spec_kvs_idfy_ns),
    ]


xnvme_spec_kvs_idfy._pack_ = 1  # source:False
xnvme_spec_kvs_idfy._anonymous_ = ("_0",)
xnvme_spec_kvs_idfy._fields_ = [
    ("_0", xnvme_spec_kvs_idfy_0),
]


class struct__IO_FILE(Structure):
    pass


class struct__IO_marker(Structure):
    pass


class struct__IO_wide_data(Structure):
    pass


class struct__IO_codecvt(Structure):
    pass


struct__IO_FILE._pack_ = 1  # source:False
struct__IO_FILE._fields_ = [
    ("_flags", ctypes.c_int32),
    ("PADDING_0", ctypes.c_ubyte * 4),
    ("_IO_read_ptr", ctypes.POINTER(ctypes.c_char)),
    ("_IO_read_end", ctypes.POINTER(ctypes.c_char)),
    ("_IO_read_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_write_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_write_ptr", ctypes.POINTER(ctypes.c_char)),
    ("_IO_write_end", ctypes.POINTER(ctypes.c_char)),
    ("_IO_buf_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_buf_end", ctypes.POINTER(ctypes.c_char)),
    ("_IO_save_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_backup_base", ctypes.POINTER(ctypes.c_char)),
    ("_IO_save_end", ctypes.POINTER(ctypes.c_char)),
    ("_markers", ctypes.POINTER(struct__IO_marker)),
    ("_chain", ctypes.POINTER(struct__IO_FILE)),
    ("_fileno", ctypes.c_int32),
    ("_flags2", ctypes.c_int32),
    ("_old_offset", ctypes.c_int64),
    ("_cur_column", ctypes.c_uint16),
    ("_vtable_offset", ctypes.c_byte),
    ("_shortbuf", ctypes.c_char * 1),
    ("PADDING_1", ctypes.c_ubyte * 4),
    ("_lock", ctypes.POINTER(None)),
    ("_offset", ctypes.c_int64),
    ("_codecvt", ctypes.POINTER(struct__IO_codecvt)),
    ("_wide_data", ctypes.POINTER(struct__IO_wide_data)),
    ("_freeres_list", ctypes.POINTER(struct__IO_FILE)),
    ("_freeres_buf", ctypes.POINTER(None)),
    ("__pad5", ctypes.c_uint64),
    ("_mode", ctypes.c_int32),
    ("_unused2", ctypes.c_char * 20),
]

xnvme_spec_log_health_fpr = _libraries["xnvme"].xnvme_spec_log_health_fpr
xnvme_spec_log_health_fpr.restype = ctypes.c_int32
xnvme_spec_log_health_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_log_health_entry),
    ctypes.c_int32,
]
xnvme_spec_log_health_pr = _libraries["xnvme"].xnvme_spec_log_health_pr
xnvme_spec_log_health_pr.restype = ctypes.c_int32
xnvme_spec_log_health_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_log_health_entry),
    ctypes.c_int32,
]
xnvme_spec_log_erri_fpr = _libraries["xnvme"].xnvme_spec_log_erri_fpr
xnvme_spec_log_erri_fpr.restype = ctypes.c_int32
xnvme_spec_log_erri_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_log_erri_entry),
    ctypes.c_int32,
    ctypes.c_int32,
]
xnvme_spec_log_erri_pr = _libraries["xnvme"].xnvme_spec_log_erri_pr
xnvme_spec_log_erri_pr.restype = ctypes.c_int32
xnvme_spec_log_erri_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_log_erri_entry),
    ctypes.c_int32,
    ctypes.c_int32,
]
xnvme_spec_log_fdp_conf_pr = _libraries["xnvme"].xnvme_spec_log_fdp_conf_pr
xnvme_spec_log_fdp_conf_pr.restype = ctypes.c_int32
xnvme_spec_log_fdp_conf_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_log_fdp_conf),
    ctypes.c_int32,
]
xnvme_spec_log_fdp_stats_pr = _libraries["xnvme"].xnvme_spec_log_fdp_stats_pr
xnvme_spec_log_fdp_stats_pr.restype = ctypes.c_int32
xnvme_spec_log_fdp_stats_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_log_fdp_stats),
    ctypes.c_int32,
]
xnvme_spec_log_fdp_events_pr = _libraries["xnvme"].xnvme_spec_log_fdp_events_pr
xnvme_spec_log_fdp_events_pr.restype = ctypes.c_int32
xnvme_spec_log_fdp_events_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_log_fdp_events),
    ctypes.c_int32,
    ctypes.c_int32,
]
xnvme_spec_log_ruhu_pr = _libraries["xnvme"].xnvme_spec_log_ruhu_pr
xnvme_spec_log_ruhu_pr.restype = ctypes.c_int32
xnvme_spec_log_ruhu_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_log_ruhu),
    ctypes.c_int32,
    ctypes.c_int32,
]
xnvme_spec_ruhs_pr = _libraries["xnvme"].xnvme_spec_ruhs_pr
xnvme_spec_ruhs_pr.restype = ctypes.c_int32
xnvme_spec_ruhs_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_ruhs),
    ctypes.c_int32,
    ctypes.c_int32,
]
xnvme_spec_idfy_ns_fpr = _libraries["xnvme"].xnvme_spec_idfy_ns_fpr
xnvme_spec_idfy_ns_fpr.restype = ctypes.c_int32
xnvme_spec_idfy_ns_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_idfy_ns),
    ctypes.c_int32,
]
xnvme_spec_idfy_ns_pr = _libraries["xnvme"].xnvme_spec_idfy_ns_pr
xnvme_spec_idfy_ns_pr.restype = ctypes.c_int32
xnvme_spec_idfy_ns_pr.argtypes = [ctypes.POINTER(xnvme_spec_idfy_ns), ctypes.c_int32]
xnvme_spec_idfy_ctrl_fpr = _libraries["xnvme"].xnvme_spec_idfy_ctrl_fpr
xnvme_spec_idfy_ctrl_fpr.restype = ctypes.c_int32
xnvme_spec_idfy_ctrl_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_idfy_ctrlr),
    ctypes.c_int32,
]
xnvme_spec_idfy_ctrl_pr = _libraries["xnvme"].xnvme_spec_idfy_ctrl_pr
xnvme_spec_idfy_ctrl_pr.restype = ctypes.c_int32
xnvme_spec_idfy_ctrl_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_idfy_ctrlr),
    ctypes.c_int32,
]
xnvme_spec_idfy_cs_fpr = _libraries["xnvme"].xnvme_spec_idfy_cs_fpr
xnvme_spec_idfy_cs_fpr.restype = ctypes.c_int32
xnvme_spec_idfy_cs_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_idfy_cs),
    ctypes.c_int32,
]
xnvme_spec_idfy_cs_pr = _libraries["xnvme"].xnvme_spec_idfy_cs_pr
xnvme_spec_idfy_cs_pr.restype = ctypes.c_int32
xnvme_spec_idfy_cs_pr.argtypes = [ctypes.POINTER(xnvme_spec_idfy_cs), ctypes.c_int32]
xnvme_spec_feat_fpr = _libraries["xnvme"].xnvme_spec_feat_fpr
xnvme_spec_feat_fpr.restype = ctypes.c_int32
xnvme_spec_feat_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    uint8_t,
    xnvme_spec_feat,
    ctypes.c_int32,
]
xnvme_spec_feat_pr = _libraries["xnvme"].xnvme_spec_feat_pr
xnvme_spec_feat_pr.restype = ctypes.c_int32
xnvme_spec_feat_pr.argtypes = [uint8_t, xnvme_spec_feat, ctypes.c_int32]
xnvme_spec_feat_fdp_events_pr = _libraries["xnvme"].xnvme_spec_feat_fdp_events_pr
xnvme_spec_feat_fdp_events_pr.restype = ctypes.c_int32
xnvme_spec_feat_fdp_events_pr.argtypes = [
    ctypes.POINTER(None),
    xnvme_spec_feat,
    ctypes.c_int32,
]
xnvme_spec_cmd_fpr = _libraries["xnvme"].xnvme_spec_cmd_fpr
xnvme_spec_cmd_fpr.restype = ctypes.c_int32
xnvme_spec_cmd_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_cmd),
    ctypes.c_int32,
]
xnvme_spec_cmd_pr = _libraries["xnvme"].xnvme_spec_cmd_pr
xnvme_spec_cmd_pr.restype = ctypes.c_int32
xnvme_spec_cmd_pr.argtypes = [ctypes.POINTER(xnvme_spec_cmd), ctypes.c_int32]
xnvme_spec_drecv_idfy_pr = _libraries["xnvme"].xnvme_spec_drecv_idfy_pr
xnvme_spec_drecv_idfy_pr.restype = ctypes.c_int32
xnvme_spec_drecv_idfy_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_idfy_dir_rp),
    ctypes.c_int32,
]
xnvme_spec_drecv_srp_pr = _libraries["xnvme"].xnvme_spec_drecv_srp_pr
xnvme_spec_drecv_srp_pr.restype = ctypes.c_int32
xnvme_spec_drecv_srp_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_streams_dir_rp),
    ctypes.c_int32,
]
xnvme_spec_drecv_sgs_pr = _libraries["xnvme"].xnvme_spec_drecv_sgs_pr
xnvme_spec_drecv_sgs_pr.restype = ctypes.c_int32
xnvme_spec_drecv_sgs_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_streams_dir_gs),
    ctypes.c_int32,
]
xnvme_spec_drecv_sar_pr = _libraries["xnvme"].xnvme_spec_drecv_sar_pr
xnvme_spec_drecv_sar_pr.restype = ctypes.c_int32
xnvme_spec_drecv_sar_pr.argtypes = [xnvme_spec_alloc_resource, ctypes.c_int32]
xnvme_spec_nvm_scopy_fmt_zero_fpr = _libraries[
    "xnvme"
].xnvme_spec_nvm_scopy_fmt_zero_fpr
xnvme_spec_nvm_scopy_fmt_zero_fpr.restype = ctypes.c_int32
xnvme_spec_nvm_scopy_fmt_zero_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_nvm_scopy_fmt_zero),
    ctypes.c_int32,
]
xnvme_spec_nvm_scopy_fmt_zero_pr = _libraries["xnvme"].xnvme_spec_nvm_scopy_fmt_zero_pr
xnvme_spec_nvm_scopy_fmt_zero_pr.restype = ctypes.c_int32
xnvme_spec_nvm_scopy_fmt_zero_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_nvm_scopy_fmt_zero),
    ctypes.c_int32,
]
xnvme_spec_nvm_scopy_source_range_fpr = _libraries[
    "xnvme"
].xnvme_spec_nvm_scopy_source_range_fpr
xnvme_spec_nvm_scopy_source_range_fpr.restype = ctypes.c_int32
xnvme_spec_nvm_scopy_source_range_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_nvm_scopy_source_range),
    uint8_t,
    ctypes.c_int32,
]
xnvme_spec_nvm_scopy_source_range_pr = _libraries[
    "xnvme"
].xnvme_spec_nvm_scopy_source_range_pr
xnvme_spec_nvm_scopy_source_range_pr.restype = ctypes.c_int32
xnvme_spec_nvm_scopy_source_range_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_nvm_scopy_source_range),
    uint8_t,
    ctypes.c_int32,
]
xnvme_spec_idfy_ctrlr_fpr = _libraries["xnvme"].xnvme_spec_idfy_ctrlr_fpr
xnvme_spec_idfy_ctrlr_fpr.restype = ctypes.c_int32
xnvme_spec_idfy_ctrlr_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_nvm_idfy_ctrlr),
    ctypes.c_int32,
]
xnvme_spec_nvm_idfy_ctrlr_pr = _libraries["xnvme"].xnvme_spec_nvm_idfy_ctrlr_pr
xnvme_spec_nvm_idfy_ctrlr_pr.restype = ctypes.c_int32
xnvme_spec_nvm_idfy_ctrlr_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_nvm_idfy_ctrlr),
    ctypes.c_int32,
]
xnvme_spec_nvm_idfy_ns_fpr = _libraries["xnvme"].xnvme_spec_nvm_idfy_ns_fpr
xnvme_spec_nvm_idfy_ns_fpr.restype = ctypes.c_int32
xnvme_spec_nvm_idfy_ns_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_nvm_idfy_ns),
    ctypes.c_int32,
]
xnvme_spec_nvm_idfy_ns_pr = _libraries["xnvme"].xnvme_spec_nvm_idfy_ns_pr
xnvme_spec_nvm_idfy_ns_pr.restype = ctypes.c_int32
xnvme_spec_nvm_idfy_ns_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_nvm_idfy_ns),
    ctypes.c_int32,
]
xnvme_spec_znd_idfy_ctrlr_fpr = _libraries["xnvme"].xnvme_spec_znd_idfy_ctrlr_fpr
xnvme_spec_znd_idfy_ctrlr_fpr.restype = ctypes.c_int32
xnvme_spec_znd_idfy_ctrlr_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_idfy_ctrlr),
    ctypes.c_int32,
]
xnvme_spec_znd_idfy_ctrlr_pr = _libraries["xnvme"].xnvme_spec_znd_idfy_ctrlr_pr
xnvme_spec_znd_idfy_ctrlr_pr.restype = ctypes.c_int32
xnvme_spec_znd_idfy_ctrlr_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_znd_idfy_ctrlr),
    ctypes.c_int32,
]
xnvme_spec_znd_idfy_lbafe_fpr = _libraries["xnvme"].xnvme_spec_znd_idfy_lbafe_fpr
xnvme_spec_znd_idfy_lbafe_fpr.restype = ctypes.c_int32
xnvme_spec_znd_idfy_lbafe_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_idfy_lbafe),
    ctypes.c_int32,
]
xnvme_spec_znd_idfy_ns_fpr = _libraries["xnvme"].xnvme_spec_znd_idfy_ns_fpr
xnvme_spec_znd_idfy_ns_fpr.restype = ctypes.c_int32
xnvme_spec_znd_idfy_ns_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_idfy_ns),
    ctypes.c_int32,
]
xnvme_spec_znd_idfy_ns_pr = _libraries["xnvme"].xnvme_spec_znd_idfy_ns_pr
xnvme_spec_znd_idfy_ns_pr.restype = ctypes.c_int32
xnvme_spec_znd_idfy_ns_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_znd_idfy_ns),
    ctypes.c_int32,
]
xnvme_spec_znd_log_changes_fpr = _libraries["xnvme"].xnvme_spec_znd_log_changes_fpr
xnvme_spec_znd_log_changes_fpr.restype = ctypes.c_int32
xnvme_spec_znd_log_changes_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_log_changes),
    ctypes.c_int32,
]
xnvme_spec_znd_log_changes_pr = _libraries["xnvme"].xnvme_spec_znd_log_changes_pr
xnvme_spec_znd_log_changes_pr.restype = ctypes.c_int32
xnvme_spec_znd_log_changes_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_znd_log_changes),
    ctypes.c_int32,
]
xnvme_spec_znd_descr_fpr = _libraries["xnvme"].xnvme_spec_znd_descr_fpr
xnvme_spec_znd_descr_fpr.restype = ctypes.c_int32
xnvme_spec_znd_descr_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_descr),
    ctypes.c_int32,
]
xnvme_spec_znd_descr_pr = _libraries["xnvme"].xnvme_spec_znd_descr_pr
xnvme_spec_znd_descr_pr.restype = ctypes.c_int32
xnvme_spec_znd_descr_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_znd_descr),
    ctypes.c_int32,
]
xnvme_spec_znd_report_hdr_fpr = _libraries["xnvme"].xnvme_spec_znd_report_hdr_fpr
xnvme_spec_znd_report_hdr_fpr.restype = ctypes.c_int32
xnvme_spec_znd_report_hdr_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_report_hdr),
    ctypes.c_int32,
]
xnvme_spec_znd_report_hdr_pr = _libraries["xnvme"].xnvme_spec_znd_report_hdr_pr
xnvme_spec_znd_report_hdr_pr.restype = ctypes.c_int32
xnvme_spec_znd_report_hdr_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_znd_report_hdr),
    ctypes.c_int32,
]
xnvme_spec_znd_descr_fpr_yaml = _libraries["xnvme"].xnvme_spec_znd_descr_fpr_yaml
xnvme_spec_znd_descr_fpr_yaml.restype = ctypes.c_int32
xnvme_spec_znd_descr_fpr_yaml.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_znd_descr),
    ctypes.c_int32,
    ctypes.POINTER(ctypes.c_char),
]
xnvme_spec_kvs_idfy_ns_fpr = _libraries["xnvme"].xnvme_spec_kvs_idfy_ns_fpr
xnvme_spec_kvs_idfy_ns_fpr.restype = ctypes.c_int32
xnvme_spec_kvs_idfy_ns_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_kvs_idfy_ns),
    ctypes.c_int32,
]
xnvme_spec_kvs_idfy_ns_pr = _libraries["xnvme"].xnvme_spec_kvs_idfy_ns_pr
xnvme_spec_kvs_idfy_ns_pr.restype = ctypes.c_int32
xnvme_spec_kvs_idfy_ns_pr.argtypes = [
    ctypes.POINTER(xnvme_spec_kvs_idfy_ns),
    ctypes.c_int32,
]


class xnvme_spec_fs_idfy_ctrlr(Structure):
    pass


class xnvme_spec_fs_idfy_ctrlr_properties(Structure):
    pass


xnvme_spec_fs_idfy_ctrlr_properties._pack_ = 1  # source:False
xnvme_spec_fs_idfy_ctrlr_properties._fields_ = [
    ("permissions_posix", ctypes.c_uint64, 1),
    ("permissions_acl", ctypes.c_uint64, 1),
    ("stamp_creation", ctypes.c_uint64, 1),
    ("stamp_access", ctypes.c_uint64, 1),
    ("stamp_change", ctypes.c_uint64, 1),
    ("stamp_archive", ctypes.c_uint64, 1),
    ("hardlinks", ctypes.c_uint64, 1),
    ("symlinks", ctypes.c_uint64, 1),
    ("case_sensitive", ctypes.c_uint64, 1),
    ("case_preserving", ctypes.c_uint64, 1),
    ("journaling_block", ctypes.c_uint64, 1),
    ("journaling_meta", ctypes.c_uint64, 1),
    ("snapshotting", ctypes.c_uint64, 1),
    ("compressed", ctypes.c_uint64, 1),
    ("encrypted", ctypes.c_uint64, 1),
    ("rsvd", ctypes.c_uint64, 48),
    ("PADDING_0", ctypes.c_uint8, 1),
]


class xnvme_spec_fs_idfy_ctrlr_limits(Structure):
    pass


xnvme_spec_fs_idfy_ctrlr_limits._pack_ = 1  # source:False
xnvme_spec_fs_idfy_ctrlr_limits._fields_ = [
    ("file_data_size", ctypes.c_uint64),
    ("file_name_len", ctypes.c_uint64),
    ("path_name_len", ctypes.c_uint64),
    ("number_of_files", ctypes.c_uint64),
]


class xnvme_spec_fs_idfy_ctrlr_iosizes(Structure):
    pass


xnvme_spec_fs_idfy_ctrlr_iosizes._pack_ = 1  # source:False
xnvme_spec_fs_idfy_ctrlr_iosizes._fields_ = [
    ("min", ctypes.c_uint32),
    ("max", ctypes.c_uint32),
    ("opt", ctypes.c_uint32),
]


class xnvme_spec_fs_idfy_ctrlr_caps(Structure):
    pass


xnvme_spec_fs_idfy_ctrlr_caps._pack_ = 1  # source:False
xnvme_spec_fs_idfy_ctrlr_caps._fields_ = [
    ("direct", ctypes.c_uint64, 1),
    ("rsvd", ctypes.c_uint64, 63),
]

xnvme_spec_fs_idfy_ctrlr._pack_ = 1  # source:False
xnvme_spec_fs_idfy_ctrlr._fields_ = [
    ("byte0_519", ctypes.c_ubyte * 520),
    ("caps", xnvme_spec_fs_idfy_ctrlr_caps),
    ("limits", xnvme_spec_fs_idfy_ctrlr_limits),
    ("properties", xnvme_spec_fs_idfy_ctrlr_properties),
    ("iosizes", xnvme_spec_fs_idfy_ctrlr_iosizes),
    ("rsvd", ctypes.c_ubyte * 3509),
    ("ac", ctypes.c_ubyte),
    ("dc", ctypes.c_ubyte),
    ("PADDING_0", ctypes.c_ubyte * 5),
]


class xnvme_spec_fs_idfy_ns(Structure):
    pass


xnvme_spec_fs_idfy_ns._pack_ = 1  # source:False
xnvme_spec_fs_idfy_ns._fields_ = [
    ("nsze", ctypes.c_uint64),
    ("ncap", ctypes.c_uint64),
    ("nuse", ctypes.c_uint64),
    ("rsvd", ctypes.c_ubyte * 3816),
    ("vendor_specific", ctypes.c_ubyte * 254),
    ("ac", ctypes.c_ubyte),
    ("dc", ctypes.c_ubyte),
]


# values for enumeration 'xnvme_spec_fs_opcs'
xnvme_spec_fs_opcs__enumvalues = {
    173: "XNVME_SPEC_FS_OPC_FLUSH",
    172: "XNVME_SPEC_FS_OPC_WRITE",
    220: "XNVME_SPEC_FS_OPC_READ",
}
XNVME_SPEC_FS_OPC_FLUSH = 173
XNVME_SPEC_FS_OPC_WRITE = 172
XNVME_SPEC_FS_OPC_READ = 220
xnvme_spec_fs_opcs = ctypes.c_uint32  # enum
xnvme_spec_adm_opc_str = _libraries["xnvme"].xnvme_spec_adm_opc_str
xnvme_spec_adm_opc_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_adm_opc_str.argtypes = [xnvme_spec_adm_opc]
xnvme_spec_csi_str = _libraries["xnvme"].xnvme_spec_csi_str
xnvme_spec_csi_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_csi_str.argtypes = [xnvme_spec_csi]
xnvme_spec_feat_id_str = _libraries["xnvme"].xnvme_spec_feat_id_str
xnvme_spec_feat_id_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_feat_id_str.argtypes = [xnvme_spec_feat_id]
xnvme_spec_feat_sel_str = _libraries["xnvme"].xnvme_spec_feat_sel_str
xnvme_spec_feat_sel_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_feat_sel_str.argtypes = [xnvme_spec_feat_sel]
xnvme_spec_flag_str = _libraries["xnvme"].xnvme_spec_flag_str
xnvme_spec_flag_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_flag_str.argtypes = [xnvme_spec_flag]
xnvme_spec_idfy_cns_str = _libraries["xnvme"].xnvme_spec_idfy_cns_str
xnvme_spec_idfy_cns_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_idfy_cns_str.argtypes = [xnvme_spec_idfy_cns]
xnvme_spec_log_lpi_str = _libraries["xnvme"].xnvme_spec_log_lpi_str
xnvme_spec_log_lpi_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_log_lpi_str.argtypes = [xnvme_spec_log_lpi]
xnvme_spec_znd_log_lid_str = _libraries["xnvme"].xnvme_spec_znd_log_lid_str
xnvme_spec_znd_log_lid_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_log_lid_str.argtypes = [xnvme_spec_znd_log_lid]
xnvme_spec_nvm_cmd_cpl_sc_str = _libraries["xnvme"].xnvme_spec_nvm_cmd_cpl_sc_str
xnvme_spec_nvm_cmd_cpl_sc_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_nvm_cmd_cpl_sc_str.argtypes = [xnvme_spec_nvm_cmd_cpl_sc]
xnvme_spec_nvm_opc_str = _libraries["xnvme"].xnvme_spec_nvm_opc_str
xnvme_spec_nvm_opc_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_nvm_opc_str.argtypes = [xnvme_spec_nvm_opc]
xnvme_spec_psdt_str = _libraries["xnvme"].xnvme_spec_psdt_str
xnvme_spec_psdt_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_psdt_str.argtypes = [xnvme_spec_psdt]
xnvme_spec_sgl_descriptor_subtype_str = _libraries[
    "xnvme"
].xnvme_spec_sgl_descriptor_subtype_str
xnvme_spec_sgl_descriptor_subtype_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_sgl_descriptor_subtype_str.argtypes = [xnvme_spec_sgl_descriptor_subtype]
xnvme_spec_znd_cmd_mgmt_recv_action_str = _libraries[
    "xnvme"
].xnvme_spec_znd_cmd_mgmt_recv_action_str
xnvme_spec_znd_cmd_mgmt_recv_action_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_cmd_mgmt_recv_action_str.argtypes = [xnvme_spec_znd_cmd_mgmt_recv_action]
xnvme_spec_znd_cmd_mgmt_recv_action_sf_str = _libraries[
    "xnvme"
].xnvme_spec_znd_cmd_mgmt_recv_action_sf_str
xnvme_spec_znd_cmd_mgmt_recv_action_sf_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_cmd_mgmt_recv_action_sf_str.argtypes = [
    xnvme_spec_znd_cmd_mgmt_recv_action_sf
]
xnvme_spec_znd_cmd_mgmt_send_action_str = _libraries[
    "xnvme"
].xnvme_spec_znd_cmd_mgmt_send_action_str
xnvme_spec_znd_cmd_mgmt_send_action_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_cmd_mgmt_send_action_str.argtypes = [xnvme_spec_znd_cmd_mgmt_send_action]
xnvme_spec_znd_opc_str = _libraries["xnvme"].xnvme_spec_znd_opc_str
xnvme_spec_znd_opc_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_opc_str.argtypes = [xnvme_spec_znd_opc]
xnvme_spec_znd_mgmt_send_action_so_str = _libraries[
    "xnvme"
].xnvme_spec_znd_mgmt_send_action_so_str
xnvme_spec_znd_mgmt_send_action_so_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_mgmt_send_action_so_str.argtypes = [xnvme_spec_znd_mgmt_send_action_so]
xnvme_spec_znd_status_code_str = _libraries["xnvme"].xnvme_spec_znd_status_code_str
xnvme_spec_znd_status_code_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_status_code_str.argtypes = [xnvme_spec_znd_status_code]
xnvme_spec_znd_state_str = _libraries["xnvme"].xnvme_spec_znd_state_str
xnvme_spec_znd_state_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_state_str.argtypes = [xnvme_spec_znd_state]
xnvme_spec_znd_type_str = _libraries["xnvme"].xnvme_spec_znd_type_str
xnvme_spec_znd_type_str.restype = ctypes.POINTER(ctypes.c_char)
xnvme_spec_znd_type_str.argtypes = [xnvme_spec_znd_type]
xnvme_spec_ctrlr_bar_fpr = _libraries["xnvme"].xnvme_spec_ctrlr_bar_fpr
xnvme_spec_ctrlr_bar_fpr.restype = ctypes.c_int32
xnvme_spec_ctrlr_bar_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_spec_ctrlr_bar),
    ctypes.c_int32,
]
xnvme_spec_ctrlr_bar_pp = _libraries["xnvme"].xnvme_spec_ctrlr_bar_pp
xnvme_spec_ctrlr_bar_pp.restype = ctypes.c_int32
xnvme_spec_ctrlr_bar_pp.argtypes = [
    ctypes.POINTER(xnvme_spec_ctrlr_bar),
    ctypes.c_int32,
]


class xnvme_cmd_ctx_async(Structure):
    pass


xnvme_cmd_ctx_async._pack_ = 1  # source:False
xnvme_cmd_ctx_async._fields_ = [
    ("queue", ctypes.POINTER(xnvme_queue)),
    ("cb", ctypes.CFUNCTYPE(None, ctypes.POINTER(xnvme_cmd_ctx), ctypes.POINTER(None))),
    ("cb_arg", ctypes.POINTER(None)),
]

xnvme_cmd_ctx._pack_ = 1  # source:False
xnvme_cmd_ctx._fields_ = [
    ("cmd", xnvme_spec_cmd),
    ("cpl", xnvme_spec_cpl),
    ("dev", ctypes.POINTER(xnvme_dev)),
    ("async", xnvme_cmd_ctx_async),
    ("opts", ctypes.c_uint32),
    ("be_rsvd", ctypes.c_ubyte * 12),
]

xnvme_cmd_ctx_from_dev = _libraries["xnvme"].xnvme_cmd_ctx_from_dev
xnvme_cmd_ctx_from_dev.restype = xnvme_cmd_ctx
xnvme_cmd_ctx_from_dev.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_cmd_ctx_from_queue = _libraries["xnvme"].xnvme_cmd_ctx_from_queue
xnvme_cmd_ctx_from_queue.restype = ctypes.POINTER(xnvme_cmd_ctx)
xnvme_cmd_ctx_from_queue.argtypes = [ctypes.POINTER(xnvme_queue)]
xnvme_cmd_ctx_clear = _libraries["xnvme"].xnvme_cmd_ctx_clear
xnvme_cmd_ctx_clear.restype = None
xnvme_cmd_ctx_clear.argtypes = [ctypes.POINTER(xnvme_cmd_ctx)]
xnvme_cmd_pass = _libraries["xnvme"].xnvme_cmd_pass
xnvme_cmd_pass.restype = ctypes.c_int32
xnvme_cmd_pass.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(None),
    size_t,
    ctypes.POINTER(None),
    size_t,
]


class struct_iovec(Structure):
    pass


struct_iovec._pack_ = 1  # source:False
struct_iovec._fields_ = [
    ("iov_base", ctypes.POINTER(None)),
    ("iov_len", ctypes.c_uint64),
]

xnvme_cmd_passv = _libraries["xnvme"].xnvme_cmd_passv
xnvme_cmd_passv.restype = ctypes.c_int32
xnvme_cmd_passv.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(struct_iovec),
    size_t,
    size_t,
    ctypes.POINTER(struct_iovec),
    size_t,
    size_t,
]
xnvme_cmd_pass_iov = _libraries["xnvme"].xnvme_cmd_pass_iov
xnvme_cmd_pass_iov.restype = ctypes.c_int32
xnvme_cmd_pass_iov.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(struct_iovec),
    size_t,
    size_t,
    ctypes.POINTER(None),
    size_t,
]
xnvme_cmd_pass_admin = _libraries["xnvme"].xnvme_cmd_pass_admin
xnvme_cmd_pass_admin.restype = ctypes.c_int32
xnvme_cmd_pass_admin.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(None),
    size_t,
    ctypes.POINTER(None),
    size_t,
]


class xnvme_lba_range_attr(Structure):
    pass


xnvme_lba_range_attr._pack_ = 1  # source:False
xnvme_lba_range_attr._fields_ = [
    ("is_zoned", ctypes.c_bool),
    ("is_valid", ctypes.c_bool),
]


class xnvme_lba_range(Structure):
    pass


xnvme_lba_range._pack_ = 1  # source:False
xnvme_lba_range._fields_ = [
    ("slba", ctypes.c_uint64),
    ("elba", ctypes.c_uint64),
    ("naddrs", ctypes.c_uint32),
    ("PADDING_0", ctypes.c_ubyte * 4),
    ("nbytes", ctypes.c_uint64),
    ("attr", xnvme_lba_range_attr),
    ("PADDING_1", ctypes.c_ubyte * 6),
]

xnvme_lba_range_fpr = _libraries["xnvme"].xnvme_lba_range_fpr
xnvme_lba_range_fpr.restype = ctypes.c_int32
xnvme_lba_range_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_lba_range),
    ctypes.c_int32,
]
xnvme_lba_range_pr = _libraries["xnvme"].xnvme_lba_range_pr
xnvme_lba_range_pr.restype = ctypes.c_int32
xnvme_lba_range_pr.argtypes = [ctypes.POINTER(xnvme_lba_range), ctypes.c_int32]
xnvme_lba_range_from_offset_nbytes = _libraries[
    "xnvme"
].xnvme_lba_range_from_offset_nbytes
xnvme_lba_range_from_offset_nbytes.restype = xnvme_lba_range
xnvme_lba_range_from_offset_nbytes.argtypes = [
    ctypes.POINTER(xnvme_dev),
    uint64_t,
    uint64_t,
]
xnvme_lba_range_from_slba_elba = _libraries["xnvme"].xnvme_lba_range_from_slba_elba
xnvme_lba_range_from_slba_elba.restype = xnvme_lba_range
xnvme_lba_range_from_slba_elba.argtypes = [
    ctypes.POINTER(xnvme_dev),
    uint64_t,
    uint64_t,
]
xnvme_lba_range_from_slba_naddrs = _libraries["xnvme"].xnvme_lba_range_from_slba_naddrs
xnvme_lba_range_from_slba_naddrs.restype = xnvme_lba_range
xnvme_lba_range_from_slba_naddrs.argtypes = [
    ctypes.POINTER(xnvme_dev),
    uint64_t,
    uint64_t,
]
xnvme_lba_range_from_zdescr = _libraries["xnvme"].xnvme_lba_range_from_zdescr
xnvme_lba_range_from_zdescr.restype = xnvme_lba_range
xnvme_lba_range_from_zdescr.argtypes = [
    ctypes.POINTER(xnvme_dev),
    ctypes.POINTER(xnvme_spec_znd_descr),
]
xnvme_ver_major = _libraries["xnvme"].xnvme_ver_major
xnvme_ver_major.restype = ctypes.c_int32
xnvme_ver_major.argtypes = []
xnvme_ver_minor = _libraries["xnvme"].xnvme_ver_minor
xnvme_ver_minor.restype = ctypes.c_int32
xnvme_ver_minor.argtypes = []
xnvme_ver_patch = _libraries["xnvme"].xnvme_ver_patch
xnvme_ver_patch.restype = ctypes.c_int32
xnvme_ver_patch.argtypes = []
xnvme_ver_fpr = _libraries["xnvme"].xnvme_ver_fpr
xnvme_ver_fpr.restype = ctypes.c_int32
xnvme_ver_fpr.argtypes = [ctypes.POINTER(struct__IO_FILE), ctypes.c_int32]
xnvme_ver_pr = _libraries["xnvme"].xnvme_ver_pr
xnvme_ver_pr.restype = ctypes.c_int32
xnvme_ver_pr.argtypes = [ctypes.c_int32]

# values for enumeration 'xnvme_pr'
xnvme_pr__enumvalues = {
    0: "XNVME_PR_DEF",
    1: "XNVME_PR_YAML",
    2: "XNVME_PR_TERSE",
}
XNVME_PR_DEF = 0
XNVME_PR_YAML = 1
XNVME_PR_TERSE = 2
xnvme_pr = ctypes.c_uint32  # enum
xnvme_be_attr_fpr = _libraries["xnvme"].xnvme_be_attr_fpr
xnvme_be_attr_fpr.restype = ctypes.c_int32
xnvme_be_attr_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_be_attr),
    ctypes.c_int32,
]
xnvme_be_attr_pr = _libraries["xnvme"].xnvme_be_attr_pr
xnvme_be_attr_pr.restype = ctypes.c_int32
xnvme_be_attr_pr.argtypes = [ctypes.POINTER(xnvme_be_attr), ctypes.c_int32]
xnvme_be_attr_list_fpr = _libraries["xnvme"].xnvme_be_attr_list_fpr
xnvme_be_attr_list_fpr.restype = ctypes.c_int32
xnvme_be_attr_list_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_be_attr_list),
    ctypes.c_int32,
]
xnvme_be_attr_list_pr = _libraries["xnvme"].xnvme_be_attr_list_pr
xnvme_be_attr_list_pr.restype = ctypes.c_int32
xnvme_be_attr_list_pr.argtypes = [ctypes.POINTER(xnvme_be_attr_list), ctypes.c_int32]
xnvme_lba_fpr = _libraries["xnvme"].xnvme_lba_fpr
xnvme_lba_fpr.restype = ctypes.c_int32
xnvme_lba_fpr.argtypes = [ctypes.POINTER(struct__IO_FILE), uint64_t, xnvme_pr]
xnvme_lba_pr = _libraries["xnvme"].xnvme_lba_pr
xnvme_lba_pr.restype = ctypes.c_int32
xnvme_lba_pr.argtypes = [uint64_t, xnvme_pr]
xnvme_lba_fprn = _libraries["xnvme"].xnvme_lba_fprn
xnvme_lba_fprn.restype = ctypes.c_int32
xnvme_lba_fprn.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(ctypes.c_uint64),
    uint16_t,
    xnvme_pr,
]
xnvme_lba_prn = _libraries["xnvme"].xnvme_lba_prn
xnvme_lba_prn.restype = ctypes.c_int32
xnvme_lba_prn.argtypes = [ctypes.POINTER(ctypes.c_uint64), uint16_t, xnvme_pr]
xnvme_ident_yaml = _libraries["xnvme"].xnvme_ident_yaml
xnvme_ident_yaml.restype = ctypes.c_int32
xnvme_ident_yaml.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_ident),
    ctypes.c_int32,
    ctypes.POINTER(ctypes.c_char),
    ctypes.c_int32,
]
xnvme_ident_fpr = _libraries["xnvme"].xnvme_ident_fpr
xnvme_ident_fpr.restype = ctypes.c_int32
xnvme_ident_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_ident),
    ctypes.c_int32,
]
xnvme_ident_pr = _libraries["xnvme"].xnvme_ident_pr
xnvme_ident_pr.restype = ctypes.c_int32
xnvme_ident_pr.argtypes = [ctypes.POINTER(xnvme_ident), ctypes.c_int32]
xnvme_dev_fpr = _libraries["xnvme"].xnvme_dev_fpr
xnvme_dev_fpr.restype = ctypes.c_int32
xnvme_dev_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_dev),
    ctypes.c_int32,
]
xnvme_dev_pr = _libraries["xnvme"].xnvme_dev_pr
xnvme_dev_pr.restype = ctypes.c_int32
xnvme_dev_pr.argtypes = [ctypes.POINTER(xnvme_dev), ctypes.c_int32]
xnvme_geo_fpr = _libraries["xnvme"].xnvme_geo_fpr
xnvme_geo_fpr.restype = ctypes.c_int32
xnvme_geo_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_geo),
    ctypes.c_int32,
]
xnvme_geo_pr = _libraries["xnvme"].xnvme_geo_pr
xnvme_geo_pr.restype = ctypes.c_int32
xnvme_geo_pr.argtypes = [ctypes.POINTER(xnvme_geo), ctypes.c_int32]
xnvme_cmd_ctx_pr = _libraries["xnvme"].xnvme_cmd_ctx_pr
xnvme_cmd_ctx_pr.restype = None
xnvme_cmd_ctx_pr.argtypes = [ctypes.POINTER(xnvme_cmd_ctx), ctypes.c_int32]
xnvme_opts_pr = _libraries["xnvme"].xnvme_opts_pr
xnvme_opts_pr.restype = ctypes.c_int32
xnvme_opts_pr.argtypes = [ctypes.POINTER(xnvme_opts), ctypes.c_int32]
xnvme_file_open = _libraries["xnvme"].xnvme_file_open
xnvme_file_open.restype = ctypes.POINTER(xnvme_dev)
xnvme_file_open.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(xnvme_opts)]
xnvme_file_close = _libraries["xnvme"].xnvme_file_close
xnvme_file_close.restype = ctypes.c_int32
xnvme_file_close.argtypes = [ctypes.POINTER(xnvme_dev)]
off_t = ctypes.c_int64
xnvme_file_pread = _libraries["xnvme"].xnvme_file_pread
xnvme_file_pread.restype = ctypes.c_int32
xnvme_file_pread.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(None),
    size_t,
    off_t,
]
xnvme_file_pwrite = _libraries["xnvme"].xnvme_file_pwrite
xnvme_file_pwrite.restype = ctypes.c_int32
xnvme_file_pwrite.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(None),
    size_t,
    off_t,
]
xnvme_file_sync = _libraries["xnvme"].xnvme_file_sync
xnvme_file_sync.restype = ctypes.c_int32
xnvme_file_sync.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_file_get_cmd_ctx = _libraries["xnvme"].xnvme_file_get_cmd_ctx
xnvme_file_get_cmd_ctx.restype = xnvme_cmd_ctx
xnvme_file_get_cmd_ctx.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_adm_idfy = _libraries["xnvme"].xnvme_adm_idfy
xnvme_adm_idfy.restype = ctypes.c_int32
xnvme_adm_idfy.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint8_t,
    uint16_t,
    uint8_t,
    uint16_t,
    uint8_t,
    ctypes.POINTER(xnvme_spec_idfy),
]
xnvme_adm_idfy_ctrlr = _libraries["xnvme"].xnvme_adm_idfy_ctrlr
xnvme_adm_idfy_ctrlr.restype = ctypes.c_int32
xnvme_adm_idfy_ctrlr.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    ctypes.POINTER(xnvme_spec_idfy),
]
xnvme_adm_idfy_ctrlr_csi = _libraries["xnvme"].xnvme_adm_idfy_ctrlr_csi
xnvme_adm_idfy_ctrlr_csi.restype = ctypes.c_int32
xnvme_adm_idfy_ctrlr_csi.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint8_t,
    ctypes.POINTER(xnvme_spec_idfy),
]
xnvme_adm_idfy_ns = _libraries["xnvme"].xnvme_adm_idfy_ns
xnvme_adm_idfy_ns.restype = ctypes.c_int32
xnvme_adm_idfy_ns.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(xnvme_spec_idfy),
]
xnvme_adm_idfy_ns_csi = _libraries["xnvme"].xnvme_adm_idfy_ns_csi
xnvme_adm_idfy_ns_csi.restype = ctypes.c_int32
xnvme_adm_idfy_ns_csi.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    ctypes.POINTER(xnvme_spec_idfy),
]
xnvme_prep_adm_log = _libraries["xnvme"].xnvme_prep_adm_log
xnvme_prep_adm_log.restype = None
xnvme_prep_adm_log.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint8_t,
    uint8_t,
    uint64_t,
    uint32_t,
    uint8_t,
    uint32_t,
]
xnvme_adm_log = _libraries["xnvme"].xnvme_adm_log
xnvme_adm_log.restype = ctypes.c_int32
xnvme_adm_log.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint8_t,
    uint8_t,
    uint64_t,
    uint32_t,
    uint8_t,
    ctypes.POINTER(None),
    uint32_t,
]
xnvme_prep_adm_gfeat = _libraries["xnvme"].xnvme_prep_adm_gfeat
xnvme_prep_adm_gfeat.restype = None
xnvme_prep_adm_gfeat.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint8_t,
]
xnvme_prep_adm_sfeat = _libraries["xnvme"].xnvme_prep_adm_sfeat
xnvme_prep_adm_sfeat.restype = None
xnvme_prep_adm_sfeat.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint32_t,
    uint8_t,
]
xnvme_adm_gfeat = _libraries["xnvme"].xnvme_adm_gfeat
xnvme_adm_gfeat.restype = ctypes.c_int32
xnvme_adm_gfeat.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint8_t,
    ctypes.POINTER(None),
    size_t,
]
xnvme_adm_sfeat = _libraries["xnvme"].xnvme_adm_sfeat
xnvme_adm_sfeat.restype = ctypes.c_int32
xnvme_adm_sfeat.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint32_t,
    uint8_t,
    ctypes.POINTER(None),
    size_t,
]
xnvme_adm_format = _libraries["xnvme"].xnvme_adm_format
xnvme_adm_format.restype = ctypes.c_int32
xnvme_adm_format.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint8_t,
    uint8_t,
    uint8_t,
    uint8_t,
    uint8_t,
]
xnvme_nvm_sanitize = _libraries["xnvme"].xnvme_nvm_sanitize
xnvme_nvm_sanitize.restype = ctypes.c_int32
xnvme_nvm_sanitize.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint8_t,
    uint8_t,
    uint32_t,
    uint8_t,
    uint8_t,
    uint8_t,
]
xnvme_adm_dir_send = _libraries["xnvme"].xnvme_adm_dir_send
xnvme_adm_dir_send.restype = ctypes.c_int32
xnvme_adm_dir_send.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint32_t,
    uint32_t,
    uint32_t,
]
xnvme_adm_dir_recv = _libraries["xnvme"].xnvme_adm_dir_recv
xnvme_adm_dir_recv.restype = ctypes.c_int32
xnvme_adm_dir_recv.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint32_t,
    uint32_t,
    ctypes.POINTER(None),
    size_t,
]
xnvme_nvm_read = _libraries["xnvme"].xnvme_nvm_read
xnvme_nvm_read.restype = ctypes.c_int32
xnvme_nvm_read.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    uint16_t,
    ctypes.POINTER(None),
    ctypes.POINTER(None),
]
xnvme_nvm_write = _libraries["xnvme"].xnvme_nvm_write
xnvme_nvm_write.restype = ctypes.c_int32
xnvme_nvm_write.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    uint16_t,
    ctypes.POINTER(None),
    ctypes.POINTER(None),
]
xnvme_nvm_write_uncorrectable = _libraries["xnvme"].xnvme_nvm_write_uncorrectable
xnvme_nvm_write_uncorrectable.restype = ctypes.c_int32
xnvme_nvm_write_uncorrectable.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    uint16_t,
]
xnvme_nvm_write_zeroes = _libraries["xnvme"].xnvme_nvm_write_zeroes
xnvme_nvm_write_zeroes.restype = ctypes.c_int32
xnvme_nvm_write_zeroes.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    uint16_t,
]
xnvme_prep_nvm = _libraries["xnvme"].xnvme_prep_nvm
xnvme_prep_nvm.restype = None
xnvme_prep_nvm.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint8_t,
    uint32_t,
    uint64_t,
    uint16_t,
]
xnvme_nvm_scopy = _libraries["xnvme"].xnvme_nvm_scopy
xnvme_nvm_scopy.restype = ctypes.c_int32
xnvme_nvm_scopy.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    ctypes.POINTER(xnvme_spec_nvm_scopy_fmt_zero),
    uint8_t,
    xnvme_nvm_scopy_fmt,
]
xnvme_nvm_dsm = _libraries["xnvme"].xnvme_nvm_dsm
xnvme_nvm_dsm.restype = ctypes.c_int32
xnvme_nvm_dsm.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(xnvme_spec_dsm_range),
    uint8_t,
    ctypes.c_bool,
    ctypes.c_bool,
    ctypes.c_bool,
]
xnvme_nvm_mgmt_recv = _libraries["xnvme"].xnvme_nvm_mgmt_recv
xnvme_nvm_mgmt_recv.restype = ctypes.c_int32
xnvme_nvm_mgmt_recv.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint16_t,
    ctypes.POINTER(None),
    uint32_t,
]
xnvme_nvm_mgmt_send = _libraries["xnvme"].xnvme_nvm_mgmt_send
xnvme_nvm_mgmt_send.restype = ctypes.c_int32
xnvme_nvm_mgmt_send.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint8_t,
    uint16_t,
    ctypes.POINTER(None),
    uint32_t,
]

# values for enumeration 'xnvme_retreive_opts'
xnvme_retreive_opts__enumvalues = {
    1: "XNVME_KVS_RETRIEVE_OPT_RETRIEVE_RAW",
}
XNVME_KVS_RETRIEVE_OPT_RETRIEVE_RAW = 1
xnvme_retreive_opts = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_store_opts'
xnvme_store_opts__enumvalues = {
    1: "XNVME_KVS_STORE_OPT_DONT_STORE_IF_KEY_NOT_EXISTS",
    2: "XNVME_KVS_STORE_OPT_DONT_STORE_IF_KEY_EXISTS",
    4: "XNVME_KVS_STORE_OPT_COMPRESS",
}
XNVME_KVS_STORE_OPT_DONT_STORE_IF_KEY_NOT_EXISTS = 1
XNVME_KVS_STORE_OPT_DONT_STORE_IF_KEY_EXISTS = 2
XNVME_KVS_STORE_OPT_COMPRESS = 4
xnvme_store_opts = ctypes.c_uint32  # enum
xnvme_kvs_retrieve = _libraries["xnvme"].xnvme_kvs_retrieve
xnvme_kvs_retrieve.restype = ctypes.c_int32
xnvme_kvs_retrieve.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(None),
    uint8_t,
    ctypes.POINTER(None),
    uint32_t,
    uint8_t,
]
xnvme_kvs_store = _libraries["xnvme"].xnvme_kvs_store
xnvme_kvs_store.restype = ctypes.c_int32
xnvme_kvs_store.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(None),
    uint8_t,
    ctypes.POINTER(None),
    uint32_t,
    uint8_t,
]
xnvme_kvs_delete = _libraries["xnvme"].xnvme_kvs_delete
xnvme_kvs_delete.restype = ctypes.c_int32
xnvme_kvs_delete.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(None),
    uint8_t,
]
xnvme_kvs_exist = _libraries["xnvme"].xnvme_kvs_exist
xnvme_kvs_exist.restype = ctypes.c_int32
xnvme_kvs_exist.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(None),
    uint8_t,
]
xnvme_kvs_list = _libraries["xnvme"].xnvme_kvs_list
xnvme_kvs_list.restype = ctypes.c_int32
xnvme_kvs_list.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    ctypes.POINTER(None),
    uint8_t,
    ctypes.POINTER(None),
    uint32_t,
]
xnvme_znd_dev_get_ns = _libraries["xnvme"].xnvme_znd_dev_get_ns
xnvme_znd_dev_get_ns.restype = ctypes.POINTER(xnvme_spec_znd_idfy_ns)
xnvme_znd_dev_get_ns.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_znd_dev_get_ctrlr = _libraries["xnvme"].xnvme_znd_dev_get_ctrlr
xnvme_znd_dev_get_ctrlr.restype = ctypes.POINTER(xnvme_spec_znd_idfy_ctrlr)
xnvme_znd_dev_get_ctrlr.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_znd_dev_get_lbafe = _libraries["xnvme"].xnvme_znd_dev_get_lbafe
xnvme_znd_dev_get_lbafe.restype = ctypes.POINTER(xnvme_spec_znd_idfy_lbafe)
xnvme_znd_dev_get_lbafe.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_znd_mgmt_recv = _libraries["xnvme"].xnvme_znd_mgmt_recv
xnvme_znd_mgmt_recv.restype = ctypes.c_int32
xnvme_znd_mgmt_recv.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    xnvme_spec_znd_cmd_mgmt_recv_action,
    xnvme_spec_znd_cmd_mgmt_recv_action_sf,
    uint8_t,
    ctypes.POINTER(None),
    uint32_t,
]
xnvme_znd_descr_from_dev = _libraries["xnvme"].xnvme_znd_descr_from_dev
xnvme_znd_descr_from_dev.restype = ctypes.c_int32
xnvme_znd_descr_from_dev.argtypes = [
    ctypes.POINTER(xnvme_dev),
    uint64_t,
    ctypes.POINTER(xnvme_spec_znd_descr),
]
xnvme_znd_descr_from_dev_in_state = _libraries[
    "xnvme"
].xnvme_znd_descr_from_dev_in_state
xnvme_znd_descr_from_dev_in_state.restype = ctypes.c_int32
xnvme_znd_descr_from_dev_in_state.argtypes = [
    ctypes.POINTER(xnvme_dev),
    xnvme_spec_znd_state,
    ctypes.POINTER(xnvme_spec_znd_descr),
]
xnvme_znd_stat = _libraries["xnvme"].xnvme_znd_stat
xnvme_znd_stat.restype = ctypes.c_int32
xnvme_znd_stat.argtypes = [
    ctypes.POINTER(xnvme_dev),
    xnvme_spec_znd_cmd_mgmt_recv_action_sf,
    ctypes.POINTER(ctypes.c_uint64),
]
xnvme_znd_log_changes_from_dev = _libraries["xnvme"].xnvme_znd_log_changes_from_dev
xnvme_znd_log_changes_from_dev.restype = ctypes.POINTER(xnvme_spec_znd_log_changes)
xnvme_znd_log_changes_from_dev.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_znd_mgmt_send = _libraries["xnvme"].xnvme_znd_mgmt_send
xnvme_znd_mgmt_send.restype = ctypes.c_int32
xnvme_znd_mgmt_send.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    ctypes.c_bool,
    xnvme_spec_znd_cmd_mgmt_send_action,
    xnvme_spec_znd_mgmt_send_action_so,
    ctypes.POINTER(None),
]
xnvme_znd_append = _libraries["xnvme"].xnvme_znd_append
xnvme_znd_append.restype = ctypes.c_int32
xnvme_znd_append.argtypes = [
    ctypes.POINTER(xnvme_cmd_ctx),
    uint32_t,
    uint64_t,
    uint16_t,
    ctypes.POINTER(None),
    ctypes.POINTER(None),
]
xnvme_znd_zrwa_flush = _libraries["xnvme"].xnvme_znd_zrwa_flush
xnvme_znd_zrwa_flush.restype = ctypes.c_int32
xnvme_znd_zrwa_flush.argtypes = [ctypes.POINTER(xnvme_cmd_ctx), uint32_t, uint64_t]


class xnvme_znd_report(Structure):
    pass


xnvme_znd_report._pack_ = 1  # source:False
xnvme_znd_report._fields_ = [
    ("nzones", ctypes.c_uint64),
    ("zd_nbytes", ctypes.c_uint32),
    ("zdext_nbytes", ctypes.c_uint32),
    ("zslba", ctypes.c_uint64),
    ("zelba", ctypes.c_uint64),
    ("nentries", ctypes.c_uint32),
    ("extended", ctypes.c_ubyte),
    ("_pad", ctypes.c_ubyte * 3),
    ("zrent_nbytes", ctypes.c_uint64),
    ("report_nbytes", ctypes.c_uint64),
    ("entries_nbytes", ctypes.c_uint64),
    ("storage", ctypes.c_ubyte * 0),
]

xnvme_znd_report_fpr = _libraries["xnvme"].xnvme_znd_report_fpr
xnvme_znd_report_fpr.restype = ctypes.c_int32
xnvme_znd_report_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_znd_report),
    ctypes.c_int32,
]
xnvme_znd_report_pr = _libraries["xnvme"].xnvme_znd_report_pr
xnvme_znd_report_pr.restype = ctypes.c_int32
xnvme_znd_report_pr.argtypes = [ctypes.POINTER(xnvme_znd_report), ctypes.c_int32]
xnvme_znd_report_from_dev = _libraries["xnvme"].xnvme_znd_report_from_dev
xnvme_znd_report_from_dev.restype = ctypes.POINTER(xnvme_znd_report)
xnvme_znd_report_from_dev.argtypes = [
    ctypes.POINTER(xnvme_dev),
    uint64_t,
    size_t,
    uint8_t,
]
xnvme_znd_report_find_arbitrary = _libraries["xnvme"].xnvme_znd_report_find_arbitrary
xnvme_znd_report_find_arbitrary.restype = ctypes.c_int32
xnvme_znd_report_find_arbitrary.argtypes = [
    ctypes.POINTER(xnvme_znd_report),
    xnvme_spec_znd_state,
    ctypes.POINTER(ctypes.c_uint64),
    ctypes.c_int32,
]


class xnvme_subsystem(Structure):
    pass


xnvme_subsystem._pack_ = 1  # source:False
xnvme_subsystem._fields_ = [
    ("dev", ctypes.POINTER(xnvme_dev)),
    ("controllers", ctypes.POINTER(xnvme_dev)),
]


class xnvme_controller(Structure):
    pass


xnvme_controller._pack_ = 1  # source:False
xnvme_controller._fields_ = [
    ("dev", ctypes.POINTER(xnvme_dev)),
    ("namespaces", ctypes.POINTER(xnvme_dev)),
]


class xnvme_namespace(Structure):
    pass


xnvme_namespace._pack_ = 1  # source:False
xnvme_namespace._fields_ = [
    ("dev", ctypes.POINTER(xnvme_dev)),
]

xnvme_subsystem_reset = _libraries["xnvme"].xnvme_subsystem_reset
xnvme_subsystem_reset.restype = ctypes.c_int32
xnvme_subsystem_reset.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_controller_reset = _libraries["xnvme"].xnvme_controller_reset
xnvme_controller_reset.restype = ctypes.c_int32
xnvme_controller_reset.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_namespace_rescan = _libraries["xnvme"].xnvme_namespace_rescan
xnvme_namespace_rescan.restype = ctypes.c_int32
xnvme_namespace_rescan.argtypes = [ctypes.POINTER(xnvme_dev)]
xnvme_controller_get_registers = _libraries["xnvme"].xnvme_controller_get_registers
xnvme_controller_get_registers.restype = ctypes.c_int32
xnvme_controller_get_registers.argtypes = [
    ctypes.POINTER(xnvme_dev),
    ctypes.POINTER(xnvme_spec_ctrlr_bar),
]
xnvme_libconf = []  # Variable ctypes.POINTER(ctypes.c_char) * 0
xnvme_libconf_fpr = _libraries["xnvme"].xnvme_libconf_fpr
xnvme_libconf_fpr.restype = ctypes.c_int32
xnvme_libconf_fpr.argtypes = [ctypes.POINTER(struct__IO_FILE), xnvme_pr]
xnvme_libconf_pr = _libraries["xnvme"].xnvme_libconf_pr
xnvme_libconf_pr.restype = ctypes.c_int32
xnvme_libconf_pr.argtypes = [xnvme_pr]


class xnvme_cli_args(Structure):
    pass


xnvme_cli_args._pack_ = 1  # source:False
xnvme_cli_args._fields_ = [
    ("dev", ctypes.POINTER(xnvme_dev)),
    ("uri", ctypes.POINTER(ctypes.c_char)),
    ("sys_uri", ctypes.POINTER(ctypes.c_char)),
    ("subnqn", ctypes.POINTER(ctypes.c_char)),
    ("hostnqn", ctypes.POINTER(ctypes.c_char)),
    ("cmd_input", ctypes.POINTER(ctypes.c_char)),
    ("cmd_output", ctypes.POINTER(ctypes.c_char)),
    ("data_nbytes", ctypes.c_uint64),
    ("data_input", ctypes.POINTER(ctypes.c_char)),
    ("data_output", ctypes.POINTER(ctypes.c_char)),
    ("meta_nbytes", ctypes.c_uint64),
    ("meta_input", ctypes.POINTER(ctypes.c_char)),
    ("meta_output", ctypes.POINTER(ctypes.c_char)),
    ("cdw", ctypes.c_uint32 * 16),
    ("lbafl", ctypes.c_uint64),
    ("lba", ctypes.c_uint64),
    ("llb", ctypes.c_uint32),
    ("nlb", ctypes.c_uint32),
    ("slba", ctypes.c_uint64),
    ("elba", ctypes.c_uint64),
    ("uuid", ctypes.c_uint32),
    ("nsid", ctypes.c_uint32),
    ("dev_nsid", ctypes.c_uint32),
    ("cns", ctypes.c_uint32),
    ("csi", ctypes.c_uint32),
    ("PADDING_0", ctypes.c_ubyte * 4),
    ("index", ctypes.c_uint64),
    ("setid", ctypes.c_uint32),
    ("PADDING_1", ctypes.c_ubyte * 4),
    ("cntid", ctypes.c_uint64),
    ("lid", ctypes.c_uint32),
    ("lsp", ctypes.c_uint32),
    ("lpo_nbytes", ctypes.c_uint64),
    ("rae", ctypes.c_uint32),
    ("clear", ctypes.c_uint32),
    ("lbafu", ctypes.c_uint32),
    ("ses", ctypes.c_uint32),
    ("sel", ctypes.c_uint32),
    ("mset", ctypes.c_uint32),
    ("ause", ctypes.c_uint32),
    ("ovrpat", ctypes.c_uint32),
    ("owpass", ctypes.c_uint32),
    ("oipbp", ctypes.c_uint32),
    ("nodas", ctypes.c_uint32),
    ("action", ctypes.c_uint32),
    ("zrms", ctypes.c_uint32),
    ("pi", ctypes.c_uint32),
    ("pil", ctypes.c_uint32),
    ("fid", ctypes.c_uint32),
    ("feat", ctypes.c_uint32),
    ("seed", ctypes.c_uint32),
    ("iosize", ctypes.c_uint32),
    ("qdepth", ctypes.c_uint32),
    ("direct", ctypes.c_uint32),
    ("limit", ctypes.c_uint32),
    ("count", ctypes.c_uint64),
    ("offset", ctypes.c_uint64),
    ("opcode", ctypes.c_uint64),
    ("flags", ctypes.c_uint64),
    ("all", ctypes.c_uint64),
    ("status", ctypes.c_uint32),
    ("save", ctypes.c_uint32),
    ("reset", ctypes.c_uint32),
    ("verbose", ctypes.c_uint32),
    ("help", ctypes.c_uint32),
    ("PADDING_2", ctypes.c_ubyte * 4),
    ("be", ctypes.POINTER(ctypes.c_char)),
    ("mem", ctypes.POINTER(ctypes.c_char)),
    ("sync", ctypes.POINTER(ctypes.c_char)),
    ("async", ctypes.POINTER(ctypes.c_char)),
    ("admin", ctypes.POINTER(ctypes.c_char)),
    ("shm_id", ctypes.c_uint64),
    ("main_core", ctypes.c_uint32),
    ("PADDING_3", ctypes.c_ubyte * 4),
    ("core_mask", ctypes.POINTER(ctypes.c_char)),
    ("css", xnvme_opts_css),
    ("use_cmb_sqs", ctypes.c_uint32),
    ("PADDING_4", ctypes.c_ubyte * 4),
    ("adrfam", ctypes.POINTER(ctypes.c_char)),
    ("poll_io", ctypes.c_uint32),
    ("poll_sq", ctypes.c_uint32),
    ("register_files", ctypes.c_uint32),
    ("register_buffers", ctypes.c_uint32),
    ("truncate", ctypes.c_uint32),
    ("rdonly", ctypes.c_uint32),
    ("wronly", ctypes.c_uint32),
    ("rdwr", ctypes.c_uint32),
    ("create", ctypes.c_uint32),
    ("create_mode", ctypes.c_uint32),
    ("nr", ctypes.c_uint32),
    ("ad", ctypes.c_uint32),
    ("idw", ctypes.c_uint32),
    ("idr", ctypes.c_uint32),
    ("vec_cnt", ctypes.c_uint32),
    ("dtype", ctypes.c_uint32),
    ("dspec", ctypes.c_uint32),
    ("doper", ctypes.c_uint32),
    ("endir", ctypes.c_uint32),
    ("tgtdir", ctypes.c_uint32),
    ("nsr", ctypes.c_uint32),
    ("lsi", ctypes.c_uint32),
    ("pid", ctypes.c_uint32),
    ("PADDING_5", ctypes.c_ubyte * 4),
    ("kv_key", ctypes.POINTER(ctypes.c_char)),
    ("kv_val", ctypes.POINTER(ctypes.c_char)),
    ("kv_store_add", ctypes.c_bool),
    ("kv_store_update", ctypes.c_bool),
    ("kv_store_compress", ctypes.c_bool),
    ("pract", ctypes.c_bool),
    ("prchk", ctypes.c_ubyte),
    ("PADDING_6", ctypes.c_ubyte * 3),
    ("apptag", ctypes.c_uint32),
    ("apptag_mask", ctypes.c_uint32),
]

xnvme_cli_args_pr = _libraries["xnvme"].xnvme_cli_args_pr
xnvme_cli_args_pr.restype = None
xnvme_cli_args_pr.argtypes = [ctypes.POINTER(xnvme_cli_args), ctypes.c_int32]

# values for enumeration 'xnvme_cli_opt'
xnvme_cli_opt__enumvalues = {
    0: "XNVME_CLI_OPT_NONE",
    1: "XNVME_CLI_OPT_CDW00",
    2: "XNVME_CLI_OPT_CDW01",
    3: "XNVME_CLI_OPT_CDW02",
    4: "XNVME_CLI_OPT_CDW03",
    5: "XNVME_CLI_OPT_CDW04",
    6: "XNVME_CLI_OPT_CDW05",
    7: "XNVME_CLI_OPT_CDW06",
    8: "XNVME_CLI_OPT_CDW07",
    9: "XNVME_CLI_OPT_CDW08",
    10: "XNVME_CLI_OPT_CDW09",
    11: "XNVME_CLI_OPT_CDW10",
    12: "XNVME_CLI_OPT_CDW11",
    13: "XNVME_CLI_OPT_CDW12",
    14: "XNVME_CLI_OPT_CDW13",
    15: "XNVME_CLI_OPT_CDW14",
    16: "XNVME_CLI_OPT_CDW15",
    17: "XNVME_CLI_OPT_CMD_INPUT",
    18: "XNVME_CLI_OPT_CMD_OUTPUT",
    19: "XNVME_CLI_OPT_DATA_NBYTES",
    20: "XNVME_CLI_OPT_DATA_INPUT",
    21: "XNVME_CLI_OPT_DATA_OUTPUT",
    22: "XNVME_CLI_OPT_META_NBYTES",
    23: "XNVME_CLI_OPT_META_INPUT",
    24: "XNVME_CLI_OPT_META_OUTPUT",
    25: "XNVME_CLI_OPT_LBAFL",
    26: "XNVME_CLI_OPT_SLBA",
    27: "XNVME_CLI_OPT_ELBA",
    28: "XNVME_CLI_OPT_LBA",
    29: "XNVME_CLI_OPT_NLB",
    30: "XNVME_CLI_OPT_URI",
    31: "XNVME_CLI_OPT_SYS_URI",
    32: "XNVME_CLI_OPT_UUID",
    33: "XNVME_CLI_OPT_NSID",
    34: "XNVME_CLI_OPT_CNS",
    35: "XNVME_CLI_OPT_CSI",
    36: "XNVME_CLI_OPT_INDEX",
    37: "XNVME_CLI_OPT_SETID",
    38: "XNVME_CLI_OPT_CNTID",
    39: "XNVME_CLI_OPT_LID",
    40: "XNVME_CLI_OPT_LSP",
    41: "XNVME_CLI_OPT_LPO_NBYTES",
    42: "XNVME_CLI_OPT_RAE",
    43: "XNVME_CLI_OPT_CLEAR",
    44: "XNVME_CLI_OPT_LBAFU",
    45: "XNVME_CLI_OPT_SES",
    46: "XNVME_CLI_OPT_SEL",
    47: "XNVME_CLI_OPT_MSET",
    48: "XNVME_CLI_OPT_AUSE",
    49: "XNVME_CLI_OPT_OVRPAT",
    50: "XNVME_CLI_OPT_OWPASS",
    51: "XNVME_CLI_OPT_OIPBP",
    52: "XNVME_CLI_OPT_NODAS",
    53: "XNVME_CLI_OPT_ACTION",
    54: "XNVME_CLI_OPT_ZRMS",
    55: "XNVME_CLI_OPT_PI",
    56: "XNVME_CLI_OPT_PIL",
    57: "XNVME_CLI_OPT_FID",
    58: "XNVME_CLI_OPT_FEAT",
    59: "XNVME_CLI_OPT_SEED",
    60: "XNVME_CLI_OPT_LIMIT",
    61: "XNVME_CLI_OPT_IOSIZE",
    62: "XNVME_CLI_OPT_QDEPTH",
    63: "XNVME_CLI_OPT_DIRECT",
    64: "XNVME_CLI_OPT_STATUS",
    65: "XNVME_CLI_OPT_SAVE",
    66: "XNVME_CLI_OPT_RESET",
    67: "XNVME_CLI_OPT_VERBOSE",
    68: "XNVME_CLI_OPT_HELP",
    69: "XNVME_CLI_OPT_COUNT",
    70: "XNVME_CLI_OPT_OFFSET",
    71: "XNVME_CLI_OPT_OPCODE",
    72: "XNVME_CLI_OPT_FLAGS",
    73: "XNVME_CLI_OPT_ALL",
    74: "XNVME_CLI_OPT_BE",
    75: "XNVME_CLI_OPT_MEM",
    76: "XNVME_CLI_OPT_SYNC",
    77: "XNVME_CLI_OPT_ASYNC",
    78: "XNVME_CLI_OPT_ADMIN",
    79: "XNVME_CLI_OPT_SHM_ID",
    80: "XNVME_CLI_OPT_MAIN_CORE",
    81: "XNVME_CLI_OPT_CORE_MASK",
    82: "XNVME_CLI_OPT_USE_CMB_SQS",
    83: "XNVME_CLI_OPT_CSS",
    84: "XNVME_CLI_OPT_POLL_IO",
    85: "XNVME_CLI_OPT_POLL_SQ",
    86: "XNVME_CLI_OPT_REGISTER_FILES",
    87: "XNVME_CLI_OPT_REGISTER_BUFFERS",
    88: "XNVME_CLI_OPT_TRUNCATE",
    89: "XNVME_CLI_OPT_RDONLY",
    90: "XNVME_CLI_OPT_WRONLY",
    91: "XNVME_CLI_OPT_RDWR",
    92: "XNVME_CLI_OPT_CREATE",
    93: "XNVME_CLI_OPT_CREATE_MODE",
    95: "XNVME_CLI_OPT_ADRFAM",
    96: "XNVME_CLI_OPT_DEV_NSID",
    97: "XNVME_CLI_OPT_VEC_CNT",
    98: "XNVME_CLI_OPT_SUBNQN",
    99: "XNVME_CLI_OPT_HOSTNQN",
    100: "XNVME_CLI_OPT_DTYPE",
    101: "XNVME_CLI_OPT_DSPEC",
    102: "XNVME_CLI_OPT_DOPER",
    103: "XNVME_CLI_OPT_ENDIR",
    104: "XNVME_CLI_OPT_TGTDIR",
    105: "XNVME_CLI_OPT_NSR",
    106: "XNVME_CLI_OPT_POSA_TITLE",
    107: "XNVME_CLI_OPT_NON_POSA_TITLE",
    108: "XNVME_CLI_OPT_ORCH_TITLE",
    109: "XNVME_CLI_OPT_AD",
    110: "XNVME_CLI_OPT_IDW",
    111: "XNVME_CLI_OPT_IDR",
    112: "XNVME_CLI_OPT_LLB",
    113: "XNVME_CLI_OPT_LSI",
    114: "XNVME_CLI_OPT_PID",
    115: "XNVME_CLI_OPT_KV_KEY",
    116: "XNVME_CLI_OPT_KV_VAL",
    117: "XNVME_CLI_OPT_KV_STORE_UPDATE",
    118: "XNVME_CLI_OPT_KV_STORE_ADD",
    119: "XNVME_CLI_OPT_KV_STORE_COMPRESS",
    120: "XNVME_CLI_OPT_PRACT",
    121: "XNVME_CLI_OPT_PRCHK",
    122: "XNVME_CLI_OPT_APPTAG",
    123: "XNVME_CLI_OPT_APPTAG_MASK",
    124: "XNVME_CLI_OPT_END",
}
XNVME_CLI_OPT_NONE = 0
XNVME_CLI_OPT_CDW00 = 1
XNVME_CLI_OPT_CDW01 = 2
XNVME_CLI_OPT_CDW02 = 3
XNVME_CLI_OPT_CDW03 = 4
XNVME_CLI_OPT_CDW04 = 5
XNVME_CLI_OPT_CDW05 = 6
XNVME_CLI_OPT_CDW06 = 7
XNVME_CLI_OPT_CDW07 = 8
XNVME_CLI_OPT_CDW08 = 9
XNVME_CLI_OPT_CDW09 = 10
XNVME_CLI_OPT_CDW10 = 11
XNVME_CLI_OPT_CDW11 = 12
XNVME_CLI_OPT_CDW12 = 13
XNVME_CLI_OPT_CDW13 = 14
XNVME_CLI_OPT_CDW14 = 15
XNVME_CLI_OPT_CDW15 = 16
XNVME_CLI_OPT_CMD_INPUT = 17
XNVME_CLI_OPT_CMD_OUTPUT = 18
XNVME_CLI_OPT_DATA_NBYTES = 19
XNVME_CLI_OPT_DATA_INPUT = 20
XNVME_CLI_OPT_DATA_OUTPUT = 21
XNVME_CLI_OPT_META_NBYTES = 22
XNVME_CLI_OPT_META_INPUT = 23
XNVME_CLI_OPT_META_OUTPUT = 24
XNVME_CLI_OPT_LBAFL = 25
XNVME_CLI_OPT_SLBA = 26
XNVME_CLI_OPT_ELBA = 27
XNVME_CLI_OPT_LBA = 28
XNVME_CLI_OPT_NLB = 29
XNVME_CLI_OPT_URI = 30
XNVME_CLI_OPT_SYS_URI = 31
XNVME_CLI_OPT_UUID = 32
XNVME_CLI_OPT_NSID = 33
XNVME_CLI_OPT_CNS = 34
XNVME_CLI_OPT_CSI = 35
XNVME_CLI_OPT_INDEX = 36
XNVME_CLI_OPT_SETID = 37
XNVME_CLI_OPT_CNTID = 38
XNVME_CLI_OPT_LID = 39
XNVME_CLI_OPT_LSP = 40
XNVME_CLI_OPT_LPO_NBYTES = 41
XNVME_CLI_OPT_RAE = 42
XNVME_CLI_OPT_CLEAR = 43
XNVME_CLI_OPT_LBAFU = 44
XNVME_CLI_OPT_SES = 45
XNVME_CLI_OPT_SEL = 46
XNVME_CLI_OPT_MSET = 47
XNVME_CLI_OPT_AUSE = 48
XNVME_CLI_OPT_OVRPAT = 49
XNVME_CLI_OPT_OWPASS = 50
XNVME_CLI_OPT_OIPBP = 51
XNVME_CLI_OPT_NODAS = 52
XNVME_CLI_OPT_ACTION = 53
XNVME_CLI_OPT_ZRMS = 54
XNVME_CLI_OPT_PI = 55
XNVME_CLI_OPT_PIL = 56
XNVME_CLI_OPT_FID = 57
XNVME_CLI_OPT_FEAT = 58
XNVME_CLI_OPT_SEED = 59
XNVME_CLI_OPT_LIMIT = 60
XNVME_CLI_OPT_IOSIZE = 61
XNVME_CLI_OPT_QDEPTH = 62
XNVME_CLI_OPT_DIRECT = 63
XNVME_CLI_OPT_STATUS = 64
XNVME_CLI_OPT_SAVE = 65
XNVME_CLI_OPT_RESET = 66
XNVME_CLI_OPT_VERBOSE = 67
XNVME_CLI_OPT_HELP = 68
XNVME_CLI_OPT_COUNT = 69
XNVME_CLI_OPT_OFFSET = 70
XNVME_CLI_OPT_OPCODE = 71
XNVME_CLI_OPT_FLAGS = 72
XNVME_CLI_OPT_ALL = 73
XNVME_CLI_OPT_BE = 74
XNVME_CLI_OPT_MEM = 75
XNVME_CLI_OPT_SYNC = 76
XNVME_CLI_OPT_ASYNC = 77
XNVME_CLI_OPT_ADMIN = 78
XNVME_CLI_OPT_SHM_ID = 79
XNVME_CLI_OPT_MAIN_CORE = 80
XNVME_CLI_OPT_CORE_MASK = 81
XNVME_CLI_OPT_USE_CMB_SQS = 82
XNVME_CLI_OPT_CSS = 83
XNVME_CLI_OPT_POLL_IO = 84
XNVME_CLI_OPT_POLL_SQ = 85
XNVME_CLI_OPT_REGISTER_FILES = 86
XNVME_CLI_OPT_REGISTER_BUFFERS = 87
XNVME_CLI_OPT_TRUNCATE = 88
XNVME_CLI_OPT_RDONLY = 89
XNVME_CLI_OPT_WRONLY = 90
XNVME_CLI_OPT_RDWR = 91
XNVME_CLI_OPT_CREATE = 92
XNVME_CLI_OPT_CREATE_MODE = 93
XNVME_CLI_OPT_ADRFAM = 95
XNVME_CLI_OPT_DEV_NSID = 96
XNVME_CLI_OPT_VEC_CNT = 97
XNVME_CLI_OPT_SUBNQN = 98
XNVME_CLI_OPT_HOSTNQN = 99
XNVME_CLI_OPT_DTYPE = 100
XNVME_CLI_OPT_DSPEC = 101
XNVME_CLI_OPT_DOPER = 102
XNVME_CLI_OPT_ENDIR = 103
XNVME_CLI_OPT_TGTDIR = 104
XNVME_CLI_OPT_NSR = 105
XNVME_CLI_OPT_POSA_TITLE = 106
XNVME_CLI_OPT_NON_POSA_TITLE = 107
XNVME_CLI_OPT_ORCH_TITLE = 108
XNVME_CLI_OPT_AD = 109
XNVME_CLI_OPT_IDW = 110
XNVME_CLI_OPT_IDR = 111
XNVME_CLI_OPT_LLB = 112
XNVME_CLI_OPT_LSI = 113
XNVME_CLI_OPT_PID = 114
XNVME_CLI_OPT_KV_KEY = 115
XNVME_CLI_OPT_KV_VAL = 116
XNVME_CLI_OPT_KV_STORE_UPDATE = 117
XNVME_CLI_OPT_KV_STORE_ADD = 118
XNVME_CLI_OPT_KV_STORE_COMPRESS = 119
XNVME_CLI_OPT_PRACT = 120
XNVME_CLI_OPT_PRCHK = 121
XNVME_CLI_OPT_APPTAG = 122
XNVME_CLI_OPT_APPTAG_MASK = 123
XNVME_CLI_OPT_END = 124
xnvme_cli_opt = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_cli_opt_type'
xnvme_cli_opt_type__enumvalues = {
    1: "XNVME_CLI_POSA",
    2: "XNVME_CLI_LFLG",
    3: "XNVME_CLI_LOPT",
    4: "XNVME_CLI_LREQ",
    5: "XNVME_CLI_SKIP",
}
XNVME_CLI_POSA = 1
XNVME_CLI_LFLG = 2
XNVME_CLI_LOPT = 3
XNVME_CLI_LREQ = 4
XNVME_CLI_SKIP = 5
xnvme_cli_opt_type = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_cli_opt_value_type'
xnvme_cli_opt_value_type__enumvalues = {
    1: "XNVME_CLI_OPT_VTYPE_URI",
    2: "XNVME_CLI_OPT_VTYPE_NUM",
    3: "XNVME_CLI_OPT_VTYPE_HEX",
    4: "XNVME_CLI_OPT_VTYPE_FILE",
    5: "XNVME_CLI_OPT_VTYPE_STR",
    6: "XNVME_CLI_OPT_VTYPE_SKIP",
}
XNVME_CLI_OPT_VTYPE_URI = 1
XNVME_CLI_OPT_VTYPE_NUM = 2
XNVME_CLI_OPT_VTYPE_HEX = 3
XNVME_CLI_OPT_VTYPE_FILE = 4
XNVME_CLI_OPT_VTYPE_STR = 5
XNVME_CLI_OPT_VTYPE_SKIP = 6
xnvme_cli_opt_value_type = ctypes.c_uint32  # enum


class xnvme_cli_opt_attr(Structure):
    pass


xnvme_cli_opt_attr._pack_ = 1  # source:False
xnvme_cli_opt_attr._fields_ = [
    ("opt", xnvme_cli_opt),
    ("vtype", xnvme_cli_opt_value_type),
    ("name", ctypes.POINTER(ctypes.c_char)),
    ("descr", ctypes.POINTER(ctypes.c_char)),
    ("getoptval", ctypes.c_char),
    ("PADDING_0", ctypes.c_ubyte * 7),
]

xnvme_cli_get_opt_attr = _libraries["xnvme"].xnvme_cli_get_opt_attr
xnvme_cli_get_opt_attr.restype = ctypes.POINTER(xnvme_cli_opt_attr)
xnvme_cli_get_opt_attr.argtypes = [xnvme_cli_opt]


class xnvme_cli_sub_opt(Structure):
    _pack_ = 1  # source:False
    _fields_ = [
        ("opt", xnvme_cli_opt),
        ("type", xnvme_cli_opt_type),
    ]


class xnvme_cli(Structure):
    pass


xnvme_cli_subfunc = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(xnvme_cli))


class xnvme_cli_sub(Structure):
    pass


xnvme_cli_sub._pack_ = 1  # source:False
xnvme_cli_sub._fields_ = [
    ("name", ctypes.POINTER(ctypes.c_char)),
    ("descr_short", ctypes.POINTER(ctypes.c_char)),
    ("descr_long", ctypes.POINTER(ctypes.c_char)),
    ("command", ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.POINTER(xnvme_cli))),
    ("opts", xnvme_cli_sub_opt * 200),
]


class xnvme_timer(Structure):
    pass


xnvme_timer._pack_ = 1  # source:False
xnvme_timer._fields_ = [
    ("start", ctypes.c_uint64),
    ("stop", ctypes.c_uint64),
]


# values for enumeration 'xnvme_cli_opts'
xnvme_cli_opts__enumvalues = {
    0: "XNVME_CLI_INIT_NONE",
    1: "XNVME_CLI_INIT_DEV_OPEN",
}
XNVME_CLI_INIT_NONE = 0
XNVME_CLI_INIT_DEV_OPEN = 1
xnvme_cli_opts = ctypes.c_uint32  # enum


class xnvme_cli_enumeration(Structure):
    pass


xnvme_ident._pack_ = 1  # source:False
xnvme_ident._fields_ = [
    ("subnqn", ctypes.c_char * 256),
    ("uri", ctypes.c_char * 384),
    ("dtype", ctypes.c_uint32),
    ("nsid", ctypes.c_uint32),
    ("csi", ctypes.c_ubyte),
    ("rsvd", ctypes.c_ubyte * 55),
]

xnvme_cli_enumeration._pack_ = 1  # source:False
xnvme_cli_enumeration._fields_ = [
    ("capacity", ctypes.c_uint32),
    ("nentries", ctypes.c_uint32),
    ("entries", xnvme_ident * 0),
]

xnvme_cli_enumeration_alloc = _libraries["xnvme"].xnvme_cli_enumeration_alloc
xnvme_cli_enumeration_alloc.restype = ctypes.c_int32
xnvme_cli_enumeration_alloc.argtypes = [
    ctypes.POINTER(ctypes.POINTER(xnvme_cli_enumeration)),
    uint32_t,
]
xnvme_cli_enumeration_free = _libraries["xnvme"].xnvme_cli_enumeration_free
xnvme_cli_enumeration_free.restype = None
xnvme_cli_enumeration_free.argtypes = [ctypes.POINTER(xnvme_cli_enumeration)]
xnvme_cli_enumeration_append = _libraries["xnvme"].xnvme_cli_enumeration_append
xnvme_cli_enumeration_append.restype = ctypes.c_int32
xnvme_cli_enumeration_append.argtypes = [
    ctypes.POINTER(xnvme_cli_enumeration),
    ctypes.POINTER(xnvme_ident),
]
xnvme_cli_enumeration_fpr = _libraries["xnvme"].xnvme_cli_enumeration_fpr
xnvme_cli_enumeration_fpr.restype = ctypes.c_int32
xnvme_cli_enumeration_fpr.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_cli_enumeration),
    ctypes.c_int32,
]
xnvme_cli_enumeration_fpp = _libraries["xnvme"].xnvme_cli_enumeration_fpp
xnvme_cli_enumeration_fpp.restype = ctypes.c_int32
xnvme_cli_enumeration_fpp.argtypes = [
    ctypes.POINTER(struct__IO_FILE),
    ctypes.POINTER(xnvme_cli_enumeration),
    ctypes.c_int32,
]
xnvme_cli_enumeration_pp = _libraries["xnvme"].xnvme_cli_enumeration_pp
xnvme_cli_enumeration_pp.restype = ctypes.c_int32
xnvme_cli_enumeration_pp.argtypes = [
    ctypes.POINTER(xnvme_cli_enumeration),
    ctypes.c_int32,
]
xnvme_cli_enumeration_pr = _libraries["xnvme"].xnvme_cli_enumeration_pr
xnvme_cli_enumeration_pr.restype = ctypes.c_int32
xnvme_cli_enumeration_pr.argtypes = [
    ctypes.POINTER(xnvme_cli_enumeration),
    ctypes.c_int32,
]
xnvme_cli_timer_start = _libraries["xnvme"].xnvme_cli_timer_start
xnvme_cli_timer_start.restype = uint64_t
xnvme_cli_timer_start.argtypes = [ctypes.POINTER(xnvme_cli)]
xnvme_cli_timer_stop = _libraries["xnvme"].xnvme_cli_timer_stop
xnvme_cli_timer_stop.restype = uint64_t
xnvme_cli_timer_stop.argtypes = [ctypes.POINTER(xnvme_cli)]
xnvme_cli_timer_bw_pr = _libraries["xnvme"].xnvme_cli_timer_bw_pr
xnvme_cli_timer_bw_pr.restype = None
xnvme_cli_timer_bw_pr.argtypes = [
    ctypes.POINTER(xnvme_cli),
    ctypes.POINTER(ctypes.c_char),
    size_t,
]
xnvme_cli_pinf = _libraries["xnvme"].xnvme_cli_pinf
xnvme_cli_pinf.restype = None
xnvme_cli_pinf.argtypes = [ctypes.POINTER(ctypes.c_char)]
xnvme_cli_perr = _libraries["xnvme"].xnvme_cli_perr
xnvme_cli_perr.restype = None
xnvme_cli_perr.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int32]
xnvme_cli_run = _libraries["xnvme"].xnvme_cli_run
xnvme_cli_run.restype = ctypes.c_int32
xnvme_cli_run.argtypes = [
    ctypes.POINTER(xnvme_cli),
    ctypes.c_int32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_char)),
    ctypes.c_int32,
]
xnvme_cli_to_opts = _libraries["xnvme"].xnvme_cli_to_opts
xnvme_cli_to_opts.restype = ctypes.c_int32
xnvme_cli_to_opts.argtypes = [ctypes.POINTER(xnvme_cli), ctypes.POINTER(xnvme_opts)]

# values for enumeration 'xnvme_pi_type'
xnvme_pi_type__enumvalues = {
    0: "XNVME_PI_DISABLE",
    1: "XNVME_PI_TYPE1",
    2: "XNVME_PI_TYPE2",
    3: "XNVME_PI_TYPE3",
}
XNVME_PI_DISABLE = 0
XNVME_PI_TYPE1 = 1
XNVME_PI_TYPE2 = 2
XNVME_PI_TYPE3 = 3
xnvme_pi_type = ctypes.c_uint32  # enum

# values for enumeration 'xnvme_pi_check_type'
xnvme_pi_check_type__enumvalues = {
    1: "XNVME_PI_FLAGS_REFTAG_CHECK",
    2: "XNVME_PI_FLAGS_APPTAG_CHECK",
    4: "XNVME_PI_FLAGS_GUARD_CHECK",
}
XNVME_PI_FLAGS_REFTAG_CHECK = 1
XNVME_PI_FLAGS_APPTAG_CHECK = 2
XNVME_PI_FLAGS_GUARD_CHECK = 4
xnvme_pi_check_type = ctypes.c_uint32  # enum


class xnvme_pi_ctx(Structure):
    pass


xnvme_pi_ctx._pack_ = 1  # source:False
xnvme_pi_ctx._fields_ = [
    ("block_size", ctypes.c_uint32),
    ("md_size", ctypes.c_uint32),
    ("guard_interval", ctypes.c_uint32),
    ("pi_flags", ctypes.c_uint32),
    ("md_interleave", ctypes.c_bool),
    ("PADDING_0", ctypes.c_ubyte),
    ("pi_type", ctypes.c_uint16),
    ("pi_format", ctypes.c_uint16),
    ("PADDING_1", ctypes.c_ubyte * 2),
    ("init_ref_tag", ctypes.c_uint64),
    ("app_tag", ctypes.c_uint16),
    ("apptag_mask", ctypes.c_uint16),
    ("PADDING_2", ctypes.c_ubyte * 4),
]

xnvme_pi_size = _libraries["xnvme"].xnvme_pi_size
xnvme_pi_size.restype = size_t
xnvme_pi_size.argtypes = [xnvme_spec_nvm_ns_pif]
xnvme_pi_ctx_init = _libraries["xnvme"].xnvme_pi_ctx_init
xnvme_pi_ctx_init.restype = ctypes.c_int32
xnvme_pi_ctx_init.argtypes = [
    ctypes.POINTER(xnvme_pi_ctx),
    uint32_t,
    uint32_t,
    ctypes.c_bool,
    ctypes.c_bool,
    xnvme_pi_type,
    uint32_t,
    uint32_t,
    uint16_t,
    uint16_t,
    xnvme_spec_nvm_ns_pif,
]
xnvme_pi_generate = _libraries["xnvme"].xnvme_pi_generate
xnvme_pi_generate.restype = None
xnvme_pi_generate.argtypes = [
    ctypes.POINTER(xnvme_pi_ctx),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    uint32_t,
]
xnvme_pi_verify = _libraries["xnvme"].xnvme_pi_verify
xnvme_pi_verify.restype = ctypes.c_int32
xnvme_pi_verify.argtypes = [
    ctypes.POINTER(xnvme_pi_ctx),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    uint32_t,
]
xnvme_geo._pack_ = 1  # source:False
xnvme_geo._fields_ = [
    ("type", xnvme_geo_type),
    ("npugrp", ctypes.c_uint32),
    ("npunit", ctypes.c_uint32),
    ("nzone", ctypes.c_uint32),
    ("nsect", ctypes.c_uint64),
    ("nbytes", ctypes.c_uint32),
    ("nbytes_oob", ctypes.c_uint32),
    ("tbytes", ctypes.c_uint64),
    ("ssw", ctypes.c_uint64),
    ("mdts_nbytes", ctypes.c_uint32),
    ("lba_nbytes", ctypes.c_uint32),
    ("lba_extended", ctypes.c_ubyte),
    ("pi_type", ctypes.c_ubyte),
    ("pi_loc", ctypes.c_ubyte),
    ("pi_format", ctypes.c_ubyte),
    ("_rsvd", ctypes.c_ubyte * 4),
]

xnvme_cli._pack_ = 1  # source:False
xnvme_cli._fields_ = [
    ("title", ctypes.POINTER(ctypes.c_char)),
    ("descr_short", ctypes.POINTER(ctypes.c_char)),
    ("descr_long", ctypes.POINTER(ctypes.c_char)),
    ("nsubs", ctypes.c_int32),
    ("PADDING_0", ctypes.c_ubyte * 4),
    ("subs", ctypes.POINTER(xnvme_cli_sub)),
    ("ver_pr", ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)),
    ("argc", ctypes.c_int32),
    ("PADDING_1", ctypes.c_ubyte * 4),
    ("argv", ctypes.POINTER(ctypes.POINTER(ctypes.c_char))),
    ("args", xnvme_cli_args),
    ("given", ctypes.c_int32 * 124),
    ("sub", ctypes.POINTER(xnvme_cli_sub)),
    ("timer", xnvme_timer),
]

__all__ = [
    "XNVME_CLI_INIT_DEV_OPEN",
    "XNVME_CLI_INIT_NONE",
    "XNVME_CLI_LFLG",
    "XNVME_CLI_LOPT",
    "XNVME_CLI_LREQ",
    "XNVME_CLI_OPT_ACTION",
    "XNVME_CLI_OPT_AD",
    "XNVME_CLI_OPT_ADMIN",
    "XNVME_CLI_OPT_ADRFAM",
    "XNVME_CLI_OPT_ALL",
    "XNVME_CLI_OPT_APPTAG",
    "XNVME_CLI_OPT_APPTAG_MASK",
    "XNVME_CLI_OPT_ASYNC",
    "XNVME_CLI_OPT_AUSE",
    "XNVME_CLI_OPT_BE",
    "XNVME_CLI_OPT_CDW00",
    "XNVME_CLI_OPT_CDW01",
    "XNVME_CLI_OPT_CDW02",
    "XNVME_CLI_OPT_CDW03",
    "XNVME_CLI_OPT_CDW04",
    "XNVME_CLI_OPT_CDW05",
    "XNVME_CLI_OPT_CDW06",
    "XNVME_CLI_OPT_CDW07",
    "XNVME_CLI_OPT_CDW08",
    "XNVME_CLI_OPT_CDW09",
    "XNVME_CLI_OPT_CDW10",
    "XNVME_CLI_OPT_CDW11",
    "XNVME_CLI_OPT_CDW12",
    "XNVME_CLI_OPT_CDW13",
    "XNVME_CLI_OPT_CDW14",
    "XNVME_CLI_OPT_CDW15",
    "XNVME_CLI_OPT_CLEAR",
    "XNVME_CLI_OPT_CMD_INPUT",
    "XNVME_CLI_OPT_CMD_OUTPUT",
    "XNVME_CLI_OPT_CNS",
    "XNVME_CLI_OPT_CNTID",
    "XNVME_CLI_OPT_CORE_MASK",
    "XNVME_CLI_OPT_COUNT",
    "XNVME_CLI_OPT_CREATE",
    "XNVME_CLI_OPT_CREATE_MODE",
    "XNVME_CLI_OPT_CSI",
    "XNVME_CLI_OPT_CSS",
    "XNVME_CLI_OPT_DATA_INPUT",
    "XNVME_CLI_OPT_DATA_NBYTES",
    "XNVME_CLI_OPT_DATA_OUTPUT",
    "XNVME_CLI_OPT_DEV_NSID",
    "XNVME_CLI_OPT_DIRECT",
    "XNVME_CLI_OPT_DOPER",
    "XNVME_CLI_OPT_DSPEC",
    "XNVME_CLI_OPT_DTYPE",
    "XNVME_CLI_OPT_ELBA",
    "XNVME_CLI_OPT_END",
    "XNVME_CLI_OPT_ENDIR",
    "XNVME_CLI_OPT_FEAT",
    "XNVME_CLI_OPT_FID",
    "XNVME_CLI_OPT_FLAGS",
    "XNVME_CLI_OPT_HELP",
    "XNVME_CLI_OPT_HOSTNQN",
    "XNVME_CLI_OPT_IDR",
    "XNVME_CLI_OPT_IDW",
    "XNVME_CLI_OPT_INDEX",
    "XNVME_CLI_OPT_IOSIZE",
    "XNVME_CLI_OPT_KV_KEY",
    "XNVME_CLI_OPT_KV_STORE_ADD",
    "XNVME_CLI_OPT_KV_STORE_COMPRESS",
    "XNVME_CLI_OPT_KV_STORE_UPDATE",
    "XNVME_CLI_OPT_KV_VAL",
    "XNVME_CLI_OPT_LBA",
    "XNVME_CLI_OPT_LBAFL",
    "XNVME_CLI_OPT_LBAFU",
    "XNVME_CLI_OPT_LID",
    "XNVME_CLI_OPT_LIMIT",
    "XNVME_CLI_OPT_LLB",
    "XNVME_CLI_OPT_LPO_NBYTES",
    "XNVME_CLI_OPT_LSI",
    "XNVME_CLI_OPT_LSP",
    "XNVME_CLI_OPT_MAIN_CORE",
    "XNVME_CLI_OPT_MEM",
    "XNVME_CLI_OPT_META_INPUT",
    "XNVME_CLI_OPT_META_NBYTES",
    "XNVME_CLI_OPT_META_OUTPUT",
    "XNVME_CLI_OPT_MSET",
    "XNVME_CLI_OPT_NLB",
    "XNVME_CLI_OPT_NODAS",
    "XNVME_CLI_OPT_NONE",
    "XNVME_CLI_OPT_NON_POSA_TITLE",
    "XNVME_CLI_OPT_NSID",
    "XNVME_CLI_OPT_NSR",
    "XNVME_CLI_OPT_OFFSET",
    "XNVME_CLI_OPT_OIPBP",
    "XNVME_CLI_OPT_OPCODE",
    "XNVME_CLI_OPT_ORCH_TITLE",
    "XNVME_CLI_OPT_OVRPAT",
    "XNVME_CLI_OPT_OWPASS",
    "XNVME_CLI_OPT_PI",
    "XNVME_CLI_OPT_PID",
    "XNVME_CLI_OPT_PIL",
    "XNVME_CLI_OPT_POLL_IO",
    "XNVME_CLI_OPT_POLL_SQ",
    "XNVME_CLI_OPT_POSA_TITLE",
    "XNVME_CLI_OPT_PRACT",
    "XNVME_CLI_OPT_PRCHK",
    "XNVME_CLI_OPT_QDEPTH",
    "XNVME_CLI_OPT_RAE",
    "XNVME_CLI_OPT_RDONLY",
    "XNVME_CLI_OPT_RDWR",
    "XNVME_CLI_OPT_REGISTER_BUFFERS",
    "XNVME_CLI_OPT_REGISTER_FILES",
    "XNVME_CLI_OPT_RESET",
    "XNVME_CLI_OPT_SAVE",
    "XNVME_CLI_OPT_SEED",
    "XNVME_CLI_OPT_SEL",
    "XNVME_CLI_OPT_SES",
    "XNVME_CLI_OPT_SETID",
    "XNVME_CLI_OPT_SHM_ID",
    "XNVME_CLI_OPT_SLBA",
    "XNVME_CLI_OPT_STATUS",
    "XNVME_CLI_OPT_SUBNQN",
    "XNVME_CLI_OPT_SYNC",
    "XNVME_CLI_OPT_SYS_URI",
    "XNVME_CLI_OPT_TGTDIR",
    "XNVME_CLI_OPT_TRUNCATE",
    "XNVME_CLI_OPT_URI",
    "XNVME_CLI_OPT_USE_CMB_SQS",
    "XNVME_CLI_OPT_UUID",
    "XNVME_CLI_OPT_VEC_CNT",
    "XNVME_CLI_OPT_VERBOSE",
    "XNVME_CLI_OPT_VTYPE_FILE",
    "XNVME_CLI_OPT_VTYPE_HEX",
    "XNVME_CLI_OPT_VTYPE_NUM",
    "XNVME_CLI_OPT_VTYPE_SKIP",
    "XNVME_CLI_OPT_VTYPE_STR",
    "XNVME_CLI_OPT_VTYPE_URI",
    "XNVME_CLI_OPT_WRONLY",
    "XNVME_CLI_OPT_ZRMS",
    "XNVME_CLI_POSA",
    "XNVME_CLI_SKIP",
    "XNVME_ENUMERATE_DEV_CLOSE",
    "XNVME_ENUMERATE_DEV_KEEP_OPEN",
    "XNVME_GEO_CONVENTIONAL",
    "XNVME_GEO_KV",
    "XNVME_GEO_UNKNOWN",
    "XNVME_GEO_ZONED",
    "XNVME_KVS_RETRIEVE_OPT_RETRIEVE_RAW",
    "XNVME_KVS_STORE_OPT_COMPRESS",
    "XNVME_KVS_STORE_OPT_DONT_STORE_IF_KEY_EXISTS",
    "XNVME_KVS_STORE_OPT_DONT_STORE_IF_KEY_NOT_EXISTS",
    "XNVME_NVM_SCOPY_FMT_SRCLEN",
    "XNVME_NVM_SCOPY_FMT_ZERO",
    "XNVME_PI_DISABLE",
    "XNVME_PI_FLAGS_APPTAG_CHECK",
    "XNVME_PI_FLAGS_GUARD_CHECK",
    "XNVME_PI_FLAGS_REFTAG_CHECK",
    "XNVME_PI_TYPE1",
    "XNVME_PI_TYPE2",
    "XNVME_PI_TYPE3",
    "XNVME_PR_DEF",
    "XNVME_PR_TERSE",
    "XNVME_PR_YAML",
    "XNVME_QUEUE_IOPOLL",
    "XNVME_QUEUE_SQPOLL",
    "XNVME_SPEC_ADM_OPC_DRECV",
    "XNVME_SPEC_ADM_OPC_DSEND",
    "XNVME_SPEC_ADM_OPC_GFEAT",
    "XNVME_SPEC_ADM_OPC_IDFY",
    "XNVME_SPEC_ADM_OPC_LOG",
    "XNVME_SPEC_ADM_OPC_SFEAT",
    "XNVME_SPEC_CSI_KV",
    "XNVME_SPEC_CSI_NVM",
    "XNVME_SPEC_CSI_ZONED",
    "XNVME_SPEC_DIR_IDENTIFY",
    "XNVME_SPEC_DIR_STREAMS",
    "XNVME_SPEC_DRECV_IDFY_RETPR",
    "XNVME_SPEC_DRECV_STREAMS_ALLRS",
    "XNVME_SPEC_DRECV_STREAMS_GETST",
    "XNVME_SPEC_DRECV_STREAMS_RETPR",
    "XNVME_SPEC_DSEND_IDFY_ENDIR",
    "XNVME_SPEC_DSEND_STREAMS_RELID",
    "XNVME_SPEC_DSEND_STREAMS_RELRS",
    "XNVME_SPEC_FEAT_ARBITRATION",
    "XNVME_SPEC_FEAT_ERROR_RECOVERY",
    "XNVME_SPEC_FEAT_FDP_EVENTS",
    "XNVME_SPEC_FEAT_FDP_MODE",
    "XNVME_SPEC_FEAT_LBA_RANGETYPE",
    "XNVME_SPEC_FEAT_NQUEUES",
    "XNVME_SPEC_FEAT_PWR_MGMT",
    "XNVME_SPEC_FEAT_SEL_CURRENT",
    "XNVME_SPEC_FEAT_SEL_DEFAULT",
    "XNVME_SPEC_FEAT_SEL_SAVED",
    "XNVME_SPEC_FEAT_SEL_SUPPORTED",
    "XNVME_SPEC_FEAT_TEMP_THRESHOLD",
    "XNVME_SPEC_FEAT_VWCACHE",
    "XNVME_SPEC_FLAG_FORCE_UNIT_ACCESS",
    "XNVME_SPEC_FLAG_LIMITED_RETRY",
    "XNVME_SPEC_FLAG_PRINFO_PRACT",
    "XNVME_SPEC_FLAG_PRINFO_PRCHK_APP",
    "XNVME_SPEC_FLAG_PRINFO_PRCHK_GUARD",
    "XNVME_SPEC_FLAG_PRINFO_PRCHK_REF",
    "XNVME_SPEC_FS_OPC_FLUSH",
    "XNVME_SPEC_FS_OPC_READ",
    "XNVME_SPEC_FS_OPC_WRITE",
    "XNVME_SPEC_IDFY_CTRLR",
    "XNVME_SPEC_IDFY_CTRLR_IOCS",
    "XNVME_SPEC_IDFY_CTRLR_NS",
    "XNVME_SPEC_IDFY_CTRLR_PRI",
    "XNVME_SPEC_IDFY_CTRLR_SEC",
    "XNVME_SPEC_IDFY_CTRLR_SUB",
    "XNVME_SPEC_IDFY_IOCS",
    "XNVME_SPEC_IDFY_NS",
    "XNVME_SPEC_IDFY_NSDSCR",
    "XNVME_SPEC_IDFY_NSGRAN",
    "XNVME_SPEC_IDFY_NSLIST",
    "XNVME_SPEC_IDFY_NSLIST_ALLOC",
    "XNVME_SPEC_IDFY_NSLIST_ALLOC_IOCS",
    "XNVME_SPEC_IDFY_NSLIST_IOCS",
    "XNVME_SPEC_IDFY_NS_ALLOC",
    "XNVME_SPEC_IDFY_NS_ALLOC_IOCS",
    "XNVME_SPEC_IDFY_NS_IOCS",
    "XNVME_SPEC_IDFY_SETL",
    "XNVME_SPEC_IDFY_UUIDL",
    "XNVME_SPEC_IO_MGMT_RECV_RUHS",
    "XNVME_SPEC_IO_MGMT_SEND_RUHU",
    "XNVME_SPEC_KV_OPC_DELETE",
    "XNVME_SPEC_KV_OPC_EXIST",
    "XNVME_SPEC_KV_OPC_LIST",
    "XNVME_SPEC_KV_OPC_RETRIEVE",
    "XNVME_SPEC_KV_OPC_STORE",
    "XNVME_SPEC_KV_SC_CAPACITY_EXCEEDED",
    "XNVME_SPEC_KV_SC_FORMAT_IN_PROGRESS",
    "XNVME_SPEC_KV_SC_INVALID_KEY_SIZE",
    "XNVME_SPEC_KV_SC_INVALID_VAL_SIZE",
    "XNVME_SPEC_KV_SC_KEY_EXISTS",
    "XNVME_SPEC_KV_SC_KEY_NOT_EXISTS",
    "XNVME_SPEC_KV_SC_NS_NOT_READY",
    "XNVME_SPEC_KV_SC_RESERVATION_CONFLICT",
    "XNVME_SPEC_KV_SC_UNRECOVERED_ERR",
    "XNVME_SPEC_LOG_CHNS",
    "XNVME_SPEC_LOG_CSAE",
    "XNVME_SPEC_LOG_ERRI",
    "XNVME_SPEC_LOG_FDPCONF",
    "XNVME_SPEC_LOG_FDPEVENTS",
    "XNVME_SPEC_LOG_FDPRUHU",
    "XNVME_SPEC_LOG_FDPSTATS",
    "XNVME_SPEC_LOG_FW",
    "XNVME_SPEC_LOG_HEALTH",
    "XNVME_SPEC_LOG_RSVD",
    "XNVME_SPEC_LOG_SELFTEST",
    "XNVME_SPEC_LOG_TELECTRLR",
    "XNVME_SPEC_LOG_TELEHOST",
    "XNVME_SPEC_LOG_ZND_CHANGES",
    "XNVME_SPEC_NVM_CMD_CPL_SC_WRITE_TO_RONLY",
    "XNVME_SPEC_NVM_NS_16B_GUARD",
    "XNVME_SPEC_NVM_NS_32B_GUARD",
    "XNVME_SPEC_NVM_NS_64B_GUARD",
    "XNVME_SPEC_NVM_OPC_COMPARE",
    "XNVME_SPEC_NVM_OPC_DATASET_MANAGEMENT",
    "XNVME_SPEC_NVM_OPC_FLUSH",
    "XNVME_SPEC_NVM_OPC_FMT",
    "XNVME_SPEC_NVM_OPC_IO_MGMT_RECV",
    "XNVME_SPEC_NVM_OPC_IO_MGMT_SEND",
    "XNVME_SPEC_NVM_OPC_READ",
    "XNVME_SPEC_NVM_OPC_SANITIZE",
    "XNVME_SPEC_NVM_OPC_SCOPY",
    "XNVME_SPEC_NVM_OPC_WRITE",
    "XNVME_SPEC_NVM_OPC_WRITE_UNCORRECTABLE",
    "XNVME_SPEC_NVM_OPC_WRITE_ZEROES",
    "XNVME_SPEC_PSDT_PRP",
    "XNVME_SPEC_PSDT_SGL_MPTR_CONTIGUOUS",
    "XNVME_SPEC_PSDT_SGL_MPTR_SGL",
    "XNVME_SPEC_SGL_DESCR_SUBTYPE_ADDRESS",
    "XNVME_SPEC_SGL_DESCR_SUBTYPE_OFFSET",
    "XNVME_SPEC_SGL_DESCR_TYPE_BIT_BUCKET",
    "XNVME_SPEC_SGL_DESCR_TYPE_DATA_BLOCK",
    "XNVME_SPEC_SGL_DESCR_TYPE_KEYED_DATA_BLOCK",
    "XNVME_SPEC_SGL_DESCR_TYPE_LAST_SEGMENT",
    "XNVME_SPEC_SGL_DESCR_TYPE_SEGMENT",
    "XNVME_SPEC_SGL_DESCR_TYPE_VENDOR_SPECIFIC",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_ACTION_REPORT",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_ACTION_REPORT_EXTENDED",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_ALL",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_CLOSED",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_EMPTY",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_EOPEN",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_FULL",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_IOPEN",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_OFFLINE",
    "XNVME_SPEC_ZND_CMD_MGMT_RECV_SF_RONLY",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_CLOSE",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_DESCRIPTOR",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_FINISH",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_FLUSH",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_OFFLINE",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_OPEN",
    "XNVME_SPEC_ZND_CMD_MGMT_SEND_RESET",
    "XNVME_SPEC_ZND_MGMT_OPEN_WITH_ZRWA",
    "XNVME_SPEC_ZND_OPC_APPEND",
    "XNVME_SPEC_ZND_OPC_MGMT_RECV",
    "XNVME_SPEC_ZND_OPC_MGMT_SEND",
    "XNVME_SPEC_ZND_SC_BOUNDARY_ERROR",
    "XNVME_SPEC_ZND_SC_INVALID_FORMAT",
    "XNVME_SPEC_ZND_SC_INVALID_TRANS",
    "XNVME_SPEC_ZND_SC_INVALID_WRITE",
    "XNVME_SPEC_ZND_SC_INVALID_ZONE_OP",
    "XNVME_SPEC_ZND_SC_IS_FULL",
    "XNVME_SPEC_ZND_SC_IS_OFFLINE",
    "XNVME_SPEC_ZND_SC_IS_READONLY",
    "XNVME_SPEC_ZND_SC_NOZRWA",
    "XNVME_SPEC_ZND_SC_TOO_MANY_ACTIVE",
    "XNVME_SPEC_ZND_SC_TOO_MANY_OPEN",
    "XNVME_SPEC_ZND_STATE_CLOSED",
    "XNVME_SPEC_ZND_STATE_EMPTY",
    "XNVME_SPEC_ZND_STATE_EOPEN",
    "XNVME_SPEC_ZND_STATE_FULL",
    "XNVME_SPEC_ZND_STATE_IOPEN",
    "XNVME_SPEC_ZND_STATE_OFFLINE",
    "XNVME_SPEC_ZND_STATE_RONLY",
    "XNVME_SPEC_ZND_TYPE_SEQWR",
    "XNVME_STATUS_CODE_INVALID_FIELD",
    "XNVME_STATUS_CODE_TYPE_CMDSPEC",
    "XNVME_STATUS_CODE_TYPE_GENERIC",
    "XNVME_STATUS_CODE_TYPE_MEDIA",
    "XNVME_STATUS_CODE_TYPE_PATH",
    "XNVME_STATUS_CODE_TYPE_VENDOR",
    "off_t",
    "size_t",
    "struct__IO_FILE",
    "struct__IO_codecvt",
    "struct__IO_marker",
    "struct__IO_wide_data",
    "struct_iovec",
    "xnvme_be_attr",
    "xnvme_be_attr_list",
    "xnvme_cli",
    "xnvme_cli_args",
    "xnvme_cli_enumeration",
    "xnvme_cli_opt_attr",
    "xnvme_cli_sub",
    "xnvme_cli_sub_opt",
    "xnvme_cmd_ctx",
    "xnvme_cmd_ctx_async",
    "xnvme_controller",
    "xnvme_dev",
    "xnvme_geo",
    "xnvme_ident",
    "xnvme_lba_range",
    "xnvme_lba_range_attr",
    "xnvme_namespace",
    "xnvme_opts",
    "xnvme_opts_css",
    "xnvme_pi_ctx",
    "xnvme_pif",
    "xnvme_pif_0_g16",
    "xnvme_pif_0_g64",
    "xnvme_queue",
    "xnvme_spec_alloc_resource",
    "xnvme_spec_alloc_resource_0_bits",
    "xnvme_spec_cmd",
    "xnvme_spec_cmd_common",
    "xnvme_spec_cmd_common_0_lnx_ioctl",
    "xnvme_spec_cmd_common_0_prp",
    "xnvme_spec_cmd_drecv",
    "xnvme_spec_cmd_drecv_0_0",
    "xnvme_spec_cmd_dsend",
    "xnvme_spec_cmd_dsend_0_0",
    "xnvme_spec_cmd_dsm",
    "xnvme_spec_cmd_format",
    "xnvme_spec_cmd_gfeat",
    "xnvme_spec_cmd_gfeat_0_0",
    "xnvme_spec_cmd_idfy",
    "xnvme_spec_cmd_log",
    "xnvme_spec_cmd_nvm",
    "xnvme_spec_cmd_nvm_0_0",
    "xnvme_spec_cmd_sanitize",
    "xnvme_spec_cmd_sfeat",
    "xnvme_spec_cmd_sfeat_0_0",
    "xnvme_spec_cpl",
    "xnvme_spec_cpl_0_0",
    "xnvme_spec_cs_vector",
    "xnvme_spec_cs_vector_0_0",
    "xnvme_spec_ctrlr_bar",
    "xnvme_spec_dsm_range",
    "xnvme_spec_elbaf",
    "xnvme_spec_fdp_conf_desc",
    "xnvme_spec_fdp_conf_desc_0_0",
    "xnvme_spec_fdp_event",
    "xnvme_spec_fdp_event_0_0",
    "xnvme_spec_fdp_event_desc",
    "xnvme_spec_fdp_event_desc_0_0",
    "xnvme_spec_fdp_event_media_reallocated",
    "xnvme_spec_fdp_event_media_reallocated_0_0",
    "xnvme_spec_feat",
    "xnvme_spec_feat_0_error_recovery",
    "xnvme_spec_feat_0_fdp_mode",
    "xnvme_spec_feat_0_nqueues",
    "xnvme_spec_feat_0_temp_threshold",
    "xnvme_spec_fs_idfy_ctrlr",
    "xnvme_spec_fs_idfy_ctrlr_caps",
    "xnvme_spec_fs_idfy_ctrlr_iosizes",
    "xnvme_spec_fs_idfy_ctrlr_limits",
    "xnvme_spec_fs_idfy_ctrlr_properties",
    "xnvme_spec_fs_idfy_ns",
    "xnvme_spec_idfy",
    "xnvme_spec_idfy_cs",
    "xnvme_spec_idfy_ctrlr",
    "xnvme_spec_idfy_ctrlr_0_0",
    "xnvme_spec_idfy_ctrlr_10_0",
    "xnvme_spec_idfy_ctrlr_11_0",
    "xnvme_spec_idfy_ctrlr_12_bits",
    "xnvme_spec_idfy_ctrlr_13_bits",
    "xnvme_spec_idfy_ctrlr_14_bits",
    "xnvme_spec_idfy_ctrlr_15_bits",
    "xnvme_spec_idfy_ctrlr_16_0",
    "xnvme_spec_idfy_ctrlr_17_0",
    "xnvme_spec_idfy_ctrlr_18_0",
    "xnvme_spec_idfy_ctrlr_19_0",
    "xnvme_spec_idfy_ctrlr_1_0",
    "xnvme_spec_idfy_ctrlr_20_0",
    "xnvme_spec_idfy_ctrlr_21_0",
    "xnvme_spec_idfy_ctrlr_22_0",
    "xnvme_spec_idfy_ctrlr_23_ctrattr",
    "xnvme_spec_idfy_ctrlr_23_ofcs",
    "xnvme_spec_idfy_ctrlr_2_0",
    "xnvme_spec_idfy_ctrlr_3_0",
    "xnvme_spec_idfy_ctrlr_4_0",
    "xnvme_spec_idfy_ctrlr_5_0",
    "xnvme_spec_idfy_ctrlr_6_0",
    "xnvme_spec_idfy_ctrlr_7_0",
    "xnvme_spec_idfy_ctrlr_8_0",
    "xnvme_spec_idfy_ctrlr_9_0",
    "xnvme_spec_idfy_ctrlr_nvmf_specific",
    "xnvme_spec_idfy_dir_rp",
    "xnvme_spec_idfy_dir_rp_directives_enabled",
    "xnvme_spec_idfy_dir_rp_directives_persistence",
    "xnvme_spec_idfy_dir_rp_directives_supported",
    "xnvme_spec_idfy_ns",
    "xnvme_spec_idfy_ns_3_0",
    "xnvme_spec_idfy_ns_4_0",
    "xnvme_spec_idfy_ns_6_0",
    "xnvme_spec_idfy_ns_7_0",
    "xnvme_spec_idfy_ns_8_bits",
    "xnvme_spec_idfy_ns_flbas",
    "xnvme_spec_idfy_ns_mc",
    "xnvme_spec_idfy_ns_nmic",
    "xnvme_spec_idfy_ns_nsfeat",
    "xnvme_spec_io_mgmt_cmd",
    "xnvme_spec_io_mgmt_recv_cmd",
    "xnvme_spec_io_mgmt_send_cmd",
    "xnvme_spec_kvs_cmd",
    "xnvme_spec_kvs_cmd_cdw11",
    "xnvme_spec_kvs_idfy",
    "xnvme_spec_kvs_idfy_ns",
    "xnvme_spec_kvs_idfy_ns_format",
    "xnvme_spec_lbaf",
    "xnvme_spec_log_erri_entry",
    "xnvme_spec_log_fdp_conf",
    "xnvme_spec_log_fdp_events",
    "xnvme_spec_log_fdp_stats",
    "xnvme_spec_log_health_entry",
    "xnvme_spec_log_ruhu",
    "xnvme_spec_nvm_cmd",
    "xnvme_spec_nvm_cmd_scopy",
    "xnvme_spec_nvm_cmd_scopy_fmt_srclen",
    "xnvme_spec_nvm_idfy",
    "xnvme_spec_nvm_idfy_ctrlr",
    "xnvme_spec_nvm_idfy_ctrlr_0_0",
    "xnvme_spec_nvm_idfy_ctrlr_1_0",
    "xnvme_spec_nvm_idfy_ns",
    "xnvme_spec_nvm_idfy_ns_iocs",
    "xnvme_spec_nvm_idfy_ns_iocs_0_0",
    "xnvme_spec_nvm_scopy_fmt_zero",
    "xnvme_spec_nvm_scopy_source_range",
    "xnvme_spec_nvm_write_zeroes",
    "xnvme_spec_power_state",
    "xnvme_spec_ruh_desc",
    "xnvme_spec_ruhs",
    "xnvme_spec_ruhs_desc",
    "xnvme_spec_ruhu_desc",
    "xnvme_spec_sgl_descriptor",
    "xnvme_spec_sgl_descriptor_0_generic",
    "xnvme_spec_sgl_descriptor_0_unkeyed",
    "xnvme_spec_status",
    "xnvme_spec_status_0_0",
    "xnvme_spec_streams_dir_gs",
    "xnvme_spec_streams_dir_rp",
    "xnvme_spec_streams_dir_rp_0_bits",
    "xnvme_spec_vs_register_bits",
    "xnvme_spec_znd_cmd",
    "xnvme_spec_znd_cmd_append",
    "xnvme_spec_znd_cmd_mgmt_recv",
    "xnvme_spec_znd_cmd_mgmt_send",
    "xnvme_spec_znd_descr",
    "xnvme_spec_znd_descr_0_0",
    "xnvme_spec_znd_idfy",
    "xnvme_spec_znd_idfy_ctrlr",
    "xnvme_spec_znd_idfy_lbafe",
    "xnvme_spec_znd_idfy_ns",
    "xnvme_spec_znd_idfy_ns_0_bits",
    "xnvme_spec_znd_idfy_ns_1_bits",
    "xnvme_spec_znd_idfy_ns_2_bits",
    "xnvme_spec_znd_log_changes",
    "xnvme_spec_znd_report_hdr",
    "xnvme_subsystem",
    "xnvme_timer",
    "xnvme_znd_report",
    "uint16_t",
    "uint32_t",
    "uint64_t",
    "uint8_t",
    "xnvme_pif_0",
    "xnvme_spec_alloc_resource_0",
    "xnvme_spec_cmd_0",
    "xnvme_spec_cmd_common_dptr",
    "xnvme_spec_cmd_drecv_cdw12",
    "xnvme_spec_cmd_dsend_cdw12",
    "xnvme_spec_cmd_gfeat_cdw10",
    "xnvme_spec_cmd_nvm_cdw13",
    "xnvme_spec_cmd_sfeat_cdw10",
    "xnvme_spec_cpl_0",
    "xnvme_spec_cs_vector_0",
    "xnvme_spec_fdp_conf_desc_fdpa",
    "xnvme_spec_fdp_event_desc_fdpeta",
    "xnvme_spec_fdp_event_fdpef",
    "xnvme_spec_fdp_event_media_reallocated_sef",
    "xnvme_spec_feat_0",
    "xnvme_spec_idfy_0",
    "xnvme_spec_idfy_ctrlr_anacap",
    "xnvme_spec_idfy_ctrlr_apsta",
    "xnvme_spec_idfy_ctrlr_avscc",
    "xnvme_spec_idfy_ctrlr_cdfs",
    "xnvme_spec_idfy_ctrlr_cmic",
    "xnvme_spec_idfy_ctrlr_cqes",
    "xnvme_spec_idfy_ctrlr_ctratt",
    "xnvme_spec_idfy_ctrlr_dsto",
    "xnvme_spec_idfy_ctrlr_fna",
    "xnvme_spec_idfy_ctrlr_frmw",
    "xnvme_spec_idfy_ctrlr_hctma",
    "xnvme_spec_idfy_ctrlr_lpa",
    "xnvme_spec_idfy_ctrlr_mec",
    "xnvme_spec_idfy_ctrlr_nvmsr",
    "xnvme_spec_idfy_ctrlr_oacs",
    "xnvme_spec_idfy_ctrlr_oaes",
    "xnvme_spec_idfy_ctrlr_oncs",
    "xnvme_spec_idfy_ctrlr_rpmbs",
    "xnvme_spec_idfy_ctrlr_sanicap",
    "xnvme_spec_idfy_ctrlr_sgls",
    "xnvme_spec_idfy_ctrlr_sqes",
    "xnvme_spec_idfy_ctrlr_vwc",
    "xnvme_spec_idfy_ctrlr_vwci",
    "xnvme_spec_idfy_ns_dlfeat",
    "xnvme_spec_idfy_ns_dpc",
    "xnvme_spec_idfy_ns_dps",
    "xnvme_spec_idfy_ns_fpi",
    "xnvme_spec_idfy_ns_nsrescap",
    "xnvme_spec_io_mgmt_cmd_0",
    "xnvme_spec_kvs_idfy_0",
    "xnvme_spec_nvm_cmd_0",
    "xnvme_spec_nvm_idfy_0",
    "xnvme_spec_nvm_idfy_ctrlr_ocfs",
    "xnvme_spec_nvm_idfy_ctrlr_oncs",
    "xnvme_spec_nvm_idfy_ns_iocs_pic",
    "xnvme_spec_sgl_descriptor_0",
    "xnvme_spec_status_0",
    "xnvme_spec_streams_dir_rp_nssc",
    "xnvme_spec_vs_register",
    "xnvme_spec_znd_cmd_0",
    "xnvme_spec_znd_descr_za",
    "xnvme_spec_znd_idfy_0",
    "xnvme_spec_znd_idfy_ns_ozcs",
    "xnvme_spec_znd_idfy_ns_zoc",
    "xnvme_spec_znd_idfy_ns_zrwacap",
    "xnvme_adm_dir_recv",
    "xnvme_adm_dir_send",
    "xnvme_adm_format",
    "xnvme_adm_gfeat",
    "xnvme_adm_idfy",
    "xnvme_adm_idfy_ctrlr",
    "xnvme_adm_idfy_ctrlr_csi",
    "xnvme_adm_idfy_ns",
    "xnvme_adm_idfy_ns_csi",
    "xnvme_adm_log",
    "xnvme_adm_sfeat",
    "xnvme_be_attr_fpr",
    "xnvme_be_attr_list_bundled",
    "xnvme_be_attr_list_fpr",
    "xnvme_be_attr_list_pr",
    "xnvme_be_attr_pr",
    "xnvme_buf_alloc",
    "xnvme_buf_clear",
    "xnvme_buf_diff",
    "xnvme_buf_diff_pr",
    "xnvme_buf_fill",
    "xnvme_buf_free",
    "xnvme_buf_from_file",
    "xnvme_buf_phys_alloc",
    "xnvme_buf_phys_free",
    "xnvme_buf_phys_realloc",
    "xnvme_buf_realloc",
    "xnvme_buf_to_file",
    "xnvme_buf_virt_alloc",
    "xnvme_buf_virt_free",
    "xnvme_buf_vtophys",
    "xnvme_cli_args_pr",
    "xnvme_cli_enumeration_alloc",
    "xnvme_cli_enumeration_append",
    "xnvme_cli_enumeration_fpp",
    "xnvme_cli_enumeration_fpr",
    "xnvme_cli_enumeration_free",
    "xnvme_cli_enumeration_pp",
    "xnvme_cli_enumeration_pr",
    "xnvme_cli_get_opt_attr",
    "xnvme_cli_opt",
    "xnvme_cli_opt_type",
    "xnvme_cli_opt_value_type",
    "xnvme_cli_opts",
    "xnvme_cli_perr",
    "xnvme_cli_pinf",
    "xnvme_cli_run",
    "xnvme_cli_subfunc",
    "xnvme_cli_timer_bw_pr",
    "xnvme_cli_timer_start",
    "xnvme_cli_timer_stop",
    "xnvme_cli_to_opts",
    "xnvme_cmd_ctx_clear",
    "xnvme_cmd_ctx_from_queue",
    "xnvme_cmd_ctx_pr",
    "xnvme_cmd_pass_iov",
    "xnvme_cmd_passv",
    "xnvme_controller_get_registers",
    "xnvme_controller_reset",
    "xnvme_dev_close",
    "xnvme_dev_derive_geo",
    "xnvme_dev_fpr",
    "xnvme_dev_get_be_state",
    "xnvme_dev_get_csi",
    "xnvme_dev_get_ctrlr",
    "xnvme_dev_get_ctrlr_css",
    "xnvme_dev_get_geo",
    "xnvme_dev_get_ident",
    "xnvme_dev_get_ns",
    "xnvme_dev_get_ns_css",
    "xnvme_dev_get_nsid",
    "xnvme_dev_get_opts",
    "xnvme_dev_get_ssw",
    "xnvme_dev_open",
    "xnvme_dev_pr",
    "xnvme_enumerate",
    "xnvme_enumerate_action",
    "xnvme_enumerate_cb",
    "xnvme_file_close",
    "xnvme_file_get_cmd_ctx",
    "xnvme_file_open",
    "xnvme_file_pread",
    "xnvme_file_pwrite",
    "xnvme_file_sync",
    "xnvme_geo_fpr",
    "xnvme_geo_pr",
    "xnvme_geo_type",
    "xnvme_ident_fpr",
    "xnvme_ident_from_uri",
    "xnvme_ident_pr",
    "xnvme_ident_yaml",
    "xnvme_kvs_delete",
    "xnvme_kvs_exist",
    "xnvme_kvs_list",
    "xnvme_kvs_retrieve",
    "xnvme_kvs_store",
    "xnvme_lba_fpr",
    "xnvme_lba_fprn",
    "xnvme_lba_pr",
    "xnvme_lba_prn",
    "xnvme_lba_range_fpr",
    "xnvme_lba_range_from_offset_nbytes",
    "xnvme_lba_range_from_slba_elba",
    "xnvme_lba_range_from_slba_naddrs",
    "xnvme_lba_range_from_zdescr",
    "xnvme_lba_range_pr",
    "xnvme_libconf",
    "xnvme_libconf_fpr",
    "xnvme_libconf_pr",
    "xnvme_mem_map",
    "xnvme_mem_unmap",
    "xnvme_namespace_rescan",
    "xnvme_nvm_dsm",
    "xnvme_nvm_mgmt_recv",
    "xnvme_nvm_mgmt_send",
    "xnvme_nvm_read",
    "xnvme_nvm_sanitize",
    "xnvme_nvm_scopy",
    "xnvme_nvm_scopy_fmt",
    "xnvme_nvm_write",
    "xnvme_nvm_write_uncorrectable",
    "xnvme_nvm_write_zeroes",
    "xnvme_nvme_sgl_descriptor_type",
    "xnvme_opts_default",
    "xnvme_opts_pr",
    "xnvme_opts_set_defaults",
    "xnvme_pi_check_type",
    "xnvme_pi_ctx_init",
    "xnvme_pi_generate",
    "xnvme_pi_size",
    "xnvme_pi_type",
    "xnvme_pi_verify",
    "xnvme_pr",
    "xnvme_prep_adm_gfeat",
    "xnvme_prep_adm_log",
    "xnvme_prep_adm_sfeat",
    "xnvme_prep_nvm",
    "xnvme_queue_cb",
    "xnvme_queue_drain",
    "xnvme_queue_get_capacity",
    "xnvme_queue_get_cmd_ctx",
    "xnvme_queue_get_completion_fd",
    "xnvme_queue_get_outstanding",
    "xnvme_queue_init",
    "xnvme_queue_opts",
    "xnvme_queue_poke",
    "xnvme_queue_put_cmd_ctx",
    "xnvme_queue_set_cb",
    "xnvme_queue_term",
    "xnvme_queue_wait",
    "xnvme_retreive_opts",
    "xnvme_spec_adm_opc",
    "xnvme_spec_adm_opc_str",
    "xnvme_spec_cmd_fpr",
    "xnvme_spec_cmd_pr",
    "xnvme_spec_csi",
    "xnvme_spec_csi_str",
    "xnvme_spec_ctrlr_bar_fpr",
    "xnvme_spec_ctrlr_bar_pp",
    "xnvme_spec_dir_types",
    "xnvme_spec_drecv_idfy_doper",
    "xnvme_spec_drecv_idfy_pr",
    "xnvme_spec_drecv_sar_pr",
    "xnvme_spec_drecv_sgs_pr",
    "xnvme_spec_drecv_srp_pr",
    "xnvme_spec_drecv_streams_doper",
    "xnvme_spec_dsend_idfy_doper",
    "xnvme_spec_dsend_streams_doper",
    "xnvme_spec_feat_fdp_events_pr",
    "xnvme_spec_feat_fpr",
    "xnvme_spec_feat_id",
    "xnvme_spec_feat_id_str",
    "xnvme_spec_feat_pr",
    "xnvme_spec_feat_sel",
    "xnvme_spec_feat_sel_str",
    "xnvme_spec_flag",
    "xnvme_spec_flag_str",
    "xnvme_spec_fs_opcs",
    "xnvme_spec_idfy_cns",
    "xnvme_spec_idfy_cns_str",
    "xnvme_spec_idfy_cs_fpr",
    "xnvme_spec_idfy_cs_pr",
    "xnvme_spec_idfy_ctrl_fpr",
    "xnvme_spec_idfy_ctrl_pr",
    "xnvme_spec_idfy_ctrlr_fpr",
    "xnvme_spec_idfy_ns_fpr",
    "xnvme_spec_idfy_ns_pr",
    "xnvme_spec_io_mgmt_recv_mo",
    "xnvme_spec_io_mgmt_send_mo",
    "xnvme_spec_kv_opc",
    "xnvme_spec_kv_status_code",
    "xnvme_spec_kvs_idfy_ns_fpr",
    "xnvme_spec_kvs_idfy_ns_pr",
    "xnvme_spec_log_erri_fpr",
    "xnvme_spec_log_erri_pr",
    "xnvme_spec_log_fdp_conf_pr",
    "xnvme_spec_log_fdp_events_pr",
    "xnvme_spec_log_fdp_stats_pr",
    "xnvme_spec_log_health_fpr",
    "xnvme_spec_log_health_pr",
    "xnvme_spec_log_lpi",
    "xnvme_spec_log_lpi_str",
    "xnvme_spec_log_ruhu_pr",
    "xnvme_spec_nvm_cmd_cpl_sc",
    "xnvme_spec_nvm_cmd_cpl_sc_str",
    "xnvme_spec_nvm_idfy_ctrlr_pr",
    "xnvme_spec_nvm_idfy_ns_fpr",
    "xnvme_spec_nvm_idfy_ns_pr",
    "xnvme_spec_nvm_ns_pif",
    "xnvme_spec_nvm_opc",
    "xnvme_spec_nvm_opc_str",
    "xnvme_spec_nvm_scopy_fmt_zero_fpr",
    "xnvme_spec_nvm_scopy_fmt_zero_pr",
    "xnvme_spec_nvm_scopy_source_range_fpr",
    "xnvme_spec_nvm_scopy_source_range_pr",
    "xnvme_spec_psdt",
    "xnvme_spec_psdt_str",
    "xnvme_spec_ruhs_pr",
    "xnvme_spec_sgl_descriptor_subtype",
    "xnvme_spec_sgl_descriptor_subtype_str",
    "xnvme_spec_status_code",
    "xnvme_spec_status_code_type",
    "xnvme_spec_znd_cmd_mgmt_recv_action",
    "xnvme_spec_znd_cmd_mgmt_recv_action_sf",
    "xnvme_spec_znd_cmd_mgmt_recv_action_sf_str",
    "xnvme_spec_znd_cmd_mgmt_recv_action_str",
    "xnvme_spec_znd_cmd_mgmt_send_action",
    "xnvme_spec_znd_cmd_mgmt_send_action_str",
    "xnvme_spec_znd_descr_fpr",
    "xnvme_spec_znd_descr_fpr_yaml",
    "xnvme_spec_znd_descr_pr",
    "xnvme_spec_znd_idfy_ctrlr_fpr",
    "xnvme_spec_znd_idfy_ctrlr_pr",
    "xnvme_spec_znd_idfy_lbafe_fpr",
    "xnvme_spec_znd_idfy_ns_fpr",
    "xnvme_spec_znd_idfy_ns_pr",
    "xnvme_spec_znd_log_changes_fpr",
    "xnvme_spec_znd_log_changes_pr",
    "xnvme_spec_znd_log_lid",
    "xnvme_spec_znd_log_lid_str",
    "xnvme_spec_znd_mgmt_send_action_so",
    "xnvme_spec_znd_mgmt_send_action_so_str",
    "xnvme_spec_znd_opc",
    "xnvme_spec_znd_opc_str",
    "xnvme_spec_znd_report_hdr_fpr",
    "xnvme_spec_znd_report_hdr_pr",
    "xnvme_spec_znd_state",
    "xnvme_spec_znd_state_str",
    "xnvme_spec_znd_status_code",
    "xnvme_spec_znd_status_code_str",
    "xnvme_spec_znd_type",
    "xnvme_spec_znd_type_str",
    "xnvme_store_opts",
    "xnvme_subsystem_reset",
    "xnvme_ver_fpr",
    "xnvme_ver_major",
    "xnvme_ver_minor",
    "xnvme_ver_patch",
    "xnvme_ver_pr",
    "xnvme_znd_append",
    "xnvme_znd_descr_from_dev",
    "xnvme_znd_descr_from_dev_in_state",
    "xnvme_znd_dev_get_ctrlr",
    "xnvme_znd_dev_get_lbafe",
    "xnvme_znd_dev_get_ns",
    "xnvme_znd_log_changes_from_dev",
    "xnvme_znd_mgmt_recv",
    "xnvme_znd_mgmt_send",
    "xnvme_znd_report_find_arbitrary",
    "xnvme_znd_report_fpr",
    "xnvme_znd_report_from_dev",
    "xnvme_znd_report_pr",
    "xnvme_znd_stat",
    "xnvme_znd_zrwa_flush",
]


def guard_unloadable():
    """Print error and do sys.exit(1) when library is not loadable"""

    if is_loaded:
        return

    print(
        "FAILED: library is not loadable; perhaps set XNVME_LIBRARY_PATH to point to the library?"
    )
    sys.exit(1)
