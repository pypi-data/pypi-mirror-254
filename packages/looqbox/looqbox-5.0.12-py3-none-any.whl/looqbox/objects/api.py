from looqbox.class_loader.lazy_load import LazyLoad
from looqbox.objects.component_utility.css_option import CssOption

import typing

if typing.TYPE_CHECKING:
    
    from looqbox.objects.visual.looq_message import ObjMessage
    from looqbox.objects.visual.looq_image import ObjImage
    from looqbox.objects.media.looq_video import ObjVideo
    from looqbox.objects.visual.looq_list import ObjList
    from looqbox.objects.looq_html import ObjHTML
    from looqbox.objects.looq_pdf import ObjPDF
    from looqbox.objects.visual.looq_web_frame import ObjWebFrame
    from looqbox.objects.visual.looq_table import ObjTable
    from looqbox.objects.plotly.looq_plotly import ObjPlotly
    from looqbox.objects.looq_form import ObjForm
    from looqbox.objects.looq_image_capture import ObjImageCapture
    from looqbox.objects.looq_embed import ObjEmbed
    from looqbox.objects.visual.looq_text import ObjText
    from looqbox.objects.looq_simple import ObjSimple
    from looqbox.objects.looq_form_html import ObjFormHTML
    from looqbox.objects.container.positional.looq_row import ObjRow
    from looqbox.objects.container.positional.looq_column import ObjColumn
    from looqbox.objects.container.looq_switch import ObjSwitch
    from looqbox.objects.visual.looq_query import ObjQuery
    from looqbox.objects.container.looq_tooltip import ObjTooltip
    from looqbox.objects.container.looq_link import ObjLink
    from looqbox.objects.visual.looq_gauge import ObjGauge
    from looqbox.objects.visual.shape.looq_line import ObjLine
    from looqbox.objects.looq_file_upload import ObjFileUpload
    from looqbox.objects.media.looq_audio import ObjAudio

else:

    @LazyLoad
    class ObjMessage: ...

    @LazyLoad
    class ObjImage: ...

    @LazyLoad
    class ObjVideo: ...

    @LazyLoad
    class ObjList: ...

    @LazyLoad
    class ObjHTML: ...

    @LazyLoad
    class ObjPDF: ...

    @LazyLoad
    class ObjWebFrame: ...

    @LazyLoad
    class ObjTable: ...

    @LazyLoad
    class ObjPlotly: ...

    @LazyLoad
    class ObjForm: ...

    @LazyLoad
    class ObjImageCapture: ...

    @LazyLoad
    class ObjEmbed: ...

    @LazyLoad
    class ObjText: ...

    @LazyLoad
    class ObjSimple: ...

    @LazyLoad
    class ObjFormHTML: ...

    @LazyLoad
    class ObjRow: ...

    @LazyLoad
    class ObjColumn: ...

    @LazyLoad
    class ObjSwitch: ...

    @LazyLoad
    class ObjQuery: ...

    @LazyLoad
    class ObjTooltip: ...

    @LazyLoad
    class ObjLink: ...

    @LazyLoad
    class ObjGauge: ...

    @LazyLoad
    class ObjLine: ...

    @LazyLoad
    class ObjFileUpload: ...

    @LazyLoad
    class ObjAudio: ...

__all__ = ["ObjTable", "ObjWebFrame", "ObjPlotly", "ObjPDF", "ObjList", "ObjHTML", "ObjImage",
           "ObjMessage", "ObjVideo", "ObjForm", "ObjFileUpload", "ObjImageCapture", "ObjEmbed",
           "ObjAudio", "ObjSimple", "ObjFormHTML", "ObjQuery", "ObjRow", "ObjColumn", "ObjSwitch",
           "ObjTooltip", "ObjLink", "ObjText", "ObjGauge", "ObjLine", "CssOption"]
